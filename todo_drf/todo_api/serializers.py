from rest_framework import serializers
from todo_api.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ['name','description']
		# fields = '__all__' # use this if you want validate all the fields in the model