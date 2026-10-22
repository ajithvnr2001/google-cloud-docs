---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt/
title: Learn about speech recognition features \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:08.603243+00:00
---

# Learn about speech recognition features  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Learn about speech recognition features Stay organized with collections  Save and categorize content based on your preferences. 

Speech-to-Text is one of the three Vertex AI pre-trained APIs on Google Distributed Cloud (GDC) air-gapped. The Speech-to-Text service recognizes speech in audio files and transcribes audio into text. Speech-to-Text meets data residency and compliance requirements.

The following table describes the key capabilities of Speech-to-Text:

Key capabilities |   
---|---  
Transcription | Apply advanced deep learning neural network algorithms for automatic speech recognition.  
Models | Deploy recognition models that are less than 1 GB in size and consume minimal resources.  
API compatible | Use the Speech-to-Text API and its client libraries to send audio and receive a text transcription from the Speech-to-Text service.  
  
## Supported audio encodings for Speech-to-Text

**Important:** The Speech-to-Text API doesn't support video files, only audio.

The Speech-to-Text API supports a number of different encodings. The following table lists supported audio codecs:

Codec | Name | Lossless | Usage notes  
---|---|---|---  
`FLAC` | Free Lossless Audio Codec | Yes | 16-bit or 24-bit required for streams  
`LINEAR16` | Linear PCM | Yes | 16-bit linear pulse-code modulation (PCM) encoding. The header must contain the sample rate.  
`MULAW` | μ-law | No | 8-bit PCM encoding  
`OGG_OPUS` | Opus encoded audio frames in an Ogg container | No | Sample rate must be one of 8000 Hz, 12000 Hz, 16000 Hz, 24000 Hz, or 48000 Hz  
  
`FLAC` is both an audio codec and an audio file format. To transcribe audio files using `FLAC` encoding, you must provide them in the `.FLAC` file format, which includes a header containing metadata.

Speech-to-Text supports `WAV` files with `LINEAR16` or `MULAW` encoded audio.

For more information on Speech-to-Text audio codecs, consult the [`AudioEncoding`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#audioencoding) reference documentation.

If you have a choice when encoding the source material, use a lossless encoding such as `FLAC` or `LINEAR16` for better speech recognition.

## Speech-to-Text features

Speech-to-Text on Distributed Cloud has the following three methods to perform speech recognition:

  * **Synchronous recognition** : sends audio data to the Speech-to-Text API, performs recognition on that data, and returns results after audio processing. Synchronous recognition requests are limited to one minute or less of audio data.

  * **Asynchronous recognition** : sends audio data to the Speech-to-Text API and initiates a [long-running operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary#l). Using this operation, you can periodically poll for recognition results. Use asynchronous requests for audio data of any duration up to 480 minutes.

  * **Streaming recognition** : performs recognition on audio data provided within a bidirectional stream. Streaming requests are designed for real-time recognition purposes, such as capturing live audio from a microphone. Streaming recognition provides interim results while audio is being captured, allowing results to appear, for example, while a user is still speaking.




Requests contain configuration parameters and audio data. The following sections describe these recognition requests, the responses they generate, and how to handle those responses in more detail.

## Synchronous requests and responses

A Speech-to-Text synchronous recognition request is the simplest method for performing recognition on speech audio data. Speech-to-Text can process up to one minute of speech audio data sent in a synchronous request. After Speech-to-Text processes and recognizes all of the audio, it returns a response.

Speech-to-Text must return a response before processing the next request. Speech-to-Text typically processes audio faster than real-time, on average processing 30 seconds of audio in 15 seconds. In cases of poor audio quality, your recognition request can take significantly longer.

### Speech recognition requests

A synchronous Speech-to-Text API request comprises a speech recognition configuration and audio data. The following example shows a request:
    
    
    {
        "config": {
            "encoding": "LINEAR16",
            "sample_rate_hertz": 16000,
            "language_code": "en-US",
        },
        "audio": {
            "content": "ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv..."
        }
    }
    

All Speech-to-Text synchronous recognition requests must include a speech recognition `config` field of type `RecognitionConfig`. A `RecognitionConfig` object contains the following required sub-fields:

  * `encoding`: specifies the encoding scheme of the supplied audio. This field is of type `AudioEncoding`. If you have a choice in a codec, prefer a lossless encoding such as `FLAC` or `LINEAR16` for best performance. For a list of supported audio encoding formats, see Supported audio encodings for Speech-to-Text. The `encoding` field is optional for `FLAC` and `WAV` files, which include the encoding in the file header.
  * `sample_rate_hertz`: specifies the sample rate of the supplied audio in Hertz. For more information on sample rates, see Sample rates. The `sample_rate_hertz` field is optional for `FLAC` and `WAV` files, which include the sample rate in the file header.
  * `language_code`: contains the language and region to use for speech recognition of the supplied audio. The language code must be a [BCP-47](https://www.rfc-editor.org/info/bcp47) identifier. Language codes consist of primary language tags and secondary region subtags to indicate dialects. In the example, `en` is for English, and `US` is for the United States. For a list of supported languages, see [Supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt-supported-langs).



For more information and a description of optional sub-fields you can include in the `config` field, see [`RecognitionConfig`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#recognitionconfig).

Provide audio to Speech-to-Text through the `audio` parameter of type [`RecognitionAudio`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#recognitionaudio). The `audio` field contains the following sub-field:

  * `content`: contains the audio to evaluate, embedded within the request. The audio data bytes are encoded using a pure binary representation. JSON representations use Base64. See Embedded audio content for more information. Audio passed directly within this field is limited to one minute in duration.



#### Sample rates

You specify the sample rate of your audio in the `sample_rate_hertz` field of the request configuration, and it must match the sample rate of the associated audio content. Speech-to-Text supports sample rates between 8000 Hz and 48000 Hz. You can specify the sample rate for a `FLAC` or `WAV` file in the file header instead of using the `sample_rate_hertz` field. However, the `sample_rate_hertz` field is required for all other audio formats.

If you have a choice when encoding the source material, capture audio using a sample rate of 16000 Hz. Lower values might impair speech recognition accuracy, and higher levels have no appreciable effect on speech recognition quality.

However, if you recorded your audio data at a sample rate other than 16000 Hz, don't resample your audio to 16000 Hz. Most legacy telephony audio, for example, uses sample rates of 8000 Hz, which might give less accurate results. If you must use such audio, provide it to the Speech-to-Text API at its original sample rate.

#### Languages

The recognition engine of Speech-to-Text supports a variety of languages and dialects. You specify your audio's language (and national or regional dialect) within the `language_code` field of the request configuration using a [BCP-47](https://www.rfc-editor.org/info/bcp47) identifier.

The [Supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt-supported-langs) page has a complete list of supported languages for each feature.

#### Model selection

When you send an audio transcription request to Speech-to-Text, you can process your audio files using a machine learning model trained to recognize speech audio from that particular source type.

To specify a model for speech recognition, include the `model` field in the [`RecognitionConfig`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#recognitionconfig) object for your request, specifying the model you want to use.

Speech-to-Text on Distributed Cloud supports the following model:

  * `default`: transcribe audio that is not a specific audio model, such as long-form audio.



#### Embedded audio content

Embedded audio is included in the speech recognition request when passing a `content` parameter within the request's `audio` field. For embedded audio provided as content within a REST request, that audio must be compatible with JSON serialization.

You can send data directly in the `content` field for synchronous recognition only if your audio data is a maximum of 60 seconds and 10 MB. Any audio data in the `content` field must be in Base64 format.

When constructing a request using a [client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries), you write out this binary or Base64-encoded data directly within the `content` field.

Most development environments come with a `base64` utility to encode a binary into ASCII text data, providing you with the necessary tools and support. Additionally, Python has built-in mechanisms for Base64 encoding content. The following examples show how to encode a file:

### Linux

Encode the file using the `base64` command line tool. Prevent line-wrapping by using the `-w 0` flag:
    
    
    base64 INPUT_FILE -w 0 > OUTPUT_FILE
    

### Python

In Python, Base64 encode audio files as follows:
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the audio data to an encoding function.
    def encode_audio(audio):
      audio_content = audio.read()
      return base64.b64encode(audio_content)
    

### Speech recognition responses

A synchronous Speech-to-Text API response might take some time to return results. Once processed, the API returns a response as in the following example:
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              "words": [
                {
                  "word": "how"
                },
                {
                  "word": "old"
                },
                {
                  "word": "is"
                },
                {
                  "word": "the"
                },
                {
                  "word": "Brooklyn"
                },
                {
                  "word": "Bridge"
                }
              ]
            }
          ]
        }
      ]
    }
    

All Speech-to-Text API synchronous recognition responses include speech recognition results of type `RecognizeResponse`. A `RecognizeResponse` object contains the following fields:

  * `results`: contains the list of results of type `SpeechRecognitionResult`, where each result corresponds to a segment of audio. Each result consists of one or more of the following sub-fields:

    * `alternatives`: contains a list of possible transcriptions of type `SpeechRecognitionAlternative`. The first alternative in the response is always the most likely. Each alternative consists of the following sub-fields:

      * `transcript`: contains the transcribed text. When provided with sequential alternatives, you can concatenate these transcriptions together.
      * `words`: contains a list of word-specific information for each recognized word.

**Note:** Pauses separate segments of audio. If Speech-to-Text doesn't recognize speech from the supplied audio, the returned `results` list contains no items. Unrecognized speech is commonly the result of poor-quality audio or from language code, encoding, or sample rate values that don't match the supplied audio.

For more information, see [`RecognizeResponse`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#recognizeresponse).

## Asynchronous requests and responses

An asynchronous Speech-to-Text API request is identical in form to a synchronous request. However, instead of returning a response, the asynchronous request initiates a [long-running operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary#l) and returns this operation immediately. You can use asynchronous speech recognition with audio of any length up to 480 minutes.

The following is an example of an operation response:
    
    
    {
      "name": "OPERATION_NAME",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.speech_v1p1beta1.LongRunningRecognizeMetadata"
        "progressPercent": 34,
        "startTime": "2016-08-30T23:26:29.579144Z",
        "lastUpdateTime": "2016-08-30T23:26:29.826903Z"
      }
    }
    

Note that results are not yet present. Speech-to-Text continues to process the audio and uses this operation to store the results. Results appear in the `response` field of the operation returned when the `LongRunningRecognize` request is complete.

The following is an example of a full response after completion of the request:
    
    
    {
      "name": "1268386125834704889",
      "metadata": {
        "lastUpdateTime": "2016-08-31T00:16:32.169Z",
        "@type": "type.googleapis.com/google.cloud.speech_v1p1beta1.LongRunningRecognizeMetadata",
        "startTime": "2016-08-31T00:16:29.539820Z",
        "progressPercent": 100
      }
      "response": {
        "@type": "type.googleapis.com/google.cloud.speech_v1p1beta1.LongRunningRecognizeResponse",
        "results": [{
          "alternatives": [{
            "transcript": "how old is the Brooklyn Bridge",
            "words": [
                {
                  "word": "how"
                },
                {
                  "word": "old"
                },
                {
                  "word": "is"
                },
                {
                  "word": "the"
                },
                {
                  "word": "Brooklyn"
                },
                {
                  "word": "Bridge"
                }
              ]
          }]}]
      },
      "done": True
    }
    

Note that `done` is set to `True` and that the operation's `response` contains a set of results of type [`SpeechRecognitionResult`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#speechrecognitionresult), the same type returned by a synchronous recognition request.

## Streaming requests and responses

A streaming Speech-to-Text API recognition call is designed for real-time capture and recognition of audio within a bidirectional stream. Your application can send audio on the request stream and receive real-time interim and final recognition results on the response stream. Interim results represent the current recognition result for a section of audio, while the final recognition result represents the last, best guess for that section of audio.

### Streaming recognition requests

Unlike synchronous and asynchronous calls, in which you send both the configuration and audio within a single request, calling the streaming Speech-to-Text API requires sending multiple requests. The first [`StreamingRecognizeRequest`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#streamingrecognizerequest) must contain a configuration of type [`StreamingRecognitionConfig`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#streamingrecognitionconfig).

A `StreamingRecognitionConfig` consists of the `config` field, which contains configuration information for the audio of type [`RecognitionConfig`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#recognitionconfig) and is the same as the one shown within synchronous and asynchronous requests.

### Streaming recognition responses

Streaming speech recognition results return a series of responses of type [`StreamingRecognizeResponse`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#streamingrecognizeresponse). Such a response consists of the following fields:

  * `speech_event_type`: contains events of type [`SpeechEventType`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#speecheventtype). The value of these events indicates when a single utterance has been completed. The speech events serve as markers within your stream's response.
  * `results`: contains the list of results, which might be either interim or final results of type [`StreamingRecognitionResult`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#streamingrecognitionresult). The `results` list includes the following sub-fields: 
    * `alternatives`: contains a list of alternative transcriptions.
    * `is_final`: indicates whether the results obtained within this list entry are interim or final.
    * `result_end_time`: indicates the time offset of the end of this result relative to the beginning of the audio.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
