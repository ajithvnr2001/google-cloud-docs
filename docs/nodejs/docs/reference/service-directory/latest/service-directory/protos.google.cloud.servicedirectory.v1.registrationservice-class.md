---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.registrationservice-class
title: Class protos.google.cloud.servicedirectory.v1.RegistrationService (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:27.031295+00:00
---

# Class protos.google.cloud.servicedirectory.v1.RegistrationService (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.registrationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.servicedirectory.v1.RegistrationService (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.2.0  4.0.7  3.4.0  3.3.2  3.2.4  3.1.2 

Represents a RegistrationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.servicedirectory.v1.RegistrationService

## Package

[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RegistrationService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RegistrationService;

Creates new RegistrationService service using the specified rpc implementation.

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
`[RegistrationService](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.registrationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEndpoint(request, callback)
    
    
    public createEndpoint(request: google.cloud.servicedirectory.v1.ICreateEndpointRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.CreateEndpointCallback): void;

Calls CreateEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreateendpointrequest)`   
CreateEndpointRequest message or plain object  
`callback` |  `[CreateEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Endpoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEndpoint(request)
    
    
    public createEndpoint(request: google.cloud.servicedirectory.v1.ICreateEndpointRequest): Promise<google.cloud.servicedirectory.v1.Endpoint>;

Calls CreateEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreateendpointrequest)`   
CreateEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Endpoint](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.endpoint)>` | Promise  
  
### createNamespace(request, callback)
    
    
    public createNamespace(request: google.cloud.servicedirectory.v1.ICreateNamespaceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.CreateNamespaceCallback): void;

Calls CreateNamespace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreatenamespacerequest)`   
CreateNamespaceRequest message or plain object  
`callback` |  `[CreateNamespaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Namespace  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNamespace(request)
    
    
    public createNamespace(request: google.cloud.servicedirectory.v1.ICreateNamespaceRequest): Promise<google.cloud.servicedirectory.v1.Namespace>;

Calls CreateNamespace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreatenamespacerequest)`   
CreateNamespaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Namespace](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.namespace)>` | Promise  
  
### createService(request, callback)
    
    
    public createService(request: google.cloud.servicedirectory.v1.ICreateServiceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.CreateServiceCallback): void;

Calls CreateService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreateservicerequest)`   
CreateServiceRequest message or plain object  
`callback` |  `[CreateServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Service  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createService(request)
    
    
    public createService(request: google.cloud.servicedirectory.v1.ICreateServiceRequest): Promise<google.cloud.servicedirectory.v1.Service>;

Calls CreateService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.icreateservicerequest)`   
CreateServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Service](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.service)>` | Promise  
  
### deleteEndpoint(request, callback)
    
    
    public deleteEndpoint(request: google.cloud.servicedirectory.v1.IDeleteEndpointRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.DeleteEndpointCallback): void;

Calls DeleteEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideleteendpointrequest)`   
DeleteEndpointRequest message or plain object  
`callback` |  `[DeleteEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEndpoint(request)
    
    
    public deleteEndpoint(request: google.cloud.servicedirectory.v1.IDeleteEndpointRequest): Promise<google.protobuf.Empty>;

Calls DeleteEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideleteendpointrequest)`   
DeleteEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.protobuf.empty)>` | Promise  
  
### deleteNamespace(request, callback)
    
    
    public deleteNamespace(request: google.cloud.servicedirectory.v1.IDeleteNamespaceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.DeleteNamespaceCallback): void;

Calls DeleteNamespace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideletenamespacerequest)`   
DeleteNamespaceRequest message or plain object  
`callback` |  `[DeleteNamespaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNamespace(request)
    
    
    public deleteNamespace(request: google.cloud.servicedirectory.v1.IDeleteNamespaceRequest): Promise<google.protobuf.Empty>;

Calls DeleteNamespace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideletenamespacerequest)`   
DeleteNamespaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.protobuf.empty)>` | Promise  
  
### deleteService(request, callback)
    
    
    public deleteService(request: google.cloud.servicedirectory.v1.IDeleteServiceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.DeleteServiceCallback): void;

Calls DeleteService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideleteservicerequest)`   
DeleteServiceRequest message or plain object  
`callback` |  `[DeleteServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteService(request)
    
    
    public deleteService(request: google.cloud.servicedirectory.v1.IDeleteServiceRequest): Promise<google.protobuf.Empty>;

Calls DeleteService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ideleteservicerequest)`   
DeleteServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.protobuf.empty)>` | Promise  
  
### getEndpoint(request, callback)
    
    
    public getEndpoint(request: google.cloud.servicedirectory.v1.IGetEndpointRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.GetEndpointCallback): void;

Calls GetEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetendpointrequest)`   
GetEndpointRequest message or plain object  
`callback` |  `[GetEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Endpoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEndpoint(request)
    
    
    public getEndpoint(request: google.cloud.servicedirectory.v1.IGetEndpointRequest): Promise<google.cloud.servicedirectory.v1.Endpoint>;

Calls GetEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetendpointrequest)`   
GetEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Endpoint](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.endpoint)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.policy)>` | Promise  
  
### getNamespace(request, callback)
    
    
    public getNamespace(request: google.cloud.servicedirectory.v1.IGetNamespaceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.GetNamespaceCallback): void;

Calls GetNamespace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetnamespacerequest)`   
GetNamespaceRequest message or plain object  
`callback` |  `[GetNamespaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Namespace  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNamespace(request)
    
    
    public getNamespace(request: google.cloud.servicedirectory.v1.IGetNamespaceRequest): Promise<google.cloud.servicedirectory.v1.Namespace>;

Calls GetNamespace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetnamespacerequest)`   
GetNamespaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Namespace](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.namespace)>` | Promise  
  
### getService(request, callback)
    
    
    public getService(request: google.cloud.servicedirectory.v1.IGetServiceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.GetServiceCallback): void;

Calls GetService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetservicerequest)`   
GetServiceRequest message or plain object  
`callback` |  `[GetServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Service  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getService(request)
    
    
    public getService(request: google.cloud.servicedirectory.v1.IGetServiceRequest): Promise<google.cloud.servicedirectory.v1.Service>;

Calls GetService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.igetservicerequest)`   
GetServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Service](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.service)>` | Promise  
  
### listEndpoints(request, callback)
    
    
    public listEndpoints(request: google.cloud.servicedirectory.v1.IListEndpointsRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.ListEndpointsCallback): void;

Calls ListEndpoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEndpointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistendpointsrequest)`   
ListEndpointsRequest message or plain object  
`callback` |  `[ListEndpointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEndpointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEndpoints(request)
    
    
    public listEndpoints(request: google.cloud.servicedirectory.v1.IListEndpointsRequest): Promise<google.cloud.servicedirectory.v1.ListEndpointsResponse>;

Calls ListEndpoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEndpointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistendpointsrequest)`   
ListEndpointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.ListEndpointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.listendpointsresponse)>` | Promise  
  
### listNamespaces(request, callback)
    
    
    public listNamespaces(request: google.cloud.servicedirectory.v1.IListNamespacesRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.ListNamespacesCallback): void;

Calls ListNamespaces.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNamespacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistnamespacesrequest)`   
ListNamespacesRequest message or plain object  
`callback` |  `[ListNamespacesCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and ListNamespacesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNamespaces(request)
    
    
    public listNamespaces(request: google.cloud.servicedirectory.v1.IListNamespacesRequest): Promise<google.cloud.servicedirectory.v1.ListNamespacesResponse>;

Calls ListNamespaces.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNamespacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistnamespacesrequest)`   
ListNamespacesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.ListNamespacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.listnamespacesresponse)>` | Promise  
  
### listServices(request, callback)
    
    
    public listServices(request: google.cloud.servicedirectory.v1.IListServicesRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.ListServicesCallback): void;

Calls ListServices.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistservicesrequest)`   
ListServicesRequest message or plain object  
`callback` |  `[ListServicesCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServicesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServices(request)
    
    
    public listServices(request: google.cloud.servicedirectory.v1.IListServicesRequest): Promise<google.cloud.servicedirectory.v1.ListServicesResponse>;

Calls ListServices.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.ilistservicesrequest)`   
ListServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.ListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.listservicesresponse)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and TestIamPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest): Promise<google.iam.v1.TestIamPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updateEndpoint(request, callback)
    
    
    public updateEndpoint(request: google.cloud.servicedirectory.v1.IUpdateEndpointRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.UpdateEndpointCallback): void;

Calls UpdateEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdateendpointrequest)`   
UpdateEndpointRequest message or plain object  
`callback` |  `[UpdateEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Endpoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEndpoint(request)
    
    
    public updateEndpoint(request: google.cloud.servicedirectory.v1.IUpdateEndpointRequest): Promise<google.cloud.servicedirectory.v1.Endpoint>;

Calls UpdateEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdateendpointrequest)`   
UpdateEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Endpoint](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.endpoint)>` | Promise  
  
### updateNamespace(request, callback)
    
    
    public updateNamespace(request: google.cloud.servicedirectory.v1.IUpdateNamespaceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.UpdateNamespaceCallback): void;

Calls UpdateNamespace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdatenamespacerequest)`   
UpdateNamespaceRequest message or plain object  
`callback` |  `[UpdateNamespaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Namespace  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateNamespace(request)
    
    
    public updateNamespace(request: google.cloud.servicedirectory.v1.IUpdateNamespaceRequest): Promise<google.cloud.servicedirectory.v1.Namespace>;

Calls UpdateNamespace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNamespaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdatenamespacerequest)`   
UpdateNamespaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Namespace](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.namespace)>` | Promise  
  
### updateService(request, callback)
    
    
    public updateService(request: google.cloud.servicedirectory.v1.IUpdateServiceRequest, callback: google.cloud.servicedirectory.v1.RegistrationService.UpdateServiceCallback): void;

Calls UpdateService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdateservicerequest)`   
UpdateServiceRequest message or plain object  
`callback` |  `[UpdateServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)`   
Node-style callback called with the error, if any, and Service  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateService(request)
    
    
    public updateService(request: google.cloud.servicedirectory.v1.IUpdateServiceRequest): Promise<google.cloud.servicedirectory.v1.Service>;

Calls UpdateService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.iupdateservicerequest)`   
UpdateServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.servicedirectory.v1.Service](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/service-directory/protos.google.cloud.servicedirectory.v1.service)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
