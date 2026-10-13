---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest
title: Cloud Security Compliance v1 API - Class ListFrameworkAuditsRequest (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:26.922148+00:00
---

# Cloud Security Compliance v1 API - Class ListFrameworkAuditsRequest (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Security Compliance v1 API - Class ListFrameworkAuditsRequest (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta05 (latest)  1.0.0-beta04 
    
    
    public sealed class ListFrameworkAuditsRequest : IMessage<ListFrameworkAuditsRequest>, IEquatable<ListFrameworkAuditsRequest>, IDeepCloneable<ListFrameworkAuditsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Security Compliance v1 API class ListFrameworkAuditsRequest.

The request message for [ListFrameworkAudits][].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListFrameworkAuditsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListFrameworkAuditsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListFrameworkAuditsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListFrameworkAuditsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudSecurityCompliance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1)

## Assembly

Google.Cloud.CloudSecurityCompliance.V1.dll

## Constructors 

### ListFrameworkAuditsRequest()
    
    
    public ListFrameworkAuditsRequest()

### ListFrameworkAuditsRequest(ListFrameworkAuditsRequest)
    
    
    public ListFrameworkAuditsRequest(ListFrameworkAuditsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListFrameworkAuditsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. The filters to apply to the framework audits. Supported filters are `compliance_framework`, `compliance_state`, `create_time,` and `framework_audit_name`. If the filter is invalid, an invalid argument error is returned. For syntax details, see [AIP-160][<https://google.aip.dev/160>].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of framework audits to return. The service might return fewer audits than this value. If unspecified, a maximum of 10 framework audits are returned. The maximum value is 50; values above 50 are limited to 50.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. The `next_page_token` value that's returned from a previous list request, if any.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource where the framework audits are listed.

Supported formats are the following:

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest#Google_Cloud_CloudSecurityCompliance_V1_ListFrameworkAuditsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ParentAsOrganizationLocationName
    
    
    public OrganizationLocationName ParentAsOrganizationLocationName { get; set; }

[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.OrganizationLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest#Google_Cloud_CloudSecurityCompliance_V1_ListFrameworkAuditsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.OrganizationLocationName)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.ListFrameworkAuditsRequest#Google_Cloud_CloudSecurityCompliance_V1_ListFrameworkAuditsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
