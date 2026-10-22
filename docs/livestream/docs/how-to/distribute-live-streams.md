---
url: https://docs.cloud.google.com/livestream/docs/how-to/distribute-live-streams/
title: Distribute live streams to remote endpoints \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:46.329148+00:00
---

# Distribute live streams to remote endpoints  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/distribute-live-streams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Distribute live streams to remote endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to distribute the live stream output to remote endpoints using the Secure Reliable Transport (SRT) protocol or the Real-Time Messaging Protocol (RTMP). Both SRT and RTMP are used in push mode to send the stream to the endpoints. The supported container formats are MPEG-TS for SRT and FLV for RTMP.

## Before you begin

This page assumes that you have completed the steps in the **Before you begin** section of the [Quickstart for an HLS live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-hls).

Depending on your choice of distribution protocol, create an SRT or an RTMP endpoint on the provider where you want to receive the output in push mode. The endpoint URI format varies according to protocol:

  * For SRT: `srt://SRT_SERVER_IP:SRT_SERVER_PORT?streamid=SRT_SERVER_STREAM_ID`
  * For RTMP: `rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME/RTMP_STREAM_KEY` or just `rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME`



SRT_SERVER_IP and RTMP_SERVER_IP can be either an IP address or a domain name.

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
    

Copy the returned OPERATION_ID to use in the next section.

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.operations/get) method to check if the input endpoint has been created. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`. Creating the first input endpoint in a region may take up to 10 minutes.

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
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.Input",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "type": "RTMP_PUSH",
        "uri":  INPUT_STREAM_URI, # For example, "rtmp://1.2.3.4/live/b8ebdd94-c8d9-4d88-a16e-b963c43a953b",
        "tier": "HD"
      }
    }
    

Find the `uri` field and copy the returned INPUT_STREAM_URI to use later in the Send the input stream section.

## Create the channel

To create the channel, use the [`projects.locations.channels.create`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/create) method.

Note the following in the channel configuration:

  * The [`distributionStreams`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.distribution_streams) array contains the multiplexing settings of streams for distributions.
  * Each [`DistributionStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream) object must include a [`key`](https://docs.cloud.google.com/livestream/docsreference/rest/v1/projects.locations.channels#DistributionStream.FIELDS.key), [`container`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream.FIELDS.container), and [`elementaryStreams`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream.FIELDS.elementary_streams) field.
        
        {
          "distributionStreams": [
            {
              "key": "ds1",
              "container": "ts", // to be used with an SRT distribution
              "elementaryStreams": [
                "es_video_720",
                "es_audio"
              ]
            },
            {
              "key": "ds2",
              "container": "flv", // to be used with an RTMP distribution
              "elementaryStreams": [
                "es_video_640",
                "es_audio"
              ]
            }
          ]
        }
        

  * The [`distributions`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.distributions) array lists the distribution configurations, which includes the remote endpoints.

  * Set the [`distributionStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Distribution.FIELDS.distribution_stream) field in the [`Distribution`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Distribution) object to the [`key`](https://docs.cloud.google.com/livestream/docsreference/rest/v1/projects.locations.channels#DistributionStream.FIELDS.key) of a [`DistributionStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream) object.

  * For SRT distribution set the [`uri`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#SrtPushOutputEndpoint.FIELDS.uri) in the [`SrtPushOutputEndpoint`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#SrtPushOutputEndpoint) object to an SRT endpoint that you created. For RTMP distribution, set the [`uri`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#RtmpPushOutputEndpoint.FIELDS.uri) in the [`RtmpPushOutputEndpoint`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#RtmpPushOutputEndpoint) object to an RTMP endpoint that you created.
        
        {
          "distributions": [
            {
              "key": "pd1",
              "distributionStream": "ds1", // defined in a distributionStreams[] object with an MPEG-TS container
              "srtPush": {
                "uri": "srt://SRT_SERVER_IP:SRT_SERVER_PORT?streamid=SRT_SERVER_STREAM_ID"
              }
            },
            {
              "key": "pd2",
              "distributionStream": "ds2", // defined in a distributionStreams[] object with an FLV container
              "rtmpPush": {
                "uri": "rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME/",
                "streamKey": "RTMP_STREAM_KEY"
              }
            }
          ]
        }
        

  * To distribute AI-generated captions and translated captions, refer to the [configuring automatic captions and translations](https://docs.cloud.google.com/livestream/docs/how-to/configure-captions-and-translations#distribute-embedded-captions) guide.




The following samples use only one [`DistributionStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream) object and one [`Distribution`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Distribution) object.

### REST

### SRT

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
  * `SRT_SERVER_IP`: the IP address or domain name of the remote endpoint
  * `SRT_SERVER_PORT`: the port number of the remote endpoint
  * `SRT_SERVER_STREAM_ID`: the stream ID of the remote endpoint



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
      },
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
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "ts",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "srtPush": {
            "uri": "srt://SRT_SERVER_IP:SRT_SERVER_PORT?streamid=SRT_SERVER_STREAM_ID"
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
      },
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
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "ts",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "srtPush": {
            "uri": "srt://SRT_SERVER_IP:SRT_SERVER_PORT?streamid=SRT_SERVER_STREAM_ID"
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
    

### RTMP

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
  * `RTMP_SERVER_IP`: the IP address or domain name of the remote endpoint
  * `RTMP_SERVER_PORT`: the port number of the remote endpoint
  * `RTMP_APP_NAME`: the path prefix for the stream name
  * `RTMP_STREAM_KEY`: the stream key of the remote endpoint



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
      },
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
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "flv",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "rtmpPush": {
            "uri": "rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME",
            "streamKey": "RTMP_STREAM_KEY"
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
      },
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
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "flv",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "rtmpPush": {
            "uri": "rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME",
            "streamKey": "RTMP_STREAM_KEY"
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
    

You can check for the result of the operation using the new operation ID.

### Get the channel

After the channel has been created, use the [`projects.locations.channels.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/get) method to query the channel state.

### REST

### SRT

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
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
      "createTime": CREATE_TIME,
      "updateTime": UPDATE_TIME,
      "inputAttachments": [
        {
          "key": "INPUT_ID",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "activeInput": "INPUT_ID",
      "output": {
        "uri": "gs://BUCKET_NAME"
      },
      "elementaryStreams": [
        {
          "videoStream": {
            "h264": {
              "widthPixels": 1280,
              "heightPixels": 720,
              "frameRate": 30,
              "bitrateBps": 3000000,
              "gopDuration": "2s",
              "vbvSizeBits": 3000000,
              "vbvFullnessBits": 2700000,
              "entropyCoder": "cabac",
              "profile": "high"
            }
          },
          "key": "es_video"
        },
        {
          "audioStream": {
            "codec": "aac",
            "bitrateBps": 160000,
            "channelCount": 2,
            "sampleRateHertz": 48000
          },
          "key": "es_audio"
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_ts",
          "container": "ts",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }
      ],
      "manifests": [
        {
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts"
          ],
          "maxSegmentCount": 5,
          "segmentKeepDuration": "60s",
          "key": "manifest_hls"
        }
      ],
      "streamingState": "STOPPED",
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "ts",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "state": "NOT_READY",
          "srtPush": {
            "uri": "srt://SRT_SERVER_IP:SRT_SERVER_PORT?streamid=SRT_SERVER_STREAM_ID"
          }
        }
      ]
    }
    

### RTMP

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
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
      "createTime": CREATE_TIME,
      "updateTime": UPDATE_TIME,
      "inputAttachments": [
        {
          "key": "INPUT_ID",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "activeInput": "INPUT_ID",
      "output": {
        "uri": "gs://BUCKET_NAME"
      },
      "elementaryStreams": [
        {
          "videoStream": {
            "h264": {
              "widthPixels": 1280,
              "heightPixels": 720,
              "frameRate": 30,
              "bitrateBps": 3000000,
              "gopDuration": "2s",
              "vbvSizeBits": 3000000,
              "vbvFullnessBits": 2700000,
              "entropyCoder": "cabac",
              "profile": "high"
            }
          },
          "key": "es_video"
        },
        {
          "audioStream": {
            "codec": "aac",
            "bitrateBps": 160000,
            "channelCount": 2,
            "sampleRateHertz": 48000
          },
          "key": "es_audio"
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_ts",
          "container": "ts",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }
      ],
      "manifests": [
        {
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts"
          ],
          "maxSegmentCount": 5,
          "segmentKeepDuration": "60s",
          "key": "manifest_hls"
        }
      ],
      "streamingState": "STOPPED",
      "distributionStreams": [
        {
          "key": "ds1",
          "container": "flv",
          "elementaryStreams": [
            "es_video",
            "es_audio"
          ]
        }
      ],
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1",
          "state": "NOT_READY",
          "rtmpPush": {
            "uri": "rtmp://RTMP_SERVER_IP:RTMP_SERVER_PORT/RTMP_APP_NAME",
            "streamKey": "RTMP_STREAM_KEY"
          }
        }
      ]
    }
    

The full response contains the following fields:
    
    
    {
      ...
      "streamingState": "STOPPED",
      "distributions": [
        {
          ...
          "state": "NOT_READY"
          ...
        }
      ]
      ...
    }
    

This response indicates the streaming state of the channel and the channel distributions.

If the distribution is in a `NOT_READY` [state](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#state), the distribution cannot be started. You must wait until the state has changed to `READY` to be able to start distributing your stream. 

Creating the first distribution stream may take up to 10 minutes. The state of the distribution is independent from the channel state; you can start the channel and wait for the distribution to become `READY` and then start the distribution.

You can now start the channel.

## Start the channel

Use the [`projects.locations.channels.start`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/start) method to start the channel. A channel must be started before it can accept input streams or generate an output stream.

Starting the first channel in a region takes about 10 minutes.

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
    

To determine if the channel has started, get the channel information as done previously. The response should contain the following:
    
    
    {
      ...
      "streamingState": "AWAITING_INPUT"
      ...
    }
    

## Send the input stream

Open a new terminal window. Run the following command, using INPUT_STREAM_URI from the Check for the result section:
    
    
    ffmpeg -re -f lavfi -i "testsrc=size=1280x720 [out0]; sine=frequency=500 [out1]" \
      -acodec aac -vcodec h264 -f flv INPUT_STREAM_URI
    

The channel is now streaming, but the distributions are still stopped.

## Start the distributions

The distributions must be in the `READY` state to be started. To start distributing the live stream output to all remote endpoints, use the [`projects.locations.channels.startdistribution`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/startdistribution) method.

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
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:startdistribution"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:startdistribution" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "startdistribution",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID. After starting a distribution, it can be in the `AWAITING_INPUT` state if the input stream is not started or the `DISTRIBUTING` state if the input stream is being distributed to the specified endpoints.

### (Optional) Start a set of distributions

You can start a set of distributions rather than all of them at once. List the distributions that you want to start by adding their keys to the [`distributionKeys`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/startdistribution#body.request_body.FIELDS.distribution_keys) array list.

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
  * `DISTRIBUTION_KEYS`: a comma-separated list of string keys (for example, `"pd1"`)



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "distributionKeys": [
        DISTRIBUTION_KEYS
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:startdistribution"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "distributionKeys": [
        DISTRIBUTION_KEYS
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:startdistribution" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "startdistribution",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

## Verify that the distributions are running

To verify that the distributions started, get the channel information as done previously. The response should contain the following:
    
    
    {
      "distributions": [
        {
          ...
          "state": "DISTRIBUTING"
          ...
        },
        ...
      ]
    }
    

On the remote SRT or RTMP server, verify that the endpoint you created is receiving data.

## Stop the distributions

To stop distributing the live stream output to all remote endpoints, use the [`projects.locations.channels.stopdistribution`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/stopdistribution) method.

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
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stopdistribution"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stopdistribution" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "stopdistribution",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

**Note:** Stopping a channel stops all of the running distributions by default. If you start the channel again, the distributions won't resume running by default. You need to start the distributions again.

### (Optional) Stop a set of distributions

You can stop a set of distributions rather than all of them at once. List the distributions that you want to stop by adding their keys to the [`distributionKeys`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/startdistribution#body.request_body.FIELDS.distribution_keys) array list.

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
  * `DISTRIBUTION_KEYS`: a comma-separated list of string keys (for example, `"pd1"`)



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "distributionKeys": [
        DISTRIBUTION_KEYS
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stopdistribution"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "distributionKeys": [
        DISTRIBUTION_KEYS
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
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stopdistribution" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "stopdistribution",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

## SRT encryption support

If you use the SRT protocol to distribute the live stream output to the remote endpoint, Live Stream API protects your live stream content with AES encryption.

### Create the passphrase and prepare the remote SRT server

Before you begin, create an SRT passphrase which complies with the remote SRT server. The passphrase should typically be a string of 10-79 characters.

Ensure the decryption process works by setting the same passphrase in the remote SRT server. Refer to the user guide of the remote SRT server for how to do so.

### Add the passphrase to Secret Manager

**Live Stream API does not accept or manage the passphrase directly.** You must share the passphrase with the Live Stream API through Google Secret Manager.

You must complete all these steps before configuring the channel:

  1. Create a secret with the Secret Manager.
  2. Configure Identity and Access Management permissions on your secret so that the Live Stream API can access the secret content. To do this, grant the `secretmanager.secretAccessor` role to the `service-PROJECT_NUMBER@gcp-sa-livestream.iam.gserviceaccount.com` service account (this is similar to how the [service account has access to your Cloud Storage buckets](https://docs.cloud.google.com/livestream/docs/access-control#access_to_gcs)).
  3. Find the resource name of the secret version you created (for example, `projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/VERSION_ID`). You need this name to configure the channel.



### Configure the channel

The secret version of the passphrase is specified within the [`SrtPushOutputEndpoint`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#SrtPushOutputEndpoint):
    
    
    {
      "distributions": [
        {
          "key": "pd1",
          "distributionStream": "ds1", // defined in a distributionStreams[] object with an MPEG-TS container
          "srtPush": {
            "uri": "srt://{SRT_SERVER_IP}:{SRT_SERVER_PORT}?streamid={SRT_SERVER_STREAM_ID}",
            "passphrase_secret_version": "projects/PROJECT_NUMBER/secrets/key1/versions/1"
          }
        }
      ]
    }
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

### Stop the channel

Use the [`projects.locations.channels.stop`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/stop) method to stop the channel. You must stop the channel before you can delete it.

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
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stop"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID:stop" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "stop",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

### Stop the input stream

If you used `ffmpeg` to send the input stream, the connection is automatically broken after you stop the channel.

### Delete the channel

Use the [`projects.locations.channels.delete`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/delete) method to delete the channel. You must delete the channel before you can delete the input endpoint that is used by the channel.

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
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

### Delete the input endpoint

Use the [`projects.locations.inputs.delete`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/delete) method to delete the input endpoint.

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
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

### Delete the Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage Browser page.

[Go to the Cloud Storage Browser page](https://console.cloud.google.com/storage/browser)

  2. Select the checkbox next to the bucket that you created.

  3. Click **Delete**.

  4. In the dialog window that appears, click **Delete** to delete the bucket and its contents.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
