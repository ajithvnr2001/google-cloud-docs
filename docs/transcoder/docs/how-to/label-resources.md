---
url: https://docs.cloud.google.com/transcoder/docs/how-to/label-resources/
title: Organize resources with labels \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:26.211322+00:00
---

# Organize resources with labels  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/label-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Organize resources with labels Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to add and view labels on Transcoder API resources. Labels are key-value pairs you can use to organize resources. You can attach a label to individual resources, then filter the resources based on their labels. Information about labels is forwarded to the billing system, so you can [break down your billing charges](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) by label.

You can add labels when creating Transcoder API jobs and job templates. If you create a job based on a job template that contains labels, the job will contain the same labels as the job template. To override the labels from the job template, you can directly specify the labels on the job itself.

**Note:** You cannot add, edit, or remove a label on an existing Transcoder API resource because these resources are immutable.

Labels are available using the REST or RPC APIs. Labels are not available in the Google Cloud CLI or Google Cloud console.

## Label requirements

The labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding and international characters are allowed.
  * The key of a label must be unique in a single resource, but you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.



## Adding a label to a job

The following sample shows how to add a label when creating a new job. For example, you could use a label to signify that the job will be used in a test environment. The key for the label would be `environment` and the value would be `test`.

To create the job, use the [`projects.locations.jobs.create`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * `LOCATION`: The location where your job will run. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

Show locations

    * `us-central1`
    * `us-west1`
    * `us-west2`
    * `us-east1`
    * `us-east4`
    * `southamerica-east1`
    * `northamerica-northeast1`
    * `asia-east1`
    * `asia-northeast1`
    * `asia-northeast3`
    * `asia-south1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west4`
    * `me-west1`
    * `me-central1`
    * `me-central2`
  * `STORAGE_BUCKET_NAME`: The name of the Cloud Storage bucket you created.
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). **Note:** The input video must have at least one video track and one audio track in order to use the [`preset/web-hd` preset](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.template_id).
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "inputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
      "outputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/",
      "templateId": "preset/web-hd",
      "labels": {
        "environment": "test"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "inputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
      "outputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/",
      "templateId": "preset/web-hd",
      "labels": {
        "environment": "test"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0"
            ],
            "startTimeOffset": "0s"
          }
        ],
        "elementaryStreams": [
          {
            "videoStream": {
              "h264": {
                "widthPixels": 640,
                "heightPixels": 360,
                "frameRate": 30,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream0"
          },
          {
            "videoStream": {
              "h264": {
                "widthPixels": 1280,
                "heightPixels": 720,
                "frameRate": 30,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream1"
          },
          {
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "sampleRateHertz": 48000
            },
            "key": "audio-stream0"
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "fileName": "sd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "hd",
            "fileName": "hd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "media-sd",
            "fileName": "media-sd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "media-hd",
            "fileName": "media-hd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "video-only-sd",
            "fileName": "video-only-sd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "video-only-hd",
            "fileName": "video-only-hd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream1"
            ]
          },
          {
            "key": "audio-only",
            "fileName": "audio-only.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "media-sd",
              "media-hd"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "video-only-sd",
              "video-only-hd",
              "audio-only"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30,
      "labels": {
        "environment": "test"
      }
    }
    

To add multiple labels, separate each label by a comma.

## Listing and filtering by labels

You can list resources and filter them by their labels. For example, after adding a label to a job, you can list the jobs in a given location and filter by the labels you added. The following sample lists the jobs and filters out any that do not contain the label `"environment": "test"`.

To list the jobs, use the [`projects.locations.jobs.list`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/list) method. The following filter is appended to the URL: `?filter=labels.environment:test`.

Before using any of the request data, make the following replacements: 

* `PROJECT_ID`: Your Google Cloud project ID.
* `LOCATION`: The location of your jobs. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

Show locations

  * `us-central1`
  * `us-west1`
  * `us-west2`
  * `us-east1`
  * `us-east4`
  * `southamerica-east1`
  * `northamerica-northeast1`
  * `asia-east1`
  * `asia-northeast1`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west4`
  * `me-west1`
  * `me-central1`
  * `me-central2`



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?filter=labels.environment:test"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?filter=labels.environment:test" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "jobs": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/MY_JOB",
          "config": {
            ....
           },
          "state": "PENDING",
          "createTime": CREATE_TIME,
          "ttlAfterCompletionDays": 30,
          "labels": {
            "environment": "test"
          }
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/MY_OTHER_JOB",
          "config": {
            ....
           },
          "state": "SUCCEEDED",
          "createTime": CREATE_TIME,
          "startTime": START_TIME,
          "endTime": END_TIME,
          "ttlAfterCompletionDays": 30,
          "labels": {
            "environment": "test"
          }
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
