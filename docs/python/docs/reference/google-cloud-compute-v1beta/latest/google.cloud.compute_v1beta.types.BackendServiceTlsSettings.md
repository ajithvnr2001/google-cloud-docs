---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendServiceTlsSettings
title: Class BackendServiceTlsSettings (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:00.180082+00:00
---

# Class BackendServiceTlsSettings (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendServiceTlsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackendServiceTlsSettings (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    BackendServiceTlsSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`authentication_config` |  `str`   
Reference to the BackendAuthenticationConfig resource from the networksecurity.googleapis.com namespace. Can be used in authenticating TLS connections to the backend, as specified by the authenticationMode field. Can only be specified if authenticationMode is not NONE. This field is a member of `oneof`_ `_authentication_config`.   
`identity` |  `str`   
Assigns the Managed Identity for the BackendService Workload. Use this property to configure the load balancer back-end to use certificates and roots of trust provisioned by the Managed Workload Identity system. The `identity` property is the fully-specified SPIFFE ID to use in the SVID presented by the Load Balancer Workload. The SPIFFE ID must be a resource starting with the `trustDomain` property value, followed by the path to the Managed Workload Identity. Supported SPIFFE ID format: :: \- //  
`sni` |  `str`   
Server Name Indication - see RFC3546 section 3.1. If set, the load balancer sends this string as the SNI hostname in the TLS connection to the backend, and requires that this string match a Subject Alternative Name (SAN) in the backend's server certificate. With a Regional Internet NEG backend, if the SNI is specified here, the load balancer uses it regardless of whether the Regional Internet NEG is specified with FQDN or IP address and port. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[]. This field is a member of `oneof`_ `_sni`.   
`subject_alt_names` |  `MutableSequence[[google.cloud.compute_v1beta.types.BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendServiceTlsSettingsSubjectAltName)]`   
A list of Subject Alternative Names (SANs) that the Load Balancer verifies during a TLS handshake with the backend. When the server presents its X.509 certificate to the Load Balancer, the Load Balancer inspects the certificate's SAN field, and requires that at least one SAN match one of the subjectAltNames in the list. This field is limited to 5 entries. When both sni and subjectAltNames[] are specified, the load balancer matches the backend certificate's SAN only to subjectAltNames[].   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
