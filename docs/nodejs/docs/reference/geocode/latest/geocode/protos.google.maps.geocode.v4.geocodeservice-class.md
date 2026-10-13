---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocodeservice-class
title: Class protos.google.maps.geocode.v4.GeocodeService (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:33.731028+00:00
---

# Class protos.google.maps.geocode.v4.GeocodeService (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocodeservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.geocode.v4.GeocodeService (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a GeocodeService

## Inheritance

$protobuf.rpc.Service > protos.google.maps.geocode.v4.GeocodeService

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new GeocodeService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): GeocodeService;

Creates new GeocodeService service using the specified rpc implementation.

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
`[GeocodeService](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocodeservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### geocodeAddress(request, callback)
    
    
    public geocodeAddress(request: google.maps.geocode.v4.IGeocodeAddressRequest, callback: google.maps.geocode.v4.GeocodeService.GeocodeAddressCallback): void;

Calls GeocodeAddress.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGeocodeAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodeaddressrequest)`   
GeocodeAddressRequest message or plain object  
`callback` |  `[GeocodeAddressCallback](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)`   
Node-style callback called with the error, if any, and GeocodeAddressResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### geocodeAddress(request)
    
    
    public geocodeAddress(request: google.maps.geocode.v4.IGeocodeAddressRequest): Promise<google.maps.geocode.v4.GeocodeAddressResponse>;

Calls GeocodeAddress.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGeocodeAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodeaddressrequest)`   
GeocodeAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.geocode.v4.GeocodeAddressResponse](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocodeaddressresponse)>` | Promise  
  
### geocodeLocation(request, callback)
    
    
    public geocodeLocation(request: google.maps.geocode.v4.IGeocodeLocationRequest, callback: google.maps.geocode.v4.GeocodeService.GeocodeLocationCallback): void;

Calls GeocodeLocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGeocodeLocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodelocationrequest)`   
GeocodeLocationRequest message or plain object  
`callback` |  `[GeocodeLocationCallback](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)`   
Node-style callback called with the error, if any, and GeocodeLocationResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### geocodeLocation(request)
    
    
    public geocodeLocation(request: google.maps.geocode.v4.IGeocodeLocationRequest): Promise<google.maps.geocode.v4.GeocodeLocationResponse>;

Calls GeocodeLocation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGeocodeLocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodelocationrequest)`   
GeocodeLocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.geocode.v4.GeocodeLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocodelocationresponse)>` | Promise  
  
### geocodePlace(request, callback)
    
    
    public geocodePlace(request: google.maps.geocode.v4.IGeocodePlaceRequest, callback: google.maps.geocode.v4.GeocodeService.GeocodePlaceCallback): void;

Calls GeocodePlace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGeocodePlaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodeplacerequest)`   
GeocodePlaceRequest message or plain object  
`callback` |  `[GeocodePlaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)`   
Node-style callback called with the error, if any, and GeocodeResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### geocodePlace(request)
    
    
    public geocodePlace(request: google.maps.geocode.v4.IGeocodePlaceRequest): Promise<google.maps.geocode.v4.GeocodeResult>;

Calls GeocodePlace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGeocodePlaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocodeplacerequest)`   
GeocodePlaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.maps.geocode.v4.GeocodeResult](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.geocoderesult-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
