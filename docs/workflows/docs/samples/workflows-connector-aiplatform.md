---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-aiplatform/
title: Connector for Vertex AI \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:57.885855+00:00
---

# Connector for Vertex AI  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-aiplatform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Vertex AI within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Vertex AI API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the aiplatform (Vertex AI) connector.
    # This workflow creates a Vertex AI custom Job and then deletes the
    # job once the long-running operation of creating the job completes.
    # Expected successful output: "SUCCESS"
    main:
      steps:
        - init:
            assign:
              - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
              - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              # Follow https://cloud.google.com/vertex-ai/docs/training/create-custom-container to build
              # a custom container image for training.
              - container_image_uri: "IMAGE_URI"
        - create_custom_job:
            call: googleapis.aiplatform.v1.projects.locations.customJobs.create
            args:
              parent: ${"projects/" + project + "/locations/" + location}
              region: ${location}
              body:
                displayName: "example-custom-job"
                jobSpec:
                  workerPoolSpecs:
                    - machineSpec:
                        machineType: "n1-standard-4"
                        acceleratorType: "NVIDIA_TESLA_V100"
                        acceleratorCount: 1
                      replicaCount: 1
                      containerSpec:
                        imageUri: ${container_image_uri}
                        command: []
                        args: []
            result: customJobsResponse
        - delete_custom_job:
            call: googleapis.aiplatform.v1.projects.locations.customJobs.delete
            args:
              name: ${customJobsResponse.name}
              region: ${location}
            result: deleteCustomJobResponse
        - return:
            return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
