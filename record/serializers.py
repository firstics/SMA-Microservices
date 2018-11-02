from rest_framework import serializers
from accounts.models import User
from record.models import Cashier, Photo, DailyRecord, Manager, Store, Signature

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','tel')

class CashierSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Cashier
        fields = ('user','cashier_id','created_on')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        #get user json
        #user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user = User.objects.create_user(username=user_data['username'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            tel=user_data['tel'])
        #user.is_staff=True
        #user.save()
        cashier, created = Cashier.objects.update_or_create(user=user)
        return cashier

class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Manager
        fields = ('user','manager_id','created_on')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_id','store_name','store_email','contract_type','store_detail',
                'store_facility','created_on')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id','file','description','created_on')

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ('id','file','created_on')

class DailySerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    class Meta:
        model = DailyRecord
        fields = ('record_id','store','cashier','record_status','verify_status','verified_by','verified_date',
            'record_amount','collected_amount','voucher','assigned_by','number_of_1000','number_of_500','number_of_100',
            'number_of_50','number_of_20','number_of_10','number_of_5','number_of_2','number_of_1',
            'number_of_50_satang','number_of_25_satang','collect_date','created_on','receipts','note','credit'
)