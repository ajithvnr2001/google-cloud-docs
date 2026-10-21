---
url: https://docs.cloud.google.com/dialogflow/docs/editions/
title: Editions \u00a0|\u00a0 Dialogflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:59.122193+00:00
---

# Editions  |  Dialogflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/docs/editions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)



Send feedback 

#  Editions Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow offers multiple agent types and editions, each with different features, pricing, and quotas.

## Agent types

You can use the following agent types:

X | Item  
---|---  
Dialogflow CX agent | This [advanced agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) type is suitable for large or complex applications. It supports both a generative conversation design with [Playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) and a deterministic approach based on [Flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics). To learn more, see [Generative versus deterministic](https://docs.cloud.google.com/dialogflow/cx/docs/generative-deterministic).  
Dialogflow ES agent | This is the [standard agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview) type. It's suitable for small to medium, moderately complex applications. [Intents](https://docs.cloud.google.com/dialogflow/docs/intents-overview) are the building blocks of conversation design, and [Contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) control conversation paths. See [Dialogflow ES basics](https://docs.cloud.google.com/dialogflow/docs/basics).  
  
The following table provides a summary comparison of agent types. If you have an existing Dialogflow ES agent and want a more detailed comparison, see [Migrating from Dialogflow ES to Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/how/migrate).

Category | Dialogflow ES agent | Dialogflow CX agent  
---|---|---  
Editions | Dialogflow ES Trial Edition, Dialogflow ES Essentials Edition | Dialogflow CX Edition  
Agent building blocks | Flat structure of [intents](https://docs.cloud.google.com/dialogflow/docs/intents-overview) | Graph structure of [flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) and [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)  
Conversation control | Linear conversation paths that simulate nonlinear paths using [intents](https://docs.cloud.google.com/dialogflow/docs/intents-overview) as nodes and [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) to control paths | State machine model with explicit conversation control using [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) as nodes and [state handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) to control paths  
Console user experience | Mostly text forms | Visual graphs showing conversation paths and text forms for configurations  
Intent reusability | [Intents](https://docs.cloud.google.com/dialogflow/docs/intents-overview) are coupled with fulfillment, events, and responses; specific to a conversation state, so difficult to reuse | [Intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) are simplified to remove this coupling and made highly reusable  
Webhook error handling | Errors quietly ignored by agent, passed to API caller if present | Explicit [error event handling built-in](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) to your agent  
Event handling | Invoked [events](https://docs.cloud.google.com/dialogflow/docs/events-overview) trigger intent matches | [Events handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event) are built-in types with powerful controls.  
Conditional response messages | Requires webhook calls | Can be configured statically [in fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#cond), with static [conditions for a route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route), or with [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) calls  
Parameter scope | Can be scoped to [intent](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters), [context](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#param), or [event](https://docs.cloud.google.com/dialogflow/docs/events-overview#param) | Can be scoped to [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#intent), [form](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form), or [session](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#session)  
Built-in testing | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case)  
Redaction | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings)  
Conditional logic | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#cond)  
DTMF input | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf)  
System functions for advanced responses and conditions | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions)  
Advanced NLU | Not provided | [Provided](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-ml)  
Agents per project | 1 | 1000  
Recommended agent size | Up to medium size agents | Up to very large  
Recommended agent complexity | Up to moderately complex agents | Up to highly complex  
Learning curve to design a simple agent | Basic | Moderate  
Learning curve to design a complex agent | High | Moderate  
Pricing and quotas | Granular | Simplified  
  
## Edition comparison

You can use the following editions:

X | Item  
---|---  
Dialogflow ES Trial Edition | A no-cost edition that provides most of the features of the standard _Dialogflow ES agent_ type. It offers limited quota and support by community and email. This edition is suitable to experiment with Dialogflow ES.  
Dialogflow ES Essentials Edition | This is a pay-as-you-go edition that provides the standard _Dialogflow ES agent_ type. This edition offers production-ready quotas and support from Google Cloud support.  
Dialogflow CX Edition | This is a pay-as-you-go edition that provides the advanced _Dialogflow CX agent_ type. This edition offers production-ready quotas and support from Google Cloud support.  
  
The following tables provide a summary comparison for editions by agent type. For details, see [Pricing](https://cloud.google.com/products/conversational-agents/pricing) and [Quotas and Limits](https://docs.cloud.google.com/dialogflow/quotas).

###  Dialogflow CX Agent

Feature | Dialogflow CX Edition  
---|---  
**Text**  
(includes all DetectIntent, StreamingDetectIntent, and FulfillIntent requests that do not contain audio)  | 1200 requests per minute  
  
$0.007 per request  
**Audio input/output**  
(speech recognition, speech-to-text, STT, speech synthesis, text-to-speech, TTS, telephony)  | 600 requests per minute  
  
$0.06 per minute  
**Service Level Agreement** | [SLA](https://cloud.google.com/dialogflow/sla)  
**Support** | Eligible for [Cloud Support](https://docs.cloud.google.com/support) packages with committed response times for supporting production applications  
**Terms of Service** | [Google Cloud Platform ToS](https://cloud.google.com/terms/)  
  
###  Dialogflow ES Agent

Feature | Trial Edition | Essentials Edition  
---|---|---  
**Text**  
(includes all DetectIntent and StreamingDetectIntent requests that do not contain audio)  | Production-ready quota  
  
No charge | Production-ready quota  
  
$0.002 per request  
**Audio input**  
(also known as speech recognition, speech-to-text, STT)  | Limited quota  
  
No charge | Production-ready quota  
  
$0.0065 per 15 seconds of audio  
**Audio output**  
(also known as speech synthesis, text-to-speech, TTS)  | Limited quota  
  
No charge | Production-ready quota  
  
$4 to $16 per million characters  
**Knowledge connectors (Beta)** | Limited quota  
  
No charge | Production-ready quota  
  
No charge  
**Sentiment analysis** | Not available | Unlimited quota  
  
$0.25 to $1.00 per 1000 requests  
**Dialogflow ES phone gateway**  
Includes audio input and output.  | Toll-free number not available  
  
Limited quota  
  
No charge | Production-ready quota  
  
$0.05 to $0.06 per minute  
**Mega agent** | Limited quota  
  
No charge | Unlimited quota  
  
$0.002 to $0.006 per request  
**Service Level Agreement** | None | [SLA](https://cloud.google.com/dialogflow/sla)  
**Support** | Community support and via email | Eligible for [Cloud Support](https://docs.cloud.google.com/support) packages with committed response times for supporting production applications  
**Terms of Service** | [Dialogflow ES Trial Edition ToS](https://docs.cloud.google.com/dialogflow/docs/terms-trial-edition) | [Google Cloud Platform ToS](https://cloud.google.com/terms/)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
