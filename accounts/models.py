from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_spec=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.spec = is_spec
        user_obj.save(using=self._db)

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_spec=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user



class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    active      = models.BooleanField(default=True)
    spec        = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects =UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_spec(self):
        return self.spec

class Specialist(models.Model):
    SPECIALITY = [
        ('elektrik', 'elektrik'),
        ('plotnik', 'plotnik'),
        ('svarshik', 'svarshik')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="specialist", null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    # email = models.EmailField(null=True)
    speciality = models.CharField(max_length=200, null=True, choices=SPECIALITY)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('derevo', 'derevo'),
        ('metal', 'metal'),
        ('dostavka', 'dostavka')
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    price = models.FloatField(null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('order in process', 'order in process'),
        ('delivered', 'delivered')
    )

    description = models.CharField(max_length=500, null=True)
    specialist = models.ForeignKey(Specialist, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(null=True)
    deposit = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description


