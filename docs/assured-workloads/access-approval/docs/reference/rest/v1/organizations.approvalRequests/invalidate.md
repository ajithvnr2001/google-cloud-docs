---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/organizations.approvalRequests/invalidate/
title: Method: organizations.approvalRequests.invalidate \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:01.159236+00:00
---

# Method: organizations.approvalRequests.invalidate  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/organizations.approvalRequests/invalidate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/authentication)



Send feedback 

#  Method: organizations.approvalRequests.invalidate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest.

NOTE: This action revokes Google access based on this approval request. If the resource has other active approvals, access will remain granted.

Returns FAILED_PRECONDITION if the request exists but is not in an approved state.

### HTTP request

`POST https://accessapproval.googleapis.com/v1/{name=organizations/*/approvalRequests/*}:invalidate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Name of the ApprovalRequest to invalidate. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `accessapproval.requests.invalidate`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ApprovalRequest](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/folders.approvalRequests#ApprovalRequest)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-25 UTC."],[],[]] 
