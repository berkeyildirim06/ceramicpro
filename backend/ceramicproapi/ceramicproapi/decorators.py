from functools import wraps
from django.utils.decorators import method_decorator

def skip_api_key_auth(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    wrapped_view.skip_api_key_auth = True
    return wrapped_view