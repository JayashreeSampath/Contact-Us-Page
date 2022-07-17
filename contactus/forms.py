from django import forms
class details(forms.Form):
    Name=forms.CharField(max_length=200)
    Mail=forms.EmailField(max_length=200)
    Sub=forms.CharField(max_length=200)
    Msg=forms.CharField(max_length=1000)