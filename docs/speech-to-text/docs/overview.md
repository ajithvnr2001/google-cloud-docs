---
url: https://docs.cloud.google.com/speech-to-text/docs/overview/
title: Cloud Speech-to-Text overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:26.296687+00:00
---

# Cloud Speech-to-Text overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Cloud Speech-to-Text overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Speech-to-Text is an API that lets you integrate Google's speech recognition technologies into your developer applications. This document covers the basics of using Cloud Speech-to-Text, including the types of requests you can make to Cloud STT, how to construct those requests, and how to handle their responses. Before you dive into using the API, read this guide and one of the associated tutorials.

## Cloud Speech-to-Text recognition requests

Cloud Speech-to-Text (STT) has three main methods to perform speech recognition. The following methods are available:

  * [**Synchronous recognition**](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize) (REST and gRPC) sends audio data to the Cloud Speech-to-Text API, performs recognition on that data, and returns results after all audio has been processed. Synchronous recognition requests process audio data of 1 minute or less.

  * [**Asynchronous recognition**](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize) (REST and gRPC) sends audio data to the Cloud Speech-to-Text API and initiates a _long-running operation_. Using this operation, you can periodically poll for recognition results. Use asynchronous requests for audio data of any duration up to 480 minutes.

  * [**Streaming recognition**](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize) (gRPC only) performs recognition on audio data provided within a [gRPC bi-directional stream](http://www.grpc.io/docs/guides/concepts.html#bidirectional-streaming-rpc). Streaming requests are designed for real-time recognition purposes, such as capturing live audio from a microphone. Streaming recognition provides interim results as audio is captured. For example, results can appear while a user is still speaking.




Requests contain configuration parameters as well as audio data. Recognition requests can optionally contain a [recognizer](https://docs.cloud.google.com/speech-to-text/docs/recognizers), a stored and reusable recognition configuration.

### Audio Metadata

For most audio files, Cloud Speech-to-Text API can automatically deduce the audio metadata. Cloud STT parses the header of the file and decodes it according to that information. See the [encoding](https://docs.cloud.google.com/speech-to-text/docs/encoding) page for supported file types.

For headerless audio files, Cloud Speech-to-Text API lets you specify the audio metadata explicitly in the recognition config. See the [encoding](https://docs.cloud.google.com/speech-to-text/docs/encoding) page for more details.

If you have a choice when encoding the source material, capture audio using a sample rate of 16000 Hz. Values lower than this can impair speech recognition accuracy, and higher levels have no appreciable effect on speech recognition quality.

However, if your audio data has already been recorded at an existing sample rate other than 16000 Hz, don't resample your audio to 16000 Hz. For example, most legacy telephony audio uses sample rates of 8000 Hz, which can give less accurate results. If you must use such audio, provide the audio to the Cloud Speech-to-Text API at its original sample rate.

### Languages

Cloud STT's recognition engine supports a variety of languages and dialects. You specify the language (and national or regional dialect) of your audio within the request configuration's `languageCode` field, using a [BCP-47](https://tools.ietf.org/html/bcp47) identifier.

A full list of supported languages for each feature is available on the [Supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) page.

### Recognition features

Cloud Speech-to-Text API has additional recognition features such as [automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation) and [word-level confidence](https://docs.cloud.google.com/speech-to-text/docs/word-confidence). You enable these features in the recognition configuration in requests. See the sample code in the provided links and the [languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) page for feature availability.

### Model selection

Cloud STT can use one of several machine learning _models_ to transcribe your audio file. Google has trained these speech recognition models for specific audio types and sources. See the [model selection](https://docs.cloud.google.com/speech-to-text/docs/transcription-model) documentation to learn about the available models and how to select one in your requests.

### Embedded audio content

You include embedded audio in the speech recognition request by passing a `content` parameter within the request's `audio_source` field. For embedded audio that you provide as content within a gRPC request, the audio must be compatible with [Proto3](https://developers.google.com/protocol-buffers/docs/reference/proto3-spec) serialization and provided as binary data. For embedded audio that you provide as content within a REST request, the audio must be compatible with JSON serialization and first be Base64-encoded. See [Base64 Encoding Your Audio](https://docs.cloud.google.com/speech-to-text/docs/base64-encoding) for more information.

When constructing a request using a [Google Cloud client library](https://cloud.google.com/sdk/cloud-client-libraries), you generally write out this binary (or Base64-encoded) data directly within the `content` field.

### Pass audio referenced by a URI

More typically, you pass a `uri` parameter within the Cloud Speech-to-Text API request's `audio_source` field, pointing to an audio file (in binary format, not Base64) located on Cloud Storage in the following form:
    
    
    gs://bucket-name/path/to/audio/file
    

Speech-to-Text uses a service account to access your files in Cloud Storage. By default, the service account has access to Cloud Storage files in the same project.

The service account email address is the following:
    
    
    service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com
    

In order to transcribe Cloud Storage files in another project, you can give this service account the [Speech-to-Text Service Agent][speech-service-agent] role in the other project:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com \
        --role=roles/speech.serviceAgent

More information about project IAM policy is available at [Manage access to projects, folders, and organizations][manage-access].

You can also give the service account more granular access by giving it permission to a specific Cloud Storage bucket:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com \
        --role=roles/storage.admin

More information about managing access to Cloud Storage is available at [Create and Manage access control lists][buckets-manage-acl] in the Cloud Storage documentation.

## Cloud Speech-to-Text API responses

After Cloud Speech-to-Text API processes audio, it returns the transcription results in [`SpeechRecognitionResult`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#speechrecognitionresult) messages for synchronous and batch requests, and in [`StreamingRecognitionResult`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#streamingrecognitionresult) messages for streaming requests. In synchronous and batch requests, the RPC response contains a list of results. The list of recognized audio appears in contiguous order. For streaming responses, all results marked as `is_final` appear in contiguous order.

**Note:** If Cloud Speech-to-Text API cannot recognize speech from the supplied audio, then the `results` field in the RPC response contains no items. Unrecognized speech is commonly the result of very poor-quality audio, or from language code, encoding, or sample rate values that don't match the supplied audio.

### Select alternatives

Each result within a successful synchronous recognition response can contain one or more `alternatives` (if the [`max_alternatives`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.RecognitionFeatures.FIELDS.int32.google.cloud.speech.v2.RecognitionFeatures.max_alternatives) is greater than `1`). If Cloud STT determines that an alternative has a sufficient confidence value, then Cloud STT includes that alternative in the response. The first alternative in the response is always the best (most likely) alternative.

Setting `max_alternatives` to a higher value than `1` does not imply or guarantee that multiple alternatives are returned. In general, more than one alternative is more appropriate for providing real-time options to users who get results through a [streaming recognition request](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize).

### Handling transcriptions

Each alternative in the response contains a `transcript` with the recognized text. When you receive sequential alternatives, concatenate these transcriptions.

### Confidence values

The `confidence` value is an estimate between 0.0 and 1.0. It's calculated by aggregating the "likelihood" values assigned to each word in the audio. A higher number indicates a greater estimated likelihood that the individual words are recognized correctly. This field is typically provided only for the top hypothesis and only for results where `is_final=true`. For example, you can use the `confidence` value to decide whether to show alternative results or ask for your confirmation.

Be aware, however, that the model determines the "best", top-ranked result based on more signals than the `confidence` score alone (such as sentence context). Because of this, occasional cases exist where the top result doesn't have the highest confidence score. If you haven't requested multiple alternative results, the single "best" result can have a lower confidence value than anticipated. This can occur, for example, when rare words are used. Even if the system recognizes a rarely used word correctly, it can be assigned a low "likelihood" value. If the model determines the rare word to be the most likely option based on context, it returns that result at the top even if the result's `confidence` value is lower than alternative options.

**Important:** Don't include `confidence` as a required field in your code. It may not be set in any of the results, and it may not be accurate.

## What's next

  * Use [client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) to transcribe audio using your favorite programming language. 
  * Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
