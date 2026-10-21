---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/projects.locations.global.policyOrchestrators
title: REST Resource: projects.locations.global.policyOrchestrators \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:21:51.343365+00:00
---

# REST Resource: projects.locations.global.policyOrchestrators  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/projects.locations.global.policyOrchestrators

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



Send feedback 

#  REST Resource: projects.locations.global.policyOrchestrators Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PolicyOrchestrator
    * JSON representation
  * Methods



## Resource: PolicyOrchestrator

PolicyOrchestrator helps managing project+zone level policy resources (e.g. OS Policy Assignments), by providing tools to create, update and delete them across projects and locations, at scale.

Policy orchestrator functions as an endless loop. Each iteration orchestrator computes a set of resources that should be affected, then progressively applies changes to them. If for some reason this set of resources changes over time (e.g. new projects are added), the future loop iterations will address that.

Orchestrator can either upsert or delete policy resources. For more details, see the description of the `action`, and `orchestratedResource` fields.

Note that policy orchestrator do not "manage" the resources it creates. Every iteration is independent and only minimal history of past actions is retained (apart from Cloud Logging). If orchestrator gets deleted, it does not affect the resources it created in the past. Those will remain where they were. Same applies if projects are removed from the orchestrator's scope.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "etag": string,
      "state": string,
      "reconciling": boolean,
      "orchestrationScope": {
        object ([OrchestrationScope](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationScope))
      },
      "action": string,
      "orchestratedResource": {
        object ([OrchestratedResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestratedResource))
      },
      "orchestrationState": {
        object ([OrchestrationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationState))
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
`name` |  `string` Immutable. Identifier. In form of * `organizations/{organization_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `folders/{folder_id}/locations/global/policyOrchestrators/{orchestrator_id}` * `projects/{project_id_or_number}/locations/global/policyOrchestrators/{orchestrator_id}`  
`description` |  `string` Optional. Freeform text describing the purpose of the resource.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`state` |  `string` Optional. State of the orchestrator. Can be updated to change orchestrator behaviour. Allowed values: - `ACTIVE` \- orchestrator is actively looking for actions to be taken. - `STOPPED` \- orchestrator won't make any changes.Note: There might be more states added in the future. We use string here instead of an enum, to avoid the need of propagating new states to all the client code.  
`reconciling` |  `boolean` Output only. Set to true, if the there are ongoing changes being applied by the orchestrator.  
`orchestrationScope` |  `object (`[OrchestrationScope](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationScope)`)` Optional. Defines scope for the orchestration, in context of the enclosing PolicyOrchestrator resource.Scope is expanded into a list of <project, zone> pairs, in which the rollout action will take place. Expansion starts with a Folder resource parenting the PolicyOrchestrator resource: - All the descendant projects are listed. - List of project is cross joined with a list of all available zones. - Resulting list of <project, zone> pairs is filtered according to the selectors.  
`action` |  `string` Required. Action to be done by the orchestrator in `projects/{projectId}/zones/{zone_id}` locations defined by the `orchestrationScope`. Allowed values: - `UPSERT` \- Orchestrator will create or update target resources. - `DELETE` \- Orchestrator will delete target resources, if they exist  
`orchestratedResource` |  `object (`[OrchestratedResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestratedResource)`)` Required. Resource to be orchestrated by the policy orchestrator.  
`orchestrationState` |  `object (`[OrchestrationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OrchestrationState)`)` Output only. State of the orchestration.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the policy orchestrator resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the policy orchestrator resource was last modified.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/create)`

|  Creates a new policy orchestrator under the given project resource.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/delete)`

|  Deletes an existing policy orchestrator resource, parented by a project.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/get)`

|  Retrieves an existing policy orchestrator, parented by a project.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/list)`

|  Lists the policy orchestrators under the given parent project resource.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/patch)`

|  Updates an existing policy orchestrator, parented by a project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
