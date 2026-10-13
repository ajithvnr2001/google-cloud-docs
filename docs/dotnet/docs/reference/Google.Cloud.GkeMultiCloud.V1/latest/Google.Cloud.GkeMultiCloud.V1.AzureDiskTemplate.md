---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate
title: Anthos Multi-Cloud v1 API - Class AzureDiskTemplate (2.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:38.444435+00:00
---

# Anthos Multi-Cloud v1 API - Class AzureDiskTemplate (2.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Anthos Multi-Cloud v1 API - Class AzureDiskTemplate (2.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 
    
    
    [Obsolete]
    public sealed class AzureDiskTemplate : IMessage<AzureDiskTemplate>, IEquatable<AzureDiskTemplate>, IDeepCloneable<AzureDiskTemplate>, IBufferMessage, IMessage

Reference documentation and code samples for the Anthos Multi-Cloud v1 API class AzureDiskTemplate.

Configuration for Azure Disks.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AzureDiskTemplate

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AzureDiskTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AzureDiskTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AzureDiskTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeMultiCloud.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1)

## Assembly

Google.Cloud.GkeMultiCloud.V1.dll

## Constructors 

### AzureDiskTemplate()
    
    
    public AzureDiskTemplate()

### AzureDiskTemplate(AzureDiskTemplate)
    
    
    public AzureDiskTemplate(AzureDiskTemplate other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AzureDiskTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AzureDiskTemplate)`  
  
  
## Properties 

### SizeGib
    
    
    public int SizeGib { get; set; }

Optional. The size of the disk, in GiBs.

When unspecified, a default value is provided. See the specific reference in the parent resource.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
