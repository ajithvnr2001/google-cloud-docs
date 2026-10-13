---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/folders.approvalRequests/list/
title: Method: folders.approvalRequests.list \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:27.468296+00:00
---

# Method: folders.approvalRequests.list  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/folders.approvalRequests/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/authentication)



Send feedback 

#  Method: folders.approvalRequests.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

### HTTP request

`GET https://accessapproval.googleapis.com/v1/{parent=folders/*}/approvalRequests`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The parent resource. This may be "projects/{project}", "folders/{folder}", or "organizations/{organization}". Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `accessapproval.requests.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter on the type of approval requests to retrieve. Must be one of the following values:

  * [not set]: Requests that are pending or have active approvals.
  * ALL: All requests.
  * PENDING: Only pending requests.
  * ACTIVE: Only active (i.e. currently approved) requests.
  * DISMISSED: Only requests that have been dismissed, or requests that are not approved and past expiration.
  * EXPIRED: Only requests that have been approved, and the approval has expired.
  * HISTORY: Active, dismissed and expired requests.

  
`pageSize` |  `integer` Requested page size.  
`pageToken` |  `string` A token identifying the page of results to return.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListApprovalRequestsResponse](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/ListApprovalRequestsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-25 UTC."],[],[]] 
