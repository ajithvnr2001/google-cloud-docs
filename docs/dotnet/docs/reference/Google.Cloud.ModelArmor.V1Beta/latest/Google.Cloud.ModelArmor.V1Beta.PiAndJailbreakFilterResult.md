---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult
title: Model Armor v1beta API - Class PiAndJailbreakFilterResult (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:07.543329+00:00
---

# Model Armor v1beta API - Class PiAndJailbreakFilterResult (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class PiAndJailbreakFilterResult (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class PiAndJailbreakFilterResult : IMessage<PiAndJailbreakFilterResult>, IEquatable<PiAndJailbreakFilterResult>, IDeepCloneable<PiAndJailbreakFilterResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class PiAndJailbreakFilterResult.

Prompt injection and Jailbreak Filter Result.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PiAndJailbreakFilterResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PiAndJailbreakFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PiAndJailbreakFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PiAndJailbreakFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### PiAndJailbreakFilterResult()
    
    
    public PiAndJailbreakFilterResult()

### PiAndJailbreakFilterResult(PiAndJailbreakFilterResult)
    
    
    public PiAndJailbreakFilterResult(PiAndJailbreakFilterResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PiAndJailbreakFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult)`  
  
  
## Properties 

### ConfidenceLevel
    
    
    public DetectionConfidenceLevel ConfidenceLevel { get; set; }

Confidence level identified for Prompt injection and Jailbreak.

**Property Value**  
---  
**Type** | **Description**  
`[DetectionConfidenceLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DetectionConfidenceLevel)` |   
  
### ExecutionState
    
    
    public FilterExecutionState ExecutionState { get; set; }

Output only. Reports whether Prompt injection and Jailbreak filter was successfully executed or not.

**Property Value**  
---  
**Type** | **Description**  
`[FilterExecutionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterExecutionState)` |   
  
### MatchState
    
    
    public FilterMatchState MatchState { get; set; }

Output only. Match state for Prompt injection and Jailbreak.

**Property Value**  
---  
**Type** | **Description**  
`[FilterMatchState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterMatchState)` |   
  
### MessageItems
    
    
    public RepeatedField<MessageItem> MessageItems { get; }

Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MessageItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MessageItem)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
