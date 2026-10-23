---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/mergeVersionAliases/
title: Method: models.mergeVersionAliases \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:04.167680+00:00
---

# Method: models.mergeVersionAliases  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/mergeVersionAliases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.mergeVersionAliases Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.models.mergeVersionAliases

Merges a set of aliases for a Model version.

### Endpoint

post  `https://{service-endpoint}/v1/{name}:mergeVersionAliases`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The name of the model version to merge aliases, with a version id explicitly included.Example: `projects/{project}/locations/{location}/models/{model}@1234`

### Request body

The request body contains data with the following structure: | Fields  
  
`versionAliases[]` `string` Required. The set of version aliases to merge. The alias should be at most 128 characters, and match `[a-z][a-zA-Z0-9-]{0,126}[a-z-0-9]`. Add the `-` prefix to an alias means removing that alias from the version. `-` is NOT counted in the 128 characters. Example: `-golden` means removing the `golden` alias from the version.There is NO ordering in aliases, which means 1) The aliases returned from models.get API might not have the exactly same order from this models.mergeVersionAliases API. 2) Adding and deleting the same alias in the request is not recommended, and the 2 operations will be cancelled out.

### Response body

If successful, the response body contains an instance of `[Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.models.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
