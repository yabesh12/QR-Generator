import threading

_user = threading.local()

class CurrentUserMiddleware:
    """
    Middleware to store the currently logged-in user in a thread-local variable.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, "user") and request.user.is_authenticated:
            _user.value = request.user
        else:
            _user.value = None

        response = self.get_response(request)
        return response

def get_current_user():
    """Helper function to get the stored user"""
    return getattr(_user, "value", None)
