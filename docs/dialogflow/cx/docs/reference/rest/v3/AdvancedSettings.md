---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings/
title: AdvancedSettings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:28.055498+00:00
---

# AdvancedSettings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  AdvancedSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GcsDestination
    * JSON representation
  * SpeechSettings
    * JSON representation
  * DtmfSettings
    * JSON representation
  * LoggingSettings
    * JSON representation



Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playbackInterruptionSettings at fulfillment level only overrides the playbackInterruptionSettings at the agent level, leaving other settings at the agent level unchanged.

DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel.

Hierarchy: Agent->Flow->Page->Fulfillment/Parameter.

JSON representation  
---  
      
    
    {
      "audioExportGcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#GcsDestination))
      },
      "speechSettings": {
        object ([SpeechSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#SpeechSettings))
      },
      "dtmfSettings": {
        object ([DtmfSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#DtmfSettings))
      },
      "loggingSettings": {
        object ([LoggingSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#LoggingSettings))
      }
    }  
  
Fields  
---  
`audioExportGcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#GcsDestination)`)` If present, incoming audio is exported by Dialogflow to the configured Google Cloud Storage destination. Exposed at the following levels: - Agent level - Flow level  
`speechSettings` |  `object (`[SpeechSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#SpeechSettings)`)` Settings for speech to text detection. Exposed at the following levels: - Agent level - Flow level - Page level - Parameter level  
`dtmfSettings` |  `object (`[DtmfSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#DtmfSettings)`)` Settings for DTMF. Exposed at the following levels: - Agent level - Flow level - Page level - Parameter level.  
`loggingSettings` |  `object (`[LoggingSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#LoggingSettings)`)` Settings for logging. Settings for Dialogflow History, Contact Center messages, StackDriver logs, and speech logging. Exposed at the following levels: - Agent level.  
  
## GcsDestination

Google Cloud Storage location for a Dialogflow operation that writes or exports objects (e.g. exported agent or transcripts) outside of Dialogflow.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The Google Cloud Storage URI for the exported objects. A URI is of the form: `gs://bucket/object-name-or-prefix` Whether a full object name, or just a prefix, its usage depends on the Dialogflow operation.  
  
## SpeechSettings

Define behaviors of speech to text detection.

JSON representation  
---  
      
    
    {
      "endpointerSensitivity": integer,
      "noSpeechTimeout": string,
      "useTimeoutBasedEndpointing": boolean,
      "models": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`endpointerSensitivity` |  `integer` Sensitivity of the speech model that detects the end of speech. Scale from 0 to 100.  
`noSpeechTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Timeout before detecting no speech.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`useTimeoutBasedEndpointing` |  `boolean` Use timeout based endpointing, interpreting endpointer sensitivity as seconds of timeout value.  
`models` |  `map (key: string, value: string)` Mapping from language to Speech-to-Text model. The mapped Speech-to-Text model will be selected for requests from its corresponding language. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## DtmfSettings

Define behaviors for DTMF (dual tone multi frequency).

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "maxDigits": integer,
      "finishDigit": string,
      "interdigitTimeoutDuration": string,
      "endpointingTimeoutDuration": string
    }  
  
Fields  
---  
`enabled` |  `boolean` If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance).  
`maxDigits` |  `integer` Max length of DTMF digits.  
`finishDigit` |  `string` The digit that terminates a DTMF digit sequence.  
`interdigitTimeoutDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Interdigit timeout setting for matching dtmf input to regex.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`endpointingTimeoutDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Endpoint timeout setting for matching dtmf input to regex.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## LoggingSettings

Define behaviors on logging.

JSON representation  
---  
      
    
    {
      "enableStackdriverLogging": boolean,
      "enableInteractionLogging": boolean,
      "enableConsentBasedRedaction": boolean
    }  
  
Fields  
---  
`enableStackdriverLogging` |  `boolean` Enables Google Cloud Logging.  
`enableInteractionLogging` |  `boolean` Enables DF Interaction logging.  
`enableConsentBasedRedaction` |  `boolean` Enables consent-based end-user input redaction, if true, a pre-defined session parameter `$session.params.conversation-redaction` will be used to determine if the utterance should be redacted.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
