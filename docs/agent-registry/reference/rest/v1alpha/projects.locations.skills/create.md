---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/create/
title: Method: projects.locations.skills.create \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:40.799600+00:00
---

# Method: projects.locations.skills.create  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.skills.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



=========================================================================

### Skills Collection APIs

Creates a Skill resource container, optionally publishing the initial SkillRevision inline in a single, atomic CRUD roundtrip.

### HTTP request

`POST https://agentregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/skills`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location location to bootstrap.  
  
### Query parameters

Parameters  
---  
`skillId` |  `string` Required. Custom, user-defined unique container identifier. Must be unique within the parent project and location. This value should be 4-64 characters, and valid characters are `/[a-z][0-9]-/`.  
`requestId` |  `string` Optional. Signed UUID request idempotency token.  
  
### Request body

The request body contains an instance of `[Skill](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#Skill)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/agent-registry/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skills.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
