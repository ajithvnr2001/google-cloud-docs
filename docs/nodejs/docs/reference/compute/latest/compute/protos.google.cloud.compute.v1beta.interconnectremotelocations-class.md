---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.interconnectremotelocations-class
title: Class protos.google.cloud.compute.v1beta.InterconnectRemoteLocations (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:48.117060+00:00
---

# Class protos.google.cloud.compute.v1beta.InterconnectRemoteLocations (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.interconnectremotelocations-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.InterconnectRemoteLocations (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents an InterconnectRemoteLocations

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.InterconnectRemoteLocations

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new InterconnectRemoteLocations service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): InterconnectRemoteLocations;

Creates new InterconnectRemoteLocations service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocations](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.interconnectremotelocations-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetInterconnectRemoteLocationRequest, callback: google.cloud.compute.v1beta.InterconnectRemoteLocations.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInterconnectRemoteLocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetinterconnectremotelocationrequest)`   
GetInterconnectRemoteLocationRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and InterconnectRemoteLocation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetInterconnectRemoteLocationRequest): Promise<google.cloud.compute.v1beta.InterconnectRemoteLocation>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInterconnectRemoteLocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetinterconnectremotelocationrequest)`   
GetInterconnectRemoteLocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.InterconnectRemoteLocation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.interconnectremotelocation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1beta.IListInterconnectRemoteLocationsRequest, callback: google.cloud.compute.v1beta.InterconnectRemoteLocations.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInterconnectRemoteLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistinterconnectremotelocationsrequest)`   
ListInterconnectRemoteLocationsRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and InterconnectRemoteLocationList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1beta.IListInterconnectRemoteLocationsRequest): Promise<google.cloud.compute.v1beta.InterconnectRemoteLocationList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInterconnectRemoteLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistinterconnectremotelocationsrequest)`   
ListInterconnectRemoteLocationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.InterconnectRemoteLocationList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.interconnectremotelocationlist)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
