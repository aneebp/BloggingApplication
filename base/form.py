from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

class SignUpCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password1']


class Updateuser(ModelForm):
    class Meta:
        model = User
        fields = ['name','username','email','bio','avatar']