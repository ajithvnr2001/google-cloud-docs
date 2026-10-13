---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.projects-class
title: Class protos.google.cloud.compute.v1beta.Projects (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:25.168365+00:00
---

# Class protos.google.cloud.compute.v1beta.Projects (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.projects-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.Projects (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a Projects

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.Projects

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Projects service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Projects;

Creates new Projects service using the specified rpc implementation.

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
`[Projects](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.projects-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### disableXpnHost(request, callback)
    
    
    public disableXpnHost(request: google.cloud.compute.v1beta.IDisableXpnHostProjectRequest, callback: google.cloud.compute.v1beta.Projects.DisableXpnHostCallback): void;

Calls DisableXpnHost.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.idisablexpnhostprojectrequest)`   
DisableXpnHostProjectRequest message or plain object  
`callback` |  `[DisableXpnHostCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableXpnHost(request)
    
    
    public disableXpnHost(request: google.cloud.compute.v1beta.IDisableXpnHostProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls DisableXpnHost.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.idisablexpnhostprojectrequest)`   
DisableXpnHostProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### disableXpnResource(request, callback)
    
    
    public disableXpnResource(request: google.cloud.compute.v1beta.IDisableXpnResourceProjectRequest, callback: google.cloud.compute.v1beta.Projects.DisableXpnResourceCallback): void;

Calls DisableXpnResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableXpnResourceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.idisablexpnresourceprojectrequest)`   
DisableXpnResourceProjectRequest message or plain object  
`callback` |  `[DisableXpnResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableXpnResource(request)
    
    
    public disableXpnResource(request: google.cloud.compute.v1beta.IDisableXpnResourceProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls DisableXpnResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableXpnResourceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.idisablexpnresourceprojectrequest)`   
DisableXpnResourceProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### enableXpnHost(request, callback)
    
    
    public enableXpnHost(request: google.cloud.compute.v1beta.IEnableXpnHostProjectRequest, callback: google.cloud.compute.v1beta.Projects.EnableXpnHostCallback): void;

Calls EnableXpnHost.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ienablexpnhostprojectrequest)`   
EnableXpnHostProjectRequest message or plain object  
`callback` |  `[EnableXpnHostCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableXpnHost(request)
    
    
    public enableXpnHost(request: google.cloud.compute.v1beta.IEnableXpnHostProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls EnableXpnHost.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ienablexpnhostprojectrequest)`   
EnableXpnHostProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### enableXpnResource(request, callback)
    
    
    public enableXpnResource(request: google.cloud.compute.v1beta.IEnableXpnResourceProjectRequest, callback: google.cloud.compute.v1beta.Projects.EnableXpnResourceCallback): void;

Calls EnableXpnResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableXpnResourceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ienablexpnresourceprojectrequest)`   
EnableXpnResourceProjectRequest message or plain object  
`callback` |  `[EnableXpnResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableXpnResource(request)
    
    
    public enableXpnResource(request: google.cloud.compute.v1beta.IEnableXpnResourceProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls EnableXpnResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableXpnResourceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ienablexpnresourceprojectrequest)`   
EnableXpnResourceProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetProjectRequest, callback: google.cloud.compute.v1beta.Projects.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetprojectrequest)`   
GetProjectRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Project  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetProjectRequest): Promise<google.cloud.compute.v1beta.Project>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetprojectrequest)`   
GetProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Project](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.project-class)>` | Promise  
  
### getXpnHost(request, callback)
    
    
    public getXpnHost(request: google.cloud.compute.v1beta.IGetXpnHostProjectRequest, callback: google.cloud.compute.v1beta.Projects.GetXpnHostCallback): void;

Calls GetXpnHost.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetxpnhostprojectrequest)`   
GetXpnHostProjectRequest message or plain object  
`callback` |  `[GetXpnHostCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Project  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getXpnHost(request)
    
    
    public getXpnHost(request: google.cloud.compute.v1beta.IGetXpnHostProjectRequest): Promise<google.cloud.compute.v1beta.Project>;

Calls GetXpnHost.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetXpnHostProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetxpnhostprojectrequest)`   
GetXpnHostProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Project](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.project-class)>` | Promise  
  
### getXpnResources(request, callback)
    
    
    public getXpnResources(request: google.cloud.compute.v1beta.IGetXpnResourcesProjectsRequest, callback: google.cloud.compute.v1beta.Projects.GetXpnResourcesCallback): void;

Calls GetXpnResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetXpnResourcesProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetxpnresourcesprojectsrequest)`   
GetXpnResourcesProjectsRequest message or plain object  
`callback` |  `[GetXpnResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and ProjectsGetXpnResources  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getXpnResources(request)
    
    
    public getXpnResources(request: google.cloud.compute.v1beta.IGetXpnResourcesProjectsRequest): Promise<google.cloud.compute.v1beta.ProjectsGetXpnResources>;

Calls GetXpnResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetXpnResourcesProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetxpnresourcesprojectsrequest)`   
GetXpnResourcesProjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.ProjectsGetXpnResources](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.projectsgetxpnresources)>` | Promise  
  
### listXpnHosts(request, callback)
    
    
    public listXpnHosts(request: google.cloud.compute.v1beta.IListXpnHostsProjectsRequest, callback: google.cloud.compute.v1beta.Projects.ListXpnHostsCallback): void;

Calls ListXpnHosts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListXpnHostsProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistxpnhostsprojectsrequest)`   
ListXpnHostsProjectsRequest message or plain object  
`callback` |  `[ListXpnHostsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and XpnHostList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listXpnHosts(request)
    
    
    public listXpnHosts(request: google.cloud.compute.v1beta.IListXpnHostsProjectsRequest): Promise<google.cloud.compute.v1beta.XpnHostList>;

Calls ListXpnHosts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListXpnHostsProjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistxpnhostsprojectsrequest)`   
ListXpnHostsProjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.XpnHostList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.xpnhostlist)>` | Promise  
  
### moveDisk(request, callback)
    
    
    public moveDisk(request: google.cloud.compute.v1beta.IMoveDiskProjectRequest, callback: google.cloud.compute.v1beta.Projects.MoveDiskCallback): void;

Calls MoveDisk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveDiskProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovediskprojectrequest)`   
MoveDiskProjectRequest message or plain object  
`callback` |  `[MoveDiskCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveDisk(request)
    
    
    public moveDisk(request: google.cloud.compute.v1beta.IMoveDiskProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls MoveDisk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveDiskProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovediskprojectrequest)`   
MoveDiskProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### moveInstance(request, callback)
    
    
    public moveInstance(request: google.cloud.compute.v1beta.IMoveInstanceProjectRequest, callback: google.cloud.compute.v1beta.Projects.MoveInstanceCallback): void;

Calls MoveInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveInstanceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imoveinstanceprojectrequest)`   
MoveInstanceProjectRequest message or plain object  
`callback` |  `[MoveInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveInstance(request)
    
    
    public moveInstance(request: google.cloud.compute.v1beta.IMoveInstanceProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls MoveInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveInstanceProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imoveinstanceprojectrequest)`   
MoveInstanceProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setCloudArmorTier(request, callback)
    
    
    public setCloudArmorTier(request: google.cloud.compute.v1beta.ISetCloudArmorTierProjectRequest, callback: google.cloud.compute.v1beta.Projects.SetCloudArmorTierCallback): void;

Calls SetCloudArmorTier.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetCloudArmorTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcloudarmortierprojectrequest)`   
SetCloudArmorTierProjectRequest message or plain object  
`callback` |  `[SetCloudArmorTierCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setCloudArmorTier(request)
    
    
    public setCloudArmorTier(request: google.cloud.compute.v1beta.ISetCloudArmorTierProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetCloudArmorTier.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetCloudArmorTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcloudarmortierprojectrequest)`   
SetCloudArmorTierProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setCommonInstanceMetadata(request, callback)
    
    
    public setCommonInstanceMetadata(request: google.cloud.compute.v1beta.ISetCommonInstanceMetadataProjectRequest, callback: google.cloud.compute.v1beta.Projects.SetCommonInstanceMetadataCallback): void;

Calls SetCommonInstanceMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcommoninstancemetadataprojectrequest)`   
SetCommonInstanceMetadataProjectRequest message or plain object  
`callback` |  `[SetCommonInstanceMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setCommonInstanceMetadata(request)
    
    
    public setCommonInstanceMetadata(request: google.cloud.compute.v1beta.ISetCommonInstanceMetadataProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetCommonInstanceMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetcommoninstancemetadataprojectrequest)`   
SetCommonInstanceMetadataProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setDefaultNetworkTier(request, callback)
    
    
    public setDefaultNetworkTier(request: google.cloud.compute.v1beta.ISetDefaultNetworkTierProjectRequest, callback: google.cloud.compute.v1beta.Projects.SetDefaultNetworkTierCallback): void;

Calls SetDefaultNetworkTier.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetdefaultnetworktierprojectrequest)`   
SetDefaultNetworkTierProjectRequest message or plain object  
`callback` |  `[SetDefaultNetworkTierCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setDefaultNetworkTier(request)
    
    
    public setDefaultNetworkTier(request: google.cloud.compute.v1beta.ISetDefaultNetworkTierProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetDefaultNetworkTier.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetdefaultnetworktierprojectrequest)`   
SetDefaultNetworkTierProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setManagedProtectionTier(request, callback)
    
    
    public setManagedProtectionTier(request: google.cloud.compute.v1beta.ISetManagedProtectionTierProjectRequest, callback: google.cloud.compute.v1beta.Projects.SetManagedProtectionTierCallback): void;

Calls SetManagedProtectionTier.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetManagedProtectionTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetmanagedprotectiontierprojectrequest)`   
SetManagedProtectionTierProjectRequest message or plain object  
`callback` |  `[SetManagedProtectionTierCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setManagedProtectionTier(request)
    
    
    public setManagedProtectionTier(request: google.cloud.compute.v1beta.ISetManagedProtectionTierProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetManagedProtectionTier.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetManagedProtectionTierProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetmanagedprotectiontierprojectrequest)`   
SetManagedProtectionTierProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setUsageExportBucket(request, callback)
    
    
    public setUsageExportBucket(request: google.cloud.compute.v1beta.ISetUsageExportBucketProjectRequest, callback: google.cloud.compute.v1beta.Projects.SetUsageExportBucketCallback): void;

Calls SetUsageExportBucket.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetUsageExportBucketProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetusageexportbucketprojectrequest)`   
SetUsageExportBucketProjectRequest message or plain object  
`callback` |  `[SetUsageExportBucketCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setUsageExportBucket(request)
    
    
    public setUsageExportBucket(request: google.cloud.compute.v1beta.ISetUsageExportBucketProjectRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetUsageExportBucket.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetUsageExportBucketProjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetusageexportbucketprojectrequest)`   
SetUsageExportBucketProjectRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
