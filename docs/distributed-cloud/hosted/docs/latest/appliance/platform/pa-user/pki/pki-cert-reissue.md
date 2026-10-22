---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/pki-cert-reissue/
title: Manually reissue PKI web certificates \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:07.677928+00:00
---

# Manually reissue PKI web certificates  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/pki-cert-reissue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manually reissue PKI web certificates Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions to manually trigger certificate reissuance for your Google Distributed Cloud (GDC) air-gapped appliance web endpoints.

## Before you begin

Before manually reissuing web certificates, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete PKI web certificates in a namespace, contact your Organization IAM Admin to request the **Web TLS Certificate Admin** (`web-tls-cert-admin`) role.

Consider the following account requirements:

  * A member of your infrastructure operator group must reissue PKI web certificates in the system namespace.
  * Members of the platform administrator group can reissue PKI web certificates in all other namespaces that they manage.



### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Reissue a certificate

You can manually reissue a certificate with an annotation update. If the default certificate issuer changes, GDC air-gapped appliance won't automatically reissue certificates signed by the previous default certificate issuer unless the certificate is about to expire.

To manually trigger the reissuance of a certificate, use the `kubectl` CLI to perform the following steps:

  1. Set the `manual-reissuance` annotation to `requested` for target `Certificate`. The following example updates the `default-wildcard-cert` certificate in the `istio-system` namespace which uses the current default certificate issuer:
         
         kubectl annotate --overwrite certificate.pki.security.gdc.goog
         default-wildcard-cert -n istio-system
         pki.security.gdc.goog/manual-reissuance='requested'
         

  2. You might see an `in-progress` annotation value as a transitioning state while the certificate is being reissued. Wait for the `manual-reissuance` annotation value to show `finished`:
         
         kubectl -n istio-system get
         certificate.pki.security.gdc.goog/default-wildcard-cert -ojson | jq -r '
         .metadata.annotations."pki.security.gdc.goog/manual-reissuance"'
         

The output looks similar to the following:
         
         finished
         

  3. Verify the certificate issuer; it must either match the issuer mentioned in the certificate specification or, if not specified, the issuer must match the current default issuer:
         
         kubectl -n istio-system get certificate.pki.security.gdc.goog/default-wildcard-cert -ojson | jq -r '
         .status.issuedBy'
         

The output looks similar to the following:
         
         {
           "name": "byo-cert-issuer",
           "namespace": "pki-system"
         }
         




### Bring-your-own certificate manual rotation

When you trigger and complete a manual bring-your-own certificate (BYO cert) rotation, you must sign the newly generated Certificate Signing Request (CSR) for a previously signed BYO cert. For more information, see [Sign the BYO certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/transition-pki-modes#sign-byo-cert).

During rotation, GDC air-gapped appliance creates a new private and public key pair. This makes the signed certificate uploaded earlier incompatible with the new CSR. If the certificate specification hasn't changed since the initial upload, the previously uploaded certificate remains in use until it expires. If the specification changes, one of the following events occur:

  * GDC air-gapped appliance uses an existing matching certificate.
  * A fallback Certificate Authority (CA) issues a new certificate.



#### BYO cert manual rotation example

In the following example, you see a previously signed BYO cert triggered for manual rotation:

  * The `byoCertStatus` shows the certificate `type` value is `Ready`,
  * The `reason` value is `Issued` with an earlier `lastTransitionTime` value than the previous value:
        
        {
         "byoCertStatus": {
           "csrStatus": {
             "conditions": [
               {
                 "lastTransitionTime": "2024-05-03T22:38:43Z",
                 "message": "",
                 "observedGeneration": 2,
                 "reason": "WaitingForSigning",
                 "status": "False",
                 "type": "Ready"
               }
             ],
             "csr": "LS0tLS1CRUdJTiBDRVJ..."
           },
           "signedCertStatus": {
             "conditions": [
               {
                 "lastTransitionTime": "2024-05-03T22:38:43Z",
                 "message": "RawSubjectPublickKeyInfo does not match with the CSR",
                 "observedGeneration": 2,
                 "reason": "Rejected",
                 "status": "False",
                 "type": "Ready"
               }
             ]
           }
         },
         ```
        




In the following example, you see output for a previously signed BYO cert triggered for manual rotation:

  * In the `signedCertStatus`, the `reason` field shows `Rejected` because the previously signed certificate no longer matches the new CSR after rotation.
  * The CSR `reason` states `WaitingForSigning`:
        
        "conditions": [
          {
            "lastTransitionTime": "2024-05-03T08:42:10Z",
            "message": "Certificate is issued",
            "observedGeneration": 2,
            "reason": "Issued",
            "status": "True",
            "type": "Ready"
          }
        ],
        "errorStatus": {
          "errors": [
            {
              "code": "PLATAUTH2002",
              "message": "Waiting for CSR signing"
            }
          ],
          "lastUpdateTime": "2024-05-03T22:38:43Z"
        },
        "issuedBy": {
          "name": "byo-cert-issuer",
          "namespace": "pki-system"
        }
        }
        




## Manage certificate signing alerts

Certificate signing alerts for initial issuance, rotation, and expiration must be addressed by your IO using the troubleshooting steps documented in these sections of the PKI runbook:

  * For subCA errorCode: `PLATAUTH2001`, see [PLATAUTH-R2001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/platauth/runbooks/platauth-r2001).

  * For BYO cert errorCode: `PLATAUTH2002`, see [PLATAUTH-R2002](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/platauth/runbooks/platauth-r2002).




## What's next

  * [Configure secret rotations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-secret-rotations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
