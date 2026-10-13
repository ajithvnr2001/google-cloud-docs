---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest
title: Google Cloud Data Loss Prevention v2 API - Class ListDeidentifyTemplatesRequest (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:35.568706+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class ListDeidentifyTemplatesRequest (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class ListDeidentifyTemplatesRequest (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class ListDeidentifyTemplatesRequest : IMessage<ListDeidentifyTemplatesRequest>, IEquatable<ListDeidentifyTemplatesRequest>, IDeepCloneable<ListDeidentifyTemplatesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class ListDeidentifyTemplatesRequest.

Request message for ListDeidentifyTemplates.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListDeidentifyTemplatesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### ListDeidentifyTemplatesRequest()
    
    
    public ListDeidentifyTemplatesRequest()

### ListDeidentifyTemplatesRequest(ListDeidentifyTemplatesRequest)
    
    
    public ListDeidentifyTemplatesRequest(ListDeidentifyTemplatesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest)`  
  
  
## Properties 

### LocationId
    
    
    public string LocationId { get; set; }

Deprecated. This field has no effect.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.

Example: `name asc,update_time, create_time desc`

Supported fields are:

  * `create_time`: corresponds to the time the template was created.
  * `update_time`: corresponds to the time the template was last updated.
  * `name`: corresponds to the template's name.
  * `display_name`: corresponds to the template's display name.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Page token to continue retrieval. Comes from the previous call to `ListDeidentifyTemplates`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent resource name.

The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`



The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest#Google_Cloud_Dlp_V2_ListDeidentifyTemplatesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ParentAsOrganizationLocationName
    
    
    public OrganizationLocationName ParentAsOrganizationLocationName { get; set; }

[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OrganizationLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest#Google_Cloud_Dlp_V2_ListDeidentifyTemplatesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OrganizationLocationName)` |   
  
### ParentAsOrganizationName
    
    
    public OrganizationName ParentAsOrganizationName { get; set; }

[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest#Google_Cloud_Dlp_V2_ListDeidentifyTemplatesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest#Google_Cloud_Dlp_V2_ListDeidentifyTemplatesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest#Google_Cloud_Dlp_V2_ListDeidentifyTemplatesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
