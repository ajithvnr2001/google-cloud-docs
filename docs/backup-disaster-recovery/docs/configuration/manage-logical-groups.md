---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups/
title: Manage logical groups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:39.354054+00:00
---

# Manage logical groups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage logical groups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A logical group is a grouping of applications from one or more hosts used for ease of management to apply a common policy to all the group's applications. Mount, clone, and restore operations are performed on the backups of each application in the group individually. Although you apply a backup plan against a logical group, management of the data capture is performed one-by-one to the individual applications and there is no association among the applications in the group.

## Create a logical group

The **Create Logical Group** page has user controls to help you with the following:

  * Easier filtering
  * A search field in the top left side of the page that queries applications
  * Ability to set columns as visible or hidden
  * Ability to set the number of rows to display



While creating a new logical group when you filter by managed applications, you can see a list of all managed applications that you can add to the logical group. However, once you add a managed application to add to the group, you can subsequently select only those applications that have the same **Template** and **Resource Profile** of the added application.

### Create a group of applications managed by a common policy

Use these instructions to create a group of applications and manage that group using a common policy:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Logical Groups** from the drop-down menu. The **Logical Groups** page opens.
  2. Click **Create Logical Group**.
  3. Select the backup/recovery appliance from which you want to select applications for the logical group from the **Select an Appliance** drop-down list. You can select applications from multiple appliances for inclusion in the same consistency group.
  4. Enter a name in **Group Name** using an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name; but don't include special characters.
  5. Enter a description for the logical group in the **Description** field.
  6. Highlight the applications that you want to add to the logical group, then click **Add** (**+**).
  7. Click **Create Group**.

When the logical group is created, a success message appears.




Keep in mind the following:

  * If you add applications to a logical group and then decide not to include them, highlight those applications in the list on the right and then click **Remove**.
  * When you create a Logical Group by adding a managed application, the logical group that is created is managed by the same template and profile of the application that is added.



### Create a logical group and add an application to the group

Use these instructions to create a logical group and add the application to that group:

  1. Select one or more managed or unmanaged applications from the **Applications List** view. You cannot select both managed or unmanaged applications.
  2. Right-click and select **Add to Logical Group** from the drop-down list.

The **Add/Create Logical Group** dialog opens.

  3. Select the **Create New Logical Group** option. If you are adding a managed application, the **Create New Logical Group** option is hidden if the appliance does not support adding a managed application to an empty logical group.

  4. In **Group Name** , enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name. Don't include special characters.

  5. Optionally, provide a brief description about the logical group in the **Description** field.

  6. Click **Create** to create the logical group.

When the logical group is created a success message appears.

**Note:** When you create a logical group by adding a managed application, the logical group that is created is managed by the same **Template** and **Profile** of the application that is added.



### Create an empty logical group

From the **Logical Groups** page, you can create an empty logical group as a placeholder and add applications to the group later. You can add applications from multiple appliances to the same consistency group. If the applications you add to the group are unmanaged, you can protect the logical group by applying a backup plan. All the members are managed by the same **Template** and **Profile** of the logical group.

Use these instructions to create an empty logical group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Logical Groups** from the drop-down menu.

The **Logical Groups** page opens.

  2. Select an appliance you want to select applications from for the logical group from the **Select an Appliance** drop-down list. You can select applications from multiple appliances for inclusion in the same consistency group.

  3. In **Group Name** , enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name. Don't include special characters.

  4. Optionally, enter a brief description of the logical group in the **Description** field.

  5. Click **Create**.




## Add an application to a logical group

Use these instructions to add applications to a logical group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select one or more managed or unmanaged applications. You cannot select both managed and unmanaged applications.

  3. Right-click and select **Add to Logical Group** from the drop-down list.

The **Add/Create Logical Group** dialog opens. By default, the **Add to Logical Group** option is selected.

**Note:** When you are adding managed applications, the **Create New Logical Group** option is hidden if the appliance does not support adding a managed application to an empty logical group.
  4. To add the selected application to an existing group, select the group and click **Add**. Once the application is added, a success message appears.

**Note:** When adding applications to a Logical Group that is either managed or unmanaged, the newly-added applications are listed.



## Protect a logical group

Logical groups are managed in the same way that individual applications are managed. You manage a logical group by assigning a resource profile and a template to it to define the backup plan to capture the application data from the different applications in the logical group. An application in a logical group is managed until you remove the application from the logical group, or until you remove the backup plan that is managing the logical group.

For details on creating a logical group, see Create a logical group.

Use these instructions to manage a logical group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the logical group containing the applications that you want to manage, and then select **Manage Backup Plan** from the drop-down list at the bottom right corner of the window.

The **Manage Backup Plan** window appears.

  3. Click the application left hand panel icon to open to refine your search results. You can open the application left hand panel from the **Applications** > **Consistency Groups** > **Logical Groups**.

  4. From the **Manage Backup Plan** window, choose the following from the **Template** and **Profile** drop-down lists:

     * **Template** : An existing backup template that includes policies to define the snapshot or replication of the application data.
     * **Profile** : An existing resource profile that defines the resources used to store the data of the application as snapshot or replicated backups.

The **App Manager** service shows a view of the policies assigned to the selected applications in the backup plan policy map. Management comes from the template policies and profiles that you designed in the backup plans.

  5. Click **Apply** to apply the backup template and resource profile.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

The applications in the logical group are not managed until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job does not start until the appliance has an available job slot at 02:00 (UTC).

**Note:** To change settings for an application that is in a managed state, see [Modify backup plan of a managed application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application).
  6. After you apply the backup plan to manage the applications in the logical group, if required, you can override specific policy settings previously configured in the selected backup template. You can override policy settings in the **App Manager** only if the policy template **Allow Overrides on Policy Settings** parameter has been set to **Yes**.

Select an application from the list under **Group Members** and click **Advanced Settings**. After you override advanced policy settings, click **Save Changes**. See [Configure policy overrides](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.

**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** checkbox to the right of the selection you want to reset, or click **Reset All to Default** to reset all application selections back to their default state.
  7. After you apply the backup plan to manage the applications in the logical group, if want to review the details of the managed application or modify any of the application-specific settings, select an application from the list under **Group Members** and click **App Settings**.

The **Application Details and Settings** dialog includes the following:

     * Application-specific information associated with the consistency group, such as application type, hostname, host IP address, path, operating system, backup/recovery appliance, and appliance IP address.
     * Application-specific settings that you can modify for each application in the logical group.
  8. Click **Save Changes**. To disable the backup plan, see [Remove backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove).




## Edit a logical group

Use these instructions to edit an existing logical group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Click **Logical Groups** to access the **Logical Groups** list.

  3. Select the logical group you want to edit and then select **Edit** from the drop-down list.

  4. Make the necessary modifications to the logical group.




## Delete a logical group

Use these instructions to delete an existing logical group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Logical Groups** from the drop-down menu.

The **Logical Groups** page opens.

  2. Click **Logical Groups** to access the **Logical Groups** list.

  3. Select the logical group you want to delete and then select **Delete** from the drop-down list. You can also right-click on the item in the list and select **Delete** from the menu.

  4. Click **Confirm**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
