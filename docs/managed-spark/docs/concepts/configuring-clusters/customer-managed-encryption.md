---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption/
title: Customer managed encryption keys (CMEK) \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:34.147606+00:00
---

# Customer managed encryption keys (CMEK)  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Customer managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

When you use Managed Service for Apache Spark, cluster and job data is stored on persistent disks associated with the Compute Engine VMs in your cluster and in a Cloud Storage [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket). By default, this persistent disk and bucket data is encrypted using a Google-generated data encryption key (DEK) and [key encryption key (KEK)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys).

If you want to control and manage the key encryption key (KEK), you can use [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) (Google continues to control the data encryption key (DEK)). For more information on Google data encryption keys, see [Encryption at Rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

CMEK is different from Customer-Supplied Encryption Keys (CSEK), which is a feature that lets you specify the contents of the key encryption key. For more information, see [Customer-supplied encryption keys](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys).

## CMEK cluster data encryption

You can use customer-managed encryption keys (CMEK) to encrypt the following cluster data:

  * Data on persistent disks attached to Managed Service for Apache Spark cluster VMs
  * Job argument data submitted to your cluster, such as a query string submitted with a Spark SQL job
  * Cluster metadata, [job driver output](https://docs.cloud.google.com/managed-spark/docs/guides/job-output#job_driver_output), and other data written to your Managed Service for Apache Spark cluster [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket#create_your_own_staging_and_temp_buckets)

**Note:** You can also use CMEK with encryption of workflow template job arguments.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Cloud Key Management Service, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,cloudkms.googleapis.com,compute.googleapis.com,storage.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Dataproc, Cloud Key Management Service, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,cloudkms.googleapis.com,compute.googleapis.com,storage.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Create keys

To protect your Managed Service for Apache Spark resources with CMEK, you can automate the creation of keys or create keys manually.

### Automated key creation

Use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) to automate CMEK provisioning and assignment. Autokey generates key rings and keys on demand when resources are created. Service agents use the keys in encrypt and decrypt operations. If needed, Autokey creates the agents and grants the required Identity and Access Management (IAM) (IAM) roles to them. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

### Manual key creation

Follow these steps to manually create keys for CMEK encryption of cluster data:

  1. Create one or more keys using the [Cloud KMS](https://docs.cloud.google.com/kms/docs/creating-keys). The resource name, also called the resource ID of a key, which you use in the next steps, is constructed as follows: 
         
         projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         

Use the **Cryptographic Keys** page in the Google Cloud console to copy a key resource ID to the clipboard. ![Screenshot showing how to copy the key resource ID from the Cryptographic Keys page.](https://docs.cloud.google.com/static/managed-spark/images/key-resource-id.png) The key (CMEK) must be located in the same location as the encrypted resource. For example, the CMEK used to encrypt a resource in the `us-central1` region must also be located in the `us-central1` region.
  2. To ensure that each of the following service accounts, [Compute Engine Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent), [Cloud Storage Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-storage-service-agent), and [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-cloud-dataproc-service-agent), has the necessary permissions to protect resources by using Cloud KMS keys, ask your administrator to grant the [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role to each of the following service accounts, [Compute Engine Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent), [Cloud Storage Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-storage-service-agent), and [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-cloud-dataproc-service-agent), on your project. 

Example assignment of Cloud KMS CryptoKey Encrypter/Decrypter role to the Managed Service for Apache Spark service Agent service account using Google Cloud CLI:
         
         gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
         --member serviceAccount:service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

`KMS_PROJECT_ID`: the ID of your Google Cloud project that contains the Cloud KMS key.

`PROJECT_NUMBER`: the project number (not the project ID) of your Google Cloud project that runs Managed Service for Apache Spark resources.

  3. If the [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) is not attached to the [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-cloud-dataproc-service-agent), add the `serviceusage.services.use` permission to a custom role attached to the Managed Service for Apache Spark Service Agent service account.




## Create a cluster with CMEK

Pass the resource ID of your key when you create the Managed Service for Apache Spark cluster.

### gcloud CLI

  * To encrypt cluster persistent disk data using your key, pass the resource ID of your key to the `--gce-pd-kms-key` flag when you create the cluster. 
        
        gcloud dataproc clusters create CLUSTER_NAME \
            --region=REGION \
            --gce-pd-kms-key='projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME' \
            other arguments ...
            

You can verify the key setting from the `gcloud` command-line tool.
        
        gcloud dataproc clusters describe CLUSTER_NAME \
            --region=REGION
            

Command output snippet:
        
        ...
        configBucket: dataproc- ...
          encryptionConfig:
            **gcePdKmsKeyName:** projects/project-id/locations/region/keyRings/key-ring-name/cryptoKeys/key-name
        ...
            

  * To encrypt cluster persistent disk data and job argument data using your key, pass the resource ID of the key to the `--kms-key` flag when you create the cluster. See [Cluster.EncryptionConfig.kmsKey](/managed-spark/docs/reference/rest/v1/ClusterConfig#EncryptionConfig.FIELDS.kms_key) for a list of job types and arguments that are encrypted with the `--kms-key` flag. 
        
        gcloud dataproc clusters create CLUSTER_NAME \
            --region=REGION \
            --kms-key='projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME' \
            other arguments ...
              

You can verify key settings with the gcloud CLI `dataproc clusters describe` command. The key resource ID is set on `gcePdKmsKeyName` and `kmsKey` to use your key with the encryption of cluster persistent disk and job argument data.
        
        gcloud dataproc clusters describe CLUSTER_NAME \
            --region=REGION
              

Command output snippet:
        
        ...
        configBucket: dataproc- ...
          encryptionConfig:
          **gcePdKmsKeyName:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
          **kmsKey:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
        ...
            

You can use either the `--gce-pd-kms-key` or the `--kms-key` flag, but not both, to encrypt cluster data using your key.
  * To encrypt cluster metadata, job driver, and other output data written to your Managed Service for Apache Spark staging bucket in Cloud Storage: 
    * [Create your own bucket with CMEK](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys). When [adding the key to the bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key), use a key that you created in Step 1.
    * Pass the bucket name to the `--bucket` flag when you create the cluster.
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --bucket=CMEK_BUCKET_NAME \
        other arguments ...
            

You can also pass CMEK-enabled buckets to the `gcloud dataproc jobs submit` command if your job takes bucket arguments, as shown in the following `cmek-bucket` example:
    
    gcloud dataproc jobs submit pyspark gs://cmek-bucket/wordcount.py \
        --region=region \
        --cluster=cluster-name \
        -- gs://cmek-bucket/shakespeare.txt gs://cmek-bucket/counts
          

    * Managed Service for Apache Spark doesn't manage customer managed encryption keys on your Cloud Storage bucket.
    * Using a bucket with a customer managed encryption key can slow write times to large files.



### REST API

  * To encrypt cluster VM persistent disk data using your key, include the [ClusterConfig.EncryptionConfig.gcePdKmsKeyName](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#encryptionconfig) field as part of a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. 

You can verify the key setting with the gcloud CLI `dataproc clusters describe` command.
        
        gcloud dataproc clusters describe CLUSTER_NAME \
            --region=REGION
            

Command output snippet:
        
        ...
        configBucket: dataproc- ...
          encryptionConfig:
            **gcePdKmsKeyName:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
        ...
            

  * To encrypt cluster VM persistent disk data and job argument data using your key, include the `Cluster.EncryptionConfig.kmsKey` field as part of a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. See [Cluster.EncryptionConfig.kmsKey](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#EncryptionConfig.FIELDS.kms_key) for a list of job types and arguments that are encrypted with the `--kms-key` field. You can include either the `Cluster.EncryptionConfig.gcePdKmsKeyName` field or the `Cluster.EncryptionConfig.kmsKey` field, but not both, with your cluster creation request.

You can verify key settings with the gcloud CLI `dataproc clusters describe` command. The key resource ID is set on `gcePdKmsKeyName` and `kmsKey` to use your key with the encryption of cluster persistent disk and job argument data.
        
        gcloud dataproc clusters describe CLUSTER_NAME \
            --region=REGION
            

Command output snippet:
        
        ...
        configBucket: dataproc- ...
          encryptionConfig:
            **gcePdKmsKeyName:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
            **kmsKey:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
        ...
            

  * To encrypt cluster metadata, job driver, and other output data written to your Managed Service for Apache Spark staging bucket in Cloud Storage: 
    * [Create your own bucket with CMEK](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys). When [adding the key to the bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key), use a key that you created in Step 1.
    * Pass the bucket name to the [ClusterConfig.configBucket](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#FIELDS.config_bucket) field as part of a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --bucket=CMEK_BUCKET_NAME \
        other arguments ...
        

    * Managed Service for Apache Spark doesn't manage customer managed encryption keys on your Cloud Storage bucket.
    * Using a bucket with a customer managed encryption key can slow write times to large files.

You can also pass CMEK-enabled buckets to the `gcloud dataproc jobs submit` command if your job takes bucket arguments, as shown in the following `cmek-bucket` example:
    
    gcloud dataproc jobs submit pyspark gs://cmek-bucket/wordcount.py \
        --region=region \
        --cluster=cluster-name \
        -- gs://cmek-bucket/shakespeare.txt gs://cmek-bucket/counts
          




## Use CMEK with workflow template data

Managed Service for Apache Spark workflow template job argument data, such as the query string of a Spark SQL job, can be encrypted using CMEK. Follow steps 1, 2, and 3 in this section to use CMEK with your Managed Service for Apache Spark workflow template. See [WorkflowTemplate.EncryptionConfig.kmsKey](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#encryptionconfig) for a list of workflow template job types and arguments that are encrypted using CMEK when this feature is enabled.

  1. Create a key using the [Cloud KMS](https://docs.cloud.google.com/kms/docs/creating-keys). The resource name of the key, which you use in the next steps, is constructed as follows: 
         
         projects/project-id/locations/region/keyRings/key-ring-name/cryptoKeys/key-name
         

Use the **Cryptographic Keys** page of the Google Cloud console to copy a key resource ID to the clipboard. ![Screenshot showing how to copy the key resource ID from the Cryptographic Keys page.](https://docs.cloud.google.com/static/managed-spark/images/key-resource-id.png)
  2. To enable the Managed Service for Apache Spark service accounts to use your key:

     1. Assign the Cloud KMS `CryptoKey Encrypter/Decrypter` role to the [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service-agent). You can use the gcloud CLI to assign the role:
            
            gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
             --member serviceAccount:service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
            

Replace the following:

KMS_PROJECT_ID: the ID of your Google Cloud project that runs Cloud KMS. This project can also be the project that runs Managed Service for Apache Spark resources.

PROJECT_NUMBER: the project number (not the project ID) of your Google Cloud project that runs Managed Service for Apache Spark resources.

     2. Enable the Cloud KMS API on the project that runs Managed Service for Apache Spark resources.

     3. If the [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) is not attached to the [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service-agent), then add the `serviceusage.services.use` permission to the custom role attached to the Managed Service for Apache Spark Service Agent service account. If the Managed Service for Apache Spark Service Agent role is attached to the Managed Service for Apache Spark Service Agent service account, you can skip this step.

  3. You can use the gcloud CLI or the Dataproc API to set the key you created in Step 1 on a workflow. Once the key is set on a workflow, all the workflow job arguments and queries are encrypted using the key for any of the job types and arguments listed in [WorkflowTemplate.EncryptionConfig.kmsKey](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#encryptionconfig). 

### gcloud CLI

Pass resource ID of your key to the `--kms-key` flag when you create the workflow template with the [gcloud dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create) command.

**Example:**
         
         gcloud dataproc workflow-templates create my-template-name \
             --region=region \
             --kms-key='projects/project-id/locations/region/keyRings/key-ring-name/cryptoKeys/key-name' \
             other arguments ...
         

You can verify the key setting from the `gcloud` command-line tool. 
         
         gcloud dataproc workflow-templates describe TEMPLATE_NAME \
             --region=REGION
         
         
         ...
         id: my-template-name
         encryptionConfig:
         **kmsKey:** projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         ...
         

### REST API

Use [WorkflowTemplate.EncryptionConfig.kmsKey](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#encryptionconfig) as part of a [workflowTemplates.create request](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create).

You can verify the key setting by issuing a [workflowTemplates.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/get) request. The returned JSON contains the `kmsKey`:
         
         ...
         "id": "my-template-name",
         "encryptionConfig": {
           **"kmsKey": "projects/ project-id/locations/region/keyRings/key-ring-name/cryptoKeys/key-name"**
         },
         




## Cloud External Key Manager

[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) lets you protect Managed Service for Apache Spark data using keys managed by a [supported external key management partner](https://docs.cloud.google.com/kms/docs/ekm#supported_partners). The steps you follow to use Cloud EKM in Managed Service for Apache Spark are the same as those you use to [set up CMEK keys](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption#cmek_cluster_data_encryption), with the following difference: your key points to a URI for the **externally managed key** (see [Cloud EKM Overview](https://docs.cloud.google.com/kms/docs/ekm#overview)).

### Cloud EKM errors

When you use Cloud EKM, an attempt to create a cluster can fail due to errors associated with inputs, Cloud EKM, the external key management partner system, or communications between Cloud EKM and the external system. If you use the REST API or the Google Cloud console, errors are logged in [Cloud Logging](https://docs.cloud.google.com/logging). You can examine the failed cluster's errors from the **View Log** tab.

If you use [Cloud Shell](https://docs.cloud.google.com/shell) to create a cluster, errors are displayed in the Cloud Shell terminal and in Logging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
