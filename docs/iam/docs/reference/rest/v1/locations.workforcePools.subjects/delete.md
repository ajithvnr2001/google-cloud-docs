---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/delete/
title: Method: locations.workforcePools.subjects.delete \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:52.098985+00:00
---

# Method: locations.workforcePools.subjects.delete  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: locations.workforcePools.subjects.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Deletes a `WorkforcePoolSubject`.

Subject must not already be in a deleted state.

A `WorkforcePoolSubject` is automatically created the first time an external credential is exchanged for a Google Cloud credential using a mapped `google.subject` attribute. There is no endpoint to manually create a `WorkforcePoolSubject`.

For 30 days after a `WorkforcePoolSubject` is deleted, using the same `google.subject` attribute in token exchanges with Google Cloud STS fails.

Call `[subjects.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject)` to undelete a `WorkforcePoolSubject` that has been deleted, within within 30 days of deleting it.

After 30 days, the `WorkforcePoolSubject` is permanently deleted. At this point, a token exchange with Google Cloud STS that uses the same mapped `google.subject` attribute automatically creates a new `WorkforcePoolSubject` that is unrelated to the previously deleted `WorkforcePoolSubject` but has the same `google.subject` value.

### HTTP request

`DELETE https://iam.googleapis.com/v1/{name=locations/*/workforcePools/*/subjects/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the `WorkforcePoolSubject`. Special characters, like `/` and `:`, must be escaped, because all URLs need to conform to the "When to Escape and Unescape" section of [RFC3986](https://www.ietf.org/rfc/rfc2396.txt).Format: `locations/{location}/workforcePools/{workforcePoolId}/subjects/{subject_id}`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
