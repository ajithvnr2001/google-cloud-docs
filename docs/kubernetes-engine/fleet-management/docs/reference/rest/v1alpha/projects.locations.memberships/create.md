---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/create/
title: Method: projects.locations.memberships.create \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:06.090022+00:00
---

# Method: projects.locations.memberships.create  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/create/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a new Membership.

**This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>.

### HTTP request

`POST https://gkehub.googleapis.com/v1alpha/{parent=projects/*/locations/*}/memberships`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the Memberships will be created. Specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.memberships.create`

  
  
### Query parameters

Parameters  
---  
`membershipId` |  `string` Required. Client chosen ID for the membership. `membershipId` must be a valid RFC 1123 compliant DNS label:

  1. At most 63 characters in length
  2. It must consist of lower case alphanumeric characters or `-`
  3. It must start and end with an alphanumeric character

Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.  
`requestId` |  `string` Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[Membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
