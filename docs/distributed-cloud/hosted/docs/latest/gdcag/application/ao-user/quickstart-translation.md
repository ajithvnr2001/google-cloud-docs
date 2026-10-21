---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation/
title: Translate text \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:27:58.286884+00:00
---

# Translate text  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Translate text Stay organized with collections  Save and categorize content based on your preferences. 

The Vertex AI Translation service lets you translate text written in a language into any of the other [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs).

This page shows you how to translate a sample text using the Vertex AI Translation API on Google Distributed Cloud (GDC) air-gapped.

## Before you begin

To translate text, contact your Project IAM Admin to request the **AI Translation Developer** (`ai-translation-developer`) role in your project namespace.

For more information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

Before you can start using the Vertex AI Translation API, you must have a project with the Vertex AI Translation API enabled, and you must have the appropriate credentials. You can also install client libraries to help you make calls to the API. For more information, see [Set up a translation project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-translation).

## Translate text

The `translateText` method takes input text in a particular language and returns the translated text into another language. You can enter plain or HTML text as input.

If you enter HTML text, the `translateText` method translates only the text between the HTML tags without translating the tags. However, it translates attributes in HTML5 tags, such as `alt` attributes. An example of using HTML5 tags and attributes is used in the syntax to exclude text from translation. The output retains the untranslated HTML tags and includes the translated text between them.

**Note:** Differences can exist between the source and target languages. Because of word order changes in the translation, the order of HTML tags in the output might differ from that in the input text.

Make a `curl` request to the Vertex AI Translation pre-trained API. Otherwise, interact with the Vertex AI Translation pre-trained API from a Python script to translate text from one language to another.

The following examples show how to translate an input text from one language to another:

### curl

Follow these steps to make a `curl` request:

  1. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  2. Make the request:



    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d '{"parent": "projects/PROJECT_ID", "source_language_code": "SOURCE_LANGUAGE", "target_language_code": "TARGET_LANGUAGE", "contents": ["INPUT_TEXT"]}'
    

Replace the following:

  * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
  * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
  * `PROJECT_ID`: your project ID.
  * `SOURCE_LANGUAGE`: the language code of your input text. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
  * `TARGET_LANGUAGE`: the language code you want to translate your text into. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
  * `INPUT_TEXT`: your input text in the source language.



Use the `mime_type` field to specify a type of file. Set the `mime_type` field to one of the following values:

  * `text/plain`: your input is plain text.
  * `text/html`: your input is HTML text.



If the `mime_type` field is empty, `text/html` is the default value.

The following example uses the `mime_type` field:
    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d '{"mime_type": "text/html", "parent": "projects/PROJECT_ID", "source_language_code": "SOURCE_LANGUAGE", "target_language_code": "TARGET_LANGUAGE", "contents": ["INPUT_TEXT"]}'
    

The output returns the translated text.

### Python

Follow these steps to use the Vertex AI Translation service from a Python script:

  1. [Install the latest version of the Vertex AI Translation client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

  2. [Set the required environment variables on a Python script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-translation#set-env-var).

  3. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  4. Add the following code to the Python script you created:
         
         from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
         import google.auth
         from google.auth.transport import requests
         from google.api_core.client_options import ClientOptions
         
         audience = "https://ENDPOINT:443"
         api_endpoint="ENDPOINT:443"
         
         def translate_client(creds):
           opts = ClientOptions(api_endpoint=api_endpoint)
           return [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)(credentials=creds, client_options=opts)
         
         def main():
           creds = None
           try:
             creds, project_id = google.auth.default()
             creds = creds.with_gdch_audience(audience)
             req = requests.Request()
             creds.refresh(req)
             print("Got token: ")
             print(creds.token)
           except Exception as e:
             print("Caught exception" + str(e))
             raise e
           return creds
         
         def translate_func(creds):
           tc = translate_client(creds)
           req = {
             "parent": "projects/PROJECT_ID",
             "source_language_code": "SOURCE_LANGUAGE",
             "target_language_code": "TARGET_LANGUAGE",
             "mime_type": "text/plain",
             "contents": ["INPUT_TEXT"]
           }
         
           resp = tc.translate_text(req)
           print(resp)
         
         if __name__=="__main__":
           creds = main()
           translate_func(creds)
         

Replace the following:

     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.
     * `SOURCE_LANGUAGE`: the language code of your input text. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the language code you want to translate your text into. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `INPUT_TEXT`: your input text in the source language.

Use the `mime_type` field to specify a type of file. Set the `mime_type` field to one of the following values:

     * `text/plain`: your input is plain text.
     * `text/html`: your input is HTML text.

If the `mime_type` field is empty, `text/html` is the default value.

  5. Save the Python script.

  6. Run the Python script to translate the text:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `translation.py`.




For more information on the `translateText` method, see the [Python client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/Python/google.cloud.translate_v3.services.translation_service.TranslationServiceClient#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text).

### Exclude text from translation

Use one of the following HTML tags on the `contents` field of requests to exclude parts of your text from translation:

  * `<span translate="no">"TEXT"</span>`
  * `<span class="notranslate">"TEXT"</span>`



Replace `TEXT` with the portion of text you want to exclude from translation.

For example, if you have the following input text in Spanish:
    
    
    Hola, esto es una prueba.
    

The expected translated text to English is:
    
    
    Hello, this is a test.
    

Suppose you only want to translate the following part of the text, excluding `Hola,` from the input text:
    
    
    esto es una prueba.
    

The expected translated text to English is:
    
    
    this is a test.
    

Use the HTML tags to exclude text from the translation. For example, the following `curl` request uses the `<span class="notranslate">"TEXT"</span>` tag to exclude `Hola,` from the previous input text in Spanish when translating the text to English:
    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d '{"parent": "projects/PROJECT_ID", "source_language_code": "es", "target_language_code": "en", "contents": ["<span class=\"notranslate\">\"Hola,\"</span>\"esto es una prueba.\""]}'
    

### Translate with glossary

To translate text with words from a glossary, you must [create a glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-glossary):

  1. Save the following `request_glossary.json` file:
         
         cat <<- EOF > request_glossary.json
         {
         "sourceLanguageCode": "SOURCE_LANGUAGE",
         "targetLanguageCode": "SOURCE_LANGUAGE",
         "contents": "TEXT",
         "glossaryConfig": {
           "glossary": "projects/PROJECT_ID/glossaries/GLOSSARY_ID",
           "ignoreCase": IGNORE_CASE_BOOLEAN,
           "contextual_translation_enabled": CONTEXTUAL_BOOLEAN
         }
         }
         EOF
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `SOURCE_LANGUAGE`: the language in which your document is written. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the language or languages into which you want to translate your document. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TEXT`: translating text which includes glossary words
     * `GLOSSARY_ID`: the ID of glossary, example: `G11111111114524`
  2. Make the request:
         
         curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d @request_glossary.json
         




#### Example and expected output:

Request:
    
    
    {
      "sourceLanguageCode": "es",
      "targetLanguageCode": "en",
      "contents": "La novela cuenta la historia de una joven que viaja a Madrid",
      "glossaryConfig": {
        "glossary": "projects/test-project/glossaries/GLOSSARY_ID",
        "ignoreCase": true,
        "contextual_translation_enabled": true
      }
    }
    

Response:
    
    
    {"translations":[
      {
        "translatedText":"The novel tells the story of a young woman who travels to Madrid"}],
        "glossaryTranslations":[{"translatedText":"The novel account the story of a young woman who travels to Madrid",
        "glossaryConfig":
          {
            "glossary":"projects/test-project/glossaries/GLOSSARY_ID"
          }}
      ]}
    

The `translations` field contains the regular machine translation before the glossary is applied; the `glossaryTranslations` field contains the translation after the glossary is applied. When you set the `contextual_translation_enabled` field to `true`, the response will only contain the `glossaryTranslations` field and not the `translations` field.

## Detect language

The `detectLanguage` method returns the language of a text string by sending an HTTP request.

For example, the following request detects English as the language from the input text `Hello, this is a test`:

### curl
    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:detectLanguage -d '{"parent": "projects/PROJECT_ID", "content": "Hello, this is a test"}'
    

## Get an operation

The `getOperation` method returns the latest state of a [long-running operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary#longrunning). Use this method to retrieve the operation result generated by the Vertex AI Translation API service. To use this method, specify your project ID and [the Vertex AI Translation endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

For example, the following request returns the state of a long-running operation, such as [creating a glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-glossary), that is running in your project:

### curl
    
    
    curl -vv -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID/operations/PROJECT_ID
    

## List operations

The `listOperations` method returns a list of the [long-running operations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary#longrunning) that match a specified filter in the request. To use this method, specify your project ID and [the Vertex AI Translation endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

For example, the following request returns the list of operations running in your project and limit the page size to ten results per page:

### curl
    
    
    curl -vv -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID/operations?page_size=10
    

## Get supported languages

The `supportedLanguages` method returns the list of languages that the Vertex AI Translation API supports.

For example, the following request returns the supported languages by specifying [the Vertex AI Translation endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status):

### curl
    
    
    curl -vv -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID/locations/PROJECT_ID/supportedLanguages
    

For the complete list of the supported languages, see [Supported languages for Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
