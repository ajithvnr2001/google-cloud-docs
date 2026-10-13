---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity
title: Vertex AI Notebooks v1beta1 API - Class ReservationAffinity (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:03.094010+00:00
---

# Vertex AI Notebooks v1beta1 API - Class ReservationAffinity (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v1beta1 API - Class ReservationAffinity (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/2.0.0-beta05/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/1.0.0-beta04/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity)


    
    
    public sealed class ReservationAffinity : IMessage<ReservationAffinity>, IEquatable<ReservationAffinity>, IDeepCloneable<ReservationAffinity>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v1beta1 API class ReservationAffinity.

Reservation Affinity for consuming Zonal reservation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReservationAffinity

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1)

## Assembly

Google.Cloud.Notebooks.V1Beta1.dll

## Constructors 

### ReservationAffinity()
    
    
    public ReservationAffinity()

### ReservationAffinity(ReservationAffinity)
    
    
    public ReservationAffinity(ReservationAffinity other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity)`  
  
  
## Properties 

### ConsumeReservationType
    
    
    public ReservationAffinity.Types.Type ConsumeReservationType { get; set; }

Optional. Type of reservation to consume

**Property Value**  
---  
**Type** | **Description**  
`[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ReservationAffinity.Types.Type)` |   
  
### Key
    
    
    public string Key { get; set; }

Optional. Corresponds to the label key of reservation resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Values
    
    
    public RepeatedField<string> Values { get; }

Optional. Corresponds to the label values of reservation resource.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
