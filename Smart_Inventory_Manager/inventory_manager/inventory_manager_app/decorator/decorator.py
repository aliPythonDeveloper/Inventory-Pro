from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("inventory_manager_app:home")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


#the below function was made to check if the user in the admin group
# def allowed_user(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('You are not authorized to view')
#         return wrapper_func
#     return decorator


def superuser_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redirect unauthenticated users to the login page
            return redirect('inventory_manager_app:login')

        if not request.user.is_superuser:
            # Return an error for non-superusers
            return HttpResponse("You are not authorized to view this page.", status=403)

        # Allow access to the view if the user is a superuser
        return view_func(request, *args, **kwargs)

    return wrapper_func