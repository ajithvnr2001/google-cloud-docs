---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/create/
title: Method: caseCloseDefinitions.create \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:44.782761+00:00
---

# Method: caseCloseDefinitions.create  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseCloseDefinitions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.caseCloseDefinitions.create

Creates a new CaseCloseDefinition. Use this method to add a new pairing of root cause and reason to the system. Similar root cause and reason combinations cannot be duplicated.

### HTTP request

`POST https://{endpoint}/v1/{parent}/caseCloseDefinitions`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this CaseCloseDefinition will be created. Format: projects/{project}/locations/{location}/instances/{instance}/caseCloseDefinitions  
  
### Request body

The request body contains an instance of `[CaseCloseDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions#CaseCloseDefinition)`.

### Response body

If successful, the response body contains a newly created instance of `[CaseCloseDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions#CaseCloseDefinition)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.caseCloseDefinitions.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
