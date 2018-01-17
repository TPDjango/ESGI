from django.urls import reverse, resolve
from django.test import TestCase
from django.urls import get_resolver


class TestUrlsAreWorking(TestCase):

    def testProfessor(self):
        url = reverse('get_professor', kwargs={'id': 2})
        self.assertEqual(url, '/esgi/professors/2/')



    def testStudent(self):
        url = reverse('get_student', kwargs={'id': 1})
        self.assertEqual(url, '/esgi/students/1/')



    def testImage(self):
        url = reverse('get_image', kwargs={'id': 3})
        self.assertEqual(url, '/esgi/images/3/')



    def testCourse(self):
        url = reverse('get_cours', kwargs={'id': 3})
        self.assertEqual(url, '/esgi/courses/3/')


    def testStudents(self):
            url = reverse('students')
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)

    def testProfessors(self):
            url = reverse('professors')
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)

    def testImages(self):
            url = reverse('images')
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)


    def testCourses(self):
            url = reverse('courses')
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)