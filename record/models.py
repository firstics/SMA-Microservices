from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
# Create your models here.

class Photo(models.Model):
    id = models.AutoField(max_length=10,primary_key=True)
    file = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

class Signature(models.Model):
    id = models.AutoField(max_length=10,primary_key=True)
    file = models.ImageField(upload_to='signatures/%Y/%m/%d')
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    class Meta:
        verbose_name = 'signature'
        verbose_name_plural = 'signatures'

class Cashier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    cashier_id = models.AutoField(max_length=10,primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    def __str__(self):
        return "%s %s" %  (self.user.first_name, self.user.last_name)
 
class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    manager_id = models.AutoField(max_length=10,primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    def __str__(self):
        return "%s %s" %  (self.user.first_name, self.user.last_name)

class Store(models.Model):
    contract_type_choices = (
        ('normal', 'เก็บเงินสด'),
        #('untrusted_company', 'Untrusted Company'),
        ('trusted_company', 'จดยอด'),
    )
    store_facility_choices = (
        ('fashion_island', 'Fashion Island'),
        ('promenade', 'Promenade'),
    )
    store_id = models.AutoField(max_length=10,primary_key=True)
    store_name = models.CharField(max_length=60)
    store_email = models.EmailField(max_length=100,null=True)
    contract_type = models.CharField(max_length=50,
        choices=contract_type_choices,
        default='normal',
    )
    store_detail = models.CharField(max_length=255,null=True)
    store_facility = models.CharField(max_length=100,
        choices=store_facility_choices,
        default='fashion_island',
        null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)

    def __str__(self):
        return self.store_name

class DailyRecord(models.Model):
    class Meta:
        get_latest_by = 'created_on'
    class RecordID():
        def get_record_id():
            while True:
                unique_id = get_random_string(length=32)
                unique_id = str(unique_id)
                try:
                    DailyRecord.objects.get(record_id=unique_id)
                except:
                    return unique_id
    
    record_status_choices = (
        ('archive','สำเร็จ'),
        ('inarchive','ไม่สำเร็จ'),
    )
    verify_status_choices = (
        ('held_for_review','อยู่ในระหว่างการตรวจสอบ'),
        ('approved','อนุมัติ'),
        ('declined','ไม่อนุมัติ'),
    )
    record_id = models.CharField(max_length=32,
        primary_key=True,
        serialize=False,
        default=RecordID.get_record_id)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    cashier = models.ForeignKey(Cashier,on_delete=models.CASCADE,null=True,blank=True)
    record_status = models.CharField(choices=record_status_choices,max_length=30,default='inarchive')
    verify_status = models.CharField(choices=verify_status_choices,max_length=30,default='held_for_review')
    verified_by = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True,blank=True,related_name="verified_by")
    verified_date = models.DateTimeField(blank=True,null=True)
    record_amount = models.FloatField(default=0)
    collected_amount = models.FloatField(default=0)
    voucher = models.FloatField(default=0)
    credit = models.FloatField(default=0)
    assigned_by = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True,blank=True,related_name="assigned_by")

    number_of_1000 = models.IntegerField(default=0)
    number_of_500 = models.IntegerField(default=0)
    number_of_100 = models.IntegerField(default=0)
    number_of_50 = models.IntegerField(default=0)
    number_of_20 = models.IntegerField(default=0)
    number_of_10 = models.IntegerField(default=0)
    number_of_5 = models.IntegerField(default=0)
    number_of_2 = models.IntegerField(default=0)  
    number_of_1 = models.IntegerField(default=0)
    number_of_50_satang = models.IntegerField(default=0)
    number_of_25_satang = models.IntegerField(default=0) 
    collect_date = models.DateTimeField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.CharField(null=True,blank=True,max_length=255)
    signature = models.ManyToManyField(Signature,blank=True)
    receipts = models.ManyToManyField(Photo,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, using='default', **kwargs)
        super().save(*args, using='authen-replica', **kwargs)
        super().save(*args, using='service-primary', **kwargs)
        super().save(*args, using='service-replica-1', **kwargs)
        super().save(*args, using='service-replica-2', **kwargs)
    
    def __str__(self):
        time = str(self.created_on)
        time = time[0:11]
        return '%s, %s' % (self.store,time)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile_number = models.CharField(max_length=50, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

#     def __str__(self):
#         return self.user.username
