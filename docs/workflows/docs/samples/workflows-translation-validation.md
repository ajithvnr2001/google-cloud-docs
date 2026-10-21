---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-translation-validation/
title: Validate a translation request using a callback endpoint \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:46.984421+00:00
---

# Validate a translation request using a callback endpoint  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-translation-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Validate a translation request using a callback endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Validates translation requests by supporting a callback endpoint that waits for HTTP requests to arrive at that endpoint, resuming the execution of the workflow at a later point in time. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a human-in-the-loop workflow using callbacks](https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore)



## Code sample

### YAML
    
    
    main:
        params: [translation_request]
        steps:
            - log_request:
                call: sys.log
                args:
                    text: ${translation_request}
            - vars:
                assign:
                    - exec_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                    - text_to_translate: ${translation_request.text}
                    - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/translations/"}
            - log_translation_request:
                call: sys.log
                args:
                    text: ${text_to_translate}
    
            - store_translation_request:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                    name: ${database_root + exec_id}
                    updateMask:
                        fieldPaths: ['text']
                    body:
                        fields:
                            text:
                                stringValue: ${text_to_translate}
                result: store_translation_request_result
    
            - translate:
                call: googleapis.translate.v2.translations.translate
                args:
                    query:
                        q: ${text_to_translate}
                        target: "FR"
                        format: "text"
                        source: "EN"
                result: translation_result
            - assign_translation:
                assign:
                    - translation: ${translation_result.data.translations[0].translatedText} 
            - log_translation_result:
                call: sys.log
                args:
                    text: ${translation}
    
            - store_translated_text:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                    name: ${database_root + exec_id}
                    updateMask:
                        fieldPaths: ['translation']
                    body:
                        fields:
                            translation:
                                stringValue: ${translation}
                result: store_translation_request_result   
    
            - create_callback:
                call: events.create_callback_endpoint
                args:
                    http_callback_method: "POST"
                result: callback_details
            - log_callback_details:
                call: sys.log
                args:
                    text: ${callback_details}
    
            - store_callback_details:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                    name: ${database_root + exec_id}
                    updateMask:
                        fieldPaths: ['callback']
                    body:
                        fields:
                            callback:
                                stringValue: ${callback_details.url}
                result: store_callback_details_result
    
            - await_callback:
                call: events.await_callback
                args:
                    callback: ${callback_details}
                    timeout: 3600
                result: callback_request
            - assign_approval:
                assign:
                    - approved: ${callback_request.http_request.body.approved}
    
            - store_approval:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                    name: ${database_root + exec_id}
                    updateMask:
                        fieldPaths: ['approved']
                    body:
                        fields:
                            approved:
                                booleanValue: ${approved}
                result: store_approval_result
    
            - return_outcome:
                return:
                    text: ${text_to_translate}
                    translation: ${translation}
                    approved: ${approved}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
