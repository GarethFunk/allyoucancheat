from simple_rest_client.api import API
from simple_rest_client.resource import Resource

class TranslateResource(Resource):
    actions = {
        'translate': {'method': 'POST', 'url': 'language/translate/v2'}
    }


def translate(text, langin, langout, key):

    # set default params
    default_params = {'key': key, 'model': 'nmt', 'format': "text"}
    # create api instance
    translate_api = API(
        api_root_url='https://translation.googleapis.com', params=default_params,
        json_encode_body=True
    )

    translate_api.add_resource(resource_name="translate", resource_class=TranslateResource)
    output = translate_api.translate.translate(params={'source': langin, 'target': langout, 'q': text}).body
    return output['data']['translations'][0]['translatedText']

def translateshuffle(text, langin, langout, key):

    translatedtext = translate(text, langin, langout, key)
    shuffledtext = translate(translatedtext, langout, langin, key)

    return shuffledtext