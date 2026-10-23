---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations/
title: Manage long-running operations \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:23.114340+00:00
---

# Manage long-running operations  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Manage long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage the lifecycle of a Video Stitcher API Long-Running Operation (LRO).

[_Long-Running Operations_](https://google.aip.dev/151) are returned when method calls might take a long time to complete. For example, the Video Stitcher API creates an LRO every time you call [`projects.locations.liveConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/create). The LRO tracks the status of the processing job.

You can use the [`projects.locations.operations` methods](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations) that the Video Stitcher API provides to check the status of LROs. You can also list, cancel, or delete LROs.

LROs are managed at the Google Cloud project and location level. When making a request to the API, include the Google Cloud project and the location in which the LRO is running.

The record of an LRO is kept for approximately 30 days after the LRO finishes, meaning that you cannot view or list an LRO after that point.

## Get details about a long-running operation

Suppose you [created a live config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs). The `name` value in the response shows that the Video Stitcher API created an LRO named `projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID`.

To check if the input endpoint has been created, use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. This operation can take a few minutes to complete.

You can also retrieve the LRO name by listing long-running operations.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the data; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "endTime": END_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.LiveConfig",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "sourceUri": "SOURCE_LIVESTREAM_URI",
        "adTagUri": "AD_TAG_URI",
        "state": "READY",
        "adTracking": "CLIENT",
        "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
        "stitchingPolicy": "CUT_CURRENT",
        "defaultAdBreakDuration": "30s"
      }
    }
    

If the operation fails, you receive error information in the form of an `error` object to assist in [troubleshooting](https://docs.cloud.google.com/video-stitcher/docs/troubleshooting).
    
    
    {
      "error": {
        "code": 404,
        "message": "got status code 403 when fetching playlist from URI \"https://example.com/manifest.m3u8\"",
        "status": "NOT_FOUND"
      }
    }
    

## List long-running operations

To list all of the operations in a given location, use the [`projects.locations.operations.list`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the operations; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "operations": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.OperationMetadata",
            "createTime": CREATE_TIME,
            "endTime": END_TIME,
            "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID,
            "verb": "create",
            "requestedCancellation": false,
            "apiVersion": "v1"
          },
          "done": false
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/my-other-operation",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.OperationMetadata",
            "createTime": CREATE_TIME,
            "endTime": END_TIME,
            "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/my-other-live-config",
            "verb": "create",
            "requestedCancellation": false,
            "apiVersion": "v1"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.LiveConfig",
            "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/my-other-live-config",
            "sourceUri": "SOURCE_LIVESTREAM_URI",
            "adTagUri": "AD_TAG_URI",
            "state": "READY",
            "adTracking": "SERVER",
            "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
            "stitchingPolicy": "CUT_CURRENT",
            "defaultAdBreakDuration": "30s"
          }
        }
      ]
    }
    

## Cancel a long-running operation

To start asynchronous cancellation on a long-running operation, use the [`projects.locations.operations.cancel`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/cancel) method. The server makes a best effort to cancel the operation, but success is not guaranteed.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the operation; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID:cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

You should receive an empty JSON object as the response: 
    
    
    {}
    

## Delete a long-running operation

To delete a completed long-running operation, use the [`projects.locations.operations.delete`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/delete) method. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the operation; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive an empty JSON object as the response: 
    
    
    {}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
