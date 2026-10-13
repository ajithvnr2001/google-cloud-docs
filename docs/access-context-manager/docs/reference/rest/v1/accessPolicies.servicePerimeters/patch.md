---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/patch/
title: Method: accessPolicies.servicePerimeters.patch \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:03.361143+00:00
---

# Method: accessPolicies.servicePerimeters.patch  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Method: accessPolicies.servicePerimeters.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`. The long-running operation from this RPC has a successful status after the `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` propagates to long-lasting storage. If a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` contains errors, an error response is returned for the first error encountered.

### HTTP request

`PATCH https://accesscontextmanager.googleapis.com/v1/{servicePerimeter.name=accessPolicies/*/servicePerimeters/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`servicePerimeter.name` |  `string` Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{access_policy}/servicePerimeters/{servicePerimeter}`.The `servicePerimeter` component must begin with a letter, followed by alphanumeric characters or `_`.After you create a `ServicePerimeter`, you cannot change its `name`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Mask to control which fields get updated. Must be non-empty.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `accesscontextmanager.servicePerimeters.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
