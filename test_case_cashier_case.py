# import time
# from record.models import Cashier
# from accounts.models import User
# from record.serializers import *

# user = User.objects.create_user(username='username1',
#     password='password',
#     first_name='demo',
#     last_name='test')
# cashier, created = Cashier.objects.update_or_create(user=user)

# user = User.objects.get(first_name="demo")
# cashier = Cashier.objects.get(user=user)
# assertEqual(cashier.user.first_name, 'demo')
# assertEqual(cashier.user.last_name, 'test')