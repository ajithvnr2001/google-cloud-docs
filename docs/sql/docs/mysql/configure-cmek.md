---
url: https://docs.cloud.google.com/sql/docs/mysql/configure-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:49.659044+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/configure-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek "View this page for the SQL Server database engine")

Customer-managed encryption keys (CMEK) let you protect Cloud SQL data at rest using your own cryptographic keys in Cloud Key Management Service. Controlling your own keys helps you satisfy regulatory compliance requirements and maintain direct oversight of key access policies and rotation schedules.

You can set up a service account and Cloud KMS keys, and then create a Cloud SQL instance that uses a manually created CMEK. To learn more about using customer-managed encryption keys with Cloud SQL, see [Overview of customer-managed encryption keys](https://docs.cloud.google.com/sql/docs/mysql/cmek).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Make sure you have the Cloud SQL Admin role on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  13. Enable the Cloud Key Management Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  14. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin)




## Workflow for creating a Cloud SQL instance with CMEK

  1. _gcloud and API users only:_ Create a service account for each project that requires customer-managed encryption keys.
  2. Create a key ring and key in the same Google Cloud region where you want to create the instance.
  3. _gcloud and API users only:_ Grant the service account access to the key.
  4. Make a note of the key ID (KMS_KEY_ID), key ring location (GCP_REGION), and key ring ID (KMS_KEYRING_ID).
  5. Go to a project and create a Cloud SQL instance with the following options: 
     1. The same location as the customer-managed encryption key
     2. The customer-managed key configuration
     3. The customer-managed encryption key ID



Your Cloud SQL instance is now enabled with CMEK.

## Create a service account

You need to create a service account for each project that requires customer-managed encryption keys.

To allow a user to manage service accounts, grant one of the following roles:

  * Service Account User (`roles/iam.serviceAccountUser`): Includes permissions to list service accounts, get details about a service account, and impersonate a service account.
  * Service Account Admin (`roles/iam.serviceAccountAdmin`): Includes permissions to list service accounts and get details about a service account. Also includes permissions to create, update, and delete service accounts, and to view or change the Cloud SQL for MySQL policy on a service account.



You can only use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands to create the type of service account you need for customer-managed encryption keys. If you are using the Google Cloud console, Cloud SQL automatically creates this service account for you.

### gcloud
    
    
    gcloud beta services identity create \
    --service=sqladmin.googleapis.com \
    --project=PROJECT_ID

### Terraform

To create a service account, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_service_identity). 
    
    
    resource "google_project_service_identity" "gcp_sa_cloud_sql" {
      provider = google-beta
      service  = "sqladmin.googleapis.com"
    }

#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

The previous command returns a service account name. You use this service account name during the procedure in Granting the service account access to the key.

## Create a key

**Note:** You can use an [externally managed key](https://docs.cloud.google.com/kms/docs/ekm) with CMEK using the Cloud EKM service to make the key available through Cloud KMS.

You can create the key in the same Google Cloud project as the Cloud SQL instance or in a separate user project. The Cloud KMS key ring location must match the region where you want to create Cloud SQL instance. A multi-region or global region key **will not** work. The Cloud SQL instance create request fails if the regions don't match.

**Warning:** Never delete the primary key version that you initially use when you create your instance. You can't restore the backup for the instance if the key version that was originally used when the instance was created is destroyed. Even when the key version is rotated, the original key version must be maintained. If it is destroyed, it can't be re-created.**Note:** Sometimes, a Cloud SQL instance enabled with CMEK has the Cloud KMS key hosted in a different cloud project. For this scenario, when you enable VPC-SC, you must add the KMS key hosting project to the security perimeter.**Note:** Cloud KMS usage is subject to a [quota](https://docs.cloud.google.com/kms/quotas). GKE calls the Cloud KMS API every time it performs a cryptographic operation. Confirm that you have enough quota to enable application-layer secrets encryption for your application.

To create a Cloud KMS key:

### Console

  1. In the Google Cloud console, go to the **Key management** page.

[Go to Key management](https://console.cloud.google.com/security/kms/keyrings)

  2. Click **Create key ring**.
  3. Add a **Key ring name**. Note this name because you need it when granting the service account access to the key.
  4. Select a **Key ring location**.
  5. Click **Create**. The **Create key** page opens.
  6. Add a **Key name**.
  7. For **Purpose** , select **Symmetric encrypt/decrypt**.
  8. Select a **Rotation period** and **Starting on date**.
  9. Click **Create**.
  10. On the **Keys** table, click the three dots in the last column, and select **Copy Resource ID** or write it down. This is the KMS_KEY_ID. You need the KMS_KEY_ID when granting the key access to the service account.



### gcloud

  1. Create a new key ring. 
         
         gcloud kms keyrings create KMS_KEYRING_ID \
         --location=GCP_REGION
           

Write down this name because you need it when granting the key access to the service account.
  2. Create a key on the key ring. 
         
         gcloud kms keys create KMS_KEY_ID \
         --location=GCP_REGION \
         --keyring=KMS_KEYRING_ID \
         --purpose=encryption
           

Write down this name because you need it when granting the key access to the service account.



### Terraform

To create a key ring, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_key_ring). 
    
    
    resource "google_kms_key_ring" "keyring" {
      provider = google-beta
      name     = "keyring-name"
      location = "us-central1"
    }

To create a key, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_crypto_key).
    
    
    resource "google_kms_crypto_key" "key" {
      provider = google-beta
      name     = "crypto-key-name"
      key_ring = google_kms_key_ring.keyring.id
      purpose  = "ENCRYPT_DECRYPT"
    }

Apply the Terraform configuration:
    
    
    terraform apply

## Grant service accounts access to the key

When you create a Cloud SQL instance with CMEK, the service account for the project that will contain your instance must be granted access to the key. If you use the Google Cloud console to create your instance, then the service accounts are automatically granted access to the key when you create the instance. If you use gcloud CLI or the API to create your instance, or if you encounter permission errors after creating your instance, then complete the following procedure.

To grant the service account access:

### Console

  1. In the Google Cloud console, go to the **Key management** page.

[Go to Key management](https://console.cloud.google.com/security/kms/keyrings)

  2. To select the project hosting the key, use the project selector.
  3. Click the name of the key ring.
  4. Click the name of the key.
  5. Click the **Permissions** tab.
  6. To open the panel, click **Grant access**.
  7. Enter the service account as the principal and select "Cloud KMS CryptoKey Encrypter/Decrypter" as the role.
  8. Click **Save**.



Alternatively, you can also grant it in the project IAM page.

[GO TO THE PROJECT IAM PAGE](https://console.cloud.google.com/iam-admin/iam)

### gcloud
    
    
    gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
    --location=GCP_REGION \
    --keyring=KMS_KEYRING_ID \
    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloud-sql.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

### Terraform

To grant access to the key, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_kms_crypto_key_iam#google_kms_crypto_key_iam_binding). 
    
    
    resource "google_kms_crypto_key_iam_binding" "crypto_key" {
      provider      = google-beta
      crypto_key_id = google_kms_crypto_key.key.id
      role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
    
      members = [
        "serviceAccount:${google_project_service_identity.gcp_sa_cloud_sql.email}",
      ]
    }

Apply the Terraform configuration:
    
    
    terraform apply

## Create a Cloud SQL instance with CMEK

**Note:** You can't enable customer-managed encryption keys on existing instances.

To create an instance with customer-managed encryption keys:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Choose the database engine.
  4. Enter a name for the instance. Do not include sensitive or personally identifiable information in your instance name; it is externally visible. You do not need to include the project ID in the instance name. This is created automatically where appropriate (for example, in the log files).
  5. Enter the password for the `'root'@'%'` user.
  6. Set the region for your instance. Place your instance in the same region as the resources that access it. In most cases, you don't need to specify a zone.
  7. In the **Configuration options** section, select all your configurations options until you reach **Machine type and storage**.
  8. Expand **Machine type and storage**.
  9. In the **Encryption** section, select **Customer-managed key**. 
  10. Select the KMS key from the dropdown menu or manually enter the KMS_KEY_ID. Only KMS keys in the same project and region as the instance are displayed. The primary key version of the key is used, so if a key version is provided in the key name, then it's trimmed. To choose a KMS key belonging to a different project but in the same region, select **Don't see your key? Enter key resource ID** and enter the KMS_KEY_ID captured earlier.
  11. If the service account does not have permission to encrypt/decrypt with the selected key, a message displays. If this happens, click **Grant** to grant the service account the `roles/cloudkms.cryptoKeyEncrypterDecrypter>` IAM role on the selected KMS key.
  12. Once the configuration options are selected, click **Create**.
  13. You see a message explaining the implications of using customer-managed encryption key. Read and acknowledge it to proceed further with instance creation. 



### gcloud
    
    
    gcloud sql instances create INSTANCE_NAME \
    --project=PROJECT_ID \
    --disk-encryption-key=KMS_KEY_ID \
    --database-version=VERSION \
    --tier=MACHINE_TYPE \
    --region=REGION \
    --root-password=INSERT-PASSWORD-HERE

### Terraform

To create an instance with CMEK, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "mysql_instance_with_cmek" {
      name                = "mysql-instance-cmek"
      provider            = google-beta
      region              = "us-central1"
      database_version    = "MYSQL_8_0"
      encryption_key_name = google_kms_crypto_key.key.id
      settings {
        tier = "db-n1-standard-2"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### REST v1

To create an instance with customer-managed encryption keys, pass `diskEncryptionConfiguration` to the command. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * region: The region
  * database-version: Emum version string (for example, MYSQL_8_0)
  * kms-resource-id: The ID you received from creating a key.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances

Request JSON body: 
    
    
    {
      "name":"instance-id",
      "region":"region",
      "databaseVersion": "database-version",
      "diskEncryptionConfiguration" :
      {
          "kmsKeyName" : "kms-resource-id"
      },
      "settings":
      {
         "backupConfiguration":
          {
             "binaryLogEnabled": true,
             "enabled":true
          }
       }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

This example uses [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert). 

### REST v1beta4

To create an instance with customer-managed encryption keys, pass `diskEncryptionConfiguration` to the command. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * region: The region
  * database-version: Emum version string (for example, MYSQL_8_0)
  * kms-resource-id: The ID you received from creating a key.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances

Request JSON body: 
    
    
    {
      "name":"instance-id",
      "region":"region",
      "databaseVersion": "database-version",
      "diskEncryptionConfiguration" :
      {
          "kmsKeyName" : "kms-resource-id"
      },
      "settings":
      {
         "backupConfiguration":
          {
             "binaryLogEnabled": true,
             "enabled":true
          }
       }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

This example uses [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert). 

## Create a backup for a CMEK-enabled instance

When you create a backup of a Cloud SQL instance, the backup is encrypted with the same primary key version as the primary instance's customer-managed key. If your instance uses a CMEK created by [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview), the backup still uses the same key as the primary instance; Autokey doesn't create keys for backups.

See [Creating and managing on-demand and automatic backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up).

You will see a message on the **Create a backup** form that says: "Your backup will be encrypted with the primary version of this instance's customer-managed encryption key. If anyone destroys or disables this key version, all backup data encrypted using that key version will be permanently lost. You can check the primary version for the key in Cloud KMS."

On the backups page, the list of backups enabled with customer-managed encryption keys have two extra columns. One column that shows that the backup is for a CMEK-enabled instance, and a column that displays the key version used to encrypt the backup.

## Create a replica for a CMEK-enabled instance

When you create a read replica of a Cloud SQL instance in the same region, it inherits the same customer-managed encryption key as the parent instance. If you create a read replica in a different region, you are given a new list of customer-managed encryption keys to select from. Each region uses its own set of keys.

See [Creating read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica).

On the **Create read replica** page, you see the following information:

  1. The **Encryption** shows **customer-managed**.
  2. The **Encryption key** for the replica is displayed.
  3. There is a message saying "Your replica will be encrypted with the primary instance's customer-managed key. If anyone destroys this key, all data encrypted with it will be permanently lost."



For a cross-region replica, you see the following message:

"Your cross-region replica will be encrypted with the selected customer-managed key. If anyone destroys this key, all data encrypted with it will be permanently lost."

## Create a clone of a CMEK-enabled instance

When you create a clone of Cloud SQL instance, it inherits the same customer-managed encryption key as the one used to encrypt the source instance.

See [Cloning instances](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).

On the **Create clone** page, you see the following information:

  1. The **Encryption** shows **customer-managed**.
  2. The **Encryption key** for the clone is displayed.
  3. There is a message saying "Your clone will be encrypted with the source instance's customer-managed key. If anyone destroys this key, all data encrypted with it will be permanently lost."



## View key information for a CMEK-enabled instance

Once you successfully create a Cloud SQL instance, you can look at the instance list or the instance overview page to see that it was created using a customer-managed encryption key. The details also show the key that was used to create the instance.

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the Instances list, scroll to the right until you see the **Encryption** column. In this column, you see **Google-managed** and **Customer-managed**.
  3. Click an instance name to open its **Overview** page. The customer-managed encryption key is listed in the **Configuration** pane.



## Re-encrypt an existing CMEK-enabled instance or replica

You can re-encrypt your existing Cloud SQL instances and replicas with the latest primary key version. When you re-encrypt instances that use Persistent Disk for their storage, the re-encryption is completed with zero downtime.

For more information about re-encrypting your existing CMEK-enabled instance or replica, see [About keys](https://docs.cloud.google.com/sql/docs/mysql/cmek#about_keys).

**Note:** Until re-encryption is completed, don't disable or destroy the existing key versions.

### Obtain the new primary key version

  * To re-encrypt your instance or replica with a new version, you'll need the new primary key version. If you need a new key version for your instances, you'll need to rotate your key using Cloud Key Management Service. To rotate your primary key, see [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key).

  * After your key rotation is complete, wait for the primary key change to be propagated before you re-encrypt your instances. If your key version change isn't consistent, your instance will continue to use the old key version after re-encryption. For more information, see [Consistency of key versions](https://docs.cloud.google.com/kms/docs/consistency#key_versions).




### Re-encrypt your CMEK-enabled instance

After key rotation is complete, re-encrypt your existing CMEK-enabled instance or replica. Re-encryption only requires downtime for instances that use the Google Cloud Hyperdisk Balanced storage option.

**Note:** If your new key version isn't consistent across Cloud SQL, the instance continues using the old key version after re-encryption.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Configuration** section, click **Re-encrypt instance**.
  4. In the dialog that appears, confirm your selection by clicking **Re-encrypt**.



### gcloud

To re-encrypt the instance or replica, run the following command: 
    
    
    gcloud sql instances reencrypt INSTANCE_NAME

Replace `INSTANCE_NAME` with name of the instance or replica you are re-encrypting. 

### REST v1

To re-encrypt your instance or replica with your new key, run the following command:
    
    
        POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2023-06-28T21:19:09.503Z",
      "operationType": "REENCRYPT",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To re-encrypt your instance or replica with your new key, run the following command: 
    
    
        POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/reencrypt" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2023-06-28T21:22:13.663Z",
      "operationType": "REENCRYPT",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### Automatic re-encryption backups

When you re-encrypt a primary instance that uses the Google Cloud Hyperdisk Balanced storage option, Cloud SQL automatically creates an on-demand backup called the re-encryption backup. Re-encryption backups aren't created for instances that use Persistent Disk for their storage.

In your [list of backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#viewbackups) for your Cloud SQL instance, the re-encryption backup is listed as type `on-demand` and labeled with `backup created automatically for data before CMEK re-encryption`.

As with other on-demand backups, re-encryption backups persist until you delete them or delete the instance.

### Re-encryption limitations

When you re-encrypt an instance, keep note of the following limitations:

  * You can't perform any other admin operations on the instance while the re-encryption operation is going on.
  * For instances that use the Google Cloud Hyperdisk Balanced storage option, the re-encryption operation triggers a downtime that depends on the instance or replica size.
  * Replicas of an instance aren't re-encrypted when an instance is en-encrypted. You need to re-encrypt each replica separately.
  * Backups aren't automatically re-encrypted with the new key version when you re-encrypt your instance. To restore the backup or point-in-time-recovery to a time after the backup is taken, you'll need to keep the Cloud KMS key version the backup is encrypted with.
  * Backups created after the Cloud KMS key that the instance is encrypted with is rotated will use the primary key version of that key automatically, even if the instance isn't encrypted with this key version.



For troubleshooting, see the [Re-encryption troubleshooting table](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#re-encryption-troubleshooting-table).

## Enhanced backups

When you use enhanced backups to protect a CMEK-enabled instance, your backups automatically use the same CMEK as the instance. You can only back up CMEK-enabled instances to a CMEK-enabled backup vault, however, the Cloud SQL backups in the backup vault will be encrypted using the CMEK inherited from the instance, not the vault key.

Before you can enable enhanced backups for your instance, you must complete the steps listed at [Back up Cloud SQL instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup).

**Caution:** If the Backup and DR Service service agent lacks the required permissions on the CMEK used by the instance, or if the CMEK is unusable, you can't associate the backup plan with the instance.

## Use Cloud External Key Manager (Cloud EKM)

To protect data in Cloud SQL instances, you can use keys that you manage within a supported external key management partner. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm), including the [Considerations](https://docs.cloud.google.com/kms/docs/ekm#considerations) section.

When you are ready to create a Cloud EKM key, see [Managing Cloud EKM keys](https://docs.cloud.google.com/kms/docs/ekm). After a key is created, provide the key name when you create a Cloud SQL instance.

You can use Key Access Justifications as part of Cloud EKM. Key Access Justifications lets you view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. To learn more, see [Overview of Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).

Thus, Key Access Justifications provides extra control over your data by providing a justification for each attempt to decrypt the data.

Google lacks control over the availability of keys in an external key management partner system.

**Warning:** If an external key is deleted or cannot be recovered, any Cloud SQL instances encrypted with that key become permanently inaccessible.

## Disable and re-enable key versions

See the following topics:

  * [Disable an enabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version)
  * [Enable a disabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version)



## Troubleshoot

This section describes things to try when you get an error message while setting up or using CMEK-enabled instances.

Cloud SQL administrator operations, such as create, clone, or update, might fail due to Cloud KMS errors, and missing roles or permissions. Common reasons for failure include a missing Cloud KMS key version, a disabled or destroyed Cloud KMS key version, insufficient IAM permissions to access the Cloud KMS key version, or the Cloud KMS key version is in a different region than the Cloud SQL instance. Use the following troubleshooting table to diagnose and resolve common problems. 

#### Customer-managed encryption keys troubleshooting table

For this error... | The issue might be... | Try this...  
---|---|---  
Per-product, per-project service account not found | The service account name is incorrect. | Make sure you created a service account for the correct user project.   
[GO TO THE SERVICE ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/serviceaccounts).   
Cannot grant access to the service account | The user account does not have permission to grant access to this key version. | Add the **Organization Administrator** role to your user or service account.   
[GO TO THE IAM ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/iam)  
Cloud KMS key version is destroyed | The key version is destroyed. | If the key version is destroyed, you cannot use it to encrypt or decrypt data.  
Cloud KMS key version is disabled | The key version is disabled. | Re-enable the Cloud KMS key version.   
[ GO TO THE CRYPTO KEYS PAGE](https://console.cloud.google.com/security/kms)  
Insufficient permission to use the Cloud KMS key | The `cloudkms.cryptoKeyEncrypterDecrypter` role is missing on the user or service account you are using to run operations on Cloud SQL instances, or the Cloud KMS key version doesn't exist. | In the Google Cloud project that hosts the key, add the `cloudkms.cryptoKeyEncrypterDecrypter` role to your user or service account.   
[GO TO THE IAM ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/iam)   
If the role is already granted to your account, see [Creating a key](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#key) to learn how to create a new key version. See note.  
Cloud KMS key is not found | The key version does not exist. | Create a new key version. See [Creating a key](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#key). See note.  
EKM key is unreachable | The External Key Manager (EKM) key is unreachable for several hours. Even after multiple retries, the EKM key remains unreachable.   
  
If your instance is suspended because a key is unavailable, but the key shows as active and available in the Google Cloud console, then the issue is likely your EKM connection or authentication. | Verify EKM connection status and troubleshoot the issue with your EKM provider. 

  * Ensure that Cloud KMS Data Access audit logs are enabled for your project.
  * To see the specific error returned by your EKM provider, search your Cloud Audit Logs for failed `Decrypt` operations.
  * Check your external key manager's internal logs (for example, Thales appliance logs) for connection drops or JSON Web Token (JWT) validation failures. Check your [network firewall rules](https://docs.cloud.google.com/kms/docs/ekm-partner/design/security) to ensure that your EKM is allowed to connect to the internet to download Google's public verification certificates.

  
[ GO TO THE CRYPTO KEYS PAGE](https://console.cloud.google.com/security/kms)  
Cloud SQL instance and Cloud KMS key version are in different regions | The Cloud KMS key version and Cloud SQL instance must be in the same region. It does not work if the Cloud KMS key version is in a global region or multi-region. | Create a key version in the same region where you want to create instances. See [Creating a key](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#key). See note.   
Cloud KMS key version is restored but the instance is still suspended a few minutes later. | The internal validation process for the instance can take up to 10 minutes before the instance becomes available again. | Wait for 10 minutes for the instance to become available.  
Cloud KMS key version is restored but the instance is still suspended more than 10 minutes later. | The key version is disabled or doesn't grant proper permissions. | Re-enable the key version, and grant the `cloudkms.cryptoKeyEncrypterDecrypter` role to your user or service account in the Google Cloud project that hosts the key.  
**Note:** If the instance is in a failed state during the `create` operation, you must delete it, add the role to the account you are using, and create a new instance with an active Cloud KMS key version. 

#### Re-encryption troubleshooting table

For this error... | The issue might be... | Try this...  
---|---|---  
CMEK resource re-encryption failed because the Cloud KMS key is inaccessible. Please ensure that the primary key version is enabled and the permission is granted properly. | The key version is disabled or doesn't grant proper permissions. | Re-enable the Cloud KMS key version: [ GO TO THE CRYPTO KEYS PAGE](https://console.cloud.google.com/security/kms) In the Google Cloud project that hosts the key, confirm the `cloudkms.cryptoKeyEncrypterDecrypter` role is granted to your user or service account: [GO TO THE IAM ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/iam)  
CMEK resource re-encryption failed due to server internal error. Please retry later | There is a server internal error. | Retry re-encryption. For more information, see [Re-encrypt an existing CMEK-enabled instance or replica](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#reencrypt)  
  
## What's next

  * [Configure access to the instance](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control).
  * [Connect to the instance with a client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).
  * [Create a database on the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases).
  * [Import data into the instance](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * [Create users on the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).
  * [Learn more about instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings).
  * Learn how to add [key access justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) to your keys.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
