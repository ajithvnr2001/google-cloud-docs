---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-tls-certificate-verification-failure/
title: Cassandra TLS certificate verification failure \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:43.301790+00:00
---

# Cassandra TLS certificate verification failure  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-tls-certificate-verification-failure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra TLS certificate verification failure Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptoms

The TLS certificate verification process in Cassandra pods could fail with an error similar to the following: 
    
    
    Caused by: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
    at sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:456)
    at sun.security.validator.PKIXValidator.engineValidate(PKIXValidator.java:323)
    at sun.security.validator.Validator.validate(Validator.java:271)
    at sun.security.ssl.X509TrustManagerImpl.validate(X509TrustManagerImpl.java:315)
    at sun.security.ssl.X509TrustManagerImpl.checkTrusted(X509TrustManagerImpl.java:278)
    at sun.security.ssl.X509TrustManagerImpl.checkServerTrusted(X509TrustManagerImpl.java:141)
    at io.netty.handler.ssl.ReferenceCountedOpenSslClientContext$ExtendedTrustManagerVerifyCallback.verify(ReferenceCountedOpenSslClientContext.java:261)
    at io.netty.handler.ssl.ReferenceCountedOpenSslContext$AbstractCertificateVerifier.verify(ReferenceCountedOpenSslContext.java:698)
    ...
    Suppressed: javax.net.ssl.SSLHandshakeException: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED
    at io.netty.handler.ssl.ReferenceCountedOpenSslEngine.sslReadErrorResult(ReferenceCountedOpenSslEngine.java:1309)
    at io.netty.handler.ssl.ReferenceCountedOpenSslEngine.unwrap(ReferenceCountedOpenSslEngine.java:1270)
    ...

## Possible Causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Apigee CA certificate does not match across Apigee clusters |  If the Apigee CA certificate does not match across clusters, then TLS certificate verification in Cassandra could fail.  | Apigee hybrid  
  
### Prerequisites

  * [ kubectl](https://kubernetes.io/docs/reference/kubectl/) needs to be installed and configured for accessing Apigee clusters. 
  * [ jq](https://jqlang.github.io/jq/) is required for formatting JSON content. 
  * [ keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) is required for printing TLS certificates. 
  * [ cmctl](https://cert-manager.io/docs/reference/cmctl/) is required for reissuing certificates using Cert Manager. 



## Cause: Apigee CA certificate does not match across Apigee clusters

### Diagnosis

  1. Read `apigee-ca` secret and print Apigee CA certificate of all clusters using the following command: 
         
         kubectl -n cert-manager get secret apigee-ca -o json | jq -r '.data["tls.crt"]' | base64 -d | keytool -printcert | grep Version -B 10

An example output:
         
         kubectl -n cert-manager get secret apigee-ca -o json | jq -r '.data["tls.crt"]' | base64 -d | keytool -printcert | grep Version -B 10
         Owner: CN=apigee-hybrid, O=apigee + O=cluster.local
         Issuer: CN=apigee-hybrid, O=apigee + O=cluster.local
         Serial number: afcc2ef957cebfd52b118b0b1622021
         Valid from: Wed Oct 30 03:09:23 UTC 2024 until: Sat Oct 28 03:09:23 UTC 2034
         Certificate fingerprints:
                 SHA1: 32:D9:77:54:B1:FC:CB:6C:9E:28:C1:04:25:49:0D:F5:7C:88:A5:6C
                 SHA256: 7C:97:31:3B:56:CD:A3:EF:88:A7:DC:17:AE:D5:F2:A7:6A:48:B3:FC:AA:04:F0:6B:9F:43:C4:5C:6E:15:DE:37
         Signature algorithm name: SHA256withECDSA
         Subject Public Key Algorithm: 256-bit EC (secp256r1) key
         Version: 3

  2. Read `apigee-cassandra-default-tls` secret and verify whether the above Apigee CA certificate has been used when generating the Cassandra certificate. The `apigee-cassandra-default-tls` secret contains the Apigee CA certificate under `ca.crt`: 
         
         kubectl -n apigee get secret apigee-cassandra-default-tls -o json | jq -r '.data["ca.crt"]' | base64 -d | keytool -printcert | grep Version -B 10

An example output:
         
         kubectl -n apigee get secret apigee-cassandra-default-tls -o json | jq -r '.data["ca.crt"]' | base64 -d | keytool -printcert | grep Version -B 10
         Owner: CN=apigee-hybrid, O=apigee + O=cluster.local
         Issuer: CN=apigee-hybrid, O=apigee + O=cluster.local
         Serial number: afcc2ef957cebfd52b118b0b1622021
         Valid from: Wed Oct 30 03:09:23 UTC 2024 until: Sat Oct 28 03:09:23 UTC 2034
         Certificate fingerprints:
                 SHA1: 32:D9:77:54:B1:FC:CB:6C:9E:28:C1:04:25:49:0D:F5:7C:88:A5:6C
                 SHA256: 7C:97:31:3B:56:CD:A3:EF:88:A7:DC:17:AE:D5:F2:A7:6A:48:B3:FC:AA:04:F0:6B:9F:43:C4:5C:6E:15:DE:37
         Signature algorithm name: SHA256withECDSA
         Subject Public Key Algorithm: 256-bit EC (secp256r1) key
         Version: 3

  3. In the above example, the serial number of the Apigee CA certificate found in the `apigee-ca` secret matches with the Apigee CA certificate found in the `apigee-cassandra-default-tls` secret: `afcc2ef957cebfd52b118b0b1622021`. This confirms that the Cassandra certificate has been signed by the same Apigee CA certificate. We could verify this further by following the steps below. 
  4. Extract Apigee CA certificate pem file: 
         
         kubectl -n cert-manager get secret apigee-ca -o json | jq -r '.data["tls.crt"]' | base64 -d > apigee-ca.crt

An example output:
         
         kubectl -n cert-manager get secret apigee-ca -o json | jq -r '.data["tls.crt"]' | base64 -d > apigee-ca.crt
         cat apigee-ca.crt
         -----BEGIN CERTIFICATE-----
         MIIBvjCCAWSgAwIBAgIQCvzC75V86/1SsRiwsWIgITAKBggqhkjOPQQDAjA/MSUw
         DQYDVQQKEwZhcGlnZWUwFAYDVQQKEw1jbHVzdGVyLmxvY2FsMRYwFAYDVQQDEw1h
         cGlnZWUtaHlicmlkMB4XDTI0MTAzMDAzMDkyM1oXDTM0MTAyODAzMDkyM1owPzEl
         MA0GA1UEChMGYXBpZ2VlMBQGA1UEChMNY2x1c3Rlci5sb2NhbDEWMBQGA1UEAxMN
         YXBpZ2VlLWh5YnJpZDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABNSow7pxNvjj
         R/jV66nY/w/tn22tu7oXyZS8tAFBnP7D2fFfIdk4tJub3gw/CsoyNa1cKXwAt7Tw
         SLp1iGJ3CY+jQjBAMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MB0G
         A1UdDgQWBBRSjN/cNNbg2kvmddskzdurglxuwTAKBggqhkjOPQQDAgNIADBFAiBp
         pCgNNC8TVEgF8jR5RK9dXZJRcNY39nFY4DqbH6bUJwIhAPdzx5gee3BIWYwlQAYX
         CgtCf4blLNq3KlBWTO993XoY
         -----END CERTIFICATE-----

  5. Extract Cassandra certificate pem file: 
         
         kubectl -n apigee get secrets apigee-cassandra-default-tls -o json | jq -r '.data["tls.crt"]' | base64 -d > apigee-cassandra-default-tls.crt

An example output:
         
         kubectl -n apigee get secrets apigee-cassandra-default-tls -o json | jq -r '.data["tls.crt"]' | base64 -d > apigee-cassandra-default-tls.crt
         cat apigee-cassandra-default-tls.crt
         -----BEGIN CERTIFICATE-----
         MIIDSDCCAu6gAwIBAgIQZcYk/VOfGUQEzpLbAvyyNjAKBggqhkjOPQQDAjA/MSUw
         DQYDVQQKEwZhcGlnZWUwFAYDVQQKEw1jbHVzdGVyLmxvY2FsMRYwFAYDVQQDEw1h
         cGlnZWUtaHlicmlkMB4XDTI0MTAzMDAzMTAyMFoXDTM0MTAyODAzMTAyMFowPDE6
         MDgGA1UEAxMxYXBpZ2VlLWNhc3NhbmRyYS1kZWZhdWx0LmFwaWdlZS5zdmMuY2x1
         c3Rlci5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM6k8YyB
         m/AV9cgexU8fZ4OFw8M72oxWEF44sFezZB7NpCqIFBxAM/7iL0tF2qU4S4gpcabD
         bn30fKKID8651Kytc7KHGT13Nlj9vQRjd0HJD8Qa8YtRcmGKtp+1fbQOcMPxvuNA
         CzaQyuPwieYKc6D9DpDDkPPCmjVwfaxHmNpdswrt0NQbSecg/xZPXbpzOZ6bUFha
         2vTvSTomiDKIPGhWrMnEMJDjFyjpdYND74HnYgw1XGnC4SQNts/kvXligbVmW+Rz
         oyV7n99eN6cE5J/FHDgiHrBRZUw8ujP2l/p7Y96NcMBnXCsQu6RsCDltXqX1f1pG
         sIjUAFAZZvM0pDECAwEAAaOCAQIwgf8wDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQW
         MBQGCCsGAQUFBwMCBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaA
         FFKM39w01uDaS+Z12yTN26uCXG7BMIGeBgNVHREEgZYwgZOCGGFwaWdlZS1jYXNz
         YW5kcmEtZGVmYXVsdIIfYXBpZ2VlLWNhc3NhbmRyYS1kZWZhdWx0LmFwaWdlZYIj
         YXBpZ2VlLWNhc3NhbmRyYS1kZWZhdWx0LmFwaWdlZS5zdmOCMWFwaWdlZS1jYXNz
         YW5kcmEtZGVmYXVsdC5hcGlnZWUuc3ZjLmNsdXN0ZXIubG9jYWwwCgYIKoZIzj0E
         AwIDSAAwRQIhANt7WYfSbS4a14Fvf3IXcG+/p3iEGg61suK8jOxtgJMyAiBG3z7Y
         kgR7SWNzSoom4Oznq9NSub7v75kfQJFKEtP0Mg==
         -----END CERTIFICATE-----

  6. Verify Cassandra certificate using Apigee CA certificate: 
         
         openssl verify -CAfile apigee-ca.crt apigee-cassandra-default-tls.crt

A successful example output:
         
         openssl verify -CAfile apigee-ca.crt apigee-cassandra-default-tls.crt
         apigee-cassandra-default-tls.crt: OK

A failure example output:
         
         openssl verify -CAfile apigee-ca.crt apigee-cassandra-default-tls.crt
         CN = apigee-cassandra-default.apigee.svc.cluster.local
         error 20 at 0 depth lookup: unable to get local issuer certificate
         error apigee-cassandra-default-tls.crt: verification failed




### Resolution

  1. Select an Apigee cluster which has the correct Apigee CA certificate.
  2. Export Apigee CA certificate secret from that cluster to a file: 
         
         kubectl -n cert-manager get secret apigee-ca -o yaml > apigee-ca.yaml

  3. Apply above Apigee CA certificate secret to all other clusters by selecting one cluster at a time, perform all remaining steps in all clusters: 
         
         kubectl -n cert-manager apply -f apigee-ca.yaml

  4. Export all existing certificates available in the `apigee` namespace to a backup file: 
         
         kubectl -n apigee get certificates --all -o yaml > all-certificates.yaml

  5. Execute following `cmctl` command for reissuing all certificates found in the `apigee` namespace: 
         
         cmctl renew --namespace=apigee --all

An example output:
         
         cmctl renew --namespace=apigee --all
         
           Manually triggered issuance of Certificate apigee/apigee-cassandra-default
           Manually triggered issuance of Certificate apigee/apigee-cassandra-schema-setup-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-cassandra-schema-val-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-cassandra-user-setup-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-connect-agent-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-datastore-guardrails-tls
           Manually triggered issuance of Certificate apigee/apigee-istiod
           Manually triggered issuance of Certificate apigee/apigee-mart-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-metrics-adapter-apigee-telemetry
           Manually triggered issuance of Certificate apigee/apigee-redis-default
           Manually triggered issuance of Certificate apigee/apigee-redis-envoy-default
           Manually triggered issuance of Certificate apigee/apigee-runtime-demo-hybrid-de-dev-b276d3f
           Manually triggered issuance of Certificate apigee/apigee-serving-cert
           Manually triggered issuance of Certificate apigee/apigee-synchronizer-demo-hybrid-de-dev-b276d3f
           Manually triggered issuance of Certificate apigee/apigee-udca-demo-hybrid-de-5fdc6d2
           Manually triggered issuance of Certificate apigee/apigee-watcher-demo-hybrid-de-5fdc6d2

This step should reissue all Apigee runtime certificates using the newly imported Apigee CA certificate and that should resolve this problem. 

  6. Check the issue date of all certificates against the UTC time and verify whether they have been reissued: 
         
         kubectl get certificates -n apigee -o json | jq -r '.items[] | "\(.metadata.name): \(.status.notBefore)"'
         date -u

An example output:
         
         kubectl get certificates -n apigee -o json | jq -r '.items[] | "\(.metadata.name): \(.status.notBefore)"'
         
           apigee-cassandra-default: 2024-12-16T04:19:58Z
           apigee-cassandra-schema-setup-demo-hybrid-de-5fdc6d2: 2024-12-16T04:19:58Z
           apigee-cassandra-schema-val-demo-hybrid-de-5fdc6d2: 2024-12-16T04:19:58Z
           apigee-cassandra-user-setup-demo-hybrid-de-5fdc6d2: 2024-12-16T04:19:59Z
           apigee-connect-agent-demo-hybrid-de-5fdc6d2: 2024-12-16T04:20:00Z
           apigee-datastore-guardrails-tls: 2024-12-16T04:20:01Z
           apigee-istiod: 2024-12-16T04:20:02Z
           apigee-mart-demo-hybrid-de-5fdc6d2: 2024-12-16T04:20:02Z
           apigee-metrics-adapter-apigee-telemetry: 2024-12-16T04:20:03Z
           apigee-redis-default: 2024-12-16T04:20:04Z
           apigee-redis-envoy-default: 2024-12-16T04:20:04Z
           apigee-runtime-demo-hybrid-de-dev-b276d3f: 2024-12-16T04:20:04Z
           apigee-serving-cert: 2024-12-16T04:20:04Z
           apigee-synchronizer-demo-hybrid-de-dev-b276d3f: 2024-12-16T04:20:05Z
           apigee-udca-demo-hybrid-de-5fdc6d2: 2024-12-16T04:20:06Z
           apigee-watcher-demo-hybrid-de-5fdc6d2: 2024-12-16T04:20:07Z
         
           date -u
           Mon Dec 16 04:23:45 AM UTC 2024

  7. Check the expiry date of all certificates and confirm that has been extended accordingly: 
         
         kubectl get certificates -n apigee -o json | jq -r '.items[] | "\(.metadata.name): \(.status.notAfter)"'

An example output:
         
         kubectl get certificates -n apigee -o json | jq -r '.items[] | "\(.metadata.name): \(.status.notAfter)"'
         
           apigee-cassandra-default: 2034-12-14T04:19:58Z
           apigee-cassandra-schema-setup-demo-hybrid-de-5fdc6d2: 2034-12-14T04:19:58Z
           apigee-cassandra-schema-val-demo-hybrid-de-5fdc6d2: 2034-12-14T04:19:58Z
           apigee-cassandra-user-setup-demo-hybrid-de-5fdc6d2: 2034-12-14T04:19:59Z
           apigee-connect-agent-demo-hybrid-de-5fdc6d2: 2034-12-14T04:20:00Z
           apigee-datastore-guardrails-tls: 2024-12-16T05:20:01Z
           apigee-istiod: 2024-12-18T04:20:02Z
           apigee-mart-demo-hybrid-de-5fdc6d2: 2034-12-14T04:20:02Z
           apigee-metrics-adapter-apigee-telemetry: 2034-12-14T04:20:03Z
           apigee-redis-default: 2034-12-14T04:20:04Z
           apigee-redis-envoy-default: 2034-12-14T04:20:04Z
           apigee-runtime-demo-hybrid-de-dev-b276d3f: 2034-12-14T04:20:04Z
           apigee-serving-cert: 2025-03-16T04:20:04Z
           apigee-synchronizer-demo-hybrid-de-dev-b276d3f: 2034-12-14T04:20:05Z
           apigee-udca-demo-hybrid-de-5fdc6d2: 2034-12-14T04:20:06Z
           apigee-watcher-demo-hybrid-de-5fdc6d2: 2034-12-14T04:20:07Z

**Note:** `apigee-datastore-guardrails-tls` and `apigee-istiod` are expected to have much shorter lifetimes than the other certificates. 



## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The Apigee hybrid organization.
  3. The `overrides.yaml` files from both source and new regions, masking any sensitive information.
  4. The outputs from the commands in [ Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather). 
  5. The outputs from the commands in [ Apigee hybrid Cassandra must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-cassandra-must-gather). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
