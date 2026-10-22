---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/encryption-keys/
title: Encrypt template parameters by using Cloud KMS \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:15.918086+00:00
---

# Encrypt template parameters by using Cloud KMS  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Encrypt template parameters by using Cloud KMS Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to encrypt sensitive data in Google-provided template parameters, by using encryption keys with Cloud KMS.

## Overview

Some Google-provided templates enable you to encrypt sensitive data in the template parameters, such as usernames, passwords, JDBC connection strings, and API keys. When supported, these templates include a parameter to specify the Cloud KMS encryption key, such as:

  * `KMSEncryptionKey`
  * `tokenKMSEncryptionKey`
  * `apiKeyKMSEncryptionKey`



To use Cloud KMS encryption keys with these templates, perform the following steps:

  1. Grant the Dataflow [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) the [**Cloud KMS CryptoKey Decrypter**](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) role.
  2. [Create an encryption key](https://docs.cloud.google.com/kms/docs/create-encryption-keys).
  3. Use the key to encrypt the data.
  4. Base64-encode the encrypted data.
  5. When you run the template, specify the encryption key and use the encrypted parameter values.



If you specify an encryption key, you must encrypt all of the parameters that support encryption. To understand which parameters can be encrypted, see the documentation for the specific template.

## Example

The following example uses the [MySQL to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mysql-to-bigquery) template.

  1. Create a key ring.
         
         gcloud kms keyrings create "KEY_RING_NAME" \
          --location "global"
         

  2. Create an encryption key.
         
         gcloud kms keys create "KEY_NAME" \
          --location "global" \
          --keyring "KEY_RING_NAME" \
          --purpose "encryption"
         

  3. Encrypt and base64-encode the username, password, and JDBC connection string.
         
         export USER_NAME=`echo -n "USER_NAME" \
          | gcloud kms encrypt --key=quickstart --keyring=test --location=global --plaintext-file=- --ciphertext-file=- \
          | base64 -w 0`
         export PASSWORD=`echo -n "PASSWORD" \
          | gcloud kms encrypt --key=quickstart --keyring=test --location=global --plaintext-file=- --ciphertext-file=- \
          | base64 -w 0`
         export CONNECTION_STRING=`echo -n "CONNECTION_STRING" \
          | gcloud kms encrypt --key=quickstart --keyring=test --location=global --plaintext-file=- --ciphertext-file=- \
          | base64 -w 0`
         

  4. Run the template.
         
         gcloud dataflow flex-template run mysql-job \
          --project=PROJECT_ID \
          --region=us-central1 \
          --template-file-gcs-location=gs://dataflow-templates/latest/flex/MySQL_to_BigQuery \
          --parameters \
         connectionURL="$CONNECTION_STRING",\
         query="SOURCE_SQL_QUERY",\
         outputTable=PROJECT_ID:DATASET.TABLE_NAME,\
         bigQueryLoadingTemporaryDirectory=CLOUD_STORAGE_PATH,\
         username="$USER_NAME",\
         password="$PASSWORD",\
         KMSEncryptionKey=projects/PROJECT_ID/locations/global/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         




## Troubleshooting

This section contains troubleshooting information for encrypting template parameters.

### Permission denied

When you run the job, you see a `PERMISSION_DENIED` error in the job logs, similar to the following:
    
    
    PERMISSION_DENIED: Permission cloudkms.cryptoKeyVersions.useToDecrypt denied on
    resource RESOURCE_PATH (or it may not exist)
    

To decrypt the data, the Dataflow worker service account needs the **cloudkms.cryptoKeyVersions.useToDecrypt** permission for the encryption key. Make sure the worker service account has the **Cloud KMS CryptoKey Decrypter** role. For more information, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

## What's next

  * Learn more about [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
