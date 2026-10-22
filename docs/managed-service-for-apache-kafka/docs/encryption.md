---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption/
title: Configure message encryption in Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:10.758062+00:00
---

# Configure message encryption in Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Configure message encryption in Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure customer-managed encryption keys (CMEK) for a Google Cloud Managed Service for Apache Kafka cluster.

## Overview of message encryption

By default, Managed Service for Apache Kafka encrypts [messages at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) with Google-owned and Google-managed encryption keys. No additional setup is required.

If you need more control over the encryption keys used to protect Managed Service for Apache Kafka data at rest, you can set a CMEK when you create your cluster. CMEKs are encryption keys that you own. They are managed and stored in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) (Cloud KMS). When you configure a cluster with a CMEK, the service automatically uses that key to encrypt all cluster data at rest. Using a CMEK might incur additional costs, depending on your usage patterns.

A CMEK associated with a Managed Service for Apache Kafka cluster is a key-encryption key (KEK). The KEK is used to encrypt a data encryption key (DEK). The DEK is then used to read and write data at rest on persistent disks attached to brokers and data in tiered storage in Cloud Storage.

Because Managed Service for Apache Kafka resources are regional, we recommend that you create CMEKs in the same region as the Kafka cluster.

## Required roles and permissions

The Managed Kafka service account must have permission to encrypt and decrypt data using a CMEK.

Grant the service account the Cloud KMS Crypto Key Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the Cloud KMS key:
    
    
    gcloud kms keys add-iam-policy-binding KEY \
      --keyring=KEY_RING \
      --location=LOCATION \
      --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com \
      --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

  * KEY: The name of the key.

  * KEY_RING: The name of the key ring where the key is located.

  * LOCATION: the Cloud KMS location for the key ring.

  * PROJECT_NUMBER: The project number of the Google Cloud project that contains the Managed Service for Apache Kafka cluster.




For more information about granting roles on a Cloud KMS key, see [Granting roles on a resource](https://docs.cloud.google.com/kms/docs/iam#granting_roles_on_a_resource).

## Rotate keys

You can't change the key associated with a cluster. Instead, you can rotate a key by creating a new key version and setting it as primary for the key.

For the disks attached to brokers, the new KEK takes effect only after a broker is restarted. You can force a rolling restart of brokers by updating a cluster's capacity configuration. For example, you can change the cluster RAM amount.

All new partition segment files are written to tiered storage using the new primary key version. A delay of several minutes is possible after a new primary key version is chosen.

## Audit logs

Cloud KMS produces audit logs when keys are enabled, disabled, or used by Managed Service for Apache Kafka to encrypt and decrypt messages. This is useful in debugging issues with publish or delivery availability.

Cloud KMS key IDs are attached to audit logs for Managed Service for Apache Kafka cluster resources. Managed Service for Apache Kafka does not include any other Cloud KMS-related information in audit logs.

## Disable and re-enable CMEK

There are two ways to disable CMEK. Choose one of the following methods:

  * [Disable the Cloud KMS key](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) that you've associated with the cluster. This approach affects all Cloud resources associated with that key.

  * [Revoke the CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) from the Managed Service for Apache Kafka service agent (`service-${PROJECT_NUMBER}@gcp-sa-managedkafka.iam.gserviceaccount.com`) by using Identity and Access Management (IAM). This approach affects all of the Managed Service for Apache Kafka clusters in the project and the messages encrypted by using CMEK.




Although neither operation might cause instantaneous access revocation, IAM changes generally propagate faster.

For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

When Managed Service for Apache Kafka cannot access a Cloud KMS key, message publishing and delivery fails with errors. To resume delivery and publishing, [restore access](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version) to the Cloud KMS key.

After the Cloud KMS key is accessible to Managed Service for Apache Kafka, publishing is available within 12 hours and message delivery resumes within 2 hours.

Although intermittent Cloud KMS outages of less than a minute are unlikely to significantly interrupt publishing and delivery, extended Cloud KMS unavailability has the same effect as key revocation.

## Limitations

  * You can't change the key associated with a cluster. Instead, you can rotate the key by creating new versions.

  * If you disable a non-primary key version, local disks continue working with no change. Each broker downloads the new KEK when it is restarted. However, Cloud Storage can't access topic segment files that were encrypted using the original version, which might make it impossible to consume messages from these segment files. You might not be able to consume older data.

  * If you disable the primary version of a key, the brokers can't write new segment files to tiered storage, which increases local disk utilization. In additions, broker restarts will fail. A restart can be triggered both by you proactively or an service-initiated update to the cluster at any time.

  * If you remove access to a key from the Managed Service for Apache Kafka service agent, the behavior is similar to what happens if you disable both the primary key and non-primary key versions.

  * If you delete a key, the cluster is scheduled for shutdown and can't be recovered.

  * You can't request re-encryption of the data stored at rest. The CMEK is used as a KEK, but re-encryption requires a change in the data encryption keys.




## What's next

  * [Create encryption keys with Cloud KMS](https://docs.cloud.google.com/kms/docs/create-encryption-keys).

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

  * For more information about disk encryption, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

  * For more information about encryption in Cloud Storage, see [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
