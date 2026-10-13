---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse
title: Cloud Commerce Producer v1beta API - Class ListServicesResponse (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:48.078541+00:00
---

# Cloud Commerce Producer v1beta API - Class ListServicesResponse (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Commerce Producer v1beta API - Class ListServicesResponse (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class ListServicesResponse : IMessage<ListServicesResponse>, IEquatable<ListServicesResponse>, IDeepCloneable<ListServicesResponse>, IBufferMessage, IMessage, IPageResponse<Service>, IEnumerable<Service>, IEnumerable

Reference documentation and code samples for the Cloud Commerce Producer v1beta API class ListServicesResponse.

Message for response to listing Services

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListServicesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Service), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Service), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CommerceProducer.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta)

## Assembly

Google.Cloud.CommerceProducer.V1Beta.dll

## Constructors 

### ListServicesResponse()
    
    
    public ListServicesResponse()

### ListServicesResponse(ListServicesResponse)
    
    
    public ListServicesResponse(ListServicesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListServicesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Services
    
    
    public RepeatedField<Service> Services { get; }

The list of Service

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Service)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Service> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Service)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
