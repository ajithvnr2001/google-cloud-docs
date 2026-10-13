---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals
title: Google Cloud Web Risk v1beta1 API - Class ThreatEntryRemovals (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:47.258730+00:00
---

# Google Cloud Web Risk v1beta1 API - Class ThreatEntryRemovals (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Web Risk v1beta1 API - Class ThreatEntryRemovals (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/3.0.0-beta05/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/2.0.0-beta05/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals)


    
    
    public sealed class ThreatEntryRemovals : IMessage<ThreatEntryRemovals>, IEquatable<ThreatEntryRemovals>, IDeepCloneable<ThreatEntryRemovals>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Web Risk v1beta1 API class ThreatEntryRemovals.

Contains the set of entries to remove from a local database.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ThreatEntryRemovals

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ThreatEntryRemovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ThreatEntryRemovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ThreatEntryRemovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WebRisk.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1)

## Assembly

Google.Cloud.WebRisk.V1Beta1.dll

## Constructors 

### ThreatEntryRemovals()
    
    
    public ThreatEntryRemovals()

### ThreatEntryRemovals(ThreatEntryRemovals)
    
    
    public ThreatEntryRemovals(ThreatEntryRemovals other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ThreatEntryRemovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.ThreatEntryRemovals)`  
  
  
## Properties 

### RawIndices
    
    
    public RawIndices RawIndices { get; set; }

The raw removal indices for a local list.

**Property Value**  
---  
**Type** | **Description**  
`[RawIndices](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.RawIndices)` |   
  
### RiceIndices
    
    
    public RiceDeltaEncoding RiceIndices { get; set; }

The encoded local, lexicographically-sorted list indices, using a Golomb-Rice encoding. Used for sending compressed removal indices. The removal indices (uint32) are sorted in ascending order, then delta encoded and stored as encoded_data.

**Property Value**  
---  
**Type** | **Description**  
`[RiceDeltaEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebRisk.V1Beta1/latest/Google.Cloud.WebRisk.V1Beta1.RiceDeltaEncoding)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
