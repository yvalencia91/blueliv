from db import db


class ThreatModel(db.Model):

    __tablename__ = 'threats'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    topic = db.Column(db.String(500))
    post_date = db.Column(db.String(25))

    def __init__(self, author, topic, post_date):
        self.author = author
        self.topic = topic
        self.post_date = post_date

    def json(self):
        return {
            'author': self.author,
            'topic': self.topic,
            'post_date': self.post_date
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
