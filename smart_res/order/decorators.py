from django.http import Http404, HttpResponse



def check_form_submitted(func):
    def wrap(request, *args, **kwargs):
        if not request.session.get('form_submitted'):
            raise Http404()

        return func(request, *args, **kwargs)
    return wrap
