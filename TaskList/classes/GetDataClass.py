from TaskList.classes.DbConnectorClass import DbConnectorClass

class GetDataClass( DbConnectorClass ):
	def __init__( self, request ):
		self.request 	= request
		
	def getData( self ):
		rows = self.d_getTaskListByUsername(self.request.user.username)
		return rows