from django.contrib.auth import views as auth_views


class Login(auth_views.LoginView):
    template_name = 'auth/login.html'


class Logout(auth_views.LogoutView):
    template_name = 'auth/logout.html'


class PasswordReset(auth_views.PasswordResetView):
    template_name = 'auth/password-reset.html'
    email_template_name = 'auth/password-reset.eml'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'auth/password-reset-done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'auth/password-reset-confirm.html'


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'auth/password-reset-complete.html'
