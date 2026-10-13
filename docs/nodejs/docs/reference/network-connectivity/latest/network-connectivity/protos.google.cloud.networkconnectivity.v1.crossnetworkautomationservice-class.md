---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.crossnetworkautomationservice-class
title: Class protos.google.cloud.networkconnectivity.v1.CrossNetworkAutomationService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:26.770673+00:00
---

# Class protos.google.cloud.networkconnectivity.v1.CrossNetworkAutomationService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.crossnetworkautomationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1.CrossNetworkAutomationService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a CrossNetworkAutomationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.networkconnectivity.v1.CrossNetworkAutomationService

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CrossNetworkAutomationService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CrossNetworkAutomationService;

Creates new CrossNetworkAutomationService service using the specified rpc implementation.

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
`[CrossNetworkAutomationService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.crossnetworkautomationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createServiceConnectionMap(request, callback)
    
    
    public createServiceConnectionMap(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionMapRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionMapCallback): void;

Calls CreateServiceConnectionMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectionmaprequest)`   
CreateServiceConnectionMapRequest message or plain object  
`callback` |  `[CreateServiceConnectionMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServiceConnectionMap(request)
    
    
    public createServiceConnectionMap(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionMapRequest): Promise<google.longrunning.Operation>;

Calls CreateServiceConnectionMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectionmaprequest)`   
CreateServiceConnectionMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### createServiceConnectionPolicy(request, callback)
    
    
    public createServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionPolicyRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionPolicyCallback): void;

Calls CreateServiceConnectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectionpolicyrequest)`   
CreateServiceConnectionPolicyRequest message or plain object  
`callback` |  `[CreateServiceConnectionPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServiceConnectionPolicy(request)
    
    
    public createServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionPolicyRequest): Promise<google.longrunning.Operation>;

Calls CreateServiceConnectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectionpolicyrequest)`   
CreateServiceConnectionPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### createServiceConnectionToken(request, callback)
    
    
    public createServiceConnectionToken(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionTokenRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionTokenCallback): void;

Calls CreateServiceConnectionToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectiontokenrequest)`   
CreateServiceConnectionTokenRequest message or plain object  
`callback` |  `[CreateServiceConnectionTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServiceConnectionToken(request)
    
    
    public createServiceConnectionToken(request: google.cloud.networkconnectivity.v1.ICreateServiceConnectionTokenRequest): Promise<google.longrunning.Operation>;

Calls CreateServiceConnectionToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreateserviceconnectiontokenrequest)`   
CreateServiceConnectionTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteServiceClass(request, callback)
    
    
    public deleteServiceClass(request: google.cloud.networkconnectivity.v1.IDeleteServiceClassRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceClassCallback): void;

Calls DeleteServiceClass.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceclassrequest)`   
DeleteServiceClassRequest message or plain object  
`callback` |  `[DeleteServiceClassCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServiceClass(request)
    
    
    public deleteServiceClass(request: google.cloud.networkconnectivity.v1.IDeleteServiceClassRequest): Promise<google.longrunning.Operation>;

Calls DeleteServiceClass.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceclassrequest)`   
DeleteServiceClassRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteServiceConnectionMap(request, callback)
    
    
    public deleteServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionMapRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionMapCallback): void;

Calls DeleteServiceConnectionMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectionmaprequest)`   
DeleteServiceConnectionMapRequest message or plain object  
`callback` |  `[DeleteServiceConnectionMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServiceConnectionMap(request)
    
    
    public deleteServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionMapRequest): Promise<google.longrunning.Operation>;

Calls DeleteServiceConnectionMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectionmaprequest)`   
DeleteServiceConnectionMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteServiceConnectionPolicy(request, callback)
    
    
    public deleteServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionPolicyRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionPolicyCallback): void;

Calls DeleteServiceConnectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectionpolicyrequest)`   
DeleteServiceConnectionPolicyRequest message or plain object  
`callback` |  `[DeleteServiceConnectionPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServiceConnectionPolicy(request)
    
    
    public deleteServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionPolicyRequest): Promise<google.longrunning.Operation>;

Calls DeleteServiceConnectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectionpolicyrequest)`   
DeleteServiceConnectionPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteServiceConnectionToken(request, callback)
    
    
    public deleteServiceConnectionToken(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionTokenRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionTokenCallback): void;

Calls DeleteServiceConnectionToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectiontokenrequest)`   
DeleteServiceConnectionTokenRequest message or plain object  
`callback` |  `[DeleteServiceConnectionTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServiceConnectionToken(request)
    
    
    public deleteServiceConnectionToken(request: google.cloud.networkconnectivity.v1.IDeleteServiceConnectionTokenRequest): Promise<google.longrunning.Operation>;

Calls DeleteServiceConnectionToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideleteserviceconnectiontokenrequest)`   
DeleteServiceConnectionTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### getServiceClass(request, callback)
    
    
    public getServiceClass(request: google.cloud.networkconnectivity.v1.IGetServiceClassRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceClassCallback): void;

Calls GetServiceClass.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceclassrequest)`   
GetServiceClassRequest message or plain object  
`callback` |  `[GetServiceClassCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ServiceClass  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServiceClass(request)
    
    
    public getServiceClass(request: google.cloud.networkconnectivity.v1.IGetServiceClassRequest): Promise<google.cloud.networkconnectivity.v1.ServiceClass>;

Calls GetServiceClass.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceclassrequest)`   
GetServiceClassRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ServiceClass](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceclass)>` | Promise  
  
### getServiceConnectionMap(request, callback)
    
    
    public getServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionMapRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionMapCallback): void;

Calls GetServiceConnectionMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectionmaprequest)`   
GetServiceConnectionMapRequest message or plain object  
`callback` |  `[GetServiceConnectionMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ServiceConnectionMap  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServiceConnectionMap(request)
    
    
    public getServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionMapRequest): Promise<google.cloud.networkconnectivity.v1.ServiceConnectionMap>;

Calls GetServiceConnectionMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectionmaprequest)`   
GetServiceConnectionMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ServiceConnectionMap](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap-class)>` | Promise  
  
### getServiceConnectionPolicy(request, callback)
    
    
    public getServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionPolicyRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionPolicyCallback): void;

Calls GetServiceConnectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectionpolicyrequest)`   
GetServiceConnectionPolicyRequest message or plain object  
`callback` |  `[GetServiceConnectionPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ServiceConnectionPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServiceConnectionPolicy(request)
    
    
    public getServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionPolicyRequest): Promise<google.cloud.networkconnectivity.v1.ServiceConnectionPolicy>;

Calls GetServiceConnectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectionpolicyrequest)`   
GetServiceConnectionPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ServiceConnectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionpolicy-class)>` | Promise  
  
### getServiceConnectionToken(request, callback)
    
    
    public getServiceConnectionToken(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionTokenRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionTokenCallback): void;

Calls GetServiceConnectionToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectiontokenrequest)`   
GetServiceConnectionTokenRequest message or plain object  
`callback` |  `[GetServiceConnectionTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ServiceConnectionToken  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServiceConnectionToken(request)
    
    
    public getServiceConnectionToken(request: google.cloud.networkconnectivity.v1.IGetServiceConnectionTokenRequest): Promise<google.cloud.networkconnectivity.v1.ServiceConnectionToken>;

Calls GetServiceConnectionToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceConnectionTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetserviceconnectiontokenrequest)`   
GetServiceConnectionTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ServiceConnectionToken](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectiontoken)>` | Promise  
  
### listServiceClasses(request, callback)
    
    
    public listServiceClasses(request: google.cloud.networkconnectivity.v1.IListServiceClassesRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceClassesCallback): void;

Calls ListServiceClasses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServiceClassesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceclassesrequest)`   
ListServiceClassesRequest message or plain object  
`callback` |  `[ListServiceClassesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServiceClassesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServiceClasses(request)
    
    
    public listServiceClasses(request: google.cloud.networkconnectivity.v1.IListServiceClassesRequest): Promise<google.cloud.networkconnectivity.v1.ListServiceClassesResponse>;

Calls ListServiceClasses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServiceClassesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceclassesrequest)`   
ListServiceClassesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListServiceClassesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listserviceclassesresponse)>` | Promise  
  
### listServiceConnectionMaps(request, callback)
    
    
    public listServiceConnectionMaps(request: google.cloud.networkconnectivity.v1.IListServiceConnectionMapsRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionMapsCallback): void;

Calls ListServiceConnectionMaps.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionMapsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectionmapsrequest)`   
ListServiceConnectionMapsRequest message or plain object  
`callback` |  `[ListServiceConnectionMapsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServiceConnectionMapsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServiceConnectionMaps(request)
    
    
    public listServiceConnectionMaps(request: google.cloud.networkconnectivity.v1.IListServiceConnectionMapsRequest): Promise<google.cloud.networkconnectivity.v1.ListServiceConnectionMapsResponse>;

Calls ListServiceConnectionMaps.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionMapsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectionmapsrequest)`   
ListServiceConnectionMapsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListServiceConnectionMapsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listserviceconnectionmapsresponse)>` | Promise  
  
### listServiceConnectionPolicies(request, callback)
    
    
    public listServiceConnectionPolicies(request: google.cloud.networkconnectivity.v1.IListServiceConnectionPoliciesRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionPoliciesCallback): void;

Calls ListServiceConnectionPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectionpoliciesrequest)`   
ListServiceConnectionPoliciesRequest message or plain object  
`callback` |  `[ListServiceConnectionPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServiceConnectionPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServiceConnectionPolicies(request)
    
    
    public listServiceConnectionPolicies(request: google.cloud.networkconnectivity.v1.IListServiceConnectionPoliciesRequest): Promise<google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesResponse>;

Calls ListServiceConnectionPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectionpoliciesrequest)`   
ListServiceConnectionPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listserviceconnectionpoliciesresponse)>` | Promise  
  
### listServiceConnectionTokens(request, callback)
    
    
    public listServiceConnectionTokens(request: google.cloud.networkconnectivity.v1.IListServiceConnectionTokensRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionTokensCallback): void;

Calls ListServiceConnectionTokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectiontokensrequest)`   
ListServiceConnectionTokensRequest message or plain object  
`callback` |  `[ListServiceConnectionTokensCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServiceConnectionTokensResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServiceConnectionTokens(request)
    
    
    public listServiceConnectionTokens(request: google.cloud.networkconnectivity.v1.IListServiceConnectionTokensRequest): Promise<google.cloud.networkconnectivity.v1.ListServiceConnectionTokensResponse>;

Calls ListServiceConnectionTokens.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServiceConnectionTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistserviceconnectiontokensrequest)`   
ListServiceConnectionTokensRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListServiceConnectionTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listserviceconnectiontokensresponse)>` | Promise  
  
### updateServiceClass(request, callback)
    
    
    public updateServiceClass(request: google.cloud.networkconnectivity.v1.IUpdateServiceClassRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceClassCallback): void;

Calls UpdateServiceClass.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceclassrequest)`   
UpdateServiceClassRequest message or plain object  
`callback` |  `[UpdateServiceClassCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServiceClass(request)
    
    
    public updateServiceClass(request: google.cloud.networkconnectivity.v1.IUpdateServiceClassRequest): Promise<google.longrunning.Operation>;

Calls UpdateServiceClass.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceclassrequest)`   
UpdateServiceClassRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### updateServiceConnectionMap(request, callback)
    
    
    public updateServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IUpdateServiceConnectionMapRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionMapCallback): void;

Calls UpdateServiceConnectionMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceconnectionmaprequest)`   
UpdateServiceConnectionMapRequest message or plain object  
`callback` |  `[UpdateServiceConnectionMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServiceConnectionMap(request)
    
    
    public updateServiceConnectionMap(request: google.cloud.networkconnectivity.v1.IUpdateServiceConnectionMapRequest): Promise<google.longrunning.Operation>;

Calls UpdateServiceConnectionMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceConnectionMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceconnectionmaprequest)`   
UpdateServiceConnectionMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### updateServiceConnectionPolicy(request, callback)
    
    
    public updateServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IUpdateServiceConnectionPolicyRequest, callback: google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionPolicyCallback): void;

Calls UpdateServiceConnectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceconnectionpolicyrequest)`   
UpdateServiceConnectionPolicyRequest message or plain object  
`callback` |  `[UpdateServiceConnectionPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServiceConnectionPolicy(request)
    
    
    public updateServiceConnectionPolicy(request: google.cloud.networkconnectivity.v1.IUpdateServiceConnectionPolicyRequest): Promise<google.longrunning.Operation>;

Calls UpdateServiceConnectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceConnectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdateserviceconnectionpolicyrequest)`   
UpdateServiceConnectionPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
