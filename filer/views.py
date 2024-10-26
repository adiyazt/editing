from django.shortcuts import render
from filer.models import User, File
from django.shortcuts import redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.core.signing import TimestampSigner
import json


API_REQUESTS = []


def authreg(request):
    return render(request, 'authreg.html')
    
    
def api_auth(request):
    request_ = {
        'descrition' : 'Authorization',
        'input' : '',
        'output' : ''
    }
    if request.POST:
        data = request.POST 
        login = data.get('login')
        password = data.get('password')
        request_.update({'input' : {
            'login': login,
            'password' : password
        }})
        if User.objects.filter(login=login, password=password)[0]:
            user = User.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            signer = TimestampSigner()
            request.session['token'] = signer.sign(f'{login}{password}')
            API_REQUESTS.append(request_)
            return redirect('home')
    API_REQUESTS.append(request_)
    return HttpResponse('error')


def api_reg(request):
    request_ = {
        'descrition' : 'Registration',
        'input' : '',
        'output' : ''
    }
    if request.POST:
        data = request.POST 
        login = data.get('login')
        password = data.get('password')
        request_.update({'input' : {
            'login': login,
            'password' : password
        }})
        if not User.objects.filter(login=login, password=password):
            print(0)
            user = User(login=login, password=password)
            user.save()
            request.session['user_id'] = user.id
            signer = TimestampSigner()
            request.session['token'] = signer.sign(f'{login}{password}')
            API_REQUESTS.append(json.dumps(request_))
            return redirect('home')
    API_REQUESTS.append(json.dumps(request_))
    print(API_REQUESTS)
    return HttpResponse('error')


def home(request):
    if request.session.get('user_id'):
        context = {
            'files' : File.objects.filter(user_id=request.session.get('user_id')),
            'user' : User.objects.get(id=request.session.get('user_id'))
        }
        return render(request, 'home.html', context)
    return HttpResponse('error')

def create_file(request, ext=None):
    if ext and request.session.get('user_id'):
        user_id = request.session.get('user_id')
        file = File(user_id=user_id)
        file.save()
        print('created')
        dir = f'filer/static/files/{file.id}.{ext}'
        f = open(dir, 'w', encoding='utf-8')
        file.dir = dir
        file.save()
        return redirect('home')
    
    
def edit_file(request, file_id=None):
    file = File.objects.get(id=file_id)
    with open(f'{file.dir}', 'r') as f:
        content = f.read()
    if request.POST:
        data = request.POST
        content = data.get('content')
        with open(f'{file.dir}', 'w') as f:
            f.write(content)
    context = ({
        'file' : file,
        'content' : content
    })
    return render(request, 'edit_file.html', context)


def delete(request, file_id=None):
    request_ = {
        'descrition' : 'Delete a file',
        'input' : {'file_id' : file_id},
        'output' : ''
    }
    if file_id:
        file = File.objects.get(id=file_id)
        file.delete()
        API_REQUESTS.append(request_)
        return redirect('home')
    API_REQUESTS.append(request_)
    return HttpResponse('error')


def download(request, file_id=None):
    request_ = {
        'descrition' : 'Delete a file',
        'input' : {'file_id' : file_id},
        'output' : ''
    }
    if file_id:
        file = File.objects.get(id=file_id)
        request_.update({'output' : {'file' : f'file at {file.dir}'}})
        API_REQUESTS.append(request_)
        return FileResponse(open(f'{file.dir}', 'rb'), as_attachment=True)
    API_REQUESTS.append(request_)
    return HttpResponse('error')


def tables(request):
    files = File.objects.all()
    users = User.objects.all()
    context = {
        'files': files,
        'users': users,
    }
    return render(request, 'tables.html', context)


def api_requests(request):
    return JsonResponse({'result':  API_REQUESTS})