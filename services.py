__author__ = 'Canon'


def getNestedComments(commentList):
    resultList = []
    commentMap = {}
    for comment in commentList:
        comment.children = []
        print comment.id, comment.parentCmt_id
        commentMap[comment.id] = comment
        if comment.parentCmt_id is None:
            resultList.append(comment)

    for comment in commentList:
        parent_id = comment.parentCmt_id
        if parent_id:
            commentMap[parent_id].children.append(comment)

    return resultList


