---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxies-class
title: Class protos.google.cloud.compute.v1beta.TargetHttpsProxies (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:46.070924+00:00
---

# Class protos.google.cloud.compute.v1beta.TargetHttpsProxies (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxies-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.TargetHttpsProxies (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a TargetHttpsProxies

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.TargetHttpsProxies

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new TargetHttpsProxies service.

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
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListTargetHttpsProxiesRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.AggregatedListCallback): void;

Calls AggregatedList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListTargetHttpsProxiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlisttargethttpsproxiesrequest)`   
AggregatedListTargetHttpsProxiesRequest message or plain object  
`callback` |  `[AggregatedListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TargetHttpsProxyAggregatedList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregatedList(request)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListTargetHttpsProxiesRequest): Promise<google.cloud.compute.v1beta.TargetHttpsProxyAggregatedList>;

Calls AggregatedList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListTargetHttpsProxiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlisttargethttpsproxiesrequest)`   
AggregatedListTargetHttpsProxiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TargetHttpsProxyAggregatedList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxyaggregatedlist)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): TargetHttpsProxies;

Creates new TargetHttpsProxies service using the specified rpc implementation.

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
`[TargetHttpsProxies](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxies-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletetargethttpsproxyrequest)`   
DeleteTargetHttpsProxyRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletetargethttpsproxyrequest)`   
DeleteTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igettargethttpsproxyrequest)`   
GetTargetHttpsProxyRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TargetHttpsProxy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.TargetHttpsProxy>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igettargethttpsproxyrequest)`   
GetTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TargetHttpsProxy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxy-class)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinserttargethttpsproxyrequest)`   
InsertTargetHttpsProxyRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinserttargethttpsproxyrequest)`   
InsertTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1beta.IListTargetHttpsProxiesRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetHttpsProxiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilisttargethttpsproxiesrequest)`   
ListTargetHttpsProxiesRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TargetHttpsProxyList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1beta.IListTargetHttpsProxiesRequest): Promise<google.cloud.compute.v1beta.TargetHttpsProxyList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTargetHttpsProxiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilisttargethttpsproxiesrequest)`   
ListTargetHttpsProxiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TargetHttpsProxyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.targethttpsproxylist)>` | Promise  
  
### patch(request, callback)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.PatchCallback): void;

Calls Patch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchtargethttpsproxyrequest)`   
PatchTargetHttpsProxyRequest message or plain object  
`callback` |  `[PatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request)
    
    
    public patch(request: google.cloud.compute.v1beta.IPatchTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Patch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPatchTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchtargethttpsproxyrequest)`   
PatchTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setCertificateMap(request, callback)
    
    
    public setCertificateMap(request: google.cloud.compute.v1beta.ISetCertificateMapTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.SetCertificateMapCallback): void;

Calls SetCertificateMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetCertificateMapTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcertificatemaptargethttpsproxyrequest)`   
SetCertificateMapTargetHttpsProxyRequest message or plain object  
`callback` |  `[SetCertificateMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setCertificateMap(request)
    
    
    public setCertificateMap(request: google.cloud.compute.v1beta.ISetCertificateMapTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetCertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetCertificateMapTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcertificatemaptargethttpsproxyrequest)`   
SetCertificateMapTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setQuicOverride(request, callback)
    
    
    public setQuicOverride(request: google.cloud.compute.v1beta.ISetQuicOverrideTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.SetQuicOverrideCallback): void;

Calls SetQuicOverride.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetQuicOverrideTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetquicoverridetargethttpsproxyrequest)`   
SetQuicOverrideTargetHttpsProxyRequest message or plain object  
`callback` |  `[SetQuicOverrideCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setQuicOverride(request)
    
    
    public setQuicOverride(request: google.cloud.compute.v1beta.ISetQuicOverrideTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetQuicOverride.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetQuicOverrideTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetquicoverridetargethttpsproxyrequest)`   
SetQuicOverrideTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setSslCertificates(request, callback)
    
    
    public setSslCertificates(request: google.cloud.compute.v1beta.ISetSslCertificatesTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.SetSslCertificatesCallback): void;

Calls SetSslCertificates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetSslCertificatesTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetsslcertificatestargethttpsproxyrequest)`   
SetSslCertificatesTargetHttpsProxyRequest message or plain object  
`callback` |  `[SetSslCertificatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setSslCertificates(request)
    
    
    public setSslCertificates(request: google.cloud.compute.v1beta.ISetSslCertificatesTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetSslCertificates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetSslCertificatesTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetsslcertificatestargethttpsproxyrequest)`   
SetSslCertificatesTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setSslPolicy(request, callback)
    
    
    public setSslPolicy(request: google.cloud.compute.v1beta.ISetSslPolicyTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.SetSslPolicyCallback): void;

Calls SetSslPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetSslPolicyTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetsslpolicytargethttpsproxyrequest)`   
SetSslPolicyTargetHttpsProxyRequest message or plain object  
`callback` |  `[SetSslPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setSslPolicy(request)
    
    
    public setSslPolicy(request: google.cloud.compute.v1beta.ISetSslPolicyTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetSslPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetSslPolicyTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetsslpolicytargethttpsproxyrequest)`   
SetSslPolicyTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setUrlMap(request, callback)
    
    
    public setUrlMap(request: google.cloud.compute.v1beta.ISetUrlMapTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.SetUrlMapCallback): void;

Calls SetUrlMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetUrlMapTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iseturlmaptargethttpsproxyrequest)`   
SetUrlMapTargetHttpsProxyRequest message or plain object  
`callback` |  `[SetUrlMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setUrlMap(request)
    
    
    public setUrlMap(request: google.cloud.compute.v1beta.ISetUrlMapTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetUrlMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetUrlMapTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iseturlmaptargethttpsproxyrequest)`   
SetUrlMapTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsTargetHttpsProxyRequest, callback: google.cloud.compute.v1beta.TargetHttpsProxies.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionstargethttpsproxyrequest)`   
TestIamPermissionsTargetHttpsProxyRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsTargetHttpsProxyRequest): Promise<google.cloud.compute.v1beta.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsTargetHttpsProxyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionstargethttpsproxyrequest)`   
TestIamPermissionsTargetHttpsProxyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
