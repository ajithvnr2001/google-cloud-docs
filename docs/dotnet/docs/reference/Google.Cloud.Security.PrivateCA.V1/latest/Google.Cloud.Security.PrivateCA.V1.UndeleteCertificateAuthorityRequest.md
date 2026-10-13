---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest
title: Certificate Authority v1 API - Class UndeleteCertificateAuthorityRequest (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:43.959670+00:00
---

# Certificate Authority v1 API - Class UndeleteCertificateAuthorityRequest (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Certificate Authority v1 API - Class UndeleteCertificateAuthorityRequest (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class UndeleteCertificateAuthorityRequest : IMessage<UndeleteCertificateAuthorityRequest>, IEquatable<UndeleteCertificateAuthorityRequest>, IDeepCloneable<UndeleteCertificateAuthorityRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Certificate Authority v1 API class UndeleteCertificateAuthorityRequest.

Request message for [CertificateAuthorityService.UndeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UndeleteCertificateAuthorityRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Security.PrivateCA.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1)

## Assembly

Google.Cloud.Security.PrivateCA.V1.dll

## Constructors 

### UndeleteCertificateAuthorityRequest()
    
    
    public UndeleteCertificateAuthorityRequest()

### UndeleteCertificateAuthorityRequest(UndeleteCertificateAuthorityRequest)
    
    
    public UndeleteCertificateAuthorityRequest(UndeleteCertificateAuthorityRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest)`  
  
  
## Properties 

### CertificateAuthorityName
    
    
    public CertificateAuthorityName CertificateAuthorityName { get; set; }

[CertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateAuthorityName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.UndeleteCertificateAuthorityRequest#Google_Cloud_Security_PrivateCA_V1_UndeleteCertificateAuthorityRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateAuthorityName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name for this [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
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
