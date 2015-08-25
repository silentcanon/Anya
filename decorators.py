__author__ = 'Canon'
from functools import wraps
from flask import abort
from flask.ext.login import current_user
from models import Permission

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def dec_func(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return dec_func
    return decorator

def permission_required_json(permission):
    def decorator(f):
        @wraps(f)
        def dec_func(*args, **kwargs):
            if not current_user.can(permission):
                return {'success': False, 'error': 'Authorization Failed'}
            return f(*args, **kwargs)
        return dec_func
    return decorator

def admin_required_json(f):
    return permission_required_json(Permission.ROOT)(f)

def admin_required(f):
    return permission_required(Permission.ROOT)(f)