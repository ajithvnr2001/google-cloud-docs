---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024/
title: Speech model migration for phone_call in Q2 2024 \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:33.578467+00:00
---

# Speech model migration for phone_call in Q2 2024  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Speech model migration for phone_call in Q2 2024 Stay organized with collections  Save and categorize content based on your preferences. 

## Migration status

As of July 2024, the automatic migration has been completed for the following combination of settings that correspond to the second row in the migration table:

Current [`model`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.InputAudioConfig.FIELDS.string.google.cloud.dialogflow.cx.v3.InputAudioConfig.model) identifier | Current [`model_variant`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#speechmodelvariant) | Current [`single_utterance`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.single_utterance) setting * | Model identifier that traffic is directed to  
---|---|---|---  
`phone_call` | Other than `USE_STANDARD` | `false` | `telephony`  
Symbol | Description  
---|---  
* | If your Dialogflow CX agent has [enabled advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity), then the model identifier is routed assuming `single_utterance` is `false`, even if the setting is set to `true` at runtime.  
  
For other combination of settings, the automatic migration will remain on hold until further notice (no ETA).

You can continue to use the `phone_call` model identifier but are encouraged to opt in to use conformer-based speech models.

## Migration overview

For certain [language tag](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) and speech setting combinations, the Dialogflow CX and Dialogflow ES traffic with audio will gradually route away from the classic Speech-to-Text model behind the `phone_call` model identifier to the new conformer-based [speech models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model). As the redirection will be internal only, the current model identifiers and code will remain valid and continue to serve traffic.

The affected language tags are: `en-au`, `en-gb`, `de`, `de-de`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `it-it`, `ja`, `pt-br`.

The following table shows the routing of Speech-to-Text `phone_call` model that will take place when the migration takes effect. If your configuration matches the language tag and the first three columns in the table, the new model identifier is listed in the fourth column.

Current [`model`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.InputAudioConfig.FIELDS.string.google.cloud.dialogflow.cx.v3.InputAudioConfig.model) identifier | Current [`model_variant`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#speechmodelvariant) | Current [`single_utterance`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.single_utterance) setting * | Model identifier that traffic will be directed to  
---|---|---|---  
`phone_call` | `USE_STANDARD` | `false` | `latest_long`  
`phone_call` | Other than `USE_STANDARD` | `false` | `telephony`  
`phone_call` | any | `true` | `latest_short`  
Symbol | Description  
---|---  
* | If your Dialogflow CX agent has [enabled advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity), then the model identifier is routed assuming `single_utterance` is `false`, even if the setting is set to `true` at runtime.  
  
## Migration options

There are three migration options: early opt-in, automatic, and temporary opt-out.

### Opt in and migrate earlier

To opt in proactively, change the speech model identifier that you have been using in the [Dialogflow CX API](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#inputaudioconfig) and [Dialogflow ES API](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#inputaudioconfig) with the updated one. For Dialogflow CX, you can also change the [model identifier](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) in the **Advanced speech settings** under **Speech and IVR settings** in the Dialogflow CX console.

Speech model specified in the API at runtime takes precedence over the speech model specified in the Dialogflow CX console, unless you enable the [**Override request-level speech model**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) setting. Read more about precedence in [speech models](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models).

For partner telephony integrations, check with your telephony provider if the speech model is being set in the API. If you are using the Dialogflow CX Phone Gateway, review the speech model [limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#limits).

Migrating your project proactively gives you time to test the models and take advantage of the improved accuracy and robustness earlier. Most integrations require `single_utterance = true`, so if you are not using [advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity) you'll likely want to use `latest_short`.

If you experience issues with the new models, [open a Google Cloud support case](https://docs.cloud.google.com/support/docs/customer-care-procedures) with issue details.

### Migrate automatically

**Note:** See migration status.

To be migrated automatically, no action is required on your part. The existing Speech-to-Text model identifiers are valid and we will shift traffic internally.

### Opt out and migrate later

Due to the suspended migration status, new opt-out requests are not accepted. If your projects were opted out before July 2024, they will remain in this state until further announcement.

[ Previous arrow_back  Speech model migration Q1 2024  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration)

[ Next Search  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
