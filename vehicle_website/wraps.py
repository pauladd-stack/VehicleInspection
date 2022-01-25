from functools import wraps
from django.http import HttpResponseRedirect

def admin_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.role == 'Admin':
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap

def mechanic_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.role == 'Admin' or profile.role == 'Mechanic':
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap

def driver_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.role == 'Admin' or profile.role == 'Driver':
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap