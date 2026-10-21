---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-event-sample/
title: Store callback details in a Firestore database \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:48.760979+00:00
---

# Store callback details in a Firestore database  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-callback-event-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Store callback details in a Firestore database Stay organized with collections  Save and categorize content based on your preferences. 

Stores callback details in a Firestore database, halts execution, and then waits for specific events to occur.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Wait for events using callbacks and Eventarc triggers](https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks)



## Code sample

### YAML
    
    
    main:
      steps:
        - init:
            assign:
              - pubsub_topic: topic-callback
              - storage_bucket: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "-bucket-callback"}
        - await_pubsub_message:
            call: await_callback_event
            args:
              event_source: ${pubsub_topic}
            result: pubsub_event
        - await_storage_bucket:
            call: await_callback_event
            args:
              event_source: ${storage_bucket}
            result: storage_event
        - return_events:
            return:
                pubsub_event: ${pubsub_event}
                storage_event: ${storage_event}
    
    await_callback_event:
        params: [event_source]
        steps:
            - init:
                assign:
                  - database_root: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/databases/(default)/documents/callbacks/"}
                  - doc_name: ${database_root + event_source}
                  - execution_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                  - firestore_key: ${"exec_" + text.split(execution_id, "-")[0]}
            - create_callback:
                call: events.create_callback_endpoint
                args:
                  http_callback_method: POST
                result: callback_details
            - save_callback_url:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                  name: ${doc_name}
                  updateMask:
                    fieldPaths: ["${firestore_key}"]
                  body:
                    fields:
                      ${firestore_key}:
                        stringValue: ${callback_details.url}
            - log_and_await_callback:
                try:
                  steps:
                    - log_await_start:
                        call: sys.log
                        args:
                          severity: INFO
                          data: ${"Started waiting 1hr for an event from source " + event_source}
                    - await_callback:
                        call: events.await_callback
                        args:
                          callback: ${callback_details}
                          timeout: 3600
                        result: callback_request
                    - log_await_stop:
                        call: sys.log
                        args:
                          severity: INFO
                          data: ${"Stopped waiting for an event from source " + event_source}
                except:
                    as: e
                    steps:
                        - log_error:
                            call: sys.log
                            args:
                                severity: "ERROR"
                                text: ${"Received error " + e.message}
            - delete_callback_url:
                call: googleapis.firestore.v1.projects.databases.documents.patch
                args:
                  name: ${doc_name}
                  updateMask:
                    fieldPaths: ["${firestore_key}"]
            - check_null_event:
                switch:
                  - condition: ${callback_request == null}
                    return: null
            - log_await_result:
                call: sys.log
                args:
                  severity: INFO
                  data: ${callback_request.http_request.body.event}
            - return_event:
                return: ${callback_request.http_request.body.event}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
