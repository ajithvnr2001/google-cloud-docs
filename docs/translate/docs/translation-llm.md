---
url: https://docs.cloud.google.com/translate/docs/translation-llm/
title: Translation LLM (TLLM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:13.889501+00:00
---

# Translation LLM (TLLM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/translation-llm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Translation LLM (TLLM) model

Google's latest state-of-the-art translation model, TLLM, is a Large Language Model (LLM) that provides the highest available quality of translation. It achieves significantly better [MetricX](https://github.com/google-research/metricx) and [COMET](https://huggingface.co/Unbabel/wmt22-comet-da) scores on difficult workloads compared to other translation models. It supports customization as well as more lightweight [Adaptive Translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation).

Its model ID is `general/translation-llm`.

To access the TLLM model, you must have a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with Cloud Translation - Basic API or Cloud Translation - Advanced API enabled and credentials to make authenticated calls. To access the model using Python or another programming language, install the client library (v3 is required for Cloud Translation - Advanced API features).

In the examples presented here, `PROJECT_ID` represents your project ID, and `REGION_NAME` represents the technical region name of the Google Cloud region where you want to run the translation operation (such as `us-central1`). Use [ISO-639](https://wikipedia.org/wiki/ISO_639) codes to identify source and target languages where necessary.

## Text translation REST example

You can use the REST API to call [TranslateText](https://docs.cloud.google.com/translate/docs/reference/rest/v3beta1/projects/translateText) on the TLLM model. You can put request fields into a JSON file named something like `request.json`:
    
    
    {
      "contents": ["This is text that I would like to have translated.",
                   "It can include up to 1024 strings."],
      "mimeType": "text/plain",
      "sourceLanguageCode": "en"
      "targetLanguageCode": "it",
      "model": "projects/PROJECT_ID/locations/REGION_NAME/models/general/translation-llm"
    }
    

You can then use a `curl` command to submit the request:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "x-goog-user-project: PROJECT_ID" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://translation.googleapis.com/v3/projects/PROJECT_ID:translateText"
    

The response is a JSON document that looks like this:
    
    
    {
      "translations": [
        {
          "translatedText": "Este es el texto que me gustaría traducir.",
          "model": "projects/PROJECT_ID/locations/REGION_NAME/models/general/translation-llm"
        },
        {
          "translatedText": "Puede incluir hasta 1024 cadenas.",
          "model": "projects/PROJECT_ID/locations/REGION_NAME/models/general/translation-llm"
        }
      ]
    }
    

## Text translation REST example (Basic/V2)

You can use the Cloud Translation - Basic (V2) REST API to call the standard `Translation LLM` model. You must use an API key for authentication.
    
    
    curl -X POST \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
           "q": ["The old lighthouse stood on the edge of the cliff."],
           "target": "es",
           "model": "projects/PROJECT_ID/locations/REGION_NAME/models/general/translation-llm"
         }' \
         "https://translation.googleapis.com/language/translate/v2?key=YOUR_API_KEY"
    

## Text translation Python example

Here is sample Python code for calling `TranslateText` with the TLLM model:
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)_v3
    
    def translate():
    
      response = translate_v3.[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)().translate_text(
          contents=["Life is short.",
                      "Art is long."],
          target_language_code='fr',
          source_language_code='en',
          parent=f"projects/PROJECT_ID/locations/REGION_NAME",
          model=f"projects/PROJECT_ID/locations/REGION_NAME/models/general/translation-llm"
      )
    
      print(response)
    
      return response
    
    translate()
    

The response takes the form of JSON objects:
    
    
    translations {
      translated_text: "La vie est courte."
      model: "projects/261347268520/locations/us-central1/models/general/translation-llm"
    }
    translations {
      translated_text: "L&#39;art est long."
      model: "projects/261347268520/locations/us-central1/models/general/translation-llm"
    }
    
    translations {
      translated_text: "La vie est courte."
      model: "projects/261347268520/locations/us-central1/models/general/translation-llm"
    }
    translations {
      translated_text: "L&#39;art est long."
      model: "projects/261347268520/locations/us-central1/models/general/translation-llm"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
