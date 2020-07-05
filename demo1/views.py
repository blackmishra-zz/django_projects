from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
"""
class first_class(View):
	#demo desc for first class
	books = Book.objects.filter(is_pub = True)
	output = ''
	for book in books:
		output += f"We have {book.title} on {book.id} number<br>"

	def get(self, request):
		return HttpResponse(self.output)
		"""

	
"""

def first(request):
	book = Book.objects.all()
	return render(request,'first_temp.html', {'book' : book})

"""
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
