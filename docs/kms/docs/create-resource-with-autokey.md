---
url: https://docs.cloud.google.com/kms/docs/create-resource-with-autokey/
title: Create protected resources using Cloud KMS Autokey \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:29.925699+00:00
---

# Create protected resources using Cloud KMS Autokey  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/create-resource-with-autokey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Create protected resources using Cloud KMS Autokey Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create protected resources using keys created by Cloud KMS Autokey for encryption. For more information about Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

**Note:** `CreateKeyHandle` requests can intermittently complete slowly or time out after 8 minutes. If the request has timed out, retry the operation.

## Before you begin

Before you can create protected resources using Autokey, you must complete the following steps to prepare:

  1. If you don't already have a project where Autokey is enabled, then you must first complete the setup steps in [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey), and then return to this document.
  2. You need permissions to create resources in the chosen project. To find the specific roles required for each resource, see the service-specific documentation. You can find this documentation by locating the service in the [CMEK integrations table](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_integrations) and visiting the link for the type of resource that you want to create. No additional permissions are required to use Autokey to request keys on demand.



## Using Autokey with Compute Engine resources

Autokey creates a new key for each disk, image, and machine image in the same location as the resource that is being created.

Autokey doesn't create new keys for snapshots. Snapshots should use the same key used to encrypt the disk. If you create a snapshot using the Google Cloud console, the encryption key used by the disk is automatically applied to the snapshot. If you create a snapshot using the gcloud CLI, Terraform, or the Compute Engine API, you must identify the key used to encrypt the disk and use that key to encrypt the snapshot.

For more information about using CMEK with snapshots, see [Create a snapshot from a disk encrypted with CMEK](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create_snapshot).

### Create a protected Compute Engine resource

###  Console 

To create a disk, complete the following steps:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk** and enter the properties for the new disk.

  3. Under **Encryption** , select **Cloud KMS key**.

  4. For **Key type** , select **Cloud KMS with Autokey** , and then click **Request a new key**. A message indicates when your key has been successfully created and is ready for use.

  5. To finish creating the disk, click **Create**.




You can follow a similar process to create protected VM instance, image, and machine image resources.

###  Terraform 

The following Terraform sample creates a [key handle](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) and uses the returned key to protect a new persistent disk resource:
    
    
    resource "google_kms_key_handle" "my_key_handle" {
      provider               = google-beta
      project                = "RESOURCE_PROJECT_ID"
      name                   = "KEY_HANDLE"
      location               = "LOCATION"
      resource_type_selector = "compute.googleapis.com/Disk"
    }
    
    resource "google_compute_disk" "persistent_disk" {
      project = "RESOURCE_PROJECT_ID"
      name    = "DISK_NAME"
      type    = "pd-ssd"
      zone    = "ZONE"
      size    = 30
      physical_block_size_bytes = 4096
      disk_encryption_key {
        kms_key_self_link = google_kms_key_handle.my_key_handle.kms_key
      }
    }
    

Replace the following:

  * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
  * `KEY_HANDLE`: an ID to use for the key handle.
  * `LOCATION`: the location where you want to create the protected resource.
  * `DISK_NAME`: the name of the new disk.
  * `ZONE`: the zone of the protected resource. This must be a zone within the location where you are creating the resource. For example, if you are creating the resource in the location `us-central1`, the zone could be `us-central1-a`.



You can't delete `KeyHandle` resources. If you're using a create-and-destroy pattern, attempting to recreate a `KeyHandle` produces an `ALREADY_EXISTS` error. To avoid this issue, you can import a previously-created `KeyHandle`. For more information, see Create and destroy patterns in Terraform on this page.

###  REST 

  1. Request a new Cloud KMS key by creating a [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
         
         curl -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X POST https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles \
             -d '{"resource_type_selector": "RESOURCE_TYPE"}'
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `RESOURCE_TYPE`: the type of resource that you want to create—for example, `compute.googleapis.com/Disk`.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the `OPERATION_ID` from the output. You need this value to get the resource ID of the created key.

  2. Find the Cloud KMS key associated with the key handle:
         
         curl -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X GET https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `OPERATION_ID`: The identifier of the key handle request operation from the output of the previous step.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "RESOURCE_TYPE"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Autokey for this resource. You can use this resource ID the same way that you use the resource ID for any other Cloud KMS resource.

  3. Create an encrypted disk by using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create), with the `--kms-key` flag:
         
         gcloud compute disks create DISK_NAME \
           --kms-key projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME
         

Replace the following:

     * `DISK_NAME`: the name of the new disk.
     * `KEY_PROJECT_ID`: the project ID of the project where the key was created.
     * `LOCATION`: the location where you want to create the resource.
     * `KEY_NAME`: the name of the key returned in the output from the previous step.



## Using Autokey with Cloud Storage resources

Autokey creates a new key in the same location as the bucket. The key created by Autokey is assigned as the bucket default key.

Autokey doesn't create keys for objects. By default, objects created in a bucket use the bucket default key. If you want to encrypt an object using a key other than the bucket default key, you can create a CMEK and use that key when creating the object.

If you want to change the default key assigned to a bucket, you can use an existing CMEK, including keys created by Autokey.

### Create a protected Cloud Storage resource

###  Console 

  1. In the Google Cloud console, go to the **Create a bucket** page.

[Go to Create a bucket](https://console.cloud.google.com/storage/create-bucket)

  2. Follow the instructions to [Create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket) up to the instruction **Choose how to protect object data**.

  3. Under **Choose how to protect object data** , expand the **Data encryption** section, and then select **Cloud KMS key**.

  4. For **Key type** , select **Cloud KMS with Autokey** , and then click **Request a new key**. A message indicates when your key has been successfully created and is ready for use.

  5. To finish creating the bucket, click **Create**.




###  Terraform 

The following Terraform sample creates a [key handle](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) and uses the returned key to protect a new storage bucket:
    
    
    resource "google_kms_key_handle" "my_key_handle" {
      provider               = google-beta
      project                = "RESOURCE_PROJECT_ID"
      name                   = "KEY_HANDLE"
      location               = "LOCATION"
      resource_type_selector = "storage.googleapis.com/Bucket"
    }
    
    resource "google_storage_bucket" "simple_bucket_name" {
      name                        = "BUCKET_NAME"
      location                    = "LOCATION"
      force_destroy               = true
      project                     = "RESOURCE_PROJECT_ID"
      uniform_bucket_level_access = true
      encryption {
        default_kms_key_name      = google_kms_key_handle.my_key_handle.kms_key
      }
    }
    

Replace the following:

  * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
  * `KEY_HANDLE`: an ID to use for the key handle.
  * `LOCATION`: the location where you want to create the protected resource.
  * `BUCKET_NAME`: the name of the new bucket.



You can't delete `KeyHandle` resources. If you're using a create-and-destroy pattern, attempting to recreate a `KeyHandle` produces an `ALREADY_EXISTS` error. To avoid this issue, you can import a previously-created `KeyHandle`. For more information, see Create and destroy patterns in Terraform on this page.

###  REST 

  1. Request a new Cloud KMS key by creating a [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
         
         curl -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X POST https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles \
             -d '{"resource_type_selector": "RESOURCE_TYPE"}'
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `RESOURCE_TYPE`: the type of resource that you want to create—for example, `storage.googleapis.com/Bucket`.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the `OPERATION_ID` from the output. You need this value to get the resource ID of the created key.

  2. Find the Cloud KMS key associated with the key handle:
         
         curl -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X GET https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `OPERATION_ID`: The identifier of the key handle request operation from the output of the previous step.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "RESOURCE_TYPE"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Autokey for this resource. You can use this resource ID the same way you would use the resource ID for any other Cloud KMS resource.

  3. Create an encrypted bucket by using the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create), with the `--default-encryption-key` flag:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --location=LOCATION \
             --default-encryption-key=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME
         

Replace the following:

     * `BUCKET_NAME`: the name of the new bucket. The bucket name must follow the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `LOCATION`: the location where you want to create the bucket.
     * `KEY_PROJECT_ID`: the project ID of the project where the key was created.
     * `LOCATION`: the location where you want to create the resource.
     * `KEY_NAME`: the name of the key returned in the output from the previous step.



## Using Autokey with BigQuery resources

Cloud KMS is available in several editions of BigQuery. Make sure the edition of BigQuery that you are using is compatible with Cloud KMS before you try to use Autokey to protect BigQuery resources. For more information about BigQuery editions, see [Understand BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).

For each new dataset, Autokey creates a new key, in the same location as the resource itself, which becomes the dataset default key.

Autokey doesn't create keys for tables, queries, temporary tables, or models. By default, these resources are protected by the dataset default key. If you want to protect a resource in a dataset using a key other than the dataset default key, you can manually create a CMEK and use that key when creating the resource.

For queries and temporary tables that are not inside a dataset, use project default keys. Use a different project default key for each location in the project that contains BigQuery resources. For more information about using project default keys, see [Set a project default key](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#project_default_key).

For more information about using CMEK with BigQuery, see [Customer-managed Cloud KMS keys](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).

### Create a protected BigQuery resource

###  Console 

Before attempting to create a BigQuery dataset using Autokey, make sure you have the required permissions. For more information about creating datasets, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Follow the instructions to [Create a dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) until you get to **Advanced options > Encryption**.

  3. Under **Encryption** select **Cloud KMS key**.

  4. For **Key type** , select **Cloud KMS with Autokey** , and then click **Request a new key**. A message indicates when your key has been successfully created and is ready for use.

  5. To finish creating the dataset, click **Create dataset**.




### Terraform

The following Terraform sample creates a [key handle](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) and uses the returned key to protect a new dataset:
    
    
    resource "google_kms_key_handle" "my_key_handle" {
      provider               = google-beta
      project                = "RESOURCE_PROJECT_ID"
      name                   = "test-key-handle"
      location               = "LOCATION"
      resource_type_selector = "bigquery.googleapis.com/Dataset"
    }
    
    resource "google_bigquery_dataset" "dataset" {
      project                     = "RESOURCE_PROJECT_ID"
      dataset_id                  = "DATASET_ID"
      friendly_name               = "DATASET_NAME"
      description                 = "DATASET_DESCRIPTION"
      location                    = "LOCATION"
      default_table_expiration_ms = 3600000
    
      default_encryption_configuration {
        kms_key_name = google_kms_key_handle.my_key_handle.kms_key
      }
    }
    

Replace the following:

  * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
  * `LOCATION`: the location where you want to create the protected resource.
  * `DATASET_ID`: the ID to use for the new dataset.
  * `DATASET_NAME`: a human-friendly name for the new dataset.
  * `DATASET_DESCRIPTION`: a description for the new dataset.



You can't delete `KeyHandle` resources. If you're using a create-and-destroy pattern, attempting to recreate a `KeyHandle` produces an `ALREADY_EXISTS` error. To avoid this issue, you can import a previously-created `KeyHandle`. For more information, see Create and destroy patterns in Terraform on this page.

###  REST 

  1. Request a new Cloud KMS key by creating a [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
         
         curl -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X POST https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles \
             -d '{"resource_type_selector": "RESOURCE_TYPE"}'
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `RESOURCE_TYPE`: the type of resource that you want to create—for example, `bigquery.googleapis.com/Dataset`.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the `OPERATION_ID` from the output. You need this value to get the resource ID of the created key.

  2. Find the Cloud KMS key associated with the key handle:
         
         curl -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X GET https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `OPERATION_ID`: The identifier of the key handle request operation from the output of the previous step.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "RESOURCE_TYPE"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Autokey for this resource. You can use this resource ID the same way you would use the resource ID for any other Cloud KMS resource.

  3. Create an encrypted dataset by using the [`bq mk` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_mk), with the `--destination_kms_key` flag.
         
         bq --location=LOCATION mk \
             --dataset \
             --default_kms_key=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME \
             --default_table_expiration=TABLE_EXPIRATION \
             --description="DATASET_DESCRIPTION" \
             RESOURCE_PROJECT_ID:DATASET_ID
         

Replace the following:

     * `LOCATION`: the location where you want to create the dataset.
     * `KEY_PROJECT_ID`: the project ID of the project where the key was created.
     * `KEY_NAME`: the name of the key returned in the output from the previous step.
     * `TABLE_EXPIRATION`: the default lifetime for new tables in this dataset, in seconds.
     * `DATASET_DESCRIPTION`: a description for the new dataset.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `DATASET_ID`: the ID of the dataset that you're creating.

For more information about the `bq` tool, see [Explore the bq command-line tool](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool).




## Using Autokey with Secret Manager resources

Autokey creates a single key to protect all secrets in the same project and location. When the key rotates, new secrets added to the project use the new primary version of the key.

Secret Manager is only compatible with Cloud KMS Autokey when creating resources using Terraform or the REST API.

### Create a protected Secret Manager resource

### Terraform

The following Terraform sample creates a [key handle](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) and uses the returned key to protect a new secret with automatic replication:
    
    
    resource "google_kms_key_handle" "my_key_handle" {
      provider               = google-beta
      project                = "RESOURCE_PROJECT_ID"
      name                   = "test-key-handle"
      location               = "global"
      resource_type_selector = "secretmanager.googleapis.com/Secret"
    }
    
    resource "google_secret_manager_secret" "my_secret" {
      project   = "RESOURCE_PROJECT_ID"
      secret_id = "SECRET_ID"
    
      replication {
        auto {
          customer_managed_encryption {
            kms_key_name = google_kms_key_handle.my_key_handle.kms_key
          }
        }
      }
    }
    

Replace the following:

  * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
  * `SECRET_ID`: the ID to use for the new secret.



If you attempt to create a key handle for a secret in the same project and location for which a key handle already exists, an error message returns the details of the existing key handle. If this happens, make sure that you only have one block creating the key handle. You can reuse the key handle using its ID (`KEY_HANDLE`) to create additional secrets that should share the key.

You can't delete `KeyHandle` resources. If you're using a create-and-destroy pattern, attempting to recreate a `KeyHandle` produces an `ALREADY_EXISTS` error. To avoid this issue, you can import a previously-created `KeyHandle`. For more information, see Create and destroy patterns in Terraform on this page.

###  REST 

  1. Request a new Cloud KMS key by creating a [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
         
         curl -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X POST https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles \
             -d '{"resource_type_selector": "RESOURCE_TYPE"}'
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `RESOURCE_TYPE`: the type of resource that you want to create—for example, `secretmanager.googleapis.com/Secret`.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the `OPERATION_ID` from the output. You need this value to get the resource ID of the created key.

If you attempt to create a key handle for a secret in the same project and location for which a key handle already exists, an error message returns the details of the existing key handle. In this case, skip over the next step and use the key resource ID in the `existingKmsKey` field to protect your new secret.

  2. Find the Cloud KMS key associated with the key handle:
         
         curl -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X GET https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `OPERATION_ID`: The identifier of the key handle request operation from the output of the previous step.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "RESOURCE_TYPE"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Autokey for this resource. You can use this resource ID the same way you would use the resource ID for any other Cloud KMS resource.

  3. Create an encrypted secret with automatic replication by using the [`gcloud secrets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/create), with the `--kms-key-name` flag.
         
         gcloud secrets create "SECRET_ID" \
             --replication-policy "automatic" \
             --kms-key-name "projects/KEY_PROJECT_ID/locations/global/keyRings/autokey/cryptoKeys/KEY_NAME" \
             --project "RESOURCE_PROJECT_ID"
         

Replace the following:

     * `SECRET_ID`: the ID to use for the new secret.
     * `KEY_PROJECT_ID`: the project ID of the project where the key was created.
     * `KEY_NAME`: the name of the key returned in the output from the previous step.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.



## Using Autokey with Dataflow resources

Autokey can be used to create a single key for each Dataflow job.

###  REST 

  1. Request a new Cloud KMS key by creating a [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
         
         curl -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X POST https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles \
             -d '{"resource_type_selector": "dataflow.googleapis.com/Job"}'
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the `OPERATION_ID` from the output. You need this value to get the resource ID of the created key.

  2. Find the Cloud KMS key associated with the key handle:
         
         curl -H "X-Goog-User-Project: USER_PROJECT" \
             -H "Authorization: Bearer TOKEN" \
             -X GET https://cloudkms.googleapis.com/v1/projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
         

Replace the following:

     * `USER_PROJECT`: the project to be billed for charges associated with this request.
     * `RESOURCE_PROJECT_ID`: the project ID of the resource project where Autokey is enabled and where you want to create a protected resource.
     * `LOCATION`: the location where you want to create the protected resource.
     * `OPERATION_ID`: The identifier of the key handle request operation from the output of the previous step.

The output is similar to the following:
    
    {
      "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "RESOURCE_TYPE"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Autokey for this resource. You can use this resource ID the same way you would use the resource ID for any other Cloud KMS resource.




## Create-and-destroy patterns in Terraform

Cloud KMS doesn't let you delete `KeyHandle` resources. If you're using Terraform and a create-and-destroy pattern, attempting to recreate a `KeyHandle` produces an `ALREADY_EXISTS` error. You can avoid this issue by using an [`import`](https://developer.hashicorp.com/terraform/language/import#add-a-resource-block) block. Insert the following block before the `resource` block for the `google_kms_key_handle` resource:
    
    
    import {
      to = google_kms_key_handle.KEY_HANDLE
      id = "projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE"
    }
    

## What's next

  * Learn more about [when to use Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey).
  * Learn more about [how Autokey works](https://docs.cloud.google.com/kms/docs/autokey-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
