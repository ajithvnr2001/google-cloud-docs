---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators
title: REST Resource: folders.locations.global.policyOrchestrators \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:00.295956+00:00
---

# REST Resource: folders.locations.global.policyOrchestrators  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: folders.locations.global.policyOrchestrators Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PolicyOrchestrator
    * JSON representation
    * OrchestrationScope
      * JSON representation
    * Selector
      * JSON representation
    * ResourceHierarchySelector
      * JSON representation
    * LocationSelector
      * JSON representation
    * OrchestratedResource
      * JSON representation
    * OrchestrationState
      * JSON representation
    * IterationState
      * JSON representation
    * State
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
  
### OrchestrationScope

Defines a set of selectors which drive which resources are in scope of policy orchestration.

JSON representation  
---  
      
    
    {
      "selectors": [
        {
          object ([Selector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Selector))
        }
      ]
    }  
  
Fields  
---  
`selectors[]` |  `object (`[Selector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Selector)`)` Optional. Selectors of the orchestration scope. There is a logical AND between each selector defined.When there is no explicit `ResourceHierarchySelector` selector specified, the scope is by default bounded to the parent of the policy orchestrator resource.  
  
### Selector

Selector for the resources in scope of orchestration.

JSON representation  
---  
      
    
    {
    
      // Union field selector_type can be only one of the following:
      "resourceHierarchySelector": {
        object ([ResourceHierarchySelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceHierarchySelector))
      },
      "locationSelector": {
        object ([LocationSelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LocationSelector))
      }
      // End of list of possible types for union field selector_type.
    }  
  
Fields  
---  
Union field `selector_type`. Type of Selector to be used for rollouts. `selector_type` can be only one of the following:  
`resourceHierarchySelector` |  `object (`[ResourceHierarchySelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceHierarchySelector)`)` Selector for selecting resource hierarchy.  
`locationSelector` |  `object (`[LocationSelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LocationSelector)`)` Selector for selecting locations.  
  
### ResourceHierarchySelector

Selector containing Cloud Resource Manager resource hierarchy nodes.

JSON representation  
---  
      
    
    {
      "includedProjects": [
        string
      ],
      "includedFolders": [
        string
      ]
    }  
  
Fields  
---  
`includedProjects[]` |  `string` Optional. Names of the projects in scope. Format: `projects/{project_number}`  
`includedFolders[]` |  `string` Optional. Names of the folders in scope. Format: `folders/{folder_id}`  
  
### LocationSelector

Selector containing locations in scope.

JSON representation  
---  
      
    
    {
      "includedLocations": [
        string
      ]
    }  
  
Fields  
---  
`includedLocations[]` |  `string` Optional. Names of the locations in scope. Format: `us-central1-a`  
  
### OrchestratedResource

Represents a resource that is being orchestrated by the policy orchestrator.

JSON representation  
---  
      
    
    {
      "id": string,
    
      // Union field payload can be only one of the following:
      "osPolicyAssignmentV1Payload": {
        object ([OSPolicyAssignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment))
      }
      // End of list of possible types for union field payload.
    }  
  
Fields  
---  
`id` |  `string` Optional. ID of the resource to be used while generating set of affected resources.For UPSERT action the value is auto-generated during PolicyOrchestrator creation when not set. When the value is set it should following next restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

For DELETE action, ID must be specified explicitly during PolicyOrchestrator creation.  
Union field `payload`. For UPSERT action, payload represents a type and content of the resource that will be created/updated for a particular <project, zone> pair from orchestration scope.For DELETE action, a payload must be set to indicate type of the resource that will be deleted. It can be either: - an empty message, - a correct resource content. `payload` can be only one of the following:  
`osPolicyAssignmentV1Payload` |  `object (`[OSPolicyAssignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment)`)` Optional. OSPolicyAssignment resource to be created, updated or deleted. Name field is ignored and replace with a generated value.With this field set, orchestrator will perform actions on `project/{project}/locations/{zone}/osPolicyAssignments/{resource_id}` resources, where `project` and `zone` pairs come from the expanded scope, and `resource_id` comes from the `resource_id` field of orchestrator resource.  
  
### OrchestrationState

Describes the state of the orchestration process.

JSON representation  
---  
      
    
    {
      "currentIterationState": {
        object ([IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState))
      },
      "previousIterationState": {
        object ([IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState))
      }
    }  
  
Fields  
---  
`currentIterationState` |  `object (`[IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState)`)` Output only. Current Wave iteration state.  
`previousIterationState` |  `object (`[IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState)`)` Output only. Previous Wave iteration state.  
  
### IterationState

Describes the state of a single iteration of the orchestrator.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.State)),
      "iterationId": string,
      "progress": number,
      "performedActions": string,
      "failedActions": string,
      "startTime": string,
      "finishTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/ListOperationsResponse#Status))
      }
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator.State)`)` Output only. State of the iteration.  
`iterationId` |  `string` Output only. Unique identifier of the iteration.  
`progress` |  `number` Output only. An estimated percentage of the progress. Number between 0 and 100.  
`performedActions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Overall number of actions done by the orchestrator so far.  
`failedActions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of orchestration actions which failed so far. For more details, query the Cloud Logs.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Start time of the wave iteration.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`finishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Finish time of the wave iteration.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Error thrown in the wave iteration.  
  
### State

Possible states of the iteration.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`PROCESSING` | Iteration is in progress.  
`COMPLETED` | Iteration completed, with all actions being successful.  
`FAILED` | Iteration completed, with failures.  
`CANCELLED` | Iteration was explicitly cancelled.  
`UNKNOWN` | Impossible to determine current state of the iteration.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/create)`

|  Creates a new policy orchestrator under the given folder resource.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/delete)`

|  Deletes an existing policy orchestrator resource, parented by a folder.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/get)`

|  Retrieves an existing policy orchestrator, parented by a folder.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/list)`

|  Lists the policy orchestrators under the given parent folder resource.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/patch)`

|  Updates an existing policy orchestrator, parented by a folder.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
