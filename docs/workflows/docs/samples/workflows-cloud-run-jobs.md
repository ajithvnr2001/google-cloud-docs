---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-run-jobs/
title: Execute a Cloud Run job \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:56.669009+00:00
---

# Execute a Cloud Run job  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-run-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Execute a Cloud Run job Stay organized with collections  Save and categorize content based on your preferences. 

Deploy a workflow that executes a Cloud Run job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Execute a Cloud Run job using Workflows](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs)



## Code sample

### YAML
    
    
    main:
        params: [event]
        steps:
            - init:
                assign:
                    - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                    - event_bucket: ${event.data.bucket}
                    - event_file: ${event.data.name}
                    - target_bucket: ${"input-" + project_id}
                    - job_name: parallel-job
                    - job_location: us-central1
            - check_input_file:
                switch:
                    - condition: ${event_bucket == target_bucket}
                      next: run_job
                    - condition: true
                      next: end
            - run_job:
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
