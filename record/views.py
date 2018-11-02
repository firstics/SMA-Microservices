from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from django.utils.timezone import datetime
from record.models import *
from record.serializers import *
import json
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import smtplib
# Create your views here.

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

# Rest api end point

class CashierList(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        rest_list = Cashier.objects.order_by('created_on')
        serializer = CashierSerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)
    def post(self,request,format=None):
        serializer = CashierSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.create(validated_data=request.data)
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CashierDetail(APIView):
    @method_decorator(csrf_exempt)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get_object(self, cashier_id):
        try:
            return Cashier.objects.get(cashier_id=cashier_id)
        except Cashier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,cashier_id,format=None):
        cashier = self.get_object(cashier_id)
        serializer = CashierSerializer(cashier)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

    def patch(self,request,cashier_id,format=None):
        cashier = self.get_object(cashier_id)
        user = User.objects.get(id=cashier.user.id)
        user_data = request.data.pop('user')
        serializer = UserSerializer(user,data=user_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cashier_id, format=None):
        cashier = self.get_object(cashier_id)
        cashier.user.delete()
        cashier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class StoreList(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        rest_list = Store.objects.order_by('created_on')
        serializer = StoreSerializer(rest_list, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)
    def post(self,request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            store = serializer.save()
            record = DailyRecord(store=store)
            record.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoList(APIView):
    def post(self,request):
        print('request.data',request.data)
        serializer = PhotoSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        if serializer.is_valid():
            photo = serializer.save()
            record = DailyRecord.objects.get(record_id=request.data['record_id'])
            record.receipts.add(photo)
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignatureList(APIView):
    def post(self,request):
        print('request.data',request.data)
        serializer = SignatureSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        if serializer.is_valid():
            signature = serializer.save()
            record = DailyRecord.objects.get(record_id=request.data['record_id'])
            record.signature.add(signature)
            return Response("Success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordByStore(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get_objects(self, store_id):
        try:
            return DailyRecord.objects.filter(store=store_id)
        except DailyRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,store_id,format=None):
        records = self.get_objects(store_id)
        serializer = DailySerializer(records, many=True)
        print(serializer.data)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

class StoreDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get_object(self, store_id):
        try:
            return Store.objects.get(store_id=store_id)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,store_id,format=None):
        store = self.get_object(store_id)
        serializer = StoreSerializer(store)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

class DailyRecordList(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        records = DailyRecord.objects.filter(created_on__date=datetime.today()).order_by('record_status','created_on')
        #records = DailyRecord.objects.filter(created_on__date=datetime(2018,4,12))
        serializer = DailySerializer(records, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)
    
    def post(self,request,format=None):
        serializer = DailySerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.create(validated_data=request.data)
            store = Store.objects.get(store_id=request.data['store_id'])
            cashier = Cashier.objects.get(cashier_id=request.data['cashier_id'])
            obj.store = store
            obj.cashier = cashier
            obj.save()
            return Response({"record_id":obj.record_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DailyRecordListByCashier(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self,request,cashier_id):
        records = DailyRecord.objects.filter(cashier__cashier_id=cashier_id,created_on__date=datetime.today()).order_by('record_status','created_on')
        serializer = DailySerializer(records, many=True)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)

class DailyRecordDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get_object(self,record_id):
        try:
            return DailyRecord.objects.get(record_id=record_id)
        except DailyRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,record_id,format=None):
        record = self.get_object(record_id)
        serializer = DailySerializer(record)
        json_data = {}
        json_data['data'] = serializer.data
        return JsonResponse(json_data, safe=False)
    def patch(self,request,record_id,format=None):
        record = self.get_object(record_id)
        try:
            if request.data['cashier'] == 0 or request.data['cashier'] == "0":
                cashier_id = request.data.pop('cashier')
                record.cashier = None
                record.save()
        except:
            pass
        serializer = DailySerializer(record,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Receipt(APIView):
    def post(self,request,record_id):
        record = DailyRecord.objects.get(record_id=record_id)
        message = '<div class="container" style="padding:25px;color:#999;text-align:center;background-color:#f9f9f9;">'
        message+= '<div class="container" style="padding:25px;text-align:left;background-color:white;color:#373D3F;border: .05rem solid #e5e5e5;" align="center">'
        message+= '<h2> ใบเสร็จเก็บยอด ร้าน '+record.store.store_name+'</h2>'
        message+= '<hr />'
        message+= '<p> ยอดเงิน : '+ str(record.record_amount) +'</p>'
        message+= '<p> จำนวนเงิน : '+ str(record.collected_amount) +'</p>'
        message+= '<p> Voucher : '+ str(record.voucher) +'</p>'
        message+= '<p> Credit : '+ str(record.credit) +'</p>'
        message+= '<p> แคชเชียร์ : '+ record.cashier.user.first_name +' '+ record.cashier.user.last_name +'</p>'
        message+= '<p> เวลาเก็บ : '+ record.collect_date.date().strftime('%Y/%m/%d') +'</p>'
        message+= '<p> เวลา : '+ record.created_on.date().strftime('%Y/%m/%d') +'</p>'
        message+= '</div>'
        message+= '<p><small>Siam Retail Development Co., Ltd.'
        message+= '587, 589, 589/7-9 Ramindra Road, Khannayao Bangkok 10230, Thailand.'
        message+= 'T. +66 2947 5000 Fax: +66 2947 5312 Mobile: +66 81 812 5528 '
        message+= 'www.fashionisland.co.th</small></p>'
        message+= '</div>'


        message+= '</div>'
        mail = EmailMessage()
        mail.subject = 'ใบเสร็จเก็บยอดร้าน'+record.store.store_name
        mail.body = message
        mail.from_email = settings.EMAIL_HOST_USER
        mail.to = [record.store.store_email,'phusith.sukt@gmail.com','bagpigham@gmail.com']
        mail.content_subtype = "html"
        try:
            for url in record.signature.all():
                mail.attach_file(url.file.path)
        except FileNotFoundError:
            print('file not found')
        except:
            print('an error occur while attach signature')
        mail.send()
        # send_mail(subject='ใบเสร็จเก็บยอดร้าน'+record.store.store_name,
        #     message='body of the message',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list= [record.store.store_email,'phusith.sukt@gmail.com','bagpigham@gmail.com'],
        #     fail_silently=False,
        #     html_message=message)
        return Response(status=200)

@api_view(['PATCH'])
def forgot_password(request):
    try:
        username = request.data['username']
        print(username)
        user = User.objects.get(username=username)
        print(request.data['password'])
        user.set_password(request.data['password'])
        user.save()
        return Response("Success")
    except User.DoesNotExist:
        return Response({"detail": "Invalid credentials"}, status=401)

class Login(APIView):
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
                    print('payload: ',payload)
                    print('token: ',token)
                    print('response: ',response)
                    cashier = Cashier.objects.get(user_id=user.id)
                    serializer = CashierSerializer(cashier)
                    json_data = {}
                    json_data['data'] = serializer.data
                    return JsonResponse(json_data, safe=False,status=200)    
        return Response({"detail": "Invalid credentials"}, status=401)

class Logout(APIView):
    def get(self,request):
        logout(request)
        if request.user.is_authenticated:
            return Response("Unable to logout",status=401)
        return Response({"success"}, status=200)