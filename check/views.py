# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Fuser
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Exists

# Create your views here.


def saveData(request):

	if request.method == "POST":
		cid = request.POST['spid']
		
	print(cid)

	if Fuser.objects.filter(fid=cid).exists():
		if Fuser.objects.filter(nop=0).exists() :
			fob=Fuser.objects.filter(fid=cid).update(nop=1)
 			return redirect(dispCred,cid)
		else:
			text="""<h1> Credentials already issued </h1>"""
			return HttpResponse(text)
	else:
		text="""<h2> Invalid ID </h2>"""
		return HttpResponse(text)

def dispCred(request,id):

	obj=Fuser.objects.filter(fid=id)
	resp={}
	resp['flag']=False
	resp['fusers']=obj
	return render(request, 'cred.html',resp)


def fourdig(request):
#need to write code to check if first time

	return render(request, 'start.html')
