from urllib import request
import re


def data_capture_common(target_url, pat):
    '''
    公共抓取方法
    :param target_url:
    :param pat:
    :return:
    '''

    data = request.urlopen(target_url).read()
    resolver_concent = re.compile(pat).findall(str(data, 'utf8'))
    return resolver_concent


def data_douban_movie_list():
    '''
    豆瓣电影列表
    :return:
    '''
    target_url = 'https://read.douban.com/provider/all'
    pat = '<div class="name">(.*?)</div>'
    ret = data_capture_common(target_url, pat)
    for x in ret:
        print(x)


if __name__ == '__main__':
    data_douban_movie_list()