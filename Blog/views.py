from django.http import JsonResponse
from django.shortcuts import render
import requests

def home(request):
    response_data = get_threads(request)
    threads = response_data.get('threads', [])
    return render(request, 'index.html', {'threads': threads})

def register_view(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Prepare data for the API request
        data = {
            "username": username,
            "email": email,
            "displayName": "string",
            "password": password,
            "emailVerified": True,
            "image": "string",
            "roles": ["string"],
            "bio": "string",
            "signature": "string",
            "url": "string",
            "extendedData": {}
        }

        

        # API endpoint
        url = 'https://foru-ms.vercel.app/api/v1/user'

        # Add the API key and Bearer token to the request headers
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
            "Authorization": "Bearer 123"
        }

        # Make the request to the API with the headers
        response = requests.post(url, json=data, headers=headers)

        #print(response.json())

        # Check if the request was successful
        if response.status_code == 201:
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse({'error': 'Registration failed'}, status=response.status_code)

    else:
        return render(request, 'login.html')
    # Render the registration form template


def login_view(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('login-email')
        
        password = request.POST.get('login-password')

        # Prepare data for the API request
        url = "https://foru-ms.vercel.app/api/v1/auth/login"

        payload = {
            "login": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
            "Authorization": "Bearer 123"
        }

        response = requests.post(url, json=payload, headers=headers)

        #print(response.json())

        request.session['token'] = response.json()['token']

        token = token = request.session.get('token', None)

        print(token)

        # Check if the request was successful
        if response.status_code == 200:
            response_data = get_threads(request)
            threads = response_data.get('threads', [])
            return render(request, 'index.html', {'threads': threads})
        else:
            return JsonResponse({'error': 'Login failed'}, status=response.status_code)

    else:
        return render(request, 'login.html')
    # Render the registration form template


def get_threads(request):
    url = "https://foru-ms.vercel.app/api/v1/threads"

    token = token = request.session.get('token', None)

    headers = {
        "Accept": "application/json",
        "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

    #print(response.json())

    return response.json()

def get_userId(token):
    url = "https://foru-ms.vercel.app/api/v1/auth/me"

    headers = {
        "Accept": "application/json",
        "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

    #print(response.json())

    return response.json()['id']



def new_thread(request):
    if request.method == 'POST':
        # Retrieve form data

        title = request.POST.get('title')
        
        body = request.POST.get('body')

        token = request.session.get('token', None)

        userId=get_userId(token)



        url = "https://foru-ms.vercel.app/api/v1/thread"

        payload = {
            "title": title,
            "slug": "string",
            "body": body,
            "userId": userId,
            "locked": True,
            "pinned": True,
            "tags": ["string"],
            "poll": {
                "title": "string",
                "options": [
                    {
                        "color": "string",
                        "title": "string",
                        "extendedData": {}
                    }
                ]
            },
            "extendedData": {}
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
            "Authorization": "Bearer 123"
        }

        response = requests.post(url, json=payload, headers=headers)

        #print(response.json())

        # Check if the request was successful
        if response.status_code == 201:
            response_data = get_threads(request)
            threads = response_data.get('threads', [])
            return render(request, 'index.html', {'threads': threads})
        else:
            return JsonResponse({'error': 'Thread Failed '}, status=response.status_code)

    else:
        return render(request, 'new-thread.html')
    # Render the registration form template

def search_threads(request):
    
    search = request.GET.get('search')

    print(search)

    url = "https://foru-ms.vercel.app/api/v1/threads"

    querystring = {"query":search}

    token = request.session.get('token', None)

    headers = {
        "Accept": "application/json",
        "x-api-key": "8271a51f-053c-4609-8c1b-1c70c77362c9",
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    if response.status_code == 200:
            threads = response.json().get('threads', [])
            return render(request, 'index.html', {'threads': threads})
    else:
        return JsonResponse({'error': 'Thread Failed '}, status=response.status_code)