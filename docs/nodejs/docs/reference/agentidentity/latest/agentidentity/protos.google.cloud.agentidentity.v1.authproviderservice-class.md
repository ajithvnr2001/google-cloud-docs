---
url: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authproviderservice-class
title: Class protos.google.cloud.agentidentity.v1.AuthProviderService (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:28.456780+00:00
---

# Class protos.google.cloud.agentidentity.v1.AuthProviderService (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authproviderservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.agentidentity.v1.AuthProviderService (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an AuthProviderService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.agentidentity.v1.AuthProviderService

## Package

[@google-cloud/agentidentity](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AuthProviderService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AuthProviderService;

Creates new AuthProviderService service using the specified rpc implementation.

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
`[AuthProviderService](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authproviderservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAuthProvider(request, callback)
    
    
    public createAuthProvider(request: google.cloud.agentidentity.v1.ICreateAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.CreateAuthProviderCallback): void;

Calls CreateAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.icreateauthproviderrequest)`   
CreateAuthProviderRequest message or plain object  
`callback` |  `[CreateAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAuthProvider(request)
    
    
    public createAuthProvider(request: google.cloud.agentidentity.v1.ICreateAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls CreateAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.icreateauthproviderrequest)`   
CreateAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
### deleteAuthorization(request, callback)
    
    
    public deleteAuthorization(request: google.cloud.agentidentity.v1.IDeleteAuthorizationRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.DeleteAuthorizationCallback): void;

Calls DeleteAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ideleteauthorizationrequest)`   
DeleteAuthorizationRequest message or plain object  
`callback` |  `[DeleteAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthorization(request)
    
    
    public deleteAuthorization(request: google.cloud.agentidentity.v1.IDeleteAuthorizationRequest): Promise<google.protobuf.Empty>;

Calls DeleteAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ideleteauthorizationrequest)`   
DeleteAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.protobuf.empty)>` | Promise  
  
### deleteAuthProvider(request, callback)
    
    
    public deleteAuthProvider(request: google.cloud.agentidentity.v1.IDeleteAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.DeleteAuthProviderCallback): void;

Calls DeleteAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ideleteauthproviderrequest)`   
DeleteAuthProviderRequest message or plain object  
`callback` |  `[DeleteAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthProvider(request)
    
    
    public deleteAuthProvider(request: google.cloud.agentidentity.v1.IDeleteAuthProviderRequest): Promise<google.protobuf.Empty>;

Calls DeleteAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ideleteauthproviderrequest)`   
DeleteAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.protobuf.empty)>` | Promise  
  
### disableAuthProvider(request, callback)
    
    
    public disableAuthProvider(request: google.cloud.agentidentity.v1.IDisableAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.DisableAuthProviderCallback): void;

Calls DisableAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.idisableauthproviderrequest)`   
DisableAuthProviderRequest message or plain object  
`callback` |  `[DisableAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableAuthProvider(request)
    
    
    public disableAuthProvider(request: google.cloud.agentidentity.v1.IDisableAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls DisableAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.idisableauthproviderrequest)`   
DisableAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
### enableAuthProvider(request, callback)
    
    
    public enableAuthProvider(request: google.cloud.agentidentity.v1.IEnableAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.EnableAuthProviderCallback): void;

Calls EnableAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ienableauthproviderrequest)`   
EnableAuthProviderRequest message or plain object  
`callback` |  `[EnableAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableAuthProvider(request)
    
    
    public enableAuthProvider(request: google.cloud.agentidentity.v1.IEnableAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls EnableAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ienableauthproviderrequest)`   
EnableAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
### getAccessSummary(request, callback)
    
    
    public getAccessSummary(request: google.cloud.agentidentity.v1.IGetAccessSummaryRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.GetAccessSummaryCallback): void;

Calls GetAccessSummary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetaccesssummaryrequest)`   
GetAccessSummaryRequest message or plain object  
`callback` |  `[GetAccessSummaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessSummary  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessSummary(request)
    
    
    public getAccessSummary(request: google.cloud.agentidentity.v1.IGetAccessSummaryRequest): Promise<google.cloud.agentidentity.v1.AccessSummary>;

Calls GetAccessSummary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetaccesssummaryrequest)`   
GetAccessSummaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)>` | Promise  
  
### getAuthorization(request, callback)
    
    
    public getAuthorization(request: google.cloud.agentidentity.v1.IGetAuthorizationRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.GetAuthorizationCallback): void;

Calls GetAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetauthorizationrequest)`   
GetAuthorizationRequest message or plain object  
`callback` |  `[GetAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and Authorization  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuthorization(request)
    
    
    public getAuthorization(request: google.cloud.agentidentity.v1.IGetAuthorizationRequest): Promise<google.cloud.agentidentity.v1.Authorization>;

Calls GetAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetauthorizationrequest)`   
GetAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authorization-class)>` | Promise  
  
### getAuthProvider(request, callback)
    
    
    public getAuthProvider(request: google.cloud.agentidentity.v1.IGetAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.GetAuthProviderCallback): void;

Calls GetAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetauthproviderrequest)`   
GetAuthProviderRequest message or plain object  
`callback` |  `[GetAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuthProvider(request)
    
    
    public getAuthProvider(request: google.cloud.agentidentity.v1.IGetAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls GetAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.igetauthproviderrequest)`   
GetAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
### listAccessSummaries(request, callback)
    
    
    public listAccessSummaries(request: google.cloud.agentidentity.v1.IListAccessSummariesRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.ListAccessSummariesCallback): void;

Calls ListAccessSummaries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistaccesssummariesrequest)`   
ListAccessSummariesRequest message or plain object  
`callback` |  `[ListAccessSummariesCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccessSummariesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessSummaries(request)
    
    
    public listAccessSummaries(request: google.cloud.agentidentity.v1.IListAccessSummariesRequest): Promise<google.cloud.agentidentity.v1.ListAccessSummariesResponse>;

Calls ListAccessSummaries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccessSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistaccesssummariesrequest)`   
ListAccessSummariesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.ListAccessSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.listaccesssummariesresponse)>` | Promise  
  
### listAuthorizations(request, callback)
    
    
    public listAuthorizations(request: google.cloud.agentidentity.v1.IListAuthorizationsRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.ListAuthorizationsCallback): void;

Calls ListAuthorizations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistauthorizationsrequest)`   
ListAuthorizationsRequest message or plain object  
`callback` |  `[ListAuthorizationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuthorizationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthorizations(request)
    
    
    public listAuthorizations(request: google.cloud.agentidentity.v1.IListAuthorizationsRequest): Promise<google.cloud.agentidentity.v1.ListAuthorizationsResponse>;

Calls ListAuthorizations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistauthorizationsrequest)`   
ListAuthorizationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.ListAuthorizationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.listauthorizationsresponse)>` | Promise  
  
### listAuthProviders(request, callback)
    
    
    public listAuthProviders(request: google.cloud.agentidentity.v1.IListAuthProvidersRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.ListAuthProvidersCallback): void;

Calls ListAuthProviders.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistauthprovidersrequest)`   
ListAuthProvidersRequest message or plain object  
`callback` |  `[ListAuthProvidersCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuthProvidersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthProviders(request)
    
    
    public listAuthProviders(request: google.cloud.agentidentity.v1.IListAuthProvidersRequest): Promise<google.cloud.agentidentity.v1.ListAuthProvidersResponse>;

Calls ListAuthProviders.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuthProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.ilistauthprovidersrequest)`   
ListAuthProvidersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.ListAuthProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.listauthprovidersresponse)>` | Promise  
  
### queryAuthProviders(request, callback)
    
    
    public queryAuthProviders(request: google.cloud.agentidentity.v1.IQueryAuthProvidersRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.QueryAuthProvidersCallback): void;

Calls QueryAuthProviders.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryAuthProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iqueryauthprovidersrequest)`   
QueryAuthProvidersRequest message or plain object  
`callback` |  `[QueryAuthProvidersCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryAuthProvidersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryAuthProviders(request)
    
    
    public queryAuthProviders(request: google.cloud.agentidentity.v1.IQueryAuthProvidersRequest): Promise<google.cloud.agentidentity.v1.QueryAuthProvidersResponse>;

Calls QueryAuthProviders.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryAuthProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iqueryauthprovidersrequest)`   
QueryAuthProvidersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.QueryAuthProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.queryauthprovidersresponse)>` | Promise  
  
### queryWorkloads(request, callback)
    
    
    public queryWorkloads(request: google.cloud.agentidentity.v1.IQueryWorkloadsRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.QueryWorkloadsCallback): void;

Calls QueryWorkloads.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iqueryworkloadsrequest)`   
QueryWorkloadsRequest message or plain object  
`callback` |  `[QueryWorkloadsCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryWorkloadsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryWorkloads(request)
    
    
    public queryWorkloads(request: google.cloud.agentidentity.v1.IQueryWorkloadsRequest): Promise<google.cloud.agentidentity.v1.QueryWorkloadsResponse>;

Calls QueryWorkloads.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iqueryworkloadsrequest)`   
QueryWorkloadsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.QueryWorkloadsResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.queryworkloadsresponse)>` | Promise  
  
### revokeAuthorization(request, callback)
    
    
    public revokeAuthorization(request: google.cloud.agentidentity.v1.IRevokeAuthorizationRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.RevokeAuthorizationCallback): void;

Calls RevokeAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRevokeAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.irevokeauthorizationrequest)`   
RevokeAuthorizationRequest message or plain object  
`callback` |  `[RevokeAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and RevokeAuthorizationResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### revokeAuthorization(request)
    
    
    public revokeAuthorization(request: google.cloud.agentidentity.v1.IRevokeAuthorizationRequest): Promise<google.cloud.agentidentity.v1.RevokeAuthorizationResponse>;

Calls RevokeAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRevokeAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.irevokeauthorizationrequest)`   
RevokeAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.RevokeAuthorizationResponse](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.revokeauthorizationresponse)>` | Promise  
  
### undeleteAuthProvider(request, callback)
    
    
    public undeleteAuthProvider(request: google.cloud.agentidentity.v1.IUndeleteAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.UndeleteAuthProviderCallback): void;

Calls UndeleteAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iundeleteauthproviderrequest)`   
UndeleteAuthProviderRequest message or plain object  
`callback` |  `[UndeleteAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteAuthProvider(request)
    
    
    public undeleteAuthProvider(request: google.cloud.agentidentity.v1.IUndeleteAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls UndeleteAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iundeleteauthproviderrequest)`   
UndeleteAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
### updateAuthProvider(request, callback)
    
    
    public updateAuthProvider(request: google.cloud.agentidentity.v1.IUpdateAuthProviderRequest, callback: google.cloud.agentidentity.v1.AuthProviderService.UpdateAuthProviderCallback): void;

Calls UpdateAuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iupdateauthproviderrequest)`   
UpdateAuthProviderRequest message or plain object  
`callback` |  `[UpdateAuthProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthProvider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAuthProvider(request)
    
    
    public updateAuthProvider(request: google.cloud.agentidentity.v1.IUpdateAuthProviderRequest): Promise<google.cloud.agentidentity.v1.AuthProvider>;

Calls UpdateAuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iupdateauthproviderrequest)`   
UpdateAuthProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.agentidentity.v1.AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.authprovider-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-12 UTC."],[],[]] 
