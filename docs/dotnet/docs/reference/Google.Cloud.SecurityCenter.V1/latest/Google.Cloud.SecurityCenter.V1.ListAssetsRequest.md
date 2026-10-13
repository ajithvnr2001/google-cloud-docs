---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest
title: Google Cloud Security Command Center v1 API - Class ListAssetsRequest (3.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:03.444200+00:00
---

# Google Cloud Security Command Center v1 API - Class ListAssetsRequest (3.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1 API - Class ListAssetsRequest (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ListAssetsRequest : IPageRequest, IMessage<ListAssetsRequest>, IEquatable<ListAssetsRequest>, IDeepCloneable<ListAssetsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1 API class ListAssetsRequest.

Request message for listing assets.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListAssetsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1)

## Assembly

Google.Cloud.SecurityCenter.V1.dll

## Constructors 

### ListAssetsRequest()
    
    
    public ListAssetsRequest()

### ListAssetsRequest(ListAssetsRequest)
    
    
    public ListAssetsRequest(ListAssetsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest)`  
  
  
## Properties 

### CompareDuration
    
    
    public Duration CompareDuration { get; set; }

When compare_duration is set, the ListAssetsResult's "state_change" attribute is updated to indicate whether the asset was added, removed, or remained present during the compare_duration period of time that precedes the read_time. This is the time between (read_time - compare_duration) and read_time.

The state_change value is derived based on the presence of the asset at the two points in time. Intermediate state changes between the two times don't affect the result. For example, the results aren't affected if the asset is removed and re-created again.

Possible "state_change" values when compare_duration is specified:

  * "ADDED": indicates that the asset was not present at the start of compare_duration, but present at read_time.
  * "REMOVED": indicates that the asset was present at the start of compare_duration, but not present at read_time.
  * "ACTIVE": indicates that the asset was present at both the start and the end of the time period defined by compare_duration and read_time.



If compare_duration is not specified, then the only possible state_change is "UNUSED", which will be the state_change set for all assets present at read_time.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### FieldMask
    
    
    public FieldMask FieldMask { get; set; }

A field mask to specify the ListAssetsResult fields to be listed in the response. An empty field mask will list all fields.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### Filter
    
    
    public string Filter { get; set; }

Expression that defines the filter to apply across assets. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.

Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the Asset resource. Examples include:

  * name
  * security_center_properties.resource_name
  * resource_properties.a_property
  * security_marks.marks.marka



The supported operators are:

  * `=` for all value types.
  * `>`, `<`, `>=`, `<=` for integer values.
  * `:`, meaning substring matching, for strings.



The supported value types are:

  * string literals in quotes.
  * integer literals without quotes.
  * boolean literals `true` and `false` without quotes.



The following are the allowed field and operator combinations:

  * name: `=`
  * update_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `update_time = "2019-06-10T16:07:18-07:00"` `update_time = 1560208038000`

  * create_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `create_time = "2019-06-10T16:07:18-07:00"` `create_time = 1560208038000`

  * iam_policy.policy_blob: `=`, `:`

  * resource_properties: `=`, `:`, `>`, `<`, `>=`, `<=`
  * security_marks.marks: `=`, `:`
  * security_center_properties.resource_name: `=`, `:`
  * security_center_properties.resource_display_name: `=`, `:`
  * security_center_properties.resource_type: `=`, `:`
  * security_center_properties.resource_parent: `=`, `:`
  * security_center_properties.resource_parent_display_name: `=`, `:`
  * security_center_properties.resource_project: `=`, `:`
  * security_center_properties.resource_project_display_name: `=`, `:`
  * security_center_properties.resource_owners: `=`, `:`



For example, `resource_properties.size = 100` is a valid filter string.

Use a partial match on the empty string to filter based on a property existing: `resource_properties.my_property : ""`

Use a negated partial match on the empty string to filter based on a property not existing: `-resource_properties.my_property : ""`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Expression that defines what fields and order to use for sorting. The string value should follow SQL syntax: comma separated list of fields. For example: "name,resource_properties.a_property". The default sorting order is ascending. To specify descending order for a field, a suffix " desc" should be appended to the field name. For example: "name desc,resource_properties.a_property". Redundant space characters in the syntax are insignificant. "name desc,resource_properties.a_property" and " name desc , resource_properties.a_property " are equivalent.

The following fields are supported: name update_time resource_properties security_marks.marks security_center_properties.resource_name security_center_properties.resource_display_name security_center_properties.resource_parent security_center_properties.resource_parent_display_name security_center_properties.resource_project security_center_properties.resource_project_display_name security_center_properties.resource_type

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

The value returned by the last `ListAssetsResponse`; indicates that this is a continuation of a prior `ListAssets` call, and that the system should return the next page of data.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the parent resource that contains the assets. The value that you can specify on parent depends on the method in which you specify parent. You can specify one of the following values: `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsFolderName
    
    
    public FolderName ParentAsFolderName { get; set; }

[FolderName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.FolderName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest#Google_Cloud_SecurityCenter_V1_ListAssetsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FolderName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.FolderName.html)` |   
  
### ParentAsOrganizationName
    
    
    public OrganizationName ParentAsOrganizationName { get; set; }

[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest#Google_Cloud_SecurityCenter_V1_ListAssetsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest#Google_Cloud_SecurityCenter_V1_ListAssetsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.ListAssetsRequest#Google_Cloud_SecurityCenter_V1_ListAssetsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
### ReadTime
    
    
    public Timestamp ReadTime { get; set; }

Time used as a reference point when filtering assets. The filter is limited to assets existing at the supplied time and their values are those at that specific time. Absence of this field will default to the API's version of NOW.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
