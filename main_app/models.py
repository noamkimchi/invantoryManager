from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    inventory = models.IntegerField(default=0)
    issued = models.IntegerField(default=0)
    reminder = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Kit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    issued = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class KitContains(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, models.SET_NULL, null=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return '{}-{}'.format(self.kit.name, self.item.name)

