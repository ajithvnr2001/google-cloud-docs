---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-otherdb/
title: Add other database hosts and discover other databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:10.542133+00:00
---

# Add other database hosts and discover other databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add other database hosts and discover other databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you can back up a database, first add the host to the appliance management console and discover the database or its instance. Use the following steps:

  1. Add the host to the appliance management console

  2. Discover the database or instance from the App Manager

  3. Set the host staging disk format

  4. Find the discovered database or instance in the App Manager




## Install the Backup and DR agent on the database server

The Backup and DR agent, a small-footprint, lightweight service on the server, is used to capture an application-consistent copy of databases. It uses change block tracking to identify changes to database data for Backup and DR's incremental forever capture strategy. All database servers that have data to be protected by Backup and DR must have the Backup and DR agent installed.

  1. [Obtain the right Backup and DR agent for your host](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#right-connector)

  2. Log onto the Linux server as root.

  3. [Install the Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)




## Add the host to the appliance management console

After the agent is installed, you must [add the host to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications#add-host).

## Set the host staging disk format

Once the host is added, edit the host to set the staging disk format:

  1. Right-click the host and select **Edit**.

  2. On the **Edit Host** page, select the staging disk format:

     * **Block** : Block-based staging disks are required for volume-level backups. These volume-level backups are the most useful for both backup and recovery and TDM usage. Backup and DR changed-block tracking is only available on block-based staging disks, and virtual databases can only be mounted to block-based staging disks.
     * **NFS** : NFS staging disks permit only file-based backup.
  3. Select **Save** at the bottom of **Edit Host** page.




## Discover the database or instance application from the App Manager

Use the following instructions to discover and protect the database or instance:

  1. Click **App Manager** > **Applications** , then select **Add Application**.

  2. In the **Add Application** wizard, select the database type and then follow the steps in the wizard.




## Find the discovered database or instance in the App Manager

To find the newly-discovered instance and its databases, go to the appliance management console **App Manager** > **Applications** page. All applications known to the appliance management console of all types are listed. You can use the **Type** application filter on the left pane to show only the instances and databases of interest. The new database or the instance and its databases appear in the list as unmanaged—the red shield icon.

## What's next

After the databases have been added to the appliance management console:

  * [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)

  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/application-details)

  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/otherdb-required-settings)

  * [Protect the database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
