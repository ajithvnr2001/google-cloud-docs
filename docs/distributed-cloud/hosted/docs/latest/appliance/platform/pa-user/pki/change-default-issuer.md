---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/change-default-issuer/
title: Change the default certificate issuer \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:14.157473+00:00
---

# Change the default certificate issuer  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/change-default-issuer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Change the default certificate issuer Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance provides a [public key infrastructure (PKI) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/security/pki/v1/security-pki-v1) to get web certificates. This document provides instructions to change the default certificate issuer to another issuer. For more information about PKI certificate modes, see [Web TLS certificate configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/web-tls-cert-config).

## Before you begin

Before changing the default certificate issuer, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete certificate issuers, contact your Organization IAM Admin to request the **Infra PKI Admin** (`infra-pki-admin`) role in the system namespace.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Change default certificate issuer

  1. The default issuer label looks like the following example. For each namespace, one `CertificateIssuer` must contain the label:
         
         pki.security.gdc.goog/is-default-issuer: 'true'
         

  2. View the current default issuer in the `pki-system` namespace:
         
         kubectl get certificateissuers -n pki-system -l pki.security.gdc.goog/is-default-issuer=true
         

The output looks similar to the following:
         
         NAME                    READY   REASON       ISDEFAULT
         default-tls-ca-issuer   True    CAaaSReady   true
         

  3. Edit the existing default issuer, and update the default issuer label from the issuer:
         
         kubectl label --overwrite certificateissuers CURRENT_DEFAULT_ISSUER -n pki-system pki.security.gdc.goog/is-default-issuer='false'
         

Replace CURRENT_DEFAULT_ISSUER with the name of the current default certificate issuer.

  4. To set the new `CertificateIssuer` as the default issuer, update the label:
         
         kubectl label --overwrite certificateissuers NEW_DEFAULT_ISSUER -n pki-system pki.security.gdc.goog/is-default-issuer=true
         

Replace NEW_DEFAULT_ISSUER with the name of the new default certificate issuer.




## Manually trigger certificate reissuance

After you switch the default certificate issuer, GDC air-gapped appliance won't automatically reissue certificates signed by the previous default certificate issuer unless the certificate is about to expire. To immediately reissue certificates with the new default issuer, see [Manually reissue PKI web certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/pki-cert-reissue).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
