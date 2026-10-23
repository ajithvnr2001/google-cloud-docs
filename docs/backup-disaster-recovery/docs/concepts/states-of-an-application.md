---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/states-of-an-application/
title: Manage applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:44.274296+00:00
---

# Manage applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/states-of-an-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can change the backup plan state of an application at any time. Future application captures occurs based on the new backup template. Existing point-in-time backups are retained according to the old template that was assigned when those backups were created. The following information outlines the different states of an application when viewing applications data in the **App Manager** , including what the application state is and what that state means.

  * **Unmanaged** : An application is unmanaged when no backup plan is associated with it.
  * **Managed** : An application becomes managed when the first replication job completes successfully based on the assigned backup plan, or when the application is failed back—see **Failed over**. In this state, there is at least one replicated backup to fail over to. An application remains in this state as long as the backup plan associated with it is not removed or the application is not failed over. When you remove the backup plan, the application becomes unmanaged.
  * **Ignored** : An unmanaged application has been manually set to **Ignored** , see [Ignore unmanaged applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application). There may be specific applications or VMs that you don't want identified as unmanaged applications. Applications and VMs flagged as **Ignored** are not included in the total count of unprotected applications in the dashboard.
  * **Discovered on Multiple Appliances** : If you have assigned management of the same applications to multiple backup/recovery appliances, the applications that have been discovered on multiple appliances are flagged in the **Applications** window. When you click the icon, the appliance management console displays the **Application Discovered on Multiple Appliances** dialog to identify the appliance ID, management state—true or false—appliance name, and host IP address.



Don't maintain multiple copies of the same application managed by two or more backup/recovery appliances.

**Note:** If there is an assigned management of the same applications to multiple backup/recovery appliances, and the application is in a managed state on one appliance and in an unmanaged state on another appliance, that application is identified as **Managed** in the **Applications** window.

  * **Host Added to Multiple Appliances** : This icon appears if a single host has been added to multiple backup/recovery appliances managed by the management console.
  * **Orphaned** : An application appears as an orphan in the **Applications** window when you delete an application or VM from the **App Manager** and there are backups attached to the application that no longer exist on the associated backup/recovery appliance.
  * **Disabled** : An application appears **Disabled** if the schedule is disabled—paused—for an application in the **App Manager** service.
  * **Failed over** : From the **App Manager** , if the StreamSnap replication backup fails over to a remote site, its state changes to failed over. In the failed over state, the application, which is also configured on the remote site, accesses the remote backup directly. Consequently, replication to the remote site is paused. When the application is ready to operate from the local site, you can synchronize the data back to the local site—this is called syncback—and then when the data is back in sync, failback to the local site.



## Ignore unmanaged applications

You can configure unmanaged applications and VMs as ignored. Ignored applications and VMs don't include the total count of unprotected applications in the dashboard.

Ignored applications can be set as unmanaged applications when you change their state back to **Unmanaged**.

To ignore an application or VM, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select one or more unmanaged applications. To bulk ignore multiple unprotected applications, you can **Shift+Click** to select a continuous range of unmanaged applications or **Ctrl+Click** to select multiple non-continuous applications.

  3. Right-click and choose **Ignore Applications** from the drop-down menu.

**Note:** You can also select **Ignore Applications** from drop-down list at the bottom right corner of the page.

A confirmation message prompts you to confirm that you want to ignore the selected applications.

  4. Click **Confirm** to ignore the selected applications.

The selected items in the **Applications** list changes to the **Ignored** state.

  5. To return the application or VM state back to the **Unmanaged** state, select **Cancel** in the confirmation message.




## Modify backup plan management of a managed application

To modify the backup template and resource profile for a managed application, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM whose backup plan management you want modify, and click **Manage Backup Configuration** from the drop-down list at the bottom right corner of the page.

The **Manage Backup Configuration** page opens.

  3. Modify the backup template or resource profile by selecting a different option from the **Template** and **Profile** drop-down lists.

     * **Template** : An existing backup template that includes policies to define the snapshot or replication of the application data. See [Create a new template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [Create a production-to-snapshot policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prd-snap) for details.
     * **Profile** : An existing resource profile that defines the resources used to store the data of the application as snapshot or replicated backups. See [Creating a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) for details.
  4. Optionally, click the application left-hand panel icon to open to refine your search results. You can open the application left-hand panel from the **Applications** , **Consistency Groups** , and **Logical Groups**.

  5. Optionally, to change **Database Inclusion** rule, click **Edit**. The **Manage Membership** page opens. Update the **Inclusion** rule as necessary and select the databases that should be managed. Click **Save** to update the membership rules.

  6. Click **Apply** to apply your changes.

The **Update Backup Plan** message opens prompting you to confirm the changes.

  7. Click **Update** on the message to confirm.

The **Apply Backup Plan** page opens.

  8. Make changes as appropriate and click **Apply Backup Plan**.

A success message opens.

  9. Click **Okay** to close the message.

The application may not get captured until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job does not start until the appliance has an available job slot at 02:00 (UTC) of the following day.. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).




## Disable backup plan management of an application

To temporarily disable—interrupt—the backup plan management of an application, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select a managed application or VM and then select **Manage Backup Configuration** from the drop-down list.

The **Manage Backup Configuration** page opens.

  3. Click **Disable** from the drop-down list in the right-corner of the **Manage Backup Configuration** page.

  4. From the **Disable Backup Plan** message box, click **Disable** to confirm that you want to disable the backup plan.

The success message box opens.

  5. To resume backup plan management of the application, click **Enable** from the drop-down list in the right-corner of the page. When prompted, click **Enable** to confirm that you want to re-enable backup plan management of your VM or application.

Application management can then resume, using the existing template and resource profile.




## Remove backup plan management of an application

To remove the backup plan assigned to the application and stop data capture for an application, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select a managed application or a VM, then click **Manage Backup Configuration** from the drop-down list at the bottom right corner of the page.

The **Manage Backup Configuration** page opens.

  3. Select **Remove backup plan** from the drop-down list.

  4. From the **Remove backup plan** message box, click **Remove** to confirm that you want to stop applying the backup plan to the application.

The **Remove backup plan** button changes to **Apply** , and the management console stops managing based on the current, selected template and resource profile.

  5. To resume backup plan management, select a templates and resource profile, then click **Apply**.

  6. From the backup template page, make the following changes prior to applying a backup plan:

     * **Details and Settings** : Apply application-specific settings.
     * **Policy Overrides** : Override specific policy settings previously configured in the selected backup template. Advanced settings may be useful or required in certain circumstances. See [Configure policy overrides](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.
**Note:** You can override policy settings in the **App Manager** only if the policy template **Allow Overrides on Policy Settings** parameter has been set to **Yes**.
  7. Click **Save Changes** to save the modified settings.

The **Success** message opens.

The application is not captured until the scheduled job runs according to the hours of operations defined in the backup template.




## Delete an application

You can delete the following:

  * Unmanaged applications or VMs
  * Managed applications or VMs after removing the backup plan from them—that is dissociating the backup plan.



When you delete an application or VM, this action also removes that application or VM from the corresponding backup/recovery appliance.

Use these instructions to delete applications or VMs:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the VM or application that you want to delete, then right-click and select **Delete Application** from the drop-down menu. You can also right-click on the item and select **Delete** at the bottom right corner of the page. A confirmation dialog opens listing the application that will get deleted.

  3. Click **Confirm** in the confirmation dialog. The application shows as an orphan if there are any active backups corresponding to the deleted application.




## Delete multiple applications

You can also select multiple unmanaged applications and delete them at the same time.

Use these instructions to delete multiple unmanaged applications or VMs:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the VMs or applications that you want to delete, right-click and select **Delete Applications** from the drop-down menu. You can also right-click on the item and select **Delete** at the bottom right corner of the page.

A confirmation dialog opens listing the applications to be deleted.

  3. Click **Confirm**.

When all the selected applications are deleted successfully, a success dialog opens. In case any of the selected application fails to get deleted, an information dialog opens. This lists the app name, app type as well as any error message that was returned as part of the delete operation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
