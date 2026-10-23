---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan/
title: Set up and plan a backup/recovery appliance deployment \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:33.755392+00:00
---

# Set up and plan a backup/recovery appliance deployment  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Set up and plan a backup/recovery appliance deployment Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR supports backing up Cloud SQL instances, AlloyDB clusters, and Compute Engine instances and individual disks from the Google Cloud console. The procedures for backing up and restoring those resources can be found in their documentation. If all of your workloads fit within these categories, then you don't need a backup/recovery appliance.

Backup and DR for VMware VMs and SAP HANA, IBM Db2, Oracle, and Microsoft SQL Server databases that run inside Compute Engine instances requires a Backup and DR appliance management console and one or more backup/recovery appliances. When using this setup, you need to choose the size of your backup/recovery appliances to match the applications that you back up. The flow for this setup involves creating a management server, deploying appliances, and then using the appliance management console to configure backup schedules and to define what is backed up and where.

For an overview of strategies to ensure your most effective use of your backup/recovery appliances, see [Backup/recovery appliance deployment considerations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-considerations).

This page describes how to perform initial activation of Backup and DR and set up configurations for your project.

## Components of the backup/recovery appliance architecture

The Backup and DR architecture is delivered through the following components:

  * **Google Cloud console** : The Google Cloud console includes the Backup and DR product for central management of your Persistent Disk vaulted backups, backup plans for Compute Engine instances, and enhanced backup for Cloud SQL in those products.

  * **appliance management console** : The appliance management console serves as the management plane for your backup/recovery appliances. Each Backup and DR deployment includes a single appliance management console managing any number of backup/recovery appliances. The appliance management console is deployed in the [backup administration project](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep#project-shared) and is highly available within the deployed region, providing resilience against zonal outages.

  * **Backup/recovery appliances** : The backup/recovery appliance is the data mover that efficiently captures, moves, and manages the lifecycle of backup data within your enterprise. The backup/recovery appliances are deployed in the [Workload entity](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep#project-shared) for cloud workloads. If you deploy multiple backup/recovery appliances, each appliance must be associated with a unique Service Account.

**Warning:** The backup/recovery appliance machine type or configuration (CPU, memory) must not be changed after deployment without consulting with [Support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support).   
Also, don't rename the backup/recovery appliance after deployment as it may make the appliance unusable. Renaming of the appliance is not supported.
  * **Backup and DR agents** : The Backup and DR agent calls the application-native APIs to efficiently capture data from production applications in an incremental-forever fashion, and provides the application awareness at the time of recovery. The agent is installed on application hosts where applications to be protected reside. If you are only protecting the entire VM or a subset of its disks, then the Backup and DR agent is not required.




The appliance management console is activated into a service producer VPC network. This service producer VPC communicates with your project using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).

Communication between management server and appliances, between appliances, and between appliances and host agents is secured by mutual TLS authentication.

## Set up Backup and DR in the Google Cloud console

Go to the Google Cloud console to activate the backupdr API and set up permissions for your account:

[Activate Google Cloud Backup and DR ](https://console.cloud.google.com/backupdr?project=_)

## Backup/recovery appliance types

Backup and DR provides appliance types that are optimized for different workloads—Compute Engine VMs, VMware VMs, databases, and file systems. You can choose the appliance type that best meets your needs. It's important to select the best appliance type for your workloads. Once the backup/recovery appliance is in service, it runs continuously forever, always ready to run and re-run backup, restore, and other jobs at all times.

Backup and DR provides the following appliance types:

  * **Standard for VMware VMs and other databases or resources** : This n2-standard-16 machine type supports optimal performance to back up production databases, VMware VMs, and other resources. This appliance adds 4 TB of balanced disk capacity at deployment and you can add 63 additional 4 TB disks. This appliance can manage up to 1,500 applications and 5000 daily snapshots.
  * **Standard for Compute Engine VMs or SAP HANA databases** : This e2-standard-4 machine type is best for backing up Compute Engine instances, Cloud SQL instances, AlloyDB clusters, and data resources that use Persistent Disk for backups: IBM Db2 and SAP HANA databases configured to use Persistent Disk. This appliance type has a minimum Persistent Disk capacity of 10 GB. This appliance can manage up to 5,000 Compute Engine and Cloud SQL instances, AlloyDB clusters, and Persistent Disk-based data applications.
  * **Basic for VMware VMs and other databases or resources** : This e2-standard-16 machine type supports moderate performance to back up databases, VMware VMs, and other resources. This appliance can manage up to 1,500 applications and 5000 daily snapshots. This appliance adds 4 TB of standard disk capacity at deployment and you can add 63 additional 4 TB disks of the following types:

    * **Minimal capacity Persistent Disk** : this option provides a minimum disk capacity of 10 GB. In this storage type, backups are stored as Persistent Disk snapshots and don't consume the local storage of the backup/recovery appliance.
    * **Standard Persistent Disk** : select this storage type if you want to have efficient block storage. This is recommended for Google Cloud VMware Engine VMs, databases, or file system application with mid-high I/O, in addition to Compute Engine VMs. This adds 4 TB of Persistent Disk capacity as the minimum disk capacity.
    * **SSD Persistent Disk** : select this storage type if you want to have fast block storage. This is recommended for Google Cloud VMware Engine, databases, or file system applications with very high I/O, in addition to Compute Engine VMs. This adds 4 TB of Persistent Disk capacity as the minimum disk capacity.



When you deploy an appliance, a service account is created automatically regardless of the appliance type. You can view the service account from the **Service Account** page.

The service account's name appears in the email address format:

`APPLIANCE_NAME@PROJECT_ID.iam.gserviceaccount.com`

Replace the following:

  * APPLIANCE_NAME: the name of your Backup/recovery appliance.
  * PROJECT_ID: the ID of your Google Cloud project (source).



You can move backups with long-term retention needs to Standard, Nearline, and Coldline storage depending on your expected need to access the data.

## Firewall configurations

The following required firewall rules for ingress into Backup and DR are automatically added.

Purpose | Source | Target | Port (TCP)  
---|---|---|---  
Support traffic (support to appliance) | SSH_CLIENT_IP | Backup/recovery appliance | 26  
iSCSI backup (host to appliance) | AGENT_HOST_IP | Backup/recovery appliance | 3260  
StreamSnap traffic (appliance to appliance) | SOURCE_APPLIANCE_IP | Backup/recovery appliance | 5107  
Backup/recovery appliance connectivity to appliance management console | APPLIANCE_IP | *.backupdr.googleusercontent.com | 443  
  
Replace the following:

  * SSH_CLIENT_IP: the IP address of the host running the SSH client.
  * AGENT_HOST_IP: the IP address of the host running the Backup and DR agent.
  * SOURCE_APPLIANCE_IP: the IP address of the source appliance.
  * APPLIANCE_IP: the IP address or subnet of the Backup/recovery appliance.



For more detail on how to configure this rule, see [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep).

For any host that is running the Backup and DR agent, you must manually add the following TCP port to allow connectivity with an ingress firewall rule.

Purpose | Source | Target | Port (TCP)  
---|---|---|---  
Agent traffic (appliance to host) | Backup/recovery appliance | Host running Backup and DR agent | 5106  
  
For hosts using NFS for backup traffic, or for ESX hosts running in Google Cloud VMware Engine that are using NFS for mounts, you need to manually add the following TCP and UDP ports to allow connectivity with an ingress firewall rule.

Purpose | Source | Target | Port (TCP/UDP)  
---|---|---|---  
NFS backup or mount | Host running Agent or ESXi host running mount | Backup/recovery appliance | 111, 756, 2049, 4001, 4045  
  
For a list of the permissions used during this operation, see [Backup and DR installation permissions reference](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-permissions-reference).

## Supported regions

The following section lists the appliance management console and backup/recovery appliances supported regions.

### Appliance management console supported regions

While Backup and DR can be used to back up supported workloads in any Google Cloud region, the appliance management console can be activated only in the following regions:

Geographic Area | Region Name | Region Description |   
---|---|---|---  
**North America** |  |  |   
| `northamerica-northeast1` * | Montréal |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `northamerica-northeast2` | Toronto |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-central1` | Iowa |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-east1` | South Carolina |   
| `us-east4` | Northern Virginia |   
| `us-east5` | Columbus |   
| `us-south1` | Dallas |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-west1` | Oregon |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-west2` | Los Angeles |   
| `us-west3` | Salt Lake City |   
| `us-west4` | Las Vegas |   
| `northamerica-south1` * | Querétaro |   
**South America** |  |  |   
| `southamerica-east1` | São Paulo |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `southamerica-west1` | Santiago |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
**Europe** |  |  |   
| `europe-central2` | Warsaw |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-north1` | Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-north2` | Stockholm |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-southwest1` | Madrid |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west1` | Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west2` | London |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt |   
| `europe-west4` | Netherlands |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west6` | Zürich |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west8` | Milan |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west9` | Paris |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west10` | Berlin |   
| `europe-west12` | Turin |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
**Middle East** |  |  |   
| `me-central1` | Doha |   
| `me-central2` | Dammam |   
| `me-west1` | Israel |   
**Africa** |  |  |   
| `africa-south1` | Johannesburg |   
**Asia Pacific** |  |  |   
| `asia-east1` | Taiwan |   
| `asia-east2` | Hong Kong |   
| `asia-northeast1` | Tokyo |   
| `asia-northeast2` * | Osaka |   
| `asia-northeast3` | Seoul |   
| `asia-southeast1` | Singapore |   
| `asia-southeast2` | Jakarta |   
| `australia-southeast1` | Sydney |   
| `australia-southeast2` | Melbourne |   
**India** |  |  |   
| `asia-south1` | Mumbai |   
| `asia-south2` | Delhi |   
  
* Querétaro (northamerica-south1), Montréal (northamerica-northeast1), and Osaka (asia-northeast2) don't support zone separation. This means the multiple zones within each of these regions may not be located in physically separate data center campuses. Consequently, a single, localized physical disaster event could potentially impact multiple zones within the same region, increasing the risk of data loss compared to regions that support zone separation.

**Note:** You cannot move a appliance management console to a different region after it has been deployed.

### Backup/recovery appliance supported regions

Backup/recovery appliances can be deployed into any [Google Cloud zone](https://docs.cloud.google.com/compute/docs/regions-zones#available).

Workflow service to perform the backup/recovery appliance deployment is supported in the listed [regions](https://docs.cloud.google.com/workflows/docs/locations). If the Workflow service isn't available in a region where your backup/recovery appliance is deployed, then the Backup and DR defaults to running the workflow in the `us-central1` region (the appliance itself is still created in your selected region). If you have an organization policy that is set to prevent creating resources in other regions, then you must temporarily update your organization policy to allow creation of resources in `us-central1` region. You can restrict the `us-central1` region after deployment of the backup/recovery appliance.

## What's next

  * [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
