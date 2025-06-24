from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    comment = models.TextField()

    def __str__(self):
        return self.name

class InquiryForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    comment = models.TextField()

    class Meta:
        db_table = "inquiry_form"  # Custom table name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
