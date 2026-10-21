---
url: https://docs.cloud.google.com/certificate-manager/docs/overview/
title: Certificate Manager overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:45:49.548226+00:00
---

# Certificate Manager overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Certificate Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Certificate Manager simplifies the acquisition, deployment, and management of Transport Layer Security (TLS) certificates. Certificate Manager supports deployment of global and regional certificates on Google Cloud load balancers, regional certificates on [ Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) proxies, and global certificates on [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview).

## Supported load balancers

Google Cloud load balancers that refer to a target HTTPS proxy or a target SSL proxy (`TargetSslProxy`) use TLS certificates to encrypt information sent over the network.

To use Certificate Manager, your load balancer must be compatible with the corresponding [Network Service Tier](https://docs.cloud.google.com/network-tiers/docs/overview). For a comprehensive breakdown of load balancer types and their respective network service tier support, see [Summary of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#summary-gclb).

The following table shows which certificate configuration methods each load balancer supports.

Load balancer | Certificate configuration method  
---|---  
Certificate Manager (certificate map) | Certificate Manager (individual certificates)  
**Application Load Balancers (target HTTPS proxies)**  
Global external Application Load Balancer |  Self-managed  
Google-managed  |   
Classic Application Load Balancer |  Self-managed  
Google-managed  |   
Regional external Application Load Balancer |  |  Self-managed  
Google-managed   
Regional internal Application Load Balancer |  |  Self-managed  
Google-managed   
Cross-region internal Application Load Balancer |  |  Self-managed  
Google-managed   
**Proxy Network Load Balancers (target SSL proxies)**  
Global external proxy Network Load Balancer |  Self-managed  
Google-managed  |   
Classic proxy Network Load Balancer |  Self-managed  
Google-managed  |   
  
For more information about the differences between target HTTPS and target SSL proxy types, see [Target proxies](https://docs.cloud.google.com/load-balancing/docs/target-proxies).

## Supported TLS certificates

Certificate Manager supports the following types of TLS certificates:

  * **Google-managed certificates** : certificates that Google Cloud obtains and manages for you. Using Certificate Manager, you can automatically issue and renew Google-managed certificates. If you want to use your own trust chain rather than rely on public certificate authorities (CAs) to issue your certificates, you can configure Certificate Manager to [use a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool) from the Certificate Authority Service as the certificate issuer instead.

  * **Self-managed certificates** : certificates that you obtain, provision, and renew yourself. You manually upload the certificates to Certificate Manager and manage them. You can use certificates issued by third-party CAs, or CAs you trust, or your own [self-signed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).




For more information about the supported certificates, see [Certificates](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#certificates).

## Benefits

Certificate Manager offers the following benefits:

**Automation**

  * Automatically issue, renew, and manage Google-managed certificates.
  * Provision Google-managed certificates in advance to enable seamless, zero-downtime migrations to Google Cloud.



**Security**

  * Securely store and deploy millions of certificates.
  * Secure your configurations with Google-managed certificates, eliminating the need to manage certificate private keys.
  * Implement mutual TLS (mTLS) authentication on your load balancer for enhanced security. For more information, see [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls) in the Cloud Load Balancing documentation.



**Flexibility**

  * Verify ownership of domains using either DNS-based or load balancer-based authorization methods.
  * Choose between Google-managed certificates (automatically handled by Google) or self-managed certificates (obtained and managed independently).
  * Use the ACME protocol to get publicly trusted certificates for endpoints you manage from the Public Certificate Authority. For more information, see [Public CA](https://docs.cloud.google.com/certificate-manager/docs/public-ca).
  * Manage all certificates in a unified manner using the Google Cloud console, Google Cloud CLI, or the Certificate Manager API.
  * Control certificate assignment and selection based on domain names. This lets you manage and serve a larger number of certificates than with [Compute Engine SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#config-tech).
  * Control the assignment and selection of certificates based on hostnames at a granular level.



## Limitations

Certificate Manager has the following limitations:

  * Certificate Manager only supports the Public Certificate Authority and the Let's Encrypt CA for issuing publicly trusted Google-managed certificates.
  * Certificate Manager only supports Certificate Authority Service for issuing privately trusted Google-managed certificates.
  * The number of domains allowed in the Subject Alternative Names (SANs) field for Google-managed certificates is limited to a maximum of 100 when using DNS authorization and to a maximum of five when using load balancer authorization.
  * Google-managed certificates have limitations on the length of supported domain names. For more information, see [Domain name length limitations for Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/quotas#domain_name_length_limitations_for_google-managed_certificates).
  * Certificates with the `ALL_REGIONS` scope don't support load balancer authorization.
  * When using either a global external Application Load Balancer or an SSL-based global external proxy Network Load Balancer, you might experience higher TLS handshake latencies in some locations with Certificate Manager compared with using Compute Engine SSL certificates.



## Certificate Manager (2nd gen)

Certificate Manager also offers a second generation product called Certificate Manager (2nd gen). For information about the features and capabilities of the next generation of this product, see [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview).

## What's next

  * [Core components of Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/core-components)
  * [How Certificate Manager works](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic)
  * [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
