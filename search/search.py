''' A Search class.
'''

from craigslist import CraigslistForSale

class Search:
    ''' This class searches Craigslist for information contained in a Query
    object.

    >>> from query import Query
    >>> query = Query(category='sss', sites=['boone'], query='foo')
    >>> s = Search(query=query)
    >>> s.get_results()
    []
    >>> s.query.get_filters()
    {'query': 'foo'}
    '''

    def __init__(self, **kwargs):
        self.query = kwargs.get('query', None)
        self.results = list()

    def run(self):
        ''' This function searches Craiglist for criteria defined above.
        '''
        for site in self.query.sites:
            results = CraigslistForSale(site=site,
                category=self.query.category,
                filters=self.query.get_filters())
            for result in results.get_results():
                self.results.append(result)

    def get_results(self):
        ''' Returns a list of results.
        '''
        return self.results


if __name__ == '__main__':
    import doctest
    doctest.testmod()

