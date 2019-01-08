#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - views.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

import string
import re
import bleach

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Realm, Page
from blog.models import Post
from .forms import newRealmForm, RealmEditForm, PageEditForm
from blog.forms import PostEditForm, CommentForm
from .decorators import user_is_author, user_is_creator

from markdownx.utils import markdownify

#Globals

tech_levels = ['Stone Age', 'Bronze Age', 'Iron Age', 'Medieval', 'Colonial Age', 'Industrial Age', 'Steam Age', 'Nuclear Age', 'Digital Age', 'Microtech Age' ]

magic_levels = ['Historical', 'Folkloric', 'Miraculous', 'Low magic', 'Heroic', 'Mythical', 'Paranormal', 'Enchanted', 'High magic', 'Very High magic', ]

def slugify(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    out = regex.sub('', text).lower()
    out = out.replace(" ", "_").lower()
    out = out.replace("-", "_")
    out = out.replace("__", "_")
    return out

"""
Realm Views
"""

def realm_new(request):
    if request.method == "POST":
        new_realm = newRealmForm(request.POST)
        new_player = UserCreationForm(request.POST)
        if new_realm.is_valid():
            realm = new_realm.save(commit=False)
            if request.user.is_authenticated:
                #realm.name is unique?
                realm.author = request.user
                realm.created_date = timezone.now()
                realm.realm_slug = slugify(realm.name)
                realm.wallpaper = 'uploads/dungeondisorder.jpg'
                realm.save()
                return redirect('realm_view', realm_slug=realm.realm_slug)
            else: 
                return redirect('accounts/login/?next=/')
        else:
            new_realm = newRealmForm()
        
        if new_player.is_valid():
            #create new user
            player = new_player.save()
            return redirect('realm_list')
        else:
            new_player = UserCreationForm()
    else:
        new_realm = newRealmForm()
        new_player = UserCreationForm()
    
    realms = Realm.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'index.html', {'new_realm': new_realm, 'new_player': new_player, 'realms': realms})

def realm_view(request, realm_slug):
    realm = get_object_or_404(Realm, realm_slug=realm_slug)
    realm.description = markdownify(realm.description)
    new_post = PostEditForm()
    new_comment = CommentForm()
    warning = ""
    
    if request.method == "POST":
        new_post = PostEditForm(request.POST)
        if new_post.is_valid() and request.user.is_authenticated:
            mode = request.POST.get('mode', None)
            if mode == 'new':
                post = new_post.save(commit=False)
                post.author = request.user
                post.created_date = timezone.now()
                post.published_date = timezone.now()
                post.realm_slug = request.POST.get('realm_slug', None)
                post.ancestor = request.POST.get('ancestor', None)
                post.parent = request.POST.get('parent', 0)
                post.save()
                warning = "Posted new comment"
            elif mode == 'edit':
                post = get_object_or_404(Post, pk=request.POST.get('pk', None))
                if request.user == post.author:
                    post.text = request.POST.get('text', None)
                    post.published_date = timezone.now()
                    post.save()
                    warning = "Edited comment"
                else:
                    warning = "You don't have permission to edit that comment"
            elif mode == 'delete':
                post = get_object_or_404(Post, pk=request.POST.get('pk', None))
                if request.user == post.author:
                    post.delete()
                    warning = "Deleted comment"
                else:
                    warning = "You don't have permission to delete that comment"
            else:
                warning = 'Can\'t perform that action.'
        else:
            warning = 'You must be logged in to comment.'
    
    new_post = PostEditForm()
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    posts = Post.objects.filter(realm_slug=realm.realm_slug).filter(parent=0).order_by('-created_date')
    for post in posts:
        post.children = Post.objects.filter(parent=post.pk)
    return render(request, 'realm_view.html', {
        'realm': realm,
        'pages': pages,
        'posts': posts,
        'new_post': new_post,
        'new_comment': new_comment,
        'tech_desc': tech_levels[realm.tech_level - 1],
        'magic_desc': magic_levels[realm.magic_level - 1],
        'warning': warning
    })

@user_is_creator
def realm_edit(request, realm_slug):
    realm = get_object_or_404(Realm, realm_slug=realm_slug)
    if request.method == "POST":
        form = RealmEditForm(request.POST, request.FILES, instance=realm)
        if form.is_valid():
            realm = form.save(commit=False)
            realm.author = request.user
            realm.realm_slug = slugify(realm.realm_slug)
            realm.rule_set = bleach.clean(realm.rule_set)
            realm.genre = bleach.clean(realm.genre)
            realm.save()
            return redirect('realm_view', realm_slug=realm.realm_slug)
    else:
        form = RealmEditForm(instance=realm)
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'realm_edit.html', {'form': form, 'pages':pages, 'realm':realm})

@user_is_creator
def realm_delete(request, *args, **kwargs):
    realm = get_object_or_404(Realm, realm_slug=kwargs['realm_slug'])

    if request.method == "POST":
        # Delete the realm
        r_del = realm.delete()
    
        #Return to Maginaria index
        new_realm = newRealmForm()
        new_player = UserCreationForm()
        realms = Realm.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return redirect('/')

    # Show Confirmation dialog
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'realm_delete.html', {'realm':realm, 'pages':pages})


"""
Page Views
"""

@user_is_creator
def page_new(request, realm_slug):
    realm = get_object_or_404(Realm, realm_slug=realm_slug)
    if request.method == "POST":
        new_page = PageEditForm(request.POST)
        if new_page.is_valid():
            page = new_page.save(commit=False)
            if request.user.is_authenticated:
                #page.title is unique?
                page.author = request.user
                page.created_date = timezone.now()
                page.page_slug = slugify(page.title)
                page.realm_slug = realm.realm_slug
                page.save()
                return redirect('page_view', realm_slug=realm.realm_slug, page_slug=page.page_slug)
            else: 
                return redirect('accounts/login/?next=/')
        else:
            form = PageEditForm()
    else:
        form = PageEditForm()
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'page_edit.html', {'form': form, 'pages':pages, 'realm':realm})

def page_view(request, realm_slug, page_slug):
    page = get_object_or_404(Page, page_slug=page_slug)
    realm = get_object_or_404(Realm, realm_slug=realm_slug)
    page.description = markdownify(page.description)
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'page_view.html', { 'page': page, 'pages': pages, 'realm': realm })

@user_is_author
def page_edit(request, realm_slug, page_slug):
    realm = get_object_or_404(Realm, realm_slug=realm_slug)
    page = get_object_or_404(Page, page_slug=page_slug)
    if request.method == "POST":
        form = PageEditForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.realm_slug = realm.realm_slug
            page.page_slug = slugify(page.page_slug)
            page.save()
            return redirect('page_view', realm_slug=page.realm_slug, page_slug=page.page_slug)
    else:
        form = PageEditForm(instance=page)
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'page_edit.html', {'form': form, 'pages':pages, 'page':page, 'realm':realm})
  
@user_is_author
def page_delete(request, *args, **kwargs):
    realm = get_object_or_404(Realm, realm_slug=kwargs['realm_slug'])
    page = get_object_or_404(Page, page_slug=kwargs['page_slug'])
    
    if request.method == "POST":
        # Delete the page
        r_del = page.delete()
    
        # Return to Realm homepage
        return redirect('realm_view', realm_slug=realm.realm_slug)      

    # Show Confirmation dialog
    pages = Page.objects.filter(realm_slug=realm.realm_slug).order_by('title')
    return render(request, 'page_delete.html', {'realm':realm, 'page':page, 'pages':pages})
    

"""
Error Pages
"""

def handler403(request):
    return render(request, '403.html', status=403)

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
