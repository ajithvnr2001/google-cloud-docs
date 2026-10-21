---
url: https://docs.cloud.google.com/resource-manager/docs/organization-setup/
title: Organization resource setup wizard \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:56:51.794139+00:00
---

# Organization resource setup wizard  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)



Send feedback 

#  Organization resource setup wizard Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Organization setup wizard makes it simple for you to establish and delegate administration of your organization resource. It also allows you to migrate existing projects and billing accounts into your new organization resource.

To get started with the Organization setup wizard:

  1. Acquire an organization resource. For detailed instructions, see [Getting an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring).

  2. Assign Organization, Billing, and Network Administrators for your Google Cloud organization resource. For detailed instructions, see [granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




To start the migration process:

  1. Send the project and billing migration request to Project owners.

  2. Wait for Project owners to confirm the migration request.

  3. Approve project and billing account migration.




This guide provides instruction about how to migrate projects and billing accounts using the Google Cloud setup wizard. For more information about using Resource Manager, see [Migrating projects](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing).

Associating projects or billing accounts with an organization resource allows central control of all resources in the organization resource. To learn more, see [benefits of the organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#benefits_of_the_organization_resource).

The sections below provide detailed instructions for the above steps.

## Migrate existing projects and billing accounts

After an organization resource is created for your domain, all projects created under the organization resource will automatically belong to the organization resource. You can also migrate already existing projects into the organization resource.

  * If you're an owner or an editor of a project and a **Project Creator** for the organization resource, you can [migrate projects directly](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing).

  * If you're an Organization Administrator, you can request project owners give you control of a project so you can migrate it into your organization resource.




Project migration isn't reversible. After a project is associated with an organization resource, you can't change it back to **No organization** or move it to another organization resource on your own. If you need to move a project after it's associated with an organization resource, you'll need to contact [Google Cloud Premium Support](https://docs.cloud.google.com/support).

When a project is migrated to an organization resource, the Organization Administrator gains administrative control of the project and it inherits organization policies and Identity and Access Management (IAM) allow and deny policies. Read more about Policy implications.

When you move existing projects into an organization resource, they're billed like they were before the migration, even if the project's billing account hasn't been migrated yet. Similarly, if you move the billing account into an organization resource, all projects linked to it will continue to work even if they are still outside of the organization resource. You can link newly imported projects to a new or existing billing account in your organization resource at any time, without interruption of project functionality.

## Organization resource setup for super admins

### Create an organization resource

Before you delegate Google Cloud administrators and migrate projects and billing accounts, you must have an organization resource. To acquire an organization resource, sign up for Google Workspace or Cloud Identity, verify your domain, and then create a Project using that account. An organization resource will be automatically provisioned once the Project is created. For more information about acquiring an organization resource, see [Getting an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring).

### Delegate Google Cloud administrators

To delegate Google Cloud administrators:

  1. In the "Welcome to [ORGANIZATION_NAME] at Google Cloud" email, click **Go to My Console** or go to the [Organization Setup](https://console.cloud.google.com/iam-admin/org-onboarding/zerostate) page in the Google Cloud console.

  2. On the **Organization Setup** page, click **Delegate setup**.

  3. On the **Delegate Organization Administrator Role** page that appears, enter the email addresses of individuals or groups you want to add as **Organization Administrators**.

  4. When you're finished adding **Organization Administrators** , click **Delegate**.




The email addresses you entered will receive an email notification that they are now an **Organization Administrator** for your Google Cloud organization resource.

To add more administrators later, click **Set Permissions** on the [Identity & Organization](https://console.cloud.google.com/iam-admin/org-onboarding) page.

## Migration for Google Cloud administrators

When a Google Workspace or Cloud Identity account user delegates the **Organization Administrator** role to you through the organization resource setup process, you'll receive an email notification. During organization resource setup, you'll be able to assign permissions to other Organization, Billing, and Network Administrators. Individuals you assign as administrators won't receive an email.

You need the **Project Creator** role to request project and billing account migration. By default, all users in your domain are granted this role. For more information on changing this default behavior and granting users this role, see [Managing default organization roles](https://docs.cloud.google.com/resource-manager/docs/default-access-control).

### Migrate projects and billing accounts

To migrate projects or billing accounts from other user accounts, first you'll request the owners approve migration. The owners then receive a notification to review your request and approve projects or billing accounts for migration. Project owners can ignore your request and it will expire after 30 days. You can request migration again if the original request expires or is still pending. After an owner approves projects or billing accounts for migration, you'll receive a notification and select what you want to migrate.

### Request project or billing account migration

  1. Go to the Google Cloud console [Identity & Organization](https://console.cloud.google.com/iam-admin/org-onboarding/migration/request) page.

![Organization setup wizard UI](https://docs.cloud.google.com/resource-manager/img/onboarding-ui.png)

  2. In the **Request projects or billing accounts from** box, add the email addresses for the billing account or project owners you want to request projects from, then click **Request**.

![Request projects UI](https://docs.cloud.google.com/resource-manager/img/onboarding-request.png)




The billing account or project owners will receive an email with your request for migration. After they approve migration, you'll receive an email with a link to complete migration.

### Wait for migration request approvals

When you request project or billing account migration, the project or billing account owners receive an email with your request. They will be able to select the projects to set up for migration. Your request remains valid for up to 30 days. After 30 days, the request expires and you'll need to send a new migration request for any outstanding projects or billing accounts.

When a project or billing account owner confirms the migration request, you will receive an email and a notification will appear on your Google Cloud console. To approve migration, continue to the next step.

### Approve project and billing account migration

After an owner approves your migration request, you'll receive an email from Platform Notifications that the project owner has responded to your migration request, and a notification will appear on your Google Cloud console.

You will need the **Project Creator** , **Billing Account Creator** , and **Organization Administrator** roles on the organization resource to which you are migrating projects. To complete migration:

  1. Click **Migrate** in the email, or go to the [Migrate projects](https://console.cloud.google.com/iam-admin/org-onboarding/migration/accept) page in the Google Cloud console.

![Migrate projects page](https://docs.cloud.google.com/resource-manager/img/onboarding-migrate.png)

  2. On the **Select projects** and **Select billing accounts** tabs, select any combination of projects and billing accounts you want to migrate, then click **Next**.

  3. The **Review and approve** tab displays a list of all the projects and billing accounts you selected to migrate.

  4. To complete migration, click **Approve**.




The projects or billing accounts you selected to migrate are now associated with your organization resource. Any projects or billing accounts you didn't migrate will remain in the **No organization** list. You'll still have the Project Mover IAM role for those projects and the Billing Administrator role for those billing accounts. You can revisit the Google Cloud console [Migrate projects](https://console.cloud.google.com/iam-admin/org-onboarding/migration/accept) page to approve migration for those projects and billing accounts.

When you complete migration for a project, it's billed like it was before the migration, even if its billing account hasn't been migrated yet. Similarly, when you complete migration for a billing account, all projects linked to it will continue to work even if they're still outside of the organization resource.

## Reviewing migrate requests

When an Organization Administrator requests you to migrate a project or billing account to their organization resource, you'll receive a "Migrate request" email. When you approve migration, you grant the Organization Administrator the following roles:

  * Projects: `role/project.mover`

    * The Project Mover role allows a user to import projects and change the IAM permissions on those projects.
  * Billing accounts: `roles/billing.admin`

    * The Billing Administrator role allows a user to import billing accounts and change the IAM permissions on those projects.



After the Organization Administrator approves a migration, they can change IAM roles for the project and the project inherits existing organization policies. Read more about policy implications.

To review requests, follow the steps below:

  1. Click **Review Request** in the email to open the **Review migrate request** page.

  2. On the **Select projects** and **Select billing accounts** tabs, select any combination of projects and billing accounts you want to migrate to the organization resource, then click **Next**. It can take up to five minutes for the list of projects to be populated.

  3. The **Confirm** tab displays the following details about the migration:

     1. The email address of the Organization Administrator that you're granting the Project Mover and Billing Administrator roles.

     2. A confirmation list of all the projects and billing accounts you selected to migrate.

  4. To complete migration, enter the email address of the entity that made the migration request, then click **Confirm**.




The projects or billing accounts you selected to migrate are now available for the Organization Administrator to migrate into their organization resource.

If you want to stop the migration process for a project or billing account, you must do so before the Organization Administrator imports it into their organization resource. To stop migration, go to the Google Cloud console [IAM](https://console.cloud.google.com/projectselector/iam-admin/iam) page for the project and remove the Project Mover or Billing Administrator role from the Organization Administrator.

Any projects or billing accounts that you didn't select to migrate will remain with **No organization**. You can click the link in your "Migrate request" email to approve migration for up to 30 days. After 30 days, the migration request expires and the Organization Administrator will have to send a new migration request for you to review.

## Policy implications

IAM allow and deny policies that are already defined for a project are migrated with the project. This means that principals that have been granted roles on the project before a migration will have the same roles after the project is migrated. Principals that have had permissions denied using a deny policy will have the same permissions denied after the migration.

Because IAM roles are inherited and additive, roles that are defined at the organization level are inherited by projects when they migrate to the organization resource. For example, if `projectAuthor@myorganization.com` has the Project Editor role defined at the organization level, they will also have that role on any project that is migrated into the organization resource. This won't break anything in existing projects, but more users may gain access due to the inheritance.

Organization policies are also inherited down the hierarchy. By default, newly created organization resources don't have organization policies. If you define organization policies for your organization resource, make sure that projects you migrate are consistent with your organization policies.

**Key Point:** It's your responsibility to make sure that IAM and organization policies are consistent when you move a project into the organization resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
