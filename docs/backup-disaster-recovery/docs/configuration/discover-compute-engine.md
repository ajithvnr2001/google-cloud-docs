---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine/
title: Discover and protect Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:59.086159+00:00
---

# Discover and protect Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Discover and protect Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to configure and manage self-managed backups for Compute Engine instances. The self-managed backup model supports specialized requirements, such as cross-region configurations, disk-specific protection, and automated tagging.

For more information about backup models, see the [Backup and Disaster Recovery documentation](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine/).

## Before you begin

Ensure you satisfy the following requirements before you start:

  * Configure a default cloud credential or create a new one to allow the appliance to access Google Cloud projects.
  * Assign the necessary Identity and Access Management (IAM) roles and permissions to the service account of the backup/recovery appliance.
  * Create a backup template to define the underlying backup policy rules.



## Onboard Compute Engine instances

The Compute Engine onboarding wizard discovers instances based on your cloud credentials and project settings.

  1. Open the onboarding wizard in the appliance management console.
  2. Select a cloud credential and the target appliance.
  3. Specify the Project ID and Zone.
  4. Click **Search**.

**Note:** Remove labels from instances before onboarding if you create them using **Create Machine Image** or **Create Similar** , as existing labels might not read correctly in the appliance management console.

For a large instance list, use the following options to filter instances:

  * **New** : This shows instances that have not yet been discovered on the appliance management console. By default only new instances are shown.
  * **Unmanaged** : This shows instances that were previously discovered but not managed by applying a backup plan.
  * **Managed** : This shows instances that were previously discovered and are managed by applying a backup plan.
  * **Ignored** : This shows the instances that have been already discovered but marked as ignored.

**Note:** If you have discovered an instance into Backup and DR, and then in Google Cloud console you create a copy of the instance from the source instance (using either **Create Machine Image** or **Create Similar**), then labels from the source instance are copied to the copy instance. The labels from the copy instance may not be read correctly in the appliance management console. [Remove any labels](https://docs.cloud.google.com/compute/docs/labeling-resources#remove_a_label) before onboarding the new instance.

For the selected instances, you can apply a backup plan, add to a logical group, add as unmanaged, or mark as ignored. After onboarding the Compute Engine instances, go to the **App Manager** then **Applications** page to find the discovered instances.

## Enable protection for instances

Follow these steps to protect your Compute Engine instances.

  1. In the appliance management console, open the wizard by selecting **Back up & Recover** > **Back up** , or **App Manager** > **Applications** > **Add Application**.
  2. Select **Compute Engine**.
  3. Select a Cloud Credential and the target appliance.
  4. Select the **Project ID** and **Zone** then click **Search** to list the instances available in the project and zone. 
     * If you cannot find your project in the **Project ID** drop-down, click **Don't see your project ID here** and it lists the missing permissions required for the project.
     * Add the listed missing permissions or roles to the service account of the backup/recovery appliance, or add the relevant service account to the relevant project with the correct IAM role.
  5. Select the instances you want to protect.
  6. Choose whether to protect all disks or only the boot volume for each VM.
  7. To apply a plan immediately, select the instance, choose **Apply a backup plan** from the drop-down, and select a backup template.
  8. Review the summary and click **Finish**.
  9. After the backup plans are applied to Compute Engine instances, the status changes to a green check mark. The green check indicates that your instance is onboarded successfully. You can view your onboarded Compute Engine instance from **App Manager** > **Applications** to page. If you want to run the job immediately, see [Run an on-demand job](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

**Note:** If you back up a Compute Engine instance to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back the data up to a different backup/recovery appliance.**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs, unprotected data, and failed restore operations.



## Manage logical groups

A logical group is a group of applications from one appliance used for ease of management to apply a common backup plan to all the group's applications. Mount, clone, and restore operations are performed on the images of each application in the group individually. Although you apply a backup plan against a logical group, management of the data capture is performed one-by-one to the individual applications and there is no association among the applications in the group.

To add the instance to a logical group, you must [create a logical group](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups#create-lg) and then [protect the logical group](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups#protect-lg). The newly added logical groups and backup plans applied to logical groups are displayed after selecting the instances in the onboarding section.

You can add an instance to a logical group during onboarding:

  1. In the onboarding wizard, select an instance.
  2. Choose **Add to logical group**.
  3. Select the **Choose group** drop-down and pick a pre-created logical group.
  4. Complete the wizard to add the instance to the group.



Data capture and management operations, such as mount, clone, and restore, occur on individual applications within the group independently.

## Manage unmanaged and ignored instances

You can categorize instances as unmanaged or ignored to control their protection status.

### Unmanaged instances

  1. In the wizard, select the instance and choose **Add as Unmanaged**.
  2. To apply protection later, go to the **Applications** page.
  3. Filter by **Unmanaged**.
  4. Right-click the application and select **Manage Backup Plan**.
  5. Choose a Template and a Profile.



### Ignored instances

  1. In the wizard, select the instance and choose **Mark as Ignored**.
  2. To protect an ignored instance later, go to **App Manager > Applications**.
  3. Apply the **Ignored** filter.
  4. Right-click the instance and select **Unignore application**.
  5. Right-click the instance again and select **Manage Backup Plan** to apply a template and profile.



## Troubleshoot

To find methods for diagnosing and resolving errors, see [Troubleshoot conflicts when adding backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/troubleshoot-conflicts-when-adding-appliances).

## What's next

  * [Check for the cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backup images of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
