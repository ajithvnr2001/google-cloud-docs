---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting
title: Model Armor v1beta API - Class AiPlatformFloorSetting (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:20.213744+00:00
---

# Model Armor v1beta API - Class AiPlatformFloorSetting (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class AiPlatformFloorSetting (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class AiPlatformFloorSetting : IMessage<AiPlatformFloorSetting>, IEquatable<AiPlatformFloorSetting>, IDeepCloneable<AiPlatformFloorSetting>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class AiPlatformFloorSetting.

message describing AiPlatformFloorSetting

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AiPlatformFloorSetting

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AiPlatformFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AiPlatformFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AiPlatformFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### AiPlatformFloorSetting()
    
    
    public AiPlatformFloorSetting()

### AiPlatformFloorSetting(AiPlatformFloorSetting)
    
    
    public AiPlatformFloorSetting(AiPlatformFloorSetting other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AiPlatformFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting)`  
  
  
## Properties 

### EnableCloudLogging
    
    
    public bool EnableCloudLogging { get; set; }

Optional. If true, log Model Armor filter results to Cloud Logging.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnforcementTypeCase
    
    
    public AiPlatformFloorSetting.EnforcementTypeOneofCase EnforcementTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AiPlatformFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting)[EnforcementTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.AiPlatformFloorSetting.EnforcementTypeOneofCase)` |   
  
### HasInspectAndBlock
    
    
    public bool HasInspectAndBlock { get; }

Gets whether the "inspect_and_block" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInspectOnly
    
    
    public bool HasInspectOnly { get; }

Gets whether the "inspect_only" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InspectAndBlock
    
    
    public bool InspectAndBlock { get; set; }

Optional. If true, Model Armor filters will be run in inspect and block mode. Requests that trip Model Armor filters will be blocked.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InspectOnly
    
    
    public bool InspectOnly { get; set; }

Optional. If true, Model Armor filters will be run in inspect only mode. No action will be taken on the request.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
