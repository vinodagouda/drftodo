from django.db import models

# Create your models here.

class ToDo(models.Model):
	"""docstring for ToDo"""

	name = models.CharField(max_length=250)
	description = models.TextField()
	is_finished = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name