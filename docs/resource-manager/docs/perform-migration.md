---
url: https://docs.cloud.google.com/resource-manager/docs/perform-migration/
title: Perform the migration \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:28.108330+00:00
---

# Perform the migration  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/perform-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Perform the migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides the steps to migrate a Google Cloud project from one organization resource to another, or from no organization resource into an organization resource.

To migrate a project, you must ensure you have the correct (Identity and Access Management (IAM)) permissions and that specific organization policies are configured on both the source and destination resources.

## Before you begin

A project migration is a cross-organization operation. To prevent unauthorized movement of resources, you must satisfy the following requirements.

### Required roles

To get the permissions that you need to migrate projects between organization resources, ask your administrator to grant you the following IAM roles: 

  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project you want to migrate between organization resources
  * [Project Mover ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectMover) (`roles/resourcemanager.projectMover`) on the project's parent resource (folder or organization resource)
  * If the destination resource is a folder: [Project Mover ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectMover) (`roles/resourcemanager.projectMover`) on the destination resource 
  * If the destination resource is an organization: [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`) on the destination resource 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

These roles must be granted to the same user account in both the source and destination organizations. These predefined roles contain the permissions required to migrate projects. To see the exact permissions that are required, expand the **Required permissions** section.

### Required permissions

The following permissions are required to migrate projects:

  * `resourcemanager.projects.getIamPolicy` on the project you want to migrate between organization resources
  * `resourcemanager.projects.update` on the project you want to migrate between organization resources
  * `resourcemanager.projects.move` on the project's parent resource (folder or organization resource)
  * **If the destination resource is a folder:** `resourcemanager.projects.move` on the destination resource
  * **If the destination resource is an organization resource:** `resourcemanager.projects.create` on the destination resource
  * **If you want to migrate a project that is not associated with an organization:** `resourcemanager.projects.setIamPolicy` on the project you want to migrate



You can also gain these permissions with a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or other predefined roles.

### Required organization policies

By default, project migration is restricted. You must explicitly allow the export and import by setting organization policies at the root of both organizations. To configure organization policies required for the migration, you must have the `roles/orgPolicy.policyAdmin` role on the parent and the destination organization.

  * On the source organization resource: Set the `constraints/resourcemanager.allowedExportDestinations` policy. Add the ID of the _destination_ organization as an allowed value.

  * On the destination organization resource: Set the `constraints/resourcemanager.allowedImportSources` policy. Add the ID of the _source_ organization as an allowed value.


**Caution:** If these policies are not enforced, the migration command returns a `FAILED_PRECONDITION` error.**Note:** Whether you are using [dedicated import and export folders](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan#import_export_folders) or not, it is good practice to remove these organization policies after you are done moving projects across organization resources. You can enforce them again if you need to perform another project migration.

## Perform the migration

Once permissions are granted and policies are enforced, you can migrate the project using the Google Cloud CLI or the Resource Manager API.

**Note:** The following instructions are only for migrating a project from one organization resource to another organization resource. If the project you want to migrate is not associated with an organization resource, see [Migrating projects with no organization resource](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases#migrating_projects_no_org).

###  gcloud 

To migrate a project to another organization resource, run the following command:
    
    
    gcloud beta projects move PROJECT_ID \
        --organization ORGANIZATION_ID
    

You can also specify a folder as the target resource, with the following command:
    
    
    gcloud beta projects move PROJECT_ID \
        --folder FOLDER_ID
    

Replace the following fields:

  * PROJECT_ID: the ID or number of the project you want to migrate.
  * ORGANIZATION_ID: the ID of the organization resource you are moving the project to.
  * FOLDER_ID: the ID of the folder you are moving the project to.



You can only specify one target, either a folder or an organization resource.

**Note:** You can execute this command regardless of your Google Cloud CLI scope.

###  API 

Using the v1 Resource Manager API, you can migrate a project between organization resources by setting its `parent` field to the ID of the destination resource.

To migrate a project, do the following:

  * Get the `project` object using the `projects.get()` method.
  * Update the `parent` field to the destination resource ID.
  * Execute the `projects.update()` method.



The following code snippet demonstrates these steps:
    
    
        project = crm.projects().get(projectId=flags.projectId).execute()
        project['parent'] = {
            'type': 'organization',
            'id': flags.organizationId
        }
    
        project = crm.projects().update(
        projectId=flags.projectId, body=project).execute()
    

**Note:** It generally takes less than a minute for the project migration to complete. After migrating a project between organization resources, it may take several minutes to reflect this change in the Google Cloud console. For information about finding the current details of a project, see [Get an existing project](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#get_existing_project).

## Post-migration tasks

After successfully migrating your project, you must perform several post-migration tasks to ensure continuity of operations, security compliance, and proper billing. Migrating a project changes its resource hierarchy, which affects inherited permissions and organization-level policies.

Here are some steps that you can complete post migration:

  1. Policy verification: Verify that the project is inheriting the expected organization policies from its new parent.

  2. Access control: Audit IAM roles to ensure users in the new organization have the necessary access.

  3. Billing: Update the billing account if the project needs to be billed to the destination organization. This is an optional step. For details, see [Change the billing account for a project](https://docs.cloud.google.com/resource-manager/docs/perform-migration#change_billing_account) and [Migrate a billing account between organization resources](https://docs.cloud.google.com/resource-manager/docs/perform-migration#migrating_existing_billing_accounts).

  4. Cleanup: Revoke the temporary Project Mover roles and remove the `allowedExportDestinations` and the `allowedImportSources` constraints."




### Change the billing account for a project

Cloud Billing accounts can be used across organization resources. Moving a project from one organization resource to another won't impact billing, and charges will continue against the old billing account. However, migration of projects between organization resources often also include a requirement to migrate to a new billing account.

To change the billing account, do the following:

  1. Go to the **Billing page** in the Google Cloud console.  
[Go to the Billing page](https://console.cloud.google.com/billing)
  2. Click the name of the billing account you want to change.
  3. Under **Projects linked to this billing account** , find the name of the Project to migrate and then click the menu button to the right.
  4. Click **Change billing** , and then select the new billing account.
  5. Click **Set account**.



Charges already incurred that have not yet been reported in the transaction history will be billed to the former billing account. This can include charges from up to two days prior to when the project was migrated.

**Note:** If you change the billing account attached to a project which has active Google Cloud Marketplace subscriptions, those subscriptions are automatically canceled. For more information, see [Managing billing for Cloud Marketplace products](https://docs.cloud.google.com/marketplace/docs/manage-billing).

### Migrate a billing account between organization resources

A billing account can be migrated from one organization resource to another, although this isn't often a necessary step. Most existing organization resources will already have a billing account that should be used instead.

If a new billing account has no organization resource associated with it, you must get the `roles/billing.admin` role on the billing account and the `roles/billing.admin` and `roles/billing.creator` roles on the organization resource that you want to associate with your billing account.

If you need to migrate an existing billing account:

  1. In the Google Cloud console, go to the **Billing page**.  
[Go to the Billing page](https://console.cloud.google.com/billing)
  2. Click the name of the billing account you want to migrate.
  3. At the top of the **Account Management** page, click **Change organization**.
  4. Select the destination organization resource, and then click **Ok**.



The billing account is now associated with the specified organization resource.

## Roll back a migration

Google Cloud migrations between organizations don't automatically roll back if an issue occurs during or after the migration. If you need to revert a migration, you must manually perform a rollback.

If you have mistakenly migrated a project, you can roll back the operation by performing the migration again, with the old source as the new destination, and the old destination as the new source. You must have the necessary IAM permissions and organization policies enforced to allow this as if this were an entirely new migration.

To reverse a migration, do the following:

  1. Swap the source and destination IDs in your Organization Policies (`allowedExportDestinations` and `allowedImportSources`).
  2. Repeat the migration command, moving the project back to the original source ID.

**Note:** To roll back a migration for a project that originally had "No organization, contact [Google Cloud Customer Care](https://docs.cloud.google.com/support).

## What's next

  * [Handle special cases](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
