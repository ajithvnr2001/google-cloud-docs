---
url: https://docs.cloud.google.com/livestream/docs/how-to/configure-captions-and-translations/
title: Configure automatic captions and translations \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:14.767872+00:00
---

# Configure automatic captions and translations  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/configure-captions-and-translations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Configure automatic captions and translations Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure AI-generated captions and translated captions (that is, translations) for a live stream.

AI-generated captions and translations are supported for HLS and DASH live streams.

## Before you begin

This page assumes that you have completed the steps in the **Before you begin** section of the [Quickstart for an HLS live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-hls) or the [Quickstart for an MPEG-DASH live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-dash).

## Supported locations

Language codes for AI-generated captions are supported on a per-location basis. 

Show locations

Location | Supported language codes  
---|---  
`asia-northeast1` | `en-US`  
`asia-south1` | `en-IN`  
`en-GB`  
`en-US`  
`asia-southeast1` | `en-US`  
`australia-southeast1` | `en-AU`  
`europe-west1` | `da-DK`  
`nl-NL`  
`en-GB`  
`en-US`  
`fr-FR`  
`de-DE`  
`it-IT`  
`es-ES`  
`europe-west2` | `en-GB`  
`europe-west3` | `da-DK`  
`nl-NL`  
`en-GB`  
`en-US`   
`fr-FR`  
`de-DE`  
`it-IT`  
`es-ES`  
`northamerica-northeast1` | `en-CA`  
`fr-CA`  
`us-central1` | `en-US`  
`pt-BR`  
`es-CO`  
`es-MX`  
`es-US`  
`us-east1` | `en-US`  
`pt-BR`  
`es-CO`  
`es-MX`  
`es-US`  
`us-west1` | `en-US`  
`pt-BR`  
`es-CO`  
`es-MX`  
`es-US`  
  
The AI-generated translation feature is only supported on `us-west1` and `europe-west1`. All supported language codes for AI-generated captions are supported as source and target language codes for AI-generated translations.

**Use either`us-west1` or `europe-west1` for all API requests on this page.**

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

  * One [`ElementaryStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream), a [`TextStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#textstream), is used for the captions.
        
        {
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1 // audio track number
              }
            ]
          }
        }
        

  * The `TextStream` [`codec`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.codec) field must be set to `webvtt`.

  * The `TextStream` [`mapping`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.mapping) field uses [`inputTrack`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextMapping.FIELDS.input_track) to designate the input audio track to generate captions from. The mapping must **not** include a [`inputCeaChannel`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextMapping.FIELDS.input_cea_channel) field, which is only used for user-supplied closed captions.

  * Set the [`languageCode`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.language_code) to the language spoken in the audio track.

  * The elementary stream is used to create a [`MuxStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream) with key `vtt_english_ai`.
        
        {
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }
        

This mux stream is then referenced in both HLS and DASH [manifests](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest).
        
        {
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai"
          ],
          "maxSegmentCount": 5
        }
        




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
        },**{
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },**{
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",**"vtt_english_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",**"vtt_english_ai"**
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
        },**{
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },**{
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",**"vtt_english_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",**"vtt_english_ai"**
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
        },**{
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },**{
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",**"vtt_english_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",**"vtt_english_ai"**
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

#### Response
    
    
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
    

### Get the channel

You can check for the result of the operation using the new operation ID.

After the channel has been created, use the [`projects.locations.channels.get`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/get) method to query the channel state.

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

#### Response
    
    
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
        },
        {
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },
        {
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",
            "vtt_english_ai"
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai"
          ],
          "maxSegmentCount": 5
        }
      ],
      "streamingState": "STOPPED"
    }
    

The full response contains the following field:
    
    
    {
      ...
      "streamingState": "STOPPED"
      ...
    }
    

This response indicates that you can now start the channel.

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

#### Response
    
    
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

Now that the channel is ready, send an input stream to the input endpoint to generate the live stream. You can download an MP4 (or other TEST_VOD_FILE) with captions and use `ffmpeg` to send it to the input endpoint.

Open a new terminal window. Run the following command, using the INPUT_STREAM_URI from the Check for the result section:
    
    
    ffmpeg -re -stream_loop -1 -i "TEST_VOD_FILE" \
      -c:v copy -c:a aac -strict 2 -f "flv" "INPUT_STREAM_URI"
    

**Note:** Use format `flv` if the input endpoint uses the RTMP protocol. Use `mpegts` for the SRT protocol.

## Verify the captions in the output manifest

Run the following command to see the contents of the generated HLS manifest:
    
    
    gcloud storage cat gs://BUCKET_NAME/main.m3u8
    

The AI-generated webvtt English captions show up in the output manifest similar to the following:
    
    
    #EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="sub",LANGUAGE="en-US",NAME="English (AI captioned)",AUTOSELECT=YES,DEFAULT=YES,FORCED=NO,URI="vtt_english_ai/index-1.m3u8"
    

## Stop the channel

You must stop a channel before you update the channel configuration.

Use the [`projects.locations.channels.stop`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/stop) method to stop the channel.

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

#### Response
    
    
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
    

## Update the channel configuration for a translation

Update the channel configuration to include translated captions (that is, a translation).

Note the following _additions_ to the channel configuration:

  * One [`ElementaryStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream), a [`TextStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#textstream), is used for the captions for a single translated language.
        
        {
          "key": "webvtt_spanish_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "Spanish (AI captioned)",
            "languageCode": "es-MX",
            "mapping": [
              {
                "inputTrack": 1, // audio track number
                "fromLanguageCode": "en-US" // original audio in English
              }
            ]
          }
        }
        

  * Set [`languageCode`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.language_code) to the chosen translated language.

  * Set [`fromLanguageCode`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextMapping.FIELDS.from_language_code) to the original source language in the audio track.

  * The elementary stream is used to create a [`MuxStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream) with key `vtt_spanish_ai`.
        
        {
          "key": "vtt_spanish_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_spanish_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }
        

This mux stream is then referenced in both HLS and DASH [manifests](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest).
        
        {
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai",
            "vtt_spanish_ai"
          ],
          "maxSegmentCount": 5
        }
        




To update the channel, use the [`projects.locations.channels.patch`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels/patch) method.

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
        },
        {
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        },**{
          "key": "webvtt_spanish_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "Spanish (AI captioned)",
            "languageCode": "es-MX",
            "mapping": [
              {
                "inputTrack": 1,
                "fromLanguageCode": "en-US"
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },
        {
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },**{
          "key": "vtt_spanish_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_spanish_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",
            "vtt_english_ai",**"vtt_spanish_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai",**"vtt_spanish_ai"**
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
        },
        {
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        },**{
          "key": "webvtt_spanish_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "Spanish (AI captioned)",
            "languageCode": "es-MX",
            "mapping": [
              {
                "inputTrack": 1,
                "fromLanguageCode": "en-US"
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },
        {
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },**{
          "key": "vtt_spanish_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_spanish_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",
            "vtt_english_ai",**"vtt_spanish_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai",**"vtt_spanish_ai"**
          ],
          "maxSegmentCount": 5
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID?updateMask=elementary_streams,mux_streams,manifests"

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
        },
        {
          "key": "webvtt_english_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "mapping": [
              {
                "inputTrack": 1
              }
            ]
          }
        },**{
          "key": "webvtt_spanish_ai",
          "textStream": {
            "codec": "webvtt",
            "displayName": "Spanish (AI captioned)",
            "languageCode": "es-MX",
            "mapping": [
              {
                "inputTrack": 1,
                "fromLanguageCode": "en-US"
              }
            ]
          }
        }**
      ],
      "muxStreams": [
        {
          "key": "mux_video_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_video"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_fmp4",
          "container": "fmp4",
          "elementaryStreams": [
            "es_audio"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
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
        },
        {
          "key": "vtt_english_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_english_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },**{
          "key": "vtt_spanish_ai",
          "container": "vtt",
          "elementaryStreams": [
            "webvtt_spanish_ai"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        }**
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "fileName": "main.mpd",
          "type": "DASH",
          "muxStreams": [
            "mux_video_fmp4",
            "mux_audio_fmp4",
            "vtt_english_ai",**"vtt_spanish_ai"**
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_ts",
            "vtt_english_ai",**"vtt_spanish_ai"**
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
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID?updateMask=elementary_streams,mux_streams,manifests" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/channels/CHANNEL_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID.

## Restart the channel and resend the input stream

As done previously, start the channel and send the input stream again.

## Verify the translation in the output manifest

Run the following command to see the contents of the generated HLS manifest:
    
    
    gcloud storage cat gs://BUCKET_NAME/main.m3u8
    

The AI-generated webvtt English and Spanish captions show up in the output manifest similar to the following:
    
    
    #EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="sub",LANGUAGE="en-US",NAME="English (AI captioned)",AUTOSELECT=YES,DEFAULT=YES,FORCED=NO,URI="vtt_english_ai/index-1.m3u8"
    #EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="sub",LANGUAGE="es-MX",NAME="Spanish (AI captioned)",AUTOSELECT=NO,DEFAULT=NO,FORCED=NO,URI="vtt_spanish_ai/index-1.m3u8"
    

## Configure AI-generated transcripts for distribution

Before configuring AI-generated captions and translations for distribution, familiarize yourself with how to [distribute live streams to remote endpoints](https://docs.cloud.google.com/livestream/docs/how-to/distribute-live-streams).

To distribute AI-generated captions and translations to remote endpoints, don't reference the text streams in the `webvtt` format that were configured previously when creating channel with AI-generated captions and updating channel for translation. Text streams for distribution must be embedded captions, with the [`codec`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.codec) set to `cea608` or `cea708`.

In the channel configuration, consider the following:

  * One [`ElementaryStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream), a [`TextStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#textstream), is used for the captions, and another [`ElementaryStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream), a [`TextStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#textstream), is used for the translation.
        
        {
          "key": "embedded_english_ai",
          "textStream": {
            "codec": "cea608",
            "displayName": "English (AI captioned)",
            "languageCode": "en-US",
            "outputCeaChannel": "CC1", // closed caption channel that will contain AI-generated English captions
            "mapping": [
              {
                "inputTrack": 1 // audio track number
              }
            ]
          }
        }
        
        {
          "key": "embedded_spanish_ai",
          "textStream": {
            "codec": "cea608",
            "displayName": "Spanish (AI captioned)",
            "languageCode": "es-MX",
            "outputCeaChannel": "CC2", // closed caption channel that will contain AI-generated Spanish captions
            "mapping": [
              {
                "inputTrack": 1, // audio track number
                "fromLanguageCode": "en-US" // original audio in English
              }
            ]
          }
        }
        

  * The `TextStream` [`codec`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.codec) field must be set to either `cea608` or `cea708`.

  * The `TextStream` [`mapping`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.mapping) field uses [`inputTrack`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextMapping.FIELDS.input_track) to designate the input audio track to generate captions from. The mapping must **not** include a [`inputCeaChannel`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextMapping.FIELDS.input_cea_channel) field, which is only used for user-supplied closed captions.

  * Set the [`outputCeaChannel`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.output_cea_channel) to the channel of closed caption to contain AI-generated transcripts in the distribution stream.

  * Set the [`languageCode`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#TextStream.FIELDS.language_code) to the language spoken in the audio track.

  * The elementary streams are included in the [`elementaryStreams`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream.FIELDS.elementary_streams) field of the [`DistributionStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#DistributionStream) object.
        
        {
          "distributionStreams": [
            {
              "key": "ds1",
              "container": "ts", // to be used with an SRT distribution
              "elementaryStreams": [
                "es_video",
                "es_audio",
                "embedded_english_ai", // distribute both English
                "embedded_spanish_ai"  // and Spanish captions
              ]
            },
            {
              "key": "ds2",
              "container": "flv", // to be used with an RTMP distribution
              "elementaryStreams": [
                "es_video",
                "es_audio",
                "embedded_spanish_ai" // only distribute Spanish captions
              ]
            }
          ]
        }
        




Complete channel creation by following [distribute live stream to remote endpoint guide](https://docs.cloud.google.com/livestream/docs/how-to/distribute-live-streams#create-channel).

## Advanced configurations

Set [`AutoTranscriptionConfig`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#AutoTranscriptionConfig) at the channel level to further tune the AI-generated text streams to your needs.

### Caption display timing

By default, AI-generated captions are displayed asynchronously with the audio and video. Set the [`DisplayTiming`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#AutoTranscriptionConfig.FIELDS.display_timing) field in `AutoTranscriptionConfig` to `SYNC` to display them synchronously.
    
    
    {
      "autoTranscriptionConfig": {
        "displayTiming": "SYNC"
      }
    }
    

Displaying captions synchronously decreases the viewing latency between audio and text but increases the overall end-to-end media latency.

### Quality presets

Use the [`QualityPreset`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#AutoTranscriptionConfig.FIELDS.quality_preset) field in `AutoTranscriptionConfig` to configure the quality preferences for AI-generated text streams.

For example, you can further reduce the latency of text stream generation by setting:
    
    
    {
      "autoTranscriptionConfig" : {
        "qualityPreset": "LOW_LATENCY"
      }
    }
    

## Clean up

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

#### Response
    
    
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

#### Response
    
    
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

#### Response
    
    
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
