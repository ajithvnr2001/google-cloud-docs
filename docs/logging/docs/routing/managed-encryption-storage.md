---
url: https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage/
title: Configure CMEK for log buckets \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:35.097518+00:00
---

# Configure CMEK for log buckets  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure CMEK for log buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for configuring customer-managed encryption keys (CMEK) for logs stored in [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries). This document also describes how to manage those keys, and limitations associated with using CMEK.

For organizations and folders, you can configure CMEK as a default resource settings for Cloud Logging. When configured, Cloud Logging ensures that all new log buckets in the organization or folder are encrypted with a customer-managed key. If you don't supply a key when you create a log bucket, then the key specified by the default resource settings for Cloud Logging is used. For more information, see [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

The information in this document doesn't apply to observability buckets. If you are interested in observability buckets, then see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## Overview

By default, Cloud Logging encrypts customer content at rest. Logging handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Logging. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Logging resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

**Note:** After a log bucket is created, you can't reconfigure the log bucket to change or remove CMEK.

## Prerequisites

Complete the following steps:

  1. There are some limitations when using CMEK. Before you create a log bucket with CMEK enabled, review the Limitations.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. Configure the Google Cloud project where you plan to create your keys:

     1. To get the permissions that you need to create keys, ask your administrator to grant you the [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on the project or a parent resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

     2. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com).

     3. [Create a key ring and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

Cloud Logging lets you use a key from any region. However, when you create a log bucket, the location of the log bucket must match the location of the key. For information about supported regions, see the following:

        * [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations)
        * [Logging Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions)

You can't enable CMEK for log buckets created in the `global` region.

  4. Ensure that you have the following Cloud Logging permissions on the Google Cloud project where you plan to create log buckets:

     * `logging.settings.get`
     * `logging.buckets.get`
     * `logging.buckets.list`
     * `logging.buckets.create`
     * `logging.buckets.update`



## Enable CMEK

After you've completed the prerequisite steps, follow these instructions to enable CMEK for an individual log bucket.

### Determine the service account ID

To determine the service account ID associated with the Google Cloud resource for which CMEK will apply, do the following:

  1. Run the following [`gcloud logging settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/describe) command:
         
         gcloud logging settings describe --project=BUCKET_PROJECT_ID
         

Before running the previous command, make the following replacement:

     * BUCKET_PROJECT_ID: Name of the Google Cloud project where you plan to create the log bucket.

The previous command generates a service account for the specified resource, when one doesn't exist already, and it returns the ID of that service account in the `kmsServiceAccountId` field:
    
    kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    name: projects/BUCKET_PROJECT_ID/settings
    

The `kmsServiceAccountId` field lists the service account that is used by Cloud Logging to call Cloud Key Management Service.

  2. If the KMS_SERVICE_ACCT_NAME field has the format of `cmek-pPROJECT_NUMBER`, and if you are using VPC Service Controls or if you [enable domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), then determine whether you need to migrate your CMEK service account. For information about when you need to migrate and the steps to perform the migration, see [Troubleshoot VPC Service Controls and domain restricted sharing](https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs#troubleshoot-vpc-sc-drs).




### Assign the Encrypter/Decrypter role

When you're configuring CMEK at the log bucket level, give the service account permission to use your Cloud KMS by assigning the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role to the service account identified by the `kmsServiceAccountId` field:
    
    
    gcloud kms keys add-iam-policy-binding \
    --project=KMS_PROJECT_ID \
    --member=serviceAccount:KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
    --location=KMS_KEY_LOCATION \
    --keyring=KMS_KEY_RING \
    KMS_KEY_NAME
    

Before running the previous command, make the following replacements:

  * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * KMS_SERVICE_ACCT_NAME: The name of the service account shown in the `kmsServiceAccountId` field of the response of the `gcloud logging settings describe` command.
  * KMS_KEY_LOCATION: The Cloud KMS key's region.
  * KMS_KEY_RING: The Cloud KMS key ring's name.
  * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.



### Create a log bucket and supply the Cloud KMS key

To create a log bucket and enable CMEK for the log bucket, run the following [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command:
    
    
    gcloud logging buckets create BUCKET_ID \
    --location=LOCATION \
    --cmek-kms-key-name=KMS_KEY_NAME \
    --project=BUCKET_PROJECT_ID
    

Before running the previous command, make the following replacements:

  * BUCKET_ID: The name or ID of the log bucket.
  * LOCATION: The location of the log bucket.
  * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.
  * BUCKET_PROJECT_ID: Name of the Google Cloud project where the log bucket will be created.



### Verify key enablement

To verify that you've successfully created a log bucket with CMEK enabled, run the following [`gcloud logging buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/list) command:
    
    
    gcloud logging buckets list --project=BUCKET_PROJECT_ID
    

Before running the previous command, make the following replacement:

  * BUCKET_PROJECT_ID: Name of the Google Cloud project that stores the log bucket.



In the tabular output, you see a column labeled `CMEK`. If the value of the `CMEK` column is `TRUE`, then CMEK is enabled for the log bucket.

To view the details for a specific log bucket, including the key's details, run this command:
    
    
    gcloud logging buckets describe BUCKET_ID --location=LOCATION --project=BUCKET_PROJECT_ID
    

## Manage your Cloud KMS key

The following sections describe how to update a log bucket to use the latest primary key version of a Cloud KMS key. They also describe how to change, revoke access for, and disable your Cloud KMS key.

**Caution:** If Logging loses access to the Cloud KMS key, there are data loss and user implications; to learn more, see Limitations on this page.

### Rotate your Cloud KMS key

**Note:** If you rotate a Cloud KMS key, that action doesn't apply to existing log buckets. That is, rotating the key doesn't change the key version that the log bucket uses to protect its data. For information about how to change the key version used by a log bucket, see Rotate your Cloud KMS key.

When you [create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/creating-keys), you can configure a rotation period. You can also [rotate a Cloud KMS key manually](https://docs.cloud.google.com/kms/docs/rotating-keys#manual). Each time a key is rotated, a new version for that key is created.

If you rotate a Cloud KMS key, then the new key version applies only to log buckets created after the key rotation. If the key is used by an existing log bucket, rotating the key doesn't change how the log bucket protects its data.

For example, suppose that you create a log bucket and enable CMEK, and then you rotate the Cloud KMS key. The log bucket that you created doesn't use the new key version, instead it continues to protect its data with the key version that was marked as primary when the log bucket was created.

To update a log bucket to use the most recent primary key version of a Cloud KMS key, do the following:

  1. Identify the current Cloud KMS key for the log bucket. For more information, see Verify key enablement.
  2. Identify another Cloud KMS key that you can use. If your key ring has only one key, then [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys).
  3. Change the Cloud KMS key for the log bucket to the Cloud KMS key created in the previous step.
  4. Change the Cloud KMS key for the log bucket to the original Cloud KMS key.



### Change your Cloud KMS key

To change the Cloud KMS key associated with your log bucket, [create a key](https://docs.cloud.google.com/kms/docs/creating-keys) and update the CMEK settings for log bucket:
    
    
    gcloud logging buckets update BUCKET_ID --location=LOCATION \
    --cmek-kms-key-name=NEW_KMS_KEY_NAME --project=BUCKET_PROJECT_ID
    

  * BUCKET_ID: The name or ID of the log bucket.
  * LOCATION: The location of the log bucket.
  * NEW_KMS_KEY_NAME: Name of the new key.
  * BUCKET_PROJECT_ID: Name of the Google Cloud project that stores the log bucket.



### Revoke access to the Cloud KMS key

**Caution:** If Logging loses access to the Cloud KMS key, there are data loss and user implications; to learn more, see Limitations on this page.

To revoke Logging's access to the Cloud KMS key at any time, remove the configured service account's IAM permission for that key.

If you remove Logging's access to a key, it can take up to one hour for the change to take effect.

If you have a [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset), BigQuery can't use this access to apply to key to a new BigQuery table. If you want to use a key on BigQuery table that aren't linked to Logging, follow [BigQuery's documentation](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption) to do so. If you revoke Logging's access to a key and if you have a [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset), then you also revoke BigQuery's access to the same key.

You can't revoke BigQuery's access to the linked BigQuery dataset's key while preserving Logging's access.

For more information about the impact of revoking access, see Limitations.

To remove Logging's access to a key, run the following command:
    
    
    gcloud kms keys remove-iam-policy-binding \
    --project=KMS_PROJECT_ID \
    --member=serviceAccount:KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
    --location=KMS_KEY_LOCATION \
    --keyring=KMS_KEY_RING \
    KMS_KEY_NAME
    

Before running the previous command, make the following replacements:

  * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * KMS_SERVICE_ACCT_NAME: The name of the service account shown in the `kmsServiceAccountId` field of the response of the `gcloud logging settings describe` command.
  * KMS_KEY_LOCATION: The Cloud KMS key's region.
  * KMS_KEY_RING: The Cloud KMS key ring's name.
  * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.



## Limitations

The following are known limitations.

### CMEK disables Error Reporting

If you want to use Error Reporting, then don't enable customer-managed encryption keys (CMEK) on your log buckets. For more information, see [Troubleshooting](https://docs.cloud.google.com/error-reporting/docs/troubleshooting).

### CMEK can't be removed from log buckets

You can't reconfigure log buckets to change or remove CMEK.

### Degradation due to Cloud KMS key unavailability

A Cloud KMS key is considered available and accessible by Logging if both of the following are true:

  * The key is [enabled](https://docs.cloud.google.com/kms/docs/key-states#enabled).
  * The Logging service account has encryption and decryption permissions on the key.

**Note:** If a key becomes unavailable, then Logging buffers the most recent three hours of logs. Logs older than this sliding three-hour window might be discarded. The Cloud KMS key must be available and accessible for at least 24 consecutive hours in the 48 hour period after log entries have been written for those logs to be persisted. If the Cloud KMS key isn't available and accessible, then log entries might not be fully persisted to storage and might be dropped. All logs are also unavailable for query until key access is repaired.

Logging strongly recommends ensuring that any keys are properly configured and always available.

#### Loss of disaster recovery

If there are critical failures in Cloud Logging primary storage, then Logging mirrors the logging data to disaster-recovery files. When CMEK is enabled for a resource, such as a Google Cloud organization, logs belonging to that resource are protected by the configured CMEK key. If the CMEK key isn't accessible, the disaster-recovery files can't be written for that resource.

Loss of disaster-recovery files doesn't affect normal logging operations. However, in the event of a storage disaster, Cloud Logging might be unable to recover logs from resources whose CMEK isn't properly configured.

#### Support constraints

[Cloud Customer Care](https://docs.cloud.google.com/support/docs) can't read your resource's logs if its key isn't properly configured or becomes unavailable.

#### Degraded query performance

When a customer-managed encryption key is inaccessible, Cloud Logging continues to encrypt your data and store data in log buckets. However, Cloud Logging can't perform background optimizations on this data. If key access is restored, the data becomes available; however, the data is initially be stored in an unoptimized state and query performance may suffer.

### Degradation due to Cloud EKM key unavailability

When you use a Cloud EKM key, Google Cloud has no control over the availability of your externally managed key in the external key-management partner system. For bucket-level CMEK, if an externally managed key is unavailable, Cloud Logging continues to store logs in log buckets but users aren't able to access those logs.

For more considerations, and potential alternatives, when using external keys, see the [Cloud External Key Manager documentation](https://docs.cloud.google.com/kms/docs/ekm#considerations).

### Regionality

When you create a log bucket and enable CMEK, you must use a key whose region matches the regional scope of your data. You can't configure CMEK for log buckets created in the `global` [region](https://docs.cloud.google.com/kms/docs/locations).

### Client library availability

Logging client libraries don't provide methods for configuring CMEK.

## Quotas

When you use CMEK in Logging, your projects can consume Cloud KMS cryptographic requests quotas. For example, enabling CMEK on a log bucket can consume these quotas. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

For details on Logging usage limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## Troubleshoot configuration errors

For information about troubleshooting CMEK configuration errors, see [Troubleshoot CMEK and organization setting errors](https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
