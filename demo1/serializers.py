from rest_framework import serializers
from .models import Book, BookNumber, Character, Author



class BookNumberSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = BookNumber
		fields = ['id', 'ISBN_10', 'ISBN_13']

class CharacterSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Character
		fields = ['id', 'name']
class AuthorSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Author
		fields = ['id', 'fname', 'lname']

class BookSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	number = BookNumberSerializer(many=False)
	characters = CharacterSerializer(many=True)
	authors = AuthorSerializer(many=True)

	class Meta:
		model = Book
		fields = ['id', 'title', 'description' ,'is_pub', 'launch_date', 'number', 'characters', 'authors']

class BookMiniSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Book
		fields = ['id', 'title']

	