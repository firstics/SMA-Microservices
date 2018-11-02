from srd_web import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from django.conf.urls import url



urlpatterns = [
    url(r'api-login',views.LoginManager.as_view(),name='api-login'),
    url(r'^signin',views.signin,name='signin'),
    url(r'^index/(?P<inputDate>[0-9\-]+)$',login_required(views.record_list_by_date),name='record_list_by_date'),
    url(r'^record/store/(?P<store_id>[0-9]+)$',login_required(views.assign_store),name='assign_store'),
    url(r'^manage',login_required(views.manage),name='manage'),
    url(r'^add_cashier',login_required(views.add_cashier),name='add_cashier'),
    url(r'^edit_cashier/(?P<cashier_id>[0-9]+)$',login_required(views.edit_cashier),name='assign'),
    url(r'^assign',login_required(views.assign),name='assign'),
    url(r'^group_assign',login_required(views.group_assign),name='group_assign'),
    url(r'^verify',login_required(views.verify),name='verify'),
    url(r'^history',login_required(views.history),name='history'),
    url(r'^records/store/(?P<store_id>[0-9]+)$',login_required(views.history_detail),name='history_detail'),
    url(r'^unverify/record/(?P<record_id>[\w]+)$',views.unverify,name='unverify'),
    url(r'^export/csv', views.ExportCSV.as_view(), name='export_records_csv'),
    url(r'^export/pdf/(?P<date_start>[0-9\-]+)/(?P<date_end>[0-9\-]+)', views.ExportPDF.as_view(), name='export_records_pdf'),
]
