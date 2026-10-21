---
url: https://docs.cloud.google.com/speech-to-text/docs/voice-activity-events/
title: Voice activity events and timeouts \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:43.992167+00:00
---

# Voice activity events and timeouts  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/voice-activity-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Voice activity events and timeouts Stay organized with collections  Save and categorize content based on your preferences. 

Voice activity events indicate when speech start or end has been detected throughout a stream. The events are sent in real-time as they are detected by Cloud Speech-to-Text. Voice activity events can be useful for developing applications that rely on automatic detection of when a user has started or finished speaking. Cloud STT can also be configured to automatically close the stream based on voice activity.

Voice activity events are only available for [StreamingRecognize](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#streamingrecognizerequest) gRPC requests.

## Enable voice activity events

You can enable receiving voice activity responses by setting the `enable_voice_activity_events` flag to true under the `streaming_features` [message](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#streamingfeatures).

### Voice activity event types

Voice activity events are usually returned in real time as Cloud STT detects speech start or stop during the stream. They will usually be returned before the transcription results for the corresponding segment of speech. Speech activity events can be sent for audio that produces empty transcription results.

#### Speech Activity Begin

Sent when Cloud STT detects that speech has started. 
    
    
    {
      "speechEventType": "SPEECH_ACTIVITY_BEGIN",
      "speechEventOffset": "1.070s"
    }
    

#### Speech Activity End

Sent when Cloud STT detects that speech has ended.
    
    
    {
      "speechEventType": "SPEECH_ACTIVITY_END",
      "speechEventOffset": "1.070s"
    }
    

If the stream is closed before speech ends, a `SPEECH_ACTIVITY_END` event won't be sent.

## Enable voice activity timeouts

You can enable voice activity timeouts by setting values on the `voice_activity_timeout` [message](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#streamingfeatures) in `streaming_features`. Voice activity timeouts must be greater than 500ms and less than 60s. Speech begin and end timeouts can be set independently.

### Speech begin timeout

When a speech begin timeout is set, Cloud STT will automatically close the stream if speech has not started before the timeout period. Once a `SPEECH_ACTIVITY_START` event has been detected and returned, the timeout is canceled for the duration of the stream. This feature is useful for applications that expect a user to begin speaking within a given period of time.

### Speech end timeout

When a speech end timeout is set, Cloud STT will automatically close the stream if no further speech is detected within the timeout duration after a `SPEECH_ACTIVITY_END` event. Once a `SPEECH_ACTIVITY_START` event has been detected and returned, the timeout is canceled and will start again once a `SPEECH_ACTIVITY_END` event is sent.

### Time measurement for timeouts

Time elapsed is measured by the bytes of audio sent in requests to Cloud STT, as opposed to server time. This allows for preserving accuracy during variations in stream transmission. Sending very large audio chunks in requests, or sending requests in very rapid succession will reduce accuracy in timeout measurement. Note: the size limit for audio chunks is 15360 bytes per request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
