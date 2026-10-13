---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.configdelivery-class
title: Class protos.google.cloud.configdelivery.v1alpha.ConfigDelivery (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:34.126673+00:00
---

# Class protos.google.cloud.configdelivery.v1alpha.ConfigDelivery (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.configdelivery-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1alpha.ConfigDelivery (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a ConfigDelivery

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.configdelivery.v1alpha.ConfigDelivery

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
    
    
    public abortRollout(request: google.cloud.configdelivery.v1alpha.IAbortRolloutRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.AbortRolloutCallback): void;

Calls AbortRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAbortRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iabortrolloutrequest)`   
AbortRolloutRequest message or plain object  
`callback` |  `[AbortRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### abortRollout(request)
    
    
    public abortRollout(request: google.cloud.configdelivery.v1alpha.IAbortRolloutRequest): Promise<google.longrunning.Operation>;

Calls AbortRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAbortRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iabortrolloutrequest)`   
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
`[ConfigDelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.configdelivery-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFleetPackage(request, callback)
    
    
    public createFleetPackage(request: google.cloud.configdelivery.v1alpha.ICreateFleetPackageRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.CreateFleetPackageCallback): void;

Calls CreateFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatefleetpackagerequest)`   
CreateFleetPackageRequest message or plain object  
`callback` |  `[CreateFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFleetPackage(request)
    
    
    public createFleetPackage(request: google.cloud.configdelivery.v1alpha.ICreateFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls CreateFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatefleetpackagerequest)`   
CreateFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createRelease(request, callback)
    
    
    public createRelease(request: google.cloud.configdelivery.v1alpha.ICreateReleaseRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.CreateReleaseCallback): void;

Calls CreateRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
`callback` |  `[CreateReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRelease(request)
    
    
    public createRelease(request: google.cloud.configdelivery.v1alpha.ICreateReleaseRequest): Promise<google.longrunning.Operation>;

Calls CreateRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatereleaserequest)`   
CreateReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createResourceBundle(request, callback)
    
    
    public createResourceBundle(request: google.cloud.configdelivery.v1alpha.ICreateResourceBundleRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.CreateResourceBundleCallback): void;

Calls CreateResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreateresourcebundlerequest)`   
CreateResourceBundleRequest message or plain object  
`callback` |  `[CreateResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createResourceBundle(request)
    
    
    public createResourceBundle(request: google.cloud.configdelivery.v1alpha.ICreateResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls CreateResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreateresourcebundlerequest)`   
CreateResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### createVariant(request, callback)
    
    
    public createVariant(request: google.cloud.configdelivery.v1alpha.ICreateVariantRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.CreateVariantCallback): void;

Calls CreateVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatevariantrequest)`   
CreateVariantRequest message or plain object  
`callback` |  `[CreateVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVariant(request)
    
    
    public createVariant(request: google.cloud.configdelivery.v1alpha.ICreateVariantRequest): Promise<google.longrunning.Operation>;

Calls CreateVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.icreatevariantrequest)`   
CreateVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteFleetPackage(request, callback)
    
    
    public deleteFleetPackage(request: google.cloud.configdelivery.v1alpha.IDeleteFleetPackageRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.DeleteFleetPackageCallback): void;

Calls DeleteFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletefleetpackagerequest)`   
DeleteFleetPackageRequest message or plain object  
`callback` |  `[DeleteFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFleetPackage(request)
    
    
    public deleteFleetPackage(request: google.cloud.configdelivery.v1alpha.IDeleteFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls DeleteFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletefleetpackagerequest)`   
DeleteFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteRelease(request, callback)
    
    
    public deleteRelease(request: google.cloud.configdelivery.v1alpha.IDeleteReleaseRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.DeleteReleaseCallback): void;

Calls DeleteRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletereleaserequest)`   
DeleteReleaseRequest message or plain object  
`callback` |  `[DeleteReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRelease(request)
    
    
    public deleteRelease(request: google.cloud.configdelivery.v1alpha.IDeleteReleaseRequest): Promise<google.longrunning.Operation>;

Calls DeleteRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletereleaserequest)`   
DeleteReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteResourceBundle(request, callback)
    
    
    public deleteResourceBundle(request: google.cloud.configdelivery.v1alpha.IDeleteResourceBundleRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.DeleteResourceBundleCallback): void;

Calls DeleteResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideleteresourcebundlerequest)`   
DeleteResourceBundleRequest message or plain object  
`callback` |  `[DeleteResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteResourceBundle(request)
    
    
    public deleteResourceBundle(request: google.cloud.configdelivery.v1alpha.IDeleteResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls DeleteResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideleteresourcebundlerequest)`   
DeleteResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### deleteVariant(request, callback)
    
    
    public deleteVariant(request: google.cloud.configdelivery.v1alpha.IDeleteVariantRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.DeleteVariantCallback): void;

Calls DeleteVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletevariantrequest)`   
DeleteVariantRequest message or plain object  
`callback` |  `[DeleteVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVariant(request)
    
    
    public deleteVariant(request: google.cloud.configdelivery.v1alpha.IDeleteVariantRequest): Promise<google.longrunning.Operation>;

Calls DeleteVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ideletevariantrequest)`   
DeleteVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### getFleetPackage(request, callback)
    
    
    public getFleetPackage(request: google.cloud.configdelivery.v1alpha.IGetFleetPackageRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.GetFleetPackageCallback): void;

Calls GetFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetfleetpackagerequest)`   
GetFleetPackageRequest message or plain object  
`callback` |  `[GetFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and FleetPackage  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFleetPackage(request)
    
    
    public getFleetPackage(request: google.cloud.configdelivery.v1alpha.IGetFleetPackageRequest): Promise<google.cloud.configdelivery.v1alpha.FleetPackage>;

Calls GetFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetfleetpackagerequest)`   
GetFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.fleetpackage-class)>` | Promise  
  
### getRelease(request, callback)
    
    
    public getRelease(request: google.cloud.configdelivery.v1alpha.IGetReleaseRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.GetReleaseCallback): void;

Calls GetRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetreleaserequest)`   
GetReleaseRequest message or plain object  
`callback` |  `[GetReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Release  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRelease(request)
    
    
    public getRelease(request: google.cloud.configdelivery.v1alpha.IGetReleaseRequest): Promise<google.cloud.configdelivery.v1alpha.Release>;

Calls GetRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetreleaserequest)`   
GetReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.Release](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.release-class)>` | Promise  
  
### getResourceBundle(request, callback)
    
    
    public getResourceBundle(request: google.cloud.configdelivery.v1alpha.IGetResourceBundleRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.GetResourceBundleCallback): void;

Calls GetResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetresourcebundlerequest)`   
GetResourceBundleRequest message or plain object  
`callback` |  `[GetResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ResourceBundle  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResourceBundle(request)
    
    
    public getResourceBundle(request: google.cloud.configdelivery.v1alpha.IGetResourceBundleRequest): Promise<google.cloud.configdelivery.v1alpha.ResourceBundle>;

Calls GetResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetresourcebundlerequest)`   
GetResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ResourceBundle](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.resourcebundle)>` | Promise  
  
### getRollout(request, callback)
    
    
    public getRollout(request: google.cloud.configdelivery.v1alpha.IGetRolloutRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.GetRolloutCallback): void;

Calls GetRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
`callback` |  `[GetRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Rollout  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRollout(request)
    
    
    public getRollout(request: google.cloud.configdelivery.v1alpha.IGetRolloutRequest): Promise<google.cloud.configdelivery.v1alpha.Rollout>;

Calls GetRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetrolloutrequest)`   
GetRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.Rollout](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.rollout)>` | Promise  
  
### getVariant(request, callback)
    
    
    public getVariant(request: google.cloud.configdelivery.v1alpha.IGetVariantRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.GetVariantCallback): void;

Calls GetVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetvariantrequest)`   
GetVariantRequest message or plain object  
`callback` |  `[GetVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Variant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVariant(request)
    
    
    public getVariant(request: google.cloud.configdelivery.v1alpha.IGetVariantRequest): Promise<google.cloud.configdelivery.v1alpha.Variant>;

Calls GetVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.igetvariantrequest)`   
GetVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.variant)>` | Promise  
  
### listFleetPackages(request, callback)
    
    
    public listFleetPackages(request: google.cloud.configdelivery.v1alpha.IListFleetPackagesRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ListFleetPackagesCallback): void;

Calls ListFleetPackages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFleetPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistfleetpackagesrequest)`   
ListFleetPackagesRequest message or plain object  
`callback` |  `[ListFleetPackagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFleetPackagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFleetPackages(request)
    
    
    public listFleetPackages(request: google.cloud.configdelivery.v1alpha.IListFleetPackagesRequest): Promise<google.cloud.configdelivery.v1alpha.ListFleetPackagesResponse>;

Calls ListFleetPackages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFleetPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistfleetpackagesrequest)`   
ListFleetPackagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ListFleetPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.listfleetpackagesresponse)>` | Promise  
  
### listReleases(request, callback)
    
    
    public listReleases(request: google.cloud.configdelivery.v1alpha.IListReleasesRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ListReleasesCallback): void;

Calls ListReleases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
`callback` |  `[ListReleasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReleasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleases(request)
    
    
    public listReleases(request: google.cloud.configdelivery.v1alpha.IListReleasesRequest): Promise<google.cloud.configdelivery.v1alpha.ListReleasesResponse>;

Calls ListReleases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistreleasesrequest)`   
ListReleasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.listreleasesresponse)>` | Promise  
  
### listResourceBundles(request, callback)
    
    
    public listResourceBundles(request: google.cloud.configdelivery.v1alpha.IListResourceBundlesRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ListResourceBundlesCallback): void;

Calls ListResourceBundles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourceBundlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistresourcebundlesrequest)`   
ListResourceBundlesRequest message or plain object  
`callback` |  `[ListResourceBundlesCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourceBundlesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResourceBundles(request)
    
    
    public listResourceBundles(request: google.cloud.configdelivery.v1alpha.IListResourceBundlesRequest): Promise<google.cloud.configdelivery.v1alpha.ListResourceBundlesResponse>;

Calls ListResourceBundles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourceBundlesRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistresourcebundlesrequest)`   
ListResourceBundlesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ListResourceBundlesResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.listresourcebundlesresponse)>` | Promise  
  
### listRollouts(request, callback)
    
    
    public listRollouts(request: google.cloud.configdelivery.v1alpha.IListRolloutsRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ListRolloutsCallback): void;

Calls ListRollouts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
`callback` |  `[ListRolloutsCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRolloutsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRollouts(request)
    
    
    public listRollouts(request: google.cloud.configdelivery.v1alpha.IListRolloutsRequest): Promise<google.cloud.configdelivery.v1alpha.ListRolloutsResponse>;

Calls ListRollouts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistrolloutsrequest)`   
ListRolloutsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.listrolloutsresponse)>` | Promise  
  
### listVariants(request, callback)
    
    
    public listVariants(request: google.cloud.configdelivery.v1alpha.IListVariantsRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ListVariantsCallback): void;

Calls ListVariants.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVariantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistvariantsrequest)`   
ListVariantsRequest message or plain object  
`callback` |  `[ListVariantsCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and ListVariantsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVariants(request)
    
    
    public listVariants(request: google.cloud.configdelivery.v1alpha.IListVariantsRequest): Promise<google.cloud.configdelivery.v1alpha.ListVariantsResponse>;

Calls ListVariants.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVariantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.ilistvariantsrequest)`   
ListVariantsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.configdelivery.v1alpha.ListVariantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.listvariantsresponse)>` | Promise  
  
### resumeRollout(request, callback)
    
    
    public resumeRollout(request: google.cloud.configdelivery.v1alpha.IResumeRolloutRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.ResumeRolloutCallback): void;

Calls ResumeRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iresumerolloutrequest)`   
ResumeRolloutRequest message or plain object  
`callback` |  `[ResumeRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeRollout(request)
    
    
    public resumeRollout(request: google.cloud.configdelivery.v1alpha.IResumeRolloutRequest): Promise<google.longrunning.Operation>;

Calls ResumeRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iresumerolloutrequest)`   
ResumeRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### suspendRollout(request, callback)
    
    
    public suspendRollout(request: google.cloud.configdelivery.v1alpha.ISuspendRolloutRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.SuspendRolloutCallback): void;

Calls SuspendRollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuspendRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.isuspendrolloutrequest)`   
SuspendRolloutRequest message or plain object  
`callback` |  `[SuspendRolloutCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suspendRollout(request)
    
    
    public suspendRollout(request: google.cloud.configdelivery.v1alpha.ISuspendRolloutRequest): Promise<google.longrunning.Operation>;

Calls SuspendRollout.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISuspendRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.isuspendrolloutrequest)`   
SuspendRolloutRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateFleetPackage(request, callback)
    
    
    public updateFleetPackage(request: google.cloud.configdelivery.v1alpha.IUpdateFleetPackageRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.UpdateFleetPackageCallback): void;

Calls UpdateFleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatefleetpackagerequest)`   
UpdateFleetPackageRequest message or plain object  
`callback` |  `[UpdateFleetPackageCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFleetPackage(request)
    
    
    public updateFleetPackage(request: google.cloud.configdelivery.v1alpha.IUpdateFleetPackageRequest): Promise<google.longrunning.Operation>;

Calls UpdateFleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFleetPackageRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatefleetpackagerequest)`   
UpdateFleetPackageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateRelease(request, callback)
    
    
    public updateRelease(request: google.cloud.configdelivery.v1alpha.IUpdateReleaseRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.UpdateReleaseCallback): void;

Calls UpdateRelease.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatereleaserequest)`   
UpdateReleaseRequest message or plain object  
`callback` |  `[UpdateReleaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRelease(request)
    
    
    public updateRelease(request: google.cloud.configdelivery.v1alpha.IUpdateReleaseRequest): Promise<google.longrunning.Operation>;

Calls UpdateRelease.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatereleaserequest)`   
UpdateReleaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateResourceBundle(request, callback)
    
    
    public updateResourceBundle(request: google.cloud.configdelivery.v1alpha.IUpdateResourceBundleRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.UpdateResourceBundleCallback): void;

Calls UpdateResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdateresourcebundlerequest)`   
UpdateResourceBundleRequest message or plain object  
`callback` |  `[UpdateResourceBundleCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateResourceBundle(request)
    
    
    public updateResourceBundle(request: google.cloud.configdelivery.v1alpha.IUpdateResourceBundleRequest): Promise<google.longrunning.Operation>;

Calls UpdateResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateResourceBundleRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdateresourcebundlerequest)`   
UpdateResourceBundleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
### updateVariant(request, callback)
    
    
    public updateVariant(request: google.cloud.configdelivery.v1alpha.IUpdateVariantRequest, callback: google.cloud.configdelivery.v1alpha.ConfigDelivery.UpdateVariantCallback): void;

Calls UpdateVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatevariantrequest)`   
UpdateVariantRequest message or plain object  
`callback` |  `[UpdateVariantCallback](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateVariant(request)
    
    
    public updateVariant(request: google.cloud.configdelivery.v1alpha.IUpdateVariantRequest): Promise<google.longrunning.Operation>;

Calls UpdateVariant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVariantRequest](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1alpha.iupdatevariantrequest)`   
UpdateVariantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
