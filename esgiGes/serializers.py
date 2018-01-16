from rest_framework import serializers
from .models import Professor, Image, Student, Cours


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'code', 'name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image_url', 'image_url')


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ('id', 'name', 'name')
