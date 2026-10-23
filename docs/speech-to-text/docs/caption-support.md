---
url: https://docs.cloud.google.com/speech-to-text/docs/caption-support/
title: Generate WebVTT and SRT captions \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:22.914712+00:00
---

# Generate WebVTT and SRT captions  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/caption-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Generate WebVTT and SRT captions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Cloud Speech-to-Text API to automatically generate captions from audio files, in SRT and WebVTT formats. These formats can store the text and timing information of audio, making it possible to display subtitles or captions in sync with the media for subtitling and closed captioning.

Enabling caption outputs in your request to Cloud Speech-to-Text is only supported in the V2 API. Specifically, you can only use `BatchRecognize` to transcribe long audio files. You can save outputs in a Cloud Storage bucket, or they can be returned inline. Multiple formats can be specified at the same time for the Cloud Storage output configuration, which is written to the specified bucket with different file extensions.

## Enable caption outputs in a request

To generate SRT or VTT caption outputs for your audio using Cloud Speech-to-Text, follow the next steps to enable caption outputs in your transcription request:

  1. Make a request to the Cloud Speech-to-Text API `BatchRecognize` method with the `output_format_config` field populated. Values specified are: 
     * `srt`, for the output to follow the [SRT format](https://www.matroska.org/technical/subtitles.html#srt-subtitles). \- `vtt`, for the output to follow the [WebVTT format](https://www.w3.org/TR/webvtt1/).
     * `native`, which is the default output format if no format is specified as a serialized `BatchRecognizeResults` request.
  2. Since the operation is async, poll the request until it's complete.



Multiple formats can be specified at the same time for the Cloud Storage output configuration. They're written to the specified bucket with different file extensions (either `.json`, `.srt`, or `.vtt`).

If multiple formats are specified for the inline output config, each format will be available as a field in the `BatchRecognizeFileResult.inline_result` message.

The following code snippet demonstrates how to enable caption outputs in a transcription request to Cloud Speech-to-Text using local and remote files:

### API
    
    
      curl -X POST \
        -H "Content-Type: application/json; charset=utf-8" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v2/projects/my-project/locations/global/recognizers/_:batchRecognize \
        --data '{
          "files": [{
            "uri": "gs://my-bucket/jfk_and_the_press.wav"
          }],
          "config": {
            "features": { "enableWordTimeOffsets": true },
            "autoDecodingConfig": {},
            "model": "long",
            "languageCodes": ["en-US"]
          },
          "recognitionOutputConfig": {
            "gcsOutputConfig": { "uri": "gs://my-bucket" },
            "output_format_config": { "srt": {} }
          }
        }'
    

## What's next

  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 
  * Learn how to [choose the best transcription model](https://docs.cloud.google.com/speech-to-text/docs/transcription-model). 
  * Transcribe audio files using [Chirp](https://docs.cloud.google.com/speech-to-text/docs/chirp-model). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
