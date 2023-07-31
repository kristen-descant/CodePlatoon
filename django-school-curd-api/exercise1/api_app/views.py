from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from dotenv import dotenv_values
from django.http import Http404

# Create your views here.
class Noun_Project(APIView):

    def get(self, request, subject):
        try:
            env = dotenv_values('.env')
            my_api = env.get('apikey')
            secretkey = env.get('secretkey')
            auth = OAuth1(my_api, secretkey)
            endpoint = f'http://api.thenounproject.com/icon/{subject}'
            response = requests.get(endpoint, auth=auth)
            responseJSON = response.json()
            return Response(responseJSON['icon']['preview_url'])
        except KeyError:
            raise Http404("Subject not found.")