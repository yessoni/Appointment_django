from django.contrib.sessions.models import Session


# Session model stores the session data
from django.contrib.sessions.models import Session
from .models import LoggedInUser


class OneSessionPerUser:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            session_key = request.session.session_key

            # if there is a stored_session_key  in our database and it is
            # different from the current session, delete the stored_session_key
            # session_key with from the Session table
            try:
                logged_in_user = request.user.logged_in_user
                stored_session_key = logged_in_user.session_key
                # stored_session_key exists so delete it if it's different
                if stored_session_key != session_key:
                    Session.objects.filter(session_key=stored_session_key).delete()
                logged_in_user.session_key = session_key
                logged_in_user.save()
            except LoggedInUser.DoesNotExist:
                LoggedInUser.objects.create(user=request.user, session_key=session_key)

        response = self.get_response(request)

        return response