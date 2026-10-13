---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult
title: Model Armor v1beta API - Class MaliciousUriFilterResult (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:23.121544+00:00
---

# Model Armor v1beta API - Class MaliciousUriFilterResult (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class MaliciousUriFilterResult (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class MaliciousUriFilterResult : IMessage<MaliciousUriFilterResult>, IEquatable<MaliciousUriFilterResult>, IDeepCloneable<MaliciousUriFilterResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class MaliciousUriFilterResult.

Malicious URI Filter Result.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaliciousUriFilterResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### MaliciousUriFilterResult()
    
    
    public MaliciousUriFilterResult()

### MaliciousUriFilterResult(MaliciousUriFilterResult)
    
    
    public MaliciousUriFilterResult(MaliciousUriFilterResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult)`  
  
  
## Properties 

### ExecutionState
    
    
    public FilterExecutionState ExecutionState { get; set; }

Output only. Reports whether Malicious URI filter was successfully executed or not.

**Property Value**  
---  
**Type** | **Description**  
`[FilterExecutionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterExecutionState)` |   
  
### MaliciousUriMatchedItems
    
    
    public RepeatedField<MaliciousUriFilterResult.Types.MaliciousUriMatchedItem> MaliciousUriMatchedItems { get; }

List of Malicious URIs found in data.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult.Types)[MaliciousUriMatchedItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult.Types.MaliciousUriMatchedItem)` |   
  
### MatchState
    
    
    public FilterMatchState MatchState { get; set; }

Output only. Match state for this Malicious URI. Value is MATCH_FOUND if at least one Malicious URI is found.

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
