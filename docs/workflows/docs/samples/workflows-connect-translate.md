---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-translate/
title: Translate text using the Cloud Translation API \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:24.297126+00:00
---

# Translate text using the Cloud Translation API  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-translate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Translate text using the Cloud Translation API Stay organized with collections  Save and categorize content based on your preferences. 

Makes an HTTP POST request to the Cloud Translation API to translate text from English to Russian.

## Code sample

### YAML
    
    
    main:
      params: [args]
      steps:
        - new_translation:
            call: http.post
            args:
              url: ${"https://translation.googleapis.com/v3/projects/"+sys.get_env("GOOGLE_CLOUD_PROJECT_NUMBER")+":translateText"}
              auth:
                type: OAuth2
              body:
                contents: ${args.textToTranslate}
                sourceLanguageCode: "en-US"
                targetLanguageCode: "ru-RU"
            result: translate_response
        - assign_translation:
            assign:
              - translation_result: ${translate_response.body.translations[0].translatedText}
        - return_result:
            return: ${translation_result}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
