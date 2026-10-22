---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration/
title: Speech model migration in Q1 2024 \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:06.544130+00:00
---

# Speech model migration in Q1 2024  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Speech model migration in Q1 2024 Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This migration may affect you only if the client or integration you use sends audio requests to Dialogflow with the following language tags: `en`, `en-us`, `en-au`, `en-gb`, `en-in`, `de`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `ja`, `nl`, `pt-br`.

## Migration status

As of July 2024, no projects have been automatically migrated. The automatic migration will remain on hold until further notice (no ETA).

You can continue to use the classic Speech-to-Text models but are encouraged to opt in to use conformer-based speech models.

## Migration overview

For certain [language tag](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) and speech setting combinations, the Dialogflow CX and Dialogflow ES traffic with audio will gradually route away from the classic Speech-to-Text models behind the `command_and_search`, `default`, `phone_call`, and `video` model identifiers to the new conformer-based [speech models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model). As the redirection will be internal only, the current model identifiers and code will remain valid and continue to serve traffic.

The tables in the Migration for `en` and `en-us`language tags and Migration for `de`, `en-au`, `en-gb`, `en-in`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `ja`, `nl`, `pt-br` language tags sections show the routing of Speech-to-Text models that will take place when the migration takes effect. If your configuration matches the language tag and the first two columns in the table, the new model identifier is listed in the third column. No change is expected for other configurations.

See the Migration options section to choose the best option for you.

## Migration for `en` and `en-us` language tags

Current [`model`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.InputAudioConfig.FIELDS.string.google.cloud.dialogflow.cx.v3.InputAudioConfig.model) identifier | Current [`single_utterance`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.single_utterance) setting * | Model identifier that traffic will be directed to  
---|---|---  
`command_and_search` | `false` | `latest_long`  
`command_and_search` | `true` | `latest_short`  
`default` | `false` | `telephony`  
`phone_call` | `false` | `telephony`  
`phone_call` ([`model_variant`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.model_variant) is not `USE_STANDARD`) | `true` | `telephony_short`  
`video` | `false` | `telephony`  
Unspecified | `true/false` | Model is auto-selected from among the above, based on the parameters in [`InputAudioConfig`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#inputaudioconfig)  
Symbol | Description  
---|---  
* | If your Dialogflow CX agent has [enabled advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity), then the model identifier is routed assuming `single_utterance` is `false`, even if the setting is set to `true` at runtime.  
  
## Migration for `de`, `en-au`, `en-gb`, `en-in`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `ja`, `nl`, `pt-br` language tags

Current [`model`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.InputAudioConfig.FIELDS.string.google.cloud.dialogflow.cx.v3.InputAudioConfig.model) identifier | Current [`single_utterance`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.single_utterance) setting * | Model identifier that traffic will be directed to  
---|---|---  
`command_and_search` | `false` | `latest_long`  
`command_and_search` | `true` | `latest_short`  
`default` | `false` | `latest_long`  
Unspecified | `true/false` | Model is auto-selected from among the above, based on the parameters in [`InputAudioConfig`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#inputaudioconfig)  
Symbol | Description  
---|---  
* | If your Dialogflow CX agent has [enabled advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity), then the model identifier is routed assuming `single_utterance` is `false`, even if the setting is set to `true` at runtime.  
  
## Migration options

There are three migration options: early opt-in, automatic, and temporary opt-out.

### Opt in and migrate earlier

To opt in proactively, change the speech model identifier that you have been using in the [Dialogflow CX API](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#inputaudioconfig) and [Dialogflow ES API](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#inputaudioconfig) with the updated one. For Dialogflow CX, you can also change the [model identifier](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) in the **Advanced speech settings** under **Speech and IVR settings** in the Dialogflow CX console.

Speech model specified in the API at runtime takes precedence over the speech model specified in the Dialogflow CX console, unless you enable the [**Override request-level speech model**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) setting. Read more about precedence in [speech models](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models).

For partner telephony integrations, check with your telephony provider if the speech model is being set in the API. If you are using the Dialogflow CX Phone Gateway, review the speech model [limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#limits).

Migrating your project proactively gives you time to test the models and take advantage of the improved accuracy and robustness earlier. This approach is highly recommended, especially if you are using a model that will migrate to the new `telephony` and `telephony_short` models. Most integrations require `single_utterance = true`, so if you are not using [advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity) you'll likely want to use `telephony_short` or `latest_short`.

If you experience issues with the new models, [open a Google Cloud support case](https://docs.cloud.google.com/support/docs/customer-care-procedures) with issue details.

### Migrate automatically

**Note:** See migration status.

To be migrated automatically, no action is required on your part. The existing Speech-to-Text model identifiers are valid and we will shift traffic internally.

### Opt out and migrate later

Due to the suspended migration status, new opt-out requests are not accepted. If your projects were opted out before July 2024, they will remain in this state until further announcement.

[ Previous arrow_back  Advanced speech settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech)

[ Next Speech model migration for phone_call Q2 2024  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
