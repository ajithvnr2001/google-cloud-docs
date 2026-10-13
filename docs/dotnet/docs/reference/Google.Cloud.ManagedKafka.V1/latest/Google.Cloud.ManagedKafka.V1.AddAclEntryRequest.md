---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest
title: Managed Service for Apache Kafka API v1 API - Class AddAclEntryRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:36.451653+00:00
---

# Managed Service for Apache Kafka API v1 API - Class AddAclEntryRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class AddAclEntryRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)


    
    
    public sealed class AddAclEntryRequest : IMessage<AddAclEntryRequest>, IEquatable<AddAclEntryRequest>, IDeepCloneable<AddAclEntryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class AddAclEntryRequest.

Request for AddAclEntry.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddAclEntryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### AddAclEntryRequest()
    
    
    public AddAclEntryRequest()

### AddAclEntryRequest(AddAclEntryRequest)
    
    
    public AddAclEntryRequest(AddAclEntryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)`  
  
  
## Properties 

### Acl
    
    
    public string Acl { get; set; }

Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`.

The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AclAsAclName
    
    
    public AclName AclAsAclName { get; set; }

[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)-typed view over the [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest#Google_Cloud_ManagedKafka_V1_AddAclEntryRequest_Acl) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)` |   
  
### AclEntry
    
    
    public AclEntry AclEntry { get; set; }

Required. The acl entry to add.

**Property Value**  
---  
**Type** | **Description**  
`[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
