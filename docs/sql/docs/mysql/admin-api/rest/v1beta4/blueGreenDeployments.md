---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/
title: REST Resource: blueGreenDeployments \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:03.312088+00:00
---

# REST Resource: blueGreenDeployments  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  REST Resource: blueGreenDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BlueGreenDeployment
    * JSON representation
  * State
  * TargetConfig
    * JSON representation
  * SourceTargetPairedNode
    * JSON representation
  * NodeInfo
    * JSON representation
  * State
  * CurrentlyServingTraffic
  * DeploymentTask
    * JSON representation
  * Type
  * State
  * ConfigDiff
    * JSON representation
  * DeploymentTasks
    * JSON representation
  * RequestedConfig
    * JSON representation
  * Methods



## Resource: BlueGreenDeployment

A `BlueGreenDeployment` resource represents a Cloud SQL blue-green deployment setup. It orchestrates the lifecycle of creating a synchronized "green" environment from a "blue" production environment, performing updates, and managing the switchover process to minimize downtime.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State)),
      "sourceInstance": string,
      "targetConfig": {
        object ([TargetConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#TargetConfig))
      },
      "switchoverTargetInstance": string,
      "pairedNodes": [
        {
          object ([SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#SourceTargetPairedNode))
        }
      ],
      "errorDetail": string,
      "deploymentMappings": [
        {
          object ([SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#SourceTargetPairedNode))
        }
      ],
      "deploymentTasks": {
        object ([DeploymentTasks](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTasks))
      },
      "requestedConfig": {
        object ([RequestedConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#RequestedConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The full resource name of the deployment. Format: projects/{project}/locations/{location}/blueGreenDeployments/{deploymentId}  
`description` |  `string` Optional. User-provided description for the deployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the deployment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State)`)` Output only. The current state of the blue-green deployment.  
`sourceInstance` |  `string` Required. Immutable. The instance ID of the source instance (the "blue" instance). The value for this field does not include the project ID, for example, `my-instance-id`. This field is immutable.  
`targetConfig  
**(deprecated)**` |  `object (`[TargetConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#TargetConfig)`)` This item is deprecated!Optional. Immutable. Deprecated: Use requestedConfig instead. The configuration intended for the target instance(s) when the deployment was created. This field is immutable.  
`switchoverTargetInstance` |  `string` Output only. Details about the primary target instance (the "Green" instance) that will be promoted during switchover.  
`pairedNodes[]  
**(deprecated)**` |  `object (`[SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#SourceTargetPairedNode)`)` This item is deprecated!Output only. Deprecated: Use deploymentMappings instead. Output only. A list representing the pairs of source and target instances in the deployment.  
`errorDetail` |  `string` Output only. Provides an error message with details on why switchover is not possible.  
`deploymentMappings[]` |  `object (`[SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#SourceTargetPairedNode)`)` Output only. A list representing the pairs of source and target instances in the deployment.  
`deploymentTasks` |  `object (`[DeploymentTasks](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTasks)`)` Output only. Combined list of tasks for all paired nodes.  
`requestedConfig` |  `object (`[RequestedConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#RequestedConfig)`)` Optional. Immutable. Optional on create, and immutable. The configuration intended for the target instance(s) when the deployment was created.  
  
## State

The state of the blue-green deployment. This enum is not frozen, and new values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the deployment is unknown.  
`PROVISIONING` | The deployment is being provisioned.  
`SWITCHOVER_READY` | The deployment is ready for switchover.  
`SWITCHOVER_NOT_READY` | The deployment is not ready for switchover.  
`SWITCHOVER_IN_PROGRESS` | The deployment is in the process of switching over.  
`SWITCHOVER_COMPLETED` | The deployment has completed switchover.  
`DELETING` | The deployment is being deleted.  
  
## TargetConfig

This item is deprecated!

Deprecated: Use RequestedConfig instead. Configuration specified by the user at creation time for the target (Green) instance.

JSON representation  
---  
      
    
    {
      "databaseVersion": string
    }  
  
Fields  
---  
`databaseVersion` |  `string` Optional. The target database major version for the upgrade.  
  
## SourceTargetPairedNode

Represents a pairing of a source instance node and a target instance node.

JSON representation  
---  
      
    
    {
      "source": {
        object ([NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#NodeInfo))
      },
      "target": {
        object ([NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#NodeInfo))
      },
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State_1)),
      "currentlyServingTraffic": enum ([CurrentlyServingTraffic](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#CurrentlyServingTraffic)),
      "tasks": [
        {
          object ([DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTask))
        }
      ],
      "diffs": [
        {
          object ([ConfigDiff](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#ConfigDiff))
        }
      ]
    }  
  
Fields  
---  
`source` |  `object (`[NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#NodeInfo)`)` Output only. Resource name of the source instance in this pair.  
`target` |  `object (`[NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#NodeInfo)`)` Output only. Details of the corresponding target instance in this pair.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State_1)`)` Output only. The current state of this specific source-target pair.  
`currentlyServingTraffic  
**(deprecated)**` |  `enum (`[CurrentlyServingTraffic](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#CurrentlyServingTraffic)`)` This item is deprecated!Output only. Deprecated: Indicates which instance (SOURCE or TARGET) in the pair is currently live. Used for internal implementation and deprecated for external use.  
`tasks[]` |  `object (`[DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTask)`)` Output only. Tasks performed or being performed on the target instance of this pair.  
`diffs[]` |  `object (`[ConfigDiff](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#ConfigDiff)`)` Output only. Describes the list of differences for this pair.  
  
## NodeInfo

Details about an instance within the deployment.

JSON representation  
---  
      
    
    {
      "instance": string,
      "connection": string,
      "dns": string,
      "ipMappings": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/IpMapping))
        }
      ]
    }  
  
Fields  
---  
`instance` |  `string` Output only. The full resource name of the instance. Format: projects/{project}/instances/{instance}  
`connection` |  `string` Output only. The instance connection name.  
`dns` |  `string` Output only. The unique DNS name for this instance.  
`ipMappings[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/IpMapping)`)` Output only. The list of IP addresses for this instance.  
  
## State

The state of a pair of source and target instances in deployment (paired node).

Enums  
---  
`STATE_UNSPECIFIED` | The state of the paired node is unknown.  
`PROVISIONING` | The paired node is being provisioned.  
`PROVISIONED` | The paired node is provisioned.  
`UPGRADING` | The paired node is upgrading.  
`UPGRADED` | The paired node is upgraded.  
`UPGRADE_FAILED` | Upgrade failed on the paired node.  
`SWITCHOVER_IN_PROGRESS` | Switchover is in progress.  
`SWITCHOVER_FAILED` | Switchover failed on the paired node.  
`SWITCHOVER_SUCCEEDED` | Switchover completed successfully.  
`DELETING` | The paired node is being deleted.  
  
## CurrentlyServingTraffic

The instance currently serving traffic.

Enums  
---  
`CURRENTLY_SERVING_TRAFFIC_UNSPECIFIED` | The instance serving traffic is unknown.  
`SOURCE` | The source instance is serving traffic.  
`TARGET` | The target instance is serving traffic.  
  
## DeploymentTask

Represents a task executed as part of the deployment on a target instance.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#Type)),
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State_2)),
      "startTime": string,
      "endTime": string,
      "errorMessage": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#Type)`)` Output only. The type of the task.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#State_2)`)` Output only. The current state of the task.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Task start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Task end time (if completed).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`errorMessage` |  `string` Output only. Optional Error details if the task state is FAILED.  
  
## Type

The type of the task. This enum is not frozen, and new values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value is used if the type is omitted.  
`PROVISION` | Creating target instance.  
`UPGRADE` | e.g., Major Version Upgrade on Target.  
`SWITCHOVER` | Promoting Target, Demoting Source for this pair.  
`DELETE` | The task is to delete deployment.  
`POST_SWITCHOVER_OPERATIONS` | Post-switchover operations, including cleaning up resources of the old instance, taking final backups, and updating metadata.  
  
## State

The state of the task. This enum is not frozen, and new values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the task is unknown.  
`PENDING` | The task is pending.  
`RUNNING` | The task is running.  
`SUCCEEDED` | The task has succeeded.  
`FAILED` | The task has failed.  
  
## ConfigDiff

Represents a specific configuration difference between Blue and Green instances.

JSON representation  
---  
      
    
    {
      "field": string,
      "sourceValue": string,
      "targetValue": string
    }  
  
Fields  
---  
`field` |  `string` Output only. The name of the field that differs, fully-qualified. Example: settings.tier  
`sourceValue` |  `string` Output only. The value on the source instance.  
`targetValue` |  `string` Output only. The value on the target instance.  
  
## DeploymentTasks

Combined list of tasks for all paired nodes in the deployment.

JSON representation  
---  
      
    
    {
      "task": [
        {
          object ([DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTask))
        }
      ]
    }  
  
Fields  
---  
`task[]` |  `object (`[DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#DeploymentTask)`)` Output only. Tasks performed or being performed on the paired nodes of the deployment at a consolidated level.  
  
## RequestedConfig

Configuration specified by the user at creation time for the target (Green) instance.

JSON representation  
---  
      
    
    {
      "databaseVersion": string
    }  
  
Fields  
---  
`databaseVersion` |  `string` Optional. The target database major version for the upgrade.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/create)`

|  Creates a blue-green deployment under a given project and location.  
  
### `[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/delete)`

|  Deletes a blue-green deployment, including metadata and underlying resources based on the deployment state.  
  
### `[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/get)`

|  Retrieves a blue-green deployment resource under a given project and location.  
  
### `[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/list)`

|  Lists blue-green deployments under a given project.  
  
### `[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/switchover)`

|  Switches over to green instance for a blue-green deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
