---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest
title: Database Center v1beta API - Class QueryIssuesRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:00.254262+00:00
---

# Database Center v1beta API - Class QueryIssuesRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class QueryIssuesRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class QueryIssuesRequest : IPageRequest, IMessage<QueryIssuesRequest>, IEquatable<QueryIssuesRequest>, IDeepCloneable<QueryIssuesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class QueryIssuesRequest.

QueryIssuesRequest is the request to get a list of issues.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QueryIssuesRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### QueryIssuesRequest()
    
    
    public QueryIssuesRequest()

### QueryIssuesRequest(QueryIssuesRequest)
    
    
    public QueryIssuesRequest(QueryIssuesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. Supported fields are: 'product', `location`, `issue_severity`, 'tags', 'labels',

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. Following fields are sortable: SignalType Product Location IssueSeverity

The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. If unspecified, at most 50 issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `QueryIssues` call. Provide this to retrieve the subsequent page. All parameters except page size should match the parameters used in the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to.

The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SignalProductsFilters
    
    
    public RepeatedField<SignalProductsFilters> SignalProductsFilters { get; }

Optional. Filters based on signal and product. The filter list will be ORed across pairs and ANDed within a signal and products pair.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SignalProductsFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalProductsFilters)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
