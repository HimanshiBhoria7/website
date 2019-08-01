from django.db import models

class Lip_Product(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=250)
    stream = models.CharField(max_length=205)
    rollno = models.CharField(max_length=102)




class Nyka(models.Model):
    rollno_stream = models.ForeignKey(Lip_Product,on_delete=models.CASCADE)


class Student(models.Model):
    registerno = models.IntegerField()
    rollno = models.IntegerField()
    name = models.CharField(max_length=150)
    emailid = models.EmailField(max_length=250,unique=True)


