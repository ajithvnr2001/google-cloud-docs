---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-root-ca/
title: Create a root certificate authority \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:49.714152+00:00
---

# Create a root certificate authority  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-root-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a root certificate authority Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to create a root certificate authority (CA) in Google Distributed Cloud (GDC) air-gapped.

A root CA, which sits atop the public key infrastructure (PKI) hierarchy, establishes the trust anchor for the PKI. To use certificates within a PKI, devices, software, and components must trust the root CA. This configuration ensures trust in all certificates issued by the root CA, thereby enabling trust in the PKI itself.

This document is for audiences within the application operator group, such as application developers or data scientists, who manage certificate lifecycles within their project. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you can create a root certificate authority, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete a root certificate authority, contact your Organization IAM Admin to request the **Certificate Authority Service Admin** (`certificate-authority-service-admin`) role.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Create a root certificate authority

To create a root CA, apply a custom resource to your Distributed Cloud air-gapped instance.

  1. Create a `CertificateAuthority` resource and save it as a YAML file called `root-ca.yaml`:
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateAuthority
         metadata:
           name: ROOT_CA_NAME
           namespace: USER_PROJECT_NAMESPACE
         spec:
           caProfile:
             commonName: COMMON_NAME
             duration: DURATION
             renewBefore: RENEW_BEFORE
             organizations:
             - ORGANIZATION
             organizationalUnits:
             - ORGANIZATIONAL_UNITS
             countries:
             - COUNTRIES
             localities:
             - LOCALTIES
             provinces:
             - PROVINCES
             streetAddresses:
             - STREET_ADDRESSES
             postalCodes:
             - POSTAL_CODES
           caCertificate:
             selfSignedCA: {}
           certificateProfile:
             keyUsage:
               - digitalSignature
               - keyCertSign
               - crlSign
             extendedKeyUsage:
               - EXTENDED_KEY_USAGE
           secretConfig:
             secretName: SECRET_NAME
             privateKeyConfig:
               algorithm: KEY_ALGORITHM
               size: KEY_SIZE
           acme:
             enabled: ACME_ENABLED
         

Replace the following variables:

Variable | Description  
---|---  
ROOT_CA_NAME | The name of the root CA.  
USER_PROJECT_NAMESPACE | The name of the namespace where the user project resides.  
COMMON_NAME | The common name of the CA certificate.  
DURATION | The requested lifetime of the CA certificate. Specify as a duration in hours (for example, `1000h`). Units such as days (`d`) or years (`y`) are not supported.  
SECRET_NAME | The name of the Kubernetes Secret that holds the private key and signed CA certificate.  
  
The following variables are optional values: 

Variable | Description  
---|---  
RENEW_BEFORE | The rotation time before the CA certificate expires.  
ORGANIZATION | Organization to be used on the certificate.  
ORGANIZATIONAL_UNITS | Organizational units to be used on the certificate.  
COUNTRIES | Countries to be used on the certificate.  
LOCALITIES | Cities to be used on the certificate.  
PROVINCES | State or Provinces to be used on the certificate.  
STREET_ADDRESSES | Street addresses to be used on the certificate.  
POSTAL_CODES | Postal codes to be used on the certificate.  
EXTENDED_KEY_USAGE | The extended key usage for the certificate. If provided, the allowed values are `serverAuth` and `clientAuth`.  
KEY_ALGORITHYM | The private key algorithm used for this certificate. Allowed values are `RSA`, `Ed25519`, or `ECDSA`. If the size is not provided, it defaults to 256 for `ECDSA` and 2048 for `RSA`. Key size is ignored for `Ed25519`.  
KEY_SIZE | The size, in bits, of the private key for this certificate depends on the algorithm. `RSA` allows 2048, 3072, 4096, or 8192 (default 2048). `ECDSA` allows 256, 384, or 521 (default 256). `Ed25519` ignores size.  
ACME_ENABLED | If set to `true`, CA runs in ACME mode and outputs the ACME server URL. You can then use the ACME client and protocol to manage certificates.  
  2. Apply the custom resource to your Distributed Cloud instance:
         
         kubectl apply -f root-ca.yaml –kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG
         

Replace `MANAGEMENT_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of the Management API server.

  3. Verify the readiness of the root CA. It normally takes around 40 minutes for the CA to become ready:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificateauthority.pki.security.gdc.goog/ROOT_CA_NAME -ojson | jq -r ' 
         .status.conditions[] | select( .type as $id | "Ready" | index($id))
         

The output looks similar to the following:
         
         {
           "lastTransitionTime": "2025-01-24T17:09:19Z",
           "message": "CA reconciled",
           "observedGeneration": 2,
           "reason": "Ready",
           "status": "True",
           "type": "Ready"
         }
         




## List CAs

To list all of the Certificate Authority Service resources in your Distributed Cloud air-gapped instance, do the following:

Use the `certificateauthorities` parameter to list all `CertificateAuthority` resources:
    
    
       kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificateauthorities
    

The output looks similar to the following:
    
    
       NAMESPACE    NAME              READY   REASON   AGE
       foo          root-ca           True    Ready    7h24m
       foo          sub-ca            True    Ready    7h24m
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
