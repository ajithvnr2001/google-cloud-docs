---
url: https://docs.cloud.google.com/dialogflow/quotas/
title: Quotas and limits \u00a0|\u00a0 Dialogflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:50:42.188664+00:00
---

# Quotas and limits  |  Dialogflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dialogflow/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the commonly encountered quotas and limits for Dialogflow. For information on how to find a complete list of quotas and limits, see the following sections.

We reserve the right to change these constraints, and this page is updated to reflect any changes.

## Quotas

[Quotas](https://docs.cloud.google.com/docs/quotas/overview) are default constraints applied to your project. When using generative features, each combination of model and region has its own generative quota. If you are using a paid [edition](https://docs.cloud.google.com/dialogflow/docs/editions), you can request a quota increase. Quotas throttle service load per client, which protects services from being overloaded and protects you from unexpected resource usage.

Dialogflow quotas vary, depending on the [edition](https://docs.cloud.google.com/dialogflow/docs/editions) of your agent. Quotas apply to each project and are shared across all applications and IP addresses that use a project.

Quota time boundary details:

  * Per-month quotas are replenished on the 1st of each month at 12:00 AM Pacific Time.
  * Per-day quotas are replenished daily at 12:00 AM Pacific Time. When a Pacific Time daylight savings transition increases the length of a day, Dialogflow grants a proportional quota bonus. However, there's no equivalent deduction when a shorter day occurs due to the daylight savings transition.
  * Per-minute quotas are refreshed every 60 seconds on the minute.



The quotas listed in the quotas table are the commonly encountered quotas. To review all quotas, see the [Google Cloud console Dialogflow quotas](https://console.cloud.google.com/apis/api/dialogflow.googleapis.com/quotas) page.

### Generative quotas

When your agent uses Dialogflow CX [generative features](https://docs.cloud.google.com/dialogflow/cx/docs/generative-deterministic), each combination of model and region has unique quotas.

#### Quota identifier

Generative quotas track token usage for large language models (LLMs) in Dialogflow CX across the following features:

  * Generators.
  * Generative fallback.
  * Playbook.
  * Data store.



The default limit for generative LLM token consumption quotas is 600,000 tokens per minute. The quota identifier depends on the model and region:

  * **Gemini 2.5 models (`gemini-2.5-flash` and `gemini-2.5-flash-lite`)**: Use the regional `ConversationalAgentLlmTokenConsumption` quota.
  * **Gemini 3 and later models (such as`gemini-3.1-flash-lite`)**: Use the `ConversationalAgentMultiRegionLLMTokenConsumption` or `ConversationalAgentGlobalLLMTokenConsumption` quota with the following regional mapping: 
    * All regions in the United States use the `ConversationalAgentMultiRegionLLMTokenConsumption` quota with `multi_region=us`.
    * All regions in Europe use the `ConversationalAgentMultiRegionLLMTokenConsumption` quota with `multi_region=eu`.
    * Other regions (including `global`) use the `ConversationalAgentGlobalLLMTokenConsumption` quota.



#### Multi-region quota increase request

For `gemini-2.5-flash` and `gemini-2.5-flash-lite`, which use the `ConversationalAgentLlmTokenConsumption` quota, if your agent is in a multi-region (`us`, `eu`, or `global`), submit your quota increase request for one of the following specific regions:

  * For agents in the **US** and **Global** multi-regions, use **us-central1**.
  * For agents in the **EU** multi-region, use **europe-west4**.



Specifically for the `ConversationalAgentMultiRegionLLMTokenConsumption` quota used by Gemini 3 and later models, if you don't see the dimensional quota (such as `ConversationalAgentMultiRegionLLMTokenConsumption` with `multi_region=us` and `base_model=gemini-3.1-flash-lite`) in the Google Cloud console, either you haven't used this quota yet or you can submit a quota increase request using the following `gcloud` command:
    
    
    PROJECT_ID=foo-test
    TARGET_TPM=1000000
    MULTI_REGION=us
    BASE_MODEL=gemini-3.1-flash-lite
    USER_EMAIL=user@example.com
    REASON="Reason for requesting higher multi-region token per minute limit"
    gcloud beta quotas preferences create \
      --service=dialogflow.googleapis.com \
      --project="${PROJECT_ID}" \
      --billing-project="${PROJECT_ID}" \
      --quota-id=ConversationalAgentMultiRegionLLMTokensPerMinutePerBaseModel \
      --preferred-value=${TARGET_TPM} \
      --dimensions=multi_region=${MULTI_REGION},base_model=${BASE_MODEL} \
      --email="${USER_EMAIL}" \
      --justification="${REASON}"
    

#### Visualize token usage by region and model

To gain insights into your LLM token consumption across different regions and models, follow these steps using [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  1. **Access Metrics Explorer:** Open [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer).
  2. **Select the Metric:** Select `Conversational Agent LLM tokens quota usage` as the metric you want to analyze.
  3. **Configure Aggregation and Aligner:**
     * Set the aggregation function to `Sum` to obtain the total token usage.
     * Select `Configure Aligner` to calculate changes between consecutive data points in your time series. Understanding usage trends over time is easier this way.
  4. **Define Aggregation Dimensions:** To break down the token usage, select `location` and `base_model` as the dimensions for aggregation. Token consumption varies across different regions and models.
  5. **Set Aligner Function:** Select `Sum` as the aligner function to calculate the total change in token usage between consecutive data points.



### Quota increase request

You can request a [quota increase adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) if you need to.

If you use different projects for Dialogflow agents and for authenticating with service accounts, request a quota increase for the consumer project. For more information, see [Using multiple projects for Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/multi-project) or [Using multiple projects for Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project).

For [Dialogflow ES agents](https://docs.cloud.google.com/dialogflow/docs/editions#agent-types), you must [upgrade](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#change-editions) the agent to the Dialogflow Essentials [edition](https://docs.cloud.google.com/dialogflow/docs/editions) before you request a quota increase.

### Quotas table

The following terms are used to describe pricing and quotas:

  * **Request:** A _request_ is defined as any API call to the Dialogflow CX service, whether direct with API usage or indirect with integration or console usage. Depending on the task and design of the agent, the number of requests needed for an end-user to accomplish a task with a Dialogflow CX agent can vary greatly.
  * **Session:** A _session_ is a conversation between an end-user and a Dialogflow CX agent. A session remains active and its data is stored for 30 minutes after the last request is sent for the session. A session can be either a _chat session_ or a _voice session_. 
    * **Chat session:** A _chat session_ only uses text for both requests and responses.
    * **Voice session:** A _voice session_ uses audio for requests, responses, or both.
  * **Consumer projects and resource projects:** If you use multiple projects, it is possible that the project associated with your request authentication (consumer project) is not the same project that is associated with the agent in the request (resource project). In this case, the consumer project is used to determine prices and quotas. For more information, see [Using multiple projects for Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/multi-project) or [Using multiple projects for Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project).



The following tables provide a quota comparison for editions by [agent type](https://docs.cloud.google.com/dialogflow/docs/editions#agent-types). Unless a feature is indicated as included, quotas are cumulative for all features used by a request.

###  Dialogflow CX Agent

Feature | Dialogflow CX Edition  
---|---  
**Text**  
(includes all DetectIntent, StreamingDetectIntent, and FulfillIntent requests that do not contain audio)  | 1200 requests per minute  
**Audio input/output**  
(speech recognition, speech-to-text, STT, speech synthesis, text-to-speech, TTS, telephony)  | 600 requests per minute  
**Audio query operations with Chirp3 HD voice**  
(speech synthesis, text-to-speech, TTS, telephony)  | 25 requests per minute *  
**Generative features**  
(playbooks, datastores, generators, generative fallback)  | 600,000 tokens per minute, see [generative quotas](https://docs.cloud.google.com/dialogflow/quotas#generative)  
**Dialogflow CX Phone Gateway**  
Includes audio input and output.  | 100 total phone minutes per minute ‡  
**Design-time write requests**  
For example, calls to build or update an agent.  | 60 requests per minute  
**Design-time read requests**  
For example, calls to list or get agent resources.  | 300 requests per minute  
**Other session requests**  
For example, setting or getting session entities.  | 100 requests per minute  
Symbol | Description  
---|---  
* | If the quota is exceeded, Chirp 3 HD voices may fall back to Neural or Standard voices  
‡ | "Phone minutes per minute" is the total sum of time per minute that is used by all users making calls through the phone system. For example: in one 60-second time period one user is on for 60 seconds, a second for 30 seconds, and a third for 30 seconds. This is calculated as 2 minutes per minute. More minutes per minute allows more users to use the system simultaneously.  
  
###  Dialogflow ES Agent

Feature | Trial Edition | Essentials Edition  
---|---|---  
**Text**  
(includes all DetectIntent and StreamingDetectIntent requests that do not contain audio)  | 180 requests per minute ¶ | 600 requests per minute ¶  
**Audio input**  
(also known as speech recognition, speech-to-text, STT)  | 100 requests per minute †  
  
1000 requests per day †  
  
15,000 requests per month †  
  
Maximum 60 seconds of audio length per request † | 300 requests per minute †  
  
Maximum 60 seconds of audio length per request †  
**Audio output**  
(also known as speech synthesis, text-to-speech, TTS)  | Same as audio input | Same as audio input  
**Knowledge connectors (Beta)** | Maximum 10 MB total document size  
  
1000 requests per month  
  
100 requests per day | Unlimited #  
**Sentiment analysis** | Not available | Unlimited #  
**Dialogflow ES phone gateway**  
Includes audio input and output.  | Toll-free number: Not available  
  
3 total phone minutes per minute ‡  
  
30 phone minutes per day  
  
500 phone minutes per month  
  
Phone number reserved for 30 days | 100 total phone minutes per minute ‡  
**Mega agent** | 1000 requests per day | Unlimited #  
**Design-time write requests**  
For example, calls to build or update an agent.  | 60 requests per minute | 60 requests per minute  
**Design-time read requests**  
For example, calls to list or get agent resources.  | 60 requests per minute | 60 requests per minute  
**Other session requests**  
For example, setting or getting session entities or updating/querying context.  | 100 requests per minute | 100 requests per minute  
Symbol | Description  
---|---  
† | Each [StreamingDetectIntent](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-stream) stream is considered a single request, even though the stream might include multiple frames of `StreamingDetectIntentRequest` audio within the stream.  
‡ | "Phone minutes per minute" is the total sum of time per minute that is used by all users making calls through the phone system. For example: in one 60-second time period one user is on for 60 seconds, a second for 30 seconds, and a third for 30 seconds. This is calculated as 2 minutes per minute. More minutes per minute allows more users to use the system simultaneously.  
# | Features marked as unlimited are still potentially limited by use of other features. For example, if your edition provides unlimited quota for knowledge connectors, a text request that uses knowledge connectors is still limited by the quota for text requests.  
¶ | Google Assistant audio input and output is considered a text request.  
  
### Agent Assist

If you are using Agent Assist, the quotas listed under the **Dialogflow CX Agent** and **Dialogflow ES Agent** tabs also apply, according to which agent type you're using.

Feature | Trial Edition | Essentials Edition  
---|---|---  
**Agent Assist conversation other operations**  
Includes all requests that manage Conversations and Participants.  | Not available | 300 requests per minute  
**Agent Assist analyze text/audio operations**  
Includes all AnalyzeContent or StreamingAnalyzeContent requests for any [conversation stage](https://docs.cloud.google.com/agent-assist/docs/basics#conversation_stages). This includes all such requests involving text, speech synthesis, and/or speech recognition.  | Not available | 300 requests per minute  
**Concurrent bidi streaming sessions**  
Includes all BidiStreamingAnalyzeContent requests for any [conversation stage](https://docs.cloud.google.com/agent-assist/docs/basics#conversation_stages). This includes all such requests involving speech synthesis and/or speech recognition.  | Not available | 50 concurrent requests  
**Agent Assist conversation summary suggestion polling requests**  
Includes all requests for getting conversation summaries.  | Not available | 60 requests per minute  
**Agent Assist SearchKnowledge requests**  
Includes all SearchKnowledge requests for any [conversation stage](https://docs.cloud.google.com/agent-assist/docs/basics#conversation_stages).  | Not available | 60 requests per minute  
  
## Limits

_Limits_ are fixed constraints that can't be increased. Many resources and fields have count, duration, or length limitations, which are fixed constraints for the service implementation.

The following tables list commonly encountered limits. Feature-specific documentation and API reference documentation may provide additional limits.

### Count limits

**Note:** Some resources are language-specific ([Dialogflow CX documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#lang-specific), [Dialogflow ES documentation](https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual#lang-specific)) and these limits are described as "per _resource_ and per language". This means that you can define the maximum quantity of that resource for each language. For example, if your agent supports English and French, an intent can have at most 2,000 English training phrases and 2,000 French training phrases. All other language-independent resources have straightforward limits because these resources are shared across all languages for your agent.

###  Dialogflow CX Agent 

Description | Limit  
---|---  
Maximum number of agents per Google Cloud project | 1000  
Maximum number of phone numbers per project (except for the `global` region) | 5  
Maximum number of phone numbers per project per region (except for the `global` region) | 5  
Maximum number of flows per agent | 50  
Maximum number of entity types per agent | 250  
Maximum number of webhooks per agent | 100  
Maximum number of environments per agent | 20  
Maximum number of test cases per agent | 2000  
Maximum number of changelog per agent | 20,000  
Maximum number of pages per flow | 250  
Maximum number of route groups per flow | 100  
Maximum number of versions per flow | 20  
Maximum number of intents per agent | 10,000  
Maximum number of referenced intents per flow | 2000  
Maximum number of training phrases per intent and per language (except "Default Negative Intent") | 2000  
Maximum number of training phrases per flow and per language | 100,000  
Maximum number of parameters per intent | 20  
Maximum number of entity entries per entity | 30,000  
Maximum number of entity synonyms per entity entry | 200  
Maximum number of entity reference values and synonyms per agent and per language | 1,000,000  
Maximum number of parameters per page | 20  
Maximum number of routes per page | 2000  
Maximum number of event handlers per page | 100  
Maximum number of routes per route group | 2000  
Maximum number of playbooks per agent | 50  
Maximum number of playbook invocations in one conversational turn | 3  
Maximum number of LLM calls per playbook invocation in same conversational turn | 10  
Maximum number of playbook examples per agent | With the default example retrieval strategy, the system will automatically limit the number of examples to fit in the token limit of the model that is being used, based on the relevance of the examples to the session context.  
Maximum number of versions per playbook | 100  
Maximum number of tools per agent | 100  
Maximum number of steps per conversation | 100  
  
###  Dialogflow ES Agent 

Description | Limit  
---|---  
Maximum number of agents per [region](https://docs.cloud.google.com/dialogflow/docs/how/region) and per Google Cloud project ¶ | 1  
Maximum number of phone numbers per project (except for the `global` region) | 5  
Maximum number of phone numbers per project per region (except for the `global` region) | 5  
Maximum number of intents | 2000  
Maximum number of [entity types](https://docs.cloud.google.com/dialogflow/docs/entities-overview#terminology) | 250  
Maximum number of training phrases per intent and per language | 2000  
Maximum number of training phrases per agent and per language | 100,000  
Maximum number of [entity entries](https://docs.cloud.google.com/dialogflow/docs/entities-overview#terminology) | 30000  
Maximum number of entity synonyms per [entity entry](https://docs.cloud.google.com/dialogflow/docs/entities-overview#terminology) | 200  
Maximum number of [entity reference values and synonyms](https://docs.cloud.google.com/dialogflow/docs/entities-overview#terminology) per agent and per language | 1,000,000  
Maximum number of parameters per intent | 20  
Maximum number of input contexts per intent | 5  
Maximum number of output contexts per intent | 30  
Maximum number of text responses per intent and per language | 30  
Maximum number of prompts per parameter and per language | 30  
Maximum number of environments per agent | 10  
Maximum number of versions per agent | 1000  
¶ |  Maximum number of agents per account depends on the number of Google projects you can create in your account. See [how to request more projects](https://support.google.com/cloud/answer/7283050).   
---|---  
  
###  Agent Assist 

If you are using Agent Assist, the limits listed under the **Dialogflow CX Agent** and **Dialogflow ES** tabs also apply according to which agent type you're using.

Description | Limit  
---|---  
Minimum number of conversations required for model training | 30,000  
Maximum number of models trained concurrently per project | 1  
Maximum number of phone numbers per project (except for the `global` region) | 5  
Maximum number of phone numbers per project per region (except for the `global` region) | 5  
Maximum number of training node GPU hours per month | 4200  
Maximum number of conversation profiles | 100  
  
### Duration limits

###  Dialogflow CX Agent 

Description | Limit  
---|---  
Maximum timeout per webhook | 30 seconds  
Maximum audio input duration | 120 seconds  
  
###  Dialogflow ES Agent 

Description | Limit  
---|---  
Maximum webhook timeout | 5 seconds  
Maximum telephony call duration | 3.5 hours  
  
### Length limits

###  Dialogflow CX Agent 

Description | Limit  
---|---  
Maximum training phrase length | 768 characters  
Maximum text response length | 4,000 characters  
Maximum text input length for detect intent matched by _non-generative intents_ or _parameters_ | 256 characters  
  
###  Dialogflow ES Agent 

Description | Limit  
---|---  
Minimum agent name length | 1 character  
Maximum agent name length | 150 characters  
Maximum agent description length | 500 characters  
Maximum intent name length | 100 characters  
Maximum [entity type](https://docs.cloud.google.com/dialogflow/docs/entities-overview#terminology) name length | 30 characters  
Maximum training phrase length | 768 characters  
Maximum action name length | 250 characters  
Maximum context name length | 250 characters  
Maximum entry value length | 512 characters  
Maximum parameter name length | 30 characters  
Maximum text response length | 4000 characters  
Maximum detect intent text input length * | 256 characters  
Maximum event name length | 150 characters  
* |  This limit is enforced by the Dialogflow service. If you are using an [integration](https://docs.cloud.google.com/dialogflow/docs/integrations), the integration platform may have a smaller limit. See the details for your integration.   
---|---  
  
### Size limits

###  Dialogflow CX Agent 

Description | Limit  
---|---  
Maximum speech synthesis request size | See the TTS API content [limits](https://docs.cloud.google.com/text-to-speech/quotas#content_limits).  
Maximum tool specifications size | 20KB  
  
###  Dialogflow ES Agent 

Description | Limit  
---|---  
Maximum agent size (unzipped content) for agent [import/restore](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#export) | 50 MB  
Maximum speech synthesis request size | See the TTS API content [limits](https://docs.cloud.google.com/text-to-speech/quotas#content_limits).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
