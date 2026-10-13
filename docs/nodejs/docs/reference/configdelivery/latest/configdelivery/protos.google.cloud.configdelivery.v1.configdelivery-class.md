---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.configdelivery-class
title: Class protos.google.cloud.configdelivery.v1.ConfigDelivery (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:24.123088+00:00
---

# Class protos.google.cloud.configdelivery.v1.ConfigDelivery (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.configdelivery-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1.ConfigDelivery (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a ConfigDelivery

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.configdelivery.v1.ConfigDelivery

## Package

[@google-cloud/configdelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConfigDelivery service.

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

### abortRollout(request, callback)
    
    
    public abortRollout(request: google.cloud.configdelivery.v1.IAbortRolloutRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.AbortRolloutCallback): void;

Calls AbortRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAbortRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iabortrolloutrequest)`   
AbortRolloutRequest message or plain object  
`callback` |  `[AbortRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### abortRollout(request)
    
    
    public abortRollout(request: google.cloud.configdelivery.v1.IAbortRolloutRequest): Promise<google.longrunning.Operation>;

Calls AbortRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAbortRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iabortrolloutrequest)`   
AbortRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConfigDelivery;

Creates new ConfigDelivery service using the specified rpc implementation.

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
`[ConfigDelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.configdelivery-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFleetPackage(request, callback)
    
    
    public createFleetPackage(request: google.cloud.configdelivery.v1.ICreateFleetPackageRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.CreateFleetPackageCallback): void;

Calls CreateFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatefleetpackagerequest)`   
CreateFleetPackageRequest message or plain object  
`callback` |  `[CreateFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFleetPackage(request)
    
    
    public createFleetPackage(request: google.cloud.configdelivery.v1.ICreateFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls CreateFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatefleetpackagerequest)`   
CreateFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createRelease(request, callback)
    
    
    public createRelease(request: google.cloud.configdelivery.v1.ICreateReleaseRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.CreateReleaseCallback): void;

Calls CreateRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
`callback` |  `[CreateReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRelease(request)
    
    
    public createRelease(request: google.cloud.configdelivery.v1.ICreateReleaseRequest): Promise<google.longrunning.Operation>;

Calls CreateRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createResourceBundle(request, callback)
    
    
    public createResourceBundle(request: google.cloud.configdelivery.v1.ICreateResourceBundleRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.CreateResourceBundleCallback): void;

Calls CreateResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreateresourcebundlerequest)`   
CreateResourceBundleRequest message or plain object  
`callback` |  `[CreateResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createResourceBundle(request)
    
    
    public createResourceBundle(request: google.cloud.configdelivery.v1.ICreateResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls CreateResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreateresourcebundlerequest)`   
CreateResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createVariant(request, callback)
    
    
    public createVariant(request: google.cloud.configdelivery.v1.ICreateVariantRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.CreateVariantCallback): void;

Calls CreateVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatevariantrequest)`   
CreateVariantRequest message or plain object  
`callback` |  `[CreateVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVariant(request)
    
    
    public createVariant(request: google.cloud.configdelivery.v1.ICreateVariantRequest): Promise<google.longrunning.Operation>;

Calls CreateVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.icreatevariantrequest)`   
CreateVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteFleetPackage(request, callback)
    
    
    public deleteFleetPackage(request: google.cloud.configdelivery.v1.IDeleteFleetPackageRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.DeleteFleetPackageCallback): void;

Calls DeleteFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletefleetpackagerequest)`   
DeleteFleetPackageRequest message or plain object  
`callback` |  `[DeleteFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFleetPackage(request)
    
    
    public deleteFleetPackage(request: google.cloud.configdelivery.v1.IDeleteFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls DeleteFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletefleetpackagerequest)`   
DeleteFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteRelease(request, callback)
    
    
    public deleteRelease(request: google.cloud.configdelivery.v1.IDeleteReleaseRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.DeleteReleaseCallback): void;

Calls DeleteRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletereleaserequest)`   
DeleteReleaseRequest message or plain object  
`callback` |  `[DeleteReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRelease(request)
    
    
    public deleteRelease(request: google.cloud.configdelivery.v1.IDeleteReleaseRequest): Promise<google.longrunning.Operation>;

Calls DeleteRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletereleaserequest)`   
DeleteReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteResourceBundle(request, callback)
    
    
    public deleteResourceBundle(request: google.cloud.configdelivery.v1.IDeleteResourceBundleRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.DeleteResourceBundleCallback): void;

Calls DeleteResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideleteresourcebundlerequest)`   
DeleteResourceBundleRequest message or plain object  
`callback` |  `[DeleteResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteResourceBundle(request)
    
    
    public deleteResourceBundle(request: google.cloud.configdelivery.v1.IDeleteResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls DeleteResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideleteresourcebundlerequest)`   
DeleteResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteVariant(request, callback)
    
    
    public deleteVariant(request: google.cloud.configdelivery.v1.IDeleteVariantRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.DeleteVariantCallback): void;

Calls DeleteVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletevariantrequest)`   
DeleteVariantRequest message or plain object  
`callback` |  `[DeleteVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVariant(request)
    
    
    public deleteVariant(request: google.cloud.configdelivery.v1.IDeleteVariantRequest): Promise<google.longrunning.Operation>;

Calls DeleteVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ideletevariantrequest)`   
DeleteVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### getFleetPackage(request, callback)
    
    
    public getFleetPackage(request: google.cloud.configdelivery.v1.IGetFleetPackageRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.GetFleetPackageCallback): void;

Calls GetFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetfleetpackagerequest)`   
GetFleetPackageRequest message or plain object  
`callback` |  `[GetFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and FleetPackage  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFleetPackage(request)
    
    
    public getFleetPackage(request: google.cloud.configdelivery.v1.IGetFleetPackageRequest): Promise<google.cloud.configdelivery.v1.FleetPackage>;

Calls GetFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetfleetpackagerequest)`   
GetFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.fleetpackage-class)>` | Promise  
  
### getRelease(request, callback)
    
    
    public getRelease(request: google.cloud.configdelivery.v1.IGetReleaseRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.GetReleaseCallback): void;

Calls GetRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetreleaserequest)`   
GetReleaseRequest message or plain object  
`callback` |  `[GetReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Release  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRelease(request)
    
    
    public getRelease(request: google.cloud.configdelivery.v1.IGetReleaseRequest): Promise<google.cloud.configdelivery.v1.Release>;

Calls GetRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetreleaserequest)`   
GetReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.Release](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.release-class)>` | Promise  
  
### getResourceBundle(request, callback)
    
    
    public getResourceBundle(request: google.cloud.configdelivery.v1.IGetResourceBundleRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.GetResourceBundleCallback): void;

Calls GetResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetresourcebundlerequest)`   
GetResourceBundleRequest message or plain object  
`callback` |  `[GetResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ResourceBundle  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResourceBundle(request)
    
    
    public getResourceBundle(request: google.cloud.configdelivery.v1.IGetResourceBundleRequest): Promise<google.cloud.configdelivery.v1.ResourceBundle>;

Calls GetResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetresourcebundlerequest)`   
GetResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ResourceBundle](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.resourcebundle)>` | Promise  
  
### getRollout(request, callback)
    
    
    public getRollout(request: google.cloud.configdelivery.v1.IGetRolloutRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.GetRolloutCallback): void;

Calls GetRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
`callback` |  `[GetRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Rollout  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRollout(request)
    
    
    public getRollout(request: google.cloud.configdelivery.v1.IGetRolloutRequest): Promise<google.cloud.configdelivery.v1.Rollout>;

Calls GetRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.Rollout](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rollout)>` | Promise  
  
### getVariant(request, callback)
    
    
    public getVariant(request: google.cloud.configdelivery.v1.IGetVariantRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.GetVariantCallback): void;

Calls GetVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetvariantrequest)`   
GetVariantRequest message or plain object  
`callback` |  `[GetVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Variant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVariant(request)
    
    
    public getVariant(request: google.cloud.configdelivery.v1.IGetVariantRequest): Promise<google.cloud.configdelivery.v1.Variant>;

Calls GetVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.igetvariantrequest)`   
GetVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)>` | Promise  
  
### listFleetPackages(request, callback)
    
    
    public listFleetPackages(request: google.cloud.configdelivery.v1.IListFleetPackagesRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ListFleetPackagesCallback): void;

Calls ListFleetPackages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFleetPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistfleetpackagesrequest)`   
ListFleetPackagesRequest message or plain object  
`callback` |  `[ListFleetPackagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFleetPackagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFleetPackages(request)
    
    
    public listFleetPackages(request: google.cloud.configdelivery.v1.IListFleetPackagesRequest): Promise<google.cloud.configdelivery.v1.ListFleetPackagesResponse>;

Calls ListFleetPackages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFleetPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistfleetpackagesrequest)`   
ListFleetPackagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ListFleetPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.listfleetpackagesresponse)>` | Promise  
  
### listReleases(request, callback)
    
    
    public listReleases(request: google.cloud.configdelivery.v1.IListReleasesRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ListReleasesCallback): void;

Calls ListReleases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
`callback` |  `[ListReleasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReleasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleases(request)
    
    
    public listReleases(request: google.cloud.configdelivery.v1.IListReleasesRequest): Promise<google.cloud.configdelivery.v1.ListReleasesResponse>;

Calls ListReleases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.listreleasesresponse)>` | Promise  
  
### listResourceBundles(request, callback)
    
    
    public listResourceBundles(request: google.cloud.configdelivery.v1.IListResourceBundlesRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ListResourceBundlesCallback): void;

Calls ListResourceBundles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourceBundlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistresourcebundlesrequest)`   
ListResourceBundlesRequest message or plain object  
`callback` |  `[ListResourceBundlesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourceBundlesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResourceBundles(request)
    
    
    public listResourceBundles(request: google.cloud.configdelivery.v1.IListResourceBundlesRequest): Promise<google.cloud.configdelivery.v1.ListResourceBundlesResponse>;

Calls ListResourceBundles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourceBundlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistresourcebundlesrequest)`   
ListResourceBundlesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ListResourceBundlesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.listresourcebundlesresponse)>` | Promise  
  
### listRollouts(request, callback)
    
    
    public listRollouts(request: google.cloud.configdelivery.v1.IListRolloutsRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ListRolloutsCallback): void;

Calls ListRollouts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
`callback` |  `[ListRolloutsCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRolloutsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRollouts(request)
    
    
    public listRollouts(request: google.cloud.configdelivery.v1.IListRolloutsRequest): Promise<google.cloud.configdelivery.v1.ListRolloutsResponse>;

Calls ListRollouts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.listrolloutsresponse)>` | Promise  
  
### listVariants(request, callback)
    
    
    public listVariants(request: google.cloud.configdelivery.v1.IListVariantsRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ListVariantsCallback): void;

Calls ListVariants.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVariantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistvariantsrequest)`   
ListVariantsRequest message or plain object  
`callback` |  `[ListVariantsCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListVariantsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVariants(request)
    
    
    public listVariants(request: google.cloud.configdelivery.v1.IListVariantsRequest): Promise<google.cloud.configdelivery.v1.ListVariantsResponse>;

Calls ListVariants.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVariantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ilistvariantsrequest)`   
ListVariantsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1.ListVariantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.listvariantsresponse)>` | Promise  
  
### resumeRollout(request, callback)
    
    
    public resumeRollout(request: google.cloud.configdelivery.v1.IResumeRolloutRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.ResumeRolloutCallback): void;

Calls ResumeRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iresumerolloutrequest)`   
ResumeRolloutRequest message or plain object  
`callback` |  `[ResumeRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeRollout(request)
    
    
    public resumeRollout(request: google.cloud.configdelivery.v1.IResumeRolloutRequest): Promise<google.longrunning.Operation>;

Calls ResumeRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iresumerolloutrequest)`   
ResumeRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### suspendRollout(request, callback)
    
    
    public suspendRollout(request: google.cloud.configdelivery.v1.ISuspendRolloutRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.SuspendRolloutCallback): void;

Calls SuspendRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuspendRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.isuspendrolloutrequest)`   
SuspendRolloutRequest message or plain object  
`callback` |  `[SuspendRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suspendRollout(request)
    
    
    public suspendRollout(request: google.cloud.configdelivery.v1.ISuspendRolloutRequest): Promise<google.longrunning.Operation>;

Calls SuspendRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISuspendRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.isuspendrolloutrequest)`   
SuspendRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateFleetPackage(request, callback)
    
    
    public updateFleetPackage(request: google.cloud.configdelivery.v1.IUpdateFleetPackageRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.UpdateFleetPackageCallback): void;

Calls UpdateFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatefleetpackagerequest)`   
UpdateFleetPackageRequest message or plain object  
`callback` |  `[UpdateFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFleetPackage(request)
    
    
    public updateFleetPackage(request: google.cloud.configdelivery.v1.IUpdateFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls UpdateFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatefleetpackagerequest)`   
UpdateFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateRelease(request, callback)
    
    
    public updateRelease(request: google.cloud.configdelivery.v1.IUpdateReleaseRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.UpdateReleaseCallback): void;

Calls UpdateRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatereleaserequest)`   
UpdateReleaseRequest message or plain object  
`callback` |  `[UpdateReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRelease(request)
    
    
    public updateRelease(request: google.cloud.configdelivery.v1.IUpdateReleaseRequest): Promise<google.longrunning.Operation>;

Calls UpdateRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatereleaserequest)`   
UpdateReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateResourceBundle(request, callback)
    
    
    public updateResourceBundle(request: google.cloud.configdelivery.v1.IUpdateResourceBundleRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.UpdateResourceBundleCallback): void;

Calls UpdateResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdateresourcebundlerequest)`   
UpdateResourceBundleRequest message or plain object  
`callback` |  `[UpdateResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateResourceBundle(request)
    
    
    public updateResourceBundle(request: google.cloud.configdelivery.v1.IUpdateResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls UpdateResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdateresourcebundlerequest)`   
UpdateResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateVariant(request, callback)
    
    
    public updateVariant(request: google.cloud.configdelivery.v1.IUpdateVariantRequest, callback: google.cloud.configdelivery.v1.ConfigDelivery.UpdateVariantCallback): void;

Calls UpdateVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatevariantrequest)`   
UpdateVariantRequest message or plain object  
`callback` |  `[UpdateVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateVariant(request)
    
    
    public updateVariant(request: google.cloud.configdelivery.v1.IUpdateVariantRequest): Promise<google.longrunning.Operation>;

Calls UpdateVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.iupdatevariantrequest)`   
UpdateVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
