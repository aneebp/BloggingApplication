from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password1']
