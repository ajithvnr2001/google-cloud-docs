---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates/
title: Format certificates for authentication \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:55.396156+00:00
---

# Format certificates for authentication  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Format certificates for authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to format certificates for authentication from third-party identity providers. This guidance can help you avoid and troubleshoot issues with identity provider certificates when using the service. This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Overview

You can configure authentication from identity providers such as OIDC and LDAP to your clusters. While establishing a TLS connection, the cluster validates the provider's server certificate, and verifies if the `issuer` of the provider's certificate is one of the configured certificate authority (CA) certificates.

**Note:** If you're using publicly signed root certificates for your identity provider, the cluster automatically connects to these providers.

## `certificateAuthorityData` string in ClientConfig

The CA certificate that is used to verify the provider's identity is configured in the `certificateAuthorityData` field in the ClientConfig, as shown in the following examples.

**Example for LDAP**
    
    
    ...
    ldap:
      host: HOST_NAME
      certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
      connectionType: CONNECTION_TYPE
    ...

where CERTIFICATE_AUTHORITY_DATA contains a base64-encoded, PEM-formatted CA certificate for the LDAP server. Include the resulting string in `certificateAuthorityData` as a single line. This must be provided only for `ldaps` and `startTLS` connections.

**Example for OIDC**
    
    
    ...
    oidc:
      certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
    ...

where CERTIFICATE_AUTHORITY_DATA contains a base64-encoded, PEM-formatted certificate string for the identity provider. Include the resulting string in `certificateAuthorityData` as a single line.

## Base64-encoded certificate value

Defined in RFC 4864, standard base64 encoding uses the characters `A` to `Z`, `a` to `z`, `0` to `9`, `+` and `/`. Data is padded using `=`.

## Encode CA certificate

SSL certificates have formats such as DER, PEM, and PFX. PFX files are usually encrypted with a password.

When you configure an identity provider, certificates shouldn't be password protected. This is because there is no workflow available to specify the password for decryption. For this reason, make sure you convert your certificates from other formats to PEM encoded files using an `openssl` command line tool on any Linux or Unix system. If there are multiple certificates, concatenate the certificates and import these as a single PEM file.

### PEM format example

Here's an example of a PEM encoded certificate:
    
    
    -----BEGIN CERTIFICATE-----
    MIICMzCCAZygAwIBAgIJALiPnVsvq8dsMA0GCSqGSIb3DQEBBQUAMFMxCzAJBgNV
    BAYTAlVTMQwwCgYDVQQIEwNmb28xDDAKBgNVBAcTA2ZvbzEMMAoGA1UEChMDZm9v
    MQwwCgYDVQQLEwNmb28xDDAKBgNVBAMTA2ZvbzAeFw0xMzAzMTkxNTQwMTlaFw0x
    ODAzMTgxNTQwMTlaMFMxCzAJBgNVBAYTAlVTMQwwCgYDVQQIEwNmb28xDDAKBgNV
    BAcTA2ZvbzEMMAoGA1UEChMDZm9vMQwwCgYDVQQLEwNmb28xDDAKBgNVBAMTA2Zv
    bzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAzdGfxi9CNbMf1UUcvDQh7MYB
    OveIHyc0E0KIbhjK5FkCBU4CiZrbfHagaW7ZEcN0tt3EvpbOMxxc/ZQU2WN/s/wP
    xph0pSfsfFsTKM4RhTWD2v4fgk+xZiKd1p0+L4hTtpwnEw0uXRVd0ki6muwV5y/P
    +5FHUeldq+pgTcgzuK8CAwEAAaMPMA0wCwYDVR0PBAQDAgLkMA0GCSqGSIb3DQEB
    BQUAA4GBAJiDAAtY0mQQeuxWdzLRzXmjvdSuL9GoyT3BF/jSnpxz5/58dba8pWen
    v3pj4P3w5DoOso0rzkZy2jEsEitlVM2mLSbQpMM+MUVQCQoiG6W9xuCFuxSrwPIS
    pAqEAuV4DNoxQKKWmhVv+J0ptMWD25Pnpxeq5sXzghfJnslJlQND
    -----END CERTIFICATE-----

Note the following details in the example:

  * The certificate delimiters start with _BEGIN CERTIFICATE_ and end with _END CERTIFICATE_.
  * The number of hyphens used in the delimiters is fixed.
  * The certificate value uses standard base64 (RFC 4864) encoding with line breaks (after 64 characters).
  * The line breaks (_\n_) are not visible. Do not escape the new line character.



### Specify the certificate value in ClientConfig

To specify the certificate value in your ClientConfig, do the following:

  1. Determine the PEM-encoded format for the CA certificate.
  2. Base64 encode the PEM file as per RFC 4864. Ensure that the output is a long single string without any line breaks, as in the following example of a base64-encoded PEM file: 
         
         LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNNekNDQVp5Z0F3SUJBZ0lKQUxpUG5Wc3ZxOGRzTUEwR0NTcUdTSWIzRFFFQkJRVUFNRk14Q3pBSkJnTlYKQkFZVEFsVlRNUXd3Q2dZRFZRUUlFd05tYjI4eEREQUtCZ05WQkFjVEEyWnZiekVNTUFvR0ExVUVDaE1EWm05dgpNUXd3Q2dZRFZRUUxFd05tYjI4eEREQUtCZ05WQkFNVEEyWnZiekFlRncweE16QXpNVGt4TlRRd01UbGFGdzB4Ck9EQXpNVGd4TlRRd01UbGFNRk14Q3pBSkJnTlZCQVlUQWxWVE1Rd3dDZ1lEVlFRSUV3Tm1iMjh4RERBS0JnTlYKQkFjVEEyWnZiekVNTUFvR0ExVUVDaE1EWm05dk1Rd3dDZ1lEVlFRTEV3Tm1iMjh4RERBS0JnTlZCQU1UQTJadgpiekNCbnpBTkJna3Foa2lHOXcwQkFRRUZBQU9CalFBd2dZa0NnWUVBemRHZnhpOUNOYk1mMVVVY3ZEUWg3TVlCCk92ZUlIeWMwRTBLSWJoaks1RmtDQlU0Q2lacmJmSGFnYVc3WkVjTjB0dDNFdnBiT014eGMvWlFVMldOL3Mvd1AKeHBoMHBTZnNmRnNUS000UmhUV0QydjRmZ2sreFppS2QxcDArTDRoVHRwd25FdzB1WFJWZDBraTZtdXdWNXkvUAorNUZIVWVsZHErcGdUY2d6dUs4Q0F3RUFBYU1QTUEwd0N3WURWUjBQQkFRREFnTGtNQTBHQ1NxR1NJYjNEUUVCCkJRVUFBNEdCQUppREFBdFkwbVFRZXV4V2R6TFJ6WG1qdmRTdUw5R295VDNCRi9qU25weHo1LzU4ZGJhOHBXZW4KdjNwajRQM3c1RG9Pc28wcnprWnkyakVzRWl0bFZNMm1MU2JRcE1NK01VVlFDUW9pRzZXOXh1Q0Z1eFNyd1BJUwpwQXFFQXVWNEROb3hRS0tXbWhWditKMHB0TVdEMjVQbnB4ZXE1c1h6Z2hmSm5zbEpsUU5ECi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K

  3. Provide this certificate value for the `certificateAuthorityData` field in the ClientConfig.



## CA certificates for intermediate certificates

An intermediate certificate plays a "chain of trust" role between an end entity certificate and a root certificate. This certificate value should be formatted as a base64-encoded string when used in the ClientConfig. To create a single string, concatenate the complete PEM-encoded certificates into a single string and then base64 encode it.

Here's an example of a contiguous trust chain starting with the root certificate.

`ServerCert -> IntermediateCA -> DeptCA -> RootCA`

In this example, `ServerCert` is issued by `IntermediateCA`, which is issued by `DeptCA`, which in turn is issued by `RootCA`.

Partial trust chains are supported. This means you can provide chains with only some of the certificates, such as:

`IntermediateCA -> DeptCA -> RootCA`

`IntermediateCA -> DeptCA`

`ServerCert`

When only a partial chain is configured, the cluster will verify the identity of the server by trying to match the certificates in the partial chain against the identity presented by the server.

Earlier versions, such as versions before Google Distributed Cloud 1.28.200, require a contiguous trust chain starting from the root certificate to verify the server. Examples of partial chains supported by earlier versions:

`ServerCert -> IntermediateCA -> DeptCA -> RootCA`

`IntermediateCA -> DeptCA -> RootCA`

`DeptCA -> RootCA`

**Note:** The `RootCA` is always present in these chains.

If you are encountering certificate verification issues and don't know which version you're using, try adding a root certificate into your trust chain if you don't have one to see if this is the cause of the issue.

### Specify the certificate trust chain in ClientConfig

To specify the certificate trust chain in your ClientConfig, do the following:

  1. Determine the PEM-encoded format for the CA certificates you want to include in the certificate chain.
  2. Concatenate the PEM files into a single file such that the root certificate is at the end of the file. Here's what the output looks like:
         
         -----BEGIN CERTIFICATE-----
         IntermediateCA
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         DeptCA
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         RootCA certificate
         -----END CERTIFICATE-----

**Note:** The server certificate is omitted since partial chains are valid.
  3. Base64-encode the concatenated file. Ensure the file contains a single line of base64-encoded text.

  4. Provide this certificate value for the `certificateAuthorityData` field in the ClientConfig.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
