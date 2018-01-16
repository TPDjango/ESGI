from django.db import models



class Professor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return "{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ('first_name', 'last_name')

class Student(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{self.code} {self.name}"

    class Meta:
        unique_together = ('code', 'name')


class Image(models.Model):
    image_url = models.CharField(max_length=220)
    student = models.OneToOneField(Student)
    def __str__(self):
        return "{self.image_url} -"

    class Meta:
        unique_together = ('image_url', 'image_url')

class Cours(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return "{self.name} -"

    class Meta:
        unique_together = ('name', 'name')
