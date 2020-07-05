from rest_framework import serializers
from .models import Book,BookNumber



class BookNumberSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = BookNumber
		fields = ['id', 'isbn_10', 'isbn_13']

class BookNumberSerializer(serializers.ModelSerializer):
	number = BookNumberSerializer(many=False)
	

class BookSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Book
		fields = ['id', 'title', 'description' ,'is_pub', 'launch_date', 'number']


	