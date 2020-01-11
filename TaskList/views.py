from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from TaskList.classes.LoginClass import LoginClass
from TaskList.classes.GetDataClass import GetDataClass
from TaskList.classes.RegisterClass import RegisterClass
from TaskList.classes.AddTaskClass import AddTaskClass
from TaskList.classes.DeleteRecordClass import DeleteRecordClass
from TaskList.classes.EditProfileClass import EditProfileClass



import sys, time

def index_view(request):
	getDataClass = GetDataClass( request )
	
	if not request.user.is_authenticated: 
		return render(request, 'index_unlogged.html')
	
	return render(request, 'index.html', {
		'data': getDataClass.getData()
	})	
	
def add_task_view(request):
	if not request.user.is_authenticated: return redirect('/login')
	errors = False
	
	if request.method == 'POST':
		addTaskClass 	= AddTaskClass( request )
		added 			= addTaskClass.addTask()
		
		if isinstance(added, bool): return redirect('/')
		else: errors = added
		
	return render(request, 'add_task.html', {
		'errors': errors
	})	
	
def login_view(request):
	error = False
	if request.method == 'POST':
		loginClass = LoginClass( request )
		isLogged = loginClass.isLogged()
		
		if isLogged: return redirect('/')
		else: error = True
	
	return render(request, 'login.html', {
		'error': error
	})

def register_view(request):
	error = False
	
	if request.method == 'POST':
		registerClass 	= RegisterClass( request )
		isRegistered 	= registerClass.isRegistered()
		
		if isRegistered: return login_view(request)
		else: error = True
	
	return render(request, 'register.html', {
		'error': error
	})
	
def delete_record_view(request):
	error = False
	if request.method == 'GET':
		deleteRecordClass = DeleteRecordClass( request )
		deleted = deleteRecordClass.delete()
		
		if isinstance(deleted, bool): return redirect('/')
		else: error = deleted
		
	return redirect('/')
	
def edit_profile_view(request):

	if not request.user.is_authenticated: return render(request, 'index_unlogged.html')

	errors = []
	formSent = False
	
	if request.method == 'POST':
		editProfileClass = EditProfileClass( request )
		updateData 		 = editProfileClass.updateData()
		
		errors 	 = updateData
		formSent = True

	return render(request, 'editProfile.html', {
		'errors': errors,
		'formSent': formSent,
		'emailAddress': User.objects.get(username=request.user.username).email
	})
	
def logout_view(request):
	logout(request)
	return redirect('/')