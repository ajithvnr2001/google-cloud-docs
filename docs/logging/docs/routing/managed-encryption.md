---
url: https://docs.cloud.google.com/logging/docs/routing/managed-encryption/
title: Configure CMEK for Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:42.575165+00:00
---

# Configure CMEK for Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/routing/managed-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure CMEK for Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and manage customer-managed encryption keys (CMEK) for [Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/overview) to meet your organization's compliance needs. For [organizations](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) and [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders), you can force new buckets to use CMEK by configuring default resource settings for Cloud Logging. When configured, Cloud Logging ensures that all new log buckets in the organization or folder are encrypted with a customer-managed key.

For organizations and folders, you can configure default resource settings for Cloud Logging. When you create new resources, those resources inherit the settings of their parent. For example, suppose you configure your organization's default resource settings for Cloud Logging to have a CMEK setting. With this configuration, any new `_Default` and `_Required` log buckets that are created in projects, folders, or billing accounts in your organization are encrypted with the default key. Further, if you create a custom log bucket in a resource that is a child of your organization, then the default key is automatically used unless you provide a different key when creating the log bucket.

The instructions in this guide use the Google Cloud CLI.

The information in this document doesn't apply to observability buckets. If you are interested in observability buckets, then see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## Overview

By default, Cloud Logging encrypts customer content at rest. Logging handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Logging. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Logging resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

When your default resource settings for Cloud Logging include a CMEK setting, the following occur:

  * New log buckets in the organization or folder are automatically encrypted with the configured key. However, you can change that key or create log buckets and specify a different key. For more information, see [Configure CMEK for log buckets](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).


  * If you use Observability Analytics and query multiple log buckets, then the default key might be used to encrypt temporary data. For more information, see [Observability Analytics restrictions](https://docs.cloud.google.com/logging/docs/log-analytics#restrictions).



## Before you begin

To get started, complete the following steps:

  1. Before you create a log bucket with CMEK enabled, review the Limitations.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. Configure the Google Cloud project where you plan to create your keys:

     1. To get the permissions that you need to create keys, ask your administrator to grant you the [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

     2. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com).

     3. [Create a key ring and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

Cloud Logging lets you use a key from any region. However, when you create a log bucket, the location of the log bucket must match the location of the key. For information about supported regions, see the following:

        * [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations)
        * [Logging Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions)

If your default resource settings for Cloud Logging include a CMEK setting, then new log buckets created in the organization or folder are automatically configured for CMEK. Also, because the location of a log bucket must match the location of the key, if your default resource settings for Cloud Logging include a CMEK setting, then you can't create log buckets in the `global` region.

  4. Ensure that your IAM role on the organization or folder whose default resource settings for Cloud Logging you want to configure includes the following Cloud Logging permissions:

     * `logging.settings.get`
     * `logging.settings.update`



## Enable CMEK for an organization or folder

Follow these instructions to enable CMEK for your Google Cloud folder or organization.

### Determine the service account ID

To determine the service-account ID associated with the organization or folder for which CMEK will apply, run the following [`gcloud logging settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/describe) command:

###  FOLDER 
    
    
     gcloud logging settings describe --folder=FOLDER_ID
    

Before running the previous command, make the following replacement:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).



###  ORGANIZATION 
    
    
    gcloud logging settings describe --organization=ORGANIZATION_ID

Before running the previous command, make the following replacement:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



The previous command generates service accounts for the organization or folder, when they don't exist. The command also returns the IDs of two service accounts, one in the `kmsServiceAccountId` field and the other in the `loggingServiceAccountId` field. To configure the default resource settings for Cloud Logging to have a CMEK setting, use the value in the `kmsServiceAccountId` field.

The following illustrates a sample response to the previous command when an organization is specified:
    
    
    kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    name: organizations/ORGANIZATION_ID/settings
    

Run the provisioning process one time per resource. Running the `describe` command multiple times returns the same value for the `kmsServiceAccountId` field.

If you can't use the Google Cloud CLI, then run the Cloud Logging API method [`getSettings`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings).

### Assign the Encrypter/Decrypter role

To use CMEK, give the service account permission to use your Cloud KMS by assigning the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role to the service account:

###  gcloud 
    
    
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



### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Select the name of the key ring that contains the key.

  3. Select the checkbox for the key.

The **Permissions** tab becomes available.

  4. In the **Add members** dialog, specify the email address of the Logging service account you are granting access.

  5. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  6. Click **Add**.




### Configure the organization policies

**Note:** You aren't required to configure an organization policy when you want to configure default resource settings for Cloud Logging. For information about organization policies and how to configure them, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

Logging supports organization policies that can require CMEK protection and can limit which Cloud KMS CryptoKeys can be used for CMEK protection:

  * When `logging.googleapis.com` is in the `Deny` policy list of services for the constraint `constraints/gcp.restrictNonCmekServices`, Logging refuses to create new user-defined buckets that aren't CMEK-protected. However, this constraint doesn't prevent Cloud Logging from creating the `_Required` and `_Default` log buckets which are created when a Google Cloud project is created.

  * When `constraints/gcp.restrictCmekCryptoKeyProjects` is enforced, Logging creates CMEK-protected resources that are protected by a CryptoKey from an allowed project, folder, or organization.




For more information about CMEK and organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

Make sure that your default resource settings for Cloud Logging are consistent with your organizational policies. For organizations and folders, if you plan to modify their default resource settings for Cloud Logging, before you update those settings, review and, if necessary, update organization policies.

To view or configure organization policies, do the following:

  1. In the Google Cloud console, go to the **Organization Policies** page: 

[Go to **Organization Policies**](https://console.cloud.google.com/projectselector/iam-admin/orgpolicies?supportedpurview=project,folder,organizationId)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select your organization.
  3. Verify, and if necessary, update the constraints specific to CMEK.

For information about how to modify an organization policy, see [Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).




### Configure Cloud Logging with the Cloud KMS key

To update the default resource settings for Cloud Logging to have a CMEK setting, run the following [`gcloud logging settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update) command:

###  FOLDER 
    
    
    gcloud logging settings update \
        --folder=FOLDER_ID \
        --kms-location=KMS_KEY_LOCATION \
        --kms-key-name=KMS_KEY_NAME \
        --kms-keyring=KMS_KEY_RING \
        --kms-project=KMS_PROJECT_ID
    

Before running the previous command, make the following replacements:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
  * KMS_KEY_LOCATION: The Cloud KMS key's region.
  * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.
  * KMS_KEY_RING: The Cloud KMS key ring's name.
  * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



The previous command updates the default resource settings for Cloud Logging to store information about the Cloud KMS key. You must ensure that the [default storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the folder is set to the value of the KMS_KEY_LOCATION. If you haven't set the default storage location, or if the value of that location doesn't match the value of KMS_KEY_LOCATION, then append the following to the previous command:
    
    
    --storage-location=KMS_KEY_LOCATION
    

The `--storage-location` flag lets you set or update the default storage location for the folder.

###  ORGANIZATION 
    
    
    gcloud logging settings update \
        --organization=ORGANIZATION_ID \
        --kms-location=KMS_KEY_LOCATION \
        --kms-key-name=KMS_KEY_NAME \
        --kms-keyring=KMS_KEY_RING \
        --kms-project=KMS_PROJECT_ID
    

Before running the previous command, make the following replacements:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * KMS_KEY_LOCATION: The Cloud KMS key's region.
  * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.
  * KMS_KEY_RING: The Cloud KMS key ring's name.
  * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



The previous command updates the default resource settings for Cloud Logging to store information about the Cloud KMS key. You must ensure that the [default storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the organization is set to the value of the KMS_KEY_LOCATION. If you haven't set the default storage location, or if the value of that location doesn't match the value of KMS_KEY_LOCATION, then append the following to the previous command:
    
    
    --storage-location=KMS_KEY_LOCATION
    

The `--storage-location` flag lets you set or update the default storage location for the organization.

After the key is applied, new log buckets in the organization or folder are configured to encrypt their data at rest using this key. You can also [change keys](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#change-key) for individual log buckets. You can't create log buckets in the `global` region because you must use a key whose region matches the regional scope of your data.

If you can't use the Google Cloud CLI, then run the Cloud Logging API method [`updateSettings`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/updateSettings).

### Verify key enablement

To verify that you've successfully enabled CMEK for an organization or a folder, run the following [`gcloud logging settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/describe) command:

###  FOLDER 
    
    
    gcloud logging settings describe --folder=FOLDER_ID

Before running the previous command, make the following replacement:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).



###  ORGANIZATION 
    
    
    gcloud logging settings describe --organization=ORGANIZATION_ID

Before running the previous command, make the following replacement:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



When the previous command returns the Cloud KMS key name in the `kmsKeyName` field is populated, CMEK is enabled for the organization or folder:
    
    
    kmsKeyName: KMS_KEY_NAME
    kmsServiceAccountId: KMS_SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    loggingServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    

## Route logs to supported destinations

  * Cloud Logging log buckets can be configured to encrypt data with CMEK. For organizations and folders, if you configure their default resource settings for Cloud Logging with a CMEK setting, then new log buckets in the organization or folder automatically use CMEK. You can change the key of these log buckets and you can create log buckets that use a different KMS key than the one specified by the default resource settings for Cloud Logging.

For information about CMEK as applied to log buckets, including how to change keys and limitations when you enable CMEK on a log bucket, see [Configure CMEK for log buckets](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).



  * Cloud Storage supports CMEK for routing logs. For instructions about how to configure CMEK for Cloud Storage, see [Using customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

If data is lost due to key unavailability when routing logs data to Cloud Storage, then you can retroactively copy logs in bulk to Cloud Storage when those logs are also stored in a log bucket. For details, see [Copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs).



  * BigQuery, by default, encrypts customer content stored at rest. For details, see [Protecting data with Cloud Key Management Service keys](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).


  * Pub/Sub, by default, encrypts customer content stored at rest. For details, see [Configuring message encryption](https://docs.cloud.google.com/pubsub/docs/encryption).



## Manage your Cloud KMS key

The following sections explain how to change, revoke access for, or disable your Cloud KMS key.

**Note:** If Logging loses access to the Cloud KMS key, there are data loss and user implications; to learn more, see Limitations on this page.

### Change your Cloud KMS key

To change the Cloud KMS key associated with an organization or a folder, [create a key](https://docs.cloud.google.com/kms/docs/creating-keys), and then run the [`gcloud logging settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update) command and supply information about the new Cloud KMS key:

###  FOLDER 
    
    
    gcloud logging settings update \
        --folder=FOLDER_ID
        --kms-key-name=NEW_KMS_KEY_NAME
        --kms-location=NEW_KMS_KEY_LOCATION \
        --kms-keyring=NEW_KMS_KEY_RING \
        --kms-project=NEW_KMS_PROJECT_ID

You must ensure that the [default storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the folder is set to the value of the KMS_KEY_LOCATION. If you haven't set the default storage location, or if the value of that location doesn't match the value of KMS_KEY_LOCATION, then append the following to the previous command:
    
    
    --storage-location=NEW_KMS_KEY_LOCATION
    

###  ORGANIZATION 
    
    
    gcloud logging settings update \
        --organization=ORGANIZATION_ID
        --kms-key-name=NEW_KMS_KEY_NAME
        --kms-location=NEW_KMS_KEY_LOCATION \
        --kms-keyring=NEW_KMS_KEY_RING \
        --kms-project=NEW_KMS_PROJECT_ID

You must ensure that the [default storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the organization is set to the value of the KMS_KEY_LOCATION. If you haven't set the default storage location, or if the value of that location doesn't match the value of KMS_KEY_LOCATION, then append the following to the previous command:
    
    
    --storage-location=NEW_KMS_KEY_LOCATION
    

### Revoke access to the Cloud KMS key

You can revoke Logging's access to the Cloud KMS key by removing the configured service account's IAM permission for that key.

If you remove Logging's access to a key, then it can take up to one hour for the change to take effect.

To revoke Logging's access to the Cloud KMS key, run the following Google Cloud CLI command:
    
    
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



### Disable CMEK

**Note:** If, for an organization, you configure default resource settings for Cloud Logging, then any folders in that organization automatically inherit those settings. If you want a folder to have different settings, then for that folder, configure default resource settings for Cloud Logging. For example, to avoid a CMEK requirement for a folder, don't include that setting when configuring the default resource settings for Cloud Logging.

Disabling CMEK for an organization or a folder removes CMEK policy enforcement for future operations only; any previously applied configurations remain intact.

To disable CMEK on a resource that has CMEK configured as part of the default resource settings for Cloud Logging, run the following Google Cloud CLI command:

###  FOLDER 
    
    
    gcloud logging settings update --folder=FOLDER_ID --clear-kms-key

Before running the previous command, make the following replacement:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).



###  ORGANIZATION 
    
    
    gcloud logging settings update --organization=ORGANIZATION_ID --clear-kms-key

Before running the previous command, make the following replacement:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



If you want to destroy your key, see [Destroying and restoring key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

## Cloud KMS key rotation considerations

Cloud Logging doesn't automatically rotate the encryption key for temporary disaster recovery files when the Cloud KMS key associated with the Google Cloud organization or folder rotates. Existing recovery files continue to use the key version with which they were created. New recovery files use the current primary key version.

## Limitations

The following are known limitations when you configure your default resource settings for Cloud Logging to have a CMEK setting.

### Disaster recovery file unavailability

A Cloud KMS key is considered available and accessible by Logging when both of the following are true:

  * The key is [enabled](https://docs.cloud.google.com/kms/docs/key-states#enabled).
  * The service account listed in the `kmsServiceAccountId` field of the response of the `gcloud logging settings describe` command has encrypt and decrypt has permissions on the key.



If Logging loses access to the Cloud KMS key, then Logging is unable to write temporary disaster-recovery files and, for users, queries stop functioning. Query performance may remain degraded even after key access is restored.

Routing logs to Cloud Storage might also be affected because the Logging is unable to write temporary files required to facilitate the routing. If an error is encountered while encrypting or decrypting data, then a notification is sent to the Google Cloud project that contains the Cloud KMS key.

### Client library availability

Logging client libraries don't provide methods for configuring CMEK.

### Degradation due to Cloud EKM key unavailability

When you use a Cloud EKM key, Google has no control over the availability of your externally managed key in the external key-management partner system.

When the default resource settings for Cloud Logging include a CMEK setting, if the externally managed key is unavailable, then Cloud Logging continually retries accessing the key. Cloud Logging also buffers the incoming log data for up to one hour. After an hour, if Cloud Logging is still unable to access the externally managed key, then Cloud Logging begins dropping the data.

If CMEK is applied to a log bucket and if an externally managed key is unavailable, then Cloud Logging continues storing logs in log buckets, but users won't be able to access that data.

See the [Cloud External Key Manager documentation](https://docs.cloud.google.com/kms/docs/ekm#considerations) for more considerations, and potential alternatives, when using external keys.

### Limitations on log buckets

For limitations when you use CMEK with log buckets, see [Limitations](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#limits).

## Quotas

For details on Logging usage limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## Troubleshoot configuration errors

For information about troubleshooting CMEK configuration errors, see [Troubleshoot CMEK and default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
