---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval/
title: Protect project liens by using Privileged Access Manager \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:43.151986+00:00
---

# Protect project liens by using Privileged Access Manager  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect project liens by using Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Beginning November 1, 2026, Backup and DR will automatically apply a project-level lien to any project containing a backup vault with backups protected by enforced retention.

Project liens are guardrails that explicitly block a project from being deleted. This tutorial describes how to configure a multi-party approval workflow to protect your project liens on Google Cloud projects that contain backup vaults.

Applying a [project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) adds an essential layer of protection against accidental or unauthorized project deletion. However, principals with legacy basic permissions for project ownership can remove the lien and delete the project. To prevent any single user from unilaterally removing project liens, you can establish a structured multi-party approval workflow. Privileged Access Manager (PAM) provides just-in-time, temporary privilege elevation with multi-party approval workflows. For more information, see the [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview).

By leveraging Privileged Access Manager, your organization ensures that critical permissions—specifically the ability to remove liens—are granted only temporarily and require explicit approval from an authorized second party.

This tutorial assumes that you are familiar with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview), [project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens), and [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/overview).

## Objectives

  * Audit existing Identity and Access Management roles to restrict project lien modifications.
  * Create a custom Identity and Access Management role for lien administration.
  * Configure a Privileged Access Manager entitlement for multi-party approval.
  * Request, approve, and execute temporary lien deletion.
  * Clean up resources created in this tutorial.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Privileged Access Manager (PAM)](https://cloud.google.com/iam/pricing#pam)
  * [Backup and DR](https://cloud.google.com/backup-disaster-recovery/pricing)



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

## Before you begin

  1. Select or create a Google Cloud project:

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Ensure that billing is enabled for your Google Cloud project. For more information, see [Confirm the billing status of your project](https://support.google.com/cloud/answer/6293499#enable-billing).

  3. Enable the Privileged Access Manager and Resource Manager APIs:

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=privilegedaccessmanager.googleapis.com,cloudresourcemanager.googleapis.com)

  4. Ensure you have the following Identity and Access Management roles:

     * **Security Admin** (`roles/iam.securityAdmin`) or **Organization Administrator** (`roles/resourcemanager.organizationAdmin`) on the organization or folder: required to audit and modify role assignments.

     * **Organization Role Administrator** (`roles/iam.organizationRoleAdmin`): required to create custom IAM roles.

     * **Privileged Access Manager Admin** (`roles/privilegedaccessmanager.admin`): required to create and configure Privileged Access Manager entitlements.

     * **Project Lien Modifier** (`roles/resourcemanager.lienModifier`): required to create or remove project liens.




When you finish this tutorial, you can avoid continued billing by deleting the resources you created. See Clean up for more detail.

## Audit existing Identity and Access Management roles

The legacy basic Owner role (`roles/owner`) contains the permission `resourcemanager.projects.updateLiens` (allows removal of project liens) by default. Similarly, the Project Lien Modifier role (`roles/resourcemanager.lienModifier`) also grants lien removal permissions. To ensure multi-party approval cannot be bypassed, verify that no unauthorized user has permanent access to modify or delete liens.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select your organization, folder, or project.

  3. Review the list of principals and their assigned roles.

  4. Remove the **Project Lien Modifier** (`roles/resourcemanager.lienModifier`) role from all principals who should not have permanent lien deletion access.

  5. Ensure users are not assigned the legacy basic **Owner** role (`roles/owner`). Instead, assign them the legacy basic **Editor** role (`roles/editor`) or custom roles that don't contain lien modification capabilities.




## Create a custom Identity and Access Management role for lien administration

Because Privileged Access Manager does not support granting legacy basic roles (Owner, Editor, and Viewer), create a dedicated custom role with only the `resourcemanager.projects.updateLiens` permission to enforce the principle of least privilege during temporary elevation.

  1. In the Google Cloud console, go to the **Roles** page.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Select your organization or project from the project selector.

  3. Click **Create Role**.

  4. In the **Title** field, enter `Lien Administrator`.

  5. In the **ID** field, enter `lien_administrator`.

  6. In the **Role launch stage** list, select **General Availability**.

  7. Click **Add Permissions**.

  8. In the **Filter permissions** box, search for `resourcemanager.projects.updateLiens`.

  9. Select the checkbox next to `resourcemanager.projects.updateLiens`, and then click **Add**.

  10. Click **Create**.




## Configure a Privileged Access Manager entitlement

Configure a Privileged Access Manager entitlement to define who can request the Lien Administrator custom role, the required approvers, and the maximum grant duration.

  1. In the Google Cloud console, go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements)

  2. In the **Entitlements** tab, click **Create Entitlement**.

  3. In the **Entitlement details** section, configure the following:

     * **Entitlement ID** : Enter a unique name (for example, `remove-project-lien`).

     * **Resource** : Select the organization, folder (recommended), or specific project where you want this policy to apply.

  4. In the **Role** section, select the **Lien Administrator** custom role (`lien_administrator`) created in the previous task.

  5. In the **Requesters** section, select the individual principals or groups allowed to request elevated access (for example, `devops-team@example.com`).

  6. In the **Approval workflow** section, select **Approval required** , and then configure the following settings:

     * **Approvers** : Select the individual principals or groups who must approve requests (for example, `security-leads@example.com`).

     * **Approver count** : Enter `1` or the number of approvals required by your organizational policy.

  7. In the **Grant duration** section, set the **Maximum duration** (for example, `1 hour`).

  8. In the **Justification** section, select **Required**.

  9. Click **Create**.




## Request, approve, and execute lien deletion

After the entitlement is configured, users must request temporary elevated access and receive approval before they can delete a project lien.

### Request elevated access

  1. In the Google Cloud console, go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements)

  2. Locate the `remove-project-lien` entitlement, and then click **Request grant**.

  3. In the **Duration** field, enter the required duration (up to the maximum configured duration).

  4. In the **Justification** field, enter the business justification for removing the project lien.

  5. Click **Submit request**.




### Approve the access request

  1. As an authorized approver, open the approval notification email or in the Google Cloud console, go to the **Privileged Access Manager**. Then, click **Approvals**.

[Go to Approvals](https://console.cloud.google.com/iam-admin/pam/approvals)

  2. Select the pending request.

  3. Review the requester details, requested duration, and justification.

  4. Click **Approve**.




### Delete the project lien

Once approved, Privileged Access Manager temporarily binds the Lien Administrator role to the requester. The requester can now delete the project lien.

  1. In the Google Cloud console, activate Cloud Shell or open a terminal with the gcloud CLI installed.

  2. List the active liens on your project:
         
         gcloud alpha resource-manager liens list --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  3. Delete the project lien:
         
         gcloud alpha resource-manager liens delete LIEN_NAME
         

Replace `LIEN_NAME` with the name of the lien from the previous command (for example, `liens/p12345-l67890`).




After the configured grant duration expires, Privileged Access Manager automatically revokes the Lien Administrator role from the requester, preventing any further lien modifications.

**Note:** This multi-party approval process can also be used to manage and restrict modifications to backup vault configurations and backup plan settings.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the Privileged Access Manager entitlement and the custom Identity and Access Management role.

### Delete the Privileged Access Manager entitlement

  1. In the Google Cloud console, go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements)

  2. In the entitlements list, select the checkbox next to `remove-project-lien`.

  3. Click **Delete**.

  4. In the confirmation dialog, click **Delete**.




### Delete the custom IAM role

  1. In the Google Cloud console, go to the **Roles** page.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. In the roles list, locate the `lien_administrator` role.

  3. Click the **Actions** menu (three dots) next to the role, and then click **Delete**.

  4. In the confirmation dialog, click **Delete**.




### Delete the project

The easiest way to eliminate billing is to delete the project you created for the tutorial.

**Caution:** Deleting a project permanently removes all resources and work within that project. If you used an existing project for this tutorial, delete only the specific resources created instead of deleting the entire project.

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. In the dialog, enter the project ID, and then click **Shut down** to delete the project.




## What's next

  * [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)
  * [Configure cyber resilience for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/best-practices-cyber-resilience)
  * [Protect projects with project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens)
  * [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview)
  * [Request temporary elevated access using Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access)
  * Try out other Google Cloud features for yourself. Have a look at our [tutorials](https://cloud.google.com/docs/tutorials). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
