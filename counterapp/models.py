from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length= 120)
    def __str__(self):
        return self.category_name

class EmployeeModel(models.Model):
    employee_id = models.CharField("Employee Id", max_length=10, blank=False)
    employee_name = models.CharField("Employee Name", max_length=25)

    def __str__(self):
        return self.employee_id

class NewsData(models.Model):
    title = models.CharField('News Title', max_length = 120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    place = models.CharField('Place', max_length = 120)
    date = models.DateTimeField('Event Date and Time')
    description = models.TextField('Details')
    image = models.ImageField('Picture', upload_to= 'images/')

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField('Name', max_length=25, blank = False)
    email = models.EmailField('Email', blank = False)
    message = models.TextField('Message', blank = False)

    def __str__(self):
        return self.name


