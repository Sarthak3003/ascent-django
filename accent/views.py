from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import tensorflow as tf

class call_model(APIView):

    def get(self,request):
        if request.method == 'GET':
            
            new_model = tf.keras.models.load_model('model')
            results = new_model.evaluate('indian_s01_001_0','indian')
            tf.print('Accuracy: ', results[1]*100)
            
            # returning JSON response
            return JsonResponse(results)