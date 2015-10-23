__author__ = 'Canon'

from app import db
from ..models import Relationship, Tag

def registerArticle(article_url_title, tagList):
    for tag in tagList:
        relationship = Relationship(article_id=article_id, tag_name=tag)
        db.session.add(relationship)
    db.session.commit()



def addTags(tagList):
    Tag.addTags(tagList)
