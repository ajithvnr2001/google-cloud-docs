---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators
title: REST Resource: organizations.locations.global.policyOrchestrators \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:08.292494+00:00
---

# REST Resource: organizations.locations.global.policyOrchestrators  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.global.policyOrchestrators Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PolicyOrchestrator
    * JSON representation
  * Methods



## Resource: PolicyOrchestrator

A policy orchestrator manages project-level and zone-level policy resources, such as OS policy assignments. It provides methods to create, update, and delete these resources across projects and locations at scale.

The policy orchestrator operates as a continuous loop. In each iteration, the orchestrator identifies the set of resources to be modified and progressively applies changes. If the set of resources changes over time (for example, if you add new projects), subsequent iterations address those changes.

The orchestrator can either upsert or delete policy resources. For more details, see the `action` and `orchestratedResource` fields.

The policy orchestrator does not manage the lifecycle of the resources it creates. Each iteration is independent and, besides Cloud Logging, the orchestrator retains only a minimal history of past actions. Deleting the orchestrator does not affect previously created resources; these resources remain in their current state. Similarly, removing projects from the orchestrator's scope does not affect existing resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "etag": string,
      "state": string,
      "reconciling": boolean,
      "orchestrationScope": {
        object ([OrchestrationScope](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationScope))
      },
      "action": string,
      "orchestratedResource": {
        object ([OrchestratedResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestratedResource))
      },
      "orchestrationState": {
        object ([OrchestrationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationState))
      },
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. In the following format: * `organizations/{organization_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `folders/{folder_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `projects/{project_id_or_number}/locations/global/policyOrchestrators/{orchestrator_id}`  
`description` |  `string` Optional. Freeform text describing the purpose of the resource.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`state` |  `string` Optional. State of the orchestrator. Can be updated to change orchestrator behaviour. Allowed values: - `ACTIVE` \- orchestrator is actively looking for actions to be taken. - `STOPPED` \- orchestrator won't make any changes.Note: There might be more states added in the future. We use string here instead of an enum, to avoid the need of propagating new states to all the client code.  
`reconciling` |  `boolean` Output only. Set to true, if there are ongoing changes being applied by the orchestrator.  
`orchestrationScope` |  `object (`[OrchestrationScope](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationScope)`)` Optional. Defines scope for the orchestration, in context of the enclosing PolicyOrchestrator resource.Scope is expanded into a list of <project, zone> pairs, in which the rollout action will take place. Expansion starts with a Folder resource parenting the PolicyOrchestrator resource: - All the descendant projects are listed. - List of project is cross joined with a list of all available zones. - Resulting list of <project, zone> pairs is filtered according to the selectors.  
`action` |  `string` Required. Action to be done by the orchestrator in `projects/{projectId}/zones/{zone_id}` locations defined by the `orchestrationScope`. Allowed values: - `UPSERT` \- Orchestrator will create or update target resources. - `DELETE` \- Orchestrator will delete target resources, if they exist  
`orchestratedResource` |  `object (`[OrchestratedResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestratedResource)`)` Required. Resource to be orchestrated by the policy orchestrator.  
`orchestrationState` |  `object (`[OrchestrationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationState)`)` Output only. State of the orchestration.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the policy orchestrator resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the policy orchestrator resource was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/create)`

|  Creates a new policy orchestrator under the given organizations resource.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/delete)`

|  Deletes an existing policy orchestrator resource, parented by an organization.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/get)`

|  Retrieves an existing policy orchestrator, parented by an organization.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/list)`

|  Lists the policy orchestrators under the given parent organization resource.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/patch)`

|  Updates an existing policy orchestrator, parented by an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
