---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.contextProperties/list/
title: Method: contextProperties.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:43.939610+00:00
---

# Method: contextProperties.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.contextProperties/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: contextProperties.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.contextProperties.list

Lists all context properties for a specific parent entity. Use this method to discover all custom data points associated with a case, alert, or integration component.

### HTTP request

`GET https://{endpoint}/v1/{parent}/contextProperties`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list ContextProperties for. Format: projects/{project}/locations/{location}/instances/{instance} projects/{project}/locations/{location}/instances/{instance}/cases/{case} projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{alert} projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/connectors/{connector} projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/jobs/{job}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of ContextProperties to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `contextProperties.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter to be applied over multiple ContextProperty fields.  
`orderBy` |  `string` Optional. The order in which items should be returned.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListContextPropertiesResponse](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ListContextPropertiesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.contextProperties.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
