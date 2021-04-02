from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse , HttpResponseRedirect ,JsonResponse
import requests
import json
from bs4 import BeautifulSoup

# Create your views here.

def get_curriculum(request):
    islogin = 'std%5Fenm' in request.COOKIES
    if islogin:
        r =  requests.post('https://www.mcu.edu.tw/student/new-query/sel-5-3.asp?d=2',cookies=request.COOKIES)
        r.encoding = 'big5'
        soup = BeautifulSoup(r.text,"html.parser")
        soup = soup.select('body > div > p > center')[0]
        # soup.find("table")['class'] = "responsive-table"
        for td_tag in soup.find_all("td"):
            td_tag['width'] = ""
            td_tag['height'] = ""
        content = (soup)
        
    # return JsonResponse({'status': 'Get posts succeed', 'content': content})
    return HttpResponse(content)