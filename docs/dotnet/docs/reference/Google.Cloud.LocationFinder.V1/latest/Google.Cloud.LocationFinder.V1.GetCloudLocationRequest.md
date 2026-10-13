---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest
title: Cloud Location Finder v1 API - Class GetCloudLocationRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:55.660059+00:00
---

# Cloud Location Finder v1 API - Class GetCloudLocationRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class GetCloudLocationRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class GetCloudLocationRequest : IMessage<GetCloudLocationRequest>, IEquatable<GetCloudLocationRequest>, IDeepCloneable<GetCloudLocationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Location Finder v1 API class GetCloudLocationRequest.

Message for getting a cloud location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetCloudLocationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Constructors 

### GetCloudLocationRequest()
    
    
    public GetCloudLocationRequest()

### GetCloudLocationRequest(GetCloudLocationRequest)
    
    
    public GetCloudLocationRequest(GetCloudLocationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest)`  
  
  
## Properties 

### CloudLocationName
    
    
    public CloudLocationName CloudLocationName { get; set; }

[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest#Google_Cloud_LocationFinder_V1_GetCloudLocationRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Name of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
