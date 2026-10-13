---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource
title: Memorystore v1 API - Class SelfManagedSource (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:13.961698+00:00
---

# Memorystore v1 API - Class SelfManagedSource (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1 API - Class SelfManagedSource (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta09 
    
    
    public sealed class SelfManagedSource : IMessage<SelfManagedSource>, IEquatable<SelfManagedSource>, IDeepCloneable<SelfManagedSource>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1 API class SelfManagedSource.

Details of the self-managed source instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SelfManagedSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SelfManagedSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SelfManagedSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SelfManagedSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1)

## Assembly

Google.Cloud.Memorystore.V1.dll

## Constructors 

### SelfManagedSource()
    
    
    public SelfManagedSource()

### SelfManagedSource(SelfManagedSource)
    
    
    public SelfManagedSource(SelfManagedSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SelfManagedSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource)`  
  
  
## Properties 

### IpAddress
    
    
    public string IpAddress { get; set; }

Required. The IP address of the source instance. This IP address should be a stable IP address that can be accessed by the Memorystore instance throughout the migration process.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAttachment
    
    
    public string NetworkAttachment { get; set; }

Required. The resource name of the Private Service Connect Network Attachment used to establish connectivity to the source instance. This network attachment has the following requirements:

  1. It must be in the same project as the Memorystore instance.
  2. It must be in the same region as the Memorystore instance.
  3. The subnet attached to the network attachment must be in the same VPC network as the source instance nodes.



Format: projects/{project}/regions/{region}/networkAttachments/{network_attachment}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAttachmentAsNetworkAttachmentName
    
    
    public NetworkAttachmentName NetworkAttachmentAsNetworkAttachmentName { get; set; }

[NetworkAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.NetworkAttachmentName)-typed view over the [NetworkAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SelfManagedSource#Google_Cloud_Memorystore_V1_SelfManagedSource_NetworkAttachment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.NetworkAttachmentName)` |   
  
### Port
    
    
    public int Port { get; set; }

Required. The port of the source instance. This port should be a stable port that can be accessed by the Memorystore instance throughout the migration process.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
