from django.db import models

# Create your models here.

class ToDoItem(models.Model):

	content = models.CharField(max_length = 100)


	def __str__(self):
		return self.content