---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-batch/
title: Connector for Batch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:26.095130+00:00
---

# Connector for Batch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Batch Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Batch within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Batch connector.
    # This workflow sends a List request to Batch connector.
    main:
      steps:
        - init:
            assign:
              - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
              - jobId: "example-job"
        - create_job:
            call: googleapis.batch.v1.projects.locations.jobs.create
            args:
              parent: ${"projects/" + project + "/locations/" + location}
              jobId: ${jobId}
              body:
                priority: 99
                taskGroups:
                  taskSpec:
                    runnables:
                      script:
                        text: "echo Hello World!"
                    computeResource:
                      cpuMilli: 2000
                      memoryMib: 16
                  taskCount: 1
        - delete_job:
            call: googleapis.batch.v1.projects.locations.jobs.delete
            args:
              name: ${"projects/" + project + "/locations/" + location + "/jobs/" + jobId}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
