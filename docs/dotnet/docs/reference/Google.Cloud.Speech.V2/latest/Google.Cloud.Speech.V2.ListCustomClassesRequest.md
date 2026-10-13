---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest
title: Cloud Speech-to-Text v2 API - Class ListCustomClassesRequest (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:43.682861+00:00
---

# Cloud Speech-to-Text v2 API - Class ListCustomClassesRequest (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Speech-to-Text v2 API - Class ListCustomClassesRequest (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.7.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.6.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.5.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.4.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.3.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.2.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.1.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.0.0/Google.Cloud.Speech.V2.ListCustomClassesRequest)


    
    
    public sealed class ListCustomClassesRequest : IMessage<ListCustomClassesRequest>, IEquatable<ListCustomClassesRequest>, IDeepCloneable<ListCustomClassesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Speech-to-Text v2 API class ListCustomClassesRequest.

Request message for the [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListCustomClassesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListCustomClassesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListCustomClassesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListCustomClassesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2)

## Assembly

Google.Cloud.Speech.V2.dll

## Constructors 

### ListCustomClassesRequest()
    
    
    public ListCustomClassesRequest()

### ListCustomClassesRequest(ListCustomClassesRequest)
    
    
    public ListCustomClassesRequest(ListCustomClassesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListCustomClassesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Number of results per requests. A valid page_size ranges from 0 to 100 inclusive. If the page_size is zero or unspecified, a page size of 5 will be chosen. If the page size exceeds 100, it will be coerced down to 100. Note that a call might return fewer results than the requested page size.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

A page token, received from a previous [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses] call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses] must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project and location of CustomClass resources to list. The expected format is `projects/{project}/locations/{location}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ListCustomClassesRequest#Google_Cloud_Speech_V2_ListCustomClassesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ShowDeleted
    
    
    public bool ShowDeleted { get; set; }

Whether, or not, to show resources that have been deleted.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
