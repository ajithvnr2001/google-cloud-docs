---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/configure-db2-pacemaker/
title: Configure Pacemaker-aware snapshots for IBM Db2 HADR in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:14.937482+00:00
---

# Configure Pacemaker-aware snapshots for IBM Db2 HADR in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/configure-db2-pacemaker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Configure Pacemaker-aware snapshots for IBM Db2 HADR in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

Backup and DR provides a Pacemaker-aware snapshot feature for IBM Db2 High Availability Disaster Recovery (HADR) databases. Use this feature to safely take Persistent Disk snapshots of a standby database that a Pacemaker cluster manages.

This process prevents Pacemaker from misinterpreting the temporary database deactivation during a snapshot as a failure. This avoidance of a misinterpretation prevents an unnecessary database restart.

## Before you begin

Grant the Db2 instance OS user the necessary permissions to run Pacemaker commands with `sudo` privileges on all Db2 HADR standby nodes.

  1. As the `root` user, open the `/etc/sudoers.d/db2_pacemaker_access` file for editing:
         
         visudo -f /etc/sudoers.d/db2_pacemaker_access
         

  2. Add the following line to the file:
         
         DB2_INSTANCE_OS_USER  ALL=(root)    NOPASSWD: /usr/sbin/pcs status, /usr/sbin/pcs resource * DB2_HADR_PACEMAKER_RESOURCE_REGEX
         

  3. Replace the following placeholders:

     * `DB2_INSTANCE_OS_USER`: your Db2 instance OS username.
     * `DB2_HADR_PACEMAKER_RESOURCE_REGEX`: the regular expression that matches your Db2 HADR Pacemaker resource name. For example, `*_db2`.
**Note:** The wildcard `*` after the resource name lets you pass flags like `maintenance=true` to the `pcs resource` command.



## Enable Pacemaker-aware backups

To enable this feature, specify the Pacemaker resource name in the backup settings for your Db2 application.

  1. In the Backup and DR appliance management console, go to the Db2 application backup settings.
  2. Locate the **Db2 HADR CLUSTER PACEMAKER RESOURCE** option.
  3. Enter the Pacemaker resource name for the Db2 instance that manages the HADR cluster.

**Note:** If you don't specify a Pacemaker resource name, the backup proceeds as if Pacemaker is not present in the HADR environment. This field is optional.

## How Pacemaker-aware snapshots work

The Pacemaker-aware backup process coordinates Pacemaker and Db2 through a specific sequence of operations.

  1. The script runs pre-checks to verify that it is on the standby node and the HADR pair is in a healthy state.
  2. The script places the Db2 instance resource into Pacemaker's maintenance mode. This action instructs Pacemaker to stop monitoring the resource.
  3. The script deactivates the database with the `db2 deactivate` command to freeze database I/O.
  4. The script takes the Persistent Disk storage snapshot.
  5. The script activates the database with the `db2 activate` command to unfreeze I/O.
  6. The script removes the Db2 instance resource from maintenance mode, which lets Pacemaker resume monitoring.
  7. The script logs all actions and runs cleanup routines.

**Note:** To prevent the Pacemaker resource from remaining in maintenance mode, a detached background process automatically removes the maintenance mode after two minutes, regardless of the backup job's status.

## Troubleshoot

If a backup job fails, examine the following logs on the database standby node for more details:

  * `/var/act/log/customapp-db2instance.log`: contains information about standby database deactivation and activation, and Pacemaker resource maintenance mode entry and exit.
  * `/act/tmpdata/BACKUP_JOB_NAME/pcs_background_cleanup.log`: indicates if the Pacemaker resource was automatically taken out of maintenance mode because the snapshot exceeded the two-minute timeout.
  * `/var/log/pacemaker/pacemaker.log`: provides additional context from Pacemaker.



### Snapshot timeout

If a Persistent Disk snapshot job exceeds two minutes, Backup and DR automatically exits the Pacemaker resource maintenance mode. The backup job status changes to `Retrying`, and the scheduler initiates a new backup in ten minutes.

### Aborted or blocked backup jobs

If a backup job aborts or becomes blocked, the system exits Pacemaker resource maintenance mode after two minutes, and the backup job fails.

### Configure alerts

You can configure alerts from the Backup and DR appliance management console to send emails when a backup job fails. It is also recommended to configure Pacemaker alerts based on `pcs status`.

## What's next

  * Learn more about [Backup and DR concepts](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
  * Learn more about [Backup and DR for IBM Db2 databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-db2).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
