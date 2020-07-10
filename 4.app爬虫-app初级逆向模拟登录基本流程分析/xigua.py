#coding:utf8
import time
import requests

HEADERS = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; OPPO R11 Plus Build/NMF26X) VideoArticle/6.3.3 okhttp/3.7.0.6',
    'Host': 'security.snssdk.com',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

def encrypt(_string):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
      'a', 'b', 'c', 'd', 'e', 'f']
    bstr = bytes(_string,'utf8')
    arrayOfByte = [i ^ 0x5 for i in bstr]
    arrayOfChar = []
    j = 0
    for i in arrayOfByte:
        k = int(i & 0xFF)
        m = j + 1
        arrayOfChar.insert(j,a[k >> 4])
        j = m + 1
        arrayOfChar.insert(m,a[k & 0xF])
    return ''.join(arrayOfChar)

def send_code(phone):
    ts = time.time()
    mobile = encrypt(str(phone))
    api = 'https://security.snssdk.com/passport/mobile/send_code/?' \
          'ac=wifi' \
          '&channel=wandoujia' \
          '&aid=32' \
          '&app_name=video_article' \
          '&version_code=633' \
          '&version_name=6.3.3' \
          '&device_platform=android' \
          '&ssmix=a' \
          '&device_type=OPPO+R11+Plus' \
          '&device_brand=OPPO' \
          '&language=zh' \
          '&os_api=22' \
          '&os_version=5.1.1' \
          '&manifest_version_code=233' \
          '&resolution=1600*900' \
          '&dpi=320' \
          '&update_version_code=6332' \
          f'&_rticket={int(ts*1000)}' \
          '&fp=a_fake_fp'
    data = 'mix_mode=1' \
           '&type=3730' \
           '&unbind_exist=35' \
           f'&mobile={mobile}' \
           '&ac=wifi&channel=wandoujia&aid=32&app_name=video_article&version_code=633&version_name=6.3.3' \
           '&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus' \
           '&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&manifest_version_code=233' \
           f'&resolution=1600*900&dpi=320&update_version_code=6332&_rticket={int(ts*1000)}&fp=a_fake_fp'
    response = requests.post(api,data=data,headers=HEADERS,verify=False)
    print(response.text)

def login(phone,code):
    ts = time.time()
    mobile = encrypt(str(phone))
    code = encrypt(str(code))
    api = 'https://security.snssdk.com/passport/mobile/sms_login/?' \
          '&ac=wifi' \
          '&channel=wandoujia' \
          '&aid=32&app_name=video_article&version_code=633&version_name=6.3.3&device_platform=android' \
          '&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh' \
          '&os_api=22&os_version=5.1.1' \
          '&manifest_version_code=233' \
          '&resolution=1600*900' \
          f'&dpi=320&update_version_code=6332&_rticket={int(ts*1000)}&fp=a_fake_fp'
    data = f'mix_mode=1&code={code}&mobile={mobile}' \
           '&ac=wifi&channel=wandoujia&aid=32&app_name=video_article&version_code=633&version_name=6.3.3&device_platform=android' \
           '&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1' \
           f'&manifest_version_code=233&resolution=1600*900&dpi=320&update_version_code=6332&_rticket={int(ts*1000)}&fp=a_fake_fp'
    response = requests.post(api,data=data,headers=HEADERS,verify=False)
    print(response.text)
    print(response.headers)
    print(response.cookies)

if __name__ == '__main__':
    # print(encrypt('19965412404'))#343c3c3330313437313531
    phone = '18866478504'
    code = '9596'
    # send_code(phone)
    login(phone,code)