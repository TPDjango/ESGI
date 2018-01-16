from django.contrib import admin

# Register your models here.
from .models import Professor, Student, Cours, Image

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Cours)
admin.site.register(Image)
