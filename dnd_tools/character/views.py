# Create your views here.
from dnd_tools.character.models import Character
from django import http
import jsonpickle

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return jsonpickle.encode(context, unpicklable=False)


#####
## character views
#####
def get_all_characters(request):
    response = JSONResponseMixin()

    return response.render_to_response(Character.objects.all())

def get_characters_by_name(request, name):
    response = JSONResponseMixin()

    characters = Character.objects.filter(name__iexact = name)

    character_list = []
    for character in characters:
        character.load()
        character_list.append(character)


    return response.render_to_response(character_list)