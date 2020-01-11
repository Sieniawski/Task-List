from django.contrib.auth.models import User

class RegisterClass:
	def __init__( self, request ):
		self.request 	= request
		self.username 	= request.POST.get('username', False)
		self.password 	= request.POST.get('password', False)
		self.password_2 = request.POST.get('password_2', False)
		
	def validation( self ):
		if not self.username or not self.password or not self.password_2: return False
		if self.password != self.password_2: return False
		
		if self.username_present( self.username ): return False
		
		return True
		
	def isRegistered( self ):
		validation = self.validation()
		if not validation: return False
		
		user = User.objects.create_user(username = self.username, password = self.password )
		user.save()
		
		return True
		
	def username_present(self, username):
		if User.objects.filter(username=username).exists():
			return True
    
		return False	