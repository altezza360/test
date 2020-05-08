from django.shortcuts import redirect, HttpResponse


# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('home')
#         else:
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to be here')

        return wrapper_func
#
    return decorator


def check(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'specialist':
            return redirect('/user_page')
        if group == 'manager':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def is_specialist(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_spec and request.user.is_admin == False:
            return redirect('/user_page')
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
    return wrapper_function
# customers_url
# specialist_view_url
