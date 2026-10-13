---
url: https://docs.cloud.google.com/transcoder/docs/concepts/config-examples/
title: Configuration examples \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:24.585784+00:00
---

# Configuration examples  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/concepts/config-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Configuration examples Stay organized with collections  Save and categorize content based on your preferences. 

This page shows some configuration examples for the encoding of an input media file (that is, an [`ElementaryStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#elementarystream)).

## Video stream

[`VideoStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#VideoStream) properties do not have dependencies on each other. You can set properties such as resolution (height and width), bit rate, and frame rate independently.
    
    
    {
      "videoStream": {
        "h264": {
          "profile": "high",
          "preset": "veryfast",
          "heightPixels": 360,
          "widthPixels": 640,
          "pixelFormat": "yuv420p",
          "bitrateBps": 550000,
          "rateControlMode": "vbr",
          "crfLevel": 21,
          "vbvSizeBits": 550000,
          "vbvFullnessBits": 495000,
          "gopDuration": "3s",
          "entropyCoder": "cabac",
          "bFrameCount": 3,
          "frameRate": 30,
          "aqStrength": 1
        }
      },
      "key": "video-stream0"
    }
    

## Audio stream

Certain [`AudioStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#audiostream) properties are dependent on each other. The `channelCount` property value must equal the number of layouts in the `channelLayout` array. This value must also equal the number of channels in a mapped input stream.

### Basic audio stream

The following is an example of a non-mapped, non-mixed audio stream.
    
    
    {
      "audioStream": {
        "codec": "aac",
        "bitrateBps": 64000,
        "channelCount": 2,
        "channelLayout": [
          "fl",
          "fr"
        ],
        "sampleRateHertz": 48000,
        "languageCode": "en-US",
        "displayName": "English"
      },
      "key": "audio-stream0"
    }
    

### Audio stream with mapping

The following is an example of a input-mapped audio stream. The output stereo `AudioStream` is composed of the following inputs:

  * Track 1 
    * Channel 0
  * Track 1 
    * Channel 1



Note that the `channelCount` property value must equal the number of objects defined under `mapping`, each with its own `outputChannel`.
    
    
    {
      "key":  "audio-stream0",
      "audioStream": {
        "codec": "aac",
        "bitrateBps": 64000,
        "channelCount": 2,
        "channelLayout": [
          "fl",
          "fr"
        ],
        "sampleRateHertz": 48000,
        "languageCode": "en-US",
        "displayName": "English",
        "mapping": [
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 1,
            "inputChannel": 0,
            "outputChannel": 0,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 1,
            "inputChannel": 1,
            "outputChannel": 1,
            "gainDb": 0
          }
        ]
      }
    }
    

### Audio stream with mixing

The following is an example of a mixed audio stream. The output stereo `AudioStream` is composed of the following inputs:

  * Track 2 
    * Channel 0
    * Channel 2
    * Channel 4
  * Track 2 
    * Channel 1
    * Channel 3
    * Channel 5


    
    
    {
      "key":  "audio-stream0",
      "audioStream":  {
        "codec":  "aac",
        "bitrateBps":  128000,
        "channelCount":  2,
        "mapping":  [
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 0,
            "outputChannel": 0,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 2,
            "outputChannel": 0,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 4,
            "outputChannel": 0,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 1,
            "outputChannel": 1,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 3,
            "outputChannel": 1,
            "gainDb": 0
          },
          {
            "atomKey": "atom0",
            "inputKey": "video_and_stereo_audio",
            "inputTrack": 2,
            "inputChannel": 5,
            "outputChannel": 1,
            "gainDb": 0
          }
        ],
        "sampleRateHertz":  44100
      }
    }
    

### Multi-language audio streams from a single file

The following is an example config for a single input video file containing video and multiple audio tracks that are in different languages. The [`mapping[]`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#AudioStream.FIELDS.mapping) object is used to create multiple output audio streams, one per language. The video and each audio stream are included in both the HLS and DASH manifests.
    
    
    {
      "outputUri": "gs://STORAGE_BUCKET_NAME/",
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
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "widthPixels": 640,
                "heightPixels": 360,
                "frameRate": 30,
                "bitrateBps": 500000
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 1,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 1,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "en-US",
              "displayName": "English"
            }
          },
          {
            "key": "audio-stream1",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 2,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 2,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "es-ES",
              "displayName": "Spanish"
            }
          },
          {
            "key": "audio-stream2",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 3,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 3,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "fr-Fr",
              "displayName": "French"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-0",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "audio-1",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream1"
            ]
          },
          {
            "key": "audio-2",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream2"
            ]
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "sd",
              "audio-0",
              "audio-1",
              "audio-2"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "sd",
              "audio-0",
              "audio-1",
              "audio-2"
            ]
          }
        ]
      }
    }
    

### Multi-language audio streams from multiple audio files

The following is an example config for an input video file containing video and only one default language audio track. Two separate input audio files are also used, one per language. The [`mapping[]`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#AudioStream.FIELDS.mapping) object is used to create multiple output audio streams, one per language. The video and each audio stream are included in both the HLS and DASH manifests.
    
    
    {
      "outputUri": "gs://STORAGE_BUCKET_NAME/",
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          },
          {
            "key": "input1",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_AUDIO1"
          },
          {
            "key": "input2",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_AUDIO2"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "input1",
              "input2"
            ],
            "startTimeOffset": "0s"
          }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "widthPixels": 640,
                "heightPixels": 360,
                "frameRate": 30,
                "bitrateBps": 500000
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 1,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 1,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "en-US",
              "displayName": "English"
            }
          },
          {
            "key": "audio-stream1",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input1",
                  "inputTrack": 0,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input1",
                  "inputTrack": 0,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "es-ES",
              "displayName": "Spanish"
            }
          },
          {
            "key": "audio-stream2",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input2",
                  "inputTrack": 0,
                  "inputChannel": 0,
                  "outputChannel": 0
                },
                {
                  "atomKey": "atom0",
                  "inputKey": "input2",
                  "inputTrack": 0,
                  "inputChannel": 1,
                  "outputChannel": 1
                }
              ],
              "sampleRateHertz": 48000,
              "languageCode": "fr-Fr",
              "displayName": "French"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-0",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "audio-1",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream1"
            ]
          },
          {
            "key": "audio-2",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream2"
            ]
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "sd",
              "audio-0",
              "audio-1",
              "audio-2"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "sd",
              "audio-0",
              "audio-1",
              "audio-2"
            ]
          }
        ]
      }
    }
    

## Text stream

[`TextStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#textstream) properties do not have dependencies on each other. You can set properties independently.

Text streams may use an [edit list](https://docs.cloud.google.com/transcoder/docs/concepts/overview#edit_list) to modify the output file. The following sections highlight the use of the edit list to provide captions.

The following example shows a text stream with one atom in edit list.
    
    
    {
      "editList":[
         {
            "key":"atom0",
            "inputs":[
               "video_input0",
               "caption_input0"
            ],
            "startTimeOffset":"0s",
            "endTimeOffset":"300s"
         }
      ],
      "elementaryStreams":[
        {
          "key": "cea-stream0",
          "textStream": {
            "codec": "cea708",
            "languageCode": "en-US",
            "displayName": "English",
            "mapping": [
              {
                "atomKey": "atom0",
                "inputKey": "caption_input0",
                "inputTrack": 0
              }
            ]
          }
        }
      ]
    }
    

The following example shows a text stream with two atoms in edit list.
    
    
    {
      "editList":[
         {
            "key":"atom0",
            "inputs":[
               "video_input0",
               "caption_input0"
            ],
            "startTimeOffset":"0s",
            "endTimeOffset":"300s"
         },
         {
            "key":"atom1",
            "inputs":[
               "video_input1",
               "caption_input1"
            ],
            "startTimeOffset":"0s",
            "endTimeOffset":"300s"
         }
      ],
      "elementaryStreams":[
        {
          "key": "cea-stream0",
          "textStream": {
            "codec": "cea708",
            "languageCode": "en-US",
            "displayName": "English",
            "mapping": [
              {
              "atomKey": "atom0",
              "inputKey": "caption_input0",
              "inputTrack": 0
              },
              {
              "atomKey": "atom1",
              "inputKey": "caption_input1",
              "inputTrack": 0
              }
            ]
          }
        }
      ]
    }
    

## Advanced

The following sections outline various advanced configurations.

### Audio-only output

The following configuration outputs audio-only MP4 and TS files.
    
    
    {
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "elementaryStreams": [
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "languageCode": "en-US",
              "displayName": "English"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "audio-only-ts",
            "fileName": "audio-only.ts",
            "container": "ts",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "audio-only-mp4",
            "fileName": "audio-only.mp4",
            "container": "mp4",
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
            "audio-only-ts"
          ]
        }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
      }
    }
    

### MuxStream and fmp4

A [`MuxStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#muxstream) that uses the fmp4 container can only contain a single `ElementaryStream`. For this container, use two `MuxStreams`: one for audio and one for video:
    
    
    "muxStreams":[
      {
        "key": "hd3-video",
        "container": "fmp4",
        "elementaryStreams":["video-stream1"]
      },
      {
        "key": "hd3-audio",
        "container": "fmp4",
        "elementaryStreams":["audio-stream1"]
      }
    ],
    

### Reusing streams in multiple manifests

The following example configuration shows two video and one audio encodings being used in both HLS and DASH manifests:
    
    
    {
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "elementaryStreams": [
          {
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 500000,
                "frameRate": 30
              }
            },
            "key": "video-stream0"
          },
          {
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 3200000,
                "frameRate": 30
              }
            },
            "key": "video-stream1"
          },
          {
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "sampleRateHertz": 48000
            },
            "key": "audio-stream0"
          }
        ],
        "muxStreams": [
          {
            "key": "video-only-sd",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "video-only-hd",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream1"
            ]
          },
          {
            "key": "audio-only",
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
              "video-only-sd",
              "video-only-hd",
              "audio-only"
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
      }
    }
    

### Recommended settings for transcoding multiple profiles

For the output resolution and bitrate, depending on the input resolution/frame rate (50/60 FPS), add the higher frame rate step for 50/60 FPS if it applies. Note that adding additional steps requires more computing power. The following is the recommended ladder:

Resolution (ScanMode)/Frame rate  | H.264 High Profile Bitrate (Kbps)   
---|---  
170x96 p12/15  | 130   
256x144 p25/30  | 240   
416x234 p25/30  | 300   
640x360 p25/30  | 400   
768x432 p25/30  | 750   
768x432 p25/30  | 1100   
960x540 p25/30  | 2200   
1280x720 p25/30  | 3300   
1280x720 p50/60  | 5500   
1920x1080 p25/30  | 6000   
1920x1080 p50/60  | 9000   
  
For audio, the recommendations are based on the number of channels:

Channels  | AAC Bitrate (Kbps)   
---|---  
2.0  | 64   
2.0  | 160   
5.1  | 384   
  
Use this output ladder to create a configuration that outputs HLS and MPEG-DASH manifests with different combinations:
    
    
    {
      "config": {
        "inputs": [
            {
              "key": "input0",
              "uri": "gs://my-bucket/input0.mp4"
            }
          ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 96,
                "widthPixels": 170,
                "bitrateBps": 130000,
                "frameRate": 15,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream1",
            "videoStream": {
              "h264": {
                "heightPixels": 144,
                "widthPixels": 256,
                "bitrateBps": 240000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream2",
            "videoStream": {
              "h264": {
                "heightPixels": 234,
                "widthPixels": 416,
                "bitrateBps": 300000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream3",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 400000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream4",
            "videoStream": {
              "h264": {
                "heightPixels": 432,
                "widthPixels": 768,
                "bitrateBps": 1100000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream5",
            "videoStream": {
              "h264": {
                "heightPixels": 540,
                "widthPixels": 960,
                "bitrateBps": 2200000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream6",
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 3300000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream7",
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 5500000,
                "frameRate": 60,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 6,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream8",
            "videoStream": {
              "h264": {
                "heightPixels": 1080,
                "widthPixels": 1920,
                "bitrateBps": 6000000,
                "frameRate": 30,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 3,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "video-stream9",
            "videoStream": {
              "h264": {
                "heightPixels": 1080,
                "widthPixels": 1920,
                "bitrateBps": 9000000,
                "frameRate": 60,
                "gopDuration": "4.0s",
                "pixelFormat": "yuv420p",
                "rateControlMode": "crf",
                "crfLevel": 10,
                "bFrameCount": 6,
                "profile": "high",
                "enableTwoPass": true,
                "preset": "medium"
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 32000
            }
          },
          {
            "key": "audio-stream1",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          },
          {
            "key": "audio-stream2",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 96000
            }
          },
          {
            "key": "audio-stream3",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 128000
            }
          },
          {
            "key": "audio-stream4",
            "audioStream": {
              "codec": "aac-he",
              "bitrateBps": 160000
            }
          },
          {
            "key": "audio-stream5",
            "audioStream": {
              "codec": "aac-he-v2",
              "bitrateBps": 384000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "1",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "2",
            "container": "ts",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "3",
            "container": "ts",
            "elementaryStreams": [
              "video-stream2",
              "audio-stream1"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "4",
            "container": "ts",
            "elementaryStreams": [
              "video-stream3",
              "audio-stream1"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "5",
            "container": "ts",
            "elementaryStreams": [
              "video-stream4",
              "audio-stream2"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "6",
            "container": "ts",
            "elementaryStreams": [
              "video-stream5",
              "audio-stream3"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "7",
            "container": "ts",
            "elementaryStreams": [
              "video-stream6",
              "audio-stream3"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "8",
            "container": "ts",
            "elementaryStreams": [
              "video-stream7",
              "audio-stream4"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "9",
            "container": "ts",
            "elementaryStreams": [
              "video-stream8",
              "audio-stream4"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "10",
            "container": "ts",
            "elementaryStreams": [
              "video-stream9",
              "audio-stream5"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-1",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-2",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream1"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-3",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream2"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-4",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream3"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-5",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream4"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-6",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream5"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-7",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream6"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-8",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream7"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-9",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream8"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "video-10",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream9"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-1",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-2",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream1"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-3",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream2"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-4",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream3"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-5",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream4"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          },
          {
            "key": "audio-6",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream5"
            ],
            "segmentSettings": {
                "segmentDuration": "4.0s",
                "individualSegments": true
            }
          }
        ],
        "manifests": [
            {
              "fileName": "manifest.m3u8",
              "type": "HLS",
              "muxStreams": [
                "10",
                "9",
                "8",
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "1"
              ]
            },
            {
              "fileName": "manifest.mpd",
              "type": "DASH",
              "muxStreams": [
                "video-10",
                "video-9",
                "video-8",
                "video-7",
                "video-6",
                "video-5",
                "video-4",
                "video-3",
                "video-2",
                "video-1",
                "audio-6",
                "audio-5",
                "audio-4",
                "audio-3",
                "audio-2",
                "audio-1"
              ]
            }
          ],
          "output": {
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
          }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
