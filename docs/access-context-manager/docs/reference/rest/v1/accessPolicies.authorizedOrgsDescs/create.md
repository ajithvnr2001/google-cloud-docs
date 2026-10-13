---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/create/
title: Method: accessPolicies.authorizedOrgsDescs.create \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:10.658519+00:00
---

# Method: accessPolicies.authorizedOrgsDescs.create  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Method: accessPolicies.authorizedOrgsDescs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates an `[authorized orgs desc](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs#AuthorizedOrgsDesc)`. The long-running operation from this RPC has a successful status after the `[authorized orgs desc](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs#AuthorizedOrgsDesc)` propagates to long-lasting storage. If a `[authorized orgs desc](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs#AuthorizedOrgsDesc)` contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation.

### HTTP request

`POST https://accesscontextmanager.googleapis.com/v1/{parent=accessPolicies/*}/authorizedOrgsDescs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name for the access policy which owns this `[Authorized Orgs Desc](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs#AuthorizedOrgsDesc)`.Format: `accessPolicies/{policyId}`  
  
### Request body

The request body contains an instance of `[AuthorizedOrgsDesc](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs#AuthorizedOrgsDesc)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `accesscontextmanager.authorizedOrgsDescs.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
