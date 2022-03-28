from django.shortcuts import redirect


class RedirectToDashboard:
    # if user is logged in, redirect him to dashboard
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
