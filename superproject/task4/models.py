from django.db import models

class NumbersManager(models.Model):
    pass
class Numbers(models.Model):
    objects = NumbersManager()
    name = models.TextField(unique=True)
    n = models.BigIntegerField(default=0)

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id}, name = {self.name}, n = {self.n}) "