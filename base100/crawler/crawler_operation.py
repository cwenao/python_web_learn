from urllib import request
import re
from base100.crawler.model import model
from base100.crawler import db_operation
from multiprocessing.dummy import Pool


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


def data_douban_provider_list():
    '''
    豆瓣电影列表
    :return:
    '''
    target_url = 'https://read.douban.com/provider/all'
    pat = '<div class="name">(.*?)</div>'
    ret = data_capture_common(target_url, pat)
    session = db_operation.get_session()
    session.execute(model.ProviderInfo.__table__.insert(), [{'provider_name': x} for x in ret])
    session.commit()


def data_multi_douban_provider_list():
    '''
    多线程
    :return:
    '''
    pool = Pool(4)
    target_url = 'https://read.douban.com/provider/all'
    pat = '<div class="name">(.*?)</div>'
    ret = data_capture_common(target_url, pat)
    session = db_operation.get_session()
    session.execute(model.ProviderInfo.__table__.insert(), [{'provider_name': x} for x in ret])
    session.commit()
    pool.close()
    pool.join()


if __name__ == '__main__':
    #data_douban_provider_list()
    data_multi_douban_provider_list()