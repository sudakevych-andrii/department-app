from django.test import TestCase
from django.urls import reverse

from department.models import Department, Employee


class DepartmentListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_departments = 10
        for department_num in range(1, number_of_departments):
            Department.objects.create(
                title=f'Departments {department_num}',
                description=f'Departments {department_num} description'
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/departments/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('departments'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('departments'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'department/departments.html')
