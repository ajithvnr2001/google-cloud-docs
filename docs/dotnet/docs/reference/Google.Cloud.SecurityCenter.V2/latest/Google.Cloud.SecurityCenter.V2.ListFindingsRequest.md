---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest
title: Security Command Center v2 API - Class ListFindingsRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:32.528375+00:00
---

# Security Command Center v2 API - Class ListFindingsRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class ListFindingsRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListFindingsRequest : IPageRequest, IMessage<ListFindingsRequest>, IEquatable<ListFindingsRequest>, IDeepCloneable<ListFindingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class ListFindingsRequest.

Request message for listing findings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListFindingsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### ListFindingsRequest()
    
    
    public ListFindingsRequest()

### ListFindingsRequest(ListFindingsRequest)
    
    
    public ListFindingsRequest(ListFindingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest)`  
  
  
## Properties 

### FieldMask
    
    
    public FieldMask FieldMask { get; set; }

A field mask to specify the Finding fields to be listed in the response. An empty field mask will list all fields.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### Filter
    
    
    public string Filter { get; set; }

Expression that defines the filter to apply across findings. The expression is a list of one or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.

Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. Examples include:

  * name
  * security_marks.marks.marka



The supported operators are:

  * `=` for all value types.
  * `>`, `<`, `>=`, `<=` for integer values.
  * `:`, meaning substring matching, for strings.



The supported value types are:

  * string literals in quotes.
  * integer literals without quotes.
  * boolean literals `true` and `false` without quotes.



The following field and operator combinations are supported:

  * name: `=`
  * parent: `=`, `:`
  * resource_name: `=`, `:`
  * state: `=`, `:`
  * category: `=`, `:`
  * external_uri: `=`, `:`
  * event_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `event_time = "2019-06-10T16:07:18-07:00"` `event_time = 1560208038000`

  * severity: `=`, `:`

  * security_marks.marks: `=`, `:`
  * resource:
    * resource.name: `=`, `:`
    * resource.parent_name: `=`, `:`
    * resource.parent_display_name: `=`, `:`
    * resource.project_name: `=`, `:`
    * resource.project_display_name: `=`, `:`
    * resource.type: `=`, `:`
    * resource.folders.resource_folder: `=`, `:`
    * resource.display_name: `=`, `:`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Expression that defines what fields and order to use for sorting. The string value should follow SQL syntax: comma separated list of fields. For example: "name,parent". The default sorting order is ascending. To specify descending order for a field, a suffix " desc" should be appended to the field name. For example: "name desc,parent". Redundant space characters in the syntax are insignificant. "name desc,parent" and " name desc , parent " are equivalent.

The following fields are supported: name parent state category resource_name event_time security_marks.marks

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The value returned by the last `ListFindingsResponse`; indicates that this is a continuation of a prior `ListFindings` call, and that the system should return the next page of data.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Name of the source the findings belong to. If no location is specified, the default is global. The following list shows some examples:

  * `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`
  * `folders/[folder_id]/sources/[source_id]`
  * `folders/[folder_id]/sources/[source_id]/locations/[location_id]`
  * `projects/[project_id]/sources/[source_id]`
  * `projects/[project_id]/sources/[source_id]/locations/[location_id]`



To list across all sources provide a source_id of `-`. The following list shows some examples:

  * `organizations/{organization_id}/sources/-`
  * `organizations/{organization_id}/sources/-/locations/{location_id}`
  * `folders/{folder_id}/sources/-`
  * `folders/{folder_id}/sources/-locations/{location_id}`
  * `projects/{projects_id}/sources/-`
  * `projects/{projects_id}/sources/-/locations/{location_id}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsSourceName
    
    
    public SourceName ParentAsSourceName { get; set; }

[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ListFindingsRequest#Google_Cloud_SecurityCenter_V2_ListFindingsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
