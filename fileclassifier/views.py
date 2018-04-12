from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
import json
import zlib
import base64


#Base view for first page re-direction
def base_view(request):
	return render(request, 'fileclassifier/input_view.html', {'prediction':'Processing not initiated...'})

#request handler and processor
def get_response(request):
	context = {}
	data = request.POST.get('data')
	context['prediction'] = 'Processing not initiated...'

	#if data is blank throw error
	if not data:
		context['error'] = 'Please enter valid words data!'
		context['prediction'] = 'Error Encounter while processing...'
		return render(request, 'fileclassifier/input_view.html', context)

	#process API calls and build output
	try:
		data1 = str.encode(data)
		enc_data =  base64.b64encode(zlib.compress(data1,9))

		url = 'https://rb2pqd7dte.execute-api.us-east-2.amazonaws.com/dev'
		#url = 'http://localhost:5000'
		param = {"words": enc_data.strip()}
		headers = {'content-type': "application/json"}
		api_response = requests.get(url, params=param, headers=headers)
		print(api_response)
		print(api_response.content.decode())
		print(api_response.content)
		testres = json.loads(api_response.content)

		#set output
		context['prediction'] = testres['prediction']
		return render(request, 'fileclassifier/input_view.html', context)
	except Exception as e:
		context['prediction'] = 'Error Encounter while processing...'
		context['error'] = str(e)
		return render(request, 'fileclassifier/input_view.html', context)