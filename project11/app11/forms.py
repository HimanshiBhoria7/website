from django import forms
from django.core import validators
from app11.models import Student,Lip_Product

class Homeform(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)


class Studentform(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    rollnumber = forms.IntegerField
    email = forms.EmailField
    feedback = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput,label="Re-enter the password")

    def clean(self):
        print('Validation form')
        total_clean_data =super().clean()
        fpwd = total_clean_data['password']
        rpwd = total_clean_data['rpassword']
        if(fpwd!=rpwd):
            print('Password Entered is not correct')

class Formstudent(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'

class Lip(forms.ModelForm):
    class Meta():
        model = Lip_Product
        fields = '__all__'