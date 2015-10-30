__author__ = 'Canon'

from app import db
from ..models import Relationship, Article, Tag
from ..models import Relationship, Tag

def registerArticle(article_url_title, tagList):
    for tag in tagList:
        relationship = Relationship(article_url_title=article_url_title, tag_name=tag)
        db.session.add(relationship)
    db.session.commit()

def getTagsByUrlTitle(article_url_title):
    relationships = Relationship.query.filter_by(article_url_title=article_url_title).all()
    tagList = []
    for r in relationships:
        tagList.append(r.tag_name)
    return tagList





def addTags(tagList):
    Tag.addTags(tagList)

