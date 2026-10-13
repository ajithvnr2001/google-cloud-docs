---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig
title: Vertex AI Notebooks v1 API - Class InstanceConfig (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:26.872586+00:00
---

# Vertex AI Notebooks v1 API - Class InstanceConfig (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v1 API - Class InstanceConfig (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.5.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.4.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.3.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.2.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.1.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.0.0/Google.Cloud.Notebooks.V1.InstanceConfig)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/1.0.0-beta04/Google.Cloud.Notebooks.V1.InstanceConfig)


    
    
    public sealed class InstanceConfig : IMessage<InstanceConfig>, IEquatable<InstanceConfig>, IDeepCloneable<InstanceConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v1 API class InstanceConfig.

Notebook instance configurations that can be updated.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InstanceConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1)

## Assembly

Google.Cloud.Notebooks.V1.dll

## Constructors 

### InstanceConfig()
    
    
    public InstanceConfig()

### InstanceConfig(InstanceConfig)
    
    
    public InstanceConfig(InstanceConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceConfig)`  
  
  
## Properties 

### EnableHealthMonitoring
    
    
    public bool EnableHealthMonitoring { get; set; }

Verifies core internal services are running.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NotebookUpgradeSchedule
    
    
    public string NotebookUpgradeSchedule { get; set; }

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
