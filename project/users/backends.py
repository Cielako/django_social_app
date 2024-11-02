from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class UsernameOrEmailBackend(ModelBackend):
    """
    Custom authentication backend to allow login using either username or email.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            # Try to get the user by either username or email
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
        except UserModel.DoesNotExist:
            return None

        # Check if the provided password is correct and if the user is allowed to authenticate
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None  # Return None if authentication failed