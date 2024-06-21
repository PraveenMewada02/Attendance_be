from django import forms

from attend_app.models import Email_Data

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField()


# class EmailDataForm(forms.Form):
    
#         model = Email_Data
#         fields = ['empcode', 'email', 'name']