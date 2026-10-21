---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/folders.locations.global.policyOrchestrators
title: REST Resource: folders.locations.global.policyOrchestrators \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:19:22.222480+00:00
---

# REST Resource: folders.locations.global.policyOrchestrators  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/v2beta/folders.locations.global.policyOrchestrators

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



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
    * OSPolicyAssignment
      * JSON representation
    * OSPolicy
      * JSON representation
    * Mode
    * ResourceGroup
      * JSON representation
    * InventoryFilter
      * JSON representation
    * Resource
      * JSON representation
    * PackageResource
      * JSON representation
    * DesiredState
    * APT
      * JSON representation
    * Deb
      * JSON representation
    * File
      * JSON representation
    * Remote
      * JSON representation
    * Gcs
      * JSON representation
    * YUM
      * JSON representation
    * Zypper
      * JSON representation
    * RPM
      * JSON representation
    * GooGet
      * JSON representation
    * MSI
      * JSON representation
    * RepositoryResource
      * JSON representation
    * AptRepository
      * JSON representation
    * ArchiveType
    * YumRepository
      * JSON representation
    * ZypperRepository
      * JSON representation
    * GooRepository
      * JSON representation
    * ExecResource
      * JSON representation
    * Exec
      * JSON representation
    * Interpreter
    * FileResource
      * JSON representation
    * DesiredState
    * InstanceFilter
      * JSON representation
    * LabelSet
      * JSON representation
    * Inventory
      * JSON representation
    * Rollout
      * JSON representation
    * FixedOrPercent
      * JSON representation
    * RolloutState
    * OrchestrationState
      * JSON representation
    * IterationState
      * JSON representation
    * State
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
  
### OrchestrationScope

Defines a set of selectors which drive which resources are in scope of policy orchestration.

JSON representation  
---  
      
    
    {
      "selectors": [
        {
          object ([Selector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Selector))
        }
      ]
    }  
  
Fields  
---  
`selectors[]` |  `object (`[Selector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Selector)`)` Optional. Selectors of the orchestration scope. There is a logical AND between each selector defined.When there is no explicit `ResourceHierarchySelector` selector specified, the scope is by default bounded to the parent of the policy orchestrator resource.  
  
### Selector

Selector for the resources in scope of orchestration.

JSON representation  
---  
      
    
    {
    
      // Union field selector_type can be only one of the following:
      "resourceHierarchySelector": {
        object ([ResourceHierarchySelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceHierarchySelector))
      },
      "locationSelector": {
        object ([LocationSelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LocationSelector))
      }
      // End of list of possible types for union field selector_type.
    }  
  
Fields  
---  
Union field `selector_type`. Type of Selector to be used for rollouts. `selector_type` can be only one of the following:  
`resourceHierarchySelector` |  `object (`[ResourceHierarchySelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceHierarchySelector)`)` Selector for selecting resource hierarchy.  
`locationSelector` |  `object (`[LocationSelector](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LocationSelector)`)` Selector for selecting locations.  
  
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
        object ([OSPolicyAssignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OSPolicyAssignment))
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
`osPolicyAssignmentV1Payload` |  `object (`[OSPolicyAssignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OSPolicyAssignment)`)` Optional. OSPolicyAssignment resource to be created, updated or deleted. Name field is ignored and replace with a generated value.With this field set, orchestrator will perform actions on `project/{project}/locations/{zone}/osPolicyAssignments/{resource_id}` resources, where `project` and `zone` pairs come from the expanded scope, and `resource_id` comes from the `resource_id` field of orchestrator resource.  
  
### OSPolicyAssignment

OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances.

An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script.

For more information about the OS policy resource definitions and examples, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "osPolicies": [
        {
          object ([OSPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OSPolicy))
        }
      ],
      "instanceFilter": {
        object ([InstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.InstanceFilter))
      },
      "rollout": {
        object ([Rollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Rollout))
      },
      "revisionId": string,
      "revisionCreateTime": string,
      "etag": string,
      "rolloutState": enum ([RolloutState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RolloutState)),
      "baseline": boolean,
      "deleted": boolean,
      "reconciling": boolean,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Resource name.Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{osPolicyAssignmentId}`This field is ignored when you create an OS policy assignment.  
`description` |  `string` OS policy assignment description. Length of the description is limited to 1024 characters.  
`osPolicies[]` |  `object (`[OSPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.OSPolicy)`)` Required. List of OS policies to be applied to the VMs.  
`instanceFilter` |  `object (`[InstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.InstanceFilter)`)` Required. Filter to select VMs.  
`rollout` |  `object (`[Rollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Rollout)`)` Required. Rollout to deploy the OS policy assignment. A rollout is triggered in the following situations: 1) OSPolicyAssignment is created. 2) OSPolicyAssignment is updated and the update contains changes to one of the following fields: - instanceFilter - osPolicies 3) OSPolicyAssignment is deleted.  
`revisionId` |  `string` Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment  
`revisionCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the revision was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`etag` |  `string` The etag for this OS policy assignment. If this is provided on update, it must match the server's etag.  
`rolloutState` |  `enum (`[RolloutState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RolloutState)`)` Output only. OS policy assignment rollout state  
`baseline` |  `boolean` Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision.For a given OS policy assignment, there is only one revision with a value of `true` for this field.  
`deleted` |  `boolean` Output only. Indicates that this revision deletes the OS policy assignment.  
`reconciling` |  `boolean` Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rolloutState` is one of: * IN_PROGRESS * CANCELLING  
`uid` |  `string` Output only. Server generated unique id for the OS policy assignment resource.  
  
### OSPolicy

An OS policy defines the desired state configuration for a VM.

JSON representation  
---  
      
    
    {
      "id": string,
      "description": string,
      "mode": enum ([Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Mode)),
      "resourceGroups": [
        {
          object ([ResourceGroup](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceGroup))
        }
      ],
      "allowNoResourceGroupMatch": boolean
    }  
  
Fields  
---  
`id` |  `string` Required. The id of the OS policy with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the assignment.

  
`description` |  `string` Policy description. Length of the description is limited to 1024 characters.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Mode)`)` Required. Policy mode  
`resourceGroups[]` |  `object (`[ResourceGroup](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ResourceGroup)`)` Required. List of resource groups for the policy. For a particular VM, resource groups are evaluated in the order specified and the first resource group that is applicable is selected and the rest are ignored.If none of the resource groups are applicable for a VM, the VM is considered to be non-compliant w.r.t this policy. This behavior can be toggled by the flag `allowNoResourceGroupMatch`  
`allowNoResourceGroupMatch` |  `boolean` This flag determines the OS policy compliance status when none of the resource groups within the policy are applicable for a VM. Set this value to `true` if the policy needs to be reported as compliant even if the policy has nothing to validate or enforce.  
  
### Mode

Policy mode

Enums  
---  
`MODE_UNSPECIFIED` | Invalid mode  
`VALIDATION` | This mode checks if the configuration resources in the policy are in their desired state. No actions are performed if they are not in the desired state. This mode is used for reporting purposes.  
`ENFORCEMENT` | This mode checks if the configuration resources in the policy are in their desired state, and if not, enforces the desired state.  
  
### ResourceGroup

Resource groups provide a mechanism to group OS policy resources.

Resource groups enable OS policy authors to create a single OS policy to be applied to VMs running different operating Systems.

When the OS policy is applied to a target VM, the appropriate resource group within the OS policy is selected based on the `OSFilter` specified within the resource group.

JSON representation  
---  
      
    
    {
      "inventoryFilters": [
        {
          object ([InventoryFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.InventoryFilter))
        }
      ],
      "resources": [
        {
          object ([Resource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Resource))
        }
      ]
    }  
  
Fields  
---  
`inventoryFilters[]` |  `object (`[InventoryFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.InventoryFilter)`)` List of inventory filters for the resource group.The resources in this resource group are applied to the target VM if it satisfies at least one of the following inventory filters.For example, to apply this resource group to VMs running either `RHEL` or `CentOS` operating systems, specify 2 items for the list with following values: inventoryFilters[0].os_short_name='rhel' and inventoryFilters[1].os_short_name='centos'If the list is empty, this resource group will be applied to the target VM unconditionally.  
`resources[]` |  `object (`[Resource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Resource)`)` Required. List of resources configured for this resource group. The resources are executed in the exact order specified here.  
  
### InventoryFilter

Filtering criteria to select VMs based on inventory details.

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string
    }  
  
Fields  
---  
`osShortName` |  `string` Required. The OS short name  
`osVersion` |  `string` The OS versionPrefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*`An empty string matches all OS versions.  
  
### Resource

An OS policy resource is used to define the desired state configuration and provides a specific functionality like installing/removing packages, executing a script etc.

The system ensures that resources are always in their desired state by taking necessary actions if they have drifted from their desired state.

JSON representation  
---  
      
    
    {
      "id": string,
    
      // Union field resource_type can be only one of the following:
      "pkg": {
        object ([PackageResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.PackageResource))
      },
      "repository": {
        object ([RepositoryResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RepositoryResource))
      },
      "exec": {
        object ([ExecResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ExecResource))
      },
      "file": {
        object ([FileResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.FileResource))
      }
      // End of list of possible types for union field resource_type.
    }  
  
Fields  
---  
`id` |  `string` Required. The id of the resource with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the OS policy.

  
Union field `resource_type`. Resource type. `resource_type` can be only one of the following:  
`pkg` |  `object (`[PackageResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.PackageResource)`)` Package resource  
`repository` |  `object (`[RepositoryResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RepositoryResource)`)` Package repository resource  
`exec` |  `object (`[ExecResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ExecResource)`)` Exec resource  
`file` |  `object (`[FileResource](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.FileResource)`)` File resource  
  
### PackageResource

A resource that manages a system package.

JSON representation  
---  
      
    
    {
      "desiredState": enum ([DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.DesiredState)),
    
      // Union field system_package can be only one of the following:
      "apt": {
        object ([APT](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.APT))
      },
      "deb": {
        object ([Deb](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Deb))
      },
      "yum": {
        object ([YUM](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.YUM))
      },
      "zypper": {
        object ([Zypper](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Zypper))
      },
      "rpm": {
        object ([RPM](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RPM))
      },
      "googet": {
        object ([GooGet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.GooGet))
      },
      "msi": {
        object ([MSI](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.MSI))
      }
      // End of list of possible types for union field system_package.
    }  
  
Fields  
---  
`desiredState` |  `enum (`[DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.DesiredState)`)` Required. The desired state the agent should maintain for this package.  
Union field `system_package`. A system package. `system_package` can be only one of the following:  
`apt` |  `object (`[APT](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.APT)`)` A package managed by Apt.  
`deb` |  `object (`[Deb](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Deb)`)` A deb package file.  
`yum` |  `object (`[YUM](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.YUM)`)` A package managed by YUM.  
`zypper` |  `object (`[Zypper](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Zypper)`)` A package managed by Zypper.  
`rpm` |  `object (`[RPM](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.RPM)`)` An rpm package file.  
`googet` |  `object (`[GooGet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.GooGet)`)` A package managed by GooGet.  
`msi` |  `object (`[MSI](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.MSI)`)` An MSI package.  
  
### DesiredState

The desired state that the OS Config agent maintains on the VM.

Enums  
---  
`DESIRED_STATE_UNSPECIFIED` | Unspecified is invalid.  
`INSTALLED` | Ensure that the package is installed.  
`REMOVED` | The agent ensures that the package is not installed and uninstalls it if detected.  
  
### APT

A package managed by APT. - install: `apt-get update && apt-get -y install [name]` \- remove: `apt-get -y remove [name]`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
### Deb

A deb package file. dpkg packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File))
      },
      "pullDeps": boolean
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File)`)` Required. A deb package.  
`pullDeps` |  `boolean` Whether dependencies should also be installed. - install when false: `dpkg -i package` \- install when true: `apt-get update && apt-get -y install package.deb`  
  
### File

A remote or local file.

JSON representation  
---  
      
    
    {
      "allowInsecure": boolean,
    
      // Union field type can be only one of the following:
      "remote": {
        object ([Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Remote))
      },
      "gcs": {
        object ([Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Gcs))
      },
      "localPath": string
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`allowInsecure` |  `boolean` Defaults to false. When false, files are subject to validations based on the file type:Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
Union field `type`. A specific type of file. `type` can be only one of the following:  
`remote` |  `object (`[Remote](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Remote)`)` A generic remote file.  
`gcs` |  `object (`[Gcs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Gcs)`)` A Cloud Storage object.  
`localPath` |  `string` A local path within the VM to use.  
  
### Remote

Specifies a file available via some URI.

JSON representation  
---  
      
    
    {
      "uri": string,
      "sha256Checksum": string
    }  
  
Fields  
---  
`uri` |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`sha256Checksum` |  `string` SHA256 checksum of the remote file.  
  
### Gcs

Specifies a file available as a Cloud Storage Object.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "object": string,
      "generation": string
    }  
  
Fields  
---  
`bucket` |  `string` Required. Bucket of the Cloud Storage object.  
`object` |  `string` Required. Name of the Cloud Storage object.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Generation number of the Cloud Storage object.  
  
### YUM

A package managed by YUM. - install: `yum -y install package` \- remove: `yum -y remove package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
### Zypper

A package managed by Zypper. - install: `zypper -y install package` \- remove: `zypper -y rm package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
### RPM

An RPM package file. RPM packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File))
      },
      "pullDeps": boolean
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File)`)` Required. An rpm package.  
`pullDeps` |  `boolean` Whether dependencies should also be installed. - install when false: `rpm --upgrade --replacepkgs package.rpm` \- install when true: `yum -y install package.rpm` or `zypper -y install package.rpm`  
  
### GooGet

A package managed by GooGet. - install: `googet -noconfirm install package` \- remove: `googet -noconfirm remove package`

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Package name.  
  
### MSI

An MSI package. MSI packages only support INSTALLED state.

JSON representation  
---  
      
    
    {
      "source": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File))
      },
      "properties": [
        string
      ]
    }  
  
Fields  
---  
`source` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File)`)` Required. The MSI package.  
`properties[]` |  `string` Additional properties to use during installation. This should be in the format of Property=Setting. Appended to the defaults of `ACTION=INSTALL REBOOT=ReallySuppress`.  
  
### RepositoryResource

A resource that manages a package repository.

JSON representation  
---  
      
    
    {
    
      // Union field repository can be only one of the following:
      "apt": {
        object ([AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.AptRepository))
      },
      "yum": {
        object ([YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.YumRepository))
      },
      "zypper": {
        object ([ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ZypperRepository))
      },
      "goo": {
        object ([GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.GooRepository))
      }
      // End of list of possible types for union field repository.
    }  
  
Fields  
---  
Union field `repository`. A specific type of repository. `repository` can be only one of the following:  
`apt` |  `object (`[AptRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.AptRepository)`)` An Apt Repository.  
`yum` |  `object (`[YumRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.YumRepository)`)` A Yum Repository.  
`zypper` |  `object (`[ZypperRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ZypperRepository)`)` A Zypper Repository.  
`goo` |  `object (`[GooRepository](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.GooRepository)`)` A Goo Repository.  
  
### AptRepository

Represents a single apt package repository. These will be added to a repo file that will be managed at `/etc/apt/sources.list.d/google_osconfig.list`.

JSON representation  
---  
      
    
    {
      "archiveType": enum ([ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ArchiveType)),
      "uri": string,
      "distribution": string,
      "components": [
        string
      ],
      "gpgKey": string
    }  
  
Fields  
---  
`archiveType` |  `enum (`[ArchiveType](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.ArchiveType)`)` Required. Type of archive files in this repository.  
`uri` |  `string` Required. URI for this repository.  
`distribution` |  `string` Required. Distribution of this repository.  
`components[]` |  `string` Required. List of components for this repository. Must contain at least one item.  
`gpgKey` |  `string` URI of the key file for this repository. The agent maintains a keyring at `/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg`.  
  
### ArchiveType

Type of archive.

Enums  
---  
`ARCHIVE_TYPE_UNSPECIFIED` | Unspecified is invalid.  
`DEB` | Deb indicates that the archive contains binary files.  
`DEB_SRC` | Deb-src indicates that the archive contains source files.  
  
### YumRepository

Represents a single yum package repository. These are added to a repo file that is managed at `/etc/yum.repos.d/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "baseUrl": string,
      "gpgKeys": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the yum config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for resource conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
### ZypperRepository

Represents a single zypper package repository. These are added to a repo file that is managed at `/etc/zypp/repos.d/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "baseUrl": string,
      "gpgKeys": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the zypper config file and also the `displayName` if `displayName` is omitted. This id is also used as the unique identifier when checking for GuestPolicy conflicts.  
`displayName` |  `string` The display name of the repository.  
`baseUrl` |  `string` Required. The location of the repository directory.  
`gpgKeys[]` |  `string` URIs of GPG keys.  
  
### GooRepository

Represents a Goo package repository. These are added to a repo file that is managed at `C:/ProgramData/GooGet/repos/google_osconfig.repo`.

JSON representation  
---  
      
    
    {
      "name": string,
      "url": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the repository.  
`url` |  `string` Required. The url of the repository.  
  
### ExecResource

A resource that allows executing scripts on the VM.

The `ExecResource` has 2 stages: `validate` and `enforce` and both stages accept a script as an argument to execute.

When the `ExecResource` is applied by the agent, it first executes the script in the `validate` stage. The `validate` stage can signal that the `ExecResource` is already in the desired state by returning an exit code of `100`. If the `ExecResource` is not in the desired state, it should return an exit code of `101`. Any other exit code returned by this stage is considered an error.

If the `ExecResource` is not in the desired state based on the exit code from the `validate` stage, the agent proceeds to execute the script from the `enforce` stage. If the `ExecResource` is already in the desired state, the `enforce` stage will not be run. Similar to `validate` stage, the `enforce` stage should return an exit code of `100` to indicate that the resource in now in its desired state. Any other exit code is considered an error.

NOTE: An exit code of `100` was chosen over `0` (and `101` vs `1`) to have an explicit indicator of `in desired state`, `not in desired state` and errors. Because, for example, Powershell will always return an exit code of `0` unless an `exit` statement is provided in the script. So, for reasons of consistency and being explicit, exit codes `100` and `101` were chosen.

JSON representation  
---  
      
    
    {
      "validate": {
        object ([Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Exec))
      },
      "enforce": {
        object ([Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Exec))
      }
    }  
  
Fields  
---  
`validate` |  `object (`[Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Exec)`)` Required. What to run to validate this resource is in the desired state. An exit code of 100 indicates "in desired state", and exit code of 101 indicates "not in desired state". Any other exit code indicates a failure running validate.  
`enforce` |  `object (`[Exec](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Exec)`)` What to run to bring this resource into the desired state. An exit code of 100 indicates "success", any other exit code indicates a failure running enforce.  
  
### Exec

A file or script to execute.

JSON representation  
---  
      
    
    {
      "args": [
        string
      ],
      "interpreter": enum ([Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Interpreter)),
      "outputFilePath": string,
    
      // Union field source can be only one of the following:
      "file": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File))
      },
      "script": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`args[]` |  `string` Optional arguments to pass to the source during execution.  
`interpreter` |  `enum (`[Interpreter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Interpreter)`)` Required. The script interpreter to use.  
`outputFilePath` |  `string` Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 500K bytes.  
Union field `source`. What to execute. `source` can be only one of the following:  
`file` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File)`)` A remote or local file.  
`script` |  `string` An inline script. The size of the script is limited to 32KiB.  
  
### Interpreter

The interpreter to use.

Enums  
---  
`INTERPRETER_UNSPECIFIED` | Invalid value, the request will return validation error.  
`NONE` | If an interpreter is not specified, the source is executed directly. This execution, without an interpreter, only succeeds for executables and scripts that have [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)).  
`SHELL` | Indicates that the script runs with `/bin/sh` on Linux and `cmd.exe` on Windows.  
`POWERSHELL` | Indicates that the script runs with PowerShell.  
  
### FileResource

A resource that manages the state of a file.

JSON representation  
---  
      
    
    {
      "path": string,
      "state": enum ([DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.DesiredState_1)),
      "permissions": string,
    
      // Union field source can be only one of the following:
      "file": {
        object ([File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File))
      },
      "content": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`path` |  `string` Required. The absolute path of the file within the VM.  
`state` |  `enum (`[DesiredState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.DesiredState_1)`)` Required. Desired state of the file.  
`permissions` |  `string` Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4  
Union field `source`. The source for the contents of the file. `source` can be only one of the following:  
`file` |  `object (`[File](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.File)`)` A remote or local source.  
`content` |  `string` A a file with this content. The size of the content is limited to 32KiB.  
  
### DesiredState

Desired state of the file.

Enums  
---  
`DESIRED_STATE_UNSPECIFIED` | Unspecified is invalid.  
`PRESENT` | Ensure file at path is present.  
`ABSENT` | Ensure file at path is absent.  
`CONTENTS_MATCH` | Ensure the contents of the file at path matches. If the file does not exist it will be created.  
  
### InstanceFilter

Filters to select target VMs for an assignment.

If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them.

JSON representation  
---  
      
    
    {
      "all": boolean,
      "inclusionLabels": [
        {
          object ([LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LabelSet))
        }
      ],
      "exclusionLabels": [
        {
          object ([LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LabelSet))
        }
      ],
      "inventories": [
        {
          object ([Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Inventory))
        }
      ]
    }  
  
Fields  
---  
`all` |  `boolean` Target all VMs in the project. If true, no other criteria is permitted.  
`inclusionLabels[]` |  `object (`[LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LabelSet)`)` List of label sets used for VM inclusion.If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.  
`exclusionLabels[]` |  `object (`[LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.LabelSet)`)` List of label sets used for VM exclusion.If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.  
`inventories[]` |  `object (`[Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.Inventory)`)` List of inventories to select VMs.A VM is selected if its inventory data matches at least one of the following inventories.  
  
### LabelSet

Message representing label set. * A label is a key value pair set for a VM. * A LabelSet is a set of labels. * Labels within a LabelSet are ANDed. In other words, a LabelSet is applicable for a VM only if it matches all the labels in the LabelSet. * Example: A LabelSet with 2 labels: `env=prod` and `type=webserver` will only be applicable for those VMs with both labels present.

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Labels are identified by key/value pairs in this map. A VM should contain all the key/value pairs specified in this map to be selected.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Inventory

VM inventory details.

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string
    }  
  
Fields  
---  
`osShortName` |  `string` Required. The OS short name  
`osVersion` |  `string` The OS versionPrefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*`An empty string matches all OS versions.  
  
### Rollout

Message to configure the rollout at the zonal level for the OS policy assignment.

JSON representation  
---  
      
    
    {
      "disruptionBudget": {
        object ([FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.FixedOrPercent))
      },
      "minWaitDuration": string
    }  
  
Fields  
---  
`disruptionBudget` |  `object (`[FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.FixedOrPercent)`)` Required. The maximum number (or percentage) of VMs per zone to disrupt at any given moment.  
`minWaitDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. This determines the minimum duration of time to wait after the configuration changes are applied through the current rollout. A VM continues to count towards the `disruptionBudget` at least until this duration of time has passed after configuration changes are applied.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### FixedOrPercent

Message encapsulating a value that can be either absolute ("fixed") or relative ("percent") to a value.

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "fixed": integer,
      "percent": integer
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`. Type of the value. `mode` can be only one of the following:  
`fixed` |  `integer` Specifies a fixed value.  
`percent` |  `integer` Specifies the relative value defined as a percentage, which will be multiplied by a reference value.  
  
### RolloutState

OS policy assignment rollout state

Enums  
---  
`ROLLOUT_STATE_UNSPECIFIED` | Invalid value  
`IN_PROGRESS` | The rollout is in progress.  
`CANCELLING` | The rollout is being cancelled.  
`CANCELLED` | The rollout is cancelled.  
`SUCCEEDED` | The rollout has completed successfully.  
  
### OrchestrationState

Describes the state of the orchestration process.

JSON representation  
---  
      
    
    {
      "currentIterationState": {
        object ([IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState))
      },
      "previousIterationState": {
        object ([IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState))
      }
    }  
  
Fields  
---  
`currentIterationState` |  `object (`[IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState)`)` Output only. Current Wave iteration state.  
`previousIterationState` |  `object (`[IterationState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.IterationState)`)` Output only. Previous Wave iteration state.  
  
### IterationState

Describes the state of a single iteration of the orchestrator.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.State)),
      "rolloutResource": string,
      "progress": number,
      "performedActions": string,
      "failedActions": string,
      "startTime": string,
      "finishTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/Status))
      }
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators#PolicyOrchestrator.State)`)` Output only. State of the iteration.  
`rolloutResource` |  `string` Output only. Handle to the Progressive Rollouts API rollout resource, which contains detailed information about a particular orchestration iteration.  
`progress` |  `number` Output only. An estimated percentage of the progress. Number between 0 and 100.  
`performedActions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Overall number of actions done by the orchestrator so far.  
`failedActions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of orchestration actions which failed so far. For more details, query the Cloud Logs.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Start time of the wave iteration.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`finishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Finish time of the wave iteration.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/Status)`)` Output only. Error thrown in the wave iteration.  
  
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
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/create)`

|  Creates a new policy orchestrator under the given folder resource.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/delete)`

|  Deletes an existing policy orchestrator resource, parented by a folder.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/get)`

|  Retrieves an existing policy orchestrator, parented by a folder.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/list)`

|  Lists the policy orchestrators under the given parent folder resource.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/patch)`

|  Updates an existing policy orchestrator, parented by a folder.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
