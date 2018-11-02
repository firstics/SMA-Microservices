from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.settings import api_settings
from django.utils.timezone import datetime
from django.utils import timezone
from record.models import *
from record.serializers import *
from django.db.models import Q
from record.form import UserForm
import json
import csv
from .render import Render
from django.http import HttpResponse

# Create your views here.

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

def signin(request):
    if request.user.is_authenticated:
        return redirect('/srd_web/index/'+datetime.now().strftime('%Y-%m-%d'))
    return render(request, 'website/login.html')

def manage(request):
    cashiers = Cashier.objects.all()
    #records = DailyRecord.objects.filter(created_on__date=datetime(2018,4,12))
    manager = Manager.objects.filter(user_id=request.user.id)
    data = {
        "cashiers": cashiers,
        "manager": manager,
    }
    return render(request,'website/manage.html',context=data)

def add_cashier(request):
    stores = Store.objects.all()
    cashiers = Cashier.objects.all()
    #records = DailyRecord.objects.filter(created_on__date=datetime(2018,4,12))
    records = DailyRecord.objects.filter(created_on__date=datetime.today())
    manager = Manager.objects.filter(user_id=request.user.id)
    data = {
        "stores": stores,
        "cashiers": cashiers,
        "records": records,
        # "indexs": indexs,
        "manager": manager,
    }
    return render(request,'website/add_cashier.html',context=data)

def edit_cashier(request,cashier_id=None):
    if cashier_id is None:
        return redirect('/')
    cashier = Cashier.objects.get(cashier_id=cashier_id)   
    data = {
        "cashier":cashier,
    }
    return render(request,'website/edit_cashier.html',context=data)

class LoginManager(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self,request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                if request.user.is_authenticated:
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    response = jwt_response_payload_handler(token, user, request=request)
                    return Response("success", status=200)

        return Response({"detail": "Invalid credentials"}, status=401)
def record_list_by_date(request,inputDate):
    thisDate = inputDate.split('-', 2 )
    thisDate = datetime(int(thisDate[0]),int(thisDate[1]),int(thisDate[2]))
    records = list(DailyRecord.objects.filter(created_on__date=thisDate))
    data = {
        "records": records,
        "get_date": thisDate
    }
    return render(request,'website/main.html',context=data)

def history(request):
    stores = Store.objects.all()
    data = {
        "stores": stores
    }
    return render(request,'website/history.html', context=data)

def history_detail(request,store_id):
    records = DailyRecord.objects.filter(store=store_id)
    store = Store.objects.filter(store_id=store_id)
    data = {
        "records": records,
        "stores":store,
    }
    return render(request,'website/history_detail.html', context=data)

def unverify(request,record_id):
    records = DailyRecord.objects.filter(record_id=record_id)
    # store = Store.objects.filter(store_id=store_id)
    verify_choices = DailyRecord.verify_status_choices
    record_choices = DailyRecord.record_status_choices
    data = {
        "records": records,
        "verify_choices": verify_choices,
        "record_choices": record_choices
        # "stores":store,
    }
    return render(request,'website/unverify.html', context=data)

def index(request):
    #records = DailyRecord.objects.filter(created_on__date=datetime(2018,4,12))
    records = DailyRecord.objects.filter(created_on__date=datetime.today())
    data = {
        "records": records,
    }
    return render(request,'website/main.html', context=data)

def assign(request):
    stores = Store.objects.all()
    records = DailyRecord.objects.filter(created_on__date=datetime.today()).order_by('-created_on')
    #manager = Manager.objects.get(user__id=request.user.id)
    # indexs = []
    # for i in range(len(stores)):
    #     for j in range(len(cashiers)):
    #         for k in range(len(records)):
    #             if records[k].cashier.cashier_id == cashiers[j].cashier_id and records[k].store.store_id == stores[i].store_id:
    #                 #indexs.append((i,j))
    #                 indexs.append("r"+str(i)+"c"+str(j))
    #                break
    cashiers = Cashier.objects.all()
    data = {
        "records":records,
        "cashiers": cashiers,
        # "indexs": indexs,
        #"manager": manager,
    }
    return render(request,'website/assign.html',context=data)

def group_assign(request):
    stores = Store.objects.all()
    records = DailyRecord.objects.filter(created_on__date=datetime.today(), record_status="inarchive").order_by('-created_on')
    cashiers = Cashier.objects.all()
    contract_type_choices = Store.contract_type_choices
    data = {
        "records":records,
        "cashiers": cashiers,
        "stores": stores,
        "contract_type_choices": contract_type_choices,
    }
    return render(request,'website/group_assign.html',context=data)

def assign_store(request,store_id):
    stores = Store.objects.all()
    manager = Manager.objects.filter(user_id=request.user.id)
    cashiers = Cashier.objects.all()
    records = DailyRecord.objects.filter(Q(created_on__date=datetime.today()) & Q(store__store_id=store_id))
    data = {
        "stores": stores,
        "cashiers": cashiers,
        "records": records,
        "manager": manager,
    }
    return render(request,'website/assign.html',context=data)

def verify(request):
    #records = DailyRecord.objects.filter(created_on__date=datetime(2018,4,12))
    #date = datetime(2018,4,12)
    records = DailyRecord.objects.filter(verify_status="held_for_review",record_status="archive").order_by('-created_on')
    manager = Manager.objects.filter(user_id=request.user.id)
    data = {
        "records": records,
        "manager": manager,
    }
    return render(request,'website/verify.html',context=data)

class ExportCSV(APIView):
    def post(self,request):
        date_start = request.data['date_start']
        date_end = request.data['date_end']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="records.csv"'
        writer = csv.writer(response)
        writer.writerow(['Cashier','Store','ID','Record Amount','Collected Amount','Record Status','Verify Status','Date'])
        records = DailyRecord.objects.filter(created_on__date__range=[date_start, date_end]).values_list('cashier__user__first_name','store__store_name','record_id','record_amount','collected_amount','record_status','verify_status','created_on')
        for record in records:
            writer.writerow(record)
        return response

class ExportPDF(APIView):
    def get(self, request,date_start,date_end):
        records = DailyRecord.objects.filter(created_on__date__range=[date_start, date_end])
        #today = datetime.now()
        date_start.replace('-','/')
        date_end.replace('-','/')
        params = {
            #'today': today,
            'date_start':date_start,
            'date_end':date_end,
            'records':records,
            'request': request,
        }
        return Render.render('website/pdf_form.html', params)
