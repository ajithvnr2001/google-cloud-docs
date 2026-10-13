---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings
title: Model Armor v1beta API - Class PiAndJailbreakFilterSettings (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:26.102047+00:00
---

# Model Armor v1beta API - Class PiAndJailbreakFilterSettings (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class PiAndJailbreakFilterSettings (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class PiAndJailbreakFilterSettings : IMessage<PiAndJailbreakFilterSettings>, IEquatable<PiAndJailbreakFilterSettings>, IDeepCloneable<PiAndJailbreakFilterSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class PiAndJailbreakFilterSettings.

Prompt injection and Jailbreak Filter settings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PiAndJailbreakFilterSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### PiAndJailbreakFilterSettings()
    
    
    public PiAndJailbreakFilterSettings()

### PiAndJailbreakFilterSettings(PiAndJailbreakFilterSettings)
    
    
    public PiAndJailbreakFilterSettings(PiAndJailbreakFilterSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings)`  
  
  
## Properties 

### ConfidenceLevel
    
    
    public DetectionConfidenceLevel ConfidenceLevel { get; set; }

Optional. Confidence level for this filter. Confidence level is used to determine the threshold for the filter. If detection confidence is equal to or greater than the specified level, a positive match is reported. Confidence level will only be used if the filter is enabled.

**Property Value**  
---  
**Type** | **Description**  
`[DetectionConfidenceLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DetectionConfidenceLevel)` |   
  
### FilterEnforcement
    
    
    public PiAndJailbreakFilterSettings.Types.PiAndJailbreakFilterEnforcement FilterEnforcement { get; set; }

Optional. Tells whether Prompt injection and Jailbreak filter is enabled or disabled.

**Property Value**  
---  
**Type** | **Description**  
`[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings.Types)[PiAndJailbreakFilterEnforcement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterSettings.Types.PiAndJailbreakFilterEnforcement)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
