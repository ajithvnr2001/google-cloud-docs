---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-run-jobs-payload/
title: Execute a Cloud Run job that processes event data saved in Cloud Storage \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:02.902151+00:00
---

# Execute a Cloud Run job that processes event data saved in Cloud Storage  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-run-jobs-payload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Execute a Cloud Run job that processes event data saved in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Use Workflows to execute a Cloud Run job as part of a workflow that processes event data saved in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Execute a Cloud Run job that processes event data saved in Cloud Storage](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs-stored-events)



## Code sample

### YAML
    
    
    main:
        params: [event]
        steps:
            - init:
                assign:
                    - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                    - event_bucket: message-payload-UNIQUE_ID
                    - event_file: ${event.id + ".data.json"}
                    - job_name: message-payload-job
                    - job_location: us-central1
            - log_event:
                call: sys.log
                args:
                    data: ${event}
            - write_payload_to_gcs:
                call: http.post
                args:
                    url: ${"https://storage.googleapis.com/upload/storage/v1/b/" + event_bucket + "/o"}
                    auth:
                        type: OAuth2
                    query:
                        name: ${event_file}
                    body:
                        ${event.data}
            - run_job_to_process_payload:
                call: googleapis.run.v1.namespaces.jobs.run
                args:
                    name: ${"namespaces/" + project_id + "/jobs/" + job_name}
                    location: ${job_location}
                    body:
                        overrides:
                            containerOverrides:
                                env:
                                    - name: INPUT_BUCKET
                                      value: ${event_bucket}
                                    - name: INPUT_FILE
                                      value: ${event_file}
                result: job_execution
            - finish:
                return: ${job_execution}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
