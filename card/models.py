from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)


class Logo(models.Model):
    prompt = models.TextField()
    neg_prompt = models.TextField(null=True, blank=True)
    style = models.CharField(max_length=20)
    image = models.ImageField()


class Background(models.Model):
    prompt = models.TextField()
    neg_prompt = models.TextField(null=True, blank=True)
    style = models.CharField(max_length=20)
    image = models.ImageField()
    transparency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Card(models.Model):
    person = models.ForeignKey(Person, blank=False, null=False, on_delete=models.CASCADE)
    logo = models.ForeignKey(Logo, blank=False, null=False, on_delete=models.CASCADE)
    background = models.ForeignKey(Background, blank=False, null=False, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    text_color = models.CharField(max_length=100, null=True, blank=True)
    text_size = models.IntegerField()
    image = models.ImageField()

