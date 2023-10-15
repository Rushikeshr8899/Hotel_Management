from django.db import models
from django.contrib.auth.models import User


class hotel_owner_details(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    contact=models.BigIntegerField()
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=100,default='')
    distict=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=500,default='')

class hotel_details(models.Model):
    hotel_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel_name=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=500,default='')
    email=models.CharField(max_length=200,default='')
    contact=models.BigIntegerField()
    is_open = models.BooleanField(default=True)
    average_rating=models.IntegerField(default=3)
    register_date=models.DateTimeField(null=True)
    logo = models.ImageField(upload_to='hotel_logos/', blank=True, null=True)
    image=models.ImageField(upload_to='hotel_images/',blank=True,null=True)
    open_time=models.TimeField(null=True)
    close_time=models.TimeField(null=True)

class hotel_customer(models.Model):
    customer_us_id=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(hotel_details,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default='')
    contact=models.BigIntegerField()

class hotel_table(models.Model):
    hotel = models.ForeignKey(hotel_details, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=200)
    capacity = models.IntegerField()

class item_category(models.Model):
    category_name=models.CharField(max_length=200)

class menu_item(models.Model):
    hotel = models.ForeignKey(hotel_details, on_delete=models.CASCADE)
    category=models.ForeignKey(item_category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    item_image=models.ImageField(upload_to='item_images/',blank=True,null=True)
    description = models.TextField(default='')
    price = models.IntegerField()

class order(models.Model):
    hotel = models.ForeignKey(hotel_details, on_delete=models.CASCADE)
    customer = models.ForeignKey(hotel_customer, on_delete=models.CASCADE,null=True)
    table=models.ForeignKey(hotel_table,on_delete=models.CASCADE,null=True)
    items = models.CharField(max_length=500)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(null=True)


class Review(models.Model):
    hotel = models.ForeignKey(hotel_details, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(hotel_customer, on_delete=models.CASCADE,null=True)
    rating = models.IntegerField()
    review_text = models.TextField(default='')
    review_date = models.DateTimeField(auto_now_add=True)

class salary_types(models.Model):
    type=models.CharField(max_length=100)

class hotel_staff(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.CharField(max_length=100,default='')
    contact=models.BigIntegerField()
    salary=models.IntegerField()
    salary_type=models.ForeignKey(salary_types,on_delete=models.CASCADE,default=1)
    join_date=models.DateField(null=True)
