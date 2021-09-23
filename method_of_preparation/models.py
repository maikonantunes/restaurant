from django.db import models


class MethodPreparation(models.Model):
    description = models.TextField()
    order_preparation = models.IntegerField()

    def __str__(self):
        return self.description
