---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafka.ManagedKafkaBase
title: Managed Service for Apache Kafka API v1 API - Class ManagedKafka.ManagedKafkaBase (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:47.994870+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ManagedKafka.ManagedKafkaBase (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafka.ManagedKafkaBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ManagedKafka.ManagedKafkaBase (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafka.ManagedKafkaBase)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ManagedKafka.ManagedKafkaBase)


    
    
    [BindServiceMethod(typeof(ManagedKafka), "BindService")]
    public abstract class ManagedKafka.ManagedKafkaBase

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ManagedKafka.ManagedKafkaBase.

Base class for server-side implementations of ManagedKafka

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedKafka.ManagedKafkaBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Methods 

### AddAclEntry(AddAclEntryRequest, ServerCallContext)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntry(AddAclEntryRequest request, ServerCallContext context)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | The response to send back to the client (wrapped by a task).  
  
### CreateAcl(CreateAclRequest, ServerCallContext)
    
    
    public virtual Task<Acl> CreateAcl(CreateAclRequest request, ServerCallContext context)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The response to send back to the client (wrapped by a task).  
  
### CreateCluster(CreateClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateCluster(CreateClusterRequest request, ServerCallContext context)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateTopic(CreateTopicRequest, ServerCallContext)
    
    
    public virtual Task<Topic> CreateTopic(CreateTopicRequest request, ServerCallContext context)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateTopicRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAcl(DeleteAclRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteAcl(DeleteAclRequest request, ServerCallContext context)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteAclRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteCluster(DeleteClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteCluster(DeleteClusterRequest request, ServerCallContext context)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteConsumerGroup(DeleteConsumerGroupRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteConsumerGroup(DeleteConsumerGroupRequest request, ServerCallContext context)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConsumerGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteTopic(DeleteTopicRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteTopic(DeleteTopicRequest request, ServerCallContext context)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteTopicRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAcl(GetAclRequest, ServerCallContext)
    
    
    public virtual Task<Acl> GetAcl(GetAclRequest request, ServerCallContext context)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetAclRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The response to send back to the client (wrapped by a task).  
  
### GetCluster(GetClusterRequest, ServerCallContext)
    
    
    public virtual Task<Cluster> GetCluster(GetClusterRequest request, ServerCallContext context)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | The response to send back to the client (wrapped by a task).  
  
### GetConsumerGroup(GetConsumerGroupRequest, ServerCallContext)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroup(GetConsumerGroupRequest request, ServerCallContext context)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConsumerGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The response to send back to the client (wrapped by a task).  
  
### GetTopic(GetTopicRequest, ServerCallContext)
    
    
    public virtual Task<Topic> GetTopic(GetTopicRequest request, ServerCallContext context)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetTopicRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The response to send back to the client (wrapped by a task).  
  
### ListAcls(ListAclsRequest, ServerCallContext)
    
    
    public virtual Task<ListAclsResponse> ListAcls(ListAclsRequest request, ServerCallContext context)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListClusters(ListClustersRequest, ServerCallContext)
    
    
    public virtual Task<ListClustersResponse> ListClusters(ListClustersRequest request, ServerCallContext context)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListConsumerGroups(ListConsumerGroupsRequest, ServerCallContext)
    
    
    public virtual Task<ListConsumerGroupsResponse> ListConsumerGroups(ListConsumerGroupsRequest request, ServerCallContext context)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConsumerGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListTopics(ListTopicsRequest, ServerCallContext)
    
    
    public virtual Task<ListTopicsResponse> ListTopics(ListTopicsRequest request, ServerCallContext context)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)` | The response to send back to the client (wrapped by a task).  
  
### RemoveAclEntry(RemoveAclEntryRequest, ServerCallContext)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntry(RemoveAclEntryRequest request, ServerCallContext context)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAcl(UpdateAclRequest, ServerCallContext)
    
    
    public virtual Task<Acl> UpdateAcl(UpdateAclRequest request, ServerCallContext context)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateAclRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The response to send back to the client (wrapped by a task).  
  
### UpdateCluster(UpdateClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateCluster(UpdateClusterRequest request, ServerCallContext context)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateConsumerGroup(UpdateConsumerGroupRequest, ServerCallContext)
    
    
    public virtual Task<ConsumerGroup> UpdateConsumerGroup(UpdateConsumerGroupRequest request, ServerCallContext context)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConsumerGroupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The response to send back to the client (wrapped by a task).  
  
### UpdateTopic(UpdateTopicRequest, ServerCallContext)
    
    
    public virtual Task<Topic> UpdateTopic(UpdateTopicRequest request, ServerCallContext context)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateTopicRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
