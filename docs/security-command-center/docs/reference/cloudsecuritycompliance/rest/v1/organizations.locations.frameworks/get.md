---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.frameworks/get/
title: Method: organizations.locations.frameworks.get \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:26.291816+00:00
---

# Method: organizations.locations.frameworks.get  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.frameworks/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.locations.frameworks.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Gets details about a framework. This method retrieves the latest major version of the framework.

To retrieve a specific major version, include `majorRevisionId` in the request.

### HTTP request

`GET https://cloudsecuritycompliance.googleapis.com/v1/{name=organizations/*/locations/*/frameworks/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the framework to retrieve, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`.The only supported location is `global`.  
  
### Query parameters

Parameters  
---  
`majorRevisionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The framework major version to retrieve. If not specified, the most recently updated `revision_id` is retrieved.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Framework](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.frameworks#Framework)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudsecuritycompliance.frameworks.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
