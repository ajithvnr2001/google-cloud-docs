---
url: https://docs.cloud.google.com/data-studio/link-pro-to-a-google-cloud-project-mau-version/
title: Link a Data Studio Pro monthly active user subscription to a Google Cloud project \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:00.237596+00:00
---

# Link a Data Studio Pro monthly active user subscription to a Google Cloud project  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/link-pro-to-a-google-cloud-project-mau-version/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Link a Data Studio Pro monthly active user subscription to a Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

**Intended audience** : This document is intended for Cloud Identity or Google Workspace administrators whose organization has a Data Studio Pro subscription that was set up for them by Google Sales or a Google reseller partner with Monthly Active User pricing. If your organization is not already using Data Studio Pro, or if your subscription was set up using the self-service, division-based pricing model, this document doesn't apply to you. [Learn more about the Data Studio Pro self-service upgrade process](https://docs.cloud.google.com/data-studio/upgrade-content-pro). **Note:** With an MAU subscription, the **Pro subscription** page in the Data Studio left navigation isn't available, and you don't need it. Your subscription is set up and changed by your Google Cloud sales specialist and covers everyone in your organization, so you don't assign Pro licenses to individual users, either in Data Studio or in the Google Workspace Admin console. To set up Pro, link the subscription to a Google Cloud project by following the steps on this page.

In Data Studio, individual users own the assets (reports, data sources, and explorations) that they create or that have been transferred to them. To keep Data Studio assets working after their owner leaves an organization, an administrator must transfer those assets to another user. Otherwise, those assets will likely be deleted and the departing user's data credentials will be revoked, breaking that user's reports and data sources.

Data Studio Pro assets, on the other hand, are [organized hierarchically](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), with your Cloud Identity or Google Workspace organization as the ultimate owner. Organizational ownership ensures that your Data Studio assets continue to work even if their individual owner leaves the organization.

Specifically, organizational ownership offers the following benefits:

  * All the Data Studio assets that your users create are stored in a Google Cloud project that you control and manage.
  * Data Studio Pro assets are protected from deletion should their creator leave your organization.
  * You can use IAM to assign project-level permissions that apply to all Data Studio Pro assets in your organization.



## Use Data Studio Pro in your organization

To use Data Studio Pro in your organization, you'll need to link Data Studio Pro to a Google Cloud project. Optionally, you can add principals on the project to manage Data Studio assets.

### Link to a Google Cloud project

To complete this step, you'll provide a Google Cloud project which you'll use to manage Data Studio assets. This project will also be used to bill your organization for your Data Studio Pro subscription.

#### Cloud project requirements

Choose your Google Cloud project carefully. Once Data Studio is linked to your project, you can't move your Data Studio assets to another project. We recommend using a project dedicated to Data Studio. 

  * The project that you choose must use the same billing account that your organization uses for your Data Studio subscription.
  * When you set up organizational ownership of Data Studio Pro assets, Google Cloud automatically creates a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on the project to prevent accidental deletion of those assets. Be sure you have the `resourcemanager.projects.updateLiens` permission, which is granted by the `roles/lookerstudio.proManager`, `roles/resourcemanager.lienModifier`, and `roles/owner` roles, so that Google Cloud can create the lien for you.
  * The user who performs the upgrade to Data Studio Pro must have the [Services Admin](https://support.google.com/a/answer/2405986#services_admin) role in Google Workspace, or another role that grants them the `Manage Data Studio Settings` privilege in the organization that owns the project.
  * The user who performs the upgrade to Data Studio Pro must have the [**Data Studio Pro Manager** role](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`) or the [**owner** role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) for the project. We recommend using the Data Studio Pro Manager role to follow the principle of least privilege.



**For resellers** : The resold customers will need to provide a project that is linked to the billing account of the reseller subscription.

See the best practices section for additional tips before proceeding.

### Steps

  1. [Sign in](https://admin.google.com/) with an administrator account to the **Google Admin console**.

**Note:** If you aren't using an administrator account, you can't access the Admin console.
  2. In the Google Cloud console, go to **Billing** and then select [My Projects](https://console.cloud.google.com/billing/projects).

  3. Locate the project that you want to use for Data Studio asset management and billing and make a note of its project ID.

  4. [Sign in to Data Studio.](https://datastudio.google.com)

  5. In the top right, click the **Settings** (gear) icon and select **Enterprise Admin**.

  6. In the settings dialog, click **Project ownership**.

  7. In the **Project ID** field, enter your Google Cloud project ID.




### Optional: Add principals to the project

Individual Data Studio users DO NOT need to be added to the project. However, if you want to allow others in your organization to manage the Data Studio project, you can add principals to that project using the [IAM resource manager](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) in the Google Cloud console. See the best practices section for advice.

You can grant principals the following IAM roles:

Role  |  Description   
---|---  
Data Studio Admin  ( ` roles/datastudio.admin ` )  |  Includes all permissions to reports and data sources.   
Data Studio Asset Viewer  ( ` roles/datastudio.viewer ` )  |  Includes view permissions to reports and data sources.   
Data Studio Asset Editor  ( ` roles/datastudio.editor ` )  |  Includes edit permissions to reports and data sources. Does not include delete permissions.   
  
Keep the following information in mind while granting roles to principals:

  * Data Studio does not support custom roles.
  * To see the individual IAM permissions that each role includes, see the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).



## Best practices

We recommend the following best practices when you're setting up your Data Studio Pro project:

### Create a separate Google Cloud project for your Data Studio Pro assets

It's a good idea to create a dedicated project to manage Data Studio Pro assets. Keeping this project separate from your other projects helps make it clear what the project is used for and helps prevent accidental deletion of your assets.

### Limit the number of principals on the project

Keep the number of people you add to the project to a minimum. Remember, access to the project is NOT a requirement to use Data Studio. Instead, think about Data Studio project access as a way to delegate administrative functions to a select few individuals.

### Follow the principle of least privilege

If you add people to the project, grant them the minimum role that is required to manage your Data Studio assets according to your organization's policies.

Use the roles that are specific to Data Studio. **Don't use IAM basic roles**. Basic roles include thousands of permissions across all Google Cloud services. In production environments, don't grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles that meet your needs.

Learn more about how to [use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely).

## Organization changes

If you've linked Data Studio Pro to a project in one organization and later want to transfer that project to a different organization, do the following:

**Important:** If you migrate a Google Cloud project with an active Data Studio Pro subscription to a new Google Cloud organization, you might not be able to manage Pro licenses. For more information, see License management error after project migration.

  1. [Sign in](https://admin.google.com/) with an administrator account to the **Google Admin console**.

**Note:** If you aren't using an administrator account, you can't access the Admin console.
  2. Complete the setup of the new organization in Google Cloud console.

  3. Migrate the original project, users, and resources from the old organization to the new organization. Learn more about [migrating projects](https://docs.cloud.google.com/resource-manager/docs/project-migration).

  4. [Sign in to Data Studio.](https://datastudio.google.com)

  5. In the top right, click the **Settings** (gear) icon and select **Enterprise Admin**.

  6. In the settings dialog, click **Project ownership**.

  7. In the **Project ID** field, enter your Google Cloud project ID.

**Important:** This MUST be the same project that was used by the old organization.
  8. Click **Link project**.




For other transfer scenarios, please contact [Cloud Customer Care](https://docs.cloud.google.com/support) for assistance.

## Limits of Google Cloud project linking

  * You can link Data Studio to only one project.
  * Once Data Studio is linked to your project, you can't link it to another project. If you must change the project that is linked to your Data Studio Pro subscription, you must work with a Google Cloud sales specialist to cancel your current subscription and create a new one. Canceling a subscription requires you to manually migrate your Data Studio Pro assets.
  * Because Data Studio Pro projects have a Google Cloud lien placed on them, your assets are protected from accidental deletion. If you delete a project, all Data Studio Pro assets in that project are marked for deletion. If you [restore the project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#restoring_a_project) within 30 days, your Data Studio Pro assets will be recovered automatically. Restoring a Google Cloud project automatically recovers your linked Data Studio Pro assets without manual intervention. This backend synchronization process can take up to four days to complete. Verify your Data Studio Pro subscription status and allow up to four days for the reports to reappear before contacting support.



## License management error after project migration

When a Google Cloud project with an active Data Studio Pro subscription is migrated to a new Google Cloud organization, the existing licensed users from the previous organization are detected as "outside org users". By default, Data Studio Pro requires licensed users to belong to the same organization that owns the Google Cloud project used for the subscription. This might prevent you from being able to add or remove users.

To resolve this issue, you can use one of the following options:

  * Cancel the existing subscription, and create a new subscription in the new organization. When you cancel a subscription, you must remove all users who hold an active license from the previous organization.
  * Submit a request to [Cloud Customer Care](https://docs.cloud.google.com/support) to enable the **Trusted Orgs** feature. This lets you add the previous organization's domain as a trusted organization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
