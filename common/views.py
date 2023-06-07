from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def toIndex_view(request):
    return render(request, 'index.html')

def toCommittee_view(request):
    return render(request, 'committee.html')

def toProgram_view(request):
    return render(request, 'program.html')

def toSubmission_view(request):
    return render(request, 'submission.html')