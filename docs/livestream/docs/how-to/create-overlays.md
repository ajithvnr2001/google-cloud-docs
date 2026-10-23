---
url: https://docs.cloud.google.com/livestream/docs/how-to/create-overlays/
title: Create static overlays \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:27.756123+00:00
---

# Create static overlays  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/create-overlays/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Create static overlays Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to generate static overlay images on top of a live stream. A static overlay image persists during the entire live stream. You can configure the resolution and position of a static overlay image.

## Set up your Google Cloud project and authentication

If you have not created a [Google Cloud project](https://docs.cloud.google.com/docs/overview#projects) and credentials, see [Before you begin](https://docs.cloud.google.com/livestream/docs/how-to/before-you-begin). 

## Upload an image to your Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage Browser page.  
[Go to the Cloud Storage Browser page](https://console.cloud.google.com/storage/browser)  

  2. Click the name of your bucket to open it.
  3. Click **Upload files**.
  4. Select an image file (JPEG or PNG) to upload from your local machine. You can use this [sample overlay image](https://docs.cloud.google.com/static/livestream/images/overlay.png).



Your image is now saved to the Cloud Storage bucket.

## Create an asset

Assets are [video](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.assets#videoasset) or [images](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.assets#imageasset) that can be used with the Live Stream API. Create an image asset to use as a static overlay.

To create an asset, use the [`projects.locations.assets.create`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.assets/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create the asset; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

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
  * `ASSET_ID`: A user-defined identifier for the new asset to create. This value must be 1-63 characters, begin and end with `[a-z0-9]`, and can contain dashes (-) between characters. For example, `my-asset`.
  * `ASSET_URI`: the URI of the image in your Cloud Storage bucket to use, such as `gs://my-bucket/my-image.png`



Request JSON body: 
    
    
    {
      "image": {
        "uri": "ASSET_URI"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "image": {
        "uri": "ASSET_URI"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/assets?assetId=ASSET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "image": {
        "uri": "ASSET_URI"
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/assets?assetId=ASSET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Copy the returned `OPERATION_ID` to use in the next section.

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.operations/get) method to check if the asset has been created. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your asset is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

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
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "endTime": END_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.Asset",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "image": {
          "uri": "ASSET_URI"
        },
        "crc32c": "ae1EJg==",
        "state": "ACTIVE"
      }
    }
    

## Create the input endpoint

To create the input endpoint, use the [`projects.locations.inputs.create`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create the input endpoint; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

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
  * `INPUT_ID`: a user-defined identifier for the new input endpoint to create (to which you send your input stream). This value must be 1-63 characters, begin and end with `[a-z0-9]`, and can contain dashes (-) between characters. For example, `my-input`.



Request JSON body: 
    
    
    {
      "type": "RTMP_PUSH"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "type": "RTMP_PUSH"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs?inputId=INPUT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "type": "RTMP_PUSH"
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs?inputId=INPUT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the input creation operation using the new operation ID.

## Get input endpoint details

To get the details of the input endpoint, use the [`projects.locations.inputs.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your input endpoint is located; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

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
  * `INPUT_ID`: the user-defined identifier for the input endpoint



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID",
      "createTime": CREATE_TIME,
      "updateTime": UPDATE_TIME,
      "type": "RTMP_PUSH",
      "uri":  "INPUT_STREAM_URI", # For example, "rtmp://1.2.3.4/live/b8ebdd94-c8d9-4d88-a16e-b963c43a953b",
      "tier": "HD"
    }
    

Find the `uri` field and copy the returned `INPUT_STREAM_URI` to use later in the Send the input stream section.

## Create the channel

To create the channel, use the [`projects.locations.channels.create`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/create) method.

Note the [`staticOverlays`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.static_overlays) array in the channel configuration:
    
    
    "staticOverlays": [
      {
        "asset": "projects/PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
        "position": {
          "x": 0.5,
          "y": 0.5
        },
        "resolution": {
          "w": 0.1
        },
        "opacity": 0.8
      }
    ],
    

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create the channel; use one of the [supported regions](https://docs.cloud.google.com/livestream/docs/locations)

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
  * `CHANNEL_ID`: a user-defined identifier for the channel to create; this value must be 1-63 characters, begin and end with `[a-z0-9]`, and can contain dashes (-) between characters
  * `INPUT_ID`: the user-defined identifier for the input endpoint
  * `BUCKET_NAME`: the name of the Cloud Storage bucket you created to hold the live stream manifest and segment files
  * `ASSET_ID`: the user-defined identifier for the asset



Request JSON body: 
    
    
    {
      "inputAttachments": [
        {
          "key": "my-input",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "output": {
        "uri": "gs://BUCKET_NAME"
      },**"staticOverlays": [
        {
          "asset": "projects/ PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
          "position": {
            "x": 0.5,
            "y": 0.5
          },
          "resolution": {
            "w": 0.1
          },
          "opacity": 0.8
        },
      ],**
      "elementaryStreams": [
        {
          "key": "es_video",
          "videoStream": {
            "h264": {
              "profile": "high",
              "widthPixels": 1280,
              "heightPixels": 720,
              "bitrateBps": 3000000,
              "frameRate": 30
            }
          }
        },
        {
          "key": "es_audio",
          "audioStream": {
            "codec": "aac",
            "channelCount": 2,
            "bitrateBps": 160000
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_ts",
          "container": "ts",
          "elementaryStreams": ["es_video", "es_audio"],
          "segmentSettings": { "segmentDuration": "2s" }
        }
      ],
      "manifests": [
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts"
          ],
          "maxSegmentCount": 5
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "inputAttachments": [
        {
          "key": "my-input",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "output": {
        "uri": "gs://BUCKET_NAME"
      },**"staticOverlays": [
        {
          "asset": "projects/ PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
          "position": {
            "x": 0.5,
            "y": 0.5
          },
          "resolution": {
            "w": 0.1
          },
          "opacity": 0.8
        },
      ],**
      "elementaryStreams": [
        {
          "key": "es_video",
          "videoStream": {
            "h264": {
              "profile": "high",
              "widthPixels": 1280,
              "heightPixels": 720,
              "bitrateBps": 3000000,
              "frameRate": 30
            }
          }
        },
        {
          "key": "es_audio",
          "audioStream": {
            "codec": "aac",
            "channelCount": 2,
            "bitrateBps": 160000
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_ts",
          "container": "ts",
          "elementaryStreams": ["es_video", "es_audio"],
          "segmentSettings": { "segmentDuration": "2s" }
        }
      ],
      "manifests": [
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts"
          ],
          "maxSegmentCount": 5
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels?channelId=CHANNEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "inputAttachments": [
        {
          "key": "my-input",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "output": {
        "uri": "gs://BUCKET_NAME"
      },**"staticOverlays": [
        {
          "asset": "projects/ PROJECT_NUMBER/locations/LOCATION/assets/ASSET_ID",
          "position": {
            "x": 0.5,
            "y": 0.5
          },
          "resolution": {
            "w": 0.1
          },
          "opacity": 0.8
        },
      ],**
      "elementaryStreams": [
        {
          "key": "es_video",
          "videoStream": {
            "h264": {
              "profile": "high",
              "widthPixels": 1280,
              "heightPixels": 720,
              "bitrateBps": 3000000,
              "frameRate": 30
            }
          }
        },
        {
          "key": "es_audio",
          "audioStream": {
            "codec": "aac",
            "channelCount": 2,
            "bitrateBps": 160000
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_ts",
          "container": "ts",
          "elementaryStreams": ["es_video", "es_audio"],
          "segmentSettings": { "segmentDuration": "2s" }
        }
      ],
      "manifests": [
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts"
          ],
          "maxSegmentCount": 5
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels?channelId=CHANNEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the channel creation operation using the new operation ID.

## Start the channel

To start a channel, use the [`projects.locations.channels.start`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/start) method.

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
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:start"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:start" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "start",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the channel start operation using the new operation ID.

## Send the input stream

Open a new terminal window. Run the following command, using `INPUT_STREAM_URI` from the Get input endpoint details section:
    
    
    ffmpeg -re -f lavfi -i "testsrc=size=1280x720 [out0]; sine=frequency=500 [out1]" \
      -acodec aac -vcodec h264 -f flv INPUT_STREAM_URI
    

## Play the generated live stream

To play the generated media file in [Shaka Player](https://shaka-player-demo.appspot.com/demo/), complete the following steps:

  1. [Make the Cloud Storage bucket you created publicly readable](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#buckets).
  2. To [enable cross-origin resource sharing (CORS) on a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/using-cors#configure-cors-bucket), do the following: 
     1. Create a JSON file that contains the following: 
            
            [
              {
                "origin": ["https://shaka-player-demo.appspot.com/"],
                "responseHeader": ["Content-Type", "Range"],
                "method": ["GET", "HEAD"],
                "maxAgeSeconds": 3600
              }
            ]

     2. Run the following command after replacing `JSON_FILE_NAME` with the name of the JSON file you created in the previous step: 
            
            gcloud storage buckets update gs://BUCKET_NAME --cors-file=JSON_FILE_NAME.json

  3. In the Cloud Storage bucket, find the generated `main.m3u8` file. Click **Copy URL** in the file's **Public access** column.
  4. Navigate to [Shaka Player](https://shaka-player-demo.appspot.com/demo/), an online live stream player.
  5. Click **Custom Content** in the top navigation bar.
  6. Click the **+** button.
  7. Paste the public URL of the file into the **Manifest URL** box.

![](https://docs.cloud.google.com/static/livestream/images/shaka-player.png)

  8. Type a name in the **Name** box.

  9. Click **Save**.

  10. Click **Play**.




You should see the overlay appear over the live stream.

![Test pattern video](https://docs.cloud.google.com/static/livestream/images/test-livestream-overlay.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
