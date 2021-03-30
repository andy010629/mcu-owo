import requests
from bs4 import BeautifulSoup

def StuLogin(uu,pp):
    r =  requests.post('https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp?t_tea_no=08360903&t_tea_pass=andy900629')
    url = 'https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    data = {
        't_tea_no':uu,
        't_tea_pass':pp,
    }
    login_in = requests.post(url, headers = headers, data = data)
    cookies = login_in.cookies
