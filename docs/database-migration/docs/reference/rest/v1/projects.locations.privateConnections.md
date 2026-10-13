---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections
title: REST Resource: projects.locations.privateConnections \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:40.729253+00:00
---

# REST Resource: projects.locations.privateConnections  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.privateConnections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrivateConnection
    * JSON representation
  * State
  * VpcPeeringConfig
    * JSON representation
  * PscInterfaceConfig
    * JSON representation
  * Methods



## Resource: PrivateConnection

The PrivateConnection resource is used to establish private connectivity with the customer's network.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#State)),
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
    
      // Union field connectivity can be only one of the following:
      "vpcPeeringConfig": {
        object ([VpcPeeringConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#VpcPeeringConfig))
      },
      "pscInterfaceConfig": {
        object ([PscInterfaceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#PscInterfaceConfig))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`name` |  `string` The name of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of the resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` The private connection display name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#State)`)` Output only. The state of the private connection.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of state FAILED.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
Union field `connectivity`.`connectivity` can be only one of the following:  
`vpcPeeringConfig` |  `object (`[VpcPeeringConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#VpcPeeringConfig)`)` VPC peering configuration.  
`pscInterfaceConfig` |  `object (`[PscInterfaceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections#PscInterfaceConfig)`)` PSC Interface configuration.  
  
## State

Private Connection state.

Enums  
---  
`STATE_UNSPECIFIED` |   
`CREATING` | The private connection is in creation state - creating resources.  
`CREATED` | The private connection has been created with all of its resources.  
`FAILED` | The private connection creation has failed.  
`DELETING` | The private connection is being deleted.  
`FAILED_TO_DELETE` | Delete request has failed, resource is in invalid state.  
`DELETED` | The private connection has been deleted.  
  
## VpcPeeringConfig

The VPC peering configuration is used to create VPC peering with the consumer's VPC.

JSON representation  
---  
      
    
    {
      "vpcName": string,
      "subnet": string
    }  
  
Fields  
---  
`vpcName` |  `string` Required. Fully qualified name of the VPC that Database Migration Service will peer to.  
`subnet` |  `string` Required. A free subnet for peering. (CIDR of /29)  
  
## PscInterfaceConfig

The PSC Interface configuration is used to create PSC Interface between DMS's internal VPC and the consumer's PSC.

JSON representation  
---  
      
    
    {
      "networkAttachment": string
    }  
  
Fields  
---  
`networkAttachment` |  `string` Required. Fully qualified name of the Network Attachment that DMS will connect to. Format: `projects/{project}/regions/{region}/networkAttachments/{name}`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/create)`

|  Creates a new private connection in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/delete)`

|  Deletes a single Database Migration Service private connection.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/get)`

|  Gets details of a single private connection.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/list)`

|  Retrieves a list of private connections in a given project and location.  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
