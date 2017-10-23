# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from ..dashboard_app.models import Comment
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password)
    
    def registerVal(self, postData):
        results = {'errors':[], 'status': False}
        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short')
        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short')
        if not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            results['status'] = True
            results['errors'].append('Email is not in an acceptable format')
        if len(postData['password']) < 6:
            results['status'] = True
            results['errors'].append('Password is too short')
        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords did not match')
        try:
            self.get(email = postData['email'])
            results['status'] = True
            results['errors'].append('Email is already registered')
        except:
            pass
        return results
    
    def loginVal(self, postData):
        results = {'errors':[], 'status': False, 'user': None}
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check your email and try again.')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('That email does not match the password registered in the database.')
                results['status'] = True
        return results

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Comment(models.Model):
    comment = models.TextField(max_length = 1000)
    author = models.ForeignKey(User, related_name = 'comments_by')
    recipient = models.ForeignKey(User, related_name = 'comments_on')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)