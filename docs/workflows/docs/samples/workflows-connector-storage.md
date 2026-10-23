---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-storage/
title: Connector for Cloud Storage \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:56.428582+00:00
---

# Connector for Cloud Storage  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Storage within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Storage JSON API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Storage connector:
    # Create a bucket and upload an object to the bucket
    # Delete the bucket and the object
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - bucket_name: "BUCKET_NAME"  # replace BUCKET_NAME and FILE_NAME placeholders
          - encoded_object_name: ${text.url_encode("FILE_NAME.txt")}  # URL-encode object names to be path safe
    - create_bucket:
        call: googleapis.storage.v1.buckets.insert
        args:
          project: ${project_id}
          body:
            name: ${bucket_name}
    - upload_object_media:
        call: googleapis.storage.v1.objects.insert
        args:
          bucket: ${bucket_name}
          uploadType: "media"  # uploads object data
          name: ${encoded_object_name}
          body: "hello world"
    - download_object_media:
        call: googleapis.storage.v1.objects.get
        args:
          bucket: ${bucket_name}
          object: ${encoded_object_name}
          alt: "media"  # gets object data
        result: object_data
    # If `alt` is not set, get metadata
    - get_object_metadata:
        call: googleapis.storage.v1.objects.get
        args:
          bucket: ${bucket_name}
          object: ${encoded_object_name}
        result: object_metadata
    - get_bucket:
        call: googleapis.storage.v1.buckets.get
        args:
          bucket: ${bucket_name}
    - delete_object:
        call: googleapis.storage.v1.objects.delete
        args:
          bucket: ${bucket_name}
          object: ${encoded_object_name}
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
