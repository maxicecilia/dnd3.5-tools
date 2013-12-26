from django.shortcuts import render_to_response
from django.template import RequestContext
from character.models import Character


def home(request):
    '''
        Redirect to default home view.
    '''
    characters = Character.objects.all()

    ctx_dict = {'characters': characters}

    return render_to_response('website/index.html', {}, context_instance=RequestContext(request, ctx_dict))
