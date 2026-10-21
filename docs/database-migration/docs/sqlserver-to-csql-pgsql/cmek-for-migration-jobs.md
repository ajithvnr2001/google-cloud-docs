---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/cmek-for-migration-jobs/
title: Use customer-managed encryption keys (CMEK) for continuous migrations \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:18.549899+00:00
---

# Use customer-managed encryption keys (CMEK) for continuous migrations  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/cmek-for-migration-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) for continuous migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how customer-managed encryption keys (CMEK) work with Database Migration Service migration jobs.

**Note:** To use this feature right away, see  Use CMEK. Also, for more-detailed information about CMEK, see [ Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). 

## Is CMEK right for you?

CMEK is intended for organizations that have sensitive or regulated data that requires them to manage their encryption keys.

## Google-managed encryption versus customer-managed encryption

The CMEK feature lets you use your own cryptographic keys for data transported by Database Migration Service. After adding CMEK, whenever an API call is made, Database Migration Service uses your key to access data.

CMEK, including software, hardware, and external keys, are all managed through the [ Cloud Key Management Service (KMS) API](https://docs.cloud.google.com/kms/docs/reference/rest).

## Which locations support CMEK-enabled Database Migration Service migration jobs?

CMEK is available in all Database Migration Service [ locations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/ip-allowlists-and-regions).

The Cloud Key Management Service key ring location must match the region of the destination database for your migration job. A multi-region or global region key **won't** work.

## Understand service accounts

When your Database Migration Service migration jobs have CMEK enabled, you need to use a service account to request key access from Cloud Key Management Service.

To use a CMEK on a project, you must have a service account and you must grant the key access to the service account. The service account must exist inside of the project. The service account is visible in all regions.

## Understand keys

In [ Cloud Key Management Service](https://docs.cloud.google.com/kms/docs), you need to create a keyring with a cryptographic key, set with a location. When you create a new migration job in Database Migration Service, you select this key to encrypt the migration job.

You need to know the key ID and key region when you create new migration jobs that use CMEK. You must put the destination databases in the same region as the CMEK associated with the migration job. You can create one project for both keys and destination databases, or different projects for each.

CMEK uses the following format:

`projects/[CMEK_ENABLED_PROJECT]/locations/[REGION]/keyRings/[RING_NAME]/cryptoKeys/[KEYNAME]`

If you disable the primary version of the CMEK, then Database Migration Service won't be able to use the key. As a result, the associated migration job changes its status to `FAILED`. For more information on migration job states, see [ Migration job statuses](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-statuses). 

## How do you make CMEK-encrypted data inaccessible permanently?

You have complete control over keys and data access. If you destroy a key version that's associated with a migration job in Database Migration Service, then Google can't get the data back. However, if you disable the key version, you can re-enable it to get the data back.

You might have situations where you want to permanently destroy data encrypted with CMEK. To do this, you destroy the CMEK version. You can't destroy the keyring or key, but you can destroy key versions of the key.

## Restrictions

The following restrictions apply when using CMEK:

  * You can't update CMEK on a running migration job.

  * Although you can use CMEK to encrypt data from the source database, you can't use these keys to encrypt any migration job metadata, such as the migration job ID, IP address of the source database, and so on.




## Use CMEK

Now that you understand CMEK, you're ready to set up a service account and keys for CMEK. In addition, you'll learn how to set up a migration job to use CMEK.

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install and initialize the Cloud SDK.](https://docs.cloud.google.com/sdk/docs/install)
  7. Make sure that you have the Database Migration Admin role assigned to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  8. Enable the Cloud Key Management Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  9. Enable the Database Migration Service API. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datamigration.googleapis.com)




### Workflow to create migration jobs in Database Migration Service with CMEK

  1. _gcloud and API users only:_ Make sure that you have a  service account for each project that requires CMEK. For more information, see  Create a service account.

  2. Create a keyring and key, and set the location for each key. The location is the Google Cloud region.

  3. Grant the key access to the service account.

  4. Copy or write down the key ID (`KMS_KEY_ID`) and location for the key, and the ID (`KMS_KEYRING_ID`) for the keyring. You need this information when granting the key access to the service account.

  5. Go to a project, [ create a migration job in Database Migration Service](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-migration-job), and use your CMEK in the **Advanced encryption options** section.




Your migration job in Database Migration Service is now enabled with CMEK.

### Create a service account

You need to create a service account for each project that requires CMEK.

To allow a user to manage service accounts, grant one of the following roles:

  * Service Account User (`roles/iam.serviceAccountUser`): Includes permissions to list service accounts, get details about a service account, and impersonate a service account.
  * Service Account Admin (`roles/iam.serviceAccountAdmin`): Includes permissions to list service accounts and get details about a service account. Also includes permissions to create, update, and delete service accounts, and to view or change the Database Migration Service policy on a service account.



Currently, you can use only `gcloud` commands to create the type of service account you need for CMEK.

To create a service account with `gcloud`, run the following command:
    
    
    gcloud beta services identity create \
    --service=datamigration.googleapis.com\
    --project=PROJECT_ID

The previous command returns a service account name. You use this service account name during the procedure in Grant the key access to the service account.

### Create a key

You can create the key in the same Google Cloud project as the migration job in Database Migration Service, or in a separate user project. The Cloud KMS key ring location must match the region of your destination database associated with the migration job. A multi-region or global region key isn't supported. If the regions don't match, then you can't create the migration job.

If you destroy the key version that Database Migration Service uses to encrypt data, the associated migration job changes its status to `FAILED`. For more information on migration job states, see [ Migration job statuses](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-statuses).Cloud KMS usage is subject to a [ quota](https://docs.cloud.google.com/kms/quotas). GKE calls the Cloud KMS API every time it performs a cryptographic operation. Confirm that you have enough quota to enable application-layer secrets encryption for your application.

To create a Cloud KMS key:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Cryptographic keys](https://console.cloud.google.com/security/kms/keyrings)

  2. Click **Create key ring**.
  3. Add a **Key ring name**. Note this name because you need it when granting the key access to the service account.
  4. Add a **Key ring location**.
  5. Click **Create**. The **Create key** page opens.
  6. Add a **Key name**.
  7. Select a **Purpose** (symmetric or asymmetric).
  8. Select a **Rotation period** and **Starting on date**.
  9. Click **Create**.
  10. On the **Keys** table, click the three dots in the last column, and select **Copy Resource ID** or write it down. This is the `KMS_KEY_ID`. You need the `KMS_KEY_ID` when granting the key access to the service account.



### gcloud

  1. Create a new key ring. 
         
         gcloud kms keyrings create KMS_KEYRING_ID \
         --location=REGION
           

Write down this name because you need it when granting the key access to the service account.
  2. Create a key on the key ring. 
         
         gcloud kms keys create KMS_KEY_ID \
         --location=REGION \
         --keyring=KMS_KEYRING_ID \
         --purpose=encryption
           

Write down this name because you need it when granting the key access to the service account.



### Grant the key access to the service account

You only need to perform this procedure if you're using `gcloud` or the API.

To grant access to the service account, use the following code:
    
    
    gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
    --location=REGION \
    --keyring=KMS_KEYRING_ID \
    --member=serviceAccount:service-PROJECT_NUMBER@datamigrationiam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

### Create a migration job in Database Migration Service with CMEK

When you [ create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-migration-job), you can use your CMEK to manage the encryption of your data.

## Disable and re-enable key versions

See the following topics:

  * [ Disable an enabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable)
  * [ Enable a disabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
