from django.shortcuts import render
import boto3
from django.http import HttpResponse
import os
from decouple import config

# Create your views here.

def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')


def test_upload(request):
    s3 = boto3.client(
        's3',
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
        region_name='eu-north-1'
    )
    # Upload a sample file to test
    with open('static/test_file.txt', 'rb') as data:
        s3.upload_fileobj(data, 'boutiqueadowt', 'static/test_file.txt')
    return HttpResponse('File uploaded successfully.')