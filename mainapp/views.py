
from django.shortcuts import render
import time
import json
import base64
import io
#import HotsNeural.neuralmodels as NM


def home(request):
    return render(request, 'index.html')

def analyzeGeoProg(request):
    return "Done"