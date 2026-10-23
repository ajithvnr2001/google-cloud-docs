---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template/
title: Manage backup templates in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:39.576727+00:00
---

# Manage backup templates in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage backup templates in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

In the appliance management console, backup templates are composed of backup policies. In policies, you can define when to run a backup, how frequently to run a backup job, how long to retain the backup (for **Days** , **Weeks** , **Months** , **Years**), and also additional configuration when the policy is applied to a different application, such as a file system, database, or VM.

Backup policy types include:

  * [Production to snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prd-snap)
  * [Snapshot to OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#snap-vault)
  * [Production to mirror replication (StreamSnap)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#snap-mirror)
  * [Direct to OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#direct-vault)
  * [OnVault replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#vault-repli)

**Note:** Templates that are used to backup Compute Engine instances should only contain production to snapshot policies. You can't use a template that has OnVault or StreamSnap policies with a Compute Engine instance.

## Create a backup template

Use these instructions to create a backup template:

  1. In the Backup and DR appliance management console, click the **Backup Plans** tab and select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Click **Create Templates**.

The **Create Template** page opens appears with a new (empty) backup template.

  3. In the **Template** field, enter a name for the backup template. For the template name, enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name. Don't include special characters.

  4. In the **Description** field, enter a brief description about this backup template.

  5. To modify the **ALLOW OVERRIDES ON POLICY SETTINGS** :

     * Click **Yes** to allow selected **App Manager** advanced settings to override the settings specified in a backup plan policy's advanced settings. You can override policy settings in the **App Manager** only if the **ALLOW OVERRIDES ON POLICY SETTINGS** parameter is set to **Yes**.
     * Click **No** if you don't want to allow backup plan policy setting override in the **App Manager**.
  6. Click either **+(Plus)** in the backup plan policy map or **+Add** in the Policies section to add a backup policy. Backup policy includes:

     * [Production to snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prd-snap)
     * [Snapshot to OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#snap-vault)
     * [Production to mirror replication (StreamSnap)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#snap-mirror)
     * [Direct to OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#direct-vault)
     * [OnVault replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#vault-repli)
**Note:** Templates that are used to backup Compute Engine instances should only contain production to snapshot policies. You can't use a template that has OnVault or StreamSnap policies with a Compute Engine instance.
  7. Enter a **Policy Name**.

  8. If appropriate for the policy type, specify the schedule type, **Windowed** or **Continuous**. The default is **Windowed**.

     * **Windowed.** Defines a discrete snapshot backup schedule adhering to a specific frequency and time window (for example, perform a backup every 30 minutes, daily from 09:00 to 17:00 UTC). You can instruct the backup/recovery appliance to run multiple backup jobs at a specified frequency interval or once during a specified time window.
     * **Continuous.** Defines a continuous snapshot backup schedule (for example, perform a backup job every eight hours, starting the first job at 01:00 UTC). In this policy schedule, jobs run continuously (24/7) at the specified time interval.
  9. Configure the policy frequency settings per the selected schedule type as outlined in the following lists:

     * **Windowed**
     * **On These Days.** Configures the frequency of the policy by defining an interval at which backups are captured. Based on this interval setting, the snapshot job runs once every specified number of days, weeks, months, or years. Click the link of this parameter and modify the **Run** interval. The schedule is displayed in a calendar view. From this view you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes accordingly based on your selection.
     * **Except.** Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily snapshot schedule every Friday, select weekly and select Friday. Click the link of this parameter and modify the exception. The schedule is displayed in a calendar view. From this view you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes accordingly based on your selection.
     * **Within This Window.** Defines a start and end time window for capturing backups.
     * **Run Once Per Window.** Specifies that the frequency duration for capturing backups is once during the specified **Run Between** time window.
     * **Every.** Specifies a repeat frequency duration (minutes or hours) for capturing backups during the specified Run Between time window. Example: Every two hours.
     * **Continuous**
     * **Every.** Specifies the time period in which to repeat the backup capture.
     * **Starting At.** Specifies the time of day at which to run the first job in the continuous cycle of backup captures.
     * Both **Windowed** and **Continuous**
     * **Retain For.** Specifies the length of time that you intend to retain the backup. Example: Retain the backup for two days.
  10. Optionally, change the application priority from the **Priority** drop-down list. The default job priority is medium, but you can change the priority to high or low.

     * The backup plan scheduler identifies when one or more policies applied to applications are to run, and then initiates a job that places the policy into a queue when the scheduled start time occurs. For each policy type there is a pacing mechanism to ensure that the system isn't overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state, which means that even if a job is supposed to start at a particular time it will execute only occur when a job slot is available.
     * If multiple applications are scheduled to run at the same time with the same job priority, the selection of the application to run is randomized to ensure fairness across all of the applications of the same priority.
     1. Configure the **Advanced Policy Settings**. See [Configure advanced policy settings for a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.
**Note:** **Advanced Policy Settings** defined in a policy can be overridden by the **Application Details & Settings** in **App Manager** , if the policy's template has been set to allow overrides.
  11. When you are finished creating the new policy, click **Update Policy** to add it to the template. You return to the **Templates** list.

  12. Click **Save Template**.




## View and filter backup templates

The templates window lists all of the backup templates that are developed on the appliance management console. From the **Templates** window, you can view information such as the template name, description, and allow policy override for all backup templates in appliance management console. You can modify the display of fields that appear in the **Templates** table, and you can also use the filter feature to locate backup templates by these identifiers.

  1. Click the **Backup Plans** tab and select **Templates** from the drop-down menu. The **Templates** page opens.
  2. To modify the display of the properties in this view, you can:

     * **Adjust Fields.** To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed (or those fields you don't want to view).
     * **Sort Content.** To sort the content listed in a table column by alphanumeric order, select a column header and then click the Up or Down arrow to change the order.
     * **Adjust Column Width.** To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Filter By.** To filter the list, enter one or more filter criteria as appropriate. (If you don't see the **Filter By** area, click **show filter**). To clear a filter, click the **x** to the right of the applied filter.

     * **Note:** Filters that are of type text, list, and date, persist across different appliance management console sessions for the same user.
  3. To export the policy templates list click the export icon. You can export in PDF format.




## Add policies to an existing backup template

To modify an existing backup template to include an additional policy:

  1. Click the **Backup Plans** tab and select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select the backup template that you want to modify, then select **Edit** (bottom right-hand corner of the page).

The **Templates** window appears with the existing backup template.

**Note:** You can also right-click on the item in the list and select **Edit** from the menu.
  3. If you want to modify the template name or description, make the required changes in the **Template** or **Description** fields.

**Note:** For template name, enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name, but don't include special characters.
  4. If you want to modify the **ALLOW OVERRIDES ON POLICY SETTINGS** , complete the following:

     * Click **Yes** to allow selected **App Manager** advanced settings to override the settings specified in a backup plan policy's advanced settings.
     * Click **No** if you don't want to allow backup plan policy setting override in the **App Manager**.
**Note:** You can override policy settings in **App Manager** only if the backup plan policy template **ALLOW OVERRIDES ON POLICY SETTINGS** parameter has been set to **Yes**.
  5. To add a policy to an existing backup template, click either **+(Plus)** in the backup plan policy map or **+Add** in the **Policies** area of the **Templates** window. Policy types include: snapshot, snapshot to OnVault, and production-to-mirror replication (StreamSnap).

The associated policy configuration panel appears in the **Template** window.

  6. When you are done creating the new policy, click **Update Policy** to add it to the template. You return to the **Templates** window.

  7. Click **Save Template**.




## Edit an existing backup template

After creating a backup template, you can change the following:

  * Template name
  * Template description
  * Policy settings



To make the changes:

  1. Click the **Backup Plans** tab and select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select the backup template that you want to modify, then click **Edit** (bottom right-hand corner of the window).

The **Templates** page opens with the existing backup template.

**Note:** You can also right-click on the item in the list and select **Edit** from the menu.
  3. If you want to modify the template name or description, make the required changes in the **Template** or **Description** fields.

**Note:** For template name, enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name, but don't include special characters.
  4. If you want to modify the **ALLOW OVERRIDES ON POLICY SETTINGS** , complete the following:

     * Click **Yes** to allow selected **App Manager** advanced settings to override the settings specified in a backup plan policy's advanced settings.
     * Click **No** if you don't want to allow backup plan policy setting override in the **App Manager**.
**Note:** You can override policy settings in **App Manager** only if the backup plan policy template **ALLOW OVERRIDES ON POLICY SETTINGS** parameter has been set to **Yes**.
  5. In the **Policies** area of the **Template** window, click the arrow to the left of the backup plan policy you want to edit and review the settings. There might be multiple policies under a specific policy type. Select the backup plan policy that you want to edit, then click **Edit Policy**. The associated policy configuration panel appears in the **Template** window.

  6. Edit the backup plan policy as needed.

  7. When you are done making policy edits, click **Update Policy**.




## Clone a backup template

Use these instructions to clone an existing backup template:

  1. Click the **backup Plans** tab and select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select one or more templates that you want to clone.

  3. Right-click and select **Clone** from the drop-down menu options. (For multiple template selections, you can also go to the bottom right corner of the page and select the **Clone** option.)

You are prompted to confirm that you want to clone the selected templates.

  4. Click **Yes** to clone the templates. You will see a success message at the end of the cloning process.

  5. Click **Close**. The cloned template is listed in the **Templates** list and has a prefix of "Copy of ...".

**Note:** If you had selected multiple templates, a clone is created for each template.



## Delete a backup template

Use these instructions to delete a policy template:

**Note:** You can delete a policy template only when the policy template isn't used in the **App Manager** service to manage an application.

  1. Click the **Backup plans** tab and select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select the backup template from the list, then click **Delete** (bottom right-hand corner of the window). The backup template is removed from the **Templates** window.

**Note:** You can also right-click on the item in the list and select **Delete** from the menu.



You aren't allowed to delete all replication policies from a template if any snapshot policy includes database log replication.

## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
