---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo
title: Google Cloud Audit API - Class ViolationInfo (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:38.211676+00:00
---

# Google Cloud Audit API - Class ViolationInfo (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Audit API - Class ViolationInfo (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.5.0/Google.Cloud.Audit.ViolationInfo)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.4.0/Google.Cloud.Audit.ViolationInfo)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.3.0/Google.Cloud.Audit.ViolationInfo)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.2.0/Google.Cloud.Audit.ViolationInfo)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.1.0/Google.Cloud.Audit.ViolationInfo)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/2.0.0/Google.Cloud.Audit.ViolationInfo)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/1.1.0/Google.Cloud.Audit.ViolationInfo)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/1.0.0/Google.Cloud.Audit.ViolationInfo)


    
    
    public sealed class ViolationInfo : IMessage<ViolationInfo>, IEquatable<ViolationInfo>, IDeepCloneable<ViolationInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Audit API class ViolationInfo.

Provides information about the Policy violation info for this request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ViolationInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ViolationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ViolationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ViolationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Audit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit)

## Assembly

Google.Cloud.Audit.dll

## Constructors 

### ViolationInfo()
    
    
    public ViolationInfo()

### ViolationInfo(ViolationInfo)
    
    
    public ViolationInfo(ViolationInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ViolationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo)`  
  
  
## Properties 

### CheckedValue
    
    
    public string CheckedValue { get; set; }

Optional. Value that is being checked for the policy. This could be in encrypted form (if pii sensitive). This field will only be emitted in LIST_POLICY types

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Constraint
    
    
    public string Constraint { get; set; }

Optional. Constraint name

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ErrorMessage
    
    
    public string ErrorMessage { get; set; }

Optional. Error message that policy is indicating.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyType
    
    
    public ViolationInfo.Types.PolicyType PolicyType { get; set; }

Optional. Indicates the type of the policy.

**Property Value**  
---  
**Type** | **Description**  
`[ViolationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo.Types)[PolicyType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Audit/latest/Google.Cloud.Audit.ViolationInfo.Types.PolicyType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
