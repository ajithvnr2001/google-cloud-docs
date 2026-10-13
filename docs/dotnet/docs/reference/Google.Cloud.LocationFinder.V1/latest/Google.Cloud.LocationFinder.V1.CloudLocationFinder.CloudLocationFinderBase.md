---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinder.CloudLocationFinderBase
title: Cloud Location Finder v1 API - Class CloudLocationFinder.CloudLocationFinderBase (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:55.391633+00:00
---

# Cloud Location Finder v1 API - Class CloudLocationFinder.CloudLocationFinderBase (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinder.CloudLocationFinderBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class CloudLocationFinder.CloudLocationFinderBase (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    [BindServiceMethod(typeof(CloudLocationFinder), "BindService")]
    public abstract class CloudLocationFinder.CloudLocationFinderBase

Reference documentation and code samples for the Cloud Location Finder v1 API class CloudLocationFinder.CloudLocationFinderBase.

Base class for server-side implementations of CloudLocationFinder

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudLocationFinder.CloudLocationFinderBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Methods 

### GetCloudLocation(GetCloudLocationRequest, ServerCallContext)
    
    
    public virtual Task<CloudLocation> GetCloudLocation(GetCloudLocationRequest request, ServerCallContext context)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | The response to send back to the client (wrapped by a task).  
  
### ListCloudLocations(ListCloudLocationsRequest, ServerCallContext)
    
    
    public virtual Task<ListCloudLocationsResponse> ListCloudLocations(ListCloudLocationsRequest request, ServerCallContext context)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### SearchCloudLocations(SearchCloudLocationsRequest, ServerCallContext)
    
    
    public virtual Task<SearchCloudLocationsResponse> SearchCloudLocations(SearchCloudLocationsRequest request, ServerCallContext context)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
