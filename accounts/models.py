from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    tel = models.IntegerField(blank=True,null=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    class Meta:
        db_table = 'auth_user'