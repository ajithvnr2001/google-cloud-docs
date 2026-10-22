---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-logs/
title: View mounted image logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:56.606567+00:00
---

# View mounted image logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View mounted image logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the mounted image logs created in Cloud Logging. These logs provide information about the details of the mounted images present on the backup/recovery appliance. These logs are generated once every eight hours.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the mounted image logs. The Logs Viewer role gives you read-only access to view mounted image logs of all backup/recovery appliances in the specified project.

For more information about the IAM permissions and roles that apply to mounted image logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View mounted image logs

You can view Backup and DR mounted image logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **gcb_mounted_images** from the **Select Log name** list.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read your log entries of backup/recovery appliances in a project, run the following command:

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Logging API. To read your mounted image log entries of backup/recovery appliances in a project, run the following command:
    
    
    ```sh
    gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_gcb_mounted_images" --project=PROJECT_ID
    ```
    

## Mounted images log format

Backup and DR mounted images log entries include the following fields:

Field Name | Description  
---|---  
Appliance ID | The ID of the appliance associated with the host where the image is mounted.  
Appliance name | The name of the appliance associated with the host where the image is mounted.  
Last mount date | The timestamp when the image was last successfully mounted.  
Mounted hostname | The name of the host where the image is mounted.  
Mounted host ID | The ID of the host where the image is mounted.  
Mounted image age in days | The number of days from when the image was last mounted.  
Mounted image name | The name of the mounted image.  
Mounted resource label | The label associated with the mounted resource.  
Mounted resource name | The name of the resource on which the image is mounted.  
Read mode | The mode in which data gets read from the OnVault pool.  
Recovery point date | The timestamp of when the last successful backup was taken.  
Resource type | The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.  
Resource virtual size (GiB) | The size of the resource in GiB.  
Resource size (GiB) | The size of the protected resource in GiB.  
Restorable object | The object of the application which is restored as part of mount.  
Storage consumed (GiB) | The size of the storage consumed in GiB.  
Source image expiration date | The mounted image expiration date. It is in YYYY-MM-DDTHH:MM:SS.SSSZ format.  
Source image name | The name of the source image.  
Source image type | The type of source image. It can be a snapshot or OnVault image.  
Source hostname | The name of the source host.  
Source resource name | The name of the source resource.  
Source host ID | The ID of the source host where the image is mounted.  
Source resource ID | The ID of the source resource.  
Username | The name of the user who initiated the mount operation.  
  
The following sample is an example log entry logged on a backup/recovery appliance `sky-full-82959`.
    
    
        {
          "insertId": "49459606_142868351806",
          "jsonPayload": {
            "source_resource_id": "14617",
            "mounted_image_age_in_days": 72,
            "source_host_id": "14348",
            "source_image_type": "snapshot",
            "appliance_name": "sky-full-82959",
            "resource_size_in_gib": 0.31,
            "mounted_host_id": "14348",
            "restorable_object": "/postgre11-data",
            "read_mode": "Balanced",
            "storage_consumed_in_gib": 0,
            "resource_virtual_size_in_gib": 47.99,
            "recovery_point_date": "2024-05-03T18:15:46Z",
            "appliance_id": "142868351806",
            "source_resource_name": "/postgre11-data",
            "source_image_name": "Image_0014977",
            "resource_type": "FileSystem",
            "mounted_host_name": "postgres11-1",
            "source_image_expiration_date": "2024-05-05T18:16:07.530Z",
            "mounted_image_name": "Image_0015394",
            "user_name": "AGMUser(pkmishra@google.com:16924)",
            "mounted_resource_name": "postgres1",
            "last_mount_date": "2024-05-03T18:23:25Z",
            "mounted_resource_label": "postgres1",
            "source_host_name": "postgres11-1"
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "resource_container": "projects/xxxxxxxxxxxx",
              "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
              "location": "us-central1"
            }
          },
          "timestamp": "2024-07-15T08:29:56.885Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_mounted_images",
          "receiveTimestamp": "2024-07-15T08:36:04.071156102Z"
        }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view all the mounted image logs for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_mounted_images"
    

If you are looking to view mounted image details log associated with a backup/recovery appliance.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_mounted_images"
        jsonPayload.appliance_name="appliance_name"
    

If you are looking to view mounted image details log for a given resource. 
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_mounted_images"
        jsonPayload.source_resource_name="resource_name"
    

If you are looking for the view mounted image details log associated with a particular host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource"
        jsonPayload.source_host_name="host_name"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter mounted images logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
