---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig
title: Google Cloud Memorystore for Redis (cluster management) v1 API - Class PscConfig (1.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:42.463263+00:00
---

# Google Cloud Memorystore for Redis (cluster management) v1 API - Class PscConfig (1.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis (cluster management) v1 API - Class PscConfig (1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class PscConfig : IMessage<PscConfig>, IEquatable<PscConfig>, IDeepCloneable<PscConfig>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PscConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.Cluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1)

## Assembly

Google.Cloud.Redis.Cluster.V1.dll

## Constructors 

### PscConfig()
    
    
    public PscConfig()

### PscConfig(PscConfig)
    
    
    public PscConfig(PscConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.PscConfig)`  
  
  
## Properties 

### Network
    
    
    public string Network { get; set; }

Required. The network where the IP address of the discovery endpoint will be reserved, in the form of projects/{network_project}/global/networks/{network_id}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
