---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout/
title: Back up HANA 1+n and HANA scale-out databases to an appliance-managed backup \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:58.973495+00:00
---

# Back up HANA 1+n and HANA scale-out databases to an appliance-managed backup  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up HANA 1+n and HANA scale-out databases to an appliance-managed backup Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page includes information about protecting HANA 1+n and HANA scale-out.

## Protect HANA 1+n

To protect a HANA 1+n replication cluster as a single application, the application has the cluster host as sid `name_cluster` after application discovery. For example, if sr1 is the HANA instance, then the application name is sr1 and the hostname is sr1_cluster in the **App Manager Applications** list.

The HANA log backup destination must be shared between two nodes. When failover occurs, the database and log backup automatically fails over to the current primary, and log backups are performed from the current primary, capturing the last logs from the old primary as well as new logs from the new primary. Follow the preparation steps in [Prepare your SAP HANA databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-hana).

HANA 1+n is always discovered as cluster application containing all node details in the metadata. It is a good idea to run a force discovery after any changes to cluster node configuration—such as after adding or deleting a node from the cluster. If a node is removed or added after discovery and protection, the configuration does not be updated automatically in Backup and DR metadata, and may cause backup issues.

**Note:** With the failover of the HANA database from primary to secondary and back, the next database backup is low-splash and takes more time to get the incremental changes.

### Prerequisites for protecting SAP HANA 1+n instances and databases

Before protecting SAP HANA instances, ensure the following:

  * If hosts have virtual IPs configured, add only the virtual IP and hostname of the primary host during discovery.
  * The Backup and DR agent must be installed on all nodes.
  * Ports need to be opened on the hosts to allow communication on port 5106. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target and the target port is 5106. Also, there is no need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.
  * HANA log backup location must be set on shared—NFS.

**Note:** Activate logical volume manager change block tracking on all the nodes of SAP HANA scale-out cluster by running `/opt/act/cbt/bin/cbt_activate.sh` on the command line as a root user. Verify that logical volume manager change block tracking is activated by running `pgrep cbt`—this should return two processes running for change block tracking.

## Protect HANA scale-out

![SAP HANA scale-out](https://docs.cloud.google.com/static/backup-disaster-recovery/docs/images/backup/sap-hana-scaleout-concept.png)

### Prerequisites for protecting SAP HANA scale-out instances

Before protecting SAP HANA scale-out instances, be sure that the following is complete:

  * If hosts have virtual IPs configured, add only the virtual IP and the associated hostname of the primary host during discovery.
  * The Backup and DR agent must be installed on all nodes.
  * Ports need to be opened on the hosts to allow communication on port 5106. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target and the target port is 5106. Also, there is no need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.
  * For backint file based—Full+Incremental—backup, the HANA log backup location must be set to shared—NFS. See [Add the host to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host).
  * For storage snapshot protection

    * Data and log volume are non-shared across all nodes
    * Data and log volumes are managed by logical volume manager (LVM)
    * Ensure mnt000* directories exist on the local mount points to identify the primary and secondary nodes
**Note:** The discovered SAP HANA instance shows up under application list with: Application (HANA sid name): Hostname and Friendly path (HANA sid name)_cluster(site id)_(HANA hardware id).

Follow the setup procedures in [Prepare your SAP HANA databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana-scaleout).


**Note:** Activate logical volume manager change block tracking on all the nodes of SAP HANA scale-out cluster by running `/opt/act/cbt/bin/cbt_activate.sh` on the command line as a root user. Verify that logical volume manager change block tracking is activated by running `pgrep cbt`—this should return two processes running for change block tracking.**Note:** If you are protecting data on a HANA replication cluster, any reboot of the primary HANA node results in a role switch where the secondary node becomes the new primary node. Backup jobs always run from the primary HANA node. If there is a HANA failover to the secondary node, the first backup after the failover is a full copy because CBT from the old primary node is not available on the new primary (old secondary) node.

## Backup and DR documentation for SAP HANA scale-out

This page is one in a series of pages specific to protecting and recovering SAP HANA scale-out instances with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout)
  * [Prepare SAP HANA scale-out instances for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA scale-out host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout)
  * [Configure staging disk format and backup method for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout)
  * [Set application details and settings for SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout)
  * [Mount an SAP HANA scale-out backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA scale-out backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA scale-out backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
