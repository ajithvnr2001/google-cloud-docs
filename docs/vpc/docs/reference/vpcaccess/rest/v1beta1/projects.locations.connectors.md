---
url: https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors
title: REST Resource: projects.locations.connectors \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:00.238993+00:00
---

# REST Resource: projects.locations.connectors  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/apis)



Send feedback 

#  REST Resource: projects.locations.connectors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connector
    * JSON representation
  * State
  * Subnet
    * JSON representation
  * Methods



## Resource: Connector

Definition of a Serverless VPC Access connector.

JSON representation  
---  
      
    
    {
      "name": string,
      "network": string,
      "ipCidrRange": string,
      "state": enum ([State](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors#State)),
      "minThroughput": integer,
      "maxThroughput": integer,
      "connectedProjects": [
        string
      ],
      "subnet": {
        object ([Subnet](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors#Subnet))
      },
      "machineType": string,
      "minInstances": integer,
      "maxInstances": integer,
      "createTime": string,
      "lastRestartTime": string
    }  
  
Fields  
---  
`name` |  `string` The resource name in the format `projects/*/locations/*/connectors/*`.  
`network` |  `string` Optional. Name of a VPC network.  
`ipCidrRange` |  `string` Optional. The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors#State)`)` Output only. State of the VPC access connector.  
`minThroughput  
**(deprecated)**` |  `integer` This item is deprecated!Minimum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 200 through 900. Must be lower than the value specified by --max-throughput. If both min-throughput and min-instances are provided, min-instances takes precedence over min-throughput. The use of `min-throughput` is discouraged in favor of `min-instances`.  
`maxThroughput  
**(deprecated)**` |  `integer` This item is deprecated!Maximum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 300 through 1000. Must be higher than the value specified by --min-throughput. If both max-throughput and max-instances are provided, max-instances takes precedence over max-throughput. The use of `max-throughput` is discouraged in favor of `max-instances`.  
`connectedProjects[]` |  `string` Output only. List of projects using the connector.  
`subnet` |  `object (`[Subnet](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors#Subnet)`)` Optional. The subnet in which to house the VPC Access Connector.  
`machineType` |  `string` Machine type of VM Instance underlying connector. Default is e2-micro  
`minInstances` |  `integer` Minimum value of instances in autoscaling group underlying the connector.  
`maxInstances` |  `integer` Maximum value of instances in autoscaling group underlying the connector.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the connector.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastRestartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last restart time of the connector.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

State of a connector.

Enums  
---  
`STATE_UNSPECIFIED` | Invalid state.  
`READY` | Connector is deployed and ready to receive traffic.  
`CREATING` | An Insert operation is in progress. Transient condition.  
`DELETING` | A Delete operation is in progress. Transient condition.  
`ERROR` | Connector is in a bad state, manual deletion recommended.  
`UPDATING` | The connector is being updated.  
  
## Subnet

The subnet in which to house the connector

JSON representation  
---  
      
    
    {
      "name": string,
      "projectId": string
    }  
  
Fields  
---  
`name` |  `string` Optional. Subnet name (relative, not fully qualified). E.g. if the full subnet selfLink is <https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetName>} the correct input for this field would be {subnetName}  
`projectId` |  `string` Optional. Project in which the subnet exists. If not set, this project is assumed to be the project for which the connector create request was issued.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors/create)`

|  Creates a Serverless VPC Access connector, returns an operation.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors/delete)`

|  Deletes a Serverless VPC Access connector.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors/get)`

|  Gets a Serverless VPC Access connector.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors/list)`

|  Lists Serverless VPC Access connectors.  
  
### `[patch](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1beta1/projects.locations.connectors/patch)`

|  Updates a Serverless VPC Access connector, returns an operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
