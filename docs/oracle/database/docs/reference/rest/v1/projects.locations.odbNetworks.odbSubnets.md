---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets
title: REST Resource: projects.locations.odbNetworks.odbSubnets \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:51.879709+00:00
---

# REST Resource: projects.locations.odbNetworks.odbSubnets  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.odbNetworks.odbSubnets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: OdbSubnet
    * JSON representation
  * Purpose
  * State
  * Methods



## Resource: OdbSubnet

Represents OdbSubnet resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "cidrRange": string,
      "purpose": enum ([Purpose](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets#Purpose)),
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the OdbSubnet resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`cidrRange` |  `string` Required. The CIDR range of the subnet.  
`purpose` |  `enum (`[Purpose](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets#Purpose)`)` Required. Purpose of the subnet.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the OdbNetwork was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets#State)`)` Output only. State of the ODB Subnet.  
  
## Purpose

Purpose available for the subnet.

Enums  
---  
`PURPOSE_UNSPECIFIED` | Default unspecified value.  
`CLIENT_SUBNET` | Subnet to be used for client connections.  
`BACKUP_SUBNET` | Subnet to be used for backup.  
  
## State

The various lifecycle states of the ODB Subnet.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`FAILED` | Indicates that the resource is in failed state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/create)`

|  Creates a new ODB Subnet in a given ODB Network.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/delete)`

|  Deletes a single ODB Subnet.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/get)`

|  Gets details of a single ODB Subnet.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/list)`

|  Lists all the ODB Subnets in a given ODB Network.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
