---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest
title: Cloud Document AI v1 API - Class ListProcessorTypesRequest (3.25.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:09.433542+00:00
---

# Cloud Document AI v1 API - Class ListProcessorTypesRequest (3.25.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1 API - Class ListProcessorTypesRequest (3.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.25.0 (latest)  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListProcessorTypesRequest : IMessage<ListProcessorTypesRequest>, IEquatable<ListProcessorTypesRequest>, IDeepCloneable<ListProcessorTypesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Document AI v1 API class ListProcessorTypesRequest.

Request message for the [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes] method. Some processor types may require the project be added to an allowlist.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListProcessorTypesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1)

## Assembly

Google.Cloud.DocumentAI.V1.dll

## Constructors 

### ListProcessorTypesRequest()
    
    
    public ListProcessorTypesRequest()

### ListProcessorTypesRequest(ListProcessorTypesRequest)
    
    
    public ListProcessorTypesRequest(ListProcessorTypesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of processor types to return. If unspecified, at most `100` processor types will be returned. The maximum value is `500`. Values above `500` will be coerced to `500`.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Used to retrieve the next page of results, empty if at the end of the list.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest#Google_Cloud_DocumentAI_V1_ListProcessorTypesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
