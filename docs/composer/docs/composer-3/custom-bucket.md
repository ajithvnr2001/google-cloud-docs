---
url: https://docs.cloud.google.com/composer/docs/composer-3/custom-bucket/
title: Use a custom environment's bucket \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:48.421075+00:00
---

# Use a custom environment's bucket  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/custom-bucket/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Use a custom environment's bucket Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/use-custom-bucket "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

You can specify a custom Cloud Storage bucket as an environment's bucket when you create an environment. Your environment uses this bucket in the same way as the [default environment's bucket](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage), and the default environment's bucket is not created.

With a custom bucket, you can:

  * Use a bucket configuration that is compliant with your requirements.
  * Use a continuously existing bucket for periodic development or testing purposes.
  * Reuse an existing bucket from a previous environment and keep CI/CD and data integrations.
  * Delete and re-create an environment without the need to transfer data between buckets.
  * Pre-populate the custom bucket with required data, such as your DAG files, and then create an environment.



## Before you begin

  * The custom bucket must be located in the same region as the environment. Multi-region and dual-region buckets are not supported.
  * The custom bucket and the environment must be in the same project.
  * The custom bucket must have the [Standard storage class](https://docs.cloud.google.com/storage/docs/storage-classes).
  * The custom bucket must have no [retention policies or retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock) applied to it.
  * The custom bucket must not have [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.
  * It is not possible to use the same custom bucket with several environments at the same time. Managed Airflow generates an error if the specified bucket is already used by another environment. It is possible to delete an environment and then use the same bucket for another environment.

  * Managed Airflow doesn't add any missing IAM permissions to the Cloud Storage bucket when it is used to create an environment. Make sure that the environment's service account has [permissions from the Composer Worker role](https://docs.cloud.google.com/composer/docs/composer-3/access-control) on the bucket.


**Warning:** Managed Airflow does not alter the encryption settings of a custom bucket and thus does not [encrypt it with a CMEK key](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption) (even if the project's policies require encryption). Specifically, the custom bucket's encryption is not changed if your environment uses CMEK encryption. Your custom bucket follows policies of the project that it belongs to. You can [manually encrypt](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) the environment's bucket with CMEK keys before you create an environment.

## Create an environment with a custom bucket

###  Console 

To specify a custom Cloud Storage bucket when you create an environment:

  1. On the **Create environment** page, in the **Advanced configuration** section, click **Show advanced configuration**.
  2. Select **Custom bucket**.
  3. In the **Bucket name** field, specify or select a bucket.



###  gcloud 

When you create an environment, the `--storage-bucket` argument specifies the environment's custom bucket.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --storage-bucket CUSTOM_STORAGE_BUCKET
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `CUSTOM_STORAGE_BUCKET`: the name of a Cloud Storage bucket. You can also specify the bucket URI (with the `gs://` prefix).



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-cental1 \
        --storage-bucket us-central1-example-bucket
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [StorageConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#StorageConfig) resource, specify a custom bucket for your environment.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "storageConfig": {
        "bucket": "CUSTOM_STORAGE_BUCKET"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `LOCATION`: the region where the environment is located.
  * `ENVIRONMENT_NAME`: the name of your environment.
  * `CUSTOM_STORAGE_BUCKET`: the name of a Cloud Storage bucket (without the `gs://` prefix).



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "storageConfig": {
        "bucket": "us-central1-example-bucket"
      }
    }
    

###  Terraform 

When you create an environment, the `bucket` field in the `storage_config` block specifies the environment's custom bucket.

**Caution:** If you change the value of this field for an existing environment, Terraform deletes the existing environment and creates it again.
    
    
    resource "google_composer_environment" "example" {
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      storage_config {
    
        bucket = CUSTOM_STORAGE_BUCKET
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `CUSTOM_STORAGE_BUCKET`: the name of a Cloud Storage bucket. You can also specify the bucket URI (with the `gs://` prefix).



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      storage_config {
    
        bucket = "gs://us-central1-example-bucket"
    
      }
    }
    

## What's next

  * [About the environment's bucket](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage)
  * [CMEK in Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption)
  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
