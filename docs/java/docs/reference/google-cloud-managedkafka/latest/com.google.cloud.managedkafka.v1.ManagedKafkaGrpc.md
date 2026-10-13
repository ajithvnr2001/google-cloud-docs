---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc
title: Class ManagedKafkaGrpc (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:57.763783+00:00
---

# Class ManagedKafkaGrpc (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ManagedKafkaGrpc (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class ManagedKafkaGrpc

The service that a client application uses to manage Apache Kafka clusters, topics and consumer groups.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ManagedKafkaGrpc

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(ManagedKafkaGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(ManagedKafkaGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[ManagedKafkaGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAddAclEntryMethod()
    
    
    public static MethodDescriptor<AddAclEntryRequest,AddAclEntryResponse> getAddAclEntryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AddAclEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.AddAclEntryRequest),[AddAclEntryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.AddAclEntryResponse)>` |   
  
### getCreateAclMethod()
    
    
    public static MethodDescriptor<CreateAclRequest,Acl> getCreateAclMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateAclRequest),[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Acl)>` |   
  
### getCreateClusterMethod()
    
    
    public static MethodDescriptor<CreateClusterRequest,Operation> getCreateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateTopicMethod()
    
    
    public static MethodDescriptor<CreateTopicRequest,Topic> getCreateTopicMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateTopicRequest),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic)>` |   
  
### getDeleteAclMethod()
    
    
    public static MethodDescriptor<DeleteAclRequest,Empty> getDeleteAclMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteAclRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteClusterMethod()
    
    
    public static MethodDescriptor<DeleteClusterRequest,Operation> getDeleteClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteConsumerGroupMethod()
    
    
    public static MethodDescriptor<DeleteConsumerGroupRequest,Empty> getDeleteConsumerGroupMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteConsumerGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteTopicMethod()
    
    
    public static MethodDescriptor<DeleteTopicRequest,Empty> getDeleteTopicMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteTopicRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetAclMethod()
    
    
    public static MethodDescriptor<GetAclRequest,Acl> getGetAclMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GetAclRequest),[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Acl)>` |   
  
### getGetClusterMethod()
    
    
    public static MethodDescriptor<GetClusterRequest,Cluster> getGetClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster)>` |   
  
### getGetConsumerGroupMethod()
    
    
    public static MethodDescriptor<GetConsumerGroupRequest,ConsumerGroup> getGetConsumerGroupMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GetConsumerGroupRequest),[ConsumerGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroup)>` |   
  
### getGetTopicMethod()
    
    
    public static MethodDescriptor<GetTopicRequest,Topic> getGetTopicMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GetTopicRequest),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic)>` |   
  
### getListAclsMethod()
    
    
    public static MethodDescriptor<ListAclsRequest,ListAclsResponse> getListAclsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAclsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListAclsRequest),[ListAclsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListAclsResponse)>` |   
  
### getListClustersMethod()
    
    
    public static MethodDescriptor<ListClustersRequest,ListClustersResponse> getListClustersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListClustersResponse)>` |   
  
### getListConsumerGroupsMethod()
    
    
    public static MethodDescriptor<ListConsumerGroupsRequest,ListConsumerGroupsResponse> getListConsumerGroupsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListConsumerGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListConsumerGroupsRequest),[ListConsumerGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListConsumerGroupsResponse)>` |   
  
### getListTopicsMethod()
    
    
    public static MethodDescriptor<ListTopicsRequest,ListTopicsResponse> getListTopicsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListTopicsRequest),[ListTopicsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ListTopicsResponse)>` |   
  
### getRemoveAclEntryMethod()
    
    
    public static MethodDescriptor<RemoveAclEntryRequest,RemoveAclEntryResponse> getRemoveAclEntryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RemoveAclEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RemoveAclEntryRequest),[RemoveAclEntryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RemoveAclEntryResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateAclMethod()
    
    
    public static MethodDescriptor<UpdateAclRequest,Acl> getUpdateAclMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateAclRequest),[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Acl)>` |   
  
### getUpdateClusterMethod()
    
    
    public static MethodDescriptor<UpdateClusterRequest,Operation> getUpdateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateConsumerGroupMethod()
    
    
    public static MethodDescriptor<UpdateConsumerGroupRequest,ConsumerGroup> getUpdateConsumerGroupMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateConsumerGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateConsumerGroupRequest),[ConsumerGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroup)>` |   
  
### getUpdateTopicMethod()
    
    
    public static MethodDescriptor<UpdateTopicRequest,Topic> getUpdateTopicMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateTopicRequest),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Topic)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static ManagedKafkaGrpc.ManagedKafkaBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaGrpc.ManagedKafkaBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc.ManagedKafkaBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static ManagedKafkaGrpc.ManagedKafkaBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaGrpc.ManagedKafkaBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc.ManagedKafkaBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static ManagedKafkaGrpc.ManagedKafkaFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaGrpc.ManagedKafkaFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc.ManagedKafkaFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static ManagedKafkaGrpc.ManagedKafkaStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaGrpc.ManagedKafkaStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaGrpc.ManagedKafkaStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
