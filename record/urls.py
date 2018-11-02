from record import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url



urlpatterns = [
    url(r'^daily_record_list',views.DailyRecordList.as_view(),name='daily_record_list'),
    url(r'^daily_record_by_cashier/(?P<cashier_id>[0-9]+)$',views.DailyRecordListByCashier.as_view(),name='daily_record_list_by_cashier'),
    url(r'^store_list',views.StoreList.as_view(),name='store_list'),
    url(r'^cashier_list',views.CashierList.as_view(),name='cashier_list'),
    url(r'^cashier_detail/(?P<cashier_id>[0-9]+)$', views.CashierDetail.as_view()),
    url(r'^store_detail/(?P<store_id>[0-9]+)$', views.StoreDetail.as_view()),
    url(r'^store_record_list/(?P<store_id>[0-9]+)$', views.RecordByStore.as_view()),
    url(r'^record_detail/(?P<record_id>[\w]+)$', views.DailyRecordDetail.as_view()),
    url(r'^forgot_password', views.forgot_password),
    url(r'^upload/image',views.PhotoList.as_view(),name='photo_list'),
    url(r'^upload/signature',views.SignatureList.as_view(),name='signature_list'),
    url(r'^login',views.Login.as_view(),name='login'),
    url(r'^logout',views.Logout.as_view(),name='logout'),
    url(r'^receipt_list/(?P<record_id>[\w]+)$',views.Receipt.as_view())
]

# var request = $.ajax({
#                 url: "/record/export/csv/",
#                 method: "POST",
#                 contentType: "application/json",
#                 dataType: "json",
#                 data: JSON.stringify({
#                     "date_start":date_start,
#                     "date_end":date_end
#                 }),
#             });