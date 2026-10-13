---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.regionhealthcheckservices-class
title: Class protos.google.cloud.compute.v1beta.RegionHealthCheckServices (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:09.737804+00:00
---

# Class protos.google.cloud.compute.v1beta.RegionHealthCheckServices (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.regionhealthcheckservices-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.RegionHealthCheckServices (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a RegionHealthCheckServices

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.RegionHealthCheckServices

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RegionHealthCheckServices service.

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

### aggregatedList(request, callback)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListRegionHealthCheckServicesRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.AggregatedListCallback): void;

Calls AggregatedList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListRegionHealthCheckServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistregionhealthcheckservicesrequest)`   
AggregatedListRegionHealthCheckServicesRequest message or plain object  
`callback` |  `[AggregatedListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and HealthCheckServiceAggregatedList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregatedList(request)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListRegionHealthCheckServicesRequest): Promise<google.cloud.compute.v1beta.HealthCheckServiceAggregatedList>;

Calls AggregatedList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListRegionHealthCheckServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistregionhealthcheckservicesrequest)`   
AggregatedListRegionHealthCheckServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.HealthCheckServiceAggregatedList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.healthcheckserviceaggregatedlist)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RegionHealthCheckServices;

Creates new RegionHealthCheckServices service using the specified rpc implementation.

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
`[RegionHealthCheckServices](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.regionhealthcheckservices-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteRegionHealthCheckServiceRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionhealthcheckservicerequest)`   
DeleteRegionHealthCheckServiceRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteRegionHealthCheckServiceRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionhealthcheckservicerequest)`   
DeleteRegionHealthCheckServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetRegionHealthCheckServiceRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionhealthcheckservicerequest)`   
GetRegionHealthCheckServiceRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and HealthCheckService  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetRegionHealthCheckServiceRequest): Promise<google.cloud.compute.v1beta.HealthCheckService>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionhealthcheckservicerequest)`   
GetRegionHealthCheckServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.HealthCheckService](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.healthcheckservice-class)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertRegionHealthCheckServiceRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionhealthcheckservicerequest)`   
InsertRegionHealthCheckServiceRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertRegionHealthCheckServiceRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionhealthcheckservicerequest)`   
InsertRegionHealthCheckServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1beta.IListRegionHealthCheckServicesRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionHealthCheckServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionhealthcheckservicesrequest)`   
ListRegionHealthCheckServicesRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and HealthCheckServicesList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1beta.IListRegionHealthCheckServicesRequest): Promise<google.cloud.compute.v1beta.HealthCheckServicesList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRegionHealthCheckServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionhealthcheckservicesrequest)`   
ListRegionHealthCheckServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.HealthCheckServicesList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.healthcheckserviceslist)>` | Promise  
  
### patch(request, callback)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchRegionHealthCheckServiceRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.PatchCallback): void;

Calls Patch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionhealthcheckservicerequest)`   
PatchRegionHealthCheckServiceRequest message or plain object  
`callback` |  `[PatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchRegionHealthCheckServiceRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Patch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPatchRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionhealthcheckservicerequest)`   
PatchRegionHealthCheckServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsRegionHealthCheckServiceRequest, callback: google.cloud.compute.v1beta.RegionHealthCheckServices.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionhealthcheckservicerequest)`   
TestIamPermissionsRegionHealthCheckServiceRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsRegionHealthCheckServiceRequest): Promise<google.cloud.compute.v1beta.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionHealthCheckServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionhealthcheckservicerequest)`   
TestIamPermissionsRegionHealthCheckServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
