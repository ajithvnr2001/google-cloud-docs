---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest
title: Cloud Location Finder v1 API - Class ListCloudLocationsRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:55.518216+00:00
---

# Cloud Location Finder v1 API - Class ListCloudLocationsRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class ListCloudLocationsRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class ListCloudLocationsRequest : IMessage<ListCloudLocationsRequest>, IEquatable<ListCloudLocationsRequest>, IDeepCloneable<ListCloudLocationsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Location Finder v1 API class ListCloudLocationsRequest.

Message for requesting list of cloud locations..

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListCloudLocationsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Constructors 

### ListCloudLocationsRequest()
    
    
    public ListCloudLocationsRequest()

### ListCloudLocationsRequest(ListCloudLocationsRequest)
    
    
    public ListCloudLocationsRequest(ListCloudLocationsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. A filter expression that filters resources listed in the response. The expression is in the form of field=value. For example, 'cloud_location_type=CLOUD_LOCATION_TYPE_REGION'. Multiple filter queries are space-separated. For example, 'cloud_location_type=CLOUD_LOCATION_TYPE_REGION territory_code="US"' By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of cloud locations to return per page. The service might return fewer cloud locations than this value. If unspecified, server will pick an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A token identifying a page of results the server should return. Provide page token returned by a previous 'ListCloudLocations' call to retrieve the next page of results. When paginating, all other parameters provided to 'ListCloudLocations' must match the call that provided the page token.

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

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest#Google_Cloud_LocationFinder_V1_ListCloudLocationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
