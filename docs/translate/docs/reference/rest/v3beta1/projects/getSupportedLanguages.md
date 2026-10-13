---
url: https://docs.cloud.google.com/translate/docs/reference/rest/v3beta1/projects/getSupportedLanguages/
title: Method: projects.getSupportedLanguages \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:10.543952+00:00
---

# Method: projects.getSupportedLanguages  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/reference/rest/v3beta1/projects/getSupportedLanguages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ API and references ](https://docs.cloud.google.com/translate/docs/reference/api-overview)



Send feedback 

#  Method: projects.getSupportedLanguages Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Returns a list of supported languages for translation.

### HTTP request

`GET https://translate.googleapis.com/v3beta1/{parent=projects/*}/supportedLanguages`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Project or location to make a call. Must refer to a caller's project.Format: `projects/{project-number-or-id}` or `projects/{project-number-or-id}/locations/{location-id}`.For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`.Non-global location is required for AutoML models.Only models within the same region (have same location-id) can be used, otherwise an INVALID_ARGUMENT (400) error is returned.  
  
### Query parameters

Parameters  
---  
`displayLanguageCode` |  `string` Optional. The language to use to return localized, human readable names of supported languages. If missing, then display names are not returned in a response.  
`model` |  `string` Optional. Get supported languages of this model.The format depends on model type:

  * AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
  * General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,

Returns languages supported by the specified model. If missing, we get supported languages of Google general NMT model. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `model`:

  * `cloudtranslate.generalModels.get`
  * `automl.models.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[SupportedLanguages](https://docs.cloud.google.com/translate/docs/reference/rest/v3beta1/SupportedLanguages)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-translation`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
