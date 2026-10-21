---
url: https://docs.cloud.google.com/livestream/docs/how-to/create-channel-clips/
title: Create and manage channel clips \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:56.529637+00:00
---

# Create and manage channel clips  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/create-channel-clips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Create and manage channel clips Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create and manage Live Stream API channel clips. A channel clip is a sub-resource of a channel. You can use a channel clip to create video on demand (VOD) files from a live stream. These VOD files are saved to Cloud Storage. For more information, see [Create VOD clips from a live stream](https://docs.cloud.google.com/livestream/docs/how-to/live-to-vod).

## Set up your Google Cloud project and authentication

If you have not created a [Google Cloud project](https://docs.cloud.google.com/docs/overview#projects) and credentials, see [Before you begin](https://docs.cloud.google.com/livestream/docs/how-to/before-you-begin). 

## Prerequisites

You must create the following resources before creating a channel clip:

  1. [Create an input endpoint](https://docs.cloud.google.com/livestream/docs/how-to/create-input-endpoints#create_input_endpoint)

  2. [Create a channel](https://docs.cloud.google.com/livestream/docs/how-to/live-to-vod#create-channel) with a [retention config](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.retention_config)




## Create a channel clip

Make sure to [start the channel](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#start_channel) and start streaming content to the channel before creating a channel clip.

To create a channel clip, use the [`projects.locations.channels.clips.create`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your channel is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-east4`
    * `us-west1`
    * `us-west2`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `asia-east1`
    * `asia-east2`
    * `asia-south1`
    * `asia-northeast1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-north1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
  * `CHANNEL_ID`: a user-defined identifier for the channel
  * `CLIP_ID`: a user-defined identifier for the VOD clip
  * `MARK_IN_TIME`: the mark-in Unix epoch time in the original live stream manifest; uses a timestamp in RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`)
  * `MARK_OUT_TIME`: the mark-out Unix epoch time in the original live stream manifest; uses a timestamp in RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`)
  * `BUCKET_NAME`: the name of the Cloud Storage bucket you created to hold the VOD clip manifest and segment files; you can use the same bucket you created for the live stream manifest or a different bucket; you can also append a directory name to the bucket name (for example `my-bucket/vod-clip`) 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "outputUri": "gs://BUCKET_NAME",
      "clipManifests":[
        {
          "manifestKey": "manifest_hls"
        }
      ],
      "slices":[
        {
          "timeSlice": {
            "markinTime": "MARK_IN_TIME",
            "markoutTime": "MARK_OUT_TIME"
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips?clipId=CLIP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "outputUri": "gs://BUCKET_NAME",
      "clipManifests":[
        {
          "manifestKey": "manifest_hls"
        }
      ],
      "slices":[
        {
          "timeSlice": {
            "markinTime": "MARK_IN_TIME",
            "markoutTime": "MARK_OUT_TIME"
          }
        }
      ]
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips?clipId=CLIP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a long-running operation (LRO) that you can use to track the progress of your request. See [Manage long-running operations ](https://docs.cloud.google.com/livestream/docs/how-to/manage-long-running-operations) for more information. 

## Get channel clip details

To get the details of a channel clip, use the [`projects.locations.channels.clips.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your channel is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-east4`
    * `us-west1`
    * `us-west2`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `asia-east1`
    * `asia-east2`
    * `asia-south1`
    * `asia-northeast1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-north1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
  * `CHANNEL_ID`: a user-defined identifier for the channel
  * `CLIP_ID`: a user-defined identifier for the VOD clip



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID",
      "createTime": CREATE_TIME,
      "startTime": START_TIME,
      "updateTime": UPDATE_TIME,
      "state": "SUCCEEDED",
      "outputUri": "gs://BUCKET_NAME",
      "slices": [
        {
          "timeSlice": {
            "markinTime": "MARK_IN_TIME",
            "markoutTime": "MARK_OUT_TIME"
          }
        }
      ],
      "features": {},
      "clipManifests": [
        {
          "manifestKey": "manifest_hls",
          "outputUri": "gs://BUCKET_NAME/main.m3u8"
        }
      ]
    }
    

Only the most recent 1000 clip job records per channel are available using the [`projects.locations.channels.clips.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/get) method. Any clip job records older than the limit are removed. You must manage the generated clip files specified by the [`outputUri`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#ClipManifest.FIELDS.output_uri); the Live Stream API does not delete these files from Cloud Storage. 

## List channel clips

To list all of the channel clips you created for a channel, use the [`projects.locations.channels.clips.list`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your channel is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-east4`
    * `us-west1`
    * `us-west2`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `asia-east1`
    * `asia-east2`
    * `asia-south1`
    * `asia-northeast1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-north1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
  * `CHANNEL_ID`: a user-defined identifier for the channel



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
        "clips": [
          {
            "name": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID",
            "createTime": CREATE_TIME,
            "startTime": START_TIME,
            "updateTime": UPDATE_TIME,
            "state": "SUCCEEDED",
            "outputUri": "gs://BUCKET_NAME",
            "slices": [
              {
                "timeSlice": {
                  "markinTime": "MARK_IN_TIME",
                  "markoutTime": "MARK_OUT_TIME"
                }
              }
            ],
            "features": {},
            "clipManifests": [
              {
                "manifestKey": "manifest_hls",
                "outputUri": "gs://BUCKET_NAME/main.m3u8"
              }
            ]
          },
          {
            "name": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/my-clip2",
            "createTime": CREATE_TIME,
            "startTime": START_TIME,
            "updateTime": UPDATE_TIME,
            "state": "SUCCEEDED",
            "outputUri": "gs://BUCKET_NAME",
            "slices": [
              {
                "timeSlice": {
                  "markinTime": "MARK_IN_TIME",
                  "markoutTime": "MARK_OUT_TIME"
                }
              }
            ],
            "features": {},
            "clipManifests": [
              {
                "manifestKey": "manifest_hls",
                "outputUri": "gs://BUCKET_NAME/main.m3u8"
              }
            ]
          }
      ]
    }
    

## Delete a channel clip

To delete a channel clip, use the [`projects.locations.channels.clips.delete`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/delete) method. This method only deletes the clipping task. The VOD resources created in the Cloud Storage bucket are not managed by the Live Stream API and are not deleted.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your channel is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-east4`
    * `us-west1`
    * `us-west2`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `asia-east1`
    * `asia-east2`
    * `asia-south1`
    * `asia-northeast1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-north1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west4`
  * `CHANNEL_ID`: a user-defined identifier for the channel
  * `CLIP_ID`: a user-defined identifier for the VOD clip



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID/clips/CLIP_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a long-running operation (LRO) that you can use to track the progress of your request. See [Manage long-running operations ](https://docs.cloud.google.com/livestream/docs/how-to/manage-long-running-operations) for more information. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
