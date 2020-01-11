from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class EditProfileClass:
	def __init__( self, request ):
		self.request 	= request
		self.username 	= self.request.user.username
		self.password 	= request.POST.get('password', False)
		self.password_2 = request.POST.get('password_2', False)
		self.email 		= request.POST.get('email', False)
		
		self.errors = []
		
	def updateData(self):
		
		if self.email != False: 
			self.editEmail()
		
		if self.password != False and self.password.strip() != '':
			self.editPassword()
			
		
		return self.errors
		
	def editEmail(self):
		#User.objects.filter(username=self.username).update(email=self.email)
		try:
			User.objects.filter(username=self.username).update(email=self.email)
		
		except:
			self.errors.append('Email nie mogł zostać zmieniony. Spróbuj ponownie!')
		
	def editPassword(self):
	
		if self.password != self.password_2: self.errors.append('Hasło nie mogło zostać zmienione. Niepoprawnie powtórzono haslo!')
	
		try:
			u = User.objects.get(username__exact=self.username)
			u.set_password(self.password)
		except:
			self.errors.append('Hasło nie mogło zostać zmienione. Spróbuj ponownie!')
	
	
	
	
	
	
	
	
	
	