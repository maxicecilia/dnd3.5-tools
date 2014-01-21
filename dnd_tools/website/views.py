from django.shortcuts import render_to_response
from django.template import RequestContext
from character.models import Character
from history.models import History


def home(request):
    '''
        Redirect to default home view.
    '''
    characters = Character.objects.all()

    history = History.objects.all()
    if history:
        history = history[0]

    ctx_dict = {
        'characters': characters,
        'history': history,
    }

    return render_to_response('website/index.html', {}, context_instance=RequestContext(request, ctx_dict))


def character_room_index(request):
    characters = Character.objects.all()

    ctx_dict = {
        'characters': characters,
    }

    return render_to_response('character_room/index.html', {}, context_instance=RequestContext(request, ctx_dict))
