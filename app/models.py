from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255, required=True)
    rating = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Klass(models.Model):
    name = models.CharField(max_length=255, required=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Travel(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    term = models.IntegerField()
    price = models.IntegerField()
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True)
