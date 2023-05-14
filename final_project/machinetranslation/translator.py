import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = 'vccp9gG10beTweMq3ILPQoOwNcqPBGVxh6_4WrH4yZbM'
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/cfbf2c2e-f9b4-449e-8ed1-f5e7fbfdc762"
version = "2018-05-01"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    if englishText is None:
        return ""
    try:
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        phrase = translation["translations"][0]["translation"]
    except ApiException as ex:
        phrase = ""
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)

    return phrase


def frenchToEnglish(frenchText):
    if frenchText is None:
        return ""
    try:
        translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        phrase = translation["translations"][0]["translation"]
    except ApiException as ex:
        phrase = ""
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)

    return phrase
