
import sys
import requests
import pickle

from utils import to_base, pad_list, n_to_imgur, imgur_to_n


class ImgurIterator(object):

    count = 0
    results = None
    verbose = 0
    name = 'None'

    def __init__(self,name):
        self.count = 0
        self.results = {}
        self.name = '%s' % str(name)

    def _get_imgur_str(self):
        return utils.n_to_imgur(num)


    def get_next(self):

        imgur_str = utils.n_to_imgur(self.count)
        url = 'http://i.imgur.com/%s.png' % imgur_str
        resp = requests.head(url)
        results[self.count] = resp.headers

        self.count += 1

    def set_position(self, pos):
        self.count = pos

    def get_imgur(self,num):
        imgur_str = n_to_imgur(num)
        url = 'http://i.imgur.com/%s.png' % imgur_str
        resp = requests.head(url)
        if self.verbose:
            print '%s\t%d\t%d\t%s\t%s' % (self.name, len(self.results), self.count, resp.url, resp.status_code)
        self.count += 1
        self.results[imgur_str] = resp.headers

    def save_results(self,filepath):
        pickle.dump(self.results,open(filepath,'w'))

    def clear_results(self):
        self.results = {}
        self.count = 0

    def compute_range(self,start,stop):
        for i in range(start, stop):
            try:
                self.get_imgur(i)
            except Exception, e:
                print str(e)
                print 'sleeping for 5 seconds...'

