---
url: https://docs.cloud.google.com/certificate-manager/docs/core-components/
title: Core components of Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:25.265573+00:00
---

# Core components of Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/core-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Core components of Certificate Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the core components and concepts of Certificate Manager.

## Certificates

A certificate represents a single X.509 Transport Layer Security (TLS) (SSL) certificate that is issued for specific domain names or domain wildcards.

Certificate Manager supports the following types of certificates:

  * **Google-managed certificates** : certificates that Google Cloud obtains and manages for you. When a new Google-managed certificate is issued or renewed, Certificate Manager uses a freshly generated private key for the certificate.
  * **Self-managed certificates** : certificates that you obtain, provision, and renew yourself.



### Google-managed certificates

Google-managed certificates are TLS certificates that Google Cloud obtains and manages for you. Certificate Manager lets you create, manage, and automatically renew your Google-managed certificates. Certificate Manager also lets you verify domain ownership by using either load balancer-based authorization or DNS-based authorization.

Certificate Manager supports Public Certificate Authority (CA) and Let's Encrypt CA. By default, the Public CA issues Google-managed certificates. If you can't obtain a certificate from the Public CA for a particular domain, Certificate Manager falls back to the Let's Encrypt CA. This might happen in situations when the Public CA refuses to issue a certificate for a domain, or your Certificate Authority Authorization (CAA) record explicitly prohibits the Public CA from issuing certificates for that domain. For more information about how to restrict the CAs that might issue certificates for your domains, see [Specify the CAs that can issue your Google-managed certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa).

Some important points to keep in mind when using Google-managed certificates with Certificate Manager:

  * Certificate Manager supports RSA Google-managed certificates.
  * Regional Google-managed certificates only support DNS-based authorization and obtain certificates from the Public CA.
  * Using Google-managed certificates as client certificates for mutual TLS isn't supported.
  * For all scopes except [`EDGE_CACHE`](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates#cert-renewal), which has a validity of 30 days, the default validity of public Google-managed certificates is either 45 days or 90 days, depending on the issuing CA:

    * Certificates issued by Public CA are gradually transitioning from a 90-day validity period to a 45-day validity period. Existing 90-day certificates remain valid for 90 days until their next renewal.
    * Certificates issued by Let's Encrypt CA have a 90-day validity period.

You can't change the default validity period of publicly trusted Google-managed certificates.




#### Public and private certificates

Certificate Manager can manage both public and private certificates. Certificate Manager gets public certificates, which often secure public services, from Public CA. Major browsers, operating systems, and applications recognize Public CA as a root of trust. Certificate Manager gets private certificates, which often secure private services, from the CA Service.

### Self-managed certificates

If you can't use Google-managed certificates because of your business requirements, then you can upload certificates that are issued by external CAs along with their associated keys. You must issue and renew these self-managed certificates manually.

The `Certificate` resource of a self-managed certificate must include the certificate and its chain. The certificate chain contains intermediate certificates, which help establish trust to the root certificate. You can add the certificate chain either as a single PEM-encoded file or as a text block.

Make sure to specify your certificate chain in the following order:

  1. Leaf certificate
  2. All intermediate certificates



## Supported key types

Load balancers support certificates that use private keys of different key types. The following table shows the key type support depending on whether the certificates are self-managed or Google managed.  SSL certificate type arrow_forward  
  
Key type arrow_downward | Certificate Manager SSL certificates  
---|---  
Global and regional  
Self-managed | Publicly trusted Google-managed | Privately trusted Google-managed  
RSA-2048 |  |  |   
RSA-3072 |  |  |   
RSA-4096 |  |  |   
ECDSA P-256 |  |  |   
ECDSA P-384 |  |  |   
**Important:** You incur charges per TLS connection when you use RSA-3072 or RSA-4096 key types. For more information, see [All networking pricing](https://docs.cloud.google.com/vpc/network-pricing).

## Domain authorizations

Certificate Manager lets you prove ownership of domains for which you want to issue Google-managed certificates in one of the following ways:

  * **Load balancer authorization** : deploy the certificate directly to a supported load balancer without creating a DNS record.

  * **DNS authorization** : deploy the certificate directly to a supported load balancer after creating dedicated DNS records for verification of domain ownership.




For more information, see [Domain authorization types for Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization).

You don't need domain authorizations for self-managed certificates.

## Certificate maps

A certificate map references one or more certificate map entries that assign specific certificates to specific hostnames. Certificate map entries also define the selection logic that the load balancer follows when establishing client connections. You can associate a certificate map with multiple target proxies for reuse across multiple load balancers.

If a client requests a hostname specified in a certificate map, the load balancer serves the certificates mapped to that hostname. Otherwise, the load balancer serves the primary certificate, which is the first certificate listed for a target proxy. For more information, see [How Certificate Manager works](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic).

The following load balancers support certificate maps:

  * Global external Application Load Balancer
  * Global external proxy Network Load Balancer



For more information about creating and managing certificate maps, see [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps).

### Certificate map entries

A certificate map entry is a list of certificates that are served for a specific domain name. You can define different sets of certificates for the same domain. For example, you can upload an ECDSA and an RSA certificate, and map them to the same domain name.

When a client connects to a domain name, the load balancer negotiates the type of certificate to serve to the client during the handshake.

You can associate a maximum of four certificates with a single certificate map entry.

For more information about creating and managing certificate map entries, see [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries).

## Trust configs

A trust config is a resource that represents your public key infrastructure (PKI) configuration in Certificate Manager. You can use trust configs in mutual TLS (mTLS) authentication and TLS inspection scenarios. A trust config encapsulates a single trust store, which in turn encapsulates one or more trust anchors and, optionally, one or more intermediate certificates.

You can use trust configs in the following mutual TLS scenarios for Application Load Balancers:

  * **Frontend mTLS** : to authenticate connections between your clients and the load balancer, where the load balancer verifies the client's identity by using the trust config. For more information, see [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls).
  * **Backend mTLS** : to authenticate connections between the load balancer and your backend workloads, such as virtual machine (VM) instances. In this scenario, the load balancer uses the trust config to validate certificates that are presented by the backend. For more information, see [Backend authenticated TLS and backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls).



You can also use trust configs for the following use case with Cloud Next Generation Firewall (Cloud NGFW):

  * **TLS inspection** : to validate privately signed backend certificates. You can add the trust config and certificate authority (CA) pool configurations to a TLS inspection policy, which you can then attach to a firewall endpoint to decrypt and inspect traffic. For more information, see [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) and [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection).



For more information about trust configs and their components, see [Manage trust configs](https://docs.cloud.google.com/certificate-manager/docs/trust-configs).

### Trust stores

A trust store represents the trust secret configuration in Certificate Manager for use in mutual TLS authentication scenarios. A trust store encapsulates a single trust anchor and, optionally, one or more intermediate certificates.

The following limitations apply to trust config resources:

  * A trust config resource can hold a single trust store.
  * A trust store can hold up to [100 intermediate CA certificates](https://docs.cloud.google.com/certificate-manager/docs/quotas#trust-config). The total size of trust anchors, intermediate certificates, and certificates in the allowlist is governed by the project's [trust config size calculation](https://docs.cloud.google.com/certificate-manager/docs/quotas#trust-config-size-calculation).



### Trust anchors

A trust anchor represents a single root certificate for use in mutual TLS authentication scenarios. A trust anchor is encapsulated within a trust store.

### Intermediate certificates

An intermediate certificate is a certificate that is signed by a root certificate or another intermediate certificate in the trust store. Intermediate certificates are used for mutual TLS authentication.

If you have any intermediate certificates, one or more intermediate certificates can be encapsulated within a trust store, depending on your PKI configuration. In addition to the existing intermediate certificates, the trust config includes all intermediate certificates as part of the trust evaluation for all connection requests.

### Certificates that require an allowlist

To allow clients to authenticate with a certificate that's self-signed, expired, or invalid, add the certificate to the `allowlistedCertificates` field of the trust config. You can also add the certificate if you don't have access to the root and intermediate certificates. You don't need a trust store to add a certificate to an allowlist.

**Note:** Certificates in an allowlist are supported for frontend mTLS and Cloud NGFW TLS inspection, but they aren't supported for backend mTLS.

When you add a certificate to the allowlist, Certificate Manager considers the certificate valid if the certificate meets the following conditions:

  * The certificate is parseable.
  * The client proves its possession of the certificate's private key.
  * The constraints on the Subject Alternative Name (SAN) field are met.



## Certificate issuance configurations

A certificate issuance configuration is a resource that lets Certificate Manager use a CA pool from your own [ Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs) instance to issue Google-managed certificates. A certificate issuance configuration lets you specify parameters for certificate issuance and expiration, as well as the key algorithm for certificates issued.

For more information about creating and managing certificate issuance configs, see [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs).

## What's next

  * [How Certificate Manager works](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
