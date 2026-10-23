---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-reports-bigquery/
title: Connector version reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:53.179161+00:00
---

# Connector version reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-reports-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Connector version reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to view prebuilt connector version reports in BigQuery.

The Backup and DR provides prebuilt connector version reports that are accessible in BigQuery. You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script) where the logs are being routed through the log sink.

The connector version report provides information about the details of the connector versions installed on your hosts. You can use the connector version report to detect hosts with down-level connectors.

  * **Appliance name** : The name of the appliance associated with the host.
  * **Appliance ID** : The ID of the appliance associated with the host.
  * **Host name** : The name of the host associated with the connector.
  * **Host ID** : The ID of the host associated with the connector.
  * **Host OS type** : The type of OS installed on the host.
  * **Host IP address** : The IP address of the host.
  * **DB authentication** : The type of authentication, which can be `DB` or `Host` based authentication.
  * **Installed version** : The current version of the connector installed on the host.
  * **Available version** : The latest connector version available for upgrade.
  * **Version check** : Displays the current connector version status on the host and provides recommendations for upgrades if necessary. The status can be the current release, upgrade required, or newer version.
  * **Disk preference** : Determines whether backups created by the host are formatted for NFS or block IO (iSCSI or fibre channel).
  * **Transport** : The transport mode of the host, which can be NFS to hypervisor, SAN based, Guest VM ISCSI, or NFS to host. NFS to hypervisor means that the staging disk is presented over NFS to an ESX host. From the ESX host, the staging disk is mapped from the VMDK to a VM. SAN based means that the staging disk is presented over fibre channel or iSCSI to a ESX host. The ESX host then maps the staging disk from the vRDM or pRDM to a VM. Guest VM ISCSI means that the staging disk is presented to the host or the VM through iSCSI. NFS to host means that the staging disk is presented to the host or the VM through NFS.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
