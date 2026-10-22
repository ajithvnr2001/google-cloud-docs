---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-upload-server-cert/
title: Sign and upload a server certificate \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:51.762461+00:00
---

# Sign and upload a server certificate  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-upload-server-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Sign and upload a server certificate Stay organized with collections  Save and categorize content based on your preferences. 

When you create a database cluster, a server certificate that is signed by the default GDC CA will be generated and configured for use by your database server. To sign and upload a certificate for your database that is issued by your own PKI, perform the following procedure. Your organization's default issuer must be in BYO certificate mode to use this feature.

### API

  1. After you have created the database cluster and it is ready, save the generated certificate signing request as a file.
         
         kubectl get certificate.pki.security.gdc.goog \
         dbs-pg-cert-request-DBCLUSTER_NAME \
         -n USER_PROJECT -o jsonpath='{.status.byoCertStatus.csrStatus.csr}' \
         | base64 -d > DBCLUSTER_NAME.csr
         

  2. Create a CSR extensions file containing the SANs for your database cluster.
         
         export SAN=$(openssl req -in DBCLUSTER_NAME.csr -noout -text | grep 'DNS:' | sed -s 's/^[ ]*//')
         
         
         echo "keyUsage=digitalSignature,keyEncipherment
         extendedKeyUsage=serverAuth,clientAuth
         subjectAltName=${SAN:?}" > DBCLUSTER_NAME-csr.ext
         

  3. Using the CSR and extension file, generate the certificate signed by your CA. The code sample uses `openssl` but this step can be completed with other tools.
         
         openssl x509 -req -in DBCLUSTER_NAME.csr -days 365 \
         -CA CA_CERTIFICATE_FILE -CAkey CA_PRIVATE_KEY_FILE \
         -CAcreateserial -extfile DBCLUSTER_NAME-csr.ext  \
         -out DBCLUSTER_NAME-signed.crt
         

  4. Update the certificate resource with the signed certificate and CA certificate.
         
         echo "spec:
           byoCertificate:
             certificate: $(base64 -w0 DBCLUSTER_NAME-signed.crt)
             ca: $(base64 -w0 CA_CERTIFICATE_FILE)" > patch.txt
         
         
         kubectl patch certificate.pki.security.gdc.goog \
         dbs-pg-cert-request-DBCLUSTER_NAME \
         -n USER_PROJECT --patch-file patch.txt --type='merge'
         

  5. Verify that the certificate has reached a ready state after the upload.
         
         kubectl get certificate.pki.security.gdc.goog \
         dbs-pg-cert-request-DBCLUSTER_NAME \
         -n USER_PROJECT -o json | jq -r ' .status.conditions[] | select( .type as $id | "Ready" | index($id))'
         

The output should be similar to the following:
         
         {
           "lastTransitionTime": "2024-05-03T08:42:10Z",
           "message": "Certificate is issued",
           "observedGeneration": 2,
           "reason": "Issued",
           "status": "True",
           "type": "Ready"
         }
         




Replace the following:

  * `DBCLUSTER_NAME`: the name of the database cluster.
  * `USER_PROJECT`: the name of the user project where the database cluster was created.
  * `CA_CERTIFICATE_FILE`: the path to the database CA certificate file.
  * `CA_PRIVATE_KEY_FILE`: the path to the database CA private key file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
