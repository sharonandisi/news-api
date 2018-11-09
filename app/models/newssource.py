class Newssource:
    '''
    Newssource class to define Newssource Objects
    '''

    def __init__ (self,id, name, urlToImage, publishedAt,url):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url