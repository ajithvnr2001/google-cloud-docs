---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates/
title: Predefined certificate templates \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:15:44.732767+00:00
---

# Predefined certificate templates  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Predefined certificate templates Stay organized with collections  Save and categorize content based on your preferences. 

Certificate Authority Service provides predefined certificate templates to help streamline and secure the certificate issuance process. By offering pre-configured sets of X.509 parameters for common use cases, these ready-made templates simplify certificate management, reduce the risk of human error, and enforce security best practices. Each template is designed for a specific use case to make sure that certificates are issued with the correct parameters for their intended purpose, while also respecting any limitations set by the issuing certificate authority (CA).

This document is for audiences within the application operator group, such as application developers or data scientists, who manage certificate lifecycles within their project. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Apply a certificate template

To apply a template, specify the template's name in the `certificateTemplate` field of your `CertificateRequest` resource. CA Service applies the parameters from the chosen template to the issued certificate.

For detailed guidance on how to structure the `CertificateRequest` resource and include the `certificateTemplate` field, see [Request a certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert).

## Certificate template types

The following predefined certificate templates are available. Each template is designed for a specific use case and pre-configures the X.509 parameters that the template enforces.

In the template descriptions below, any parameters not explicitly set by the template are taken from the `CertificateRequest` resource, whether provided in a Certificate Signing Request (CSR) or fields you define.

### Default

Template name: `default`

This template is automatically used if you don't specify a certificate template in your `CertificateRequest` resource. The issued certificate inherits `Key usage` and `Extended key usage` settings from the issuing CA's profile, and sets `Basic constraints` to `CA:FALSE`, preventing the certificate from being used to sign other certificates.

X509 parameter | Value  
---|---  
RawSubject | [User defined SubjectOverride or Passthrough from CSR]  
Basic constraints | CA:`FALSE`  
Subject alternative name | [Passthrough from CSR]  
Key usage | [Key usage set in CA]  
Extended key usage | [Extended key usage set in CA]  
  
### Client TLS certificates

Template name: `endEntityClientAuthCertificate`

This template issues end-entity certificates for client-side TLS authentication. The issued certificate sets `Extended key usage` to `TLS web client authentication`, and `Basic constraints` to `CA:FALSE`, preventing the certificate from being used to sign other certificates.

X509 parameter | Value  
---|---  
RawSubject | [User defined SubjectOverride or Passthrough from CSR]  
Basic constraints | CA:`FALSE`  
Subject alternative name | [Passthrough from CSR]  
Key usage | Critical, digital signature, key encipherment  
Extended key usage | TLS web client authentication  
  
### Server TLS certificates

Template name: `endEntityServerAuthCertificate`

This template issues end-entity certificates for server-side TLS authentication, which is ideal for use with web servers. The issued certificate sets `Extended key usage` to `TLS web server authentication`, and `Basic constraints` to `CA:FALSE`, preventing the certificate from being used to sign other certificates.

X509 parameter | Value  
---|---  
RawSubject | [User defined SubjectOverride or Passthrough from CSR]  
Basic constraints | CA:`FALSE`  
Subject alternative name | [Passthrough from CSR]  
Key usage | Critical, digital signature, key encipherment  
Extended key usage | TLS web server authentication  
  
### Subordinate CA certificates (PathLen 0)

Template name: `blankSubCACertificate_PathLen0_CSRPassthrough`

This template issues subordinate CA certificates with a path length constraint of 0, which allows the certificate to sign end-entity certificates but not other CA certificates.

X509 parameter | Value  
---|---  
RawSubject | [User defined SubjectOverride or Passthrough from CSR]  
Basic constraints | CA:`TRUE, pathlen: 0`  
Subject alternative name | [Passthrough from CSR]  
Key usage | [Key usage set in CSR]  
Extended key usage | [Extended key usage set in CSR]  
  
### Subordinate CA certificates (PathLen 1)

Template name: `blankSubCACertificate_PathLen1_CSRPassthrough`

This template issues subordinate CA certificates with a path length constraint of 1, which allows the certificate to sign end-entity certificates as well as other subordinate CA certificates that have a path length of 0.

X509 parameter | Value  
---|---  
RawSubject | [User defined SubjectOverride or Passthrough from CSR]  
Basic constraints | CA:`TRUE, pathlen: 1`  
Subject alternative name | [Passthrough from CSR]  
Key usage | [Key usage set in CSR]  
Extended key usage | [Extended key usage set in CSR]  
  
## Conflict detection

Each CA has a profile that defines the types of certificates it's allowed to issue. For example, a CA might be restricted to only issuing client authentication certificates. The CA's profile is configured within the `certificateProfile` section of the `CertificateAuthority` resource when the CA is created, as detailed in [Create a root certificate authority](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-root-ca#create-root-ca) and [Create a subordinate certificate authority](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-subca#create-sub-ca).

When you request a certificate using a predefined template, CA Service validates the template's parameters against the issuing CA's configuration. To be valid, the X.509 parameters defined in the chosen template must be a subset of those permitted by the issuing CA according to its `certificateProfile`. A conflict occurs if the template requests attributes or permissions that the CA isn't authorized to grant. For example, a template can't request an `Extended key usage` (EKU) of `serverAuth` if the issuing CA is only authorized to grant `clientAuth`.

If CA Service detects such a conflict, the `CertificateRequest` fails. You can inspect the status of the `CertificateRequest` resource to understand the reason for the failure.

### Example

In the following scenario, a CA named `client-certs-ca` is configured to issue certificates only for client authentication. Its `certificateProfile` specifies that the only allowed `Extended key usage` is `TLS web client authentication`.

You submit the following `CertificateRequest` to issue a certificate for a server, using the `endEntityServerAuthCertificate` template:
    
    
      apiVersion: pki.security.gdc.goog/v1
      kind: CertificateRequest
      metadata:
        name: server-cert-req
        namespace: my-project
      spec:
        certificateAuthorityRef:
          name: client-certs-ca
          namespace: my-project
        csr: "..."
        certificateTemplate: endEntityServerAuthCertificate
        signedCertificateSecret: server-cert-secret
    

This request fails due to the following:

  * The `endEntityServerAuthCertificate` template requires the EKU `TLS web server authentication`.
  * The issuing CA, `client-certs-ca`, has a `certificateProfile` that only permits the EKU `TLS web client authentication`.



Since the EKU required by the template isn't included in the list of EKUs allowed by the CA's profile, the template's requirements aren't a subset of the CA's permitted parameters. The request is therefore rejected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
