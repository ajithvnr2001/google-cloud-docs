---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/patch/
title: Method: organizations.locations.workloads.patch \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:28.771205+00:00
---

# Method: organizations.locations.workloads.patch  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/patch/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates an existing workload. Currently allows updating of workload displayName and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

### HTTP request

`PATCH https://{endpoint}/v1/{workload.name=organizations/*/locations/*/workloads/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`workload.name` |  `string` Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload}Read-only.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#Workload)`.

### Response body

If successful, the response body contains an instance of `[Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#Workload)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `assuredworkloads.workload.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
