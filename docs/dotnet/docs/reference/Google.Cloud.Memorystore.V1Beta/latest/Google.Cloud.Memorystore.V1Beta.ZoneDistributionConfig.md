---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig
title: Memorystore v1beta API - Class ZoneDistributionConfig (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:47.435229+00:00
---

# Memorystore v1beta API - Class ZoneDistributionConfig (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class ZoneDistributionConfig (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    public sealed class ZoneDistributionConfig : IMessage<ZoneDistributionConfig>, IEquatable<ZoneDistributionConfig>, IDeepCloneable<ZoneDistributionConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1beta API class ZoneDistributionConfig.

Zone distribution configuration for allocation of instance resources.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ZoneDistributionConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ZoneDistributionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ZoneDistributionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ZoneDistributionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Constructors 

### ZoneDistributionConfig()
    
    
    public ZoneDistributionConfig()

### ZoneDistributionConfig(ZoneDistributionConfig)
    
    
    public ZoneDistributionConfig(ZoneDistributionConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ZoneDistributionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig)`  
  
  
## Properties 

### Mode
    
    
    public ZoneDistributionConfig.Types.ZoneDistributionMode Mode { get; set; }

Optional. Current zone distribution mode. Defaults to MULTI_ZONE.

**Property Value**  
---  
**Type** | **Description**  
`[ZoneDistributionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig.Types)[ZoneDistributionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ZoneDistributionConfig.Types.ZoneDistributionMode)` |   
  
### Zone
    
    
    public string Zone { get; set; }

Optional. Defines zone where all resources will be allocated with SINGLE_ZONE mode. Ignored for MULTI_ZONE mode.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
