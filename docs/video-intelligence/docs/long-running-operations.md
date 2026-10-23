---
url: https://docs.cloud.google.com/video-intelligence/docs/long-running-operations/
title: Long-running operations \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:41.065932+00:00
---

# Long-running operations  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/long-running-operations/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Some methods of the Video Intelligence API return a long-running operation. These methods are asynchronous, and the operation may not be completed when the method returns a response.

**Note:** Video Intelligence API does not support the `PageToken`, or `pageSize` parameters.

## Get an operation status

You can check the status of a long-running task ([detecting shot changes](https://docs.cloud.google.com/video-intelligence/docs/analyze-shots)) using the operation name.

**Note:** When using the Web UI you can monitor the status in the **Status** column of the list page.

### REST

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the `name` field returned from the call to Video Intelligence API. This is a value in the format:  
`projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID`,  
where: 
    * PROJECT_NUMBER is the [number](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project,
    * LOCATION_ID is the cloud region where annotation took place (for example: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`),
    * OPERATION_ID is the ID of the long-running operation.



HTTP method and URL: 
    
    
    GET https://videointelligence.googleapis.com/v1/OPERATION_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         "https://videointelligence.googleapis.com/v1/OPERATION_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videointelligence.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1p3beta1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputUri": "INPUT_URI",
            "progressPercent": 100,
            "startTime": "2020-05-12T19:36:09.110351Z",
            "updateTime": "2020-05-12T19:36:17.519069Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1p3beta1.AnnotateVideoResponse",
        "annotationResults": [
          {
            ...
          }
        ]
      }
    }
    

## Cancel an operation

You can cancel a long-running operation using the operation ID. However, cancellation is not guaranteed to succeed.

### REST

Before using any of the request data, make the following replacements: 

  * OPERATION_ID: provided in the response when you started the operation,  
for example `3326639765503758657` from `projects/754177431483/locations/us-west1/operations/3326639765503758657`
  * Note: 
    * PROJECT_NUMBER: your GCP project ID
    * LOCATION_ID: the Cloud region where annotation should take place. Supported cloud regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no region is specified, a region will be determined based on video file location.



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID:cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://videointelligence.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID:cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://videointelligence.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
