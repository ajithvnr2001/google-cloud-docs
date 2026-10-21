---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models/copy/
title: Method: models.copy \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:26:38.877420+00:00
---

# Method: models.copy  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models/copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.copy Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.models.copy

Copies an already existing Agent Platform Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for `[Model.metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models#Model.FIELDS.metadata)` content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/models:copy`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`sourceModel` `string` Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}` | `encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec)`)` Customer-managed encryption key options. If this is set, then the Model copy will be encrypted with the provided encryption key. | `customServiceAccount` `string` Optional. The user-provided custom service account to use to do the copy model. If empty, [Agent Platform service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) will be used to access resources needed to upload the model. This account must belong to the destination project where the model is copied to, i.e., the project specified in the `parent` field of this request and have the Agent Platform service Agent role in the source project.Requires the user copying the Model to have the `iam.serviceAccounts.actAs` permission on this service account. | `destination_model` `Union type`  
  
If both fields are unset, a new Model will be created with a generated ID. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`modelId` `string` Optional. Copy sourceModel into a new Model with this id. The id will become the final component of the model resource name.This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen. | `parentModel` `string` Optional. Specify this field to copy sourceModel into this existing Model as a new version. Format: `projects/{project}/locations/{location}/models/{model}` End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-09-01 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
