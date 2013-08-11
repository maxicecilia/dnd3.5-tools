from django.shortcuts import render_to_response
from django.template import RequestContext
#from character.models import Character

def home(request):
    '''
        Redirect to default home view.
    '''
    #company = get_object_or_404(Company, pk=SITE_ID)

    #char = Character.objects.get(pk = 1)
    
    #labels = {'news_label': _('Lastest News')}
    return render_to_response('website/index.html', {}, context_instance=RequestContext(request))