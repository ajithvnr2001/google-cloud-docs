---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest
title: Cloud Location Finder v1 API - Class SearchCloudLocationsRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:56.110460+00:00
---

# Cloud Location Finder v1 API - Class SearchCloudLocationsRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class SearchCloudLocationsRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class SearchCloudLocationsRequest : IMessage<SearchCloudLocationsRequest>, IEquatable<SearchCloudLocationsRequest>, IDeepCloneable<SearchCloudLocationsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Location Finder v1 API class SearchCloudLocationsRequest.

Message for searching cloud locations from a given source location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchCloudLocationsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Constructors 

### SearchCloudLocationsRequest()
    
    
    public SearchCloudLocationsRequest()

### SearchCloudLocationsRequest(SearchCloudLocationsRequest)
    
    
    public SearchCloudLocationsRequest(SearchCloudLocationsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of cloud locations to return. The service might return fewer cloud locations than this value. If unspecified, server will pick an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A token identifying a page of results the server should return. Provide Page token returned by a previous 'ListCloudLocations' call to retrieve the next page of results. When paginating, all other parameters provided to 'ListCloudLocations' must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest#Google_Cloud_LocationFinder_V1_SearchCloudLocationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### Query
    
    
    public string Query { get; set; }

Optional. The query string in search query syntax. While filter is used to filter the search results by attributes, query is used to specify the search requirements.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceCloudLocation
    
    
    public string SourceCloudLocation { get; set; }

Required. The source cloud location to search from. Example search can be searching nearby cloud locations from the source cloud location by latency.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceCloudLocationAsCloudLocationName
    
    
    public CloudLocationName SourceCloudLocationAsCloudLocationName { get; set; }

[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)-typed view over the [SourceCloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest#Google_Cloud_LocationFinder_V1_SearchCloudLocationsRequest_SourceCloudLocation) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
