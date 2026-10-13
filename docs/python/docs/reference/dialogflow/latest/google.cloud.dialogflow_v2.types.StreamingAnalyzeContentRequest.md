---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingAnalyzeContentRequest
title: Class StreamingAnalyzeContentRequest (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:57.902817+00:00
---

# Class StreamingAnalyzeContentRequest (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingAnalyzeContentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingAnalyzeContentRequest (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    StreamingAnalyzeContentRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The top-level message sent by the client to the Participants.StreamingAnalyzeContent method.

Multiple request messages should be sent in order:

  1. The first message must contain participant, config and optionally query_params. If you want to receive an audio response, it should also contain reply_audio_config. The message must not contain input.

  2. If config in the first message was set to audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. However, note that:

     * Dialogflow will bill you for the audio so far.
     * Dialogflow discards all Speech recognition results in favor of the text input.
  3. If StreamingAnalyzeContentRequest.config in the first message was set to StreamingAnalyzeContentRequest.text_config, then the second message must contain only input_text. Moreover, you must not send more than two messages.




After you sent all input, you must half-close or abort the request stream.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`participant` |  `str`   
Required. The name of the participant this text comes from. Format: `projects/`.   
`audio_config` |  `[google.cloud.dialogflow_v2.types.InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputAudioConfig)`   
Instructs the speech recognizer how to process the speech audio. This field is a member of `oneof`_ `config`.   
`text_config` |  `[google.cloud.dialogflow_v2.types.InputTextConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputTextConfig)`   
The natural language text to be processed. This field is a member of `oneof`_ `config`.   
`reply_audio_config` |  `[google.cloud.dialogflow_v2.types.OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OutputAudioConfig)`   
Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling StreamingAnalyzeContent. If this configuration is not supplied, speech synthesis is disabled.   
`input_audio` |  `bytes`   
The input audio content to be recognized. Must be sent if `audio_config` is set in the first message. The complete audio over all streaming messages must not exceed 1 minute. This field is a member of `oneof`_ `input`.   
`input_text` |  `str`   
The UTF-8 encoded natural language text to be processed. Must be sent if `text_config` is set in the first message. Text length must not exceed 256 bytes for virtual agent interactions. The `input_text` field can be only sent once, and would cancel the speech recognition if any ongoing. This field is a member of `oneof`_ `input`.   
`input_dtmf` |  `[google.cloud.dialogflow_v2.types.TelephonyDtmfEvents](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TelephonyDtmfEvents)`   
The DTMF digits used to invoke intent and fill in parameter value. This input is ignored if the previous response indicated that DTMF input is not accepted. This field is a member of `oneof`_ `input`.   
`suggestion_input` |  `[google.cloud.dialogflow_v2.types.SuggestionInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionInput)`   
Optional. Input for confirming, revising, or canceling a suggestion. This field is a member of `oneof`_ `input`.   
`query_params` |  `[google.cloud.dialogflow_v2.types.QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryParameters)`   
Parameters for a Dialogflow virtual-agent query.   
`assist_query_params` |  `[google.cloud.dialogflow_v2.types.AssistQueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AssistQueryParameters)`   
Parameters for a human assist query.   
`cx_parameters` |  `google.protobuf.struct_pb2.Struct`   
Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null. Note: this field should only be used if you are connecting to a Dialogflow CX agent.   
`enable_extended_streaming` |  `bool`   
Optional. Enable full bidirectional streaming. You can keep streaming the audio until timeout, and there's no need to half close the stream to get the response. Restrictions: \- Timeout: 3 mins. \- Audio Encoding: only supports AudioEncoding.AUDIO_ENCODING_LINEAR_16 and AudioEncoding.AUDIO_ENCODING_MULAW \- Lifecycle: conversation should be in `Assist Stage`, go to Conversations.CreateConversation for more information. InvalidArgument Error will be returned if the one of restriction checks failed. You can find more details in https://cloud.google.com/agent-assist/docs/extended-streaming   
`enable_partial_automated_agent_reply` |  `bool`   
Optional. Enable partial responses from Dialogflow CX agent. If this flag is not enabled, response stream still contains only one final response even if some `Fulfillment`\ s in Dialogflow CX agent have been configured to return partial responses.   
`output_multiple_utterances` |  `bool`   
Optional. If multiple uttereances are detected in the audio stream, process them individually instead of stitching them together to form a single utterance.   
`enable_debugging_info` |  `bool`   
If true, `StreamingAnalyzeContentResponse.debugging_info` will get populated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
