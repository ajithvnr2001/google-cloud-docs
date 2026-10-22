---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings/
title: Agent settings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:21.716402+00:00
---

# Agent settings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Agent settings Stay organized with collections  Save and categorize content based on your preferences. 

Agents have many settings that influence behavior, and each console provides different settings.

## Conversational Agents console agent settings

To access agent settings:

###  Console 

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com).
  2. Choose your project.
  3. Select your agent.
  4. Click these settings icon in the top right corner.
  5. Update the settings as needed.
  6. Click **Save**.



###  API 

See the `get` and `patch/update` methods for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

The following subsections describe the different categories of agent settings.

### General settings

The following general settings are available for agents:

  * **Display name** link

A human-readable name for your agent.

  * **Time zone** link

The default time zone for your agent.

  * **Conversation start** link

This setting determines whether your agent starts the conversation with a generative playbook or a deterministic flow.

  * **Agent location** link

The agent region you selected when creating the agent.

  * **Agent lock** link

    * **Lock the agent:** Indicates if the agent is locked. A locked agent cannot be edited.
  * **Logging settings** link

    * **Enable cloud logging:** Indicates if [Cloud logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging) is enabled for the agent.

    * **Enable conversation history:** Indicates if you want Google to collect and store [redacted](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings) end-user queries for quality improvement.

**Note:** Some features, such as [Experiments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments), [Conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history), [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq), [Analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics), and NLU model improvement require this setting to be enabled, as they rely on traffic logs.
    * **Specify a Cloud Storage URI to store and playback voice conversations:** When conversation history is enabled, you can provide a Cloud Storage URI, and conversation audio will be saved in this location. This field is synchronized with [advanced speech settings for audio export bucket](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech#audio-export-bucket). You can optionally use the **Browse Google cloud storage** button, which will open a bucket selection panel.

    * **Enable consent-based end-user input redaction:** If this setting is enabled, it lets you use a special session parameter to control if end-user input and parameters are redacted from [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) and [Cloud logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging). By default, the session parameter is `true`. If this setting is disabled, no redaction occurs.

User consent is collected using a boolean session parameter: `$session.params.conversation-redaction`. If this setting is enabled, and the session parameter is set to `false`, no redaction occurs **(other redaction strategies still apply)**. If this setting is enabled, and the session parameter is set to `true`, redaction occurs.

An example consent requesting flow could be: first ask the user if they want to keep end-user input, and match the response with two intents, one is "yes intent" and the other is "no intent." Then, set the session parameter to `false` (no redaction) in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the "yes intent" route in [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment), and to `true` (redaction occurs) in the [parameter preset](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the "no intent" route.

  * **BigQuery export** link

    * **Enable BigQuery export:** Indicates if [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq) is enabled.
    * **BigQuery dataset:** The BigQuery dataset name.
    * **BigQuery table:** The BigQuery table name.
  * **Intent suggestions** link

You can enable [intent suggestions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#suggestions).

  * **User feedback** link

You can enable this setting to provide feedback about the quality of the agent's answers, which includes thumbs up/down.

  * **Git integration** link

Use this setting to add a [Git integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github).




### Generative AI settings

The following generative AI settings are available:

  * **General:**

    * **Generative model selection** link

Select the model to be used by generative features. For more information, see [model versions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning).

  * **Token limits:**

    * **Input token limit** link

Select the input token limit for the [generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models). This is the maximum token size for input to be sent to the model. Depending on the model, a [token](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count) can be somewhere between one character and one word. Smaller token limits have lower latency, but the model input size is limited. Larger token limits have higher latency, but the model input size can be larger.

    * **Output token limit** link

Select the output token limit for the [generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models). This is the maximum token size for output received from the model. Depending on the model, a [token](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count) can be somewhere between one character and one word. Smaller token limits have lower latency, but the model output size is limited. Larger token limits have higher latency, but the model output size can be larger.

    * **Temperature** link

The temperature for a LLM lets you control how creative the responses are. A low value provides more predictable responses. A high value provides more creative or random responses.

    * **Context token limits** link

**Note:** This feature is restricted access.

The setting culls some past turns from the LLM prompt to keep the prompt size from growing with every sequential turn handled by the agent. This feature offers a way to mitigate unwanted prompt size growth.

Normally, without truncation, each subsequent turn will be appended into the "conversation history" of the LLM prompt regardless of whether it's relevant to the current turn. This can ultimately lead to the prompt increasing in size with every turn. As more of the prompt is taken up by conversation history, less of the prompt can be used for few-shot examples (so these might get dropped). Eventually, the prompt might also breach current token limits. You can increase token sizes to accommodate this, but keep in mind that increased prompt sizes also add to the LLM response latency.

Context truncation lets you set a percentage of the token budget to be reserved for conversation history, as a maximum. Conversation turns are preserved in most recent to least recent order. This setting can help you prevent token limits from being exceeded. Regardless of which setting yo choose, a minimum of two conversation turns are preserved, in most recent to least recent order.

You must first set a token limit before you can modify this setting.

Truncating context might cause some parameters to be inadvertently lost if they are part of culled turns. Evaluate your playbook interactions carefully after enabling this option.

Token input budget is also used by the following:

      * System instructions and examples: Automatically added to the prompt. This behavior cannot be modified.
      * Playbook instructions and goals: Any instructions and goals that you write will be added to the prompt in their entirety.
      * Playbook few-shot examples: Are added either in order (by default) or by an algorithm that you choose (such as regular expression best match ordering). Examples are culled to fit within input token budget after all other items are included.
      * Conversation history made up of user and agent utterances, flow and playbook transition context, tool calls and outputs in the same session from all previous turns sequentially handled by the current playbook.
    * **Banned phrases** link

A list of phrases that are banned for generative AI. If a banned phrase appears in the prompt or the generated response, the generation will fail. Be aware that the list of banned phrases has consequences on every query and LLM call and will increase latency.

    * **Safety filters** link

Configure sensitivity levels of safety filters with respect to different Responsible AI (RAI) categories. Content will be assessed against the following four categories:

Category | Description  
---|---  
Hate speech | Negative or harmful comments targeting identity and/or protected attributes.  
Dangerous content | Promotes or enables access to harmful goods, services, and/or activities  
Sexually explicit content | Contains references to sexual acts and/or other lewd content  
Harassment | Malicious, intimidating, bullying, and/or abusive comments targeting another individual  
  
Content is blocked based on the probability that it's harmful. The sensitivity level can be customized by choosing one of **Block none** , **Block few** , **Block some** , and **Block most** for each category.

For more information, see [configure safety attributes](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes).

    * **Prompt security** link

You can check the **enable prompt security check** setting to enable prompt security checks. If enabled, the agent will reject user queries that trigger the security filter, including prompt injection attacks. These attacks may be used to reveal parts of the agent prompt or to provide responses the agent is not supposed to supply. This is accomplished by sending an additional LLM prompt that checks whether the user query is possibly malicious. If enabled, you can provide the following options:

    * **Prompt security settings:** You can select either **Default** for default security settings or **Customize** to clarify what user queries should be considered safe or unsafe.
    * **Select generative model:** This controls the LLM used for classification. If you select **Default** (recommended), a default model will be chosen for you, which may automatically change as newer and improved models become available.
    * **Security prompt:** You can select either **Default** for a default security prompt or **Customize** to provide instructions that assist in classifying malicious user queries. If you select **Default** , the prompt may automatically update for improvements.
    * **Input threshold:** The minimum character length for a user query before security checks are applied. Small queries are more ambiguous and may be classified incorrectly. Any queries smaller than the input threshold will be treated as inherently safe.
  * **Generative fallback:**

    * **Text prompt configuration** link

See [Generative fallback: define your own prompt](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generative-fallback#define_your_own_prompt).

  * **Data Store:**

See [Data store agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings).




### Deterministic Flows

These settings apply to all flows in this agent, except for the ML settings which are applied per flow. To edit other flow-specific settings, navigate to the flow in the console and edit the settings there.

  * **Intent training:** Flows uses machine learning (ML) algorithms to understand end-user inputs, match them to intents, and extract structured data. Flows learn from [training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) that you provide and the language models built into flows. Based on this data, it builds a model for making decisions about which intent should be matched to an end-user input. You can apply unique ML settings for each flow of an agent.

The following intent training settings are available:

    * **Spell correction** link

If this is enabled and end-user input has a spelling or grammar mistake, an intent will be matched as though it was written correctly. The detect intent response will contain the corrected end-user input. For example, if an end-user enters "I want an applle," it will be processed as though the end-user entered "I want an apple." This also applies to matches involving both system and custom entities.

Spell corrections are available in English, French, German, Spanish, and Italian. They're available in all [Dialogflow CX regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region).

**Note:** If original and corrected end-user input match different intents, the intent matching the original end-user input is selected.

**Warnings and best practices:**

    * Spell correction can't correct ASR (automatic speech recognition) errors, so we don't recommend enabling it for agents using ASR inputs. 
      * It's possible for corrected input to match the wrong intent. You can fix this by adding commonly mismatched phrases to [negative examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative).
    * Spell correction increases the agent's response time slightly.

      * If an agent is defined using domain-specific jargon, the corrections may be undesired.
    * **Flow-specific ML settings:**

      * **NLU type** link

This can be one of:

      * **Advanced NLU: (default)** Advanced NLU technology. This NLU type works better than standard, especially for large agents and flows.
      * **Standard NLU:** Standard NLU technology. Will [no longer receive quality improvements or new features](https://docs.cloud.google.com/dialogflow/docs/release-notes#February_20_2024).
      * **Auto train** link

If enabled, the flow is trained whenever it is updated with the console. For large flows, this may cause console UI delays, so you should disable this setting and manually [train](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#train) as needed for large flows.

      * **Classification threshold** link

To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. This setting controls the minimum intent detection confidence required for an [intent match](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#match).

If the confidence score for an intent match is less than the threshold value, then a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) will be invoked.

You can set a separate classification threshold value for every flow in each language enabled for the agent. This is to accommodate different languages performing best at different classification thresholds. For more information about creating a multilingual agent, see the [Multilingual agents documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual).

**Note:** Before adjusting this value, you should try adding [negative examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative).
      * **Training status** link

Indicates if the flow has been trained since the latest update to the flow data.

      * **Train** link

Use this button to manually train the flow.

    * **Language** link

The languages supported by your agent. Once an agent is created, the default language cannot be changed. However, you can perform the following:

      1. Export your agent to the [JSON format](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export).
      2. Extract the downloaded file.
      3. Find the `agent.json` file.
      4. Update the `defaultLanguageCode` and `supportedLanguageCodes` fields to the chosen values.
      5. [Restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export#restore) the agent to the same or different agent from step 1.
      6. Update language-specific training phrases and entity values as needed.

You can also enable language auto detection and switching.




### Connectivity

  * **Custom payload template** link

In this section, you can create descriptions and payloads for [custom payload templates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#custom-payload-templates).

  * **Parameter definition** link

Clearly state what parameters from the session parameters will be sent to the webhook, and what session parameters can be set by the webhook response.

  * **Client certificate settings** link

Used to upload SSL certificates.




### Speech and IVR

  * **Speech options:**

    * **Text-to-Speech** link

    * **Languages and voices** link

You can select the language and voice used for speech synthesis.

You may enable [Custom voice](https://docs.cloud.google.com/text-to-speech/custom-voice/docs) for your agent by selecting the custom voice option from the voice name dropbox and specifying the custom voice name in the corresponding field. The custom voice name must follow the following pattern: `projects/PROJECT_ID/locations/LOCATION/models/MODEL_NAME`.

You can also use [voice cloning](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-cloning).

      * If you are using telephony gateway, make sure the **Dialogflow Service Agent** service account `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com` is granted with "AutoML Predictor" in your custom voice project.
      * For regular API calls, make sure the service account used to call Dialogflow CX is granted with "AutoML Predictor" role in your custom voice project.

      * **Voice pitch** link

Controls the relative highness or lowness of the tone of speech.

      * **Speaking rate** link

Controls the speaking speed of the voice.

      * **Override request-level synthesized speech configuration** link

If enabled, the synthesized speech configuration specified in the agent settings overrides the one specified in the API, partner integration, or the conversation profile.

      * **Pronunciation** link

Use these settings to provide the agent with pronunciation of certain phrases, using X-SAMPA phonetic encoding.

    * **Speech-to-Text** link

      * **Enable auto speech adaptation** link

See [Auto speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#auto-adaptation).

      * **Enable advanced speech settings** link

For details about advanced speech options, see the [Advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech) guide.

      * **DTMF settings** link

For more information, see [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf).

      * **Enable manual speech adaptation** link

For more information, see [manual speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#manual-adaptation).

  * **Call companion:** See [Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion).




### UI Settings

You can use these settings to customize the Messenger and call companion user interfaces.

### Security

For more information, see [Security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings) and [Access control](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control).

## Dialogflow CX console agent settings

**Deprecated:** The Dialogflow CX console [has been replaced](https://docs.cloud.google.com/dialogflow/docs/release-notes#October_16_2025) by the [Conversational Agents console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents).

To access agent settings:

###  Console 

  1. Open the console.
  2. Choose your project.
  3. Select your agent.
  4. Click **Agent Settings**.
  5. Update the settings as needed.
  6. Click **Save**.



###  API 

For more information, see the `get` and `patch/update` methods for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

### General settings

The following general settings are available for agents:

  * **Display name:** A human-readable name for your agent.
  * **Time zone:** The default time zone for your agent.
  * **Default language:** The default language supported by your agent. Once an agent is created, the default language cannot be changed. However, you can perform the following:

    1. Export your agent to the [JSON format](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export).
    2. Extract the downloaded file.
    3. Find the `agent.json` file.
    4. Update the `defaultLanguageCode` and `supportedLanguageCodes` fields to the needed values.
    5. [Restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export#restore) the agent to the same or different agent from step 1.
    6. Update language-specific training phrases and entity values as needed.
  * **Agent lock:**

    * **Lock the agent:** Indicates if the agent is locked. A locked agent cannot be edited.
  * **Logging settings:**

    * **Enable Cloud Logging:** Indicates if [Cloud logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging) is enabled for the agent.
    * **Enable conversation history:** Indicates if you want Google to collect and store [redacted](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings) end-user queries for quality improvement.
**Note:** Some features, such as [Experiments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments), [Conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history), [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq), [Analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics), and NLU model improvement require this setting to be enabled, as they rely on traffic logs.
    * **Enable consent-based end-user input redaction:**

If this setting is enabled, it lets you use a special session parameter to control whether end-user input and parameters are redacted from [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) and [Cloud logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging). By default, the session parameter is `true`. If this setting is disabled, no redaction occurs.

User consent is collected using a boolean session parameter: `$session.params.conversation-redaction`. If this setting is enabled, and the session parameter is set to `false`, no redaction occurs **(other redaction strategies still apply)**. If this setting is enabled, and the session parameter is set to `true`, redaction occurs.

An example consent requesting flow could be: first ask the user if they want to keep end-user input, and match the response with two intents, one is "yes intent" and the other is "no intent." Then, set the session parameter to `false` (no redaction) in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the "yes intent" route in [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment), and to `true` (redaction occurs) in the [parameter preset](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the "no intent" route.

  * **BigQuery export:**

    * **Enable BigQuery export:** Indicates if [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq) is enabled.
    * **BigQuery dataset:** The BigQuery dataset name.
    * **BigQuery table:** The BigQuery table name.
  * **Intent suggestions:** You can enable [intent suggestions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#suggestions).

  * **Custom payload template:** In this section, you can create descriptions and payloads for [custom payload templates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#custom-payload-templates).




### ML settings

Dialogflow CX uses machine learning (ML) algorithms to understand end-user inputs, match them to intents, and extract structured data. Dialogflow CX learns from [training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) that you provide and the language models built into Dialogflow CX. Based on this data, it builds a model for making decisions about which intent should be matched to an end-user input. You can apply unique ML settings for each flow of an agent, and the model created by Dialogflow CX is unique for each flow.

The following agent-wide ML settings are available:

  * **Allow ML to correct spelling:**

If this is enabled and end-user input has a spelling or grammar mistake, an intent will be matched as though it was written correctly. The detect intent response will contain the corrected end-user input. For example, if an end-user enters "I want an applle", it will be processed as though the end-user entered "I want an apple". This also applies to matches involving both system and custom entities.

Spell correction is available in English, French, German, Spanish, and Italian. It is available in all [Dialogflow CX regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region).

**Note:** If original and corrected end-user input match different intents, the intent matching the original end-user input is selected.

**Warnings and best practices:**

    * Spell correction can't correct ASR (automatic speech recognition) errors, so we don't recommend enabling it for agents using ASR inputs.
    * It's possible for corrected input to match the wrong intent. You can fix this by adding commonly mismatched phrases to [negative examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative).
    * Spell correction increases the agent's response time slightly.
    * If an agent is defined using domain-specific jargon, the corrections may be undesired.



The following flow-specific ML settings are available:

  * **NLU type:**

This can be one of:

    * **Advanced NLU (default):** Advanced NLU technology. This NLU type works better than standard, especially for large agents and flows.
    * **Standard NLU:** : Standard NLU technology. Will [no longer receive quality improvements or new features](https://docs.cloud.google.com/dialogflow/docs/release-notes#February_20_2024).
  * **Auto train:** If enabled, the flow is trained whenever it is updated with the console. For large flows, this may cause console UI delays, so you should disable this setting and manually [train](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#train) as needed for large flows.

  * **Classification threshold:**

To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. This setting controls the minimum intent detection confidence required for an [intent match](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#match).

If the confidence score for an intent match is less than the threshold value, then a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) will be invoked.

You can set a separate classification threshold value for every flow in each language enabled for the agent. This is to accommodate different languages performing best at different classification thresholds. For more information about creating a multilingual agent, see the [Multilingual agents documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual).

**Note:** Before adjusting this value, you should try adding [negative examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative).
  * **Training status:** Indicates if the flow has been trained since the latest update to the flow data.

  * **Train NLU:** Use this button to manually train the flow.




### Generative AI settings

The following generative AI settings are available:

  * **General:**

    * **Banned phrases:** A list of phrases that are banned for generative AI. If a banned phrase appears in the prompt or the generated response, the generation will fail.
    * **Safety filters:** Configure sensitivity levels of safety filters with respect to different Responsible AI (RAI) categories. Content will be assessed against the following four categories:
Category | Description  
---|---  
Hate speech | Negative or harmful comments targeting identity and/or protected attributes.  
Dangerous content | Promotes or enables access to harmful goods, services, and activities  
Sexually explicit content | Contains references to sexual acts or other lewd content  
Harassment | Malicious, intimidating, bullying, or abusive comments targeting another individual  
  
Content is blocked based on the probability that it's harmful. The sensitivity level can be customized by choosing one of **Block none** , **Block few** , **Block some** , and **Block most** for each category.

For more information, see [Configuring safety attributes](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes).

    * **Prompt security:** You can check the **enable prompt security check** setting to enable prompt security checks. If enabled, the agent will attempt to prevent prompt injection attacks. These attacks may be used to reveal parts of the agent prompt or to provide responses the agent is not supposed to supply. This is accomplished by sending an additional LLM prompt that checks if the user query is possibly malicious.
  * **Generative agent:**

**Note:** This setting has restricted access.
    * **Generative model selection:** Select the model used by generative features. For more information, see [model versions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning).
    * **Playbook context truncation:** culls some past turns from the playbook prompt to keep the prompt size from growing with every sequential turn handled by the playbook. This feature offers a way to mitigate unwanted prompt size growth.

Normally, without truncation, each subsequent turn will be appended into the "conversation history" of the LLM prompt regardless of whether it's relevant to the current turn. This can ultimately lead to the prompt increasing in size with every turn. As more of the prompt is taken up by conversation history, less of the prompt can be used for few-shot examples (so these might get dropped). Eventually, the prompt might also breach current token limits. You can increase token sizes to accommodate this, but keep in mind that increased prompt sizes also add to the LLM response latency.

Playbook context truncation lets you set a percentage of the token budget to be reserved for conversation history, as a maximum. Conversation turns are preserved in most recent to least recent order. This setting can help you prevent token limits from being exceeded. Regardless of which setting you choose, a minimum of two conversation turns are preserved, in most recent to least recent order.

You must first set a [token limit](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#builder-settings-generative) before you can modify this setting.

**Important:** Truncating context might cause some parameters to be inadvertently be lost if they are part of culled turns. Evaluate your playbook interactions carefully after enabling this option.

Token input budget is also used by the following:

    * **System instructions and examples** automatically added to the prompt. This behavior cannot be modified.
    * **Playbook instructions and goals:** Any instructions and goals that you write will be added to the prompt in their entirety.
    * **Playbook few-shot examples** added either in order (by default) or by an algorithm that you choose (such as regular expression best match ordering). Examples are culled to fit within input token budget after all other items are included.
    * **Conversation history** made up of user and agent utterances, flow and playbook transition context, tool calls and outputs in the same session from all previous turns sequentially handled by the current playbook.
  * **Generative fallback:**

    * **Text prompt configuration:** See [Generative fallback: define your own prompt](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generative-fallback#define_your_own_prompt).
  * **Data store:** See [Data store agent settings](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store-agent-settings).




### Speech and IVR settings

The following speech and IVR settings are available:

  * **Text-to-Speech:**

    * **Voice selection:**
**Note:** SSML Tags are not supported for `Chirp3-HD` voices. If you want to use `Chirp3-HD` voices, you must remove all SSML tags and test the results to assess if the quality meet your needs.

You can select the language and voice used for speech synthesis.

You can enable [Custom voice](https://docs.cloud.google.com/text-to-speech/custom-voice/docs) for your agent by selecting the custom voice option from the voice selection dropbox and specifying the custom voice name in the corresponding field. The custom voice name must follow the following pattern: `projects/PROJECT_ID/locations/LOCATION/models/MODEL_NAME`.

    * If you are using telephony gateway, make sure the **Dialogflow Service Agent** service account `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com` is granted with "AutoML Predictor" in your custom voice project.
    * For regular API calls, make sure the service account used to call Dialogflow CX is granted with "AutoML Predictor" role in your custom voice project.
  * **Speech-to-Text:**

    * **Enable auto speech adaptation:** See [Auto speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#auto-adaptation).
    * **Advanced speech settings:** For details about advanced speech options, see the [Advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech) guide.



### DTMF

See [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf).

### Multimodal

See [Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion).

### Share settings

See [Access control](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control).

### Languages settings

Add additional language support to your agent. For the full list of languages, see the [language reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).

#### Language auto detection

When you configure [language auto detection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#lang-detect), your chat agent will automatically detect the end-user's language and switch to that language. See the [language auto detection documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#lang-detect) for details.

### Security settings

See [Security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings).

### Advanced settings

The only advanced setting is for [sentiment analysis](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment).

## Generative AI App Builder settings

This section describes the settings available for agent apps.

### General

The following general settings are available for agent apps:

  * **Display name:** A human-readable name for your agent app.
  * **Location:** The agent app region.
  * **App lock:** If enabled, changes to the agent app are not permitted.



### Logging

The following logging settings are available for agent apps:

  * **Enable Cloud Logging:** If enabled, logs will be sent to [Cloud logging](https://docs.cloud.google.com/logging/docs).
  * **Enable Conversation History:** If enabled, [conversation history](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/user-interface#conversation-history) will be available. Indicates if you want Google to collect and store redacted end-user queries for quality improvement. This setting doesn't affect whether conversation history is used to generate agent responses.
  * **Enable BigQuery Export:** If enabled, conversation history is exported to BigQuery. The **Enable Conversation History** setting must also be enabled.



### GenAI

The following generative AI settings are available for agent apps:

  * **Generative model selection:** Select the [generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning) that agents should use by default.
  * **Input token limit:** Select the input token limit for the [generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models). This is the maximum token size for input to be sent to the model. Depending on the model, a [token](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count) can be somewhere between one character and one word. Smaller token limits have lower latency, but the model input size is limited. Larger token limits have higher latency, but the model input size can be larger.
  * **Output token limit:** Select the output token limit for the [generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models). This is the maximum token size for output to be received from the model. Depending on the model, a [token](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count) can be somewhere between one character and one word. Smaller token limits have lower latency, but the model output size is limited. Larger token limits have higher latency, but the model output size can be larger.
  * **Temperature:** The temperature for a LLM lets you control how creative the responses are. A low value provides more predictable responses. A high value provides more creative or random responses.
  * **Banned phrases:** A list of phrases that are banned for generative AI. If a banned phrase appears in the prompt or the generated response, the agent will return a fallback response instead.
  * **Safety filters:** Configure sensitivity levels of safety filters with respect to different Responsible AI (RAI) categories. Content will be assessed against the following four categories:

Category | Description  
---|---  
Hate speech | Negative or harmful comments targeting identity and/or protected attributes.  
Dangerous content | Promotes or enables access to harmful goods, services, and activities  
Sexually explicit content | Contains references to sexual acts or other lewd content  
Harassment | Malicious, intimidating, bullying, or abusive comments targeting another individual  
  
Content is blocked based on the probability that it's harmful. The sensitivity level can be customized by choosing one of **Block none** (disabling RAI checks), **Block few** (blocking only high-probability instances of harmful content), **Block some** (medium and high probability instances), and **Block most** (low, medium, and high probability) for each category.

For more information, see [configure safety attributes](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes).

  * **Prompt security:** You can check the **enable prompt security check** setting to enable prompt security checks. If enabled, the agent will attempt to prevent prompt injection attacks. These attacks can be used to reveal parts of the agent prompt or to provide responses the agent is not supposed to supply. This is accomplished by sending an additional LLM prompt that checks if the end-user query is possibly malicious.




### Git

These settings provide a Git integration. Follow the instructions to configure the integration.

[ Previous arrow_back  Zip code collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection)

[ Next Speech models  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
