from django.http import HttpResponse
from django.shortcuts import render

def mi_error_404(request, exception):
    return render(request,'Aplicacion/error_404.html')





    
