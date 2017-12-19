from django import forms
from django.contrib.auth import (
    authenticate,get_user_model,
    login,logout,
)


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            user_qs = User.objects.filter(username=username)

            if user_qs.count == 1:
                user = user_qs.first()

            if not user:
                raise forms.ValidationError("User Doesn't Exist")

            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")

            if not user.is_active:
                raise forms.ValidationError("User is not active")

        return super(UserLoginForm,self).clean()

