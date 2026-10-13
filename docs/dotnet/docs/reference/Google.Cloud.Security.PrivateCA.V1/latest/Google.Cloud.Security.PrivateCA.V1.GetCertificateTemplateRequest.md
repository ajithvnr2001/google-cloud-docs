---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest
title: Certificate Authority v1 API - Class GetCertificateTemplateRequest (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:57.397469+00:00
---

# Certificate Authority v1 API - Class GetCertificateTemplateRequest (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Certificate Authority v1 API - Class GetCertificateTemplateRequest (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class GetCertificateTemplateRequest : IMessage<GetCertificateTemplateRequest>, IEquatable<GetCertificateTemplateRequest>, IDeepCloneable<GetCertificateTemplateRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Certificate Authority v1 API class GetCertificateTemplateRequest.

Request message for [CertificateAuthorityService.GetCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetCertificateTemplateRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Security.PrivateCA.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1)

## Assembly

Google.Cloud.Security.PrivateCA.V1.dll

## Constructors 

### GetCertificateTemplateRequest()
    
    
    public GetCertificateTemplateRequest()

### GetCertificateTemplateRequest(GetCertificateTemplateRequest)
    
    
    public GetCertificateTemplateRequest(GetCertificateTemplateRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest)`  
  
  
## Properties 

### CertificateTemplateName
    
    
    public CertificateTemplateName CertificateTemplateName { get; set; }

[CertificateTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateTemplateName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.GetCertificateTemplateRequest#Google_Cloud_Security_PrivateCA_V1_GetCertificateTemplateRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CertificateTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateTemplateName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The [name][google.cloud.security.privateca.v1.CertificateTemplate.name] of the [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] to get.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
