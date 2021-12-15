from django.db import models
from django.template.defaultfilters import slugify


class Department(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=150, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify('-'.join([str(self.first_name), str(self.last_name)]))
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
