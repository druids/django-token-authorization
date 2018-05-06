from security.models import InputLoggedRequest
from security.decorators import throttling_all

from auth_token.contrib.is_core.default.views import TokenLoginView as DefaultTokenLoginView
from auth_token.contrib.is_core.auth_security import LOGIN_THROTTLING_VALIDATORS


@throttling_all(*LOGIN_THROTTLING_VALIDATORS)
class TokenLoginView(DefaultTokenLoginView):

    def form_valid(self, form):
        if getattr(self.request, 'input_logged_request', False):
            self.request.input_logged_request.type = InputLoggedRequest.SUCCESSFUL_LOGIN_REQUEST
        return super(TokenLoginView, self).form_valid(form)

    def form_invalid(self, form):
        if getattr(self.request, 'input_logged_request', False):
            self.request.input_logged_request.type = InputLoggedRequest.UNSUCCESSFUL_LOGIN_REQUEST
        return super(TokenLoginView, self).form_invalid(form)
