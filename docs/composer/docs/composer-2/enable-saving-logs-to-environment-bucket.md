---
url: https://docs.cloud.google.com/composer/docs/composer-2/enable-saving-logs-to-environment-bucket/
title: Enable saving logs to the environment's bucket \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:33.078024+00:00
---

# Enable saving logs to the environment's bucket  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/enable-saving-logs-to-environment-bucket/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Enable saving logs to the environment's bucket Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/enable-saving-logs-to-environment-bucket "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page explains how to enable saving Airflow task logs to the environment's bucket for a new or existing environment.

As an option, you can enable the synchronization of task logs to the environment's bucket.

## About saving logs to the environment's bucket

Saving logs to the environment's bucket works in the following way:

  * **Disabled (default)** : Task logs are available in Cloud Logging. You can view them in Airflow UI and in Cloud Logging. Task log files aren't saved to the environment's bucket.

If saving logs to the environment's bucket was disabled and you enable it, task logs displayed in Airflow UI **don't show log entries** that were generated while logs were saved only to Cloud Logging. These logs aren't lost, they are still available in Cloud Logging.

  * **Enabled** : Task logs are saved both to Cloud Logging and to the environment's bucket. You can view them in Airflow UI and in Cloud Logging. Environment's bucket stores files with these logs.

If saving logs to the environment's bucket was enabled and you disable it, the logs that were already saved to the environment's bucket aren't deleted and remain stored in the bucket.




## Before you begin

  * Starting from Managed Airflow version 2.8.0, all environments don't store task logs in the environment's bucket by default. Task logs are still available in Cloud Logging and Airflow UI.

  * When you upgrade your environment, the configuration for saving logs in the environment's bucket is not changed. For example, if you upgrade an environment that saved logs to the environment's bucket to a later version, the environment keeps saving logs to the environment's bucket.

  * To enable or disable this option, you can use Google Cloud CLI, Cloud Composer API, or Terraform. It is not possible to change this option through Google Cloud console.




## Enable or disable saving task logs to the environment's bucket when creating an environment

###  gcloud 

When you create an environment, the following arguments specify how Airflow task logs must be saved:

  * `--disable-logs-in-cloud-logging-only` argument enables saving Airflow task logs to the environment's bucket.
  * `--enable-logs-in-cloud-logging-only` argument disables saving Airflow task logs to the environment's bucket. Logs are saved only to Cloud Logging.


    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --disable-logs-in-cloud-logging-only
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --disable-logs-in-cloud-logging-only
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) > [DataRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#dataretentionconfig) > [TaskLogsRetentionConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#tasklogsretentionconfig) resource, specify how Airflow task logs must be saved:

  * `CLOUD_LOGGING_AND_CLOUD_STORAGE` to save logs to the environment's bucket and Cloud Logging.
  * `CLOUD_LOGGING_ONLY` to save logs only in Cloud Logging.


    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "dataRetentionConfig": {
          "taskLogsRetentionConfig": {
            "storageMode": "CLOUD_LOGGING_AND_CLOUD_STORAGE"
          }
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "dataRetentionConfig": {
          "taskLogsRetentionConfig": {
            "storageMode": "CLOUD_LOGGING_AND_CLOUD_STORAGE"
          }
        }
      }
    }
    

###  Terraform 

When you create an environment, the `storage_mode` field in the `task_logs_retention_config` block specifies how Airflow task logs must be saved:

  * `CLOUD_LOGGING_AND_CLOUD_STORAGE` to save logs to the environment's bucket and Cloud Logging.
  * `CLOUD_LOGGING_ONLY` to save logs only in Cloud Logging.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        data_retention_config {
    
          task_logs_retention_config {
    
            storage_mode = "CLOUD_LOGGING_AND_CLOUD_STORAGE"
    
          }
        }
      }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        data_retention_config {
    
          task_logs_retention_config {
    
            storage_mode = "CLOUD_LOGGING_AND_CLOUD_STORAGE"
    
          }
        }
      }
    }
    

## Enable or disable saving task logs to the environment's bucket for an existing environment

###  gcloud 

When you update an environment, the following arguments enable or disable saving Airflow task logs to the environment's bucket:

  * `--disable-logs-in-cloud-logging-only` argument enables saving Airflow task logs to the environment's bucket. Logs are saved to the environment's bucket and to Cloud Logging.
  * `--enable-logs-in-cloud-logging-only` argument disables saving Airflow task logs to the environment's bucket. Logs are saved only to Cloud Logging.



To save Airflow logs in the environment's bucket:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --disable-logs-in-cloud-logging-only
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --disable-logs-in-cloud-logging-only
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.dataRetentionConfig.taskLogsRetentionConfig.storageMode` mask.

     2. In the request body, specify how Airflow task logs must be saved:

        * `CLOUD_LOGGING_AND_CLOUD_STORAGE` to save logs to the environment's bucket and Cloud Logging.
        * `CLOUD_LOGGING_ONLY` to save logs only in Cloud Logging.


    
    
    {
      "config": {
        "dataRetentionConfig": {
          "taskLogsRetentionConfig": {
            "storageMode": "CLOUD_LOGGING_AND_CLOUD_STORAGE"
          }
        }
      }
    }
    

Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.dataRetentionConfig.taskLogsRetentionConfig.storageMode
    
    {
      "config": {
        "dataRetentionConfig": {
          "taskLogsRetentionConfig": {
            "storageMode": "CLOUD_LOGGING_AND_CLOUD_STORAGE"
          }
        }
      }
    }
    

###  Terraform 

In the `task_logs_retention_config` block, in the `storage_mode` field specify how Airflow task logs must be saved:

  * `CLOUD_LOGGING_AND_CLOUD_STORAGE` to save logs to the environment's bucket and Cloud Logging.
  * `CLOUD_LOGGING_ONLY` to save logs only in Cloud Logging.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        data_retention_config {
    
          task_logs_retention_config {
    
            storage_mode = "CLOUD_LOGGING_AND_CLOUD_STORAGE"
    
          }
        }
      }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        data_retention_config {
    
          task_logs_retention_config {
    
            storage_mode = "CLOUD_LOGGING_AND_CLOUD_STORAGE"
    
          }
        }
      }
    }
    

## What's next

  * [View logs](https://docs.cloud.google.com/composer/docs/composer-2/view-logs)
  * [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
