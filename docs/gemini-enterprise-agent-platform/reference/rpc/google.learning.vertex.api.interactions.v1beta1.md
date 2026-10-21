---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.learning.vertex.api.interactions.v1beta1
title: Package google.learning.vertex.api.interactions.v1beta1 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:12:59.724564+00:00
---

# Package google.learning.vertex.api.interactions.v1beta1  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.learning.vertex.api.interactions.v1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Package google.learning.vertex.api.interactions.v1beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[InteractionsService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.learning.vertex.api.interactions.v1beta1#google.learning.vertex.api.interactions.v1beta1.InteractionsService)` (interface)
  * `[VoicesHttpService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.learning.vertex.api.interactions.v1beta1#google.learning.vertex.api.interactions.v1beta1.VoicesHttpService)` (interface)
  * `[VoicesService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.learning.vertex.api.interactions.v1beta1#google.learning.vertex.api.interactions.v1beta1.VoicesService)` (interface)



## InteractionsService

API that allows users to interact with models and agents.

CancelInteraction  
---  
` rpc CancelInteraction(`[CancelInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CancelInteractionRequest)`) returns (`[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)`) ` Cancels an interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.cancel`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CancelInteractionHttp  
---  
` rpc CancelInteractionHttp(`[CancelInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CancelInteractionRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Cancels an interaction by id. This only applies to background interactions that are still running.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateInteraction  
---  
` rpc CreateInteraction(`[CreateInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionRequest)`) returns (`[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)`) ` Creates an interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateInteractionHttp  
---  
` rpc CreateInteractionHttp(`[CreateInteractionHttpRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionHttpRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Creates a new interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateInteractionStream  
---  
` rpc CreateInteractionStream(`[CreateInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionRequest)`) returns (`[InteractionStreamingEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStreamingEvent)`) ` Creates an interaction and streams the response.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteInteraction  
---  
This item is deprecated!` rpc DeleteInteraction(`[DeleteInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeleteInteractionRequest)`) returns (`[DeleteInteractionResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeleteInteractionResponse)`) ` Deletes an interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetInteraction  
---  
` rpc GetInteraction(`[GetInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionRequest)`) returns (`[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)`) ` Fully typed proto, unary version of GetInteraction that returns Interaction proto.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetInteractionHttp  
---  
` rpc GetInteractionHttp(`[GetInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Retrieves the full details of a single interaction based on its `Interaction.id`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetInteractionStream  
---  
` rpc GetInteractionStream(`[GetInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionRequest)`) returns (`[InteractionStreamingEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStreamingEvent)`) ` Fully typed proto, streaming version of GetInteraction that returns Interaction proto.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListInteractions  
---  
` rpc ListInteractions(`[ListInteractionsRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsRequest)`) returns (`[ListInteractionsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsResponse)`) ` List interactions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListInteractionsHttp  
---  
` rpc ListInteractionsHttp(`[ListInteractionsRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` List interactions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## VoicesHttpService

HTTP transcoder service for managing custom voices and listing available voices for Gemini TTS.

## VoicesService

Manages custom voices and lists available voices for Gemini TTS.

A voice is created either by _replication_ from a reference audio recording or by _prompting_ with a natural-language description. Created voices are referenced at synthesis time via `GenerationConfig.speech_config.voice_config.voice` (in `GenerateContent` / `BidiGenerateContent`) or `GenerationConfig.speech_config.voice` (in `CreateInteraction`).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-26 UTC."],[],[]] 
