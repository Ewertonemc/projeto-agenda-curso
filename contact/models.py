from django.db import models
from django.utils import timezone

# id (primary key - criado automaticamente pelo django)
# first_name(string = Charfield), last_name(string = Charfield), phone
# email, created_date, description
# category, show, owner
# picture


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
