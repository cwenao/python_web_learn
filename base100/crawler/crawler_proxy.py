from urllib import request
import socket


def get_proxy(url):
    proxy_ip = []
    i_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"}

    try:
        req = request.Request(url, headers=i_headers)
        proxy_con = request.urlopen(req).read()
        proxy_con = proxy_con.decode('utf8')
        proxy_ip = proxy_con.split('\r\n')
    except Exception as e:
        print(e)
    return proxy_ip


def test_proxy(source_ip):
    socket.setdefaulttimeout(6)
    target_url = 'https://www.baidu.com/'
    proxy_ip = []
    try:
        proxy_handler = request.ProxyHandler({"http":source_ip})
        opener = request.build_opener(proxy_handler)
        opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")]
        request.install_opener(opener)
        result = request.urlopen(target_url).read()
        print(result)
        proxy_ip.append(source_ip)
    except Exception as e:
        print(e)

    return proxy_ip


if __name__ == '__main__':
    url = 'http://http-webapi.zhimaruanjian.com/getip?num=25&type=1&pro=0&city=0&yys=0&port=2&pack=960&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1'

    print(test_proxy(get_proxy(url)))

