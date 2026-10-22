---
url: https://docs.cloud.google.com/oracle/database/docs/use-cmek/
title: Use CMEK \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:42.121904+00:00
---

# Use CMEK  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Use CMEK Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable Google Cloud CMEK with Oracle Database@Google Cloud. [Google Cloud CMEK](https://docs.cloud.google.com/oracle/database/docs/cmek#google-cloud-cmek-overview) uses [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) encryption keys.

**Important:** To enable CMEK on Exadata VM Clusters created before October 1, 2025, and Exascale VM Clusters created before July 30, 2026, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

## Before you begin

Ensure that the following requirements are met before enabling Google Cloud CMEK on an Oracle Database@Google Cloud resource:

  * Enable the Cloud Key Management Service API for the project that will store your encryption keys. [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)
  * Have the following Identity and Access Management (IAM) permissions to work with Cloud KMS keys:

    * To create new encryption key rings and keys:

      * `cloudkms.keyRings.create`
      * `cloudkms.cryptoKeys.create`
      * `cloudkms.cryptoKeys.get`
      * `cloudkms.cryptoKeys.list`
      * `cloudkms.locations.get`
    * To give Oracle Database@Google Cloud service accounts access to Cloud KMS keys:

      * `cloudkms.cryptoKeys.setIamPolicy`
    * To work with key versions:

      * `cloudkms.cryptoKeyVersions.get`
      * `cloudkms.cryptoKeyVersions.create`
      * `cloudkms.cryptoKeyVersions.list`
      * `cloudkms.cryptoKeyVersions.useToDecrypt`
      * `cloudkms.cryptoKeyVersions.useToEncrypt`
      * `cloudkms.cryptoKeyVersions.manageRawAesCbcKeys`

The `Cloud KMS Admin` role contains the required permissions. For more information, see [Cloud KMS permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

For information about how to grant roles and permissions, see [Access control with IAM](https://docs.cloud.google.com/kms/docs/iam).

  * [Create a Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and a [key](https://docs.cloud.google.com/kms/docs/create-key#create-symmetric). Oracle Database@Google Cloud supports only multi-region symmetric keys.

  * Have sufficient permissions to work with Oracle Database@Google Cloud resources. For more information, see [Oracle Database@Google Cloud predefined roles](https://docs.cloud.google.com/oracle/database/docs/iam-overview#oracle-db-predefined).




## Workflow to enable Google Cloud CMEK

The workflow to enable Google Cloud CMEK for an Oracle Database@Google Cloud resource involves the following steps:

  1. Complete the prerequisites.
  2. Create the resource for which you want to enable the CMEK:

     * [Create an Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters)
     * [Create an Exascale VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-exascale-clusters)
     * [Create an Autonomous AI Database](https://docs.cloud.google.com/oracle/database/docs/create-databases)

Oracle Database@Google Cloud automatically creates a service account for your resource as a part of the provisioning process. For more information, see [About Service accounts](https://docs.cloud.google.com/oracle/database/docs/cmek#about_service_accounts).

  3. Grant the service account access to the key:

     * Enable CMEK on an Exadata VM Cluster
     * Enable CMEK on an Exascale VM Cluster
     * Enable CMEK on an Autonomous AI Database



## CMEK for Exadata VM Cluster

### Enable CMEK on an Exadata VM Cluster

To enable CMEK on an Exadata VM Cluster, do the following:

  1. Go to the **Dedicated infrastructure** page.

[Go to Dedicated infrastructure](https://console.cloud.google.com/oracle/exadata/)

  2. Select the **Exadata VM Clusters** tab.

  3. Click the name of the cluster for which you want to enable CMEK.

  4. Go to the **Google-managed service account** section and check the **Status**.

If the **Status** shows `Disconnected`, contact [Customer care](https://cloud.google.com/support-hub). If it shows `Connected` and a Principal ID, proceed with the next steps.

  5. Copy the Principal ID to be used in the subsequent steps.

The Principal ID generated during provisioning is unique to the Exadata VM Cluster and has no permissions set by default. To enable Oracle databases access to Google Cloud services, grant permissions to the principal ID by following the next steps.

  6. Go to the **Cloud KMS key management** page.

[Go to Cloud KMS key management](https://console.cloud.google.com/security/kms)

  7. Select the key ring to which your key belongs.

  8. Select the key to grant permissions.

  9. Click **Add principal**.

  10. In the **New principals** field, paste the Principal ID you had copied.

  11. Assign the following roles to the principal:

     * `Cloud KMS CryptoKey Encrypter/Decrypter`
     * `Cloud KMS Viewer`
  12. Click **Save**.




After completing these steps, go to your OCI console, and discover and register your keys for your database. For instructions, refer to the [Oracle documentation](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/gcp-kms-integration-for-oracle-database-at-google-cloud.html#GUID-72CDF433-3501-4FE9-9B1E-0041A50F6A89).

### View Exadata VM Cluster encryption details

To view encryption details of a Exadata VM Cluster, do the following:

  1. Go to the **Dedicated infrastructure** page.

[Go to Dedicated infrastructure](https://console.cloud.google.com/oracle/exadata/)

  2. Select the **Exadata VM Clusters** tab.

  3. Click the name of the cluster.

  4. On the **Cluster details** page, go to the **Google-managed service account**.

You can view the Principal ID and the key. You can view the encryption details of your databases in the OCI console. For more information, refer to the Oracle documentation.




### Rotate a key on a Exadata VM Cluster

For a database on your Exadata VM Cluster, you can rotate the key through the OCI console. Refer to the [Oracle documentation](https://docs.oracle.com/en-us/iaas/exadatacloud/doc/gcp-kms-integration-for-oracle-database-at-google-cloud.html#ECSCM-GUID-173067DE-7B75-4986-9AFF-5536C480D4C6).

## CMEK for Exascale VM Cluster

### Enable CMEK on an Exascale VM Cluster

To enable CMEK on an Exascale VM Cluster, do the following:

  1. Go to the **Exascale infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the cluster for which you want to enable CMEK.

  4. Go to the **Google-managed service account** section and check the **Status**.

If the **Status** shows `Disconnected`, contact [Customer care](https://cloud.google.com/support-hub). If it shows `Connected` and a Principal ID, proceed with the next steps.

  5. Copy the Principal ID to be used in the subsequent steps.

The Principal ID generated during provisioning is unique to the Exascale VM Cluster and has no permissions set by default. To enable Oracle databases access to Google Cloud services, grant permissions to the principal ID by following the next steps.

  6. Go to the **Cloud KMS key management** page.

[Go to Cloud KMS key management](https://console.cloud.google.com/security/kms)

  7. Select the key ring to which your key belongs.

  8. Select the key to grant permissions.

  9. Click **Add principal**.

  10. In the **New principals** field, paste the Principal ID you had copied.

  11. Assign the following roles to the principal:

     * `Cloud KMS CryptoKey Encrypter/Decrypter`
     * `Cloud KMS Viewer`
  12. Click **Save**.




After completing these steps, go to your OCI console, and discover and register your keys for your database. For instructions, refer to the [Oracle documentation](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/gcp-kms-integration-for-oracle-database-at-google-cloud.html#GUID-72CDF433-3501-4FE9-9B1E-0041A50F6A89).

### View Exascale VM Cluster encryption details

To view encryption details of an Exascale VM Cluster, do the following:

  1. Go to the **Exascale infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the cluster.

  4. On the **Cluster details** page, go to the **Google-managed service account**.

You can view the Principal ID and the key. You can view the encryption details of your databases in the OCI console. For more information, refer to the Oracle documentation.




### Rotate a key on an Exascale VM Cluster

For a database on your Exascale VM Cluster, you can rotate the key through the OCI console. Refer to the [Oracle documentation](https://docs.oracle.com/en-us/iaas/exadatacloud/doc/gcp-kms-integration-for-oracle-database-at-google-cloud.html#ECSCM-GUID-173067DE-7B75-4986-9AFF-5536C480D4C6).

## CMEK for Autonomous AI Database

### Enable CMEK on an Autonomous AI Database

When you create an Autonomous AI Database, it is encrypted with Oracle-managed keys by default.

To enable Google Cloud CMEK on your Autonomous AI Database, do the following:

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the database for which you want to configure CMEK.

  3. Go to the **Oracle-managed service account** section.

The service account for the Autonomous AI Database is managed by Oracle.

  4. Copy the Principal ID.

The Principal ID generated during provisioning is unique to the Autonomous AI Database and has no permissions set by default. To enable Oracle databases access to Google Cloud services, grant permissions to the principal ID by following the next steps.

  5. Go to the **Cloud KMS key management** page.

[Go to Cloud KMS key management](https://console.cloud.google.com/security/kms)

  6. Select the key ring to which your key belongs.

  7. Select the key to grant permissions.

  8. Click **Add principal**.

  9. In the **New principals** field, paste the Principal ID you had copied.

  10. Assign the following roles to the principal:

     * `Cloud KMS CryptoKey Encrypter/Decrypter`
     * `Cloud KMS Viewer`
  11. Click **Save**.

  12. Once again, go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  13. Click the name of your database.

  14. Go to the **Encryption** section.

  15. Click **Manage**.

  16. Select **Google Cloud customer-managed key**.

  17. Select your key or enter it manually.

  18. Click **Save**.




### View Autonomous AI Database encryption details

To view encryption details for your Autonomous AI Database, do the following:

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the database.

  3. Go to the **Encryption** section.

You can view the encryption type and the encryption key, including a link to its Cloud KMS details page.




### Rotate a key on an Autonomous AI Database

To rotate a key for an Autonomous AI Database which is encrypted with Google Cloud CMEK, do the following:

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the database for which you want to rotate the key.

  3. Go to the **Encryption** section.

  4. Click **Manage**.

  5. On the **Manage encryption key** page, select a new key or enter one manually.

**Note:** You must assign a new key for rotation. Cloud KMS key versioning is not supported for Autonomous AI Database.
  6. Click **Save**.




## Decrypt a resource

When you want to read an object encrypted with a CMEK, you can access the object as you normally would. During such a request, the service agent automatically decrypts the requested object as long as:

  * The service agent still has permission to decrypt using the key.
  * You have not disabled or destroyed the key.



If one of these conditions is not met, the service agent does not decrypt the data, and the request fails.

## Enable and disable a key

You can [enable a Cloud KMS key](https://docs.cloud.google.com/kms/docs/enable-disable#enable) which is in the disabled [state](https://docs.cloud.google.com/kms/docs/key-states). The resource's data becomes accessible as soon as this change propagates to your resource.

To disable a Cloud KMS key, you must first switch to Oracle-managed encryption. Then, you can [disable the Cloud KMS key](https://docs.cloud.google.com/oracle/database/docs/\(/kms/docs/enable-disable#disable\)).

For an Exadata VM Cluster, you can switch the encryption type through the OCI console. For more information, refer to the Oracle documentation.

Enabling or disabling a key can take [up to three hours to propagate](https://docs.cloud.google.com/kms/docs/consistency) to your resource.

## What's next

  * Learn about [Cloud KMS](https://docs.cloud.google.com/kms/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
