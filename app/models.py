from django.db import models

# Create your models here.

class User(models.Model):
    # ID = models.AutoField(primary_key=True, unique=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    rut = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    member_type = models.CharField(max_length=200)

    observation = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Records(models.Model):
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.USER_ID} {self.time_stamp}'