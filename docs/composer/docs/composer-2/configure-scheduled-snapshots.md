---
url: https://docs.cloud.google.com/composer/docs/composer-2/configure-scheduled-snapshots/
title: Configure scheduled snapshots \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:47.122769+00:00
---

# Configure scheduled snapshots  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/configure-scheduled-snapshots/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Configure scheduled snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/configure-scheduled-snapshots "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/configure-scheduled-snapshots "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to configure your environment to save snapshots on a schedule.

For more information about how environment snapshots work and how to save snapshots manually, see [Save and load snapshots](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots).

## How scheduled snapshots work

When you enable scheduled snapshots, Managed Airflow periodically saves snapshots of your environment to a Cloud Storage bucket.

If you create snapshots manually, Managed Airflow saves snapshots in the environment's bucket by default. For scheduled snapshots, we recommend to save snapshots in a separate bucket. This way, you can set up permissions and a lifecycle configuration for this bucket. One bucket can hold snapshots from several environments, and you can also create buckets that are [redundant across regions](https://docs.cloud.google.com/storage/docs/locations#key-concepts).

## Before you begin

  * For more information about snapshot requirements and limitations, see [Save and load snapshots](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots).

  * Managed Airflow supports scheduled snapshots in 2.0.32 and later versions. Environment snapshots are supported in 2.0.9 and later versions.




## Create a bucket for scheduled snapshots

[Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for scheduled snapshots. Consider how you want to use environment snapshots. If it is a part of your [disaster recovery plan](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide), then use a bucket that is [redundant across regions](https://docs.cloud.google.com/storage/docs/locations#key-concepts) or a bucket in a different region, so you have access to the data even in case of a full regional outage. Otherwise, a bucket in the same region as the environment might be more suitable, and in this case you reduce the costs of transferring data between regions.

### Configure permissions for the bucket

**Warning:** Snapshots can contain **sensitive information** , such as Airflow connection extras and passwords, which can be decrypted from an environment snapshot. We recommend to limit access to the bucket only to trusted entities. 

To mitigate this security risk, you can store sensitive information that is used by Airflow DAGs, such as keys or passwords, in Secret Manager. For more information, see [Configure Secret Manager for your environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager).

Configure the following permissions:

  * The [service account of your environment](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account) must have read and write permissions for this bucket. For example, the [**Storage Object Admin** role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) has such permissions.

  * User accounts do not need any additional permissions for the bucket to load snapshots from it, unless you want to view the contents of the bucket from Google Cloud console. In this case a user account must have read permission on the bucket.




### Set a lifecycle configuration for the bucket

To save storage costs, you can configure a rule that deletes environment snapshots after a certain period of time.

For example, to automatically delete snapshots older than 30 days:

  1. [Set a lifecycle configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles) for the bucket.
  2. Specify the **Delete object** action.
  3. Select **Age** and 30 days as the condition.



## Enable a snapshot schedule for your environment

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In **Recovery configuration** > **Snapshot schedule** , click **Edit**. The **Snapshot schedule** pane opens.

  5. In the **Snapshot schedule** pane, select **Create snapshots periodically, according to the specified schedule**.

  6. In the **Schedule frequency** drop-down list, select daily, weekly, or custom period for snapshots.

You can specify a custom schedule with the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules). For example, to save snapshots every 30 minutes, specify `*/30 * * * *`.

  7. In the **Snapshot location** field, select the bucket folder where you want to save snapshots.




###  gcloud 

Update your environment configuration. The following arguments define parameters for scheduled snapshots:

  * `--enable-scheduled-snapshot-creation` enables scheduled snapshots.
  * `--snapshot-location` specifies a bucket folder where you want to save snapshots.
  * `--snapshot-creation-schedule` specifies how often environment snapshots must be taken, in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules). For example, to create a snapshot every 30 minutes, specify `*/30 * * * *`.

  * `--snapshot-schedule-timezone` defines a time zone for the schedule. This value is a time offset and does not take into account daylight saving time changes. Valid values are from `UTC-12` to `UTC+12`. Examples: `UTC`, `UTC-01`, `UTC+03`.



    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --enable-scheduled-snapshot-creation \
        --snapshot-location "gs://SNAPSHOTS_FOLDER" \
        --snapshot-creation-schedule "CRON_EXPRESSION" \
        --snapshot-schedule-timezone "TIME_ZONE"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `SNAPSHOTS_FOLDER` with the URI of a bucket folder where to save the snapshot.
  * `CRON_EXPRESSION` with the schedule, in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).
  * `TIME_ZONE` with a time zone for the schedule.



Example (every day at 4:00, UTC+01):
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --enable-scheduled-snapshot-creation \
        --snapshot-location "gs://example-bucket/environment_snapshots" \
        --snapshot-creation-schedule "0 4 * * *" \
        --snapshot-schedule-timezone "UTC+01"
    

###  API 

Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

In this request:

  1. In the `updateMask` parameter, specify the `config.recoveryConfig.scheduledSnapshotsConfig` mask to replace the existing scheduled snapshots configuration.

  2. In the request body, specify the configuration for snapshots:
         
         {
           "config": {
             "recoveryConfig": {
               "scheduledSnapshotsConfig": {
                 "enabled": true,
                 "snapshot_location": "gs://SNAPSHOTS_FOLDER",
                 "snapshot_creation_schedule": "CRON_EXPRESSION",
                 "time_zone": "TIME_ZONE"
               }
             }
           }
         }
         

Replace:

     * `SNAPSHOTS_FOLDER` with the URI of a bucket folder where to save the snapshot.
     * `CRON_EXPRESSION` with the schedule, in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

     * `TIME_ZONE` with a time zone for the schedule. This value is a time offset and does not take into account daylight saving time changes. Valid values are from `UTC-12` to `UTC+12`. Examples: `UTC`, `UTC-01`, `UTC+03`.

Example (every day at 4:00, UTC+01):
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
      // locations/us-central1/environments/example-environment?updateMask=
      // config.recoveryConfig.scheduledSnapshotsConfig
        {
          "config": {
            "recoveryConfig": {
              "scheduledSnapshotsConfig": {
                "enabled": true,
                "snapshot_location": "gs://example-bucket/environment_snapshots",
                "snapshot_creation_schedule": "0 4 * * *",
                "time_zone": "UTC+01"
              }
            }
          }
        }
    




###  Terraform 

The `scheduled_snapshots_config` in the `recovery_config` block defines parameters for scheduled snapshots:

  * `enabled` enables scheduled snapshots.
  * `snapshot_location` specifies a bucket folder where you want to save snapshots.
  * `snapshot_creation_schedule` specifies how often environment snapshots must be taken, in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules). For example, to create a snapshot every 30 minutes, specify `*/30 * * * *`.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      recovery_config {
        scheduled_snapshots_config {
          enabled = true
          snapshot_location = "gs://SNAPSHOTS_FOLDER"
          snapshot_creation_schedule = "CRON_EXPRESSION"
          time_zone = "TIME_ZONE"
        }
      }
    }
    

Replace:

  * `SNAPSHOTS_FOLDER` with the URI of a bucket folder where to save the snapshot.
  * `CRON_EXPRESSION` with the schedule, in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

  * `TIME_ZONE` with a time zone for the schedule. This value is a time offset and does not take into account daylight saving time changes. Valid values are from `UTC-12` to `UTC+12`. Examples: `UTC`, `UTC-01`, `UTC+03`.




Example (every day at 4:00, UTC+01):
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      recovery_config {
        scheduled_snapshots_config {
          enabled = true
          snapshot_location = "gs://example-bucket/environment_snapshots"
          snapshot_creation_schedule = "0 4 * * *"
          time_zone = "UTC+01"
        }
      }
    }
    

## Disable scheduled snapshots

If you disable scheduled snapshots, all existing snapshots that were already taken are not modified or removed. These snapshots remain in the location where they were saved.

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In **Recovery configuration** > **Snapshot schedule** , click **Edit**. The **Snapshot schedule** pane opens.

  5. In the **Snapshot schedule** pane, select **Do not create snapshots automatically**.




###  gcloud 

Update your environment configuration. The `--disable-scheduled-snapshot-creation` argument disables scheduled snapshots.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --disable-scheduled-snapshot-creation
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --disable-scheduled-snapshot-creation
    

###  API 

Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

In this request:

  1. In the `updateMask` parameter, specify the `config.recoveryConfig.scheduledSnapshotsConfig.enabled` mask to replace the value of the `enabled` field.

  2. In the request body, specify the new value:
         
         {
           "config": {
             "recoveryConfig": {
               "scheduledSnapshotsConfig": {
                 "enabled": false
               }
             }
           }
         }
         




Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.recoveryConfig.scheduledSnapshotsConfig.enabled
    {
    "config": {
      "recoveryConfig": {
        "scheduledSnapshotsConfig": {
          "enabled": false
        }
      }
    }
    }
    

###  Terraform 

To disable scheduled snapshots, set the `enabled` field in the `scheduled_snapshots_config` block to `false`:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      recovery_config {
        scheduled_snapshots_config {
          enabled = false
        }
      }
    }
    

Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      recovery_config {
        scheduled_snapshots_config {
          enabled = false
          // Other scheduled snapshots parameters
        }
      }
    }
    

## What's next

  * [Save and load environment snapshots](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots)
  * [Disaster recovery with snapshots](https://docs.cloud.google.com/composer/docs/composer-2/disaster-recovery-with-snapshots)
  * [Access control](https://docs.cloud.google.com/composer/docs/composer-2/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
