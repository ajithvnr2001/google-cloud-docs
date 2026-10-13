---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.ListDatasetsOptions
title: Google BigQuery v2 API - Class ListDatasetsOptions (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:52.534781+00:00
---

# Google BigQuery v2 API - Class ListDatasetsOptions (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.ListDatasetsOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class ListDatasetsOptions (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ListDatasetsOptions

Reference documentation and code samples for the Google BigQuery v2 API class ListDatasetsOptions.

Options used when listing datasets. Details TBD.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListDatasetsOptions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Properties 

### Filter
    
    
    public string Filter { get; set; }

The filter to apply when listing datasets. See <https://cloud.google.com/bigquery/docs/labeling-datasets#filtering_datasets_using_labels> for more details. Filters for labels can be created easily using the [Filters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.Filters) class.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IncludeHidden
    
    
    public bool? IncludeHidden { get; set; }

Whether to include hidden datasets, equivalent to the "all" parameter of the REST API. By default, hidden datasets will not be included.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
