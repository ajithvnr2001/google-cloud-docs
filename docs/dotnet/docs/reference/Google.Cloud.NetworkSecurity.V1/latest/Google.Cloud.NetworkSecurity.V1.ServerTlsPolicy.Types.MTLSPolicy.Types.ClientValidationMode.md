---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode
title: Network Security v1 API - Enum ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:53.342688+00:00
---

# Network Security v1 API - Enum ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Enum ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public enum ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode

Reference documentation and code samples for the Network Security v1 API enum ServerTlsPolicy.Types.MTLSPolicy.Types.ClientValidationMode.

Mutual TLS certificate validation mode.

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`AllowInvalidOrMissingClientCert` | Allow connection even if certificate chain validation of the client certificate failed or no client certificate was presented. The proof of possession of the private key is always checked if client certificate was presented. This mode requires the backend to implement processing of data extracted from a client certificate to authenticate the peer, or to reject connections if the client certificate fingerprint is missing.  
`RejectInvalid` | Require a client certificate and allow connection to the backend only if validation of the client certificate passed. If set, requires a reference to non-empty TrustConfig specified in `client_validation_trust_config`.  
`Unspecified` | Not allowed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
