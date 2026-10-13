---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange
title: Google Cloud Talent Solution v4beta1 API - Class CompensationInfo.Types.CompensationRange (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:29.148114+00:00
---

# Google Cloud Talent Solution v4beta1 API - Class CompensationInfo.Types.CompensationRange (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4beta1 API - Class CompensationInfo.Types.CompensationRange (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange)


    
    
    public sealed class CompensationInfo.Types.CompensationRange : IMessage<CompensationInfo.Types.CompensationRange>, IEquatable<CompensationInfo.Types.CompensationRange>, IDeepCloneable<CompensationInfo.Types.CompensationRange>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Talent Solution v4beta1 API class CompensationInfo.Types.CompensationRange.

Compensation range.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompensationInfo.Types.CompensationRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CompensationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types)[CompensationRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CompensationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types)[CompensationRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CompensationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types)[CompensationRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Talent.V4Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1)

## Assembly

Google.Cloud.Talent.V4Beta1.dll

## Constructors 

### CompensationRange()
    
    
    public CompensationRange()

### CompensationRange(CompensationRange)
    
    
    public CompensationRange(CompensationInfo.Types.CompensationRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CompensationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types)[CompensationRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompensationInfo.Types.CompensationRange)`  
  
  
## Properties 

### MaxCompensation
    
    
    public Money MaxCompensation { get; set; }

The maximum amount of compensation. If left empty, the value is set to a maximal compensation value and the currency code is set to match the [currency code][google.type.Money.currency_code] of min_compensation.

**Property Value**  
---  
**Type** | **Description**  
`[Money](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Money.html)` |   
  
### MinCompensation
    
    
    public Money MinCompensation { get; set; }

The minimum amount of compensation. If left empty, the value is set to zero and the currency code is set to match the [currency code][google.type.Money.currency_code] of max_compensation.

**Property Value**  
---  
**Type** | **Description**  
`[Money](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Money.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
