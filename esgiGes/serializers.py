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


class getImageSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Image
        fields = ('id', 'image_url', 'student')

class postImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image_url', 'student')


class getCoursSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    professor = ProfessorSerializer()

    class Meta:
        model = Cours
        fields = ('id', 'name', 'student', 'professor')

class postCoursSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    professor = ProfessorSerializer()

    class Meta:
        model = Cours
        fields = ('id', 'name', 'student', 'professor')
