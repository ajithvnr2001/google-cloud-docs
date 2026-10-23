---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-logs/
title: View unprotected resource logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:34.958808+00:00
---

# View unprotected resource logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View unprotected resource logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the unprotected resource logs created in Cloud Logging. These logs provide information about unprotected resources across backup/recovery appliances.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the unprotected resource logs. The Logs Viewer role gives you read-only access to view unprotected resource logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to unprotected resource logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View unprotected resource logs

You can view Backup and DR unprotected resource logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR unprotected resource log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**. 
  2. Select an existing Cloud project. 
  3. In the **Query builder** pane, select **gcb_unprotected_resource** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read the unprotected resource log entries of backup/recovery appliances in a project, run the following command:
    
    
    ```sh
    gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource" --project=PROJECT_ID
    ```
    

## Unprotected resource log format

Backup and DR unprotected resource log entries include the following fields:

**Field** | **Description**  
---|---  
Appliance ID | The ID of the appliance on which the resource is discovered.  
Discovered on | The date when the resource was first discovered.  
Discovered by | The name of the appliance on which the resource is discovered.  
Host ID | The host ID associated with the resource.  
Hostname | The hostname associated with the resource.  
Instance name | The name of the database instance. If the resource is not of the database type, it shows N/A.  
Resource ID | The ID of the resource.  
Resource name | The name of the resource.  
Resource type | The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.  
  
The following sample is an example log entry logged on a backup/recovery appliance `sky-full-82959`.
    
    
        {
          "insertId": "55552852_145719527555",
          "jsonPayload": {
            "host_name": "host4",
            "resource_id": "55552852",
            "host_id": "55550547",
            "instance_name": "NA",
            "discovered_on": "2024-07-02T13:59:46.795078Z",
            "resource_type": "FileSystem",
            "resource_name": "/boot/efi",
            "discovered_by": "sky-full-82959",
            "appliance_id": "145719527555"
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "resource_container": "projects/myproject",
              "location": "us-central1",
              "management_server_id": "my-management-server-id"
            }
          },
          "timestamp": "2024-07-24T10:11:14.984Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource",
          "receiveTimestamp": "2024-07-24T10:16:16.320083904Z"
        }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view all the unprotected resource logs for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource"
    

If you are looking for the unprotected data logs associated with a particular resource.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource"
        jsonPayload.resource_name="resource_name"
    

If you are looking for the unprotected resource logs associated with a particular resource type.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource"
        jsonPayload.resource_type="resource_type"
    

If you are looking for the unprotected resource logs associated with a particular host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_unprotected_resource"
        jsonPayload.host_name="host_name"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter unprotected resource logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
