from app import app
import urllib.request,json
from .models import source

Source = source.Source
#getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to the url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)

    return source_results

    def process_results(source_list):
        """
        Function that processes the source result and transform them to a list of Objects

        Args:
            source_list: A list of dictionaries that contain source details

        Returns :
            source_results: A list of source objects
        """
        source_results = []
        for source_item in source_list:
            id = source_item.get('id')
            name = source_item.get('name')
            urlToImage = source_item.get('urlToImage_path')
            publishedAt = source_item.get('publishedAt')
            url = source_item.get ('url')

            if poster:
                source_object = Source(id,name,urlToImage,publishedAt,url)
                source_results.append(source.object)
    return source_results

    def get_source(id):
        get_source_details_url = base_url.format(id,api_key)

        with urllib.request.urlopen(get_source_details_url) as url:
            source_details_data = url.read()
            source_details_response = json.loads(source_details_data)
            source_object = None
            if source_details_response:
                id = source_details_response.get('id')
                name = source_details_response.get('name')
                urlToImage = source_details_response.get('urlToImage')
                publishedAt = source_details_response.get('publishedAt')
                url = source_details_response.get ('url')
                source_object = Source(id,name,urlToImage,publishedAt,url)
    return source_object
