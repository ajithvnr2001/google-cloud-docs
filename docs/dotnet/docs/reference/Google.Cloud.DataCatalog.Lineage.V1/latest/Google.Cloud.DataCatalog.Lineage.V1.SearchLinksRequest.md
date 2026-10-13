---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest
title: Data Lineage v1 API - Class SearchLinksRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:40.443431+00:00
---

# Data Lineage v1 API - Class SearchLinksRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class SearchLinksRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SearchLinksRequest : IMessage<SearchLinksRequest>, IEquatable<SearchLinksRequest>, IDeepCloneable<SearchLinksRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Data Lineage v1 API class SearchLinksRequest.

Request message for [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchLinksRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### SearchLinksRequest()
    
    
    public SearchLinksRequest()

### SearchLinksRequest(SearchLinksRequest)
    
    
    public SearchLinksRequest(SearchLinksRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest)`  
  
  
## Properties 

### CriteriaCase
    
    
    public SearchLinksRequest.CriteriaOneofCase CriteriaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest)[CriteriaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest.CriteriaOneofCase)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of links to return in a single page of the response. A page may contain fewer links than this value. If unspecified, at most 10 links are returned.

Maximum value is 100; values greater than 100 are reduced to 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. The page token received from a previous `SearchLinksRequest` call. Use it to get the next page.

When requesting subsequent pages of a response, remember that all parameters must match the values you provided in the original request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project and location you want search in.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest#Google_Cloud_DataCatalog_Lineage_V1_SearchLinksRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### Source
    
    
    public EntityReference Source { get; set; }

Optional. Send asset information in the **source** field to retrieve all links that lead from the specified asset to downstream assets.

**Property Value**  
---  
**Type** | **Description**  
`[EntityReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.EntityReference)` |   
  
### Sources
    
    
    public MultipleEntityReference Sources { get; set; }

Optional. Send a list of asset information in the **sources** field to retrieve all links that lead from the specified assets to downstream assets. This field is similar to the `source` [source][google.cloud.datacatalog.lineage.v1.SearchLinksRequest.source] field but allows providing multiple entities. All entities within the `MultipleEntityReference` must have the same `fully_qualified_name`.

**Property Value**  
---  
**Type** | **Description**  
`[MultipleEntityReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.MultipleEntityReference)` |   
  
### Target
    
    
    public EntityReference Target { get; set; }

Optional. Send asset information in the **target** field to retrieve all links that lead from upstream assets to the specified asset.

**Property Value**  
---  
**Type** | **Description**  
`[EntityReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.EntityReference)` |   
  
### Targets
    
    
    public MultipleEntityReference Targets { get; set; }

Optional. Send a list of asset information in the **targets** field to retrieve all links that lead from upstream assets to the specified assets. This field is similar to the `target` [target][google.cloud.datacatalog.lineage.v1.SearchLinksRequest.target] field but allows providing multiple entities. All entities within the `MultipleEntityReference` must have the same `fully_qualified_name`.

**Property Value**  
---  
**Type** | **Description**  
`[MultipleEntityReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.MultipleEntityReference)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
