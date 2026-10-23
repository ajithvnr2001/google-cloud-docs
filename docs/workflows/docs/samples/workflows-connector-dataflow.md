---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-dataflow/
title: Connector for Dataflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:58.054360+00:00
---

# Connector for Dataflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-dataflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Dataflow within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Dataflow API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/dataflow/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Dataflow connector.
    # The workflow creates a word count job using a Dataflow public job template
    # and uses a Cloud Storage bucket as temporary storage for temp files.
    # The bucket resource is deleted after the job completes.
    # Expected successful output: "SUCCESS"
    
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location: "us-central1"
          - zone: "us-central1-a"
          - bucket_name: "[fill in a bucket name]"
          - job_name: "[fill in a job name]"
          - input_file: "gs://dataflow-samples/shakespeare/kinglear.txt"
          - output_storage_file_prefix: ${"gs://" + bucket_name + "/counts"}
          - temp_location: ${"gs://" + bucket_name + "/counts/temp"}
          - template_path: "gs://dataflow-templates-us-central1/latest/Word_Count"
    - create_bucket:
        call: googleapis.storage.v1.buckets.insert
        args:
          project: ${project_id}
          body:
            name: ${bucket_name}
    - create_job:
        call: googleapis.dataflow.v1b3.projects.locations.templates.create
        args:
          projectId: ${project_id}
          location: ${location}
          body:
            jobName: ${job_name}
            parameters:
              inputFile: ${input_file}
              output: ${output_storage_file_prefix}
            environment:
              numWorkers: 1
              maxWorkers: 2
              zone: ${zone}
              tempLocation: ${temp_location}
            gcsPath: ${template_path}
    - delete_bucket_object1:
        call: googleapis.storage.v1.objects.delete
        args:
          bucket: ${bucket_name}
          object: ${"counts-00000-of-00003"}
    - delete_bucket_object2:
        call: googleapis.storage.v1.objects.delete
        args:
          bucket: ${bucket_name}
          object: ${"counts-00001-of-00003"}
    - delete_bucket_object3:
        call: googleapis.storage.v1.objects.delete
        args:
          bucket: ${bucket_name}
          object: ${"counts-00002-of-00003"}
    - delete_bucket:
        call: googleapis.storage.v1.buckets.delete
        args:
          bucket: ${bucket_name}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
