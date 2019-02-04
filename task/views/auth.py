from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'auth/logout.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'auth/password-reset.html'
    email_template_name = 'auth/password-reset.eml'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'auth/password-reset-done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'auth/password-reset-confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'auth/password-reset-complete.html'
