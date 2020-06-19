from django.contrib.auth.forms import UserCreationForm
from Insta.models import InstaUser


class InstaUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ['username', 'profile_pic']
