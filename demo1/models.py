from django.db import models

# Create your models here.

class BookNumber(models.Model):
	ISBN_10 = models.CharField(max_length=10, blank=True)
	ISBN_13 = models.CharField(max_length=13, blank=True)

	

class Book(models.Model):
	title = models.CharField(blank=False, unique=True, max_length=36)

	description = models.TextField(blank=True)
	price = models.FloatField(blank=False, default=0)
	cover = models.ImageField(upload_to='covers/', blank=True)
	launch_date = models.DateField(blank=True, default=None, null=True)
	is_pub = models.BooleanField(default=False)

	number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

		

	def __str__(self):
		return self.title

class Character(models.Model):
	name = models.CharField(max_length=30)
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name = 'characters')


class Author(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=50)
	books = models.ManyToManyField(Book, related_name='authors')