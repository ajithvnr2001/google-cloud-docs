---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/quotas/
title: Quotas \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:22.075765+00:00
---

# Quotas  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

Accurate quota estimation is based on the number of your queries per second (QPS) to each API. The following sections outline the quotas for APIs used with each Agent Assist feature.

## Project types

The following quota tables list two types of projects: consumer and resource. See the documentation on using multiple projects for [definitions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project#consumer-resource) of these two project types.

## Voice transcription

This feature uses either telephony or gRPC integration, which each have different API quotas.

### Telephony integration

See the [Dialogflow quotas](https://docs.cloud.google.com/dialogflow/quotas#table) for the APIs used with telephony integration.

### gRPC integration

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`AnalyzeContentOperationsPerMinutePerProject` | 300 requests/min | Global | Consumer project | AnalyzeContent/StreamingAnalyzeContent requests. Quota is shared between Dialogflow and Agent Assist.  
`ConcurrentBidiStreamingSessionsPerProjectPerRegion` | 50 concurrent requests | Regional (global traffic is counted in `us-central1` region) | Consumer project (resource project for telephony SipRec integration) | Concurrent bidirectional streaming sessions per region.  
  
### Transcription with Chirp models

**Quota name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`SttV2StreamingRequestsPerMinutePerResourceTypePerRegion` | 20 requests per minute | Regional (Global traffic is counted in the `us-central1` region.) | Consumer project (resource project for telephony SipRec integration) | Number of new `StreamingRecognize` requests sent to STT V2 per resource type.  
  
## Sentiment analysis

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`AnalyzeSentimentOperationsPerVersion` | 300 requests/min | Global | Consumer project | Sentiment analysis requests through AnalyzeContent or StreamingAnalyzeContent.  
`AnalyzeSentimentOperationsPerVersionPerRegion` | 300 requests/min | Regional | Consumer project | Sentiment analysis requests through AnalyzeContent or StreamingAnalyzeContent.  
`AnalyzeSentimentOperationsPerMinutePerProject` | 300 requests/min | Global | Consumer project | Sentiment analysis requests through AnalyzeContent or StreamingAnalyzeContent.  
`AnalyzeSentimentOperationsPerMinutePerProjectPerRegion` | 300 requests/min | Regional | Consumer project | Sentiment analysis requests through AnalyzeContent or StreamingAnalyzeContent.  
  
## Build your own assist

This feature uses the following AI models:

  * text-bison@001 (default limit 0)
  * text-bison@002
  * text-bison-32k@002
  * gemini-1.0-pro
  * gemini-1.5-pro
  * gemini-1.5-pro-001
  * gemini-1.5-flash-001
  * gemini-1.5-flash-002
  * gemini-2.0-flash-001

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`GeneratorSuggestionOperationsPerMinutePerModelType` | 10 requests/min | Global | Consumer project | Generator suggestion operations per model type.  
`GeneratorSuggestionOperationsPerMinutePerModelTypePerRegion` | 10 requests/min | Regional | Consumer project | Generator suggestion operations per model type and region.  
  
## Smart reply

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`SmartReplyBaselineModelOperationsPerMinutePerProject` | 120 requests/min | Global | Consumer project | Get smart reply baseline model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
`SmartReplyBaselineV2ModelOperationsPerMinutePerProject` | 60 requests/min | Global | Consumer project | Get smart reply baseline V2 model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
`SmartReplyBaselineV2ModelOperationsPerMinutePerProjectPerRegion` | 60 requests/min | Regional | Consumer project | Get smart reply baseline V2 model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
  
## Generative smart reply

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`SmartReplyBaselineModelOperationsPerMinutePerProject` | 120 requests/min | Global | Consumer project | Get smart reply baseline model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
`SmartReplyBaselineV2ModelOperationsPerMinutePerProject` | 60 requests/min | Global | Consumer project | Get smart reply baseline V2 model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
`SmartReplyBaselineV2ModelOperationsPerMinutePerProjectPerRegion` | 60 requests/min | Regional | Consumer project | Get smart reply baseline V2 model requests through `AnalyzeContent` or `SuggestSmartReplies`.  
  
## Summarization

AI-generated summarization uses the following models:

  * summarization-1.0
  * summarization-2.0
  * summarization-2.1
  * summarization-3.0
  * summarization-3.1
  * summarization-4.0
  * summarization-5.0



The following table shows the quota type and model used for each version of summarization.

  
**Summarization version** |   
**Quota type** |   
**Backend model**  
---|---|---  
  
Generator 5.0 |   
Generator based |   
Pretrained Gemini-2.5-flash  
  
Generator 4.0 |   
Generator based |   
Pretrained Gemini-2.0-flash-001  
  
Generator 3.1 |   
Generator based |   
Lora-tuned gemini-1.5-flash-001  
  
Generator 3.0 |   
Generator based |   
Lora-tuned gemini-1.0-pro-002  
  
Generator 2.1 |   
Generator based |   
Lora-tuned text-bison-32k@002  
  
Generator 2.0 |   
Generator based |   
Lora-tuned text-bison-32k@002  
  
Generator 1.0 |   
Generator based |   
Lora-tuned text-bison@001  
  
Baseline v2 |   
Baseline v2 model |   
text-bison  
  
Baseline v1 |   
Non Generator based |   
LongT5 model  
  
Custom 2.0 |   
Non Generator based |   
LongT5 model  
  
The quota types in the previous table are reflected in the following quota list for APIs used with summarization.

  
**Quota type** |   
**Quota limit name** |   
**Default value** |   
**Region** |   
**Charging resource/Consumer project** |   
**Description**  
---|---|---|---|---|---  
  
Generator based |   
GeneratorSuggestionOperationsPerMinutePerModelTypePerRegion |   
10 requests/min |   
Regional |   
Consumer project |   
Generator suggestion operations per model type and region  
  
Generator based |   
GeneratorSuggestionOperationsPerMinutePerModelType |   
10 requests/min |   
Global |   
Consumer project |   
Generator suggestion operations per model type  
  
Generator based |   
SuggestConversationSummaryOperationsPerMinutePerProject |   
60 requests/min |   
Global |   
Resource project |   
Suggest conversation summary operations  
  
Non Generator based |   
SuggestConversationSummaryOperationsPerMinutePerProjectPerRegion |   
0-2 requests/min |   
Regional |   
Resource project |   
Suggest conversation summary operations in each region  
  
Baseline v2 model |   
SuggestSummaryV2BaselineOperationsPerMinutePerProject |   
120 requests/min |   
Global |   
Resource project |   
Conversation Summary Suggestion V2 Baseline polling requests  
  
Baseline v2 model |   
SuggestSummaryV2BaselineOperationsPerMinutePerProjectPerRegion |   
60 requests/min |   
Regional |   
Resource project |   
Conversation Summary Suggestion V2 Baseline polling requests in each region  
  
## Summarization autoevaluation

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`ConcurrentSummarizationEvaluationsPerProject` | 1 request per project | Consumer project | Autoevaluation requests  
  
If you need additional concurrent quotas, raise a request through the Google Cloud console. This feature can support up to four concurrent quotas per projects.

## Generative knowledge assist

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`SearchKnowledgeRequestsPerMinutePerProject` | 60 requests/min | Global | Consumer project | SearchKnowledge requests.  
`SearchKnowledgeRequestsPerMinutePerProjectPerRegion` | 30 requests/min | Regional | Consumer project | SearchKnowledge requests each region.  
  
## Proactive generative knowledge assist V1

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`SuggestKnowledgeAssistOperationsPerMinutePerProject` | 60 requests/min | Global | Resource project | KnowledgeAssist requests through `AnalyzeContent` or `SuggestKnowledgeAssist`.  
`SuggestKnowledgeAssistOperationsPerMinutePerProjectPerRegion` | 30 requests/min | Regional | Resource project | KnowledgeAssist requests through `AnalyzeContent` or `SuggestKnowledgeAssist` in each region.  
`SuggestKnowledgeAssistOpsPerMinutePerProjectPerMultiRegion` | 30 requests/min | Multi-Regional | Resource project | KnowledgeAssist requests through `AnalyzeContent` or `SuggestKnowledgeAssist` directed to multi-region endpoints, such as US or EU.  
  
## Proactive generative knowledge assist V2

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`KnowledgeAssistOpsPerMinutePerProjectPerVersion` | 30 requests/min | Global | Resource project | KnowledgeAssist requests for a specific model version when the request is directed to the global location endpoint.  
`KnowledgeAssistOpsPerMinutePerProjectPerVersionPerRegion` | 30 requests/min | Regional | Resource project | KnowledgeAssist requests directed to a single specific Google Cloud region, such as `us-central1` or `europe-west1`.  
`KnowledgeAssistOpsPerMinutePerProjectPerVersionPerMultiRegion` | 30 requests/min | Multi-Regional | Resource project | KnowledgeAssist requests directed to multi-region endpoints, such as US or EU.  
  
## AI coach (LLM)

This feature uses the agent-coaching-2.5 AI model.

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`GeneratorSuggestionOperationsPerMinutePerModelType` | 60 requests per minute | Global | Consumer project | Generator suggestion operations per model type.  
`GeneratorSuggestionOperationsPerMinutePerModelTypePerRegion` | 60 requests per minute | Regional | Consumer project | Generator suggestion operations per model type and region.  
  
## Companion agent

Companion agent API rate and token based quotas

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`CompanionAgentManagerOperationsPerMinutePerProject` | 300 requests/min | Global | Consumer project | Maximum design-time CRUDL companion agent API requests.  
`CompanionAgentManagerOperationsPerMinutePerProjectPerRegion` | 300 requests/min | Regional | Consumer project | Maximum design-time CRUDL companion agent API requests in each region.  
`CompanionAgentManagerOperationsPerMinutePerProjectPerMultiRegion` | 300 requests/min | Multi-Regional | Consumer project | Maximum design-time CRUDL companion agent API requests in each multi-region.  
`CompanionAgentLLMTokenConsumptionPerMinute` | 600,000 tokens/min | Global | Resource project for (Streaming)AnalyzeContent requests; consumer project for all others | Companion agent LLM token consumption in proactive mode.  
`CompanionAgentLLMTokenConsumptionPerMinutePerRegion` | 600,000 tokens/min | Regional | Resource project for (Streaming)AnalyzeContent requests; consumer project for all others | Companion agent LLM token consumption in proactive mode in each region.  
`CompanionAgentLLMTokenConsumptionPerMinutePerMultiRegion` | 600,000 tokens/min | Multi-Regional | Resource project for (Streaming)AnalyzeContent requests; consumer project for all others | Companion agent LLM token consumption in proactive mode in each multi-region.  
`CompAgentReactiveLLMTokensPerMinute` | 600,000 tokens/min | Global | Resource project for StreamingReactiveCompanionSuggestions; consumer project for all others | Companion agent LLM token consumption in reactive mode.  
`CompAgentReactiveLLMTokensPerMinutePerRegion` | 600,000 tokens/min | Regional | Resource project for StreamingReactiveCompanionSuggestions; consumer project for all others | Companion agent LLM token consumption in reactive mode in each region.  
`CompAgentReactiveLLMTokensPerMinutePerMultiRegion` | 600,000 tokens/min | Multi-Regional | Resource project for StreamingReactiveCompanionSuggestions; consumer project for all others | Companion agent LLM token consumption in reactive mode in each multi-region.  
**Note:** Companion agent quota limit names differ between proactive and on-demand assistant modes. Ensure to use `CompanionAgent...` prefix and `...TokenConsumptionPerMinute` suffix for proactive mode and `CompAgentReactive...` prefix and `...LLMTokensPerMinute` suffix for on-demand assistant mode while monitoring metrics or requesting quota increases in the Google Cloud console.

Companion agent resource allocation quotas

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`CompanionAgentCountPerProject` | 100 | Global | Consumer project | Maximum number of companion agents that can be created in a project.  
`CompanionAgentCountPerProjectPerRegion` | 100 | Regional | Consumer project | Maximum number of companion agents that can be created in a project in each region.  
`CompanionAgentCountPerProjectPerMultiRegion` | 100 | Multi-Regional | Consumer project | Maximum number of companion agents that can be created in a project in each multi-region.  
  
## Other API quotas

**Quota limit name** | **Default value** | **Region** | **Charging resource/Consumer project** | **Description**  
---|---|---|---|---  
`ConversationOperationsPerMinutePerProject` | 300 requests/min | Global | Consumer project | Other conversation requests except AnalyzeContent and StreamingAnalyzeContent, for example CreateConversation, CompleteConversation. Quota is shared between Dialogflow and Agent Assist.  
`MessagePollingOperationsPerMinutePerProject` | 1,200 requests / min | Global | Consumer project | ListMessages requests. Quota is shared between Dialogflow and Agent Assist.  
`AnswerRecordOperationsPerMinutePerProject` | 300 requests / min | Global | Consumer project | AnswerRecord requests.  
  
## Gemini Transcribe Live

**Quota limit name** | **Metric name** | **Default limit** | **Scope** | **Description**  
---|---|---|---|---  
`GeminiAsrConcurrentStreamsPerProject` | `dialogflow.googleapis.com/gemini_asr_concurrent_streams` | 10 concurrent streams | Global | Maximum number of concurrent streams using a Gemini ASR model.  
`GeminiAsrConcurrentStreamsPerProjectPerRegion` | `dialogflow.googleapis.com/gemini_asr_concurrent_streams_per_region` | 10 concurrent streams | Regional | Maximum number of concurrent streams using a Gemini ASR model in each region.  
`GeminiAsrConcurrentStreamsPerProjectPerMultiRegion` | `dialogflow.googleapis.com/gemini_asr_concurrent_streams_per_multi_region` | 10 concurrent streams | Multi-regional | Maximum number of concurrent streams using a Gemini ASR model in each multi-region(for example: us, eu).  
  
## What's next

  * For more information on requesting a quota increase, see the [quota page](https://docs.cloud.google.com/docs/quotas/view-manage#managing_your_quota_console). 
  * After submitting your request, Google might contact you for more information and inform you when your request is approved or denied.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
