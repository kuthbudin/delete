from django import forms
import re
from fviews.models import RegistrationModel


class StudentRegistrationForm(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistrationModel
        fields = '__all__'
        #exclude = ['contact']
    """
    
    def clean(self):
        all_data = super().clean()
        #all_data = self.cleaned_data
        print("ready...", all_data['password'])
        print("ready...", all_data['repassword'])
        if all_data['password'] != all_data['repassword']:
            print("Error....")
            raise forms.ValidationError("Password match error")
    """
    def clean_name(self):
        all_data = self.cleaned_data
        if not re.search(r"^[A-Z]", all_data['name']):
            raise forms.ValidationError("Invalid name")

        return all_data['name']

    """
    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.search(r"^[A-Z]", name):                raise forms.ValidationError("Invalid name")
        return None
    """

class StudentRegistrationFormx(forms.Form):
    roll_no = forms.IntegerField()
    name = forms.CharField(max_length=10)
    classno = forms.CharField()
    contact = forms.IntegerField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.search(r"^[A-Z]", name):
            raise forms.ValidationError("Invalid name")
        return name

    def clean_classno(self):
        classno = self.cleaned_data['classno']
        if not re.search(r"^[0-9]$", classno):
            raise forms.ValidationError("Invalid name")
        return classno