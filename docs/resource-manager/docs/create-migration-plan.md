---
url: https://docs.cloud.google.com/resource-manager/docs/create-migration-plan/
title: Create a migration plan \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:55:58.662475+00:00
---

# Create a migration plan  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/create-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Create a migration plan Stay organized with collections  Save and categorize content based on your preferences. 

A project migration plan lets you evaluate organization readiness and prevent service disruptions before you move a project between organization resources. An inventory of active services and dependencies also helps you anticipate how the destination resource hierarchy affects your workloads.

During a move, the Cloud Resource Manager API treats the project and its underlying services as a single unit without internal configuration changes. However, inherited allow, deny, and organization policies don't migrate with the project, while directly attached policies and service accounts persist. This hierarchy change can cause unexpected behavior or trigger [organization policy violations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#violations) in the destination organization.

### Inventory overview

Use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) to create an overview of resources in use, including allow policies. You can use this overview to help outline your migration plan.

You can also use Cloud Asset Inventory to transfer this data into BigQuery. This will allow you to query the data using SQL, which is easier to read compared to interpreting JSON-formatted data. For information about exporting this data, see [Exporting to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery).

To get a list of all allow and deny policies that affect access to a project, see [View all allow and deny policies that apply to a resource](https://docs.cloud.google.com/iam/docs/troubleshoot-policies#applicable-policies). 

### Policy verification

When you migrate your project, it will no longer inherit the policies from its current place in the resource hierarchy, and will be subject to the effective policy evaluation at its destination. We recommend making sure that the effective policies at the project's destination match as much as possible the policies that the project had in its source location.

Any policy that is applied directly to the project will still be attached after the migration is complete. Applying policies directly to the project is a good way to verify that the correct policies are applied from the moment the migration is complete.

Allow, deny, and organization policies are inherited through the resource hierarchy, and can block a service from functioning if not set properly. Determine the effective policy at the project's destination in your resource hierarchy to ensure the policy aligns with your governance objectives.

### Manage encrypted keys

You should verify if your project has a customer-managed encrypted key or other Cloud Key Management Service enabled on it. Cryptographic keys are owned by the project, and a user with `owner` access to that project will therefore be able to manage and perform cryptographic operations on keys in Cloud KMS in that project.

For more information, see [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties).

### Preview features

You can enable preview features on organization resources, folders, or projects. If you have enabled an alpha or beta feature on the project to be migrated, this feature should continue to function after the migration. If the preview feature is private and not added to the allowlist for the destination organization resource, you won't be able to make any configuration changes after the migration is complete.

### Identify the new billing account

Cloud Billing accounts can be used across organization resources. Moving a project from one organization resource to another doesn't impact billing. Charges continue against the old billing account. However, migration of projects between organization resources often also includes a requirement to migrate to a new billing account.

As part of your migration plan, determine whether to keep existing billing accounts. You can also associate projects with a new billing account in the destination organization resource.

To learn how to change or migrate a billing account, see [Change the billing account](https://docs.cloud.google.com/resource-manager/docs/configure-org-policy#change_billing_account).

### Rollback plan

If you discover that something is not working on any of the projects you have migrated, you can restore them to their original location. In order to do that, you need to have the necessary IAM permissions and set the required organization policies so that you can run the project migration in reverse.

For a list of permissions required, see [Assign permissions](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-roles). For the organization policies you need to configure to allow a project migration, see [Configure organization policies](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-org-policies).

### Dedicated import and export folders

Policy inheritance can cause unintended effects when you are migrating a project, both in the source and destination organization resources. You can mitigate this risk by creating specific folders to hold only projects for export and import, and ensuring that the same policies are inherited by the folders in both organization resources. You can also set permissions on these folders that will be inherited to the projects moved within them, helping to accelerate the project migration process.

When planning a migration, consider setting up a dedicated source folder first. To do this, create a folder for each destination organization resource to which you plan to export projects. Then, set an organization policy on these folders, each with the `constraints/resourcemanager.allowedExportDestinations` constraint set to the single organization resource to which you want to export projects.

**Note:** To configure organization policies required for the project migration, you must have the `roles/orgPolicy.policyAdmin` role on the parent and the destination organization.

For example, you could set up `Export to Marketing Org` and `Export to Sales Org` folders, each with appropriate organization policy constraints set.

Similarly, set up dedicated import folders in the destination organization resource, one for each organization resource from which you want to import projects. To do this, create a folder for each source organization resource from which you plan to import projects. Then, set an organization policy on these folders, each with the `constraints/resourcemanager.allowedImportSources` constraint set to the single organization resource from which you want to import projects.

For example, you could set up `Import from Marketing Org` and `Import from App Development Org` folders, each with appropriate organization policy constraints set.

On each of the import and export folders, assign the person who will be moving the projects the `roles/resourcemanager.projectMover` role. This role will be inherited by any projects that are contained within these folders, giving the user the ability to perform the move operations on any project that is moved into those folders.

After you have completed your project migration, you should remove these dedicated folders.

For information about setting organization policies, see [Configure organization policies](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-org-policies).

## What's next

To assign Identity and Access Management roles and permissions for migrating projects between organizations, see [Assign Identity and Access Management roles and permissions](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-roles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
