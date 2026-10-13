---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints
title: Certificate Authority v1 API - Class CertificateIdentityConstraints (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:35.518496+00:00
---

# Certificate Authority v1 API - Class CertificateIdentityConstraints (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Certificate Authority v1 API - Class CertificateIdentityConstraints (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class CertificateIdentityConstraints : IMessage<CertificateIdentityConstraints>, IEquatable<CertificateIdentityConstraints>, IDeepCloneable<CertificateIdentityConstraints>, IBufferMessage, IMessage

Reference documentation and code samples for the Certificate Authority v1 API class CertificateIdentityConstraints.

Describes constraints on a [Certificate][google.cloud.security.privateca.v1.Certificate]'s [Subject][google.cloud.security.privateca.v1.Subject] and [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CertificateIdentityConstraints

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CertificateIdentityConstraints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CertificateIdentityConstraints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CertificateIdentityConstraints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Security.PrivateCA.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1)

## Assembly

Google.Cloud.Security.PrivateCA.V1.dll

## Constructors 

### CertificateIdentityConstraints()
    
    
    public CertificateIdentityConstraints()

### CertificateIdentityConstraints(CertificateIdentityConstraints)
    
    
    public CertificateIdentityConstraints(CertificateIdentityConstraints other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CertificateIdentityConstraints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateIdentityConstraints)`  
  
  
## Properties 

### AllowSubjectAltNamesPassthrough
    
    
    public bool AllowSubjectAltNamesPassthrough { get; set; }

Required. If this is true, the [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames] extension may be copied from a certificate request into the signed certificate. Otherwise, the requested [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames] will be discarded.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AllowSubjectPassthrough
    
    
    public bool AllowSubjectPassthrough { get; set; }

Required. If this is true, the [Subject][google.cloud.security.privateca.v1.Subject] field may be copied from a certificate request into the signed certificate. Otherwise, the requested [Subject][google.cloud.security.privateca.v1.Subject] will be discarded.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### CelExpression
    
    
    public Expr CelExpression { get; set; }

Optional. A CEL expression that may be used to validate the resolved X.509 Subject and/or Subject Alternative Name before a certificate is signed. To see the full allowed syntax and some examples, see <https://cloud.google.com/certificate-authority-service/docs/using-cel>

**Property Value**  
---  
**Type** | **Description**  
`[Expr](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Expr.html)` |   
  
### HasAllowSubjectAltNamesPassthrough
    
    
    public bool HasAllowSubjectAltNamesPassthrough { get; }

Gets whether the "allow_subject_alt_names_passthrough" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasAllowSubjectPassthrough
    
    
    public bool HasAllowSubjectPassthrough { get; }

Gets whether the "allow_subject_passthrough" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
