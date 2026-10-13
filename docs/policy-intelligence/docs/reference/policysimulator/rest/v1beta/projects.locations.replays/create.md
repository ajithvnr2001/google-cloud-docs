---
url: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/projects.locations.replays/create/
title: Method: projects.locations.replays.create \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:40.184206+00:00
---

# Method: projects.locations.replays.create  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/projects.locations.replays/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  Method: projects.locations.replays.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates and starts a `[Replay](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays#Replay)` using the given `[ReplayConfig](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays#Replay.ReplayConfig)`.

### HTTP request

`POST https://policysimulator.googleapis.com/v1beta/{parent=projects/*/locations/*}/replays`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this `[Replay](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays#Replay)` will be created. This resource must be a project, folder, or organization with a location.Example: `projects/my-example-project/locations/global`  
  
### Request body

The request body contains an instance of `[Replay](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays#Replay)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `policysimulator.replays.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-16 UTC."],[],[]] 
