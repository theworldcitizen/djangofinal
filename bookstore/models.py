from django.db import models
from utils.constants import journal_type
from auth_.models import MainUser


# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Book(models.Model):
    num_pages = models.CharField(max_length=250, null=True, blank=True)
    genre = models.CharField(max_length=250, null=True, blank=True)
    book_fields = models.ForeignKey(BookJournalBase, related_name='books', on_delete=models.CASCADE)


class Journal(models.Model):
    type = models.CharField("Type", choices=journal_type, max_length=20)
    publisher = models.ForeignKey(MainUser, verbose_name="Publisher", on_delete=models.CASCADE, null=True)
    journal_fields = models.ForeignKey(BookJournalBase, related_name='journals', on_delete=models.CASCADE)
