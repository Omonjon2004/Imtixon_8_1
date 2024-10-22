from functools import wraps

def is_owner_maintainer(f):
    @wraps(f)
    def wrapped(self, *args, **f_kwargs):
        request_user = args[1].context.user
        if request_user.role != "Maintainer":
            raise Exception("You don't have permission for this action")
        return f(self, *args, **f_kwargs)
    return wrapped

def is_owner_developer(f):
    @wraps(f)
    def wrapped(self, *args, **f_kwargs):
        request_user = args[1].context.user
        if request_user.role != "Developer" and request_user.role != "Maintainer":
            raise Exception("You don't have permission for this action")
        return f(self, *args, **f_kwargs)
    return wrapped