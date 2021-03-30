from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse , HttpResponseRedirect
import requests
from bs4 import BeautifulSoup

def logout(request):
    response = HttpResponseRedirect('/index/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        u = request.POST.get('uu')
        p = request.POST.get('pp')
        r =  requests.post('https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp?t_tea_no=08360903&t_tea_pass=andy900629')
        url = 'https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        data = {
            't_tea_no':u,
            't_tea_pass':p,
        }
        login_in = requests.post(url, headers = headers, data = data)
        response = HttpResponseRedirect('/test/')
        for k in login_in.cookies:
           response.set_cookie(k.name,k.value)
           print(k.name,k.value)
        return response

def test(request):
    r =  requests.post('https://www.mcu.edu.tw/student/new-query/default.asp',cookies=request.COOKIES)
    r.encoding = 'big5'
    soup = BeautifulSoup(r.text,"html.parser")
    course_list = soup.select('#___01 > tr:nth-of-type(4) > td:nth-of-type(1) > table > tr:nth-of-type(2) > td > table:nth-of-type(1) > tr')
    l = []
    for course in course_list:
        l.append(course.select('td:nth-of-type(2) > a')[0].text) 
    return render(request, 'test.html', {
        'course_list': l,
    }) 
    return render(request,'test.html')
