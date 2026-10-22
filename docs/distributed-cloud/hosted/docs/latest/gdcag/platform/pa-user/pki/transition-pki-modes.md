---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/transition-pki-modes/
title: Transition to different PKI modes \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:32.368448+00:00
---

# Transition to different PKI modes  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/transition-pki-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Transition to different PKI modes Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides a [public key infrastructure (PKI) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/v1/security-pki-v1) to get web certificates. This document provides instructions to transition from one PKI certificate mode to another. For more information about PKI mode configuration types, see [Web TLS certificate configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/web-tls-cert-config).

This document is for audiences within the platform administrator group who want to manage certificate authorities and certificate issuers. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before transitioning PKI modes, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete certificate authorities and certificate issuers, contact your Organization IAM Admin to request the **PKI Infra Admin** (`infra-pki-admin`) role in the system namespace.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Transition to BYO subCA mode

This section provides a series of steps to transition to the bring your own (BYO) SubCA cert mode.

### Create a BYO subCA

To create a BYO subCA, apply a custom resource to your Distributed Cloud zone.

  1. Create a `CertificateAuthority` resource and save it as a YAML file. In the following example, you see a sample `CertificateAuthority` resource
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateAuthority
         metadata:
           name: CA_NAME
           namespace: pki-system
         spec:
           caProfile:
             commonName: COMMON_NAME
             duration: DURATION
             renewBefore: RENEW_BEFORE
           caCertificate:
             externalCA: {}
           certificateProfile:
             keyUsage:
             - digitalSignature
             - keyCertSign
             - crlSign
             extendedKeyUsage:
             - serverAuth
           secretConfig:
             secretName: SECRET_NAME
         

Replace the following variables:

     * CA_NAME: the name of the subCA.
     * COMMON_NAME: the common name of the CA certificate.
     * DURATION: the requested lifetime of the CA certificate. Specify as a duration in hours (for example, `1000h`). Units such as days (`d`) or years (`y`) are not supported.
     * RENEW_BEFORE: the rotation time before the CA certificate expires.
     * SECRET_NAME: the name of the Kubernetes Secret that will hold the private key and signed CA certificate.
  2. Apply the custom resource to your Distributed Cloud zone.
         
         kubectl apply -f byo-subca.yaml --kubeconfig MANAGEMENT_API_SERVER
         

Replace MANAGEMENT_API_SERVER with the Management API server kubeconfig file.




A CSR for Sub CA generates and waits for you to sign it. To sign the CSR, follow the instructions in the section Sign the BYO subCA certificate.

#### Sign the BYO subCA certificate

  1. Get the certificate signing requests (CSR) from your GDC environment:
         
         kubectl get certificateauthorities CA_NAME -n pki-system -ojson | jq -j '"echo ",
         .status.externalCA.csr, " | base64 -d > ","sub_ca.csr\n"' | bash
         

The command generates the file `sub_ca.csr` in the current directory. This file contains a CSR for an X.509 CA certificate.

  2. Use the customer's root CA's protocol to request signed CA certificates for the `sub_ca.csr` file.

  3. For an approved certificate signing request, you will obtain a CA certificate signed by the customer's root CA. Store the certificate to the `sub_ca.crt` file in the current directory. In addition, obtain the customer's root CA certificate and store it to the `ca.crt` file in the current directory. Reach out to PMO for exact instructions.

  4. Verify the following to ensure the integrity and accuracy of the certificates:

     1. Ensure that `sub_ca.crt` adheres to the standard PEM encoded certificate format:
            
            -----BEGIN CERTIFICATE-----
                  <Certificate>
            -----END CERTIFICATE-----
            

     2. Verify that `sub_ca.crt` is a valid Certificate Authority (CA) in the "Basic Constraints" extension:
            
            openssl x509 -text -noout -in sub_ca.crt | grep -A 1 "Basic Constraints"
            

The output must include `CA:TRUE` or further investigation is required:
            
            X509v3 Basic Constraints: critical
                CA:TRUE
            

     3. Verify the CA certificate's Common Name (CN):
            
            openssl x509 -noout -subject -in sub_ca.crt
            

If your setup requires Subject Alternative Name (SAN) extensions, verify the SAN extensions in the certificate:
            
            openssl x509 -text -noout -in sub_ca.crt | grep -A 1 "Subject Alternative Name"
            

  5. Generate the spec to patch the `CertificateAuthority` resource:
         
         echo "spec:
         caCertificate:
           externalCA:
             signedCertificate:
               certificate: $(base64 -w0 sub_ca.crt)
               ca: $(base64 -w0 ca.crt)" > patch.txt
         

The content in the `patch.txt` file looks similar to the following snippet:
         
         spec:
           caCertificate:
            externalCA:
             signedCertificate:
              certificate: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURSekNDQ…
              ca: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURRVENDQ…
         

  6. Edit the spec of the `CertificateAuthority` resource:
         
         kubectl patch certificateauthority CA_NAME -n pki-system --patch-file patch.txt --type='merge'
         

  7. Verify the readiness of the BYO subCA:
         
         kubectl get certificateauthority CA_NAME -n pki-system -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

You see output similar to the following:
         
         {
           "lastTransitionTime": "2024-04-30T22:10:50Z",
           "message": "Certificate authority is ready for use",
           "observedGeneration": 3,
           "reason": "Ready",
           "status": "True",
           "type": "Ready"
         }
         

  8. Verify the expiration of the signed CA certificates:
         
         kubectl -n pki-system get secret SECRET_NAME -ojson | jq -j '"echo ",
         .metadata.name, " $(echo ", .data["tls.crt"], "| base64 -d | openssl x509 -enddate -noout)\n"' | bash
         

  9. Create a `CertificateIssuer` resource YAML file and save the file. For example, `byo-subca-issuer.yaml`:
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateIssuer
         metadata:
           name: BYO_SUBCA_ISSUER
           namespace: pki-system
         spec:
           caaasConfig:
             certificateAuthorityRef:
               namespace: pki-system
               name: CA_NAME
         

Replace BYO_SUBCA_ISSUER with the name of the byo subCA issuer.

  10. Apply the custom resource to your Distributed Cloud zone in the Management API server using the `kubectl` CLI:
         
         kubectl apply -f byo-subca-issuer.yaml --kubeconfig MANAGEMENT_API_SERVER
         

  11. Verify the readiness of the new issuer:
         
         kubectl -n pki-system get certificateissuer.pki.security.gdc.goog/BYO_SUBCA_ISSUER -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         




## Transition to BYO Certificate mode

This section provides a series of steps to transition to the BYO-cert mode.

### Create a BYO CertificateIssuer

  1. Create a `CertificateIssuer` resource and save it as a YAML file, for example, `byo-cert-issuer.yaml`. This BYO cert issuer uses the managed `default-tls-ca` as the fallback CA:
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateIssuer
         metadata:
           name: BYO_CERT_ISSUER_NAME
           namespace: pki-system
         spec:
           byoCertConfig:
             fallbackCertificateAuthority:
               name: default-tls-ca
               namespace: pki-system
         

Replace BYO_CERT_ISSUER_NAME with the name of the BYO-cert issuer.

  2. Apply the custom resource to your Distributed Cloud zone in the Management API server:
         
         kubectl apply -f byo-cert-issuer.yaml --kubeconfig MANAGEMENT_API_SERVER
         

  3. Verify the readiness of the new issuer.
         
         kubectl -n pki-system get certificateissuer.pki.security.gdc.goog/BYO_CERT_ISSUER_NAME -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

The output looks similar to the following:
         
         {
           "lastTransitionTime": "2024-05-01T22:25:20Z",
           "message": "",
           "observedGeneration": 1,
           "reason": "FallbackCAReady",
           "status": "True",
           "type": "Ready"
         }
         




#### Sign the BYO Certificate

**Note:** Platform Administrators can't access the `default-wildcard-cert` certificate in the `istio-system` namespace. Contact your Infrastructure Operator (IO) to perform these steps.

  1. When waiting for the CSR to be externally signed, a BYO-cert can be temporarily issued by a fallback CA specified in the BYO-cert issuer. Get the current BYO-cert `default-wildcard-cert` status:
         
         kubectl get certificate.pki.security.gdc.goog/default-wildcard-cert -n istio-system -o json | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

The output looks similar to the following:
         
         {
           "lastTransitionTime": "2024-05-03T08:42:10Z",
           "message": "Certificate is issued by a fallback CA",
           "observedGeneration": 1,
           "reason": "UsingFallbackCA",
           "status": "True",
           "type": "Ready"
         }
         

The ready reason states `UsingFallbackCA` to indicate the fallback CA issues the certificate. It's then stored in the secret and ready for use.

  2. Get the certificate secret name:
         
         kubectl -n istio-system get certificate.pki.security.gdc.goog/default-wildcard-cert -ojson | jq -r '.spec.secretConfig.secretName'
         

The output looks similar to the following:
         
         web-tls
         

  3. Check the issuer from the secret:
         
         kubectl get secret web-tls -n istio-system -o jsonpath='{.data.tls\.crt}' |
         base64 -d | openssl x509 -text -noout | grep Issuer
         

The output looks similar to the following:
         
         Issuer: CN = GDC Managed ORG TLS CA
         

A bring-your-own certificate (BYO-cert) can temporarily use a matched certificate while awaiting its own CSR signature. An example-service certificate with dnsName as `example-service.org-1.zone1.google.gdch.test` is matched by the `default-wildcard-cert`with DNSName `*.org-1.zone1.google.gdch.test` from the same certificate issuer. The example-service certificate can hold the following status while waiting for its CSR to be signed:
         
         {
           "lastTransitionTime": "2024-05-03T22:30:51Z",
           "message": "Using a matched issued Certificate: default-wildcard-cert/istio-system",
           "observedGeneration": 1,
           "reason": "UsingMatchedCert",
           "status": "True",
           "type": "Ready"
         }
         

  4. Get the CSR from the certificate status:
         
         kubectl -n istio-system get certificate.pki.security.gdc.goog/default-wildcard-cert -ojson | jq -r ' .status.byoCertStatus.csrStatus'
         

The output looks similar to the following:
         
         {
           "conditions": [
             {
               "lastTransitionTime": "2024-05-03T18:14:19Z",
               "message": "",
               "observedGeneration": 1,
               "reason": "WaitingForSigning",
               "status": "False",
               "type": "Ready"
             }
           ],
           "csr": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSB..."
         }
         

  5. There are different methods for signing a CSR based on the external CA configuration. When signing, use the SAN from the CSR. For example:
         
         function signCert() {
            certName=$1
            ns=$2
         
            # Download the CSR from the certificate
            kubectl get certificate.pki.security.gdc.goog $certName -n $ns -o jsonpath='{.status.byoCertStatus.csrStatus.csr}' | base64 -d > $certName.csr
         
            # Get SAN from the csr
            san=$(openssl req -in $certName.csr -noout -text | grep 'DNS:' | sed -s 's/^[ ]*//')
         
            # Save SAN to extension config
            cat <<EOF >$certName-csr.ext
          keyUsage=digitalSignature,keyEncipherment
          extendedKeyUsage=serverAuth,clientAuth
          subjectAltName=${san}
          EOF
         
            # Sign the CSR with an external CA. You need to prepare the external CA cert and key
            openssl x509 -req -in $certName.csr -days 365 -CA ext-ca.crt -CAkey ext-ca.key -CAcreateserial -extfile $certName-csr.ext -out $certName-signed.crt
            openssl x509 -in $certName-signed.crt -text -noout
         
            # Upload the externally signed certificate by patching.
            echo "spec:
              byoCertificate:
                 certificate: $(base64 -w0 $certName-signed.crt)
                 ca: $(base64 -w0 ext-ca.crt)" > patch.txt
         
            kubectl patch certificate.pki.security.gdc.goog $certName -n $ns --patch-file patch.txt --type='merge'
          }
         
          # Use the function to sign the default-wildcard-cert in the istio-system namespace
          signCert default-wildcard-cert istio-system
         

  6. Verify the following details:

     * The certificate's CSR status is `Ready`
    
    kubectl -n istio-system get certificate.pki.security.gdc.goog/default-wildcard-cert -ojson | jq -r ' .status.byoCertStatus.csrStatus.conditions'
    
    
    [
       {
          "lastTransitionTime": "2024-05-03T21:56:25Z",
          "message": "",
          "observedGeneration": 2,
          "reason": "Signed",
          "status": "True",
          "type": "Ready"
       }
    ]
    

     * The certificate is `Ready` with the reason `Issued`
    
    kubectl get certificate.pki.security.gdc.goog/default-wildcard-cert -n istio-system -o json | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
    

The output looks similar to the following:
    
    {
      "lastTransitionTime": "2024-05-03T08:42:10Z",
      "message": "Certificate is issued",
      "observedGeneration": 2,
      "reason": "Issued",
      "status": "True",
      "type": "Ready"
    }
    

     * The secret is updated:
    
    kubectl get secret web-tls -n istio-system -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout | grep Issuer
    

The output looks similar to the following:
    
    Issuer: CN = external-ca
    




## Transition to a BYO Certificate with ACME mode

This section provides a series of steps to transition to a BYO-cert with ACME mode.

### Create a CertificateIssuer with ACME config

  1. Create a `CertificateIssuer` resource with ACME config and save it as a YAML file, such as `acme-issuer.yaml`.
         
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateIssuer
         metadata:
           name: ACME_ISSUER_NAME
           namespace: pki-system
         spec:
              acmeConfig:
                rootCACertificate: ROOT_CA_CERTIFICATE
                acme:
                  server: ACME_SERVER_URL
                  caBundle: CA_BUNDLE
                  privateKeySecretRef:
                    name: PRIVATE_KEY_SECRET_NAME
         

Replace the following variables:

     * ACME_ISSUER_NAME: the name of the ACME issuer.
     * ROOT_CA_CERTIFICATE: the root CA data of certificates issued by ACME server.
     * ACME_SERVER_URL: the URL to access the ACME server's directory endpoint.
     * CA_BUNDLE: the Base64-encoded bundle of PEM CAs that validates the certificate chain presented by the ACME server.
     * PRIVATE_KEY_SECRET_NAME: the name of the secret that contains the ACME account private key.

To use an existing ACME account private key, ensure the secret holding it uses the name PRIVATE_KEY_SECRET_NAME within the same namespace as the ACME issuer. If you don't provide this secret, a new one with the same name generates automatically to store the ACME account private key.

  2. Apply the custom resource to your Distributed Cloud zone:
         
         kubectl apply -f acme-issuer.yaml --kubeconfig MANAGEMENT_API_SERVER
         

  3. Verify the readiness of the new issuer:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER -n pki-system get certificateissuer.pki.security.gdc.goog/ACME_ISSUER_NAME -ojson | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

You see output similar to the following:
         
         {
           "lastTransitionTime": "2024-05-01T18:32:17Z",
           "message": "",
           "observedGeneration": 1,
           "reason": "ACMEClientReady",
           "status": "True",
           "type": "Ready"
         }
         




## Certificate reissuance

To switch the default issuer to the new ACME issuer, see [Change default certificate issuer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/change-default-issuer)

To immediately reissue certificates with the new default issuer, see [Manually reissue PKI web certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/pki-cert-reissue).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
