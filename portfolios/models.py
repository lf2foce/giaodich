from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Transaction(models.Model):
    # id = models.AutoField(primary_key=True)
    STATUS_CHOICES = (('pending', 'Pending'), ('canceled', 'Canceled'), ('executed', 'Executed'))
    client = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='trading_transactions')
    company = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    shares = models.IntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=4)
    symbol = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                                 choices=STATUS_CHOICES,
                                 default='pending')
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f"{self.client} {self.action} {self.shares} {self.symbol} "

# class PublishedManager(models.Manager):
#        def get_queryset(self):
#            return super(PublishedManager,
#                         self).get_queryset()\
#                              .filter(status='published')