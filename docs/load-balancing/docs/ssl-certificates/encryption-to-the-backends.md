---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends/
title: Encryption from the load balancer to the backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:30.463042+00:00
---

# Encryption from the load balancer to the backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Encryption from the load balancer to the backends Stay organized with collections  Save and categorize content based on your preferences. 

## Encryption in all Google Cloud regions

All VM-to-VM traffic within a VPC network and peered VPC networks is encrypted.

## Encryption between proxy load balancers and backends

For some proxy load balancers (see table 1), Google automatically encrypts traffic to the backends that reside within Google Cloud VPC networks. This is called _automatic network-level encryption_. Automatic network-level encryption is only applicable to communications with these types of backends:

  * Instance groups
  * Zonal NEGs (`GCE_VM_IP_PORT` endpoints)



In addition, Google Cloud provides [secure protocol options to encrypt communication with the backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#protocol_to_the_backends).

Some Google Cloud load balancers use [Google Front Ends (GFEs)](https://cloud.google.com/security/infrastructure/design#google_front_end_service) as the client to the backends whereas others use the open source [Envoy proxy](https://www.envoyproxy.io/). In all cases, the load balancer supports the cipher suites listed in [RFC 8446, section 9.1](https://datatracker.ietf.org/doc/html/rfc8446#section-9.1) for TLS 1.3. For TLS 1.2 and earlier, the load balancer supports the cipher suites associated with the COMPATIBLE [SSL policy profile](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy).

The following table provides a summary of the proxy load balancers that encrypt traffic to the backends.

**Table 1.** Communications between load balancers and backends Proxy load balancer | Proxy (client to the backend) | Automatic network-level encryption | Backend service protocol options  
---|---|---|---  
Global external Application Load Balancer | GFE (with Envoy software for advanced routing features) |  | HTTP, HTTPS, and HTTP/2   
Choose HTTPS or HTTP/2 if you require auditable encryption in transit to the backends.  
Classic Application Load Balancer | GFE |  | HTTP, HTTPS, and HTTP/2   
Choose HTTPS or HTTP/2 if you require auditable encryption in transit to the backends.  
Regional external Application Load Balancer | Envoy proxy |  | HTTP, HTTPS, and HTTP/2   
Choose HTTPS or HTTP/2 if you require auditable encryption in transit to the backends.  
Regional internal Application Load Balancer | Envoy proxy |  | HTTP, HTTPS, and HTTP/2   
Choose HTTPS or HTTP/2 if you require auditable encryption in transit to the backends.  
Cross-region internal Application Load Balancer | Envoy proxy |  | HTTP, HTTPS, and HTTP/2   
Choose HTTPS or HTTP/2 if you require auditable encryption in transit to the backends.  
Global external proxy Network Load Balancer | GFE (with Envoy software for advanced routing features) |  | SSL or TCP   
Choose SSL for the backend service protocol if you require auditable encryption in transit to the backends.  
Classic proxy Network Load Balancer | GFE |  | SSL or TCP   
Choose SSL for the backend service protocol if you require auditable encryption in transit to the backends.  
Regional external proxy Network Load Balancer | Envoy proxy |  | TCP  
Regional internal proxy Network Load Balancer | Envoy proxy |  | TCP  
Cross-region internal proxy Network Load Balancer | Envoy proxy |  | TCP  
Cloud Service Mesh | Client-side proxy |  | HTTPS and HTTP/2  
  
### Secure backend protocol use cases

A secure protocol to connect to backend instances is recommended in the following cases:

  * When you require an auditable, encrypted connection from the load balancer (or Cloud Service Mesh) to the backend instances.

  * When the load balancer connects to a backend instance that is outside of Google Cloud (with an [internet NEG](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts)). Communication to an internet NEG backend might transit the public internet. When the load balancer connects to an internet NEG, the public CA-signed certificate must [meet the validation requirements](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#ssl_server_certification_validation_and_san_validation).




### Secure backend protocol considerations

When using a secure backend service protocol, keep the following in mind:

  * Your load balancer's backend instances or endpoints must serve using the same protocol as the backend service. For example, if the backend service protocol is HTTPS, the backends must be HTTPS servers.

  * If the backend service protocol is `HTTP2`, your backends must use TLS. For configuration instructions, see the documentation for the software running on your backend instances or endpoints.

**Note:** To use HTTP/2 without TLS, use the `H2C` backend service protocol instead. For more information, see [HTTP/2 over cleartext TCP](https://docs.cloud.google.com/load-balancing/docs/https#http2-over-tcp-h2c).
  * You must install private keys and certificates on your backend instances or endpoints in order for them to function as HTTPS or SSL servers. These certificates don't need to match the load balancer's frontend SSL certificates. For installation instructions, see the documentation for the software running on your backend instances or endpoints.

  * With the exception of HTTPS load balancers with [internet NEG backends](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts), load balancers don't use the Server Name Indication (SNI) extension for connections to the backend.

  * When a load balancer connects to backends that are within Google Cloud, the load balancer accepts any certificate your backends present. In this case, the load balancer performs only minimum certificate validation.

For example, certificates are treated as valid even in the following circumstances:

    * The certificate is self-signed.
    * The certificate is signed by an unknown certificate authority (CA).
    * The certificate has expired or is not yet valid.
    * The `CN` and `subjectAlternativeName` attributes don't match a `Host` header or DNS PTR record.

For RSA certificates, starting April 28, 2025, the load balancer will only accept RSA certificates that have the X509v3 Key Usage extension present and include both the Digital Signature and Key Encipherment parameters. For more information, see the associated [release note on January 24, 2025](https://docs.cloud.google.com/load-balancing/docs/release-notes#January_24_2025).




## Secure frontend protocols

When you use a target HTTPS or target SSL proxy as part of your configuration, Google Cloud uses a secure frontend protocol.

External Application Load Balancers and external proxy Network Load Balancers use Google's BoringCrypto library. For FIPS 140-2 details, see [NIST Cryptographic Module Validation Program Certificate #3678](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/3678).

Internal Application Load Balancers use Google's BoringSSL library. For FIPS 140-2 details, see the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/ssl). Google builds Envoy proxies for internal Application Load Balancers in FIPS compliant mode.

Cloud Service Mesh supports Envoy proxies that are built in FIPS-compliant mode. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
