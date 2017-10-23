# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User, Comment

# Create your views here.
def dashboard(request):
    if request.session['id'] == None:
        return redirect('/')
    else:
        context = {
            'users': User.objects.exclude(id = request.session['id'])
        }
        return render(request, 'dashboard_app/dashboard.html', context)

def profile(request,num):
    if request.session['id'] == None:
        return redirect('/')
    else:
        # print User.objects.get(id=num).comments_on
        # person = User.objects.get(id=num)
        # print len(Comment.objects.all().filter(users=person))
        # print len(Comment.objects.filter(users=person))
        context = {
            # 'comments': User.objects.get(id=num).comments.all(),
            'comments': Comment.objects.filter(recipient_id=num),
            'user': User.objects.get(id=num).first_name,
            'id': num,
        }
        return render(request, 'dashboard_app/comments.html', context)

def submit(request,num):
    author = User.objects.get(id=request.session['id'])
    recipient = User.objects.get(id=num)
    Comment.objects.create(comment = request.POST['comment'], author = author, recipient=recipient)
    # comment = Comment.objects.last()
    # print 
    # comment_on.comments_on = comment
    # comment_on.save()
    string = "/dashboard/comments/"+num
    return redirect(string)