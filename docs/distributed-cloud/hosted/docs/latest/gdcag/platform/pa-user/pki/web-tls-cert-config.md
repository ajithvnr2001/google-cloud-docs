---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/web-tls-cert-config/
title: Web TLS certificate configuration \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:04.279299+00:00
---

# Web TLS certificate configuration  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/web-tls-cert-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Web TLS certificate configuration Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides a [public key infrastructure (PKI) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/v1/security-pki-v1) for you to obtain a web certificate. This API supports several user modes:

  * **Fully-managed** : certificates issued by GDC PKI infrastructure and chained to a GDC-managed self-signed root certificate authority (CA).
  * **BYO cert** : you provide a pool of certificates with a default wildcard certificate. GDC will use the best matched certificate for your service.
  * **BYO cert with ACME** : certificates used by public facing services issued by your ACME server.
  * **BYO SubCA** : certificates issued by GDC PKI infrastructure and chained to your SubCA. You must provide the SubCA and let GDC operate it.



## Infra PKI mode definitions

This section provides a detailed explanation of each PKI user mode.

### Fully Managed mode (default mode)

In fully managed mode, each organization admin cluster relies on the GDC public key infrastructure (PKI) to issue certificates. When you create a new organization, this mode is the default mode applied. Afterwards, you can switch to a different PKI mode.

With this mode, you must obtain and distribute the root CA to your environment for trust.

![PKI Fully Managed mode](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pki-fully-managed-mode.png)

### BYO Certificates mode

BYO certificate mode supports signing leaf certificates with external or user-managed CAs. This mode generates a certificate signing request (CSR) for every certificate request. While waiting for signing, BYO cert mode searches for an existing customer-signed certificate among the pool that matches with the certificate request:

  * If it can't find a matching certificate, a GDC-managed fallback CA issues a temporary certificate ready for immediate use.
  * If it finds a matching certificate, it uses the matching certificate as the temporary certificate for the current request.



To sign the CSR, you must perform the following steps:

  1. Download the CSR from the `Certificate` custom resource status.
  2. Upload the signed certificate and the external CA certificate to the same `Certificate` custom resource with an update to the `spec` field.



To manage verification and replace the temporary certificate, Distributed Cloud updates the certificate secret with the uploaded certificate and the external CA. You don't have to change your trust stores.

For more information, see [Sign the BYO certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/transition-pki-modes#sign-byo-cert).

![PKI BYO Certificates mode](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pki-byo-cert-mode.png)

### BYO Certificates with ACME mode

With BYO Cert with ACME mode, a GDC-managed ACME client deploys at a Distributed Cloud site and communicates with an ACME server; a CA deployed by you at your site. The ACME server uses the ACME protocol to request, validate, and manage certificates.

The ACME protocol supports different challenges, for example, HTTP-01 and DNS-01. These challenges help prove domain ownership and obtain certificates automatically. Distributed Cloud uses the DNS-01 challenge. With this challenge, the Distributed Cloud client adds a specific DNS record to the domain's DNS zone. Once the challenge completes successfully, the ACME CA will automatically issue the certificate. You don't have to change your trust stores.

To learn more about the ACME protocol, see the Datatracker public document for RFC 8555: <https://datatracker.ietf.org/doc/html/rfc8555>.

![PKI BYO Certificates with ACME mode](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pki-acme-mode.png)

### BYO SubCA mode

With BYO SubCA mode, a CSR for the SubCA generates within the Distributed Cloud organization admin cluster. You must sign the CSR request, and upload the signed certificate into the system. For more information, see [Sign the BYO SubCA certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/transition-pki-modes#sign-byo-subca-cert). You can create a `CertificateIssuer` custom resource that points to this SubCA and mark it as the default `CertificateIssuer`.

The newly created subCA issues all of the subsequent web certificates. You don't have to change your trust stores.

![PKI BYO SubCA mode](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pki-byo-subca-mode.png)

## Transition to a different PKI mode

The PKI API supports transition from the default fully-managed mode to other supported custom modes. For more information, see [transition to different PKI modes](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/transition-pki-modes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
