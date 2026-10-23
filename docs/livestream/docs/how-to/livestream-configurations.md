---
url: https://docs.cloud.google.com/livestream/docs/how-to/livestream-configurations/
title: Configure live stream settings \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:27.650605+00:00
---

# Configure live stream settings  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/livestream-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Configure live stream settings Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure settings during input endpoint or channel creation for live stream features such as multiple audio tracks, captions, and spritesheets.

## Configure through input endpoint creation

You can specify configurations for the following features during [input endpoint creation](https://docs.cloud.google.com/livestream/docs/how-to/create-input-endpoints):

### IP allowlisting

You can restrict access to input endpoints by specifying IP ranges the input stream should originate from, such as the IP address of the encoder. The video pipeline only accepts traffic from IP addresses in these ranges. The IP ranges must be in CIDR block format.

Configure the [`securityRules`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule) field in the `Input` resource:
    
    
    {
      "type": "RTMP_PUSH",
      "securityRules": {
        "ipRanges": ["1.2.3.4/32"]
      }
    }
    

## Configure through channel creation

You can specify configurations for the following features during [channel creation](https://docs.cloud.google.com/livestream/docs/how-to/create-channels):

### Multiple bitrate streams

You can create advanced channel configurations that support multiple bitrates, resolutions, and frame rates. The following configuration includes two `muxStream`s in the output, one at 360p with a frame rate of 30 FPS (`mux_video_360p30`) and another at 720p with a frame rate of 60 FPS (`mux_video_720p60`). This configuration also supports multiple audio bitrates. See [Recommended bitrates](https://docs.cloud.google.com/livestream/docs/best-practices#recommended-bitrates) for more information.
    
    
    {
      "inputAttachments":[
        {
          "key":"input-primary",
          "input": "projects/PROJECT_NUMBER/locations/LOCATION/inputs/INPUT_ID"
        }
      ],
      "output":{
        "uri": "gs://BUCKET_NAME"
      },
      "elementaryStreams": [
        {
          "key": "es_video_720p60",
          "videoStream": {
            "h264": {
              "profile": "high",
              "heightPixels": 720,
              "widthPixels": 1280,
              "bitrateBps": 5500000,
              "frameRate": 60
            }
          }
        },
        {
          "key": "es_video_360p30",
          "videoStream": {
            "h264": {
              "profile": "high",
              "heightPixels": 360,
              "widthPixels": 640,
              "bitrateBps": 400000,
              "frameRate": 30
            }
          }
        },
        {
          "key": "es_audio_160k",
          "audioStream": {
            "codec": "aac",
            "channelCount": 2,
            "bitrateBps": 160000
          }
        },
        {
          "key": "es_audio_64k",
          "audioStream": {
            "codec": "aac",
            "channelCount": 2,
            "bitrateBps": 64000
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video_720p60",
          "elementaryStreams": [
            "es_video_720p60"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_video_360p30",
          "elementaryStreams": [
            "es_video_360p30"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_160k",
          "elementaryStreams": [
            "es_audio_160k"
          ],
          "segmentSettings": {
            "segmentDuration": "2s"
          }
        },
        {
          "key": "mux_audio_64k",
          "elementaryStreams": [
            "es_audio_64k"
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
            "mux_video_720p60",
            "mux_video_360p30",
            "mux_audio_160k",
            "mux_audio_64k"
          ],
          "maxSegmentCount": 5
        },
        {
          "key": "manifest_hls",
          "fileName": "main.m3u8",
          "type": "HLS",
          "muxStreams": [
            "mux_video_720p60",
            "mux_video_360p30",
            "mux_audio_160k",
            "mux_audio_64k"
          ],
          "maxSegmentCount": 5
        }
      ]
    }
    

### Multiple audio tracks

If the input stream contains more than one audio track, use the [`AudioMapping`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#AudioMapping) object to select the track for each [`AudioStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#audiostream).
    
    
    {
      "inputAttachments": [
        {
          "key": "MY-INPUT",
          "input": "/projects/PROJECT-ID/locations/LOCATION/inputs/MY-INPUT",
        }
      ],
      "output": {
        "uri": "gs://BUCKET_NAME/outputs/"
      },
      "elementaryStreams": [
        {
          "key": "es_video",
          "videoStream": {
            "h264": {
              "heightPixels": 720,
              "widthPixels": 1280,
              "bitrateBps": 3000000,
              "frameRate": 30
            }
          }
        },
        {
          "key": "es_first_audio",
          "audioStream": {
            "codec": "aac",
            "bitrateBps": 160000,
            "mapping": [
              {
                "inputKey": "MY-INPUT",
                "inputTrack": 1
              }
            ]
          }
        },
        {
          "key": "es_second_audio",
          "audioStream": {
            "codec": "aac",
            "bitrateBps": 160000,
            "mapping": [
              {
                "inputKey": "MY-INPUT",
                "inputTrack": 2
              }
            ]
          }
        }
      ],
      "muxStreams": [
        {
          "key": "mux_video",
          "elementaryStreams": ["es_video"],
        },
        {
          "key": "mux_first_audio",
          "elementaryStreams": ["es_first_audio"],
        },
        {
          "key": "mux_second_audio",
          "elementaryStreams": ["es_second_audio"],
        }
      ],
      "manifests": [
        {
          "key": "manifest_dash",
          "type": "DASH",
          "muxStreams": [
            "mux_video",
            "mux_first_audio",
            "mux_second_audio",
          ]
        }
      ]
    }
    

Note that [Shaka Player](https://shaka-player-demo.appspot.com/demo/) doesn't support the following features for HLS streams with multiple audio tracks:

  * Alternate audio track playback with TS segments.

  * Secondary and alternate audio track selection with fMP4 segments.




### Passthrough CEA 608/708 captions

If the input streams contain CEA 608/708 captions, you can forward the captions to the output streams. Add the following [`textStream`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#textstream) to the [`elementaryStreams`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream) when creating a `Channel`. This `textStream` embeds the CEA 608/708 captions in all output video streams and renditions.
    
    
    {
      "key": "captions",
      "textStream": {
        "codec": "cea608"
      }
    }
    

### Sprite sheets

To generate a sprite sheet, configure the [`spriteSheets`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet) field in the `Channel` resource.
    
    
    {
      "spriteSheets": [
        {
          "format": "jpeg",
          "filePrefix": "sprite",
          "interval": "2s",
          "spriteWidthPixels": 320,
          "spriteHeightPixels": 240,
          "columnCount": 3,
          "rowCount": 3,
          "quality": 80
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
