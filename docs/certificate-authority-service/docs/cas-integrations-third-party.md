---
url: https://docs.cloud.google.com/certificate-authority-service/docs/cas-integrations-third-party/
title: Integration with third-party tools \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:51.483761+00:00
---

# Integration with third-party tools  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/cas-integrations-third-party/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with third-party tools

This page contains a sample provided for demonstration purposes. Google does not officially support this sample. Carefully evaluate any solution before deploying it in your production environment. 

This document provides an overview of the third-party tools that have an integration with Certificate Authority Service.

## Hashicorp Vault

[Hashicorp Vault](https://www.vaultproject.io/) lets you manage and store secrets on-premises. You can configure Hashicorp Vault CA to act as a proxy that forwards all certificate issuance requests to Certificate Authority Service.

The [Vault plugin for CA Service](https://github.com/googlecloudplatform/vault-plugin-secrets-gcppca) issues certificates through Hashicorp Vault by generating the private key and certificate signing request (CSR), or by receiving a user-provided CSR. The plugin doesn't perform create and delete CA operations, or manage other aspects of the certificate authority (CA) lifecycle.

At a high level, the plugin acts as a proxy to issue certificates.

**Note:** The Vault plugin doesn't retain any public or private key that is generated during certificate issuance. The certificate requester should retain the certificate and keys that the Vault plugin generates.

Using the Vault plugin has the following advantages:

  * Administrators can use a familiar workflow and the existing access-control list (ACL) permissions in the Vault.
  * The administrator can define who gets to request certificates and what specifications and limits those certificates have.



For more information about setting up and using the plugin, see the [README: Vault Plugin for CA Service](https://github.com/GoogleCloudPlatform/vault-plugin-secrets-gcppca/blob/master/README.md).

## Cert-Manager

[Jetstack Cert-Manager](https://cert-manager.io) is an open source Kubernetes add-on that automates the management and issuance of TLS certificates from various issuing sources.

Cert-Manager manages the lifecycle of certificates issued by CA pools that are created using Certificate Manager. Cert-Manager ensures certificates are valid and duly renewed before they expire.

For instructions on using Cert-Manager with Certificate Manager, see [README: Certificate Authority Service Issuer for Cert-Manager](https://github.com/jetstack/google-cas-issuer/blob/main/README.md).

**Note:** CA Service has a built-in integration with Google Cloud's Certificate Manager for global load balancers.

For more information, see [Use CA Service with Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/certificates#cert-cas).

## What's next

  * [Prepare your environment for Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/prepare-environment).
  * Get started with [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
