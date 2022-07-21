from django.contrib.auth.backends import ModelBackend

from .models import User

class UserAuthenticationBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        print("yes")
        user = None
        if kwargs["registered_by"] == "manual":
            email = kwargs["email"]
            password = kwargs["password"]
            registered_by = kwargs["registered_by"]

            try:
                user = User.objects.get(email=email, password=password, registered_by=registered_by)
            except User.DoesNotExist:
                user = None
        else:
            email = kwargs["email"]
            social_id = kwargs["social_id"]
            registered_by = kwargs["registered_by"]

            try:
                user = User.objects.get(email=email, social_id=social_id, registered_by=registered_by)
            except User.DoesNotExist:
                user = None
        return user

        # customer_id = kwargs['username']
        # password = kwargs['password']
        # try:
        #     customer = Customer.objects.get(customer_id=customer_id)
        #     if customer.user.check_password(password) is True:
        #         return customer.user
        # except Customer.DoesNotExist:
        #     pass