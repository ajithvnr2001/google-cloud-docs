---
url: https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects/
title: Delete and restore projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:27.974401+00:00
---

# Delete and restore projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Delete and restore projects Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to shut down and restore Google Cloud projects. Understand the 30-day recovery window, resource deletion timelines, and how to prevent data loss.

## Shut down (delete) a project

Shutting down a project stops all billing and resource usage. This action immediately moves the project into a 30-day recovery period, after which the project and all associated data are permanently deleted. Only projects with a lifecycle state of `ACTIVE` can be shut down.

**Deletion process and timeline**

When you initiate a shutdown, the following events occur:

  1. Immediate shutdown: The project is immediately marked for deletion and becomes unusable.

  2. Notification: Google Cloud sends a notification email to the user who initiated the deletion and to any contacts listed in the Technical category of [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

**Note:** Deletion proceeds even if notification emails can't be delivered. If no Technical contact is specified, fallback contacts aren't notified.
  3. Billing disconnection: Any associated Cloud Billing account is disconnected. This association isn't automatically reinstated if the project is later restored.

  4. 30-day recovery window: The project remains in a `DELETE_REQUESTED` state for 30 days. During this period, project owners can restore the project.

  5. Permanent deletion: After 30 days, the project and all its resources are permanently deleted and can't be recovered.




**Track deletion progress**

After you initiate a shutdown, you can use the `gcloud projects describe` command to track the progress of the 30-day deletion period:
    
    
    gcloud projects describe PROJECT_ID
    

The output displays the `lifecycleState` and other project details, as shown in the following example:
    
    
    createTime: '2025-06-14T10:00:00.000Z'
    lifecycleState: DELETE_REQUESTED
    name: Test Project
    parent:
      id: '123456789012'
      type: folder
    projectId: Test Project
    projectNumber: '987654321098'
    

**Critical considerations**

Before shutting down a project, review the following risks:

  * Resource recovery: While most resources are recoverable within the 30-day window, some services—such as [Cloud Storage](https://docs.cloud.google.com/storage/docs/projects#project-deletions) and Pub/Sub—might delete resources much sooner. These might not be fully recoverable even if the project is restored.

  * Restoration delays: If you restore a project, some services may take up to 36 hours to fully resume operations.

  * Project IDs: Project IDs are unique and permanent. Once a project is fully deleted, its ID can't be reused. If you want to preserve a custom project ID for future use, delete the resources within the project instead of shutting down the project itself.

  * Project quota: Until a project is permanently deleted (after the 30-day window), it continues to count toward your project quota.

  * Billing charges: Projects may continue to incur charges until the current billing cycle ends. To avoid unexpected charges, [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) manually before initiating a shutdown.

  * **Active Committed Use Discounts (CUDs)** : If you have active CUDs in a project, deleting the project can lead to unexpected billing issues or cancellation of the discounts. To prevent accidental deletion of projects with active CUDs, we recommend applying [project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).




**Safeguards**

To prevent accidental deletion of business-critical projects, you can enable [change risk recommendations](https://docs.cloud.google.com/recommender/docs/change-risk-recommendations). These recommendations provide warnings when you attempt to delete projects that Google Cloud has identified as important based on recent activity.

To learn more about data retention and safe deletion, see [How Google retains data we collect](https://policies.google.com/technologies/retention).

You can shut down projects using the Google Cloud console, Google Cloud CLI, or the API.

###  Console 

  1. In the Google Cloud console, go to the IAM & Admin **Settings** page. 

[Go to IAM & Admin Settings](https://console.cloud.google.com/iam-admin/settings?walkthrough_id=resource-manager--shutdown-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. On the **IAM & Admin Settings** page, select the project you want to delete, and then click **Shut down**. 

**Shut down** only appears for users who have the `resourcemanager.projects.delete` permission in the current project.

  3. Click **Shut down**. 
  4. Enter the project ID, and then click **Shut down anyway**.



Alternatively, you can delete a project from the **Manage resources** page:

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. Select the project you want to delete.

  3. Click **Delete**.

  4. Enter the project ID and click **Shut down**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To delete a project, use the [`gcloud projects delete`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/delete) command:
         
         gcloud projects delete PROJECT_ID
         

Where PROJECT_ID is the ID of the project you want to delete.




###  REST 

The following code snippet deletes the specified project:

Request:
    
    
    DELETE https://cloudresourcemanager.googleapis.com/v3/projects/my-project-123
    

### Troubleshoot project deletion

If you encounter issues while attempting to shut down or restore a project, it's typically due to permission constraints or specific resource "liens." For information, see [Troubleshoot project deletion](https://docs.cloud.google.com/resource-manager/docs/troubleshooting-project-deletion).

## Restore a project

Project owners can restore a deleted project within the 30-day recovery period that begins when the project is shut down.

Restoring a project returns it to its state prior to shutdown, with the following exceptions:

  * Billing is disabled on the project when the project is shut down. It isn't automatically re-enabled upon restoration. You must [manually link the project to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project). You might need to wait a few hours before you can successfully link a recently restored project to a billing account.

  * You can recover most resources if you restore a project within the 30-day period. Some services such as Cloud Storage or Pub/Sub might delete data sooner than 30 days. For example, [Cloud Storage resources that are protected by soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) might be deleted after **7 days** , depending on the soft delete retention duration, but buckets that have soft delete disabled might be deleted immediately and might not be recoverable. The success rate of resource recovery is linked to the dependencies of those resources.

  * It can take up to 36 hours for all services within a restored project to become fully functional. In particular, **OAuth clients** may take **1 to 3 days** to be fully operational after a project is restored. If your resources aren't restored after this period, reach out to [Google support](https://console.cloud.google.com/support).

  * Some services might need to be restarted manually. For more information, see [Restarting Google Cloud Services](https://docs.cloud.google.com/billing/docs/how-to/restart-services).




To restore a project, you must have the `resourcemanager.projects.undelete` permission on the project. To view projects pending deletion in the console, you also need the following permissions:

  * `resourcemanager.projects.list`
  * `resourcemanager.folders.list` (if the project is in a folder)
  * `resourcemanager.projects.get`



To restore a project, use one of the following methods:

###  Console 

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the **Project picker** at the top of the page, select your organization resource.

  3. Below the list of organization resources, folders, and projects, click **Resources pending deletion**.

  4. Select the checkbox for the project you want to restore, and then click **Restore**. In the dialog that appears, confirm that you want to restore the project.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To restore a project, use the [`gcloud projects undelete`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/undelete) command:
         
         gcloud projects undelete PROJECT_ID
         

PROJECT_ID is the project ID or project number of the project you want to restore.




###  REST 

The following code snippet restores the specified project:

Request:
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/projects/my-project-123:undelete
    

## What's next

  * Learn how to [move a project within your resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders).
  * Learn how to [migrate a project from one organization resource to another](https://docs.cloud.google.com/resource-manager/docs/project-migration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
