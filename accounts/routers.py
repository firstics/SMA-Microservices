import random

class AuthRouter:
    
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'accounts':
            return random.choice(['default', 'authen-replica'])
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'accounts':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'accounts' or \
           obj2._meta.app_label == 'accounts':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True

class ServiceRouter:
    
    def db_for_read(self, model, **hints):
        return random.choice(['service-primary', 'service-replica-1', 'service-replica-2'])

    def db_for_write(self, model, **hints):
        return 'default'


    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'authen-replica', 'service-primary', 'service-replica-1', 'service-replica-2')
        if obj1._state.db in db_list and obj2._state.db in db_list:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True