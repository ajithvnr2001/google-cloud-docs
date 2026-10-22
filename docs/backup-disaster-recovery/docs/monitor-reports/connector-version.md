---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-version/
title: View connector version logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:28.955191+00:00
---

# View connector version logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View connector version logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the connector version logs that are created in Cloud Logging. These logs provide information about the details of the connector versions that are installed on your hosts. With the connector version log, you can detect the hosts that have lower version connectors and plan for necessary upgrades. These logs are generated every day.

The connector version logs display the following connector statuses:

  * **Current release** : No action is required.
  * **Upgrade needed** : The connector running on the host must be upgraded to the available version.
  * **Newer version** : The connector running on the host has a version higher than that available on the backup/recovery appliance.



## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the connector version logs. The _Logs Viewer_ role gives you read-only access to view connector version logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to connector version logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View connector version logs

You can view Backup and DR connector version logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR connector version logs entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **gcb_connector_version** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read your connector version log entries of backup/recovery appliances in a project, run the following command:
    
    
    ```gcloud
    gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version"
    ```
    

## Connector version log format

Backup and DR connector version log entries include the following fields:

**Field** | **Description**  
---|---  
Appliance name | The name of the appliance associated with the host.  
Appliance ID | The ID of the appliance associated with the host.  
Host name | The name of the host associated with the connector.  
Host ID | The ID of the host associated with the connector.  
Host OS type | The type of OS installed on the host.  
Host IP address | The IP address of the host.  
DB authentication | Type of authentication, which can be `DB` or `Host` based authentication.  
Installed version | The current version of the connector installed on the host.  
Available version | The latest connector version available for upgrade.  
Version check | Displays the current connector version status on the host and provides recommendations for upgrades if necessary. The status can be the current release, upgrade required, or newer version.  
Disk preference | Determines whether images created by the host are formatted for NFS or block IO (iSCSI or fibre channel).  
Transport | The transport mode of the host, which can be NFS to hypervisor, SAN based, Guest VM ISCSI, or NFS to host.  
  
  * NFS to hypervisor means that the staging disk is presented over NFS to an ESX host. From the ESX host, the staging disk is mapped from the VMDK to a VM.
  * SAN based means that the staging disk is presented over fibre channel or iSCSI to a ESX host. The ESX host then maps the staging disk from the vRDM or pRDM to a VM.
  * Guest VM ISCSI means that the staging disk is presented to the host or the VM through iSCSI.
  * NFS to host means that the staging disk is presented to the host or the VM through NFS.



The following sample is an example log entry logged on a backup/recovery appliance `sky-full-82959`.
    
    
        {
          "insertId": "49945312_142868351806",
          "jsonPayload": {
            "host_name": "hana1",
            "host_ip_address": "10.10.238.233",
            "available_version": "11.0.12.4",
            "db_authentication": "Host",
            "appliance_id": "142868351806",
            "host_os_type": "Linux(SUSE Linux Enterprise Server 15 SP2)",
            "host_id": "13889",
            "disk_preference": "BLOCK",
            "version_check": "Newer version",
            "installed_version": "11.0.11.319",
            "transport": "SAN Based",
            "appliance_name": "sky-full-82959"
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
              "resource_container": "projects/XXXXXXXXXXXX",
              "location": "us-central1"
            }
          },
          "timestamp": "2024-07-25T10:37:30.772Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version",
          "receiveTimestamp": "2024-07-25T10:39:30.216711646Z"
        }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view all the connector version logs for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version"
    

If you are looking to view the connector version details log associated with a backup/recovery appliance.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version"
        jsonPayload.appliance_name="appliance_name"
    

If you are looking for the connector version logs associated with a particular host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version"
        jsonPayload.host_name="host_name"
    

If you are looking to view the connector version logs where the upgrade is needed.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_connector_version"
        jsonPayload.version_check="Upgrade Needed"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter connector version logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
