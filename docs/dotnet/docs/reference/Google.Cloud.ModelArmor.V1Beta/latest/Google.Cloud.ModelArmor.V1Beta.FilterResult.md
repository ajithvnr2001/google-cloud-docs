---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult
title: Model Armor v1beta API - Class FilterResult (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:21.961821+00:00
---

# Model Armor v1beta API - Class FilterResult (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class FilterResult (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class FilterResult : IMessage<FilterResult>, IEquatable<FilterResult>, IDeepCloneable<FilterResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class FilterResult.

Filter Result obtained after Sanitization operations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FilterResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### FilterResult()
    
    
    public FilterResult()

### FilterResult(FilterResult)
    
    
    public FilterResult(FilterResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult)`  
  
  
## Properties 

### CsamFilterFilterResult
    
    
    public CsamFilterResult CsamFilterFilterResult { get; set; }

CSAM filter results.

**Property Value**  
---  
**Type** | **Description**  
`[CsamFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CsamFilterResult)` |   
  
### FilterResultCase
    
    
    public FilterResult.FilterResultOneofCase FilterResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[FilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult)[FilterResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FilterResult.FilterResultOneofCase)` |   
  
### MaliciousUriFilterResult
    
    
    public MaliciousUriFilterResult MaliciousUriFilterResult { get; set; }

Malicious URI filter results.

**Property Value**  
---  
**Type** | **Description**  
`[MaliciousUriFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MaliciousUriFilterResult)` |   
  
### PiAndJailbreakFilterResult
    
    
    public PiAndJailbreakFilterResult PiAndJailbreakFilterResult { get; set; }

Prompt injection and Jailbreak filter results.

**Property Value**  
---  
**Type** | **Description**  
`[PiAndJailbreakFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.PiAndJailbreakFilterResult)` |   
  
### RaiFilterResult
    
    
    public RaiFilterResult RaiFilterResult { get; set; }

Responsible AI filter results.

**Property Value**  
---  
**Type** | **Description**  
`[RaiFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.RaiFilterResult)` |   
  
### SdpFilterResult
    
    
    public SdpFilterResult SdpFilterResult { get; set; }

Sensitive Data Protection results.

**Property Value**  
---  
**Type** | **Description**  
`[SdpFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SdpFilterResult)` |   
  
### VirusScanFilterResult
    
    
    public VirusScanFilterResult VirusScanFilterResult { get; set; }

Virus scan results.

**Property Value**  
---  
**Type** | **Description**  
`[VirusScanFilterResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.VirusScanFilterResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
