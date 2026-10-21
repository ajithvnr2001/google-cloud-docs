---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-listener/
title: Deploy a workflow that listens for events \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:49.845903+00:00
---

# Deploy a workflow that listens for events  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-listener/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Deploy a workflow that listens for events Stay organized with collections  Save and categorize content based on your preferences. 

Triggers when a message is published to a Pub/Sub topic or when a file is uploaded to a Cloud Storage bucket; receives the event, retrieves the appropriate callback details from a Firestore database, and then sends an HTTP request to the callback endpoint.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Wait for events using callbacks and Eventarc triggers](https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks)



## Code sample

### YAML
    
    
    main:
      params: [event]
      steps:
        - log_event:
            call: sys.log
            args:
              text: ${event}
              severity: INFO
        - init:
            assign:
              - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
              - event_source_tokens: ${text.split(event.source, "/")}
              - event_source_len: ${len(event_source_tokens)}
              - event_source: ${event_source_tokens[event_source_len - 1]}
              - doc_name: ${database_root + event_source}
        - get_document_for_event_source:
            try:
              call: googleapis.firestore.v1.projects.databases.documents.get
              args:
                name: ${doc_name}
              result: document
            except:
                as: e
                steps:
                    - known_errors:
                        switch:
                        - condition: ${e.code == 404}
                          return: ${"No callbacks for event source " + event_source}
                    - unhandled_exception:
                        raise: ${e}
        - process_callback_urls:
            steps:
              - check_fields_exist:
                  switch:
                  - condition: ${not("fields" in document)}
                    return: ${"No callbacks for event source " + event_source}
                  - condition: true
                    next: processFields
              - processFields:
                  for:
                      value: key
                      in: ${keys(document.fields)}
                      steps:
                          - extract_callback_url:
                              assign:
                                  - callback_url: ${document.fields[key]["stringValue"]}
                          - log_callback_url:
                              call: sys.log
                              args:
                                text: ${"Calling back url " + callback_url}
                                severity: INFO
                          - http_post:
                              call: http.post
                              args:
                                  url: ${callback_url}
                                  auth:
                                      type: OAuth2
                                  body:
                                      event: ${event}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
