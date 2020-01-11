from django.contrib.auth import authenticate, login

class LoginClass:
	def __init__( self, request ):
		self.request 	= request
		self.username 	= request.POST.get('username', False)
		self.password 	= request.POST.get('password', False)
		
	def getUser( self ):
		user = authenticate( self.request, username = self.username, password = self.password )
		
		return user
		
	def isLogged( self ):
		user = self.getUser()
		
		if user is not None: 
			login( self.request, user )
			return True
		else:
			return False