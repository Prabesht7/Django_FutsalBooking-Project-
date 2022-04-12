from django.db import models
from django.shortcuts import render


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    username = models.CharField(max_length=150, )
    email = models.EmailField(null=True)
    password = models.CharField(max_length=150, null=True)
    avatar = models.ImageField(upload_to='static/UserProfile', null=True , blank=True)
    address = models.CharField(max_length=150 , null=True , blank=True)
    age = models.IntegerField(null=True , blank=True)


    def register(self):
        self.save()

    @staticmethod
    def get_all_customers():
        return Customer.objects.all()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
            return False

    def userisExists(self):
        if Customer.objects.filter(username=self.username):
            return True
            return False

    def phoneisExists(self):
        if Customer.objects.filter(phone=self.phone):
            return True
            return False

    @staticmethod
    def get_customers_by_customer(customer_id):
        return Customer.objects.filter(customer=customer_id)