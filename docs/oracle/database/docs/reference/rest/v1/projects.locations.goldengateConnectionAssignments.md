---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments
title: REST Resource: projects.locations.goldengateConnectionAssignments \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:47.602448+00:00
---

# REST Resource: projects.locations.goldengateConnectionAssignments  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateConnectionAssignments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateConnectionAssignment
    * JSON representation
  * GoldengateConnectionAssignmentProperties
    * JSON representation
  * State
  * Methods



## Resource: GoldengateConnectionAssignment

Represents the metadata of a Goldengate Connection Assignment.

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([GoldengateConnectionAssignmentProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#GoldengateConnectionAssignmentProperties))
      },
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "entitlementId": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the GoldengateConnectionAssignment resource in the following format: projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengateConnectionAssignment}  
`properties` |  `object (`[GoldengateConnectionAssignmentProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#GoldengateConnectionAssignmentProperties)`)` Required. The properties of the GoldengateConnectionAssignment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the connection assignment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the GoldengateConnectionAssignment.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Optional. The display name for the GoldengateConnectionAssignment.  
`entitlementId` |  `string` Output only. The OCID of the entitlement linked to this resource.  
  
## GoldengateConnectionAssignmentProperties

The properties of a GoldengateConnectionAssignment.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "goldengateConnection": string,
      "goldengateDeployment": string,
      "alias": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#State))
    }  
  
Fields  
---  
`ocid` |  `string` Output only. The [OCID](https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection assignment being referenced.  
`goldengateConnection` |  `string` Required. The GoldengateConnection resource to be assigned. Format: projects/{project}/locations/{location}/goldengateConnections/{goldengateConnection}  
`goldengateDeployment` |  `string` Required. The GoldenGateDeployment to assign the connection to. Format: projects/{project}/locations/{location}/goldengateDeployments/{goldengateDeployment}  
`alias` |  `string` Output only. Credential store alias.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#State)`)` Output only. The lifecycle state of the connection assignment.  
  
## State

Possible lifecycle states for connection assignments.

Enums  
---  
`STATE_UNSPECIFIED` | Lifecycle state is unspecified.  
`CREATING` | Connection assignment is being created.  
`ACTIVE` | Connection assignment is active.  
`FAILED` | Connection assignment failed.  
`UPDATING` | Connection assignment is being updated.  
`DELETING` | Connection assignment is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/create)`

|  Creates a new GoldengateConnectionAssignment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/delete)`

|  Deletes a single GoldengateConnectionAssignment.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/get)`

|  Gets details of a single GoldengateConnectionAssignment.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/list)`

|  Lists GoldengateConnectionAssignments in a given project and location.  
  
### `[test](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test)`

|  Tests a single GoldengateConnectionAssignment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
