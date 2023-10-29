from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm , TaskAssignmentForm
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Task

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Task
from .forms import TaskAssignmentForm

# Create your views here.
def home(request): 
	return render(request, 'baseapp/home.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home')   
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') 
	else:
		return render(request, 'baseapp/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = form.cleaned_data.get('group')
			user.groups.add(group) 
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'baseapp/register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'baseapp/edit_profile.html', context)
	

def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else: 		 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'baseapp/change_password.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def assign_task(request):
# 	#task = get_object_or_404(Task,pk=task_id)
	
# 	if request.method =='POST':
# 		form = TaskAssignmentForm(request.POST)
# 		#form = TaskAssignmentForm(task.group, request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, ('Task Assigned Successfully..'))
# 			return redirect('home')
# 	else: 		
# 		form = TaskAssignmentForm()
# 		#form = TaskAssignmentForm(task.group, instance=task)

# 	context = {'form': form}
# 	return render(request, 'baseapp/assign_task.html',context)



#@user_passes_test(lambda u: u.is_superuser)
def assign_task(request):
	#task = get_object_or_404(Task)
	if request.method =='POST':
		form = TaskAssignmentForm(request.POST)
		#form = TaskAssignmentForm(task.assigned_to, request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request, ('Task Assigned Successfully..'))
			return redirect('home')
	else: 		
		form = TaskAssignmentForm()
		#form = TaskAssignmentForm(task.assigned_to, instance=task)

	context = {'form': form}
	return render(request, 'baseapp/assign_task.html',context)



@login_required
def task_detail(request):
	user_groups = request.user.groups.all()  # Get the groups the user belongs to
	tasks = Task.objects.filter(assigned_to_group__in=user_groups)

    #tasks = Task.objects.filter(assigned_to=request.user.groups.first())
	context = {
        'tasks': tasks,
    }
	
	return render(request, 'baseapp/task_list.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def create_task(request):
# 	#task = get_object_or_404(Task,pk=task_id)
	
# 	if request.method =='POST':
# 		form = TaskCreationForm(request.POST)
# 		#form = TaskAssignmentForm(task.group, request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, ('Task Created Successfully..'))
# 			return redirect('home')
# 	else: 		
# 		form = TaskCreationForm()
# 		#form = TaskAssignmentForm(task.group, instance=task)

# 	context = {'form': form}
# 	return render(request, 'baseapp/create_task.html',context)

# views.py

# def assign_task(request):
#     if request.method == 'POST':
#         form = TaskAssignmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home') 
#     else:
#         form = TaskAssignmentForm()
    
#     return render(request, 'baseapp/assign_task.html', {'form': form})
