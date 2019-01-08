from django.core.exceptions import PermissionDenied
from .models import Realm, Page

def user_is_author(function):
    def wrap(request, *args, **kwargs):
        page = Page.objects.get(page_slug=kwargs['page_slug'])
        if page.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_creator(function):
    def wrap(request, *args, **kwargs):
        realm = Realm.objects.get(realm_slug=kwargs['realm_slug'])
        if realm.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
