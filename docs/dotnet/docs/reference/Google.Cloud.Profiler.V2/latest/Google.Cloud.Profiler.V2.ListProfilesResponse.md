---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse
title: Cloud Profiler v2 API - Class ListProfilesResponse (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:22.572722+00:00
---

# Cloud Profiler v2 API - Class ListProfilesResponse (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Profiler v2 API - Class ListProfilesResponse (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.6.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.5.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.4.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.3.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.2.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.1.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.0.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.2.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.1.0/Google.Cloud.Profiler.V2.ListProfilesResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.0.0/Google.Cloud.Profiler.V2.ListProfilesResponse)


    
    
    public sealed class ListProfilesResponse : IPageResponse<Profile>, IEnumerable<Profile>, IEnumerable, IMessage<ListProfilesResponse>, IEquatable<ListProfilesResponse>, IDeepCloneable<ListProfilesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Profiler v2 API class ListProfilesResponse.

ListProfileResponse contains the list of collected profiles for deployments in projects which the user has permissions to view.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListProfilesResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Profile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.Profile), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Profile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.Profile), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Profiler.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2)

## Assembly

Google.Cloud.Profiler.V2.dll

## Constructors 

### ListProfilesResponse()
    
    
    public ListProfilesResponse()

### ListProfilesResponse(ListProfilesResponse)
    
    
    public ListProfilesResponse(ListProfilesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

Token to receive the next page of results. This field maybe empty if there are no more profiles to fetch.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Profiles
    
    
    public RepeatedField<Profile> Profiles { get; }

List of profiles fetched.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Profile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.Profile)` |   
  
### SkippedProfiles
    
    
    public int SkippedProfiles { get; set; }

Number of profiles that were skipped in the current page since they were not able to be fetched successfully. This should typically be zero. A non-zero value may indicate a transient failure, in which case if the number is too high for your use case, the call may be retried.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Profile> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Profile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.Profile)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
