---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse
title: Config Delivery v1 API - Class ListFleetPackagesResponse (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:54.011932+00:00
---

# Config Delivery v1 API - Class ListFleetPackagesResponse (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1 API - Class ListFleetPackagesResponse (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ListFleetPackagesResponse : IMessage<ListFleetPackagesResponse>, IEquatable<ListFleetPackagesResponse>, IDeepCloneable<ListFleetPackagesResponse>, IBufferMessage, IMessage, IPageResponse<FleetPackage>, IEnumerable<FleetPackage>, IEnumerable

Reference documentation and code samples for the Config Delivery v1 API class ListFleetPackagesResponse.

Message for response to listing FleetPackage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListFleetPackagesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1)

## Assembly

Google.Cloud.ConfigDelivery.V1.dll

## Constructors 

### ListFleetPackagesResponse()
    
    
    public ListFleetPackagesResponse()

### ListFleetPackagesResponse(ListFleetPackagesResponse)
    
    
    public ListFleetPackagesResponse(ListFleetPackagesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse)`  
  
  
## Properties 

### FleetPackages
    
    
    public RepeatedField<FleetPackage> FleetPackages { get; }

The list of FleetPackage

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token identifying a page of results the server should return.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Unordered list. Locations that could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<FleetPackage> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
