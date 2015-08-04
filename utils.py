__author__ = 'Canon'
import hashlib

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
    minsec = create_time.minute * 60 + create_time.second + (create_time.microsecond % 1000)

    if not title_str:
        t = 987
    else:
        s = 0
        for ch in title_str:
            s += ord(ch)
        t = s % 1000

    suffix = str(minsec) + str(t)

    return (prefix + suffix)