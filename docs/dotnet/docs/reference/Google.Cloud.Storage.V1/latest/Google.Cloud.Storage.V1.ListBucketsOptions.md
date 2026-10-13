---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListBucketsOptions
title: Google Cloud Storage v1 API - Class ListBucketsOptions (5.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:42.008152+00:00
---

# Google Cloud Storage v1 API - Class ListBucketsOptions (5.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListBucketsOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Storage v1 API - Class ListBucketsOptions (5.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.0 (latest)  4.16.0  4.15.0  4.14.0  4.13.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.7.0  3.6.0  3.5.0  3.4.0 
    
    
    public sealed class ListBucketsOptions

Reference documentation and code samples for the Google Cloud Storage v1 API class ListBucketsOptions.

Options for `ListBuckets` operations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListBucketsOptions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1)

## Assembly

Google.Cloud.Storage.V1.dll

## Properties 

### Fields
    
    
    public string Fields { get; set; }

If set, this specifies the fields to fetch in the result to obtain partial responses, usually to improve performance. For example, to fetch just the name and location of each bucket, set this property to "items(name,location),nextPageToken". The "nextPageToken" field is required in order to fetch multiple pages; the library does not add this automatically. See <https://cloud.google.com/storage/docs/json_api/v1/how-tos/performance#partial> for more details on specifying fields for partial responses.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int? PageSize { get; set; }

The number of results to return per page. (This modifies the per-request page size; it does not affect the total number of results returned.)

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

If set, this token is used to indicate a continued list operation. The value should be taken from the `NextPageToken` property of either a [Page<TResource>](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Page-1.html) or a raw response from [AsRawResponses()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html#Google_Api_Gax_PagedEnumerable_2_AsRawResponses).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Prefix
    
    
    public string Prefix { get; set; }

The prefix to match. Only buckets with names that start with this string will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Projection
    
    
    public Projection? Projection { get; set; }

The projection to retrieve.

**Property Value**  
---  
**Type** | **Description**  
`[Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection)` |   
  
### RetryOptions
    
    
    public RetryOptions RetryOptions { get; set; }

Options to pass custom retry configuration for each API request.

**Property Value**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.RetryOptions)` |   
  
### ReturnPartialSuccess
    
    
    public bool? ReturnPartialSuccess { get; set; }

If true, buckets from reachable locations are returned. The resource names of buckets from unreachable locations will be available on the `Unreachable` property of a raw response from [AsRawResponses()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html#Google_Api_Gax_PagedEnumerable_2_AsRawResponses). The default is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SoftDeletedOnly
    
    
    public bool? SoftDeletedOnly { get; set; }

If true, only soft-deleted buckets will be listed. The default is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
