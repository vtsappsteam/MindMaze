from django.shortcuts import render, redirect
from .models import PDFDocument
from .forms import PDFDocumentForm

def pdf_document_create(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new PDFDocument to the database
            return redirect('api:pdf_document_list')  # Use 'api:' prefix since you have app_name
    else:
        form = PDFDocumentForm()
    
    return render(request, 'api/pdf_document_create.html', {'form': form})

def index(request):
    return render(request, 'api/index.html')

def pdf_document_list(request):
    documents = PDFDocument.objects.all()
    return render(request, 'api/pdf_document_list.html', {'documents': documents})
