from django.db import models



class Professor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Student(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Image(models.Model):
    image_url = models.CharField(max_length=220)
    student = models.OneToOneField(Student)

class Cours(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)
