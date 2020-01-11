from TaskList.models import Tasks

class DbConnectorClass:
		
	def d_addTask( self, task, date, priority, type, username ):
		record = Tasks(
			Task 		= task, 
			Date 		= date,
			Priority 	= priority,
			Type		= type,
			AddedBy		= username
		)
		record.save()
		
	def d_deleteTask( self, id ):
		record = Tasks.objects.filter(id=id)
		record.delete()
		
	def d_getTask( self, id ):
		obj = Tasks.objects.get(id=id)
		
		return obj
		
	def d_getTaskListByUsername( self, username ):
		obj = Tasks.objects.filter(AddedBy=username).order_by('Date')
		
		return obj