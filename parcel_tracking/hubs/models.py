from django.db import models


class Hub(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_address(self):
        return f"{self.address} {self.province} {self.city} {self.zipcode}"

    def __str__(self):
        return f"{self.name} - {self.city}"
