---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert/
title: Request a certificate \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:21.985239+00:00
---

# Request a certificate  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Request a certificate Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to request a certificate using the Certificate Authority Service (CAS).

To establish trust and secure communication within your Google Distributed Cloud (GDC) air-gapped, request an ACME-enabled or disabled certificate from the Certificate Authority Service.

This document is for audiences within the application operator group, such as application developers or data scientists, who manage certificate lifecycles within their project. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you can request a certificate, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, view, and delete certificate requests, contact your IAM Org Admin to grant you the **CA Service Certificate Requester** (`certificate-authority-service-certificate-requester`) role in the project namespace of the certificate authority.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Request a certificate using CA with ACME mode enabled

If the certificate authority is hosted in ACME mode, it outputs the ACME server URL in its status after it becomes ready.

Gather the CA ACME server URL from your Distributed Cloud environment:
    
    
    kubectl get certificateauthorities CA_NAME -n USER_PROJECT_NAMESPACE -ojson | jq -r '.status.acme.uri'
    

Replace the following:

  * `CA_NAME`: the name of the CA, which can be a root or sub CA
  * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides



## Request a certificate using CA with ACME mode disabled

To create a certificate request with ACME mode disabled, you must create and apply a `CertificateRequest` resource to your Distributed Cloud air-gapped instance. There are two ways to do this:

  * Create a `CertificateResource` and include a CSR in the resource.
  * Create a `CertificateResource` using a GDC auto-generated private key and provide the certificate configurations as custom values.



### Request a certificate using a CSR

  1. Create a `CertificateRequest` resource and save it as a YAML file called `cert-request.yaml`. Use your private key to create a Certificate Signing Request (CSR) and add it to your resource.

Optionally, you can issue the certificate with a pre-configured set of X.509 parameters by entering the template's name into the `certificateTemplate` field.
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateRequest
         metadata:
           name: CERT_REQ_NAME
           namespace: USER_PROJECT_NAMESPACE
         spec:
           certificateAuthorityRef:
             name: CA_NAME
             namespace: USER_PROJECT_NAMESPACE
           csr: CSR
           certificateTemplate: TEMPLATE_NAME
           signedCertificateSecret: SECRET_NAME
           notBefore: VALIDITY_START_TIME
           notAfter: VALIDITY_END_TIME
           subjectOverride: SUBJECT_OVERRIDE
         

Replace the following variables:

Variable | Description  
---|---  
CERT_REQ_NAME | the name of the `CertificateRequest` resource  
USER_PROJECT_NAMESPACE | the name of the namespace where the user project resides  
CA_NAME | the name of the CA, which can be a root or sub CA  
CSR | the Certificate Signing Request to sign using CA  
SECRET_NAME | the name of the Kubernetes Secret that holds the private key and signed CA certificate  
  
Replace the following optional variables:

Variable | Description  
---|---  
TEMPLATE_NAME | the name of the predefined certificate template you want to use. For a list of available templates and details concerning conflicts, see [Predefined certificate templates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates).  
VALIDITY_START_TIME | the time from which the certificate is considered valid. This value must be in the format `YYYY-MM-DDTHH:MM:SSZ` (for example, `2025-10-19T21:45:30Z`). If not set, the certificate is valid immediately upon issuance.  
VALIDITY_END_TIME | the time at which the certificate expires. This value must be in the format `YYYY-MM-DDTHH:MM:SSZ` (for example, `2026-01-17T18:25:40Z`). If not set, the certificate expires 90 days after its start time.  
SUBJECT_OVERRIDE | a custom subject to use in the issued certificate, overriding the subject information in the CSR. Provide this value as the raw, ASN.1 DER-encoded X.509 subject.  
  2. Apply the custom resource to your Distributed Cloud instance:
         
         kubectl apply -f cert-request.yaml --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG
         

Replace `MANAGEMENT_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of the Management API server.

  3. Verify the readiness of the certificate request:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificaterequest.pki.security.gdc.goog/CERT_REQ_NAME -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
     * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides
     * `CERT_REQ_NAME` the name of the `CertificateRequest` resource

The output is similar to the following:
    
    {
      "lastTransitionTime": "2025-01-27T12:22:59Z",
      "message": "Certificate is issued",
      "observedGeneration": 1,
      "reason": "Issued",
      "status": "True",
      "type": "Ready"
    }
    

  4. Get the certificate secret name:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificaterequest.pki.security.gdc.goog/CERT_REQ_NAME -ojson | jq -r '.spec.signedCertificateSecret'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
     * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides
     * `CERT_REQ_NAME` the name of the `CertificateRequest` resource

The output shows the `SECRET_NAME` containing the signed certificate:
    
    test-jwk-1
    




### Request a certificate using an auto-generated key

  1. Create a `CertificateRequest` resource and save it as a YAML file called `cert-request.yaml`. Populate the chosen values for the certificate.

Optionally, you can issue the certificate with a pre-configured set of X.509 parameters by entering the template's name into the `certificateTemplate` field.
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateRequest
         metadata:
           name: CERT_REQ_NAME
           namespace: USER_PROJECT_NAMESPACE
         spec:
           certificateAuthorityRef:
             name: CA_NAME
             namespace: USER_PROJECT_NAMESPACE
           certificateConfig:
             subjectConfig:
               commonName: COMMON_NAME
               organization: ORGANIZATION
               locality: LOCALITY
               state: STATE
               country: COUNTRY
               dnsNames:
               - DNS_NAMES
               ipAddresses:
               - IP_ADDRESSES
               rfc822Names:
               - RFC822NAMES
               uris:
               - URIS
           certificateTemplate: TEMPLATE_NAME
           signedCertificateSecret: SECRET_NAME
           notBefore: VALIDITY_START_TIME
           notAfter: VALIDITY_END_TIME
           subjectOverride: SUBJECT_OVERRIDE
         

Replace the following variables:

Variable | Description  
---|---  
CERT_REQ_NAME | the name of the `CertificateRequest` resource  
USER_PROJECT_NAMESPACE | the name of the namespace where the user project resides  
CA_NAME | the name of the CA, which can be a root or sub CA  
SECRET_NAME | the name of the Kubernetes Secret that holds the private key and signed CA certificate  
  
Replace the following optional variables. You must include at least one of the fields from the `spec.certificateConfig.subjectConfig` block of the `CertificateRequest` resource:

Variable | Description  
---|---  
COMMON_NAME | the common name of the certificate  
ORGANIZATION | organization to be used on the certificate  
LOCALITY | the locality of the certificate  
STATE | state or province to be used on the certificate  
COUNTRY | the country of the certificate  
DNS_NAMES | a list of `dNSName subjectAltNames` to be set on the certificate  
IP_ADDRESS | a list of `ipAddress subjectAltNames` to be set on the certificate  
RFC822_NAMES | a list of `rfc822Name subjectAltNames` to be set on the certificate  
URIS | a list of `uniformResourceIdentifier subjectAltNames` to be set on the certificate  
TEMPLATE_NAME | the name of the predefined certificate template you want to use. For a list of available templates and details concerning conflicts, see [Predefined certificate templates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates).  
VALIDITY_START_TIME | the time from which the certificate is considered valid. This value must be in the format `YYYY-MM-DDTHH:MM:SSZ` (for example, `2025-10-19T21:45:30Z`). If not set, the certificate is valid immediately upon issuance.  
VALIDITY_END_TIME | the time at which the certificate expires. This value must be in the format `YYYY-MM-DDTHH:MM:SSZ` (for example, `2026-01-17T18:25:40Z`). If not set, the certificate expires 90 days after its start time.  
SUBJECT_OVERRIDE | a custom subject to use in the issued certificate, overriding the subject information in the CSR. Provide this value as the raw, ASN.1 DER-encoded X.509 subject.  
  2. Apply the custom resource to your Distributed Cloud instance:
         
         kubectl apply -f cert-request.yaml --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG
         

Replace `MANAGEMENT_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of the Management API server.

  3. Verify the readiness of the certificate request:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificaterequest.pki.security.gdc.goog/CERT_REQ_NAME -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
     * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides
     * `CERT_REQ_NAME` the name of the `CertificateRequest` resource

The output is similar to the following:
    
    {
      "lastTransitionTime": "2025-01-27T12:22:59Z",
      "message": "Certificate is issued",
      "observedGeneration": 1,
      "reason": "Issued",
      "status": "True",
      "type": "Ready"
    }
    

  4. Get the certificate secret name:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificaterequest.pki.security.gdc.goog/CERT_REQ_NAME -ojson | jq -r '.spec.signedCertificateSecret'
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
     * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides
     * `CERT_REQ_NAME`: the name of the `CertificateRequest` resource

The output shows the `SECRET_NAME` containing the signed certificate:
    
    test-jwk-1
    




## List certificate requests

Use the `certificaterequests` parameter to list all `CertificateRequest` resources:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE get certificaterequest.pki.security.gdc.goog
    

Replace the following:

  * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
  * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides



The following shows an example command using the `agtest-project` namespace:
    
    
    kubectl --kubeconfig /root/release/root-admin/root-admin-kubeconfig  -n agtest-project get certificaterequest.pki.security.gdc.goog
    

The expected output is similar to the following:
    
    
    NAME                                               READY   AGE
    test-externalca-subca-cert-req-with-csr            True    17h
    test-externalca-subca-cert-req-with-csr-override   True    17h
    

## Delete a certificate

To delete a certificate, you must delete the corresponding `CertificateRequest` custom resource. This action removes the resource from the CAS database.

  1. Find the name of the `CertificateRequest` you want to delete. You can list certificate requests to help find the name.

  2. Delete the `CertificateRequest` resource:
         
         kubectl --kubeconfig  MANAGEMENT_API_SERVER_KUBECONFIG -n USER_PROJECT_NAMESPACE delete certificaterequest.pki.security.gdc.goog/CERT_REQ_NAME
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the Management API server
     * `USER_PROJECT_NAMESPACE`: the name of the namespace where the user project resides
     * `CERT_REQ_NAME`: the name of the `CertificateRequest` resource



## Certificate request limits and cleanup

To help maintain system stability and prevent high resource usage, CAS enforces limits on the number of `CertificateRequest` custom resources and offers an optional automated cleanup feature.

### Certificate request quota

CAS enforces a quota on the number of `CertificateRequest` custom resources per organization, with a default limit of 5,000. Exceeding this limit can degrade CAS and Management API Server performance.

As the total number of `CertificateRequest` resources approaches the quota (for example, at 80% and 90% of the limit), you will see warnings in the command output when you create new requests. If you attempt to create a `CertificateRequest` after the quota is reached, the request is denied. You might see an error message similar to the following:
    
    
    Error from server (Forbidden): error when creating "cert-request.yaml":
    admission webhook "certificaterequests.pki.security.gdc.goog" denied the
    request: the number of certificate requests has exceeded the per organization
    limit of {LIMIT}. Please refer to the guide PLATAUTH-G2102 for troubleshooting
    this issue
    

If you encounter this error, you might need to delete old or unnecessary `CertificateRequest` resources. To adjust the quota, contact a member of the infrastructure operator group within your organization. They can override the quota by following the instructions in runbook [PLATAUTH-G2102](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/gdcag-io/service-manual/platauth/guides/platauth-g2102).

### Automated cleanup

You can enable automated cleanup to delete expired `CertificateRequest` resources. This feature helps free up resources by removing them after a configurable grace period. The grace period defines the length of time between a certificate's expiration and when the `CertificateRequest` resource is deleted.

Automated cleanup is disabled by default. A member of the infrastructure operator group within your organization can enable this feature and configure the grace period by following the instructions in runbook [PLATAUTH-G2103](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/gdcag-io/service-manual/platauth/guides/platauth-g2103). The feature remains disabled if the grace period is not set or is set to zero.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
