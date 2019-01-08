#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - tests.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

from django.contrib.auth.models import User
from django.test import TestCase

class RealmsViewsTest(TestCase):
    
    fixtures = ['realms_views_testdata.json']
    
    def test_realm_new(self):
        resp = self.client.get('/')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('realms' in resp.context)
        self.assertEqual([realm.name for realm in resp.context['realms']], ['My Cool Realm', 'Imaginary', 'Markdown Example', 'Grail Test'])
    
    def test_realm_view(self):
        resp = self.client.get('/imaginary/')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
        
    def test_bad_realm_view(self):
        resp = self.client.get('/non_existant/')
        # Should Fail [404]
        self.assertEqual(resp.status_code, 404)
    
    def test_realm_edit(self):
        resp = self.client.get('/imaginary/edit/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
    
    def test_page_view(self):
        resp = self.client.get('/grailtest/installing/')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
    
    def test_page_edit(self):
        resp = self.client.get('/grailtest/installing/edit/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
    
    def test_page_delete(self):
        # GET confirmation dialog
        resp = self.client.get('/grailtest/installing/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST no data
        resp = self.client.post('/grailtest/installing/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST confirmation
        # test that page is still present [Success]
        resp = self.client.get('/grailtest/installing/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
    
    def test_realm_delete(self):
        # GET confirmation dialog
        resp = self.client.get('/grailtest/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST no data
        resp = self.client.post('/grailtest/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST confirmation
        # test that realm is no longer present [Success]
        resp = self.client.get('/grailtest/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
    

class RealmsViewsLoggedInNoPrivsTest(TestCase):
    
    fixtures = ['realms_views_testdata.json']
    
    def setUp(self):
        self.noprivs_cred = {
            'username': 'testuser',
            'password': 'noprivs'
        }
        User.objects.create_user(**self.noprivs_cred)
    
    def test_login(self):
        # Login noprivs user
        r1 = self.client.post('/accounts/login/?next=/', self.noprivs_cred, follow=True)
        
        self.assertTrue(r1.context['user'].is_active)
        self.assertTrue(r1.context['user'].is_authenticated)
        self.assertEqual(r1.context['user'].username, 'testuser')
    
    def test_new_realm(self):
        # Login noprivs user
        r1 = self.client.post('/accounts/login/?next=/', self.noprivs_cred, follow=True)
        
        resp = self.client.post('/', {'name': 'My +awesome% ^new* realm'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp['Location'], 'http://testserver/my_awesome_new_realm/')
    
    def test_page_new_noprivs(self):
        # Login noprivs user
        r1 = self.client.post('/accounts/login/?next=/', self.noprivs_cred, follow=True)
        
        # Only owner of realm should be able to create pages
        # X: 403 Forbidden
        resp = self.client.get('/imaginary/new_page/')
        self.assertEqual(resp.status_code, 403)
        
        # This should fail
        # X: 403 Forbidden
        resp = self.client.post('/imaginary/new_page/', {'title': 'My +awesome% ^new* page'})
        self.assertEqual(resp.status_code, 403)
    
    def test_page_delete_logged_in_noprivs(self):
        # Login noprivs user
        r1 = self.client.post('/accounts/login/?next=/', self.noprivs_cred, follow=True)
        
        # GET confirmation dialog
        resp = self.client.get('/grailtest/installing/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST no data
        resp = self.client.post('/grailtest/installing/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST confirmation
        # test that page is still present [Success]
        resp = self.client.get('/grailtest/installing/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
    
    def test_realm_delete_logged_in_noprivs(self):
        # Login noprivs user
        r1 = self.client.post('/accounts/login/?next=/', self.noprivs_cred, follow=True)
        
        # GET confirmation dialog
        resp = self.client.get('/grailtest/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST no data
        resp = self.client.post('/grailtest/del/')
        # X:FAIL 403 Forbidden
        self.assertEqual(resp.status_code, 403)
        
        # POST confirmation
        # test that realm is still present [Success]
        resp = self.client.get('/grailtest/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
    

class RealmsViewsLoggedInOwnerTest(TestCase):
    
    fixtures = ['realms_views_testdata.json']
    
    def setUp(self):
        self.owner_cred = {
            'username': 'tim', 
            'password': 'DypidhenDom'
        }
        # Log all users out
    
    def test_page_new_owner(self):
        # Login owner
        r23 = self.client.post('/accounts/login/?next=/', self.owner_cred, follow=True)
        
        resp = self.client.get('/imaginary/new_page/')
        self.assertEqual(resp.status_code, 200)
        
        # Create page should succeed [302]
        resp = self.client.post('/imaginary/new_page/', {'title': 'My +awesome% ^new* page'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp['Location'], 'http://testserver/imaginary/my_awesome_new_page/')
    
    def test_page_edit_owner(self):
        # Login owner
        r23 = self.client.post('/accounts/login/?next=/', self.owner_cred, follow=True)
        
        resp = self.client.get('/grailtest/installing/edit/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
    
    def test_page_delete_logged_in_owner(self):
        # Login owner
        r23 = self.client.post('/accounts/login/?next=/', self.owner_cred, follow=True)
        
        # GET confirmation dialog
        resp = self.client.get('/grailtest/installing/del/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
        
        # POST no data
        resp = self.client.post('/grailtest/installing/del/')
        # X:OK 302 Redirect
        self.assertEqual(resp.status_code, 302)
        
        # POST confirmation
        # test that page is no longer present [Success]
        resp = self.client.get('/grailtest/installing/')
        # X:FAIL 404
        self.assertEqual(resp.status_code, 404)
    
    def test_realm_delete_logged_in_owner(self):
        # Login owner
        r23 = self.client.post('/accounts/login/?next=/', self.owner_cred, follow=True)
        
        # GET confirmation dialog
        resp = self.client.get('/grailtest/del/')
        # X:OK 200
        self.assertEqual(resp.status_code, 200)
        
        # POST no data
        resp = self.client.post('/grailtest/del/')
        # X:OK 302 Redirect
        self.assertEqual(resp.status_code, 302)
        
        # POST confirmation
        # test that realm is no longer present [Success]
        resp = self.client.get('/grailtest/')
        # X:FAIL 404
        self.assertEqual(resp.status_code, 404)
    
