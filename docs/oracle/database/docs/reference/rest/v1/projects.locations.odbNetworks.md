---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks
title: REST Resource: projects.locations.odbNetworks \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:51.498977+00:00
---

# REST Resource: projects.locations.odbNetworks  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.odbNetworks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: OdbNetwork
    * JSON representation
  * State
  * Methods



## Resource: OdbNetwork

Represents OdbNetwork resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "network": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks#State)),
      "entitlementId": string,
      "gcpOracleZone": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the OdbNetwork resource in the following format: projects/{project}/locations/{region}/odbNetworks/{odbNetwork}  
`network` |  `string` Required. The name of the VPC network in the following format: projects/{project}/global/networks/{network}  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the OdbNetwork was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks#State)`)` Output only. State of the ODB Network.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the OdbNetwork.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where OdbNetwork is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
  
## State

The various lifecycle states of the ODB Network.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`FAILED` | Indicates that the resource is in failed state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/create)`

|  Creates a new ODB Network in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/delete)`

|  Deletes a single ODB Network.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/get)`

|  Gets details of a single ODB Network.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/list)`

|  Lists the ODB Networks in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
