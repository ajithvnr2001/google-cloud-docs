---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdiscovery-class
title: Class protos.google.cloud.apihub.v1.ApiHubDiscovery (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:42.293166+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHubDiscovery (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdiscovery-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHubDiscovery (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHubDiscovery

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.ApiHubDiscovery

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApiHubDiscovery service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApiHubDiscovery;

Creates new ApiHubDiscovery service using the specified rpc implementation.

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
`[ApiHubDiscovery](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubdiscovery-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getDiscoveredApiObservation(request, callback)
    
    
    public getDiscoveredApiObservation(request: google.cloud.apihub.v1.IGetDiscoveredApiObservationRequest, callback: google.cloud.apihub.v1.ApiHubDiscovery.GetDiscoveredApiObservationCallback): void;

Calls GetDiscoveredApiObservation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDiscoveredApiObservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdiscoveredapiobservationrequest)`   
GetDiscoveredApiObservationRequest message or plain object  
`callback` |  `[GetDiscoveredApiObservationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and DiscoveredApiObservation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDiscoveredApiObservation(request)
    
    
    public getDiscoveredApiObservation(request: google.cloud.apihub.v1.IGetDiscoveredApiObservationRequest): Promise<google.cloud.apihub.v1.DiscoveredApiObservation>;

Calls GetDiscoveredApiObservation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDiscoveredApiObservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdiscoveredapiobservationrequest)`   
GetDiscoveredApiObservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)>` | Promise  
  
### getDiscoveredApiOperation(request, callback)
    
    
    public getDiscoveredApiOperation(request: google.cloud.apihub.v1.IGetDiscoveredApiOperationRequest, callback: google.cloud.apihub.v1.ApiHubDiscovery.GetDiscoveredApiOperationCallback): void;

Calls GetDiscoveredApiOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDiscoveredApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdiscoveredapioperationrequest)`   
GetDiscoveredApiOperationRequest message or plain object  
`callback` |  `[GetDiscoveredApiOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and DiscoveredApiOperation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDiscoveredApiOperation(request)
    
    
    public getDiscoveredApiOperation(request: google.cloud.apihub.v1.IGetDiscoveredApiOperationRequest): Promise<google.cloud.apihub.v1.DiscoveredApiOperation>;

Calls GetDiscoveredApiOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDiscoveredApiOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetdiscoveredapioperationrequest)`   
GetDiscoveredApiOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.DiscoveredApiOperation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapioperation-class)>` | Promise  
  
### listDiscoveredApiObservations(request, callback)
    
    
    public listDiscoveredApiObservations(request: google.cloud.apihub.v1.IListDiscoveredApiObservationsRequest, callback: google.cloud.apihub.v1.ApiHubDiscovery.ListDiscoveredApiObservationsCallback): void;

Calls ListDiscoveredApiObservations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDiscoveredApiObservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdiscoveredapiobservationsrequest)`   
ListDiscoveredApiObservationsRequest message or plain object  
`callback` |  `[ListDiscoveredApiObservationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDiscoveredApiObservationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDiscoveredApiObservations(request)
    
    
    public listDiscoveredApiObservations(request: google.cloud.apihub.v1.IListDiscoveredApiObservationsRequest): Promise<google.cloud.apihub.v1.ListDiscoveredApiObservationsResponse>;

Calls ListDiscoveredApiObservations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDiscoveredApiObservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdiscoveredapiobservationsrequest)`   
ListDiscoveredApiObservationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListDiscoveredApiObservationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listdiscoveredapiobservationsresponse)>` | Promise  
  
### listDiscoveredApiOperations(request, callback)
    
    
    public listDiscoveredApiOperations(request: google.cloud.apihub.v1.IListDiscoveredApiOperationsRequest, callback: google.cloud.apihub.v1.ApiHubDiscovery.ListDiscoveredApiOperationsCallback): void;

Calls ListDiscoveredApiOperations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDiscoveredApiOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdiscoveredapioperationsrequest)`   
ListDiscoveredApiOperationsRequest message or plain object  
`callback` |  `[ListDiscoveredApiOperationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDiscoveredApiOperationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDiscoveredApiOperations(request)
    
    
    public listDiscoveredApiOperations(request: google.cloud.apihub.v1.IListDiscoveredApiOperationsRequest): Promise<google.cloud.apihub.v1.ListDiscoveredApiOperationsResponse>;

Calls ListDiscoveredApiOperations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDiscoveredApiOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistdiscoveredapioperationsrequest)`   
ListDiscoveredApiOperationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListDiscoveredApiOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listdiscoveredapioperationsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
