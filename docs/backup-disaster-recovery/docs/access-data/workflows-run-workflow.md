---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-workflow/
title: Run Backup and DR Workflows in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:00.753670+00:00
---

# Run Backup and DR Workflows in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Run Backup and DR Workflows in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR Workflows can be configured to run according to a schedule or run on demand only. Scheduled Backup and DR Workflows can be run on demand.

Running a Backup and DR Workflow on demand is particularly useful when the Backup and DR Workflow's data source has been updated but the Backup and DR Workflow is not scheduled to run for a while. The Backup and DR Workflow can be run on demand to provision or re-provision an environment without having to wait for the next scheduled run.

**Note:** Appliance management console users assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run, edit, delete, or disable a Backup and DR Workflow.

To run a Backup and DR Workflow, follow these steps:

  1. Click the **App Manager** tab and select **Workflows** from the drop-down menu. The **Workflows** page opens.
  2. Right-click the workflow that you want to run and select **Run Now** from the drop-down menu. The **Run Workflow** dashboard page opens.
  3. Depending on your Backup and DR Workflow type, see the following topics for more information:

     * [Run a direct-mount Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/run-direct-mount-workflows)
     * [Run a LiveClone Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/run-liveclone-workflows)
     * [Run a scheduled direct-mount Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/run-scheduled-direct-mount-workflows)
     * [Run a scheduled LiveClone Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/run-scheduled-liveclone-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
