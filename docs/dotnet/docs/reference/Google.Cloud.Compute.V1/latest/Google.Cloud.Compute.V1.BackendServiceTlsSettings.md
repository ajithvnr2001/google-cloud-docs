---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings
title: Compute Engine v1 API - Class BackendServiceTlsSettings (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:24.478705+00:00
---

# Compute Engine v1 API - Class BackendServiceTlsSettings (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class BackendServiceTlsSettings (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BackendServiceTlsSettings : IMessage<BackendServiceTlsSettings>, IEquatable<BackendServiceTlsSettings>, IDeepCloneable<BackendServiceTlsSettings>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackendServiceTlsSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackendServiceTlsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackendServiceTlsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackendServiceTlsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### BackendServiceTlsSettings()
    
    
    public BackendServiceTlsSettings()

### BackendServiceTlsSettings(BackendServiceTlsSettings)
    
    
    public BackendServiceTlsSettings(BackendServiceTlsSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackendServiceTlsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings)`  
  
  
## Properties 

### AuthenticationConfig
    
    
    public string AuthenticationConfig { get; set; }

Reference to the BackendAuthenticationConfig resource from the networksecurity.googleapis.com namespace. Can be used in authenticating TLS connections to the backend, as specified by the authenticationMode field. Can only be specified if authenticationMode is not NONE.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAuthenticationConfig
    
    
    public bool HasAuthenticationConfig { get; }

Gets whether the "authentication_config" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIdentity
    
    
    public bool HasIdentity { get; }

Gets whether the "identity" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSni
    
    
    public bool HasSni { get; }

Gets whether the "sni" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Identity
    
    
    public string Identity { get; set; }

Assigns the Managed Identity for the BackendService Workload.

Use this property to configure the load balancer back-end to use certificates and roots of trust provisioned by the Managed Workload Identity system.

The `identity` property is the fully-specified SPIFFE ID to use in the SVID presented by the Load Balancer Workload.

The SPIFFE ID must be a resource starting with the `trustDomain` property value, followed by the path to the Managed Workload Identity.

Supported SPIFFE ID format:

  * //<trust_domain>/ns/<namespace>/sa/<subject>



The Trust Domain within the Managed Identity must refer to a valid Workload Identity Pool. The TrustConfig and CertificateIssuanceConfig will be inherited from the Workload Identity Pool.

Restrictions:

  * If you set the `identity` property, you cannot manually set the following fields:
    * tlsSettings.sni
      * tlsSettings.subjectAltNames
      * tlsSettings.authenticationConfig



When defining a `identity` for a RegionBackendServices, the corresponding Workload Identity Pool must have a ca_pool configured in the same region.

The system will set up a read-onlytlsSettings.authenticationConfig for the Managed Identity.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Sni
    
    
    public string Sni { get; set; }

Server Name Indication - see RFC3546 section 3.1. If set, the load balancer sends this string as the SNI hostname in the TLS connection to the backend, and requires that this string match a Subject Alternative Name (SAN) in the backend's server certificate. With a Regional Internet NEG backend, if the SNI is specified here, the load balancer uses it regardless of whether the Regional Internet NEG is specified with FQDN or IP address and port. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubjectAltNames
    
    
    public RepeatedField<BackendServiceTlsSettingsSubjectAltName> SubjectAltNames { get; }

A list of Subject Alternative Names (SANs) that the Load Balancer verifies during a TLS handshake with the backend. When the server presents its X.509 certificate to the Load Balancer, the Load Balancer inspects the certificate's SAN field, and requires that at least one SAN match one of the subjectAltNames in the list. This field is limited to 5 entries. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettingsSubjectAltName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
