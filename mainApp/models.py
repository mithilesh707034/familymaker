from django.db import models

class Nomination_Form(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    age=models.CharField(max_length=100,default='',null=True,blank=True)
    mobile=models.CharField(max_length=100,default='',null=True,blank=True)
    location=models.CharField(max_length=100,default='',null=True,blank=True)
    nominate_name=models.CharField(max_length=100,default='',null=True,blank=True)
    q1=models.CharField(max_length=100,default='',null=True,blank=True)
    q1_others=models.TextField(default='',null=True,blank=True)
    q2=models.CharField(max_length=100,default='',null=True,blank=True)
    q3=models.CharField(max_length=100,default='',null=True,blank=True)
    q4=models.CharField(max_length=100,default='',null=True,blank=True)
    q5=models.CharField(max_length=100,default='',null=True,blank=True)
    q6=models.CharField(max_length=100,default='',null=True,blank=True)
    q7=models.CharField(max_length=100,default='',null=True,blank=True)
    q7_others=models.TextField(default='',null=True,blank=True)
    q8=models.CharField(max_length=100,default='',null=True,blank=True)
    q9=models.CharField(max_length=100,default='',null=True,blank=True)
    q10=models.CharField(max_length=100,default='',null=True,blank=True)
    q11=models.CharField(max_length=100,default='',null=True,blank=True)
    q12=models.CharField(max_length=100,default='',null=True,blank=True)
    q13=models.CharField(max_length=100,default='',null=True,blank=True)
    q14=models.CharField(max_length=100,default='',null=True,blank=True)
    q15=models.CharField(max_length=100,default='',null=True,blank=True)
    q16=models.CharField(max_length=100,default='',null=True,blank=True)
    q17=models.CharField(max_length=100,default='',null=True,blank=True)
    q18=models.CharField(max_length=100,default='',null=True,blank=True)
    q19=models.CharField(max_length=100,default='',null=True,blank=True)
    q20=models.TextField(default='',null=True,blank=True)
    q21=models.TextField(default='',null=True,blank=True)
    q22=models.TextField(default='',null=True,blank=True)
    q23=models.CharField(max_length=100,default='',null=True,blank=True)
    picture=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    def __str__(self):
        return self.name


class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
    def __str__(self):
        return self.name
