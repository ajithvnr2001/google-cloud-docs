---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/create/
title: Method: projects.locations.memberships.rbacrolebindings.create \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:59.099694+00:00
---

# Method: projects.locations.memberships.rbacrolebindings.create  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/create/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.rbacrolebindings.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a Membership RBACRoleBinding.

### HTTP request

`POST https://gkehub.googleapis.com/v1/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the RBACRoleBinding will be created. Specified in the format `projects/*/locations/*/memberships/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.rbacrolebindings.create`

  
  
### Query parameters

Parameters  
---  
`rbacrolebindingId` |  `string` Required. Client chosen ID for the RBACRoleBinding. `rbacrolebindingId` must be a valid RFC 1123 compliant DNS label:

  1. At most 63 characters in length
  2. It must consist of lower case alphanumeric characters or `-`
  3. It must start and end with an alphanumeric character

Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.  
  
### Request body

The request body contains an instance of `[RBACRoleBinding](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
