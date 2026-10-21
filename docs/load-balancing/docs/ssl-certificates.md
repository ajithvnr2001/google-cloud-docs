---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/
title: SSL certificates overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:35.499433+00:00
---

# SSL certificates overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  SSL certificates overview Stay organized with collections  Save and categorize content based on your preferences. 

SSL/TLS is the most widely used cryptographic protocol on the internet. Technically, TLS is the successor to SSL, although the terms are sometimes used interchangeably, as they are in this document.

Transport Layer Security (TLS) is used to encrypt information while it is sent over a network, providing privacy between a client and a server or load balancer. An Application Load Balancer or proxy Network Load Balancer that uses SSL requires at least one private key and SSL certificate.

This page discusses SSL certificates and encryption in transit between an Application Load Balancer or proxy Network Load Balancer that uses SSL and its clients. For details about encryption in transit between the Google Cloud load balancer and its backends, see [Encryption to the backends](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends).

**Important:** Google Cloud strongly recommends using Certificate Manager as your primary certificate management tool for load balancer deployments. While Compute Engine SSL certificates (classic certificates) remain supported, they have notable limitations. In contrast, Certificate Manager's modern API (`certificatemanager.googleapis.com`) supports wildcards, seamless scaling, and dynamic, non-disruptive updates.

## Certificate configuration methods

Google Cloud offers three certificate configuration methods for Application Load Balancers using target HTTPS proxies and proxy Network Load Balancers using target SSL proxies.

  * **Target proxy references Compute Engine SSL certificates** : with this method, the load balancer's target proxy can reference up to 15 [Compute Engine SSL certificate resources](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates). Each Compute Engine SSL certificate resource contains the private key, corresponding certificate, and—optionally—CA certificates.

  * **Target proxy references a Certificate Manager certificate map** : with this method, the load balancer's target proxy references a single [certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps). The certificate map supports thousands of entries by default, and can scale to millions of entries. Each entry contains private key and certificate data.

  * **Target proxy references Certificate Manager certificates directly** : with this method, the load balancer's target proxy can reference up to 100 [Certificate Manager certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates).




### Load balancer support

The following table shows which certificate configuration methods each load balancer supports.

Load balancer | Certificate configuration method  
---|---  
Compute Engine SSL certificates | Certificate Manager (certificate map) | Certificate Manager (individual certificates)  
**Application Load Balancers (target HTTPS proxies)**  
Global external Application Load Balancer |  Self-managed  
Google-managed |  Self-managed  
Google-managed |   
Classic Application Load Balancer |  Self-managed  
Google-managed |  Self-managed  
Google-managed |   
Regional external Application Load Balancer |  Self-managed  
Google-managed |  |  Self-managed  
Google-managed  
Regional internal Application Load Balancer |  Self-managed  
Google-managed |  |  Self-managed  
Google-managed  
Cross-region internal Application Load Balancer |  |  |  Self-managed  
Google-managed  
**Proxy Network Load Balancers (target SSL proxies)**  
Global external proxy Network Load Balancer |  Self-managed  
Google-managed |  Self-managed  
Google-managed |   
Classic proxy Network Load Balancer |  Self-managed  
Google-managed |  Self-managed  
Google-managed |   
  
### Configuration method rules

Google Cloud enforces the following certificate configuration method rules:

  * **For load balancers that support both Compute Engine SSL certificates and Certificate Manager certificate maps** : the load balancer's target proxy can simultaneously reference both a certificate map and one or more Compute Engine SSL certificates.

**Caution:** When you use both Compute Engine certificates and certificate maps, all Compute Engine SSL certificates are ignored and only the certificates from the certificate map are used by the load balancer.
  * **For load balancers that support both Compute Engine SSL certificates and directly-attached Certificate Manager certificates** : the load balancer's target proxy can only be configured to reference up to 15 Compute Engine SSL certificates or up to 100 Certificate Manager certificates, not a combination of both.




## Certificate types

Google Cloud supports both self-managed and Google-managed certificates.

### Self-managed SSL certificates

Self-managed SSL certificates are certificates that you obtain, provision, and renew yourself. Self-managed certificates can be any of these [Public key certificate](https://en.wikipedia.org/wiki/Public_key_certificate#Validation_levels) types:

  * Domain Validation (DV)
  * Organization Validation (OV)
  * Extended Validation (EV) certificates



You can create self-managed SSL certificates using:

  * **Compute Engine SSL certificate resources** : for more information, see [Use self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

  * **Certificate Manager** : for more information, see [Deployment overview](https://docs.cloud.google.com/certificate-manager/docs/deploy) in the Certificate Manager documentation.




### Google-managed SSL certificates

Google-managed SSL certificates are certificates that Google Cloud obtains, manages, and renews automatically. Google-managed certificates are always Domain Validation (DV) certificates. They don't demonstrate the identity of an organization or individual associated with the certificate.

Google-managed certificates using wildcards are only supported by Certificate Manager when using DNS authorization.

You can create Google-managed SSL certificates using:

  * **Compute Engine SSL certificate resources** : only global Compute Engine `sslCertificates` resources support Google-managed SSL certificates; `regionSslCertificates` don't support them. Global Compute Engine SSL certificates support only publicly trusted Google-managed certificates. For more information, see [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).
  * **Certificate Manager** : Certificate Manager certificates (both global and regional) support both publicly trusted Google-managed certificates and privately trusted Google-managed certificates. For more information, see [Certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#certificates) in the Certificate Manager documentation.



## Supported key types

Load balancers support certificates that use private keys of different key types. The following table shows the key type support depending on whether the certificates are global or regional, and whether they are self-managed or Google managed.  SSL certificate type arrow_forward  
  
Key type arrow_downward | Compute Engine SSL certificates | Certificate Manager SSL certificates  
---|---|---  
Global | Regional | Global and regional  
Self-managed | Publicly trusted Google-managed | Self-managed | Self-managed | Publicly trusted Google-managed | Privately trusted Google-managed  
RSA-2048 |  |  |  |  |  |   
RSA-3072 |  |  |  |  |  |   
RSA-4096 |  |  |  |  |  |   
ECDSA P-256 |  |  |  |  |  |   
ECDSA P-384 |  |  |  |  |  |   
**Important:** You incur charges per TLS connection when you use RSA-3072 or RSA-4096 key types. For more information, see [All networking pricing](https://docs.cloud.google.com/vpc/network-pricing). To learn more about Certificate Manager certificates, see the [Certificate Manager documentation](https://docs.cloud.google.com/certificate-manager/docs/overview). 

### Use certificates with ECDSA keys

This section examines why we recommend ECDSA over RSA as a best practice for certificate signing keys.

#### Which key type to use

_ECDSA P-256_ is the recommended choice of key type for most TLS certificates, offering strong cryptographic security along with excellent performance for signing operations and efficient use of network bandwidth.

Some of the possible reasons to use other certificate key types are as follows:

  * If you need to support legacy clients that do not support ECDSA certificates, you can provide RSA-2048 certificates in addition to ECDSA P-256 certificates.
  * If you have specific compliance requirements that require you to use larger key sizes or particular key types, ECDSA P-384, RSA-2048, RSA-3072, and RSA-4096 keys can be used.



#### Why choose ECDSA over RSA

The primary advantage of ECDSA lies in its ability to provide an equivalent cryptographic security level with significantly smaller keys compared to RSA. This efficiency translates into tangible performance and resource benefits. A smaller key does not imply weaker security—ECDSA is based on the elliptic curve discrete logarithm problem, which provides stronger security per unit of key, and in some cases better computational efficiency compared to RSA.

For example:

  * A 256-bit ECDSA key provides a similar security level to an RSA-3072 key.
  * A 384-bit ECDSA key provides a greater security level than any widely-supported RSA key size.



Key benefits of ECDSA:

  * **Performance** : ECDSA signing operations are significantly less computationally intensive than RSA operations providing an equivalent security level. This reduces CPU load and latency, which is crucial for high-throughput or latency-sensitive systems.

  * **Efficiency** : smaller keys and signatures require less bandwidth and storage, which is especially beneficial for resource-constrained environments like mobile and IoT devices.




## Multiple SSL certificates

An Application Load Balancer or proxy Network Load Balancer can host two or more SSL certificates simultaneously when its target proxy is configured using a supported certificate configuration method. As a best practice, use Certificate Manager when multiple SSL certificates are needed.

  * **For load balancers that support Compute Engine SSL certificates** : the load balancer's target proxy can reference up to 15 Compute Engine SSL certificates. The first referenced Compute Engine SSL certificate resource is the default (primary) certificate for the target proxy.

  * **For load balancers that support a Certificate Manager certificate map** : the load balancer's target proxy references a single certificate map. The certificate map supports thousands of certificate map entries. You can [configure which certificate entry is the default (primary) certificate for the certificate map](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-primary).

  * **For load balancers that support directly referencing Certificate Manager certificates** : the load balancer's target proxy can reference up to 100 Certificate Manager certificates. The first referenced Certificate Manager SSL certificate resource is the default (primary) certificate for the target proxy.




For more information, see:

  * [Target proxies](https://docs.cloud.google.com/load-balancing/docs/quotas#target_proxies) and [SSL certificates](https://docs.cloud.google.com/load-balancing/docs/quotas#ssl_certificates) in the load balancing documentation.

  * [Resource quotas and limits](https://docs.cloud.google.com/certificate-manager/docs/quotas#resource_quotas_and_limits) in the Certificate Manager documentation.




### Certificate selection process

The following certificate selection process applies to load balancers whose target proxies reference multiple Compute Engine SSL certificates or multiple Certificate Manager certificates.

The certificate selection process is different if a load balancer's target proxy references a Certificate Manager certificate map. For details about the certificate selection process of a certificate map, see [Certificate selection logic](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic#selection-logic) in the Certificate Manager documentation.

**Important:** The certificate selection process doesn't consider the `notValidBefore` and `notValidAfter` attributes. The load balancer can serve an expired certificate if an expired certificate is configured. You can avoid this situation by using Google-managed certificates.

After a client connects to the load balancer, the client and load balancer negotiate a TLS session. During TLS session negotiation, the client sends the load balancer a list of TLS ciphers it supports (in the `ClientHello`). The load balancer selects a certificate whose public key algorithm is compatible with the client. The client can also send a server name indication (SNI) hostname to the load balancer as part of this negotiation. SNI hostname data is sometimes used to help the load balancer pick which certificate it should send to the client.

  * If the load balancer's target proxy references only one certificate, that certificate is used, and the value of SNI hostname sent by the client isn't relevant.

  * If the load balancer's target proxy references two or more certificates, the load balancer uses the following process to select a _single_ certificate:

    * If the client didn't send any SNI host name in its `ClientHello`, the load balancer uses the first certificate in its certificate list.

    * If the client sends an SNI hostname that didn't match any certificate common name (CN) and that doesn't match any certificate subject alternative name (SAN), load balancer uses the first certificate in its certificate list.

    * In all other situations: The load balancer selects a certificate using the following matching process:

      * Matching is done by longest suffix against both the common name (CN) and subject alternative name (SAN) certificate attributes, with a preference for ECDSA certificates over RSA certificates.

      * To illustrate the matching method, consider a target proxy that references the following two certificates:

        * Certificate A

          * CN: `cats.pets.example.com`
          * SANs: `cats.pets.example.com`, `*.pets.example.com`, `*.example.com`
        * Certificate B

          * CN: `dogs.pets.example.com`
          * SANs: `dogs.pets.example.com`, `*.pets.example.com`, `*.example.com`
      * Now consider the following scenarios:

        * If the SNI hostname sent by the client is `cats.pets.example.com`, the load balancer uses Certificate A.
        * If the SNI hostname sent by the client is `ferrets.pets.example.com`, there's no exact match, so the load balancer selects _either_ Certificate A or Certificate B because both include `*.pets.example.com` in their SANs list. You cannot control which certificate is selected in this situation.
  * After a certificate has been selected, the load balancer sends the client that certificate _only if_ the selected certificate uses a public key algorithm that is compatible with a cipher sent by the client in the `ClientHello`. TLS negotiation fails if the client doesn't support a cipher suite that includes the public key algorithm (ECDSA or RSA) of the certificate that the load balancer selected.




## Pricing

For Compute Engine SSL certificate pricing and Cloud Load Balancing pricing, see [Network pricing: Cloud Load Balancing](https://cloud.google.com/vpc/network-pricing#cloud-load-balancing).

For Certificate Manager pricing, see the [Certificate Manager pricing page](https://cloud.google.com/certificate-manager/pricing).

## What's next

  * [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview)


  * [Encryption to the backends](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends)

  * [Encryption in transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit) white paper




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
