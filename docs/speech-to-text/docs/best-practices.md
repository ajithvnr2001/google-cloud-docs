---
url: https://docs.cloud.google.com/speech-to-text/docs/best-practices/
title: Best practices \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:28.539870+00:00
---

# Best practices  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document contains recommendations on how to provide speech data to the Speech-to-Text API. These guidelines are designed for greater efficiency and accuracy as well as reasonable response times from the service. Use of the Speech-to-Text API works best when data sent to the service is within the parameters described in this document.

If you follow these guidelines and don't get the results you expect from the API, see [Troubleshooting & Support](https://docs.cloud.google.com/speech-to-text/docs/support).

For optimal results... | If possible, avoid...  
---|---  
Capture audio with a sampling rate of 16,000 Hz or higher. | Lower sampling rates may reduce accuracy. However, avoid re-sampling. For example, in telephony the native rate is commonly 8000 Hz, which is the rate that should be sent to the service.  
Use a lossless codec to record and transmit audio. `FLAC` or `LINEAR16` is recommended. | Using mp3, mp4, m4a, mu-law, a-law or other lossy codecs during recording or transmission may reduce accuracy. If your audio is already in an encoding not supported by the API, transcode it to lossless `FLAC` or `LINEAR16`. If your application must use a lossy codec to conserve bandwidth, we recommend the `AMR_WB` or `OGG_OPUS` codecs, in that preferred order.  
The recognizer is designed to ignore background voices and noise without additional noise-canceling. However, for optimal results, position the microphone as close to the user as possible, particularly when background noise is present. | Excessive background noise and echoes may reduce accuracy, especially if a lossy codec is also used.  
If you are capturing audio from more than one person, and each person is recorded on a separate channel, send each channel separately to get the best recognition results. However, if all speakers are mixed in a single channel recording, send the recording as is. | Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored.  
Use word and phrase hints to add names and terms to the vocabulary and to boost the accuracy for specific words and phrases. | The recognizer has a very large vocabulary, however terms and proper names that are out-of-vocabulary will not be recognized.  
  
## Sampling rate

If possible, set the sampling rate of the audio source to 16000 Hz.

For headerless codecs, use the [explicit_decoding_config](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#explicitdecodingconfig) setting in [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognitionconfig) to set sample_rate_hertz to match the native sample rate of the audio source (instead of re-sampling).

For codecs with a header, use the [auto_decoding_config](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#autodetectdecodingconfig) setting in [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognitionconfig) to automatically choose the correct sampling rate.

## Frame size

Streaming recognition recognizes live audio as it is captured from a microphone or other audio source. The audio stream is split into frames and sent in consecutive `StreamingRecognizeRequest` messages. Any frame size is acceptable. Larger frames are more efficient, but add latency. A 100-millisecond frame size is recommended as a good tradeoff between latency and efficiency.

## Audio preprocessing

It's best to provide audio that is as clean as possible by using a good quality and well-positioned microphone. However, applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy. The service is designed to handle noisy audio.

For best results:

  * Position the microphone as close as possible to the person that is speaking, particularly when background noise is present.
  * Avoid audio clipping.
  * Do not use automatic gain control (AGC).
  * All noise reduction processing should be disabled.
  * Listen to some sample audio. It should sound clear, without distortion or unexpected noise.



## Request configuration

Make sure that you accurately describe the audio data sent with your request to the Speech-to-Text API. Ensuring that the [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognitionconfig) for your request describes the correct `sampleRateHertz`, `encoding`, and that you are using a [Recognizer](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognizer) with the correct `language_codes` and `model` will result in the most accurate transcription and billing for your request.

## What's next

  * Use [client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) to transcribe audio using your favorite programming language. 
  * Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
