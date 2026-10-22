---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-cmek-encryption/
title: Configure encryption with customer-managed encryption keys \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:53.759304+00:00
---

# Configure encryption with customer-managed encryption keys  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-cmek-encryption/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure encryption with customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-cmek-encryption "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how to use [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to protect Managed Airflow environments.

### Data protected with CMEK encryption

Managed Airflow protects the following data with CMEK encryption:

  * Contents and schema of the Airflow database
  * Environment and Airflow task logs in Cloud Logging
  * Contents of the environment's bucket
  * Secrets stored in the environment's cluster
  * Persistent disks used by the task queue
  * Container images of environment components stored in Artifact Registry repositories



For specific details about how the data is encrypted, see:

  * [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/cmek) in the Cloud SQL documentation.
  * [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) and [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) in the Google Kubernetes Engine documentation.
  * [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) in the Cloud Storage documentation.
  * [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) in the Cloud Logging documentation.



### Data not protected with CMEK encryption

Cloud Monitoring does not support CMEK encryption. The name of your environment and names of DAGs are stored in the Monitoring database in the encrypted form using Google-owned and Google-managed encryption keys.

Managed Airflow stores the following information protected with Google-owned and Google-managed encryption keys, not customer-managed keys:

  * Environment name
  * Airflow configuration overrides
  * Environment variables

  * Descriptions of allowed IP ranges

  * IP ranges

  * Labels

  * The names of some parameters stored by Managed Airflow can include a sub-string of environment's name.




### Rotation of CMEK keys for Managed Airflow

After you configure encryption in your environment using CMEK keys, you might also want to consider rotating these keys on a regular basis as described in [KMS documentation](https://docs.cloud.google.com/kms/docs/key-rotation).

When you rotate a CMEK key, data encrypted with previous key versions is **not automatically re-encrypted** with the new key version. For more information, see [Re-encrypting data](https://docs.cloud.google.com/kms/docs/re-encrypt-data).

Specifically, this applies to:

  * Objects stored in the environment's bucket.
  * Data stored in the Airflow database.
  * All other data objects encrypted with CMEK in the Managed Airflow environment.
  * Container images of environment components stored in Artifact Registry repositories.



## Use a customer-managed encryption key for your environment

**Warning:** If you create an environment with a customer-managed encryption key and later disable or delete the key, the environment becomes **unusable**. It is **not possible to recover** an environment if its encryption key is deleted or disabled.

### Before you begin

  * You can configure CMEK only when you create an environment. It is not possible to enable CMEK for an existing environment.

  * Managed Airflow supports CMEK encryption using [keys stored in External Key Managers](https://docs.cloud.google.com/kms/docs/ekm).

  * You must create a CMEK key in the same region where your environments are located. You cannot use multi-regional or global keys.

  * If your environment runs inside a [VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc) perimeter, add the Cloud Key Management Service API and the Artifact Registry API to the perimeter.

  * If your environment runs inside a [VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc) perimeter, the project that hosts the Cloud Key Management Service keys must [belong to the same VPC Service Controls perimeter as the environment](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc#shared-vpc-cmek-perimeters).

  * Enable the Artifact Registry API.

###  Console 

Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

###  gcloud 

Enable the Artifact Registry API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable artifactregistry.googleapis.com




### Step 1. Create a customer-managed encryption key

Follow the steps outlined in [Creating symmetric encryption keys](https://docs.cloud.google.com/kms/docs/creating-keys) to create a key in the region where your environment is located.

### Step 2. Grant roles to service agents

**Important:** If your project has a [Domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) policy that excludes addresses from the google.com domain. You must turn off (or expand) this policy to grant the required roles to service agents. After you grant the roles, you can revert the policy changes. This policy does not affect the creation of environments. 

###  Console 

Skip this step. You grant permissions to [service agents](https://docs.cloud.google.com/iam/docs/service-agents) when you specify a key for your environment.

###  gcloud 

The following [service agents](https://docs.cloud.google.com/iam/docs/service-agents) must have the **Cloud KMS CryptoKey Encrypter/Decrypter** role on the key that you use for your environment.

Replace `PROJECT_NUMBER` with your [project's number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

Service agent name | Service account email | API service name  
---|---|---  
Managed Airflow Service Agent | service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com | composer.googleapis.com  
Artifact Registry Service Agent | service-PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com | artifactregistry.googleapis.com  
Kubernetes Engine Service Agent | service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com | container.googleapis.com | Pub/Sub Service Agent | service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com | pubsub.googleapis.com | Compute Engine Service Agent | service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com | compute.googleapis.com  | Cloud Storage Service Agent | service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com | Grant encrypt/decrypt permissions with `gcloud storage service-agent --authorize-cmek`

  1. (If required) If some of these service accounts are not present in your project, it means that an identity for this service is not yet created. This can happen, for example, if you did not yet create any Managed Airflow environments in your project. To add these service accounts, create identities for the listed services with the following command:
         
         gcloud beta services identity create \
           --service=API_SERVICE_NAME
         

Replace `API_SERVICE_NAME` with the [API service name](https://docs.cloud.google.com/apis/design/glossary#api_service_name) of a service that does not have a service account in your project. Example:
         
         gcloud beta services identity create \
           --service=composer.googleapis.com
         

  2. Grant permissions to service agents:
     1. Grant the role to Managed Airflow Service Agent:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member=serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com \
              --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project KEY_PROJECT_ID
            

     2. Grant the role to Artifact Registry Service Agent:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com \
              --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project KEY_PROJECT_ID
            

     3. Grant the role to GKE Service Agent:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member=serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
              --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project KEY_PROJECT_ID
            

     4. Grant the role to Pub/Sub Service Agent:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
              --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project KEY_PROJECT_ID
            

     5. Grant the role to Compute Engine Service Agent:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member=serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
              --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project KEY_PROJECT_ID
            

     6. Grant encrypt/decrypt permissions to Cloud Storage Service Agent. 
            
            gcloud storage service-agent \
              --authorize-cmek=projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
            

Replace:
     * `PROJECT_ID` with your [project's ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * `KEY_PROJECT_ID` with the ID of the project that stores your customer-managed key. If you use a key from another project, this value is different from your project's ID. If you use a key from the same project, this value is your project's ID.
     * `PROJECT_NUMBER` with your [project's number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * `KEY_LOCATION` with your customer-managed key location. This location must be the same as your environment's location.
     * `KEY_NAME` with your customer-managed key name.
     * `KEY_RING_NAME` with the keyring that stores your customer-managed key.
To get these values, you can run `gcloud projects describe`, `gcloud kms keyrings list`, and `gcloud kms keys describe` commands.



### Step 3. Create an environment with CMEK

After you create a customer-managed encryption key, you can use it to create Managed Airflow environments.

###  Console 

When you [create an environment](https://docs.cloud.google.com/composer/docs/composer-1/create-environments):

  1. Expand the **Networking, Airflow config overrides, and additional features** section. In the **Data encryption** section, select **Cloud Key Management Service key**.
  2. In the **Select a Cloud Key Management Service key** drop-down list, select your key.
  3. If additional setup is required, a message appears to inform you. In this case:
     1. Click **Open wizard**.
     2. In the **Prepare CMEK key for usage in Managed Airflow** dialog, view the list of [service agents](https://docs.cloud.google.com/iam/docs/service-agents) that must have the **Cloud KMS CryptoKey Encrypter/Decrypter** role on the key.
     3. To grant the required roles and permissions, click **Grant**.
**Important:** If your project has a [Domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) policy that excludes addresses from the google.com domain. You must turn off (or expand) this policy to grant the required roles to service agents. After you grant the roles, you can revert the policy changes. This policy does not affect the creation of environments. 



###  gcloud 

The `--kms-key` argument specifies a customer-managed enryption key for your environment. For more information about creating environments, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments). For example, you might want to specify other parameters for your environment.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
      --location LOCATION \
      --image-version IMAGE_VERSION \
      --kms-key projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `IMAGE_VERSION` with the name of the Managed Airflow image.
  * `KEY_PROJECT_ID` with the ID of the project where the key is located. If you use a key from another project, this value is different from your project's ID. If you use a key from the same project, this value is your project's ID.
  * `LOCATION` with the region where the environment is located.
  * `KEY_LOCATION` with the location of your customer-managed key. This location must be the same as your environment's location.
  * `KEY_NAME` with your customer-managed key name.
  * `KEY_RING_NAME` with the keyring that stores your customer-managed key.

Example:
    
    
    gcloud composer environments create example-environment \
      --location us-central1 \
      --image-version composer-1.20.12-airflow-1.10.15 \
      --kms-key projects/example-project/locations/us-central1/keyRings/example-key-ring/cryptoKeys/example-key
    

## View the environment's encryption configuration

You can view encryption configuration for an existing environment:

###  Console 

  1. In Google Cloud console, go to the **Environments** page. [Go to Environments](https://console.cloud.google.com/composer/environments)
  2. In the list of environments, click the name of your environment. The **Environment details** page opens.
  3. Go to the **Environment configuration** tab.
  4. Details about encryption are listed in the **Data encryption key** item.



###  gcloud 

Run the following `gcloud` command to view the encryption configuration
    
    
    gcloud composer environments describe \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --format="value(config.encryptionConfig)"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.

Example:
    
    
    gcloud composer environments describe \
      example-environment \
      --location us-central1 \
      --format="value(config.encryptionConfig)"
    

## Use CMEK for Managed Airflow logs

Cloud Logging supports encrypting Log storage with CMEK keys. We recommend to use the standard CMEK procedure for encrypting logs with CMEK keys. To encrypt logs with CMEK keys, follow the instructions outlined in [Manage the keys that protect Logging storage data](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage). **Deprecated:** The following instructions about redirecting Managed Airflow logs to a CMEK-encrypted Cloud Storage bucket are deprecated. If you use this approach in your project, consider switching to encrypting Log storage with CMEK keys instead.

### Redirect Managed Airflow logs to a CMEK-encrypted Cloud Storage bucket

If you expect your logs to contain sensitive data, you might want to redirect Managed Airflow logs to a CMEK-encrypted Cloud Storage bucket by using [Log Router](https://docs.cloud.google.com/logging/docs/routing/overview#log-router). Doing so prevents your logs from being sent to Monitoring. If you require support from Cloud Customer Care, you might need to grant Google support engineers access to the Managed Airflow logs stored in Cloud Storage. **Note:** [Audit logs](https://docs.cloud.google.com/logging/docs/audit) cannot be excluded. They are always sent to the default storage.

###  gcloud 

  1. Create a new Cloud Storage bucket to store the logs.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION
         

Replace:
     * `LOCATION` with the region where the environment is located.
     * `BUCKET_NAME` with the name for the bucket.
Example:
    
    gcloud storage buckets create gs://composer-logs-us-central1-example-environment --location=us-central1
    

  2. Encrypt the bucket with your CMEK key.
         
         gcloud storage buckets update gs://BUCKET_NAME \
           --default-encryption-key=projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         

Replace:
     * `KEY_PROJECT_ID` with the ID of the project where the key is located. If you use a key from another project, this value is different from your project's ID. If you use a key from the same project, this value is your project's ID.
     * `KEY_LOCATION` with the location of your customer-managed key. This location must be the same as your environment's location.
     * `KEY_RING_NAME` with the keyring that stores your customer-managed key.
     * `KEY_NAME` with your customer-managed key name.
     * `BUCKET_NAME` with the name of the bucket.
Example:
    
    gcloud storage buckets update gs://composer-logs-us-central1-example-environment \
      --default-encryption-key=projects/example-project/locations/us-central1/keyRings/example-key-ring/cryptoKeys/example-key
    

  3. Create a new log sink.
         
         gcloud logging sinks create \
         composer-log-sink-ENVIRONMENT_NAME \
         storage.googleapis.com/BUCKET_NAME \
         --log-filter "resource.type=cloud_composer_environment AND resource.labels.environment_name=ENVIRONMENT_NAME AND resource.labels.location=LOCATION"
         

Replace:
     * `ENVIRONMENT_NAME` with the name of the environment.
     * `LOCATION` with the region where the environment is located.
     * `BUCKET_NAME` with the name of the bucket.
Example:
    
    gcloud logging sinks create \
    composer-log-sink-example-environment \
    storage.googleapis.com/composer-logs-us-central1-example-environment \
    --log-filter "resource.type=cloud_composer_environment AND resource.labels.environment_name=example-environment AND resource.labels.location=us-central1"
    

  4. Grant the **Storage Object Creator** role to the service account for this bucket. The service account is shown in the result of the previous command).
         
         gcloud projects add-iam-policy-binding \
           PROJECT_ID \
           --member="serviceAccount:LOGGING_SERVICE_AGENT" \
           --role="roles/storage.objectCreator" \
           --condition=None
         

Replace:
     * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * `LOGGING_SERVICE_AGENT` with the Logging service agent account for this bucket. The name of this account is obtained on the previous step.
Example:
    
    gcloud projects add-iam-policy-binding \
      example-project \
      --member="serviceAccount:example-sa@gcp-sa-logging.iam.gserviceaccount.com" \
      --role="roles/storage.objectCreator" \
      --condition=None
    

  5. Exclude the logs for your new environment from Monitoring. 
         
         gcloud beta logging sinks update _Default \
           --add-exclusion name=ENVIRONMENT_NAME-exclusion,filter="resource.type=cloud_composer_environment AND resource.labels.environment_name=ENVIRONMENT_NAME AND resource.labels.location=LOCATION"
         

Replace:
     * `ENVIRONMENT_NAME` with the name of the environment.
     * `LOCATION` with the region where the environment is located.
Example:
    
    gcloud beta logging sinks update _Default \
      --add-exclusion name=example-environment-exclusion,filter="resource.type=cloud_composer_environment AND resource.labels.environment_name=example-environment AND resource.labels.location=us-central1"
    

  6. Add organization-level CMEK encryption to the Log Router.
         
         gcloud logging cmek-settings describe \
           --organization=ORGANIZATION_ID
         
         
         gcloud kms keys add-iam-policy-binding \
               --project=KEY_PROJECT_ID \
               --member LOGGING_SERVICE_AGENT \
               --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
               --location=KEY_LOCATION \
               --keyring=KEY_RING_NAME \
               KEY_NAME
         
         
         gcloud logging cmek-settings update \
           --organization=ORGANIZATION_ID \
           --kms-project=KEY_PROJECT_ID \
           --kms-keyring=KEY_RING_NAME \
           --kms-location=KEY_LOCATION \
           --kms-key-name=KEY_NAME
         

Replace:
     * `ORGANIZATION_ID` with your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * `KEY_PROJECT_ID` with the ID of the project where the key is located. If you use a key from another project, this value is different from your project's ID. If you use a key from the same project, this value is your project's ID.
     * `KEY_RING_NAME` with the keyring that stores your customer-managed key.
     * `KEY_LOCATION` with the location of your customer-managed key. This location must be the same as your environment's location.
     * `KEY_NAME` with your customer-managed key name.



## What's next

  * [Security overview](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview)
  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-20 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
