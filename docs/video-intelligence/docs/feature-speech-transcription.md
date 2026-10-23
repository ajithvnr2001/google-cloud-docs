---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-speech-transcription/
title: Speech transcription \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:46.414081+00:00
---

# Speech transcription  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-speech-transcription/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Speech transcription Stay organized with collections  Save and categorize content based on your preferences. 

_Speech Transcription_ transcribes spoken audio in a video or video segment into text and returns blocks of text for each portion of the transcribed audio.

**Caution:** VPC Service Controls egress restrictions are not enforced on the `outputUri` of `videos:annotate` requests. The service can write transcription results to a Cloud Storage bucket outside of your service perimeter. For details, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#videointelligence).

## Supported models

The Video Intelligence only supports English (US). For other languages, use the Speech-to-Text API, which supports all available languages. For the list of available languages, see [Language support](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) in the Speech-to-Text documentation.

To transcribe speech from a video, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specify [`SPEECH_TRANSCRIPTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) in the `features` field.

You can use the following features when transcribing speech:

  * **Alternative words** : Use the `maxAlternatives` option to specify the maximum number of options for recognized text translations to include in the response. This value can be an integer from 1 to 30. The default is 1. The API returns multiple transcriptions in descending order based on the confidence value for the transcription. Alternative transcriptions do not include word-level entries.

  * **Profanity filtering** : Use the `filterProfanity` option to filter out known profanities in transcriptions. Matched words are replaced with the leading character of the word followed by asterisks. The default is false.

  * **Transcription hints** : Use the `speechContexts` option to provide common or unusual phrases in your audio. Those phrases are then used to assist the transcription service to create more accurate transcriptions. You provide a transcription hint as a [SpeechContext](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#SpeechContext) object.

  * **Audio track selection** : Use the `audioTracks` option to specify which track to transcribe from multi-track video. Users can specify up to two tracks. Default is 0. Once the language code is set to en-US, the request is routed to the enhanced mode, which is trained on en-US audio; it does not really _know_ en-US or any other languages per se. If we feed a Spanish audio into the enhanced model, transcription will run its course but there may be outputs with low confidence scores, or no output at all – which is what is expected of a good model.

  * **Automatic punctuation** : Use the `enableAutomaticPunctuation` option to include punctuation in the transcribed text. The default is false.

  * **Multiple speakers** : Use the `enableSpeakerDiarization` option to identify different speakers in a video. In the response, each recognized word includes a `speakerTag` field that identifies which speaker the recognized word is attributed to.




For best results, provide audio recorded at 16,000Hz or greater sampling rate.

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Speech%20Transcription) to see this feature in action.

For examples of requesting speech transcription, see [Speech Transcription](https://docs.cloud.google.com/video-intelligence/docs/transcription).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
