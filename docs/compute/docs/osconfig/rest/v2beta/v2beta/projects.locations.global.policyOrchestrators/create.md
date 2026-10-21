---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/projects.locations.global.policyOrchestrators/create/
title: Method: projects.locations.global.policyOrchestrators.create \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:21:02.349336+00:00
---

# Method: projects.locations.global.policyOrchestrators.create  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/projects.locations.global.policyOrchestrators/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



Send feedback 

#  Method: projects.locations.global.policyOrchestrators.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new policy orchestrator under the given project resource.

`name` field of the given orchestrator are ignored and instead replaced by a product of `parent` and `policyOrchestratorId`.

Orchestrator state field might be only set to `ACTIVE`, `STOPPED` or omitted (in which case, the created resource will be in `ACTIVE` state anyway).

### HTTP request

`POST https://osconfig.googleapis.com/v2beta/{parent=projects/*/locations/global}/policyOrchestrators`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name in the form of: * `organizations/{organization_id}/locations/global` * `folders/{folder_id}/locations/global` * `projects/{project_id_or_number}/locations/global`  
  
### Query parameters

Parameters  
---  
`policyOrchestratorId` |  `string` Required. The logical identifier of the policy orchestrator, with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the parent.

  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[PolicyOrchestrator](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
