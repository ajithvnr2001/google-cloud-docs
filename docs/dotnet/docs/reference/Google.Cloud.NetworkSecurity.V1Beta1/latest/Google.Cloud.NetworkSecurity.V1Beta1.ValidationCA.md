---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA
title: Network Security v1beta1 API - Class ValidationCA (2.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:15.447334+00:00
---

# Network Security v1beta1 API - Class ValidationCA (2.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1beta1 API - Class ValidationCA (2.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/2.0.0-beta07/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/1.0.0-beta02/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA)


    
    
    public sealed class ValidationCA : IMessage<ValidationCA>, IEquatable<ValidationCA>, IDeepCloneable<ValidationCA>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Security v1beta1 API class ValidationCA.

Specification of ValidationCA. Defines the mechanism to obtain the Certificate Authority certificate to validate the peer certificate.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ValidationCA

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ValidationCA](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ValidationCA](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ValidationCA](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1)

## Assembly

Google.Cloud.NetworkSecurity.V1Beta1.dll

## Constructors 

### ValidationCA()
    
    
    public ValidationCA()

### ValidationCA(ValidationCA)
    
    
    public ValidationCA(ValidationCA other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ValidationCA](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA)`  
  
  
## Properties 

### CertificateProviderInstance
    
    
    public CertificateProviderInstance CertificateProviderInstance { get; set; }

The certificate provider instance specification that will be passed to the data plane, which will be used to load necessary credential information.

**Property Value**  
---  
**Type** | **Description**  
`[CertificateProviderInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CertificateProviderInstance)` |   
  
### GrpcEndpoint
    
    
    public GrpcEndpoint GrpcEndpoint { get; set; }

gRPC specific configuration to access the gRPC server to obtain the CA certificate.

**Property Value**  
---  
**Type** | **Description**  
`[GrpcEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.GrpcEndpoint)` |   
  
### TypeCase
    
    
    public ValidationCA.TypeOneofCase TypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ValidationCA](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA)[TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ValidationCA.TypeOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
