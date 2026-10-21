---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/updateSemanticGovernancePolicyEngine/
title: Method: locations.updateSemanticGovernancePolicyEngine \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:37.496173+00:00
---

# Method: locations.updateSemanticGovernancePolicyEngine  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/updateSemanticGovernancePolicyEngine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.updateSemanticGovernancePolicyEngine Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.updateSemanticGovernancePolicyEngine

Updates a SemanticGovernancePolicyEngine.

This method performs an upsert operation. If the SemanticGovernancePolicyEngine resource does not exist, it will be created. Otherwise, it will be updated.

### Endpoint

patch  `https://{service-endpoint}/v1beta1/{semanticGovernancePolicyEngine.name}`   


`PATCH https://{service-endpoint}/v1beta1/{semanticGovernancePolicyEngine.name}`

Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`semanticGovernancePolicyEngine.name` `string` Identifier. The resource name of the SemanticGovernancePolicyEngine. Format: projects/{project}/locations/{location}/semanticGovernancePolicyEngine

### Query parameters

| `updateMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Specifies the fields to be overwritten in the SemanticGovernancePolicyEngine resource by the update. The fields specified in the updateMask are relative to the resource itself. If no updateMask is provided, all fields are overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Request body

The request body contains an instance of `[SemanticGovernancePolicyEngine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SemanticGovernancePolicyEngine)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-07-01 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
