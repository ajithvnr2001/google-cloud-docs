---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest
title: Google Cloud Web Risk v1beta1 API - Class ComputeThreatListDiffRequest (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:04.052951+00:00
---

# Google Cloud Web Risk v1beta1 API - Class ComputeThreatListDiffRequest (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Web Risk v1beta1 API - Class ComputeThreatListDiffRequest (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/3.0.0-beta05/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/2.0.0-beta05/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest)


    
    
    public sealed class ComputeThreatListDiffRequest : IMessage<ComputeThreatListDiffRequest>, IEquatable<ComputeThreatListDiffRequest>, IDeepCloneable<ComputeThreatListDiffRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Web Risk v1beta1 API class ComputeThreatListDiffRequest.

Describes an API diff request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComputeThreatListDiffRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComputeThreatListDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComputeThreatListDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComputeThreatListDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WebRisk.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1)

## Assembly

Google.Cloud.WebRisk.V1Beta1.dll

## Constructors 

### ComputeThreatListDiffRequest()
    
    
    public ComputeThreatListDiffRequest()

### ComputeThreatListDiffRequest(ComputeThreatListDiffRequest)
    
    
    public ComputeThreatListDiffRequest(ComputeThreatListDiffRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComputeThreatListDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest)`  
  
  
## Properties 

### Constraints
    
    
    public ComputeThreatListDiffRequest.Types.Constraints Constraints { get; set; }

Required. The constraints associated with this request.

**Property Value**  
---  
**Type** | **Description**  
`[ComputeThreatListDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest.Types)[Constraints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ComputeThreatListDiffRequest.Types.Constraints)` |   
  
### ThreatType
    
    
    public ThreatType ThreatType { get; set; }

The ThreatList to update.

**Property Value**  
---  
**Type** | **Description**  
`[ThreatType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatType)` |   
  
### VersionToken
    
    
    public ByteString VersionToken { get; set; }

The current version token of the client for the requested list (the client version that was received from the last successful diff).

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
