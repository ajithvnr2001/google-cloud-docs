---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest
title: SaaS Runtime v1beta1 API - Class GetTenantRequest (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:58.201524+00:00
---

# SaaS Runtime v1beta1 API - Class GetTenantRequest (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  SaaS Runtime v1beta1 API - Class GetTenantRequest (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class GetTenantRequest : IMessage<GetTenantRequest>, IEquatable<GetTenantRequest>, IDeepCloneable<GetTenantRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the SaaS Runtime v1beta1 API class GetTenantRequest.

The request structure for the GetTenant method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetTenantRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1)

## Assembly

Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.dll

## Constructors 

### GetTenantRequest()
    
    
    public GetTenantRequest()

### GetTenantRequest(GetTenantRequest)
    
    
    public GetTenantRequest(GetTenantRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetTenantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The resource name of the resource within a service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TenantName
    
    
    public TenantName TenantName { get; set; }

[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.GetTenantRequest#Google_Cloud_SaasPlatform_SaasServiceMgmt_V1Beta1_GetTenantRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.TenantName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
