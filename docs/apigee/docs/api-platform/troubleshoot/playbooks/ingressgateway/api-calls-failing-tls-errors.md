---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-failing-tls-errors/
title: API Calls failing with TLS errors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:37:54.502876+00:00
---

# API Calls failing with TLS errors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-failing-tls-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  API Calls failing with TLS errors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

Apigee hybrid API requests fail with TLS connection errors. These errors are usually connection resets and alert handshake failures. 

## Error messages

API calls fail with TLS similar to the error shown below, or other but not identical errors: 
    
    
    * TLSv1.2 (OUT), TLS handshake, Client hello (1):
    * LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to example.apis.com:443
    * Closing connection 0
    curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to example.apis.com:443
    
    
    * (304) (OUT), TLS handshake, Client hello (1):
    * Recv failure: Connection reset by peer
    * LibreSSL/3.3.6: error:02FFF036:system library:func(4095):Connection reset by peer
    * Closing connection
    curl: (35) Recv failure: Connection reset by peer
    
    
    * (304) (OUT), TLS handshake, Client hello (1):
    * LibreSSL/3.3.6: error:1404B410:SSL routines:ST_CONNECT:sslv3 alert handshake failure
    * Closing connection
    curl: (35) LibreSSL/3.3.6: error:1404B410:SSL routines:ST_CONNECT:sslv3 alert handshake failure

## Possible causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Missing Ingress Kubernetes secret | The Kubernetes secret for the `org-envgroup` is missing from the Apigee namespace. | Apigee hybrid  
Incorrectly formatted SSL certificate | The SSL certificate which is pointed in the virtualhosts section of the overrides file is incorrectly formatted. | Apigee hybrid  
The SSL keys do not match the SSL certificate | The SSL keys do not match the SSL certificate which is pointed in the virtualhosts section of the overrides file. | Apigee hybrid  
  
## Cause: Missing Ingress Kubernetes secret

### Diagnosis

  1. Analyze the logs of `apigee-watcher` pods in the apigee namespace and see if there are any errors.  
  
You may observe an error such as the following:  

         
         NOT_FOUND: failed to get secret "MY_HYBRID_PROJECT-ENV_GROUP"
         in namespace "apigee": secrets "MY_HYBRID_PROJECT-ENV_GROUP" not found

where: 
     * `MY_HYBRID_PROJECT` is the name of the Apigee hybrid organization
     * `ENV_GROUP` is the name of the environment group
The above error indicates that `apigee-watcher` could not find the Kubernetes secret for the above-mentioned environment group of the Apigee hybrid organization. 
  2. Verify that the Kubernetes secrets are indeed missing by using the following command: 
         
         kubectl -n apigee get secrets | grep MY_HYBRID_PROJECT-ENV_GROUP

`<no output>`  
This example shows no Kubernetes secrets for `MY_HYBRID_PROJECT-ENV_GROUP`. These could have been deleted erroneously.



### Resolution

You can recreate the missing Kubernetes secrets using the TLS certificates and key files information from the `overrides.yaml` file:

  1. Run the following command to recreate the missing secrets using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 

Dry run:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         --set envgroup=ENV_GROUP \
         -f OVERRIDES_FILE \
         --dry-run=server
         

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Your installation may or may not have been set up using an ENV_GROUP_RELEASE_NAME that differs from ENV_GROUP. For information on the settings, see [Install Apigee hybrid using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-helm-charts).

Install the chart:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         --set envgroup=ENV_GROUP \
         -f OVERRIDES_FILE
         

  2. Verify that the Kubernetes secrets are successfully created using the following command: 
         
         kubectl -n apigee get secrets | grep MY_HYBRID_PROJECT-ENV_GROUP

The output of this command should show: 
         
         MY_HYBRID_PROJECT-ENV_GROUP                   Opaque                2      7s




If the problem persists, go to Must Gather Diagnostic Information.

## Cause: Incorrectly formatted SSL certificate

### Diagnosis

First, ensure that the certificate file is a .PEM file. To check if the correctly formatted SSL certificate is loaded into `apigee-ingressgateway`, follow these steps.  
  
If you've configured one-way TLS using a cert/key pair as described in [Option 1: key/cert pair](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ingress-tls#option-1:-keycert-pair), run:
    
    
    openssl x509 -in $CERT_FILE -text -noout

An example output (without errors): 
    
    
    Certificate:
      Data:
        Version: 1 (0x0)
        Serial Number: 1 (0x1)
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: C = US, O = xyz, OU = abc, CN = INTERIM-CN
        Validity
          Not Before: Dec 18 09:40:23 2023 GMT
          Not After : May  1 09:40:23 2025 GMT
        Subject: C = US, O = xyz, OU = abc, CN = shrey.example.com
        Subject Public Key Info:
          Public Key Algorithm: rsaEncryption
            RSA Public-Key: (2048 bit)
            Modulus:
              Trimmed
            Exponent: 65537 (0x10001)
        Signature Algorithm: sha1WithRSAEncryption
              Trimmed

If you've configured one-way TLS using a Kubernetes secret as described in [Option 2: Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ingress-tls#option-2:-kubernetes-secret), run:
    
    
    kubectl -n apigee get secret <$SECRET_NAME> -o jsonpath='{.data.cert}'| base64 -d > certfile ;
    openssl x509 -in certfile -text -noout
    
    kubectl -n apigee get secret <$SECRET_NAME> -o jsonpath='{.data.cert}'| base64 -d | openssl x509 -noout -text

An example output (without errors):
    
    
    Certificate:
      Data:
        Version: 1 (0x0)
        Serial Number: 1 (0x1)
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: C = US, O = xyz, OU = abc, CN = INTERIM-CN
        Validity
          Not Before: Dec 18 09:40:23 2023 GMT
          Not After : May  1 09:40:23 2025 GMT
        Subject: C = US, O = xyz, OU = abc, CN = shrey.example.com
        Subject Public Key Info:
          Public Key Algorithm: rsaEncryption
            RSA Public-Key: (2048 bit)
            Modulus:
              Trimmed
            Exponent: 65537 (0x10001)
      Signature Algorithm: sha1WithRSAEncryption
              Trimmed

If the output of the above command looks like
    
    
    unable to load certificate
    136613728412992:error:0D078095:asn1 encoding routines:asn1_item_embed_d2i:sequence not constructed:../crypto/asn1/tasn_dec.c:321:Type=X509
    136613728412992:error:0906700D:PEM routines:PEM_ASN1_read_bio:ASN1 lib:../crypto/pem/pem_oth.c:33:

For errors like
    
    
    error loading certificates
    8360934016:error:09FFF066:PEM routines:CRYPTO_internal:bad end line

see the Resolution section.

### Resolution

The errors could differ depending on the format error in the certificate file. Fix the certificate error if needed.

If the output shows the certificate instead of an error, consider [Cause: The SSL Keys do not match the SSL certificate](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/unmatched-ssl-keys).

## Cause: The SSL keys do not match the SSL certificate

### Diagnosis

If you've configured one-way TLS using cert/key pair as described in [Option 1: key/cert pair](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ingress-tls#option-1:-keycert-pair), run:
    
    
    diff -q <(openssl rsa -noout -modulus -in $KEY_FILE ) <(openssl x509 -noout -modulus -in $CERT_FILE)

An example output (without errors):
    
    
    diff -q <(openssl rsa -noout -modulus -in my_server.key ) <(openssl x509 -noout -modulus -in my_server.pem)
    <No output>

If you've configured one-way TLS using Kubernetes secret as described in [Option 2: Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ingress-tls#option-2:-kubernetes-secret), run:
    
    
    diff -q <(kubectl -n apigee get secrets $SECRET_NAME -o jsonpath='{.data.key}'| base64 -d | openssl rsa -noout -modulus) <(kubectl -n apigee get secrets $SECRET_NAME -o jsonpath='{.data.cert}'| base64 -d | openssl x509 -noout -modulus)

An example output (without errors):
    
    
    diff -q <(kubectl -n apigee get secrets my-apigee-hybrid-env-grp -o jsonpath='{.data.key}'| base64 -d | openssl rsa -noout -modulus) <(kubectl -n apigee get secrets my-apigee-hybrid-env-grp -o jsonpath='{.data.cert}'| base64 -d | openssl x509 -noout -modulus)
    <No output>

If the output of the above command shows an error like:
    
    
    unable to load Private Key
    133504499987776:error:09091064:PEM routines:PEM_read_bio_ex:bad base64 decode:../crypto/pem/pem_lib.c:949:
    Files /dev/fd/63 and /dev/fd/62 differ

then the SSL Keys do not match the SSL certificate and please see the Resolution section.

### Resolution

Ensure that you are providing the correct private keys and their corresponding SSL certificates. Fix any private key and SSL certificate problems.

If you do not see any output of the command, the SSL certificate and the SSL key match.

## Must Gather Diagnostic Information

If the problem persists after following the instructions on this page, please gather the following diagnostic information and provide it to [Apigee Support](https://cloud.google.com/apigee/support): 

  1. The entire `curl` verbose output in which you see the error.
  2. Capture a `tcpdump` on the machine on which you are seeing the errors and share it by removing any sensitive information and IP addresses.
  3. Have the entire network topology and network flow ready after consulting with your network team to be shared with Apigee Support.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
