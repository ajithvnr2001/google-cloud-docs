---
url: https://docs.cloud.google.com/translate/docs/advanced/nmt-model/
title: Neural Machine Translation (NMT) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:58.721745+00:00
---

# Neural Machine Translation (NMT)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/nmt-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Neural Machine Translation (NMT) model

Google's standard Neural Machine Translation (NMT) has evolved from the [neural network translation system](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation) that Google introduced in November 2016, with many improvements. It can translate to and from many languages in real time.

Its model ID is `general/nmt`.

You can access the NMT model without modification through either the Cloud Translation - Basic API or the Cloud Translation - Advanced API. With Cloud Translation - Advanced API, you can also [customize it](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization).

In either case, you need to have a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) that has Cloud Translation API enabled, with credentials to make authenticated calls. To access the model using Python or another programming language, install the appropriate [v2](https://docs.cloud.google.com/translate/docs/reference/libraries/v2/overview-v2) or [v3](https://docs.cloud.google.com/translate/docs/reference/libraries/v3/overview-v3) client library.

In the examples shown here, `PROJECT_ID` represents your project ID, and `REGION_NAME` represents the technical region name of the Google Cloud region where you want to run the translation operation (such as `us-central1`). Use [ISO-639](https://wikipedia.org/wiki/ISO_639) codes to identify source and target languages where necessary.

## Cloud Translation - Basic API REST example

You can make a REST call with Cloud Translation - Basic API to [TranslateText](https://docs.cloud.google.com/translate/docs/reference/rest/v2/translate) using the NMT model. You can put request fields into a JSON file named something like `request.json`, like this:
    
    
    {
      "q": ["Hello world", "My name is Jeff"],
      "target": "de"
    }
    

The Cloud Translation - Basic API supports the NMT model by default. You don't need to specify it. You can also specify the standard TLLM model if you pass its full resource name. Cloud Translation - Basic does not support customized models.

You can then use a `curl` command to submit the request:
    
    
    !curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "x-goog-user-project: cloud-ml-translate-e2e-testing" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://translate.googleapis.com/language/translate/v2"
    

The response is a JSON document which looks like this:
    
    
    {
      "data": {
        "translations": [
          {
            "translatedText": "Hallo Welt",
            "detectedSourceLanguage": "en"
          },
          {
            "translatedText": "Mein Name ist Jeff",
            "detectedSourceLanguage": "en"
          }
        ]
      }
    }
    

## Cloud Translation - Basic API Python example

Here is sample Python code for calling `TranslateText` on the NMT model using the Cloud Translation - Basic API. Because no source language is specified, the API attempts to detect it automatically.
    
    
    def translate_text(
      text: str | bytes | list[str] = "¡Hola amigos y amigas!",
      target_language: str = "en",
      source_language: str | None = None,
    ) -> dict:
    
      translate_client = translate_v2.Client()
    
      if isinstance(text, bytes):
        text = [text.decode("utf-8")]
    
      if isinstance(text, str):
        text = [text]
    
      results = translate_client.translate(
        values=text,
        target_language=target_language,
        source_language=source_language
      )
    
      for result in results:
        if "detectedSourceLanguage" in result:
          print(f"Detected source language: {result['detectedSourceLanguage']}")
        print(f"Input text: {result['input']}")
        print(f"Translated text: {result['translatedText']}")
        print()
    
      return results
    
    translate_text()
    

The output is as follows:
    
    
    Detected source language: es
    Input text: ¡Hola amigos y amigas!
    Translated text: Hello friends!
    
    [{'translatedText': 'Hello friends!',
      'detectedSourceLanguage': 'es',
      'input': '¡Hola amigos y amigas!'}]
    

## Cloud Translation - Advanced API REST example

You can make a REST call with Cloud Translation - Advanced API to [TranslateText](https://docs.cloud.google.com/translate/docs/reference/rest/v2/translate) using the default NMT model either by not specifying a model, or by explicitly requesting the NMT model. Put request fields into a JSON file named something like `request.json`, like this:
    
    
    {
      "sourceLanguageCode": "en",
      "targetLanguageCode": "ru",
      "contents": ["Dr. Watson, come here!", "Bring me some coffee!"],
      "model": "projects/PROJECT_ID/locations/REGION_NAME/models/general/nmt"
    }
    

You can then use a `curl` command to submit the request:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "x-goog-user-project: PROJECT_ID" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_NAME:translateText"
    

The response is a JSON document which looks like this:
    
    
    {
      "translations": [
        {
          "translatedText": "Доктор Ватсон, иди сюда!",
        },
        {
          "translatedText": "Принеси мне кофе!",
        }
      ]
    }
    

## Cloud Translation - Advanced API Python example
    
    
    def translate():
    
      response = translate_v3.TranslationServiceClient().translate_text(
          contents=["Life is short.",
                    "Art is long."],
          target_language_code='fr',
          source_language_code='en',
          parent=f"projects/{project_id}/locations/us-central1",
          model=f"{parent}/models/general/nmt"
      )
    
      print(response)
    
      return response
    
    translate()
    

The output is a JSON document which looks like this:
    
    
    translations {
      translated_text: "La vie est courte."
      model: "projects/261347268520/locations/us-central1/models/general/nmt"
    }
    translations {
      translated_text: "L&#39;art est long."
      model: "projects/261347268520/locations/us-central1/models/general/nmt"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
