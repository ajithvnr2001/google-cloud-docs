---
url: https://docs.cloud.google.com/transcoder/docs/concepts/stream-mappings/
title: Stream mappings \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:25.659150+00:00
---

# Stream mappings  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/concepts/stream-mappings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Stream mappings Stay organized with collections  Save and categorize content based on your preferences. 

The Transcoder API allows you to concatenate videos, mix audio tracks, and more. The [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) JSON specification is highly flexible, and this can create ambiguity between inputs and outputs. You can define certain stream mappings to clear up this ambiguity. If you do not, the API provides reasonable default stream mappings for you.

This page shows the default stream mappings provided by the API and some advanced configuration examples for the encoding of input media files.

## Background

The `inputs` list in a `JobConfig` specifies which files to download, not how to use them. Each input is paired with a key to identify it.

The `editList` defines a sequence of edits as a timeline for the output file (or manifest) from a transcoding job. The `inputs` in the `editList` determine which inputs to use in each atom.

For more information, read the [Concepts](https://docs.cloud.google.com/transcoder/docs/concepts/overview#concepts) section in the Overview.

## Default video mapping

Each atom in the `editList` must reference at least one input that contains a video track. If multiple inputs are defined for an atom and each contains a video track, the first input in the `inputs` list is used as the video source; this is the default mapping. If none of the inputs contains a video track, the job fails.

The following configuration concatenates the first 5 seconds of video track `input0.mp4` with 10 seconds of video track `input1.mov` into the output file:
    
    
    "inputs": [
      {
        "key": "input0",
        "uri": "gs://my-bucket/input0.mp4"
      },
      {
        "key": "input1",
        "uri": "gs://my-bucket/input1.mov"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["input0"],
        "endTimeOffset": "5s",
        "startTimeOffset": "0s"
      },
      {
        "key": "atom1",
        "inputs": ["input1"],
        "endTimeOffset": "20s",
        "startTimeOffset": "10s"
      }
    ]
    

See [Concatenating multiple input videos](https://docs.cloud.google.com/transcoder/docs/how-to/concatenate-videos) for more information.

## Default audio mappings

Audio mappings apply to a variety of situations, most notably when there is a mismatched number of audio inputs to outputs.

### Concatenate multiple inputs

Each atom in the `editList` must reference at least one input that contains an audio track if an `audioStream` is defined. If multiple inputs are defined for an atom and each contains an audio track, the first input in the `inputs` list is used as the audio source; this is the default mapping. If none of the inputs contains an audio track, the job fails.

The Transcoder API only generates a default mapping for each defined [`audioStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#audiostream) if the mapping is not specified explicitly by the client.

Consider the following configuration that contains a defined `audioStream`:
    
    
    "inputs": [
      {
        "key": "video_and_stereo_audio",
        "uri": "gs://my-bucket/video_and_stereo_audio.mp4"
      },
      {
        "key": "video_only",
        "uri": "gs://my-bucket/video_only.mov"
      },
      {
        "key": "stereo_audio_only",
        "uri": "gs://my-bucket/stereo_audio_only.mp3"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["video_and_stereo_audio"]
      },
      {
        "key": "atom1",
        "inputs": ["video_only", "stereo_audio_only"]
      }
    ],
    "elementaryStreams": [
      {
        "key": "output_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2, // API default
          "channelLayout": ["fl", "fr"], // API default
          "sampleRateHertz": 48000
        }
      }
    ]
    

The Transcoder API generates the following default mappings for audio output. Note that the `audioStream` fields are not applied to the `video_only` input. Although this input appears first in the `inputs` list, it does not contain an audio track.
    
    
    "elementaryStreams": [
      {
        "key": "output_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2,
          "channelLayout": ["fl", "fr"],
          "sampleRateHertz": 48000,
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
            },
            {
              "atomKey": "atom1",
              "inputKey": "stereo_audio_only",
              "inputTrack": 0,
              "inputChannel": 0,
              "outputChannel": 0,
              "gainDb": 0
            },
            {
              "atomKey": "atom1",
              "inputKey": "stereo_audio_only",
              "inputTrack": 0,
              "inputChannel": 1,
              "outputChannel": 1,
              "gainDb": 0
            }
          ]
        }
      }
    ]
    

### _N_ to _n_ copy

If the number of channels in the input audio track matches the number of channels in the output `audioStream`, the Transcoder API copies the input channels into the output channels.

Consider the following configuration that contains an input with two-channel stereo audio and a defined `audioStream` with 2 channels:
    
    
    "inputs": [
      {
        "key": "video_and_stereo_audio",
        "uri": "gs://my-bucket/video_and_stereo_audio.mp4"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["video_and_stereo_audio"]
      }
    ],
    "elementaryStreams": [
      {
        "key": "output_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2, // API default
          "channelLayout": ["fl", "fr"], // API default
          "sampleRateHertz": 48000
        }
      }
    ]
    

The Transcoder API generates the following default mappings for audio output:
    
    
    "elementaryStreams": [
      {
        "key": "output_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2,
          "channelLayout": ["fl", "fr"],
          "sampleRateHertz": 48000,
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
    ]
    

### _N_ to 1 downmix

If the number of channels in the input audio track is greater than the number of channels in the output `audioStream`, the Transcoder API copies all input channels into a single output channel.

If the `audioStream` defines multiple output channels, the single output channel is copied and used for each output channel. For example, if the input audio track consists of 5 channels and the `audioStream` defines 2 output channels, those two output channels will contain the exact same audio, a downmix of the 5 input channels.

Consider the following configuration that contains an input with two-channel stereo audio and a defined `audioStream` with one output channel:
    
    
    "inputs": [
      {
        "key": "video_and_stereo_audio",
        "uri": "gs://my-bucket/video_and_stereo_audio.mp4"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["video_and_stereo_audio"]
      }
    ],
    "elementaryStreams": [
      {
        "key": "output_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 1,
          "channelLayout": ["fc"],
          "sampleRateHertz": 48000
        }
      }
    ]
    

The Transcoder API generates the following default mappings for audio output:
    
    
    "elementaryStreams": [
      {
        "key": "output_mono_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 1,
          "channelLayout": ["fc"],
          "sampleRateHertz": 48000,
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
              "outputChannel": 0,
              "gainDb": 0
            }
          ]
        }
      }
    ]
    

### _1_ to _N_ copy

If the number of channels in the input audio track is less than the number of channels in the output `audioStream`, the Transcoder API copies the first input channel into each output channel.

Consider the following configuration that contains an input with one-channel mono audio and a defined `audioStream` with 2 output channels:
    
    
    "inputs": [
      {
        "key": "video_and_mono_audio",
        "uri": "gs://my-bucket/video_and_mono_audio.mp4"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["video_and_mono_audio"]
      }
    ],
    "elementaryStreams": [
      {
        "key": "output_mono_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2, // API default
          "channelLayout": ["fl", "fr"], // API default
          "sampleRateHertz": 48000
        }
      }
    ]
    

The Transcoder API generates the following default mappings for audio output:
    
    
    "elementaryStreams": [
      {
        "key": "output_mono_audio",
        "audioStream": {
          "codec": "aac",
          "bitrateBps": 64000,
          "channelCount": 2,
          "channelLayout": ["fl", "fr"],
          "sampleRateHertz": 48000,
          "mapping": [
            {
              "atomKey": "atom0",
              "inputKey": "video_and_mono_audio",
              "inputTrack": 1,
              "inputChannel": 0,
              "outputChannel": 0,
              "gainDb": 0
            },
            {
              "atomKey": "atom0",
              "inputKey": "video_and_mono_audio",
              "inputTrack": 1,
              "inputChannel": 0,
              "outputChannel": 1,
              "gainDb": 0
            }
          ]
        }
      }
    ]
    

## Default text mapping

Text mappings are generally used for subtitles and closed-captioning (CC).

Each atom in the `editList` must reference at least one input that contains a text track if a [`textStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#textstream) is defined. If multiple inputs are defined for an atom and each contains a text track, the first input in the `inputs` list is used as the text source; this is the default mapping. If none of the inputs contains a text track, the job fails.
    
    
    "inputs": [
      {
        "key": "video_and_audio",
        "uri": "gs://my-bucket/video_and_audio.mp4"
      },
      {
        "key": "sub",
        "uri": "gs://my-bucket/sub.srt"
      }
    ],
    "editList": [
      {
        "key": "atom0",
        "inputs": ["video_and_audio", "sub"]
      }
    ],
    "elementaryStreams": [
      {
        "key": "output_sub",
        "textStream": {
          "codec": "webvtt"
        }
      }
    ]
    

The Transcoder API generates the following default mappings for text output:
    
    
    "elementaryStreams": [
      {
        "key": "output_sub",
        "textStream": {
          "codec": "webvtt",
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
