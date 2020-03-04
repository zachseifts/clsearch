''' A search query object.

'''

from craigslist import CraigslistForSale

class Query:
    ''' A query object.
    '''

    def __init__(self, **kwargs):
        self.category = kwargs.get('category', 'sss')
        self.sites = kwargs.get('sites', list())
        self.query = kwargs.get('query', '') 
        self.results = list()

    def get_filters(self):
        ''' This function gets the filters for a search.
        '''
        return {
            'query': self.query
        }
        
    def search(self):
        ''' This function searches Craiglist for criteria defined above.
        '''
        for site in self.sites:
            results = CraigslistForSale(site=site,category=self.category, filters=self.get_filters())
            for result in results.get_results():
                self.results.append(result)

    def get_results(self):
        ''' Returns a list of results.
        '''
        return self.results

