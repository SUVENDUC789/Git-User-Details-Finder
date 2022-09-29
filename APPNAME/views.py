import requests
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request,'search.html')

    if request.method == "POST":
        username=request.POST.get('username','default')
        # username = 'SUVENDUC789'

        api = f'https://api.github.com/users/{username}'
        data = requests.get(api)
        data = data.json()

        # print(data)
        try:
            repos_url = f'https://api.github.com/users/{username}/repos'
            repo = requests.get(repos_url)
            repo = repo.json()
            p = {
                    'username': data['login'],
                    'avatar': data['avatar_url'],
                    'link': data['html_url'],
                    'name': data['name'],
                    'location': data['location'],
                    'bio': data['bio'],
                    'repository': data['public_repos'],
                    'followers': data['followers'],
                    'following': data['following'],
                    'create_date': data['created_at'].split('T')[0],
                    'update_date': data['updated_at'].split('T')[0],
                    'repolist':repo,
            }
            return render(request, 'home.html', p)
        except:
            # return HttpResponse("Nor result found ...")
            return render(request, 'noresult.html', {'name':username})
