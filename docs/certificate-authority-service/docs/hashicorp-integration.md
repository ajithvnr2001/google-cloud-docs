---
url: https://docs.cloud.google.com/certificate-authority-service/docs/hashicorp-integration/
title: Use Hashicorp Vault CA with CA Service \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:58.864679+00:00
---

# Use Hashicorp Vault CA with CA Service  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/hashicorp-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Hashicorp Vault CA with CA Service

This page contains a sample provided for demonstration purposes. Google does not officially support this sample. Carefully evaluate any solution before deploying it in your production environment. 

[Hashicorp Vault](https://www.vaultproject.io/) lets you manage and store secrets on-premises. This page provides information about how you can configure Hashicorp Vault CA to act as a proxy that forwards all certificate issuance requests to Certificate Authority Service. This configuration allows a currently deployed solution to work natively with CA Service.

The [Vault plugin for CA Service](https://github.com/googlecloudplatform/vault-plugin-secrets-gcppca) issues certificates through Hashicorp Vault by generating the private key and certificate signing request (CSR), or by receiving a user-provided CSR. The plugin doesn't perform create and delete CA operations, or manage other aspects of the certificate authority (CA) lifecycle.

At a high level, the plugin acts as a proxy to issue certificates.

**Note:** The Vault plugin doesn't retain any public or private key that is generated during certificate issuance. The certificate requester should retain the certificate and keys that the Vault plugin generates.

Using the Vault plugin has the following advantages:

  * Administrators can use a familiar workflow and the existing access-control list (ACL) permissions in the Vault.
  * The administrator can define who gets to request certificates and what specifications and limits those certificates have.



For more information about setting up and using the plugin, see the [README: Vault Plugin for CA Service](https://github.com/GoogleCloudPlatform/vault-plugin-secrets-gcppca/blob/master/README.md).

## What's next

  * [GitHub: Vault Plugin for CA Service](https://github.com/googlecloudplatform/vault-plugin-secrets-gcppca)
  * [Hashicorp Vault documentation](https://www.vaultproject.io/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
