__author__ = 'Canon'
import hashlib
from PIL import Image
from StringIO import StringIO
from models import Tag

def generateArticleId(timestamp, urlTitle):
    pass

def generateCommentId(timestamp, username, articleId):
    pass

def generateTitleUrl(title):
    pass

def allowed_file(filename):
    return True

def generate_blog_url(create_time, title):
    title_str = ''
    if isinstance(title, unicode):
        title_str = title.encode('utf8')
    elif isinstance(title, str):
        title_str = title

    prefix = create_time.strftime('%Y%m%d%H')
    minsec = create_time.minute * 60 + create_time.second

    if not title_str:
        t = 987
    else:
        s = 0
        for ch in title_str:
            s += ord(ch)
        t = s % 1000

    suffix = str(minsec) + str(t)

    return (prefix + "-" + suffix)

def generate_blog_comment_id(create_time, user_id, blog_title):
    prefix = create_time.strftime('%d%H%M%S')
    suffix1 = blog_title[-3:]
    if not user_id:
        suffix2 = 'annoy'
    else:
        suffix2 = str(user_id)

    return prefix + "-" + suffix1 + suffix2


def generate_blog_stat_id(article_id, ip):
    pass

def crop_save_img(filename, data, x1, y1, x2, y2):
    imgIO = StringIO(data)
    img = Image.open(imgIO)
    croped_img = img.crop((x1, y1, x2, y2))
    dot_pos = filename.rfind('.')
    absfilename = filename[:dot_pos]
    croped_img.save(absfilename+'.jpg', 'JPEG')


def addTagsIfNecessary(tagList):
    Tag.addTags(tagList)



