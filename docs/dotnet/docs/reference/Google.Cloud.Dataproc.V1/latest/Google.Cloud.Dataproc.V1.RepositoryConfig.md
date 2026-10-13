---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig
title: Google Cloud Dataproc v1 API - Class RepositoryConfig (5.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:11.313172+00:00
---

# Google Cloud Dataproc v1 API - Class RepositoryConfig (5.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dataproc v1 API - Class RepositoryConfig (5.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.28.0 (latest)  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.19.0  5.18.0  5.17.0  5.16.0  5.15.0  5.14.0  5.13.0  5.12.0  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.0.0  3.4.0  3.3.0  3.2.0  3.1.0 
    
    
    public sealed class RepositoryConfig : IMessage<RepositoryConfig>, IEquatable<RepositoryConfig>, IDeepCloneable<RepositoryConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dataproc v1 API class RepositoryConfig.

Configuration for dependency repositories

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RepositoryConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataproc.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1)

## Assembly

Google.Cloud.Dataproc.V1.dll

## Constructors 

### RepositoryConfig()
    
    
    public RepositoryConfig()

### RepositoryConfig(RepositoryConfig)
    
    
    public RepositoryConfig(RepositoryConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.RepositoryConfig)`  
  
  
## Properties 

### PypiRepositoryConfig
    
    
    public PyPiRepositoryConfig PypiRepositoryConfig { get; set; }

Optional. Configuration for PyPi repository.

**Property Value**  
---  
**Type** | **Description**  
`[PyPiRepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.PyPiRepositoryConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
