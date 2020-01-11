from TaskList.classes.DbConnectorClass import DbConnectorClass

class DeleteRecordClass( DbConnectorClass ):
	def __init__( self, request ):
		self.request 	= request
		self.id 		= request.GET.get('id', False)
		
	def validation( self ):
		if not self.request.user.is_authenticated: return 'Użytkownik musi być zalogowany'
		
		try: 
			username = self.request.user.username
			obj = self.d_getTask(self.id)

		except:
			return 'Rekord nie istnieje'
		
		return True
		
	def delete( self ):
		validation = self.validation()
		if not isinstance(validation, bool): return validation
		
		self.d_deleteTask(self.id)
		
		return True