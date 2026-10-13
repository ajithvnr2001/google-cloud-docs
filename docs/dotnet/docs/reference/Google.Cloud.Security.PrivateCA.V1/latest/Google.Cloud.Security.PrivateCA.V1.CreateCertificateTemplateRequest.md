---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest
title: Certificate Authority v1 API - Class CreateCertificateTemplateRequest (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:09.938487+00:00
---

# Certificate Authority v1 API - Class CreateCertificateTemplateRequest (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Certificate Authority v1 API - Class CreateCertificateTemplateRequest (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class CreateCertificateTemplateRequest : IMessage<CreateCertificateTemplateRequest>, IEquatable<CreateCertificateTemplateRequest>, IDeepCloneable<CreateCertificateTemplateRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Certificate Authority v1 API class CreateCertificateTemplateRequest.

Request message for [CertificateAuthorityService.CreateCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateCertificateTemplateRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Security.PrivateCA.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1)

## Assembly

Google.Cloud.Security.PrivateCA.V1.dll

## Constructors 

### CreateCertificateTemplateRequest()
    
    
    public CreateCertificateTemplateRequest()

### CreateCertificateTemplateRequest(CreateCertificateTemplateRequest)
    
    
    public CreateCertificateTemplateRequest(CreateCertificateTemplateRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateCertificateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest)`  
  
  
## Properties 

### CertificateTemplate
    
    
    public CertificateTemplate CertificateTemplate { get; set; }

Required. A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] with initial field values.

**Property Value**  
---  
**Type** | **Description**  
`[CertificateTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateTemplate)` |   
  
### CertificateTemplateId
    
    
    public string CertificateTemplateId { get; set; }

Required. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the location associated with the [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate], in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CreateCertificateTemplateRequest#Google_Cloud_Security_PrivateCA_V1_CreateCertificateTemplateRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
