from __future__ import unicode_literals
from django.db import models


class Register(models.Model): 
	name= models.CharField(max_length = 50)
	mobile=models.CharField(max_length=20)
	email= models.EmailField(max_length = 50)
	course= models.CharField(max_length=50)
	source=models.CharField(max_length=50)
	status=models.CharField(max_length=50)
	date= models.DateField()
	counsler=models.CharField(max_length=50)
	remark=models.CharField(max_length=50)
	class Meta:
		db_table = "register"

