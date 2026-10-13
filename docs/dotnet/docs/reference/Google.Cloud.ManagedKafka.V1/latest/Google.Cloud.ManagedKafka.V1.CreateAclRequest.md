---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest
title: Managed Service for Apache Kafka API v1 API - Class CreateAclRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:41.959655+00:00
---

# Managed Service for Apache Kafka API v1 API - Class CreateAclRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class CreateAclRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.CreateAclRequest)


    
    
    public sealed class CreateAclRequest : IMessage<CreateAclRequest>, IEquatable<CreateAclRequest>, IDeepCloneable<CreateAclRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class CreateAclRequest.

Request for CreateAcl.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateAclRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### CreateAclRequest()
    
    
    public CreateAclRequest()

### CreateAclRequest(CreateAclRequest)
    
    
    public CreateAclRequest(CreateAclRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)`  
  
  
## Properties 

### Acl
    
    
    public Acl Acl { get; set; }

Required. Configuration of the acl to create. Its `name` field is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` |   
  
### AclId
    
    
    public string AclId { get; set; }

Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following:

For acls on the cluster: `cluster`

For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}`

For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}`

For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsClusterName
    
    
    public ClusterName ParentAsClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest#Google_Cloud_ManagedKafka_V1_CreateAclRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
