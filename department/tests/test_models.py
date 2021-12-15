from django.test import TestCase

from department.models import Department, Employee


class DepartmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Department.objects.create(title='Department title', description='Description text')

    def test_title_label(self):
        department = Department.objects.get(id=1)
        field_label = department._meta.get_field('title').verbose_name
        print(field_label)
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        department = Department.objects.get(id=1)
        max_length = department._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_description_label(self):
        department = Department.objects.get(id=1)
        field_label = department._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        department = Department.objects.get(id=1)
        max_length = department._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_slug_label(self):
        department = Department.objects.get(id=1)
        field_label = department._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_slug_max_length(self):
        department = Department.objects.get(id=1)
        max_length = department._meta.get_field('slug').max_length
        self.assertEqual(max_length, 150)


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
