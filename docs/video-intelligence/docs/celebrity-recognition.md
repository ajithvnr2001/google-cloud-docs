---
url: https://docs.cloud.google.com/video-intelligence/docs/celebrity-recognition/
title: Recognize celebrities \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:34:16.699266+00:00
---

# Recognize celebrities  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/celebrity-recognition/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Recognize celebrities Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is [deprecated](https://docs.cloud.google.com/video-intelligence/docs/deprecations) and will no longer be available on Google Cloud after September 16, 2025.

This page describes how to recognize celebrities in a video using the Video Intelligence API.

The Video Intelligence API can inspect your video content to detect and track human faces that appear in the input video or video segment. When it recognizes a face, the Video Intelligence API can compare the face against a collection of celebrities collated by Google.

If a match is found, the Video Intelligence API provides the [Knowledge Graph Machine ID (MID)](https://developers.google.com/knowledge-graph/) and the name of the celebrity and a bounding box indicating where the face appears in the video.

## Request access to the feature

This feature is intended for use by media & entertainment companies or approved partners on professionally-produced media content. To request API access, please submit [this form](https://docs.google.com/forms/d/e/1FAIpQLSenUFSRovp05e4ags9g2cWCAU-mUuSNPoBmRQm9Lg4B8k5KNw/viewform) with information about your company and use case.

## Recognize a celebrity in a video

The following code samples demonstrate how to recognize a celebrity's face in a video. The sample uses the optional `outputUri` field in the request to specify a location for the annotation results.

**Note:** The `outputUri` field indicates a Cloud Storage bucket to store the annotation output. Before sending a request, ensure that your service account has write access to the output Cloud Storage bucket.

### REST

### Send the request

The following shows how to send a `POST` request to the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1p3beta1/videos/annotate) method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: the Cloud Storage location of the video file you want to annotate.
  * OUTPUT_URI: the Cloud Storage location where you want the results saved.
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1p3beta1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "gs://INPUT_URI",
      "outputUri": "gs://OUTPUT_URI",
      "features": ["CELEBRITY_RECOGNITION"]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videointelligence.googleapis.com/v1p3beta1/videos:annotate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videointelligence.googleapis.com/v1p3beta1/videos:annotate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    
    

If the request is successful, the Video Intelligence returns the name for your operation.

### Get the results

To get the results of your request, you must send a `GET` request to the [projects.operations](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) resource. The following shows how to send such a request.

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
    

The output from annotating the video should look similar to the following example.
    
    
    
    {
      "annotationResults": [ {
        "inputUri": "INPUT_URI,
        "segment": {
          "startTimeOffset": {
    
          },
          "endTimeOffset": {
            "seconds": 19,
            "nanos": 519500000
          }
        },
        "celebrityRecognitionAnnotations": {
          "celebrityTracks": [ {
            "celebrities": [...],
            "faceTrack": {...}
          }, {
            "celebrities": [ {
              "celebrity": {
                "name": "video-intelligence/CELEBRITY_MID",
                "displayName": "CELEBRITY_NAME/var>"
              },
              "confidence": 0.81873637
            } ],
            "faceTrack": {
              "segment": {
                "startTimeOffset": {
                  "seconds": 1,
                  "nanos": 459791000
                },
                "endTimeOffset": {
                  "seconds": 3,
                  "nanos": 712041000
                }
              },
              "timestampedObjects": [ {
                "normalizedBoundingBox": {...},
                "timeOffset": {...}
              }, {
                "normalizedBoundingBox": {
                  "left": 0.38046876,
                  "top": 0.26249999,
                  "right": 0.60312498,
                  "bottom": 0.72361112
                },
                "timeOffset": {
                  "seconds": 1,
                  "nanos": 459791000
                }
              }, {
                "normalizedBoundingBox": {...},
                "timeOffset": {...}
              }]
            }
          }, {
            "celebrities": [...],
            "faceTrack": {...}
          } ]
        }
        ...
    }
    
    

## Request celebrity opt-out

If you are a celebrity and would like not to be included in this feature for either the Cloud Vision or Video Intelligence API please submit [this form](https://docs.google.com/forms/d/e/1FAIpQLSeNI_qkhnUy2yGt1COZkfPwCMJnf-w-5lv5G5i7_Xl0PZyY2w/viewform?usp=sf_link).

## Report misuse

If you suspect that the Video Intelligence API celebrity recognition feature is being misused in any way, please let us know using [this form.](https://docs.google.com/forms/d/e/1FAIpQLSdQtYOpeQsGu52S9VycFc1Bl0yiJPlHKE7SFz4CVuIg5ascgg/viewform?usp=sf_link)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
