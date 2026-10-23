---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/reasoningEngines.ws.v1.projects.locations.reasoningEngines.revisions.runtimeRevisions.api/bidiInvokeReasoningEngine/
title: Method: api.bidiInvokeReasoningEngine \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:52.800522+00:00
---

# Method: api.bidiInvokeReasoningEngine  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/reasoningEngines.ws.v1.projects.locations.reasoningEngines.revisions.runtimeRevisions.api/bidiInvokeReasoningEngine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: api.bidiInvokeReasoningEngine Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : reasoningEngines.ws.v1.projects.locations.reasoningEngines.revisions.runtimeRevisions.api.bidiInvokeReasoningEngine

Invokes reasoning engine with arbitrary WebSocket requests for bidi streaming

### Endpoint

post  `https://{service-endpoint}/reasoningEngines/ws/v1/{name}/api/**`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Optional. The name of the ReasoningEngine. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}` or `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}/runtimeRevisions/{runtime_revision}`

### Request body

The request body contains an instance of `[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HttpBody)`.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `aiplatform.reasoningEngines.query`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
