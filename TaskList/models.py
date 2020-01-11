# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tasks( models.Model ):
	
	Task 	= models.CharField(max_length=100, verbose_name="Zadanie")
	Date 	= models.DateField(verbose_name="Data")
	Type 	= models.CharField(max_length=30, verbose_name="Rodzaj")
	Priority 	= models.CharField(max_length=30, verbose_name="Priorytet")
	AddedBy		= models.CharField(max_length=30, verbose_name="Wprowadził")
	DateInserted = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	class Meta:
		db_table = 'tasks'
		
	def __unicode__(self):
		return str( self.AddedBy ) + '-' + str( self.Date )
		
	
