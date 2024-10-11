from .models import PDFDocument
from django import forms

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'content']