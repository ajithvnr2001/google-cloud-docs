---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/organizations.locations.global.policyOrchestrators/patch/
title: Method: organizations.locations.global.policyOrchestrators.patch \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:54:39.296897+00:00
---

# Method: organizations.locations.global.policyOrchestrators.patch  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/organizations.locations.global.policyOrchestrators/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



Send feedback 

#  Method: organizations.locations.global.policyOrchestrators.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates an existing policy orchestrator, parented by an organization.

### HTTP request

`PATCH https://osconfig.googleapis.com/v2beta/{policyOrchestrator.name=organizations/*/locations/global/policyOrchestrators/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`policyOrchestrator.name` |  `string` Immutable. Identifier. In form of * `organizations/{organization_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `folders/{folder_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `projects/{project_id_or_number}/locations/global/policyOrchestrators/{orchestrator_id}`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[PolicyOrchestrator](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
