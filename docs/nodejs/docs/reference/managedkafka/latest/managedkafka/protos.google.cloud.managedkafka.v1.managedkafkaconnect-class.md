---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafkaconnect-class
title: Class protos.google.cloud.managedkafka.v1.ManagedKafkaConnect (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:39.255578+00:00
---

# Class protos.google.cloud.managedkafka.v1.ManagedKafkaConnect (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafkaconnect-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.managedkafka.v1.ManagedKafkaConnect (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.6.0  0.3.0  0.2.0  0.1.0 

Represents a ManagedKafkaConnect

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.managedkafka.v1.ManagedKafkaConnect

## Package

[@google-cloud/managedkafka](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ManagedKafkaConnect service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ManagedKafkaConnect;

Creates new ManagedKafkaConnect service using the specified rpc implementation.

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
`[ManagedKafkaConnect](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafkaconnect-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConnectCluster(request, callback)
    
    
    public createConnectCluster(request: google.cloud.managedkafka.v1.ICreateConnectClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnectClusterCallback): void;

Calls CreateConnectCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateconnectclusterrequest)`   
CreateConnectClusterRequest message or plain object  
`callback` |  `[CreateConnectClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnectCluster(request)
    
    
    public createConnectCluster(request: google.cloud.managedkafka.v1.ICreateConnectClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateConnectCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateconnectclusterrequest)`   
CreateConnectClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### createConnector(request, callback)
    
    
    public createConnector(request: google.cloud.managedkafka.v1.ICreateConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnectorCallback): void;

Calls CreateConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateconnectorrequest)`   
CreateConnectorRequest message or plain object  
`callback` |  `[CreateConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Connector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnector(request)
    
    
    public createConnector(request: google.cloud.managedkafka.v1.ICreateConnectorRequest): Promise<google.cloud.managedkafka.v1.Connector>;

Calls CreateConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateconnectorrequest)`   
CreateConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Connector](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.connector-class)>` | Promise  
  
### deleteConnectCluster(request, callback)
    
    
    public deleteConnectCluster(request: google.cloud.managedkafka.v1.IDeleteConnectClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnectClusterCallback): void;

Calls DeleteConnectCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconnectclusterrequest)`   
DeleteConnectClusterRequest message or plain object  
`callback` |  `[DeleteConnectClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnectCluster(request)
    
    
    public deleteConnectCluster(request: google.cloud.managedkafka.v1.IDeleteConnectClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteConnectCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconnectclusterrequest)`   
DeleteConnectClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### deleteConnector(request, callback)
    
    
    public deleteConnector(request: google.cloud.managedkafka.v1.IDeleteConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnectorCallback): void;

Calls DeleteConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconnectorrequest)`   
DeleteConnectorRequest message or plain object  
`callback` |  `[DeleteConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnector(request)
    
    
    public deleteConnector(request: google.cloud.managedkafka.v1.IDeleteConnectorRequest): Promise<google.protobuf.Empty>;

Calls DeleteConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconnectorrequest)`   
DeleteConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.protobuf.empty)>` | Promise  
  
### getConnectCluster(request, callback)
    
    
    public getConnectCluster(request: google.cloud.managedkafka.v1.IGetConnectClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnectClusterCallback): void;

Calls GetConnectCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconnectclusterrequest)`   
GetConnectClusterRequest message or plain object  
`callback` |  `[GetConnectClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ConnectCluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectCluster(request)
    
    
    public getConnectCluster(request: google.cloud.managedkafka.v1.IGetConnectClusterRequest): Promise<google.cloud.managedkafka.v1.ConnectCluster>;

Calls GetConnectCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconnectclusterrequest)`   
GetConnectClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ConnectCluster](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.connectcluster-class)>` | Promise  
  
### getConnector(request, callback)
    
    
    public getConnector(request: google.cloud.managedkafka.v1.IGetConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnectorCallback): void;

Calls GetConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconnectorrequest)`   
GetConnectorRequest message or plain object  
`callback` |  `[GetConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Connector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnector(request)
    
    
    public getConnector(request: google.cloud.managedkafka.v1.IGetConnectorRequest): Promise<google.cloud.managedkafka.v1.Connector>;

Calls GetConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconnectorrequest)`   
GetConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Connector](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.connector-class)>` | Promise  
  
### listConnectClusters(request, callback)
    
    
    public listConnectClusters(request: google.cloud.managedkafka.v1.IListConnectClustersRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectClustersCallback): void;

Calls ListConnectClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconnectclustersrequest)`   
ListConnectClustersRequest message or plain object  
`callback` |  `[ListConnectClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectClusters(request)
    
    
    public listConnectClusters(request: google.cloud.managedkafka.v1.IListConnectClustersRequest): Promise<google.cloud.managedkafka.v1.ListConnectClustersResponse>;

Calls ListConnectClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconnectclustersrequest)`   
ListConnectClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListConnectClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listconnectclustersresponse)>` | Promise  
  
### listConnectors(request, callback)
    
    
    public listConnectors(request: google.cloud.managedkafka.v1.IListConnectorsRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectorsCallback): void;

Calls ListConnectors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconnectorsrequest)`   
ListConnectorsRequest message or plain object  
`callback` |  `[ListConnectorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectors(request)
    
    
    public listConnectors(request: google.cloud.managedkafka.v1.IListConnectorsRequest): Promise<google.cloud.managedkafka.v1.ListConnectorsResponse>;

Calls ListConnectors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconnectorsrequest)`   
ListConnectorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListConnectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listconnectorsresponse)>` | Promise  
  
### pauseConnector(request, callback)
    
    
    public pauseConnector(request: google.cloud.managedkafka.v1.IPauseConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.PauseConnectorCallback): void;

Calls PauseConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ipauseconnectorrequest)`   
PauseConnectorRequest message or plain object  
`callback` |  `[PauseConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and PauseConnectorResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseConnector(request)
    
    
    public pauseConnector(request: google.cloud.managedkafka.v1.IPauseConnectorRequest): Promise<google.cloud.managedkafka.v1.PauseConnectorResponse>;

Calls PauseConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPauseConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ipauseconnectorrequest)`   
PauseConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.PauseConnectorResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.pauseconnectorresponse)>` | Promise  
  
### restartConnector(request, callback)
    
    
    public restartConnector(request: google.cloud.managedkafka.v1.IRestartConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.RestartConnectorCallback): void;

Calls RestartConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestartConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.irestartconnectorrequest)`   
RestartConnectorRequest message or plain object  
`callback` |  `[RestartConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and RestartConnectorResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restartConnector(request)
    
    
    public restartConnector(request: google.cloud.managedkafka.v1.IRestartConnectorRequest): Promise<google.cloud.managedkafka.v1.RestartConnectorResponse>;

Calls RestartConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestartConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.irestartconnectorrequest)`   
RestartConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.RestartConnectorResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.restartconnectorresponse)>` | Promise  
  
### resumeConnector(request, callback)
    
    
    public resumeConnector(request: google.cloud.managedkafka.v1.IResumeConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.ResumeConnectorCallback): void;

Calls ResumeConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iresumeconnectorrequest)`   
ResumeConnectorRequest message or plain object  
`callback` |  `[ResumeConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ResumeConnectorResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeConnector(request)
    
    
    public resumeConnector(request: google.cloud.managedkafka.v1.IResumeConnectorRequest): Promise<google.cloud.managedkafka.v1.ResumeConnectorResponse>;

Calls ResumeConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iresumeconnectorrequest)`   
ResumeConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ResumeConnectorResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.resumeconnectorresponse)>` | Promise  
  
### stopConnector(request, callback)
    
    
    public stopConnector(request: google.cloud.managedkafka.v1.IStopConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.StopConnectorCallback): void;

Calls StopConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.istopconnectorrequest)`   
StopConnectorRequest message or plain object  
`callback` |  `[StopConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and StopConnectorResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopConnector(request)
    
    
    public stopConnector(request: google.cloud.managedkafka.v1.IStopConnectorRequest): Promise<google.cloud.managedkafka.v1.StopConnectorResponse>;

Calls StopConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.istopconnectorrequest)`   
StopConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.StopConnectorResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.stopconnectorresponse)>` | Promise  
  
### updateConnectCluster(request, callback)
    
    
    public updateConnectCluster(request: google.cloud.managedkafka.v1.IUpdateConnectClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnectClusterCallback): void;

Calls UpdateConnectCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconnectclusterrequest)`   
UpdateConnectClusterRequest message or plain object  
`callback` |  `[UpdateConnectClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnectCluster(request)
    
    
    public updateConnectCluster(request: google.cloud.managedkafka.v1.IUpdateConnectClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateConnectCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconnectclusterrequest)`   
UpdateConnectClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### updateConnector(request, callback)
    
    
    public updateConnector(request: google.cloud.managedkafka.v1.IUpdateConnectorRequest, callback: google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnectorCallback): void;

Calls UpdateConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconnectorrequest)`   
UpdateConnectorRequest message or plain object  
`callback` |  `[UpdateConnectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Connector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnector(request)
    
    
    public updateConnector(request: google.cloud.managedkafka.v1.IUpdateConnectorRequest): Promise<google.cloud.managedkafka.v1.Connector>;

Calls UpdateConnector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconnectorrequest)`   
UpdateConnectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Connector](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.connector-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
