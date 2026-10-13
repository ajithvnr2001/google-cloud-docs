---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.machineimages-class
title: Class protos.google.cloud.compute.v1.MachineImages (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:26.576276+00:00
---

# Class protos.google.cloud.compute.v1.MachineImages (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.machineimages-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.MachineImages (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a MachineImages

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1.MachineImages

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MachineImages service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MachineImages;

Creates new MachineImages service using the specified rpc implementation.

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
`[MachineImages](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.machineimages-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletemachineimagerequest)`   
DeleteMachineImageRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteMachineImageRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletemachineimagerequest)`   
DeleteMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1.IGetMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetmachineimagerequest)`   
GetMachineImageRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and MachineImage  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1.IGetMachineImageRequest): Promise<google.cloud.compute.v1.MachineImage>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetmachineimagerequest)`   
GetMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.MachineImage](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.machineimage-class)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.cloud.compute.v1.IGetIamPolicyMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetiampolicymachineimagerequest)`   
GetIamPolicyMachineImageRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.cloud.compute.v1.IGetIamPolicyMachineImageRequest): Promise<google.cloud.compute.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetiampolicymachineimagerequest)`   
GetIamPolicyMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.policy)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1.IInsertMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertmachineimagerequest)`   
InsertMachineImageRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1.IInsertMachineImageRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertmachineimagerequest)`   
InsertMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1.IListMachineImagesRequest, callback: google.cloud.compute.v1.MachineImages.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistmachineimagesrequest)`   
ListMachineImagesRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and MachineImageList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1.IListMachineImagesRequest): Promise<google.cloud.compute.v1.MachineImageList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMachineImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistmachineimagesrequest)`   
ListMachineImagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.MachineImageList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.machineimagelist)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.cloud.compute.v1.ISetIamPolicyMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetiampolicymachineimagerequest)`   
SetIamPolicyMachineImageRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.cloud.compute.v1.ISetIamPolicyMachineImageRequest): Promise<google.cloud.compute.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetiampolicymachineimagerequest)`   
SetIamPolicyMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.policy)>` | Promise  
  
### setLabels(request, callback)
    
    
    public setLabels(request: google.cloud.compute.v1.ISetLabelsMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.SetLabelsCallback): void;

Calls SetLabels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetlabelsmachineimagerequest)`   
SetLabelsMachineImageRequest message or plain object  
`callback` |  `[SetLabelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request)
    
    
    public setLabels(request: google.cloud.compute.v1.ISetLabelsMachineImageRequest): Promise<google.cloud.compute.v1.Operation>;

Calls SetLabels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetlabelsmachineimagerequest)`   
SetLabelsMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1.ITestIamPermissionsMachineImageRequest, callback: google.cloud.compute.v1.MachineImages.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.itestiampermissionsmachineimagerequest)`   
TestIamPermissionsMachineImageRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1.ITestIamPermissionsMachineImageRequest): Promise<google.cloud.compute.v1.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsMachineImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.itestiampermissionsmachineimagerequest)`   
TestIamPermissionsMachineImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.testpermissionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
