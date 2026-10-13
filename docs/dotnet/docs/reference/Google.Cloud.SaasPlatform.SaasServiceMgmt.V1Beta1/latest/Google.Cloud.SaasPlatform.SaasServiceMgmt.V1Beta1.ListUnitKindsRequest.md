---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest
title: SaaS Runtime v1beta1 API - Class ListUnitKindsRequest (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:45.246007+00:00
---

# SaaS Runtime v1beta1 API - Class ListUnitKindsRequest (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  SaaS Runtime v1beta1 API - Class ListUnitKindsRequest (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class ListUnitKindsRequest : IMessage<ListUnitKindsRequest>, IEquatable<ListUnitKindsRequest>, IDeepCloneable<ListUnitKindsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the SaaS Runtime v1beta1 API class ListUnitKindsRequest.

The request structure for the ListUnitKinds method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListUnitKindsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1)

## Assembly

Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.dll

## Constructors 

### ListUnitKindsRequest()
    
    
    public ListUnitKindsRequest()

### ListUnitKindsRequest(ListUnitKindsRequest)
    
    
    public ListUnitKindsRequest(ListUnitKindsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListUnitKindsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Filter the list as specified in <https://google.aip.dev/160>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Order results as specified in <https://google.aip.dev/132>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of unit kinds to send per page.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent of the unit kind.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.ListUnitKindsRequest#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_ListUnitKindsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
