---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-consistency-groups/
title: Add consistency groups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:20.055951+00:00
---

# Add consistency groups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-consistency-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add consistency groups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A consistency group is a collection of discovered applications from the same host. You create a consistency group to back up application data of all member applications together to preserve consistency of data across the member applications. Once you have created a consistency group, you can manage the group by applying a common policy and resource profile to the members of it.

**Note:** Generic logical volume manager (LVM) applications and VMs are not allowed in consistency groups. Oracle does not support consistency groups of multiple databases. However, a consistency group may include a single Oracle database with other applications.

Use these instructions to create a consistency group:

  1. In the appliance management console, click **App Manager** > **Applications** , then click **Add Application**.
  2. Click the **Consistency Group** option.

The **Create Consistency Groups** page opens.

  3. From the **Select an Appliance** drop-down list, choose the appliance you want to select applications for the consistency group from. You can select applications from multiple appliances for inclusion in the same consistency group.

  4. Enter an alphanumeric text string in the **Group Name** field. Spaces, underscores (___), and dashes (-) are allowed in a name; but do not include special characters.

  5. Enter a description of the consistency group in the **Description** field.

  6. Make a selection from the **Host** list. If there are many hosts, use the search box to filter the list to only show your search criteria matches.

You can see a list unmanaged applications on the host. If you cannot find an application, then that application is probably already managed. For each application, you can also see the app type.

  7. Highlight the applications you want to add to the group, then click **Add**. To remove an added application, select the application from the right pane and click **Remove**.

  8. Click **Create Group** to create the group. To cancel the operation and close the **OnBoarding Wizard** , click **Cancel**.

A success message appears after the group has been created.

  9. Click **Click here to manage group** to protect the **Consistency Group**. Otherwise click **Okay** to close the success message.

The [Applications page](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/applications-page) opens. When you filter by applications to see the **Consistency Groups** , you can see the newly created group in the list.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
