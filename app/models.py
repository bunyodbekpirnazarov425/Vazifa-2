from django.db import models

class Klass(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi

class Mehmonxona(models.Model):
    nomi = models.CharField(max_length=100)
    yulduzlar_soni = models.PositiveIntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi

class Travle(models.Model):
    nomi = models.CharField(max_length=100)
    izoh = models.TextField()
    muddati = models.PositiveIntegerField(help_text="Sayohat davomiyligi (kunlarda)")
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    mehmonxona = models.ForeignKey(Mehmonxona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi
