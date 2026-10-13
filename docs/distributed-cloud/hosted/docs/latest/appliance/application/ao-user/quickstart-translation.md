---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation/
title: Translate text \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:15.008885+00:00
---

# Translate text  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Translate text Stay organized with collections  Save and categorize content based on your preferences. 

The Vertex AI Translation service lets you translate text written in a language into any of the other [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs).

This page shows you how to translate a sample text using the Vertex AI Translation API on Google Distributed Cloud (GDC) air-gapped appliance.

## Before you begin

Before you can start using the Vertex AI Translation API, you must have a project with the Vertex AI Translation API enabled, and you must have the appropriate credentials. You can also install client libraries to help you make calls to the API. For more information, see [Set up a translation project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-translation).

## Translate text

The `translateText` method takes input text in a particular language and returns the translated text into another language. You can enter plain or HTML text as input.

If you enter HTML text, the `translateText` method translates only the text between the HTML tags without translating the tags. However, it translates attributes in HTML5 tags, such as `alt` attributes. An example of using HTML5 tags and attributes is used in the syntax to exclude text from translation. The output retains the untranslated HTML tags and includes the translated text between them.

**Note:** Differences can exist between the source and target languages. Because of word order changes in the translation, the order of HTML tags in the output might differ from that in the input text.

Make a `curl` request to the Vertex AI Translation pre-trained API. Otherwise, interact with the Vertex AI Translation pre-trained API from a Python script to translate text from one language to another.

The following examples show how to translate an input text from one language to another:

### curl

Follow these steps to make a `curl` request:

  1. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth).

  2. Make the request:



    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d '{"parent": "projects/PROJECT_ID", "source_language_code": "SOURCE_LANGUAGE", "target_language_code": "TARGET_LANGUAGE", "contents": ["INPUT_TEXT"]}'
    

Replace the following:

  * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth) you obtained.
  * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).
  * `PROJECT_ID`: your project ID.
  * `SOURCE_LANGUAGE`: the language code of your input text. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs) and their respective language codes.
  * `TARGET_LANGUAGE`: the language code you want to translate your text into. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs) and their respective language codes.
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

  1. [Install the latest version of the Vertex AI Translation client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries).

  2. [Set the required environment variables on a Python script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-translation#set-env-var).

  3. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth).

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

     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.
     * `SOURCE_LANGUAGE`: the language code of your input text. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs) and their respective language codes.
     * `TARGET_LANGUAGE`: the language code you want to translate your text into. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs) and their respective language codes.
     * `INPUT_TEXT`: your input text in the source language.

Use the `mime_type` field to specify a type of file. Set the `mime_type` field to one of the following values:

     * `text/plain`: your input is plain text.
     * `text/html`: your input is HTML text.

If the `mime_type` field is empty, `text/html` is the default value.

  5. Save the Python script.

  6. Run the Python script to translate the text:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `translation.py`.




### Exclude text from translation

Use one of the following HTML tags on the `contents` field of requests to exclude parts of your text from translation:

  * `<span translate="no">"TEXT"</span>`
  * `<span class="notranslate">"TEXT"</span>`



Replace `TEXT` with the portion of text you want to exclude from translation.

For example, if you have the following input text in French:
    
    
    Bonjour, c'est un test.
    

Then, that text translates in English to the following sentence:
    
    
    Hello, this is a test.
    

Suppose you only want to translate the following part of the text, excluding `Bonjour,` from the input text:
    
    
    c'est un test.
    

That part of the text translates in English to the following sentence:
    
    
    this is a test.
    

Use the HTML tags to exclude text from the translation. For example, the following `curl` request uses the `<span class="notranslate">"TEXT"</span>` tag to exclude `Bonjour,` from the previous input text in French when translating the text to English:
    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:translateText -d '{"parent": "projects/PROJECT_ID", "source_language_code": "fr", "target_language_code": "en", "contents": ["<span class=\"notranslate\">\"Bonjour,\"</span>\"c'est un test.\""]}'
    

## Detect language

The `detectLanguage` method returns the language of a text string by sending an HTTP request.

For example, the following request detects English as the language from the input text `Hello, this is a test`:

### curl
    
    
    curl -vv -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID:detectLanguage -d '{"parent": "projects/PROJECT_ID", "content": "Hello, this is a test"}'
    

## Get supported languages

The `supportedLanguages` method returns the list of languages that the Vertex AI Translation API supports.

For example, the following request returns the supported languages by specifying [the Vertex AI Translation endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status):

### curl
    
    
    curl -vv -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" https://ENDPOINT/v3/projects/PROJECT_ID/locations/PROJECT_ID/supportedLanguages
    

For the complete list of the supported languages, see [Supported languages for Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
