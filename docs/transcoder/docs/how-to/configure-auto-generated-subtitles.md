---
url: https://docs.cloud.google.com/transcoder/docs/how-to/configure-auto-generated-subtitles/
title: Configure automatically generated subtitles \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:37.531081+00:00
---

# Configure automatically generated subtitles  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/configure-auto-generated-subtitles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Configure automatically generated subtitles Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add automatically generated subtitles to your output using the Transcoder API. This feature lets you generate subtitles from audio tracks, even if the language is not known, and translate subtitles to various languages.

You configure this feature by providing additional metadata about your input assets using the `attributes` field within each item in the `inputs` array in your job configuration. This field helps the Transcoder API understand the languages present in your audio tracks and how to process them.

## Before you begin

This page assumes that you have completed the steps in [Before you begin](https://docs.cloud.google.com/transcoder/docs/how-to/before-you-begin).

## Limitations

This feature has the following limitations:

#### Supported locations

This feature is supported in `us-central1` and `europe-west4`.

#### Output format

The output for automatically generated subtitles must be in the WebVTT (`webvtt`) format.

#### Edit list stitching

This feature does not support using an `editList` to stitch together multiple video clips.

## Configuration Examples

The following examples demonstrate how to configure automatic subtitles for various use cases.

### User-Provided Mapping

This method provides direct control by specifying exactly which input track to use for generating subtitles.

#### Explicitly map input tracks to output subtitle streams

This example shows how to use the `mapping` field within each `textStream` to precisely control which input audio track is used to generate the English and French subtitles.
    
    
    {
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://input-bucket/input.mp4",
            "attributes": {
              "trackDefinitions": [
                {
                  "inputTrack": 1,
                  "languages": [
                    "en-US"
                  ]
                },
                {
                  "inputTrack": 2,
                  "languages": [
                    "fr-FR"
                  ]
                }
              ]
            }
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0"
            ]
          }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "frameRate": 30,
                "widthPixels": 1280,
                "heightPixels": 720,
                "bitrateBps": 3200000,
                "frameRateConversionStrategy": "DOWNSAMPLE"
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "sampleRateHertz": 48000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ]
            }
          },
          {
            "key": "vtt-stream-english",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "en-US",
              "displayName": "English",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 1
                }
              ]
            }
          },
          {
            "key": "vtt-stream-french",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "fr-FR",
              "displayName": "French",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "input0",
                  "inputTrack": 2
                }
              ]
            }
          }
        ],
        "muxStreams": [
          {
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ],
            "fileName": "video-only.m4s",
            "key": "hd-video-only",
            "segmentSettings": {
              "segmentDuration": "6s"
            }
          },
          {
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ],
            "fileName": "audio-only.m4s",
            "key": "audio-only",
            "segmentSettings": {
              "segmentDuration": "6s"
            }
          },
          {
            "key": "text-vtt-english",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-english"
            ],
            "segmentSettings": {
              "individualSegments": true,
              "segmentDuration": "6s"
            }
          },
          {
            "key": "text-vtt-french",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-french"
            ],
            "segmentSettings": {
              "individualSegments": true,
              "segmentDuration": "6s"
            }
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "muxStreams": [
              "hd-video-only",
              "audio-only",
              "text-vtt-english",
              "text-vtt-french"
            ],
            "type": "HLS"
          }
        ],
        "output": {
          "uri": "gs://your-bucket/output/"
        }
      }
    }
    

The `vtt-stream-english` stream is generated from track 1 of `input0` because of the explicit mapping. The `vtt-stream-french` stream is generated from track 2 of `input0`.

### Default Mapping by Transcoder API

These examples rely on the API to infer which audio track to use based on the `attributes` provided in the `inputs`. The other parts of the configuration (`muxStreams`, `manifests`, `output`) are assumed to be similar to the complete example.

#### Single audio track with a known language

If your input video has one audio track (e.g., track 1) and you know it's in English (`en-US`), you can generate English subtitles. You can also request subtitles in other languages, like French (`fr-FR`), and the API will translate the English transcription.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "inputTrack": 1,
                "languages": [
                  "en-US"
                ]
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        },
        {
          "key": "vtt-stream-french",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "fr-FR",
            "displayName": "French"
          }
        }
      ]
    }
    

The English subtitle stream (`vtt-stream-english`) is generated directly from the defined audio track 1, as the language codes match. The French subtitle stream (`vtt-stream-french`) is produced by first transcribing the English audio from track 1 and then translating the resulting text to French.

#### Multiple audio tracks with known languages

When your input file contains multiple audio tracks with different languages (e.g., French on track 1, English on track 2), you can specify the languages for each track.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "inputTrack": 1,
                "languages": ["fr-FR"]
              },
              {
                "inputTrack": 2,
                "languages": ["en-US"]
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        },
        {
          "key": "vtt-stream-french",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "fr-FR",
            "displayName": "French"
          }
        }
      ]
    }
    

In this configuration, the `vtt-stream-english` subtitles are generated from audio track 2, and the `vtt-stream-french` subtitles are generated from audio track 1, based on the language codes provided in the `attributes`.

#### Output language not matching any input audio track

If the requested subtitle language doesn't match any defined track languages, the API uses the _first available_ audio track for transcription and translation.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "inputTrack": 1,
                "languages": ["fr-FR"]
              },
              {
                "inputTrack": 2,
                "languages": ["en-US"]
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-hindi",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "hi-IN",
            "displayName": "Hindi"
          }
        }
      ]
    }
    

Since no Hindi audio track is defined, the `vtt-stream-hindi` subtitles are generated by transcribing the first audio track (track 1, French) and then translating the transcription to Hindi.

#### Single audio track with mixed languages

If a single audio track contains multiple languages, list all of them in the `languages` array.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "inputTrack": 1,
                "languages": ["en-US", "fr-FR"]
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        },
        {
          "key": "vtt-stream-french",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "fr-FR",
            "displayName": "French"
          }
        },
        {
          "key": "vtt-stream-hindi",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "hi-IN",
            "displayName": "Hindi"
          }
        }
      ]
    }
    

All three VTT streams (English, French, and Hindi) are generated from audio track 1. The API will transcribe the mixed-language audio and provide each output stream in the single language specified by the `languageCode` field.

The API transcribes the audio, potentially detecting multiple languages within track 1. For each output `textStream`, it generates subtitles _only_ in the language specified by that stream's `languageCode` field.

#### Language detection on a specific audio track

Use `detectLanguages": true` when the language of a specific track is unknown.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "inputTrack": 1,
                "detectLanguages": true
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        }
      ]
    }
    

The API first detects the language(s) present in audio track 1. It then generates the English subtitles, including translation if the detected language is not English.

#### Language detection on the default audio track

If both the language and track number are unknown, the API defaults to using the first available audio track.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "detectLanguages": true
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        }
      ]
    }
    

The API analyzes the first audio track to detect the language(s) and then generates the English subtitles, translating if necessary.

#### Specify language for the default audio track

If you know the language but not the specific track number, the API assumes the first available audio track matches the language provided.
    
    
    {
      "inputs": [
        {
          "key": "input0",
          "uri": "gs://input-bucket/input.mp4",
          "attributes": {
            "trackDefinitions": [
              {
                "languages": ["en-US"]
              }
            ]
          }
        }
      ],
      "elementaryStreams": [
        { "key": "video-stream0", "videoStream": { ... } },
        { "key": "audio-stream0", "audioStream": { ... } },
        {
          "key": "vtt-stream-english",
          "textStream": {
            "codec": "webvtt",
            "languageCode": "en-US",
            "displayName": "English"
          }
        }
      ]
    }
    

The English subtitles (`vtt-stream-english`) are generated from the first audio track of the input, under the assumption that this track is in English.

## FAQ

**What happens if I specify both`languages` and `detectLanguages` in the same `trackDefinition`?**

You can only specify one of either the `languages` field or the `detectLanguages` field within a single `trackDefinition`. Providing both in the same definition is an invalid configuration and will result in an error.

**How does the API choose which audio track to use if multiple`trackDefinitions` match the language of a `textStream`?**

If you have multiple `trackDefinitions` in the `inputs.attributes.trackDefinitions` array that could potentially match the `languageCode` of a requested `textStream`, the API will use the audio track from the _first_ matching `trackDefinition` in the array order. This applies only when you are not using the explicit `mapping` field within the `textStream`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
