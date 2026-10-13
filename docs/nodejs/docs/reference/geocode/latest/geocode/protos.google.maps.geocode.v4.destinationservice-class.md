---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.destinationservice-class
title: Class protos.google.maps.geocode.v4.DestinationService (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:32.528665+00:00
---

# Class protos.google.maps.geocode.v4.DestinationService (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.destinationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.geocode.v4.DestinationService (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DestinationService

## Inheritance

$protobuf.rpc.Service > protos.google.maps.geocode.v4.DestinationService

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DestinationService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DestinationService;

Creates new DestinationService service using the specified rpc implementation.

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
`[DestinationService](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.destinationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### searchDestinations(request, callback)
    
    
    public searchDestinations(request: google.maps.geocode.v4.ISearchDestinationsRequest, callback: google.maps.geocode.v4.DestinationService.SearchDestinationsCallback): void;

Calls SearchDestinations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.isearchdestinationsrequest)`   
SearchDestinationsRequest message or plain object  
`callback` |  `[SearchDestinationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchDestinationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDestinations(request)
    
    
    public searchDestinations(request: google.maps.geocode.v4.ISearchDestinationsRequest): Promise<google.maps.geocode.v4.SearchDestinationsResponse>;

Calls SearchDestinations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.isearchdestinationsrequest)`   
SearchDestinationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.geocode.v4.SearchDestinationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.searchdestinationsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
