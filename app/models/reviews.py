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
        Comments.all_reviews.clear()