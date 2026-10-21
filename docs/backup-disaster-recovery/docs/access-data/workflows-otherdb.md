---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-otherdb/
title: Create Backup and DR Workflows for other database types in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:06.904556+00:00
---

# Create Backup and DR Workflows for other database types in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create Backup and DR Workflows for other database types in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can use a Backup and DR Workflow to automate the process of mounting and refreshing a database instance's databases from a backup.

  1. From the Backup and DR appliance management console, open the **App Manager** , then right-click the instance and select **Manage Workflows**.
  2. Click **\+ Add Workflow**.
  3. Complete the following information.

     * **Workflow Name** : Enter a name for this Backup and DR Workflow.
     * **Workflow Type** : Select **Direct Mount**.
     * **Schedule Type** : Choose **Scheduled** or **On Demand** based on your requirement. For a scheduled Backup and DR Workflow, specify the frequency as well.
     * **Source Image** : Select based on requirements.
     * **Mount Label** : Optionally, specify a mount label for the mounted backup.
     * **Hosts** : Select the target host or hosts where the virtual Db2 instance databases copy are created.
**Note:** Be sure that the target instance has no databases with the same name as any of the source databases, or the new target database name selected for the source databases during the mount.
     * **Mount Location** : Specify a mount point to mount the data volumes and log volumes of the target.
     * **Pre-Script** : Optionally, specify a prescript name to be run before refresh.
     * **Post-Script** : Optionally, specify a postscript name to be run at the end of refresh.
     * **Create New Virtual Application** : Enable **Create New Virtual Application**.
     * **Select Items** : Select the databases to refresh on target and specify the target dbname from **Database Options** for each database.
     * If you see **Target Instance User and Password** , enter credentials for the target instance.
     * **TARGET INSTANCE NAME** : If target instance is visible, then select it, otherwise specify the target instance name.
     * **Manage New Application** : Enable **Manage New Application**.
     * **Template** : Choose a template to protect the database.
     * **Profile** : Choose a profile.
  4. Click **Add** to create an on-demand or scheduled Backup and DR Workflow to create or refresh the instance's databases virtual copy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
