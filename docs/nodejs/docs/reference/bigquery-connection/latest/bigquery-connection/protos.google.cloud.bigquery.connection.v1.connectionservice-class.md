---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connectionservice-class
title: Class protos.google.cloud.bigquery.connection.v1.ConnectionService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:06.654119+00:00
---

# Class protos.google.cloud.bigquery.connection.v1.ConnectionService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connectionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.connection.v1.ConnectionService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.1  2.1.1  2.0.2  1.5.1  1.4.2  1.3.5 

Represents a ConnectionService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.bigquery.connection.v1.ConnectionService

## Package

[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConnectionService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConnectionService;

Creates new ConnectionService service using the specified rpc implementation.

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
`[ConnectionService](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connectionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConnection(request, callback)
    
    
    public createConnection(request: google.cloud.bigquery.connection.v1.ICreateConnectionRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.CreateConnectionCallback): void;

Calls CreateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.icreateconnectionrequest)`   
CreateConnectionRequest message or plain object  
`callback` |  `[CreateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
Node-style callback called with the error, if any, and Connection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnection(request)
    
    
    public createConnection(request: google.cloud.bigquery.connection.v1.ICreateConnectionRequest): Promise<google.cloud.bigquery.connection.v1.Connection>;

Calls CreateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.icreateconnectionrequest)`   
CreateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.connection.v1.Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)>` | Promise  
  
### deleteConnection(request, callback)
    
    
    public deleteConnection(request: google.cloud.bigquery.connection.v1.IDeleteConnectionRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.DeleteConnectionCallback): void;

Calls DeleteConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.ideleteconnectionrequest)`   
DeleteConnectionRequest message or plain object  
`callback` |  `[DeleteConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnection(request)
    
    
    public deleteConnection(request: google.cloud.bigquery.connection.v1.IDeleteConnectionRequest): Promise<google.protobuf.Empty>;

Calls DeleteConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.ideleteconnectionrequest)`   
DeleteConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.empty)>` | Promise  
  
### getConnection(request, callback)
    
    
    public getConnection(request: google.cloud.bigquery.connection.v1.IGetConnectionRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.GetConnectionCallback): void;

Calls GetConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.igetconnectionrequest)`   
GetConnectionRequest message or plain object  
`callback` |  `[GetConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
Node-style callback called with the error, if any, and Connection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnection(request)
    
    
    public getConnection(request: google.cloud.bigquery.connection.v1.IGetConnectionRequest): Promise<google.cloud.bigquery.connection.v1.Connection>;

Calls GetConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.igetconnectionrequest)`   
GetConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.connection.v1.Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
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
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.policy)>` | Promise  
  
### listConnections(request, callback)
    
    
    public listConnections(request: google.cloud.bigquery.connection.v1.IListConnectionsRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.ListConnectionsCallback): void;

Calls ListConnections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.ilistconnectionsrequest)`   
ListConnectionsRequest message or plain object  
`callback` |  `[ListConnectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnections(request)
    
    
    public listConnections(request: google.cloud.bigquery.connection.v1.IListConnectionsRequest): Promise<google.cloud.bigquery.connection.v1.ListConnectionsResponse>;

Calls ListConnections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.ilistconnectionsrequest)`   
ListConnectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.connection.v1.ListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.listconnectionsresponse)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
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
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
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
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updateConnection(request, callback)
    
    
    public updateConnection(request: google.cloud.bigquery.connection.v1.IUpdateConnectionRequest, callback: google.cloud.bigquery.connection.v1.ConnectionService.UpdateConnectionCallback): void;

Calls UpdateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iupdateconnectionrequest)`   
UpdateConnectionRequest message or plain object  
`callback` |  `[UpdateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)`   
Node-style callback called with the error, if any, and Connection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnection(request)
    
    
    public updateConnection(request: google.cloud.bigquery.connection.v1.IUpdateConnectionRequest): Promise<google.cloud.bigquery.connection.v1.Connection>;

Calls UpdateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iupdateconnectionrequest)`   
UpdateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.connection.v1.Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
