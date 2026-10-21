---
url: https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files/
title: Create VOD source files \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:45.836124+00:00
---

# Create VOD source files  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Create VOD source files Stay organized with collections  Save and categorize content based on your preferences. 

If you don't already have your own video on demand (VOD) asset, you can use the [Transcoder API](https://docs.cloud.google.com/transcoder) to create a VOD manifest and segment files that can be used with the Video Stitcher API. This is completely optional.

The VOD manifest is used as the source URI in a [VOD config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs). Both DASH and HLS formats are supported.

The following is an example job config you can use with the Transcoder API to create the VOD files. For more information, see [Creating jobs with ad-hoc configurations](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc). You will need to enable the Transcoder API in your Google Cloud project; see [Before you begin](https://docs.cloud.google.com/transcoder/docs/how-to/before-you-begin) for more information.
    
    
    {
      "config":{
        "inputs":[
          {
            "key":"input0",
            "uri":"gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "output":{
          "uri":"gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "editList":[
          {
            "key":"atom0",
            "inputs":[
              "input0"
            ]
          }
        ],
        "elementaryStreams":[
          {
            "key":"video_hd",
            "videoStream":{
              "h264":{
                "heightPixels":720,
                "widthPixels":1280,
                "pixelFormat":"yuv420p",
                "bitrateBps":5000000,
                "frameRate":25
              }
            }
          },
          {
            "key":"video_sd",
            "videoStream":{
              "h264":{
                "heightPixels":432,
                "widthPixels":768,
                "pixelFormat":"yuv420p",
                "bitrateBps":1100000,
                "frameRate":25
              }
            }
          },
          {
            "key":"video_sd_low",
            "videoStream":{
              "h264":{
                "heightPixels":360,
                "widthPixels":640,
                "pixelFormat":"yuv420p",
                "bitrateBps":365000,
                "frameRate":25
              }
            }
          },
          {
            "key":"audio_stereo",
            "audioStream":{
              "codec":"aac",
              "bitrateBps":64000,
              "channelCount":2,
              "channelLayout":[
                "fl",
                "fr"
              ],
              "sampleRateHertz":48000
            }
          }
        ],
        "muxStreams":[
          {
            "key":"hd",
            "container":"mp4",
            "elementaryStreams":[
              "video_hd",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"sd",
            "container":"mp4",
            "elementaryStreams":[
              "video_sd",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"sd_low",
            "container":"mp4",
            "elementaryStreams":[
              "video_sd_low",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"media_hd",
            "container":"ts",
            "elementaryStreams":[
              "video_hd",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"media_sd",
            "container":"ts",
            "elementaryStreams":[
              "video_sd",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"media_sd_low",
            "container":"ts",
            "elementaryStreams":[
              "video_sd_low",
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"video_only_hd",
            "container":"fmp4",
            "elementaryStreams":[
              "video_hd"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"video_only_sd",
            "container":"fmp4",
            "elementaryStreams":[
              "video_sd"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"video_only_sd_low",
            "container":"fmp4",
            "elementaryStreams":[
              "video_sd_low"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          },
          {
            "key":"audio_only",
            "container":"fmp4",
            "elementaryStreams":[
              "audio_stereo"
            ],
            "segmentSettings":{
              "segmentDuration":"6s",
              "individualSegments":true
            }
          }
        ],
        "manifests":[
          {
            "type":"HLS",
            "fileName":"manifest.m3u8",
            "muxStreams":[
              "media_hd",
              "media_sd",
              "media_sd_low"
            ]
          },
          {
            "type":"DASH",
            "fileName":"manifest.mpd",
            "muxStreams":[
              "video_only_hd",
              "video_only_sd",
              "video_only_sd_low",
              "audio_only"
            ]
          }
        ]
      }
    }
    

**Note:** Make sure that `individualSegments` is set to `true` in the job config.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
