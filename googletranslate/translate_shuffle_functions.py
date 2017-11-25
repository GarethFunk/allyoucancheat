from simple_rest_client.api import API
from simple_rest_client.resource import Resource

class TranslateResource(Resource):
    actions = {
        'translate': {'method': 'POST', 'url': 'language/translate/v2'}
    }


def translate(text, langin, langout, key, model):

    # set default params
    default_params = {'key': key, 'format': "text"}
    # create api instance
    translate_api = API(
        api_root_url='https://translation.googleapis.com', params=default_params,
        json_encode_body=True
    )

    translate_api.add_resource(resource_name="translate", resource_class=TranslateResource)
    output = translate_api.translate.translate(params={'source': langin, 'target': langout, 'q': text, 'model': model}).body
    return output['data']['translations'][0]['translatedText']

def translateshuffle(text, langin, langout, key, model):

    translatedtext = translate(text, langin, langout, key, model)
    shuffledtext = translate(translatedtext, langout, langin, key, model)

    return shuffledtext

def translateshuffleflexible(text, langin, langint1, langint2, langout, key, model1, model2):

    translatedtext = translate(text, langin, langint1, key, model1)
    translatedtext1 = translate(translatedtext, langint1, langint2, key, model1)
    translatedtext2 = translate(translatedtext1, langint2, langout, key, model1)
    shuffledtext = translate(translatedtext2, langout, langin, key, model2)

    return shuffledtext