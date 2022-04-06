from django.shortcuts import render
import requests
import json
# Create your views here.
def advices(request):
    
    url = "https://api.adviceslip.com/advice"

    
    response = requests.request("GET", url)
    response = json.loads(response.text)
    response = response['slip']['advice']
    return render(request, 'advices.html', {'response': response})


def facts(request):
    
    url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

    headers = {
	    "X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com",
	    "X-RapidAPI-Key": "b0a49fe713msh0950a0a845c0429p18aeb1jsn5a58af259d69"
        }

    response = requests.request("GET", url, headers=headers)

    response = json.loads(response.text)
    response = response[0]['fact']
    return render(request, 'facts.html', {'response': response})


def jokes(request):


    url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"
    headers = {
	    "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
	    "X-RapidAPI-Key": "b0a49fe713msh0950a0a845c0429p18aeb1jsn5a58af259d69"
}

    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)
    response = response[0]['joke']
    return render(request, 'jokes.html', {'response': response})


def quotes(request):
    
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
	    "key2": "value"
        }
    headers = {
        "content-type": "application/json",
	    "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
	    "X-RapidAPI-Key": "b0a49fe713msh0950a0a845c0429p18aeb1jsn5a58af259d69"
        }
    response = requests.request("POST", url, json=payload, headers=headers)

    return render(request, 'quotes.html', {'response': response})

