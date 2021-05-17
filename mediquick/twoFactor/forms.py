from django import forms

class Send_Mail(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email