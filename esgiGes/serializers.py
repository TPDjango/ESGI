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
    student = StudentSerializer()

    class Meta:
        model = Image
        fields = ('id', 'image_url', 'student')

    def create(self, validated_data):
        return Image.objects.create(**validated_data)


class CoursSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    professor = ProfessorSerializer()

    class Meta:
        model = Cours
        fields = ('id', 'name', 'student', 'professor')
