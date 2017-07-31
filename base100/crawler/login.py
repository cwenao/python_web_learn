from urllib import request, parse


def csdn_login(user_name, passwd):
    values = {}
    values['username'] = user_name
    values['password'] = passwd

    info  = parse.urlencode(values).encode('utf-8')
    url = 'http://passport.csdn.net/account/login'

    try:
        req = request.Request(url, info)
        data = request.urlopen(req).read()
    except Exception as e:
        print('this is the error: ' + e)

    return data


da = csdn_login('aa@126.com', '111111')
print(da)