---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/revoke-cert/
title: Revoke a certificate \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:01.430927+00:00
---

# Revoke a certificate  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/revoke-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Revoke a certificate Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to revoke a certificate using the Certificate Authority Service. Revoking a certificate invalidates it before its expiration date, preventing it from being used for authentication. You might revoke a certificate if the private key is compromised, the certificate is superseded by a new certificate, or the certificate is no longer needed (such as when the service the certificate was issued for is decommissioned).

This document is for audiences within the application operator group, such as application developers or data scientists, who manage certificate lifecycles within their project. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## About certificate revocation

CA Service supports certificate revocation by publishing Certificate Revocation Lists (CRLs). A CRL is a list of serial numbers of certificates that were revoked and are no longer trusted. By default, a new CRL is published every 15 minutes. Additionally, any successful certificate revocation automatically triggers the generation of a new CRL.

Certificates issued by CA Service include an extension called the CRL Distribution Point (CDP). This extension contains the URL where you can find and download the CRL for that certificate. Client applications use this URL to fetch the CRL and check if a certificate's serial number is present. If the serial number appears on the list, the certificate is considered invalid, and the connection must be rejected.

**Note:** While CA Service publishes CRLs, certificate revocation requires client applications to download the CRLs from the CDP URL and reject certificates with serial numbers appearing in the list.

## Before you begin

Before you can revoke a certificate, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To revoke certificates and view revocation requests, contact your IAM Org Admin to request the **CA Service Operation Manager** (`certificate-authority-service-operation-manager`) role in the project namespace of the certificate authority.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Revoke a certificate

The method for revoking a certificate depends on whether the issuing certificate authority (CA) has ACME mode enabled. After you revoke a certificate, its serial number appears in all future CRLs for that CA until the certificate expires.

### Revoke a certificate from an ACME-enabled CA

Each ACME-enabled CA exposes a unique ACME server URL in its status once it's ready. To revoke a certificate from an ACME-enabled CA, you must use an ACME client tool to interact with this URL using the ACME protocol.

Revoke a certificate from an ACME-enabled CA:

  1. Fetch the ACME server URL for your CA:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
           get certificateauthorities CA_NAME \
           -n USER_PROJECT_NAMESPACE \
           -ojson | jq -r '.status.acme.uri'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: The path to the kubeconfig file of the Management API server.
     * `CA_NAME`: The name of the ACME-enabled CA (root or subordinate).
     * `USER_PROJECT_NAMESPACE`: The namespace of the project.
  2. Use the obtained URL with the ACME client tool of your choice to issue a revocation request. Consult the documentation for your specific ACME client for details.




### Revoke a certificate from an ACME-disabled CA

If ACME mode is disabled on the CA, revoke a certificate by creating and applying a `RevokeCertificateRequest` custom resource:

  1. Create a `RevokeCertificateRequest` custom resource YAML file (such as `revoke-cert-request.yaml`):
         
         apiVersion: pki.security.gdc.goog/v1
         kind: RevokeCertificateRequest
         metadata:
           name: REVOKE_CERT_REQ_NAME
           namespace: USER_PROJECT_NAMESPACE
         spec:
           certificateRequestRef:
             name: CERT_REQ_NAME
             namespace: USER_PROJECT_NAMESPACE
           reason: REASON
         

Replace the following:

     * `REVOKE_CERT_REQ_NAME`: The user-defined name for the revocation request.
     * `USER_PROJECT_NAMESPACE`: The namespace of the project.
     * `CERT_REQ_NAME`: The name of the `CertificateRequest` resource associated with the certificate you want to revoke.
     * `REASON`: The reason for revocation. The following are valid reasons: `Unspecified`, `KeyCompromise`, `CaCompromise`, `AffiliationChanged`, `Superseded`, `CessationOfOperation`, `CertificateHold`, `RemoveFromCrl`, `PrivilegeWithdrawn`, and `AaCompromise`.
  2. Apply the custom resource:
         
         kubectl apply -f revoke-cert-request.yaml --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG
         

Replace MANAGEMENT_API_SERVER_KUBECONFIG with the path to the kubeconfig file of the Management API server.

  3. Verify the readiness of the revoke certificate request:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
           -n USER_PROJECT_NAMESPACE \
           get revokecertificaterequest.pki.security.gdc.goog/REVOKE_CERT_REQ_NAME \
           -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: The path to the kubeconfig file of the Management API server.
     * `USER_PROJECT_NAMESPACE`: The namespace of the project.
     * `REVOKE_CERT_REQ_NAME`: The name for the revocation request.

The output looks similar to the following:
    
    {
      "lastTransitionTime": "2025-08-19T23:20:22Z",
      "message": "RevokeCertificateRequest reconciled",
      "observedGeneration": 1,
      "reason": "Ready",
      "status": "True",
      "type": "Ready"
    }
    

The process is complete and the certificate's serial number is added to the next generated CRL.




## List revoked certificate requests

List all `RevokeCertificateRequest` resources in a project namespace:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
      -n USER_PROJECT_NAMESPACE \
      get revokecertificaterequests
    

Replace the following:

  * `MANAGEMENT_API_SERVER_KUBECONFIG`: The path to the kubeconfig file of the Management API server.
  * `USER_PROJECT_NAMESPACE`: The namespace of the project.



The output looks similar to the following:
    
    
    NAMESPACE    NAME                      READY   AGE
    foo          revoke-cert-req           True    30s
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
