---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-sap-workflow/
title: Create Backup and DR Workflows for SAP HANA database in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:07.199778+00:00
---

# Create Backup and DR Workflows for SAP HANA database in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-sap-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create Backup and DR Workflows for SAP HANA database in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use these instructions to create a Backup and DR Workflow to automate the process of mounting and refreshing SAP HANA database from a snapshot.

  1. In the appliance management console, click **App Manager** > **Applications** , right-click the HANA database and select **Manage Workflows**.
  2. In the upper right corner of the **Workflows: Application Dashboard** page, click **\+ Add Workflow**.
  3. Complete the following:

     * **Workflow Name** : Enter a name for the Backup and DR Workflow.
     * **Workflow Type** : Select **Direct Mount**.
     * **Schedule Type** : Choose **Scheduled** or **On Demand**. For a scheduled Backup and DR Workflow, specify the frequency as well.
     * **Mount Label** : Optionally, specify a mount label for the mounted image.
     * **Hosts** : Select the target host where the virtual HANA database copy is created.
     * **Mount Location** : Specify a mount point for the data volume and log volume of the target.
     * **Post-Script** : Specify a postscript name to be run virtual HANA database copy at the end of refresh.
     * **Create New Virtual Application** : Enable **Create New Virtual Application**.
     * **Target Database SID** : Provide the target HANA database name.
     * **SAP DB User Store-Key** : Provide the hdbuserstore key for the target database—HANA 2.0: SYSTEMDB.

Optionally, if you want to protect the new virtual database complete the following:

     * **Manage New Application** : Enable **Manage New Application**.
     * **Template** : Choose a template to protect the database.
     * **Profile** : Choose a profile.
  4. Click **Add**. This creates an on-demand or scheduled Backup and DR Workflow to create or refresh the HANA database virtual copy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
