---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest
title: Discovery Engine v1beta API - Class UpdateSampleQuerySetRequest (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:07.606042+00:00
---

# Discovery Engine v1beta API - Class UpdateSampleQuerySetRequest (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class UpdateSampleQuerySetRequest (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class UpdateSampleQuerySetRequest : IMessage<UpdateSampleQuerySetRequest>, IEquatable<UpdateSampleQuerySetRequest>, IDeepCloneable<UpdateSampleQuerySetRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class UpdateSampleQuerySetRequest.

Request message for [SampleQuerySetService.UpdateSampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateSampleQuerySetRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateSampleQuerySetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateSampleQuerySetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateSampleQuerySetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### UpdateSampleQuerySetRequest()
    
    
    public UpdateSampleQuerySetRequest()

### UpdateSampleQuerySetRequest(UpdateSampleQuerySetRequest)
    
    
    public UpdateSampleQuerySetRequest(UpdateSampleQuerySetRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateSampleQuerySetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQuerySetRequest)`  
  
  
## Properties 

### SampleQuerySet
    
    
    public SampleQuerySet SampleQuerySet { get; set; }

Required. The sample query set to update.

If the caller does not have permission to update the [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet] to update does not exist a `NOT_FOUND` error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[SampleQuerySet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQuerySet)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Indicates which fields in the provided imported 'sample query set' to update. If not set, will by default update all fields.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
