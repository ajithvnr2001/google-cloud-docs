---
url: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews.operations/get/
title: Method: organizations.locations.orgPolicyViolationsPreviews.operations.get \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:17.601103+00:00
---

# Method: organizations.locations.orgPolicyViolationsPreviews.operations.get  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews.operations/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  Method: organizations.locations.orgPolicyViolationsPreviews.operations.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

### HTTP request

`GET https://policysimulator.googleapis.com/v1beta/{name=organizations/*/locations/*/orgPolicyViolationsPreviews/*/operations/**}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the operation resource.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-16 UTC."],[],[]] 
