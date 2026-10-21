---
url: https://docs.cloud.google.com/speech-to-text/docs/release-notes/
title: Speech-to-Text release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:11.783190+00:00
---

# Speech-to-Text release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Release notes ](https://docs.cloud.google.com/speech-to-text/docs/release-notes)



Send feedback 

#  Speech-to-Text release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud STT. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/speech-release-notes.xml) directly. 

## November 13, 2025

Feature

Speech-to-Text has just launched `chirp_3` in public preview for the regions `asia-south1`, `europe-west2`, `europe-west3` and `northamerica-northeast1`.

For more information about the Chirp 3 model, see [Chirp 3 Transcription: Enhanced multilingual accuracy](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3).

## October 13, 2025

Feature

Speech-to-Text is excited to announce the General Availability (GA) of the Chirp 3: Transcription, the latest generation of Google's multilingual Automatic Speech Recognition (ASR)-specific generative model, delivering state-of-the-art ASR accuracy and multilingual capabilities. Available exclusively in the Speech-to-Text API V2, Chirp 3 delivers significant enhancements in transcription accuracy and speed over previous versions. Under the new `chirp_3` model identifier, you can now leverage powerful new capabilities, including speaker diarization to identify different speakers and automatic language detection for multilingual audio. The model supports all major recognition methods —`StreamingRecognize`, `Recognize`, and `BatchRecognize`\- making it suitable for both real-time and batch processing. Chirp 3 also offers advanced features such as speech adaptation for custom vocabularies and a built-in denoiser to improve results from noisy audio. 

To explore the new Chirp 3: Transcription model's capabilities and learn how to leverage its full potential, please visit our [updated documentation page](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3). 

## August 29, 2025

Feature

Speech-to-Text has just launched `chirp_3` in Public Preview. With this Public Preview, Chirp 3: Transcription we are now expanding language transcription in more than 85+ languages and locales, in addition to StreamingRecognize and SyncRecognize requests for real-time and short-form audio. Under the `chirp_3` model flag, you can experience significant improvements in accuracy and speed, and leverage powerful features like Speaker Diarization and language-agnostic transcription. 

To explore the new Chirp 3: Transcription model's capabilities and learn how to leverage its full potential, please visit our [official documentation page](https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model).

## April 11, 2025

Feature

Speech-to-Text has launched `chirp_3` in Private Preview. Chirp 3: Transcription is the latest generation of Google's multilingual Automatic Speech Recognition (ASR)-specific generative models that further enhances its ASR accuracy and multilingual capabilities. Under the new `chirp_3` model flag, you can experience significant improvements in accuracy and speed, and leverage powerful new features like Speaker Diarization and language-agnostic transcription. Chirp 3 supports `BatchRecognize` requests within the Speech-to-Text v2 API, making it ideal for transcribing long-form audio.

To explore the new Chirp 3: Transcription model's capabilities and to learn how to leverage its full potential, please visit our [official documentation page](https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model). To gain access to this Private Preview, please [contact our sales team](https://cloud.google.com/contact).

## January 27, 2025

Feature

Speech-to-Text is generally available (GA) in the Chirp 2 model in `asia-southeast1`, `us-central1`, and `europe-west4`.

For more information about the Chirp 2 model, see [Chirp 2: Enhanced multilingual accuracy](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_2-model?_gl=1*la7eog*_ga*NzAyNzc4MTMxLjE3MzY5NjgxMTA.*_ga_4LYFWVHBEB*MTczODAxMTAzMy45My4xLjE3MzgwMTE2OTMuMC4wLjA.). For code samples, see [Get started with Chirp 2 using Speech-to-Text V2 SDK in GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/get_started_with_chirp_2_sdk.ipynb).

## October 07, 2024

Feature

Speech-to-Text has updated the Generally Available Chirp 2 model, further enhancing its ASR accuracy and multilingual capabilities. Under the existing `chirp_2` model flag, you can experience significant improvements in accuracy and speed, as well as support for word-level timestamps, model adaptation, and speech translation. Finally, Chirp 2 can support Streaming Recognizer requests, in addition to the already supported Sync and Batch Recognition requests, allowing its use in realtime applications.

Explore the new chirp_2 model's capabilities and learn how to leverage its full potential by visiting our [updated documentation](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_2-model) and [tutorials](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/get_started_with_chirp_2_sdk.ipynb).

## January 09, 2024

Feature

[Model adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model) is now available for `latest_long` models in 13 languages. Also, its quality was substantially improved for `latest_short` models. To determine whether this feature is available for your language, see [Language support](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).

## January 08, 2024

Feature

Speech-to-Text has launched a new model, named `chirp_telephony` to bring the accuracy gains of our `chirp` model to telephony-specific use cases. The new model is a fine-tuned version of our very successful `chirp` model, based on the Universal large Speech Model(USM) architecture, on audio that originated from a phone call typically recorded at an 8 kHz sampling rate. For more information, see [Speech-to-Text supported languages](https://docs.cloud.google.com/speech-to-text/v2/docs/speech-to-text-supported-languages).

## November 06, 2023

Feature

Speech-to-Text has launched two models, named `telephony` and `telephony_short`. The two models are customized to recognize audio that originates from a phone call and corresponds to the most recent versions of the existing `phone_call` model. For more information, see [Speech-to-Text supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).

## February 07, 2023

Announcement

We are removing `SpeechContext.strength` field within the next 4 weeks, because it has been deprecated and unused for more than a year. The documentation doesn't have references to this field anymore, and the clients aren't supposed to use it.

## November 11, 2022

Change

Speech-to-Text has updated its pricing policy. Enhanced models are no longer priced differently than standard models. Usage of all models will be reported to and priced like standard models. Also, all Cloud Speech-to-Text requests will now be rounded up to the nearest 1 second, with no minimum audio length (requests were previously rounded up to the nearest 15 seconds). See the [Pricing](https://cloud.google.com/speech-to-text/pricing) page for details.

## October 03, 2022

Feature

Speaker Diarization is now available for "Latest" models in en-US. This feature recognizes multiple speakers in the same audio clip. Latest models use a new model for diarization from previous models. For more information see [Speaker Diarization](https://cloud.google.com/speech-to-text/docs/multiple-voices#speaker_diarization).

## April 21, 2022

Change

"Latest" models are available in more than 20 languages. These models employ new end-to-end machine learning techniques and can improve the accuracy of your recognized speech. For more information see [Latest models](https://docs.cloud.google.com/speech-to-text/docs/latest-models).

## November 08, 2021

Feature

Speech-to-Text has launched two new medical speech models, which are tailored for recognition of words that are common in medical settings. See the [medical models documentation](https://docs.cloud.google.com/speech-to-text/docs/medical-models) for more details.

## July 21, 2021

Announcement

Speech-to-Text has launched a GA version of the Spoken Emoji and Spoken Punctuation features. See the [documentation](https://docs.cloud.google.com/speech-to-text/docs/spoken-punctuation-emojis) for details.

## June 28, 2021

Feature

The Speech-to-Text now supports multi-region endpoints as a GA feature. See the [multi-region endpoints](https://docs.cloud.google.com/speech-to-text/docs/endpoints) documentation for more information.

## May 24, 2021

Feature

Speech-to-Text now supports Spoken Punctuation and Spoken Emoji as Preview features. See the [documentation](https://docs.cloud.google.com/speech-to-text/docs/spoken-punctuation-emojis) for details.

## May 07, 2021

Feature

The Speech-to-Text [model adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation) feature is now a GA feature. See the [model adaptation concepts page](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model) for more information about using this feature.

## March 23, 2021

Feature

Speech-to-Text now allows you to upload your longrunning transcription results directly into a Cloud Storage bucket. See the [asynchronous speech recognition documentation](https://docs.cloud.google.com/speech-to-text/docs/async-recognize#uploading_your_transcription_results_to_a_gcs_bucket) for more details.

## March 15, 2021

Feature

Speech-to-Text has launched the [Model Adaptation feature](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model). You can now create [custom classes](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#custom_classes) and build [phrase sets](https://docs.cloud.google.com/speech-to-text/docs/adaptation) to improve your transcription results.

## January 26, 2021

Feature

Speech-to-Text now supports regional EU and US endpoints. See the [multi-region endpoints](https://docs.cloud.google.com/speech-to-text/docs/endpoints) documentation for more information.

## August 25, 2020

Feature

Speech-to-Text has launched the new [On-Prem API](https://docs.cloud.google.com/speech-to-text/on-prem). Speech-to-Text On-Prem enables easy integration of Google speech recognition technologies into your on-premises solution.

## March 05, 2020

Feature

Cloud Speech-to-Text now supports seven new [languages](https://docs.cloud.google.com/speech-to-text/docs/languages): Burmese, Estonian, Uzbek, Punjabi, Albanian, Macedonian, and Mongolian.

Feature

The [speaker diarization](https://docs.cloud.google.com/speech-to-text/docs/multiple-voices), [automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation), [speech adaptation boost](https://docs.cloud.google.com/speech-to-text/docs/boost), and [enhanced telephony model](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models) features are now available for new languages. See the supported [languages page](https://docs.cloud.google.com/speech-to-text/docs/languages) for a complete list.

Change

[Class tokens](https://docs.cloud.google.com/speech-to-text/docs/class-tokens) are now available for general use. You can use class tokens with [speech adaptation](https://docs.cloud.google.com/speech-to-text/docs/speech-adaptation#classes) to help the model recognize concepts in your recorded audio data.

## November 26, 2019

Change

[Automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation) is now available for general use. Cloud Speech-to-Text can insert punctuation into transcription results, including commas, periods, and question marks.

## July 23, 2019

Feature

Cloud Speech-to-Text has several [endless streaming tutorials](https://docs.cloud.google.com/speech-to-text/docs/endless-streaming-tutorial) that demonstrate how to transcribe an infinite audio stream.

Feature

You can now use [speech adaptation](https://docs.cloud.google.com/speech-to-text/docs/context-strength) to provide 'hints' to Cloud Speech-to-Text when it performs speech recognition. This feature is now in beta.

## June 18, 2019

Feature

Cloud Speech-to-Text now has expanded to a 5 minute limit for [streaming recognition](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). To use streaming recognition with the 5 minute limit, you must use the [`v1p1beta1`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#speech) API version.

Feature

Cloud Speech-to-Text now supports transcription of [MP3 encoded audio data](https://docs.cloud.google.com/speech-to-text/docs/encoding). As this feature is in beta, you must use the [`v1p1beta1`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#speech) API version.

## April 04, 2019

Deprecated

The `v1beta` version of the service is no longer available for use. You must migrate your solutions to either the [`v1`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1) or [`v1p1beta1`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1) version of the API.

## February 20, 2019

Feature

[Data logging](https://docs.cloud.google.com/speech-to-text/docs/data-logging) is now available for general use. When you enable data logging, you can reduce the cost of using Cloud Speech-to-Text by allowing Google to log your data in order to improve the service.

Change

Using [enhanced models](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models) no longer requires you to opt-in for data logging. Enhanced models are available for use by any transcription requests for a different [price](https://cloud.google.com/speech-to-text/pricing) as standard models.

Feature

[Enhanced models](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models) are now available for general use. Using enhanced models can improve audio transcription results.

Feature

[Selecting a transcription model](https://docs.cloud.google.com/speech-to-text/docs/transcription-model) is now available for general use. You can select different speech recognition models when you send a request to Cloud Speech-to-Text, including a model optimized for transcribing audio data from video files.

Feature

You can now include more details about your audio source files in transcription requests to Cloud Speech-to-Text in the form of [recognition metadata](https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-recognition-metadata-beta), which can improve the results of the speech recognition. This feature is now available for general use.

Feature

Cloud Speech-to-Text can transcribe audio data that includes [multiple channels](https://docs.cloud.google.com/speech-to-text/docs/multi-channel). This feature is now available for general use.

## July 24, 2018

Feature

Cloud Speech-to-Text provides [word-level confidence](https://docs.cloud.google.com/speech-to-text/docs/word-confidence) Developers can use this feature to get the degree of confidence on a word-by-word level. This feature is in Beta.

Feature

Cloud Speech-to-Text can automatically detect the language used in an audio file. To use this feature, developers must specify [alternative languages](https://docs.cloud.google.com/speech-to-text/docs/multiple-languages) in their transcription request. This feature is in Beta.

Feature

Cloud Speech-to-Text can [identify different speakers](https://docs.cloud.google.com/speech-to-text/docs/multiple-voices) present in an audio file. This feature is in Beta.

Feature

Cloud Speech-to-Text can transcribe audio data that includes [multiple channels](https://docs.cloud.google.com/speech-to-text/docs/multi-channel). This feature is in Beta.

## April 09, 2018

Feature

Cloud Speech-to-Text now provides [data logging](https://docs.cloud.google.com/speech-to-text/docs/data-logging) and [enhanced models](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models). Developers that want to take advantage of the enhanced speech recognition models can [opt-in for data logging](https://docs.cloud.google.com/speech-to-text/docs/data-logging-terms). This feature is in Beta.

Feature

Cloud Speech-to-Text can insert [punctuation](https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation) into transcription results, including commas, periods, and question marks. This feature is in Beta.

Feature

You can now select different speech recognition models when you send a request to Cloud Speech-to-Text, including a model optimized for [transcribing audio from video files](https://docs.cloud.google.com/speech-to-text/docs/video-model). This feature is in Beta.

Feature

You can now include more details about your audio source files in transcription requests to Cloud Speech-to-Text in the form of [recognition metadata](https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-recognition-metadata-beta), which can improve the results of the speech recognition. This feature is in Beta.

## January 16, 2018

Feature

Support for the `OGG_OPUS` audio encoding has been expanded to support 8000 Hz, 12000 Hz, 16000 Hz, 24000 Hz, or 48000 Hz.

## August 10, 2017

Feature

Time offsets (timestamps) are now available. Set the `enableWordTimeOffsets` parameter to true in your request configuration and Cloud Speech-to-Text will include time offset values for the beginning and end of each spoken word that is recognized in the audio for your request. For more information, see [Time offsets (timestamps)](https://docs.cloud.google.com/speech-to-text/docs/basics#time-offsets).

Change

Cloud Speech-to-Text has added recognition support for 30 new languages. For a complete list of all supported languages, see the [language support reference](https://docs.cloud.google.com/speech-to-text/docs/languages).

Change

The limit on the length of audio that you can send with an asynchronous recognition request has been increased from ~80 to ~180 minutes. For information on Cloud Speech-to-Text limits, see the [quotas & limits](https://docs.cloud.google.com/speech-to-text/quotas). For more information on asynchronous recognition requests, see the [transcribing long audio files guide](https://docs.cloud.google.com/speech-to-text/docs/async-recognize).

## April 18, 2017

Feature

Release of Cloud Speech-to-Text v1.

Change

The `v1beta1` release of Cloud Speech-to-Text has been deprecated. The `v1beta1` endpoint continues to be available for a period of time as defined in the [terms of service](https://cloud.google.com/terms). To avoid being impacted when the `v1beta1` is discontinued, replace references to `v1beta1` in your code with `v1` and update your code with valid `v1` API names and values.

Change

The `result_index field` has been removed.

Change

The `sample_rate` field has been renamed to `sample_rate_hertz`. The behavior is unchanged.

Change

A `language_code` is now required with requests to Cloud Speech-to-Text. Requests with a missing or invalid `language_code` will return an error. (Pre-release versions of the API used `en-US` if the `language_code` was omitted from the request.)

Change

The `EndpointerType` enum has been renamed to `SpeechEventType`.

The following `SpeechEventType` enums have been removed.

  * `START_OF_SPEECH`
  * `END_OF_SPEECH`
  * `END_OF_AUDIO`



Change

`SyncRecognize` is renamed to `Recognize`. `v1beta1/speech:syncrecognize` is renamed to `v1/speech:recognize`. The behavior is unchanged.

Change

The `END_OF_UTTERANCE` enum has been renamed to `END_OF_SINGLE_UTTERANCE`. The behavior is unchanged.

Change

The `speech_context` field has been replaced by the `speech_contexts` field, which is a repeated field. However, you can specify, at most, one speech context. The behavior is unchanged.

Change

You are no longer required to specify the encoding and sample rate for WAV or FLAC files. If omitted, Cloud Speech-to-Text automatically determines the encoding and sample rate for WAV or FLAC files based on the file header. If you specify an encoding or sample rate value that does not match the value in the file header, then Cloud Speech-to-Text will return an error. This change is backwards-compatible and will not invalidate any currently valid requests.

Change

The `SPEEX_WITH_HEADER_BYTE` and `OGG_OPUS` codecs have been added to support audio encoder implementations for legacy applications. We do not recommend using lossy codes, as they result in a lower-quality speech transcription. If you must use a low-bitrate encoder, `OGG_OPUS` is preferred.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
