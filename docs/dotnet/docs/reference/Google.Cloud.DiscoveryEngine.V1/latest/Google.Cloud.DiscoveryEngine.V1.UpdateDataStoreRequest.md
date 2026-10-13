---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest
title: Discovery Engine v1 API - Class UpdateDataStoreRequest (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:07.456877+00:00
---

# Discovery Engine v1 API - Class UpdateDataStoreRequest (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class UpdateDataStoreRequest (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class UpdateDataStoreRequest : IMessage<UpdateDataStoreRequest>, IEquatable<UpdateDataStoreRequest>, IDeepCloneable<UpdateDataStoreRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1 API class UpdateDataStoreRequest.

Request message for [DataStoreService.UpdateDataStore][google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateDataStoreRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### UpdateDataStoreRequest()
    
    
    public UpdateDataStoreRequest()

### UpdateDataStoreRequest(UpdateDataStoreRequest)
    
    
    public UpdateDataStoreRequest(UpdateDataStoreRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateDataStoreRequest)`  
  
  
## Properties 

### DataStore
    
    
    public DataStore DataStore { get; set; }

Required. The [DataStore][google.cloud.discoveryengine.v1.DataStore] to update.

If the caller does not have permission to update the [DataStore][google.cloud.discoveryengine.v1.DataStore], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the [DataStore][google.cloud.discoveryengine.v1.DataStore] to update does not exist, a NOT_FOUND error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Indicates which fields in the provided [DataStore][google.cloud.discoveryengine.v1.DataStore] to update.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
