class Source:
    '''
    source class to define source Objects
    '''

    def __init__ (self,id, name, urlToImage, publishedAt,url):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url

class Comment:
    all_comments = []

    def __init__(self,id,name,urlToImage,comment):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.comment = comment

    def save_review(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comments.all_comments.append(self)

    @classmethod
    def clear_reviews(cls):
        Comments.all_comments.clear()
    @classmethod
    def get_comments(cls,id):
        response = []

        for comment in cls.all_comments:
            if comment.source_id == id:
                response.append(comment)
        return response