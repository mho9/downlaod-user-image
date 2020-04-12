
import requests
import json

def dowload():
    xa =input('Username : ')
    url = 'https://www.instagram.com/'+ xa +'/?__a=1'
    res = requests.get(url)
    if res.status_code ==200:
        data = json.loads(res.text)
        profile = data['graphql'].get('user').get('profile_pic_url_hd')
        image = requests.get(profile)
        src = xa+'.png'
        open(src, 'wb').write(image.content)
    else:
        print('user not found ?!!')
    

while True:
    y_n = input('Start (y/n)?: ')
    if y_n.lower() =='y':
        dowload()
    elif y_n.lower() =='n':
        exit()
    else:
      pass