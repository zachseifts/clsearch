''' A Query class.
'''

class Query:
    ''' This class defines a query that can be used along with a Search
    object to search for listings on Craigslist.
    '''

    def __init__(self, **kwargs):
        self.category = kwargs.get('category', 'sss')
        self.sites = kwargs.get('sites', list())
        self.query = kwargs.get('query', '') 

    def get_filters(self):
        ''' This function gets the filters for a search.

        >>> query = Query(query='foo')
        >>> query.get_filters()
        {'query': 'foo'}
        '''
        return {
            'query': self.query
        }


if __name__ == '__main__':
    import doctest
    doctest.testmod()

