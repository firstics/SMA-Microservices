from record.models import Store, DailyRecord
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import datetime
class RecordScheduler():
    #RUN_EVERY_MINS = 1440 # every 24 hours
    #schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'record.record_scheduler' 
    def do(self):
        stores = Store.objects.order_by('created_on')
        for store in stores:
            try:
                latest_record = DailyRecord.objects.filter(store=store).latest()
                record = DailyRecord(store=store, cashier=latest_record.cashier)
            except ObjectDoesNotExist:
                record = DailyRecord(store=store)
            record.save()
            print(store,' record created on '+str(datetime.today()))

def myScheduler():
    record_scheduler = RecordScheduler()
    record_scheduler.do()