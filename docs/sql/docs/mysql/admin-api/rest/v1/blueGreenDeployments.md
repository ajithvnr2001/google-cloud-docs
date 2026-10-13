---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/
title: REST Resource: blueGreenDeployments \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:50.936483+00:00
---

# REST Resource: blueGreenDeployments  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/

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
  * SourceTargetPairedNode
    * JSON representation
  * NodeInfo
    * JSON representation
  * State
  * ConfigDiff
    * JSON representation
  * DeploymentTasks
    * JSON representation
  * DeploymentTask
    * JSON representation
  * Type
  * State
  * RequestedConfig
    * JSON representation
  * Methods



## Resource: BlueGreenDeployment

A `BlueGreenDeployment` resource represents a Cloud SQL blue-green deployment setup.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State)),
      "sourceInstance": string,
      "switchoverTargetInstance": string,
      "errorDetail": string,
      "deploymentMappings": [
        {
          object ([SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#SourceTargetPairedNode))
        }
      ],
      "deploymentTasks": {
        object ([DeploymentTasks](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#DeploymentTasks))
      },
      "requestedConfig": {
        object ([RequestedConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#RequestedConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The full resource name of the deployment. Format: projects/{project}/locations/{location}/blueGreenDeployments/{deploymentId}  
`description` |  `string` Optional. User-provided description for the deployment. The description can be up to 255 characters long.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the deployment was created. Example: `2024-01-01T00:00:00Z`Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State)`)` Output only. The current state of the blue-green deployment.  
`sourceInstance` |  `string` Required. Immutable. Required on create, and immutable. The full resource name of the source instance (the "blue" instance). Format: projects/{project}/instances/{instance}  
`switchoverTargetInstance` |  `string` Output only. The full resource name of the primary target instance (the "green" instance) that will be promoted during switchover. This field is always populated once the deployment is created. Format: projects/{project}/instances/{instance}  
`errorDetail` |  `string` Output only. Provides details on why switchover is not possible. This field is empty unless a switchover attempt failed or the state is `SWITCHOVER_NOT_READY`. Example: "The target database version does not match the source instance database version."  
`deploymentMappings[]` |  `object (`[SourceTargetPairedNode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#SourceTargetPairedNode)`)` Output only. A list representing the pairs of source and target instances in the deployment.  
`deploymentTasks` |  `object (`[DeploymentTasks](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#DeploymentTasks)`)` Output only. Combined list of tasks for all paired nodes.  
`requestedConfig` |  `object (`[RequestedConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#RequestedConfig)`)` Optional. Immutable. Optional on create, and immutable. The configuration intended for the target instance(s) when the deployment was created.  
  
## State

The state of the blue-green deployment.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted or unknown.  
`PROVISIONING` | The deployment is being provisioned.  
`SWITCHOVER_READY` | The deployment is ready for switchover.  
`SWITCHOVER_NOT_READY` | The deployment is not ready for switchover.  
`SWITCHOVER_IN_PROGRESS` | The deployment is in the process of switching over.  
`SWITCHOVER_COMPLETED` | The deployment has completed switchover.  
`DELETING` | The deployment is being deleted.  
  
## SourceTargetPairedNode

Represents a pairing of a source instance node and a target instance node.

JSON representation  
---  
      
    
    {
      "source": {
        object ([NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#NodeInfo))
      },
      "target": {
        object ([NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#NodeInfo))
      },
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State_1)),
      "diffs": [
        {
          object ([ConfigDiff](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#ConfigDiff))
        }
      ]
    }  
  
Fields  
---  
`source` |  `object (`[NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#NodeInfo)`)` Output only. Specifies the resource name of the source instance in this pair.  
`target` |  `object (`[NodeInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#NodeInfo)`)` Output only. Specifies details of the corresponding target instance in this pair.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State_1)`)` Output only. Specifies the current state of this specific source-target pair.  
`diffs[]` |  `object (`[ConfigDiff](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#ConfigDiff)`)` Output only. Describes the list of differences for the `SourceTargetPairedNode`.  
  
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
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/IpMapping))
        }
      ]
    }  
  
Fields  
---  
`instance` |  `string` Output only. The full resource name of the instance. Format: projects/{project}/instances/{instance}  
`connection` |  `string` Output only. The instance connection name.  
`dns` |  `string` Output only. The unique DNS name for this instance.  
`ipMappings[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/IpMapping)`)` Output only. The list of IP addresses for this instance.  
  
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
  
## ConfigDiff

Represents a specific configuration difference between blue and green instances.

JSON representation  
---  
      
    
    {
      "field": string,
      "sourceValue": string,
      "targetValue": string
    }  
  
Fields  
---  
`field` |  `string` Output only. The name of the field that differs in the blue and green instances, fully-qualified. Example: `settings.tier`  
`sourceValue` |  `string` Output only. The value on the source instance.  
`targetValue` |  `string` Output only. The value on the target instance.  
  
## DeploymentTasks

Combined list of tasks for all paired nodes in the deployment.

JSON representation  
---  
      
    
    {
      "task": [
        {
          object ([DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#DeploymentTask))
        }
      ]
    }  
  
Fields  
---  
`task[]` |  `object (`[DeploymentTask](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#DeploymentTask)`)` Output only. Tasks performed or being performed on the paired nodes of the deployment at a consolidated level.  
  
## DeploymentTask

Represents a task executed as part of the deployment on a target instance.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#Type)),
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State_2)),
      "startTime": string,
      "endTime": string,
      "errorMessage": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#Type)`)` Output only. The type of the task.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#State_2)`)` Output only. The current state of the task.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Task start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Task end time (if completed).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`errorMessage` |  `string` Output only. Optional error details if the task state is `FAILED`.  
  
## Type

The type of the task. This enum type `Type` is prone to change, and new values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value is used if the type is omitted.  
`PROVISION` | Provisions the green environment, which includes creating the target instance.  
`UPGRADE` | Upgrades the green environment, for example, performing a major version upgrade on the target instance.  
`SWITCHOVER` | Promotes the target instance and then demotes the source instance for this pair.  
`DELETE` | Deletes the blue-green deployment, including underlying resources.  
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
  
## RequestedConfig

Configuration specified by the user at creation time for the target (green) instance.

JSON representation  
---  
      
    
    {
      "databaseVersion": string
    }  
  
Fields  
---  
`databaseVersion` |  `string` Optional. The target database major version for the upgrade. For example, `MYSQL_8_0` or `POSTGRES_15`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/create)`

|  Creates a blue-green deployment under a given project and location.  
  
### `[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/delete)`

|  Deletes a blue-green deployment.  
  
### `[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/get)`

|  Retrieves a blue-green deployment resource under a given project and location.  
  
### `[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/list)`

|  Lists blue-green deployments under a given project.  
  
### `[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/switchover)`

|  Switches over to green instance for a blue-green deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
