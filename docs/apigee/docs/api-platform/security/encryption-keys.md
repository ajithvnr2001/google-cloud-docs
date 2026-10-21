---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys/
title: About the Apigee encryption keys \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:07:23.869343+00:00
---

# About the Apigee encryption keys  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  About the Apigee encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** Apigee does not support [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm)

This section describes the types of encryption keys and how to create them.

During the Apigee setup process, you generate the following [Cloud Key Management Service](https://cloud.google.com/security/products/security-key-management) encryption keys:

Key Type | When Created | Description  
---|---|---  
Control plane encryption key |  Google Cloud console:

  * [ Step 3: Configure hosting and encryption (Subscription)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org)
  * [ Step 3: Configure hosting and encryption (Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)

Command line interface (CLI):

  * [ Step 5: Create an organization (Subscription and Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org)

|  When using [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), Apigee uses this key to encrypt Analytics data stored in BigQuery inside the tenant project.  Encrypts API proxies, Target Servers, Truststores and Keystores, analytic data, and anything else shared across runtimes.  Apigee will ask you to provide two control plane CMEK keys. This key, and an  API consumer data encryption key.  The control plane encryption key's location should match the control plane location.  **Warning:** Choose your key's location carefully. Once set, the key and key location cannot be changed.   
API consumer data encryption key |  Google Cloud console:

  * [ Step 3: Configure hosting and encryption (Subscription)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org)
  * [ Step 3: Configure hosting and encryption (Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)

Command line interface (CLI):

  * [ Step 5: Create an organization (Subscription and Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org)

|  When using [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), Apigee needs a single region key, in addition to the  control plane encryption key, that is used for services that are available only in a single region. For example, Dataflow, and Cloud SQL.  The API consumer data encryption key's location should be within the control plane location.  **Warning:** Choose your key's location carefully. Once set, the key and the key location cannot be changed.   
Runtime database encryption key |  Google Cloud console:

  * [ Step 3: Configure hosting and encryption (Subscription)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org)
  * [ Step 3: Configure hosting and encryption (Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)

Command line interface (CLI):

  * [ Step 5: Create an organization (Subscription and Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org)

|  Encrypts application data such as KVMs, cache, and client secrets, which is then stored in the database.  There is one runtime database encryption key per organization — all instances/regions in an organization share the same runtime database encryption key.  The runtime database encryption key supports all Cloud KMS locations that support [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm). Google recommends using a [ multi-regional location](https://docs.cloud.google.com/kms/docs/locations#multi_regional) (such as `us` or `europe`) or [ dual-regional location](https://docs.cloud.google.com/kms/docs/locations#dual_regional) (`eur5`, `nam4`) when you create this key.  The runtime database encryption key's location should be within the control plane location when using [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).  **Warning:** Choose your key's location carefully. Once set, the key and the key location cannot be changed.   
Disk encryption key |  Google Cloud console:

  * [ Step 5: Configure hosting and encryption (Subscription)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-instance)
  * [ Step 3: Configure hosting and encryption (Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)

Command line interface (CLI):

  * [ Step 6: Create a runtime instance (Subscription and Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#runtime-instance)

|  Encrypts runtime instance data before it is written to disk.  The types of data encrypted include Key Management System (KMS); Key Value Maps (KVMs); quota definitions, buckets, and counters; and all cached data. KMS data includes API products, developers, developer apps, OAuth tokens (including access tokens, refresh tokens, and authorization codes), and API keys.  This key is located in the same region as the runtime instance; when creating a new key, match the key's location to your runtime instance's location.  Each instance/region combination has its own disk encryption key.   
  
## Key points

Keep the following in mind when creating the disk and runtime database encryption keys:

  * The location of the Apigee runtime database encryption key supports all Cloud KMS locations that support [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm). 
  * The disk encryption key's location must match the location of the runtime instance that the key is used in. 
  * Once set, you cannot change the location of either key.
  * All keys must be in a key ring.
  * Keys of different types must be in separate key rings; disk encryptions keys cannot be in the same key ring as your runtime database encryption key. 
  * The keys must have a `purpose`. If you use the command line to generate your new keys, set `purpose` to `encryption`. If you use the Google Cloud console, choose **Symmetric encrypt/decrypt** for the purpose. 
  * The keys are defined by a _key path_ , which uses the following pattern: 
        
        projects/PROJECT_ID/locations/KEY_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME




## Listing existing keys

If you already created new Cloud KMS encryption keys for Apigee, you can use those rather than create new keys during your setup.

To list all KMS keys in a key ring:

Execute the [ `gcloud kms keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list) command:
    
    
    gcloud kms keys list --keyring KEY_RING_NAME --location KEY_RING_LOCATION

Replace the following:

  * KEY_RING_NAME: the name of the key ring. For example, `my-key-ring`. 
  * KEY_RING_LOCATION: the physical location of the key ring, For example, `us-west1`. 



Alternatively, you can [ view your keys in the Google Cloud console](https://docs.cloud.google.com/kms/docs/view-keys-by-project#view-keys).

## Generating new keys on the command line

You can create a key ring and key on the command line or in the Google Cloud console.

Each type of key must have its own key ring. For example, your disk encryption keys can be stored in one key ring, but your runtime database encryption key must be stored in a separate key ring.

The following steps describe how to create a key ring and a key, and how to grant access for the Apigee Service Agent to use the new key. Create key rings and keys for the control plane (if using data residency), the runtime database, and the runtime disk.

  1. Create a new key ring using the [ `gcloud kms keyrings create`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings/create) command:

### Control plane

When [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is enabled, create a key ring for the control plane, and another for the consumer data region. 
         
         gcloud kms keyrings create CONTROL_PLANE_KEY_RING_NAME \
         --location CONTROL_PLANE_LOCATION \
         --project PROJECT_ID
         
         gcloud kms keyrings create CONSUMER_DATA_KEY_RING_NAME \
         --location CONSUMER_DATA_REGION \
         --project PROJECT_ID

Replace the following:

     * CONTROL_PLANE_KEY_RING_NAME: the control plane key ring name.
     * CONTROL_PLANE_LOCATION: the physical location at which Apigee control plane data will be stored.
     * PROJECT_ID: the Google Cloud project ID.
     * CONSUMER_DATA_KEY_RING_NAME: the consumer data key ring name.
     * CONSUMER_DATA_REGION: a sub-region of the control plane region. You must specify both the CONTROL_PLANE_LOCATION and the CONSUMER_DATA_REGION.

### Runtime database
    
    gcloud kms keyrings create RUNTIMEDB_KEY_RING_NAME \
      --location RUNTIMEDB_KEY_LOCATION \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDB_KEY_RING_NAME: the name of the database key ring you are creating.
     * RUNTIMEDB_KEY_LOCATION: the physical location of the database key ring.
     * PROJECT_ID: the Google Cloud project ID.

The Apigee encryption key's location supports all Cloud KMS locations that support [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm). 

### Runtime disk
    
    gcloud kms keyrings create RUNTIMEDISK_KEY_RING_NAME \
      --location RUNTIMEDISK_KEY_LOCATION \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDISK_KEY_RING_NAME: the name of the disk key ring you are creating.
     * RUNTIMEDISK_KEY_LOCATION: the physical location of the disk key ring.
     * PROJECT_ID: the Google Cloud project ID.

Verify that the disk key ring is set to the same location as the instance. Each instance and key ring should have its own location. 
    
    gcloud kms keyrings list \
    --location  \
    --project $PROJECT_ID
    
    gcloud kms keyrings describe **$DISK_KEY_RING_NAME** \
    --location  \
    --project $PROJECT_ID

The key ring's name must be unique to your organization. If you create additional regions, the key ring names for those regions cannot be the same as existing key ring names. 

  2. Create a key using the [ `kms keys create`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/create) command:

### Control plane

When [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is enabled, create a key ring for the control plane, and another for the consumer data region. 
         
         gcloud kms keys create CONTROL_PLANE_KEY_NAME \
         --keyring CONTROL_PLANE_KEY_RING_NAME \
         --location CONTROL_PLANE_LOCATION \
         --purpose "encryption" \
         --project PROJECT_ID
         
         gcloud kms keys create CONSUMER_DATA_KEY_NAME \
         --keyring CONSUMER_DATA_KEY_RING_NAME \
         --location CONSUMER_DATA_REGION \
         --purpose "encryption" \
         --project PROJECT_ID

Replace the following:

     * CONTROL_PLANE_KEY_NAME: the control plane key name.
     * CONTROL_PLANE_KEY_RING_NAME: the control plane key ring name.
     * CONTROL_PLANE_LOCATION: the physical location at which Apigee control plane data will be stored.
     * PROJECT_ID: the Google Cloud project ID.
     * CONSUMER_DATA_KEY_NAME: the consumer data key name.
     * CONSUMER_DATA_KEY_RING_NAME: the consumer data key ring name.
     * CONSUMER_DATA_REGION: a sub-region of the control plane region. You must specify both the CONTROL_PLANE_LOCATION and the CONSUMER_DATA_REGION.

### Runtime database
    
    gcloud kms keys create RUNTIMEDB_KEY_NAME \
      --keyring RUNTIMEDB_KEY_RING_NAME \
      --location RUNTIMEDB_KEY_LOCATION \
      --purpose "encryption" \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDB_KEY_NAME: the name of the database key you are creating.
     * RUNTIMEDB_KEY_RING_NAME: the name of the database key ring you are creating.
     * RUNTIMEDB_KEY_LOCATION: the physical location of the database key ring.
     * PROJECT_ID: the Google Cloud project ID.

### Runtime disk
    
    gcloud kms keys create RUNTIMEDISK_KEY_NAME \
      --keyring RUNTIMEDISK_KEY_RING_NAME \
      --location RUNTIMEDISK_KEY_LOCATION \
      --purpose "encryption" \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDISK_KEY_NAME: the name of the disk key you are creating.
     * RUNTIMEDISK_KEY_RING_NAME: the name of the disk key ring you are creating.
     * RUNTIMEDISK_KEY_LOCATION: the physical location of the disk key ring.
     * PROJECT_ID: the Google Cloud project ID.

This command creates the key and adds it to the key ring.

When you refer to a key, use the key ID.

  3. Grant access for the Apigee Service Agent to use the new key using the [ `gcloud kms keys add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command:

### Control plane

When [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is enabled, create a key ring for the control plane, and another for the consumer data region. 
         
         gcloud kms keys add-iam-policy-binding CONTROL_PLANE_KEY_NAME \
         --location CONTROL_PLANE_LOCATION \
         --keyring CONTROL_PLANE_KEY_RING_NAME \
         --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com" \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
         --project PROJECT_ID
         
         
         gcloud kms keys add-iam-policy-binding CONSUMER_DATA_KEY_NAME \
         --location CONSUMER_DATA_REGION \
         --keyring CONSUMER_DATA_KEY_RING_NAME \
         --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com" \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
         --project PROJECT_ID
         

Replace the following:

     * CONTROL_PLANE_KEY_NAME: the control plane key name.
     * CONTROL_PLANE_LOCATION: the physical location at which Apigee control plane data will be stored.
     * CONTROL_PLANE_KEY_RING_NAME: the control plane key ring name.
     * PROJECT_NUMBER: the Google Cloud project number.
     * PROJECT_ID: the Google Cloud project ID.
     * CONSUMER_DATA_KEY_NAME: the consumer data key name.
     * CONSUMER_DATA_REGION: a sub-region of the control plane region. You must specify both the CONTROL_PLANE_LOCATION and the CONSUMER_DATA_REGION.
     * CONSUMER_DATA_KEY_RING_NAME: the consumer data key ring name.

### Runtime database
    
    gcloud kms keys add-iam-policy-binding RUNTIMEDB_KEY_NAME \
      --location RUNTIMEDB_KEY_LOCATION \
      --keyring RUNTIMEDB_KEY_RING_NAME \
      --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com \
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDB_KEY_NAME: the name of the database key you are creating.
     * RUNTIMEDB_KEY_RING_NAME: the name of the database key ring you are creating.
     * RUNTIMEDB_KEY_LOCATION: the physical location of the database key ring.
     * PROJECT_NUMBER: the Google Cloud project number.
     * PROJECT_ID: the Google Cloud project ID.

### Runtime disk
    
    gcloud kms keys add-iam-policy-binding RUNTIMEDISK_KEY_NAME \
      --location RUNTIMEDISK_KEY_LOCATION \
      --keyring RUNTIMEDISK_KEY_RING_NAME \
      --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com \
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
      --project PROJECT_ID

Replace the following:

     * RUNTIMEDISK_KEY_NAME: the name of the disk key you are creating.
     * RUNTIMEDISK_KEY_RING_NAME: the name of the disk key ring you are creating.
     * RUNTIMEDISK_KEY_LOCATION: the physical location of the disk key ring.
     * PROJECT_NUMBER: the Google Cloud project number.
     * PROJECT_ID: the Google Cloud project ID.

This command binds the key to the Apigee Service Agent.

On successful completion of this request, `gcloud` responds with something similar to the following: 
    
    Updated IAM policy for key [runtime].
    bindings:
    - members:
    - serviceAccount:service-1234567890@gcp-sa-apigee.iam.gserviceaccount.com
    role: roles/cloudkms.cryptoKeyEncrypterDecrypter
    etag: BwWqgEuCuwk=
    version: 1

If you receive an error like the following:
    
    INVALID_ARGUMENT: Role roles/cloudkms.cryptokms.cryptoKeyEncrypterDecrypter is not supported for this resource.

Be sure that you used the project number and not the project name in the service account email address. 

To verify that the key is bound to the Apigee Service Agent:
    
    gcloud kms keys get-iam-policy **$DISK_KEY_NAME** \
      --keyring **$DISK_KEY_RING_NAME** \
      --location  \
      --project $PROJECT_ID
    
    gcloud kms keys describe **$DISK_KEY_NAME** \
      --keyring **$DISK_KEY_RING_NAME** \
      --location  \
      --project $PROJECT_ID




## Generating new keys using the Google Cloud console

You can generate new keys using the console, as described in [ Create a symmetric encryption key](https://docs.cloud.google.com/kms/docs/create-key#create-symmetric).

When you use the console to create a new key:

  * For the runtime database encryption key, set the location to any Cloud KMS location that supports [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm). The UI does not let you choose any other location for the key, so it will match what you choose in the key ring. 
  * After you create the key, get the key path in the **Cryptographic keys** pane by clicking more_vert **More** next to the key and then selecting **Copy Resource Name**. 



## Get the key ID

When you refer to a Cloud Key Management Service resource using the Cloud KMS API or Google Cloud CLI, you use the resource ID. You can get the key ID with the [ `gcloud kms keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list) command:

### Control plane

When [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is enabled, there is a key ring for the control plane, and another for the consumer data region. 
    
    
    gcloud kms keys list \
    --location=CONTROL_PLANE_LOCATION \
    --keyring=CONTROL_PLANE_KEY_RING_NAME \
    --project=PROJECT_ID
    
    
    gcloud kms keys list \
    --location=CONSUMER_DATA_REGION \
    --keyring=CONSUMER_DATA_KEY_RING_NAME \
    --project=PROJECT_ID

The key ID has the following syntax (similar to a file path):
    
    
    projects/PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/CONTROL_PLANE_KEY_RING_NAME/cryptoKeys/CONTROL_PLANE_KEY_NAME

### Runtime database
    
    
    gcloud kms keys list \
    --location=RUNTIMEDB_KEY_LOCATION \
    --keyring=RUNTIMEDB_KEY_RING_NAME \
    --project=PROJECT_ID

The key ID has the following syntax (similar to a file path):
    
    
    projects/PROJECT_ID/locations/RUNTIMEDB_KEY_LOCATION/keyRings/RUNTIMEDB_KEY_RING_NAME/cryptoKeys/RUNTIMEDB_KEY_NAME

### Runtime disk
    
    
    gcloud kms keys list \
      --location=RUNTIMEDISK_KEY_LOCATION \
      --keyring=RUNTIMEDISK_KEY_RING_NAME \
      --project=PROJECT_ID

The key ID has the following syntax (similar to a file path):
    
    
    projects/PROJECT_ID/locations/RUNTIMEDISK_KEY_LOCATION/keyRings/RUNTIMEDISK_KEY_RING_NAME/cryptoKeys/RUNTIMEDISK_KEY_NAME

For example:
    
    
    NAME: projects/my-project/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-key
    PURPOSE: ENCRYPT_DECRYPT
    ALGORITHM: GOOGLE_SYMMETRIC_ENCRYPTION
    PROTECTION_LEVEL: SOFTWARE
    LABELS:
    PRIMARY_ID: 1
    PRIMARY_STATE: ENABLED

You can also get the key ID in the Google Cloud console. For more information, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[KVMs]: Key Value Maps
