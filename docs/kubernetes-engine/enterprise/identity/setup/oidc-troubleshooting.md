---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/oidc-troubleshooting/
title: Troubleshoot OIDC provider issues in fleet member clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:02.695572+00:00
---

# Troubleshoot OIDC provider issues in fleet member clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/oidc-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshoot OIDC provider issues in fleet member clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting guidance for OIDC and AzureAD identity provider issues when accessing your fleet member clusters. This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Incorrect formatting of certificate

This issue occurs when the certificate value has formatting errors. Formatting issues can correspond to certificate values that aren't base64 encoded and values that are base64 encoded but incorrect. The issue can also arise if the certificate isn't signed by a root certificate authority or a correctly formatted trust chain isn't provided.

### Error messages

The following examples are of error messages for scenarios where the certificate format is incorrect:

  * Certificate that is not base64 encoded: `Failed creating HTTP client to fetch the Discovery URI "<Discovery-document URI>" with error: Unable to decode data field, the value should be Base64 encoded`

  * Certificate that is not formatted correctly or is base64 encoded but incorrect: `Unable to connect to 'https://example.com', encountered the following error: Problem with the SSL CA cert (path? access rights?). Details: error setting certificate verify locations: CAfile: /tmp/example.pem CApath: none (The certificate could not be read, this is most likely because it's empty or contains a formatting error. Please check your configuration.)`

  * Certificate that is not formatted correctly or is base64 encoded but incorrect: `Failed fetching the Discovery URI "<Discovery-document URI>" with error: Unable to load TLS certificates.`




### Solution

You can resolve the issues in one of the following ways:

  * The certificate value you provide in the ClientConfig should be a base64 encoded string and PEM formatted string. For more information, see [Encode CA certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates#encodecertificate).
  * If your provider doesn't use certificates signed by a root certificate authority, then you need to configure a certificate trust chain. For more information, see [Intermediate certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates#intermediatecertificates).



## Wrong certificate value

This issue occurs when the certificate has a mismatched value. In this case, the formatting of the certificates is correct, however they don't match the server. It can also indicate that there were no certificates in the configuration.

A certificate value can be considered incorrect in any of the following scenarios:

  * An incorrect certificate value is shared in the ClientConfig. A certificate value is incorrect when the `issuer` of the server certificate does not match the `subject` of the configured certificate.
  * The certificate in the ClientConfig isn't a base64 encoded string.
  * The certificate chain is not provided when intermediate certificates are used to issue the server certificate.



### Error message

The following examples are of error messages for scenarios where there's a mismatch in the certificate value:

  * Certificate chain is not complete or does not match the server: `SSL peer certificate was not OK. Details: SSL certificate problem: unable to get local issuer certificate`

  * Certificate chain is not complete (corresponds to an invalid partial chain which doesn't start at the root or isn't contiguous): `Failed fetching the Discovery URI "<Discovery-document URI>" with error: The server's TLS certificate did not match expectations.`

  * Certificate chain is valid but doesn't match the OIDC server: `AIS was expecting the server to have a different certificate`

  * Certificate chain is valid but doesn't match the OIDC server: `Failed fetching the Discovery URI "<Discovery-document URI>" with error: The server's TLS certificate did not match expectations.`




### Solution

The certificate value you provide in the ClientConfig needs to include a correctly formatted certificate chain that matches the identity provider. For more information on how to format and encode certificates, see [Encode CA certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates#encodecertificate).

## `kubectl` commands fail when using a kubeconfig file generated by the `gcloud anthos auth login` command

When you use the `gcloud anthos auth login` command with OIDC on Windows machines to generate a kubeconfig file for cluster access, `kubectl` commands might fail with the following error message: **`The command line is too long.`** This issue occurs specifically on Windows systems and does not affect Linux machines that use the same kubeconfig file. The underlying cause is related to the size of the authentication token that's generated by Azure Active Directory (Azure AD) when a user belongs to a large number of groups (approximately 70 to 200 groups, depending on the lengths of group names).

This large token causes the execution of `kubectl` commands to fail because it exceeds the maximum length of the command line that's allowed by Windows, which is _8,191_ characters.

### Error message
    
    
    $ kubectl --kubeconfig test-kubeconfig.yml get nodes
    
    **The command line is too long.
    The command line is too long.**
    E0102 11:02:29.115256 24320 memcache.go:265] couldn't get current server API group list: Get "https://10.35.0.86:443/api?timeout=32s": getting credentials: exec: executable gcloud failed with exit code 1
    **The command line is too long.**
    E0102 11:02:29.350238 24320 memcache.go:265] couldn't get current server API group list: Get "https://10.35.0.86:443/api?timeout=32s": getting credentials: exec: executable gcloud failed with exit code 1
    **The command line is too long.**
    E0102 11:02:30.062811 24320 memcache.go:265] couldn't get current server API group list: Get "https://10.35.0.86:443/api?timeout=32s": getting credentials: exec: executable gcloud failed with exit code 1
    **Unable to connect to the server: getting credentials: exec: executable gcloud failed with exit code 1**
    

### Solution

To resolve this issue, do the following:

  * **Upgrade to version 1.28 or later**

If you're running a version earlier than 1.28, we recommend that you upgrade to the supported version.

  * **Reduce the affected user's group memberships**

Reducing the number of groups the authenticating user belongs to below the problematic threshold (approximately 70 groups) can resolve the issue.

  * **Increase the affected user's group memberships**

The [Microsoft Entra ID feature has a limit](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims) for the number of groups emitted in a token. Having between 70 to 200 group memberships might cause authentication problems. However, you can resolve the identity provider issues by increasing the number of group memberships beyond this limit. Due to the behavior of this limit, Azure AD omits groups from the `id_token` when the number of memberships becomes excessively large, preventing the command line from becoming too long and so resolving the identity provider issues. Review the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims) to confirm the limit and for more details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
