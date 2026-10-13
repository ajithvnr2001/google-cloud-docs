---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafka-class
title: Class protos.google.cloud.managedkafka.v1.ManagedKafka (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:39.994449+00:00
---

# Class protos.google.cloud.managedkafka.v1.ManagedKafka (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafka-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.managedkafka.v1.ManagedKafka (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.6.0  0.3.0  0.2.0  0.1.0 

Represents a ManagedKafka

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.managedkafka.v1.ManagedKafka

## Package

[@google-cloud/managedkafka](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ManagedKafka service.

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

### addAclEntry(request, callback)
    
    
    public addAclEntry(request: google.cloud.managedkafka.v1.IAddAclEntryRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.AddAclEntryCallback): void;

Calls AddAclEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAclEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iaddaclentryrequest)`   
AddAclEntryRequest message or plain object  
`callback` |  `[AddAclEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and AddAclEntryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addAclEntry(request)
    
    
    public addAclEntry(request: google.cloud.managedkafka.v1.IAddAclEntryRequest): Promise<google.cloud.managedkafka.v1.AddAclEntryResponse>;

Calls AddAclEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddAclEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iaddaclentryrequest)`   
AddAclEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.AddAclEntryResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.addaclentryresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ManagedKafka;

Creates new ManagedKafka service using the specified rpc implementation.

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
`[ManagedKafka](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.managedkafka-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAcl(request, callback)
    
    
    public createAcl(request: google.cloud.managedkafka.v1.ICreateAclRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.CreateAclCallback): void;

Calls CreateAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateaclrequest)`   
CreateAclRequest message or plain object  
`callback` |  `[CreateAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Acl  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAcl(request)
    
    
    public createAcl(request: google.cloud.managedkafka.v1.ICreateAclRequest): Promise<google.cloud.managedkafka.v1.Acl>;

Calls CreateAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateaclrequest)`   
CreateAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Acl](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.acl)>` | Promise  
  
### createCluster(request, callback)
    
    
    public createCluster(request: google.cloud.managedkafka.v1.ICreateClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.CreateClusterCallback): void;

Calls CreateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
`callback` |  `[CreateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request)
    
    
    public createCluster(request: google.cloud.managedkafka.v1.ICreateClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### createTopic(request, callback)
    
    
    public createTopic(request: google.cloud.managedkafka.v1.ICreateTopicRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.CreateTopicCallback): void;

Calls CreateTopic.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreatetopicrequest)`   
CreateTopicRequest message or plain object  
`callback` |  `[CreateTopicCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Topic  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTopic(request)
    
    
    public createTopic(request: google.cloud.managedkafka.v1.ICreateTopicRequest): Promise<google.cloud.managedkafka.v1.Topic>;

Calls CreateTopic.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.icreatetopicrequest)`   
CreateTopicRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Topic](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.topic)>` | Promise  
  
### deleteAcl(request, callback)
    
    
    public deleteAcl(request: google.cloud.managedkafka.v1.IDeleteAclRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.DeleteAclCallback): void;

Calls DeleteAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteaclrequest)`   
DeleteAclRequest message or plain object  
`callback` |  `[DeleteAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAcl(request)
    
    
    public deleteAcl(request: google.cloud.managedkafka.v1.IDeleteAclRequest): Promise<google.protobuf.Empty>;

Calls DeleteAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteaclrequest)`   
DeleteAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.protobuf.empty)>` | Promise  
  
### deleteCluster(request, callback)
    
    
    public deleteCluster(request: google.cloud.managedkafka.v1.IDeleteClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.DeleteClusterCallback): void;

Calls DeleteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
`callback` |  `[DeleteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request)
    
    
    public deleteCluster(request: google.cloud.managedkafka.v1.IDeleteClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### deleteConsumerGroup(request, callback)
    
    
    public deleteConsumerGroup(request: google.cloud.managedkafka.v1.IDeleteConsumerGroupRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.DeleteConsumerGroupCallback): void;

Calls DeleteConsumerGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconsumergrouprequest)`   
DeleteConsumerGroupRequest message or plain object  
`callback` |  `[DeleteConsumerGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConsumerGroup(request)
    
    
    public deleteConsumerGroup(request: google.cloud.managedkafka.v1.IDeleteConsumerGroupRequest): Promise<google.protobuf.Empty>;

Calls DeleteConsumerGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideleteconsumergrouprequest)`   
DeleteConsumerGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.protobuf.empty)>` | Promise  
  
### deleteTopic(request, callback)
    
    
    public deleteTopic(request: google.cloud.managedkafka.v1.IDeleteTopicRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.DeleteTopicCallback): void;

Calls DeleteTopic.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideletetopicrequest)`   
DeleteTopicRequest message or plain object  
`callback` |  `[DeleteTopicCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTopic(request)
    
    
    public deleteTopic(request: google.cloud.managedkafka.v1.IDeleteTopicRequest): Promise<google.protobuf.Empty>;

Calls DeleteTopic.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ideletetopicrequest)`   
DeleteTopicRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.protobuf.empty)>` | Promise  
  
### getAcl(request, callback)
    
    
    public getAcl(request: google.cloud.managedkafka.v1.IGetAclRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.GetAclCallback): void;

Calls GetAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetaclrequest)`   
GetAclRequest message or plain object  
`callback` |  `[GetAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Acl  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAcl(request)
    
    
    public getAcl(request: google.cloud.managedkafka.v1.IGetAclRequest): Promise<google.cloud.managedkafka.v1.Acl>;

Calls GetAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetaclrequest)`   
GetAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Acl](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.acl)>` | Promise  
  
### getCluster(request, callback)
    
    
    public getCluster(request: google.cloud.managedkafka.v1.IGetClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.GetClusterCallback): void;

Calls GetCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
`callback` |  `[GetClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Cluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request)
    
    
    public getCluster(request: google.cloud.managedkafka.v1.IGetClusterRequest): Promise<google.cloud.managedkafka.v1.Cluster>;

Calls GetCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.cluster-class)>` | Promise  
  
### getConsumerGroup(request, callback)
    
    
    public getConsumerGroup(request: google.cloud.managedkafka.v1.IGetConsumerGroupRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.GetConsumerGroupCallback): void;

Calls GetConsumerGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconsumergrouprequest)`   
GetConsumerGroupRequest message or plain object  
`callback` |  `[GetConsumerGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ConsumerGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConsumerGroup(request)
    
    
    public getConsumerGroup(request: google.cloud.managedkafka.v1.IGetConsumerGroupRequest): Promise<google.cloud.managedkafka.v1.ConsumerGroup>;

Calls GetConsumerGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igetconsumergrouprequest)`   
GetConsumerGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ConsumerGroup](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.consumergroup)>` | Promise  
  
### getTopic(request, callback)
    
    
    public getTopic(request: google.cloud.managedkafka.v1.IGetTopicRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.GetTopicCallback): void;

Calls GetTopic.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igettopicrequest)`   
GetTopicRequest message or plain object  
`callback` |  `[GetTopicCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Topic  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTopic(request)
    
    
    public getTopic(request: google.cloud.managedkafka.v1.IGetTopicRequest): Promise<google.cloud.managedkafka.v1.Topic>;

Calls GetTopic.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.igettopicrequest)`   
GetTopicRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Topic](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.topic)>` | Promise  
  
### listAcls(request, callback)
    
    
    public listAcls(request: google.cloud.managedkafka.v1.IListAclsRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.ListAclsCallback): void;

Calls ListAcls.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAclsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistaclsrequest)`   
ListAclsRequest message or plain object  
`callback` |  `[ListAclsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAclsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAcls(request)
    
    
    public listAcls(request: google.cloud.managedkafka.v1.IListAclsRequest): Promise<google.cloud.managedkafka.v1.ListAclsResponse>;

Calls ListAcls.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAclsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistaclsrequest)`   
ListAclsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListAclsResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listaclsresponse)>` | Promise  
  
### listClusters(request, callback)
    
    
    public listClusters(request: google.cloud.managedkafka.v1.IListClustersRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.ListClustersCallback): void;

Calls ListClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
`callback` |  `[ListClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request)
    
    
    public listClusters(request: google.cloud.managedkafka.v1.IListClustersRequest): Promise<google.cloud.managedkafka.v1.ListClustersResponse>;

Calls ListClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listclustersresponse)>` | Promise  
  
### listConsumerGroups(request, callback)
    
    
    public listConsumerGroups(request: google.cloud.managedkafka.v1.IListConsumerGroupsRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.ListConsumerGroupsCallback): void;

Calls ListConsumerGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconsumergroupsrequest)`   
ListConsumerGroupsRequest message or plain object  
`callback` |  `[ListConsumerGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConsumerGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConsumerGroups(request)
    
    
    public listConsumerGroups(request: google.cloud.managedkafka.v1.IListConsumerGroupsRequest): Promise<google.cloud.managedkafka.v1.ListConsumerGroupsResponse>;

Calls ListConsumerGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilistconsumergroupsrequest)`   
ListConsumerGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListConsumerGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listconsumergroupsresponse)>` | Promise  
  
### listTopics(request, callback)
    
    
    public listTopics(request: google.cloud.managedkafka.v1.IListTopicsRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.ListTopicsCallback): void;

Calls ListTopics.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTopicsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilisttopicsrequest)`   
ListTopicsRequest message or plain object  
`callback` |  `[ListTopicsCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTopicsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTopics(request)
    
    
    public listTopics(request: google.cloud.managedkafka.v1.IListTopicsRequest): Promise<google.cloud.managedkafka.v1.ListTopicsResponse>;

Calls ListTopics.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTopicsRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.ilisttopicsrequest)`   
ListTopicsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ListTopicsResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.listtopicsresponse)>` | Promise  
  
### removeAclEntry(request, callback)
    
    
    public removeAclEntry(request: google.cloud.managedkafka.v1.IRemoveAclEntryRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.RemoveAclEntryCallback): void;

Calls RemoveAclEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAclEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iremoveaclentryrequest)`   
RemoveAclEntryRequest message or plain object  
`callback` |  `[RemoveAclEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveAclEntryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAclEntry(request)
    
    
    public removeAclEntry(request: google.cloud.managedkafka.v1.IRemoveAclEntryRequest): Promise<google.cloud.managedkafka.v1.RemoveAclEntryResponse>;

Calls RemoveAclEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAclEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iremoveaclentryrequest)`   
RemoveAclEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.RemoveAclEntryResponse](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.removeaclentryresponse)>` | Promise  
  
### updateAcl(request, callback)
    
    
    public updateAcl(request: google.cloud.managedkafka.v1.IUpdateAclRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.UpdateAclCallback): void;

Calls UpdateAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateaclrequest)`   
UpdateAclRequest message or plain object  
`callback` |  `[UpdateAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Acl  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAcl(request)
    
    
    public updateAcl(request: google.cloud.managedkafka.v1.IUpdateAclRequest): Promise<google.cloud.managedkafka.v1.Acl>;

Calls UpdateAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateaclrequest)`   
UpdateAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Acl](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.acl)>` | Promise  
  
### updateCluster(request, callback)
    
    
    public updateCluster(request: google.cloud.managedkafka.v1.IUpdateClusterRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.UpdateClusterCallback): void;

Calls UpdateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
`callback` |  `[UpdateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request)
    
    
    public updateCluster(request: google.cloud.managedkafka.v1.IUpdateClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.longrunning.operation)>` | Promise  
  
### updateConsumerGroup(request, callback)
    
    
    public updateConsumerGroup(request: google.cloud.managedkafka.v1.IUpdateConsumerGroupRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.UpdateConsumerGroupCallback): void;

Calls UpdateConsumerGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconsumergrouprequest)`   
UpdateConsumerGroupRequest message or plain object  
`callback` |  `[UpdateConsumerGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and ConsumerGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConsumerGroup(request)
    
    
    public updateConsumerGroup(request: google.cloud.managedkafka.v1.IUpdateConsumerGroupRequest): Promise<google.cloud.managedkafka.v1.ConsumerGroup>;

Calls UpdateConsumerGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConsumerGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdateconsumergrouprequest)`   
UpdateConsumerGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.ConsumerGroup](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.consumergroup)>` | Promise  
  
### updateTopic(request, callback)
    
    
    public updateTopic(request: google.cloud.managedkafka.v1.IUpdateTopicRequest, callback: google.cloud.managedkafka.v1.ManagedKafka.UpdateTopicCallback): void;

Calls UpdateTopic.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdatetopicrequest)`   
UpdateTopicRequest message or plain object  
`callback` |  `[UpdateTopicCallback](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/overview.html)`   
Node-style callback called with the error, if any, and Topic  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTopic(request)
    
    
    public updateTopic(request: google.cloud.managedkafka.v1.IUpdateTopicRequest): Promise<google.cloud.managedkafka.v1.Topic>;

Calls UpdateTopic.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTopicRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.iupdatetopicrequest)`   
UpdateTopicRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.managedkafka.v1.Topic](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/managedkafka/protos.google.cloud.managedkafka.v1.topic)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
