---
url: https://docs.cloud.google.com/speech-to-text/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:13.138275+00:00
---

# Troubleshooting  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems using Cloud Speech-to-Text.

## Cannot authenticate to Cloud STT

You might receive an error message indicating that your application default credentials are unavailable. Or, you might wonder how to get an API key to use when calling Cloud STT.

Cloud STT uses [_Application Default Credentials_](https://docs.cloud.google.com/accounts/docs/application-default-credentials) (ADC) for authentication. 

The credentials for ADC must be available within the context that you call the Cloud Speech-to-Text API. For example, if you set up ADC in your terminal but run your code in the debugger of your IDE, the execution context of your code might not have access to the credentials. In that case, your request to Cloud STT might fail. 

To learn how to provide credentials to ADC, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc). 

## Cloud STT returns an empty response

There are multiple reasons why Cloud STT might return an empty response. The source of the problem can be the `RecognitionConfig` or the audio itself.

**Note:** Cloud STT provides a [Speech UI](http://console.cloud.google.com/speech) that you can use to experiment with different configurations and find the optimal `RecognitionConfig` for your needs.

### Troubleshoot `RecognitionConfig`

`RecognitionConfig` object (or `StreamingRecognitionConfig`) is part of a Cloud STT recognition request. To correctly perform a transcription, set the fields that fall into the following main categories:

  * Audio configuration
  * Model and language



A common cause of empty responses (such as an empty `{}` JSON response) is providing incorrect information about the audio metadata. If the audio configuration fields are not set correctly, transcription will most likely fail, and the recognition model will return empty results.

Audio configuration contains the metadata of the provided audio. You can obtain the metadata for your audio file using the `ffprobe` command, which is part of [FFMPEG](https://ffmpeg.org).

The following example demonstrates using the command to get the metadata for this [speech sample](https://storage.googleapis.com/cloud-samples-tests/speech/commercial_mono.wav).
    
    
    $ ffprobe commercial_mono.wav
    [...]
    Input #0, wav, from 'commercial_mono.wav':
      Duration: 00:00:35.75, bitrate: 128 kb/s
      Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 8000 Hz, 1 channels, s16, 128 kb/s
    

The file clearly has 8,000 Hz, one channel, and LINEAR16 encoding (s16), and you can use this information in your `RecognitionConfig`.

#### Encoding-related troubleshooting

Take the following steps for resolving other possible reasons for an empty response:

  1. Play the file and listen to the output. Is the audio clear and the speech intelligible?

To play files, you can use the [SoX (Sound eXchange)](https://sourceforge.net/projects/sox/) `play` command. A few examples based on different audio encodings follow.

FLAC files include a header that indicates the sample rate, encoding type and number of channels, and can be played as follows:
         
         play audio.flac

LINEAR16 files don't include a header. To play them, specify the sample rate, encoding type, and number of channels. The LINEAR16 encoding must be 16-bits, signed-integer, and little-endian.
         
         play --channels=1 --bits=16 --rate=16000 --encoding=signed-integer \
         --endian=little audio.raw

MULAW files also don't include a header and often use a lower sample rate.
         
         play --channels=1 --rate=8000 --encoding=u-law audio.raw

  2. Check that the audio encoding of your data matches the parameters you sent in `RecognitionConfig`. For example, if your request specified `"encoding":"FLAC"` and `"sampleRateHertz":16000`, the audio data parameters listed by the [SoX](https://sourceforge.net/projects/sox/) `play` command should match these parameters, as follows:
         
         play audio.flac

Should list:
         
         Encoding: FLAC
         Channels: 1 @ 16-bit
         Sampleratehertz: 16000 Hz

If the SoX listing shows a `Sampleratehertz` other than `16000Hz`, change the `"sampleRateHertz"` in `InitialRecognizeRequest` to match. If the `Encoding` is not `FLAC` or `Channels` is not `1 @ 16-bit`, you cannot use this file directly, and will need to convert it to a compatible encoding (see next step).

  3. If your audio file is not in FLAC encoding, try converting it to FLAC using SoX. Repeat the steps to play the file and verify the encoding, sampleRateHertz, and channels. Examples that convert various audio file-formats to FLAC encoding:
         
         sox audio.wav --channels=1 --bits=16 audio.flac
         sox audio.ogg --channels=1 --bits=16 audio.flac
         sox audio.au --channels=1 --bits=16 audio.flac
         sox audio.aiff --channels=1 --bits=16 audio.flac

To convert a raw file to FLAC, you need to know the audio-encoding of the file. For example, to convert stereo, 16-bit, signed, little-endian at 16,000 Hz to FLAC, follow this example:
         
         sox --channels=2 --bits=16 --rate=16000 --encoding=signed-integer \
         --endian=little audio.raw --channels=1 --bits=16 audio.flac

  4. Run the [Quickstart](https://docs.cloud.google.com/speech-to-text/docs/quickstart) example or one of the [Sample Applications](https://docs.cloud.google.com/speech-to-text/docs/samples) with the supplied sample audio file. When the example is running successfully, replace the sample audio file with your audio file.




### Model and language configuration

Model selection is very important to obtaining high-quality transcription results. [Cloud STT](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests#select-model) provides multiple models that have been tuned to different use cases and must be chosen to most closely match your audio. For example, some models (such as `latest_short` and `command_and_search` are short-form models, which means that are more suited to short audios and prompts. These models are likely to return results as soon as they detect a period of silence. Long-form models, on the other hand (such as `latest_short, phone_call, video and default` are more suited for longer audios and are not as sensitive to interpreting silence as the end of the audio.

If your recognition ends too abruptly or doesn't return quickly, see if you can get better transcription quality by experimenting with other models using the [Speech UI](http://console.cloud.google.com/speech).

## Timeout errors

These issues are, for the most part, caused by misconfiguration or misuse of Cloud Speech-to-Text.

### `LongRunningRecognize` or `BatchRecognize`

  * **Issue:** You're receiving `TimeoutError: Operation did not complete within the designated timeout`.

  * **Solution:** You can send a transcription to the Cloud Storage bucket or extend the timeout in the request.




This issue occurs when the [`LongRunningRecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize) or [`BatchRecognize`](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rest/v2/projects.locations.recognizers/batchRecognize) request doesn't complete in the specified timeout, and it's _not an error that indicates failure in speech transcription_. It means that the transcription results aren't ready to be extracted.

### `StreamingRecognize`

  * **Issue:** You're receiving `Timeout Error: Long duration elapsed without audio. Audio should be sent close to real time`.

  * **Solution:** Time between audio chunks sent needs to decrease. If Cloud Speech-to-Text doesn't get a new chunk every few seconds, it'll close the connection and trigger this error.




### `StreamingRecognize` 409 aborted

  * **Issue:** You're receiving the `409 Max duration of 5 minutes reached for stream` error.

  * **Solution:** You're reaching the streaming recognition limit of [five minutes of audio](https://docs.cloud.google.com/speech-to-text/quotas#content). When you're getting close to this limit, close the stream and open a new one.




## Low transcript quality

Automatic Speech Recognition (ASR) supports a wide variety of use cases. Most quality issues can be addressed by trying different API options. To improve recognition accuracy, follow the guidelines in [Best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices-provide-speech-data).

### Short utterances aren't recognized

  * **Issue** : End user short utterances like **Yes** , **No** , and **Next** don't get captured by the API and are missing in the transcript.

  * **Solution** : Take the following steps.

    1. Test the same request with different [models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model).

    2. Add speech adaptation and [boost](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#fine-tune_transcription_results_using_boost) missing words.

    3. If you're using [streaming input](https://docs.cloud.google.com/speech-to-text/docs/transcribe-streaming-audio), try setting [`single_utterance=true`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#streamingrecognitionconfig).




### Consistently unrecognized word or phrase

  * **Issue** : Certain words or phrases are consistently misrecognized, like **a** is recognized as **8**.

  * **Solution** : Take the following steps.

    1. Test the same request with different [models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model).

    2. Add speech adaptation and [boost](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#fine-tune_transcription_results_using_boost) missing words. You can use [class tokens](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#classes) to boost whole sets of words like digit sequences or addresses. Check available [class tokens](https://docs.cloud.google.com/speech-to-text/docs/class-tokens).

    3. Try increasing [`max_alternatives`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#recognitionconfig). Then check [SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#speechrecognitionresult) `alternatives` and choose the first one that matches the format you want.




Formatting can be challenging for ASR. Speech adaptation can often help get a required format, but post-processing might be necessary to fit required format.

### Mixed or multi-language inputs

  * **Issue** : Audio contains speech in multiple languages, like a conversation between an English and a Spanish speaker resulting in the wrong transcription.

  * **Solution** : This feature isn't supported. Speech-to-Text can transcribe only one language per request.




### Artifacts during silence or music with Chirp models

  * **Issue** : When passing audio with silence or music parts, transcription contains random numbers or hallucinated words.

  * **Solution** : Enable [Denoiser and SNR-filtering](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-2#denoiser_and_snr-filtering_details), and try different combinations of SNR threshold.




## Permission denied

  * **Issue:** You're receiving the following error.
        
        Permission denied to access GCS object BUCKET-PATH.
        Source error: PROJECT-ID@gcp-sa-speech.iam.gserviceaccount.com does not have
        storage.buckets.get access to the Google Cloud Storage bucket.
        Permission 'storage.buckets.get' denied on resource (or it may not exist).

  * **Solution:** Provide permission for PROJECT_ID@gcp-sa-speech.iam.gserviceaccount.com to access file in BUCKET-PATH bucket.




## Invalid argument

  * **Issue:** You're receiving the following error.
        
        {
          "error": {
            "code": 400,
            "message": "Request contains an invalid argument.",
            "status": "INVALID_ARGUMENT"
          }
        }

  * **Solution:** Check arguments and compare them to API documentation, then validate that they're correct. Make sure the selected endpoint matches the location in the request / resource.




## Resource exhausted

  * **Issue:** You're receiving the following error.
        
        RESOURCE_EXHAUSTED: Resource has been exhausted (e.g. check quota)

  * **Solution:** See [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).




## Streaming chunk too large

  * **Issue:** You're receiving the following error.
        
        INVALID_ARGUMENT: Request audio can be a maximum of 10485760 bytes.
        [type.googleapis.com/util.MessageSetPayload='[google.rpc.error_details_ext]
        { message: "Request audio can be a maximum of 10485760 bytes." }']

  * **Solution:** You need to decrease size of audio chunks sent in. We recommend sending chunks of 100 ms for best latency and to avoid reaching the [audio limit](https://docs.cloud.google.com/speech-to-text/quotas#content).




## Data logging

  * **Issue:** Speech-to-Text doesn't provide any Cloud Logging.

  * **Solution:** Because Speech-to-Text has data logging disabled by default, customers need to [enable it](https://docs.cloud.google.com/speech-to-text/docs/enable-data-logging) on the project level.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
