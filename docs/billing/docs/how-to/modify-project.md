---
url: https://docs.cloud.google.com/billing/docs/how-to/modify-project/
title: Enable, disable, or change billing for a project \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:16.022751+00:00
---

# Enable, disable, or change billing for a project  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/modify-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Enable, disable, or change billing for a project Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manage Cloud Billing for each of your Google Cloud projects and teaches you how to link and unlink projects and Cloud Billing accounts.

**Note:** Modifying links between projects and Cloud Billing accounts is considered a sensitive action; in some cases, you might need to reauthenticate before you can initiate the action. For more information, see [Sensitive actions](https://docs.cloud.google.com/docs/authentication/reauthentication#sensitive-actions). 

To learn how to [create](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account), [modify](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account), or [close](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account) your Cloud Billing account, visit [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).

A Google Cloud project is a top-level container for all your cloud resources, acting as the foundational element required to use any Google Cloud services. All service-level resources for Google Cloud, Google Maps Platform, Google AI Studio, and Firebase are parented by Google Cloud projects. A Cloud Billing account accrues and calculates costs for your usage of resources and services in each of the projects linked to the Cloud Billing account. The accrued costs are routed to a Google payments account to pay your bill.

![Illustrates how a Cloud Billing account is related to projects
     and to your Google payments profile and payments
     accounts. One side shows your Google Cloud resources
     \(a Cloud Billing account and its associated projects\) and the
     other side shows the Google payments center and how it's related to
     the Cloud Billing account \(with an associated Google payments
     profile and linked payments accounts\). Your projects' usage
     costs are tracked in your Cloud Billing account. The linked
     Google payments accounts manage payments-related information, including
     invoices and statements, and the payment instruments used to pay your
     bill.](https://docs.cloud.google.com/static/billing/docs/images/billing-project.png)

A Cloud Billing account defines who pays for a given set of resources, and it can be linked to one or more projects. Project usage costs are accrued by the linked Cloud Billing account and charged to the linked Google payments account.

If you create or have access to multiple Cloud Billing accounts, you can change the Cloud Billing account that a Google Cloud project is billed to. This document describes how to change the Cloud Billing account for your project, as well as how to enable and disable billing for a project.

In this document, you can learn how to:

  * Check if billing is enabled on a project
  * Change the Cloud Billing account linked to a project
  * Enable billing for a new project
  * Enable billing for an existing project
  * Disable billing for a project

**Caution:** For Google Cloud, Google Maps Platform, Firebase, and Google AI Studio services, if your projects are linked to a Cloud Billing account that is not in a billable state (such as an account suspension or billing account closure), you can't use the products and services enabled in your projects. This is true even if your projects only use Google Cloud or other eligible [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

If you want to receive invoices by email, or you want to change who receives them, see [Change payments contacts and notifications](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts).

## Required Permissions

The permissions required to accomplish the various tasks described in this document depend on the task and are noted at the start of each topic.

For more information about Cloud Billing permissions, see:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## Check if billing is enabled on a project

Billing is enabled on a project if the following are true:

  1. The project is linked to a Cloud Billing account.
  2. The linked Cloud Billing account is active and in good standing—that is, the billing account isn't closed or suspended.



See [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) to learn how to determine if billing is enabled on a project.

## Change the Cloud Billing account linked to a project

**Caution:** If you change your Cloud Billing account for a project to another customer's Cloud Billing account, or allow another customer to use your Cloud Billing account (even with each other's permission) to reduce or avoid fees, you could be in violation of your terms with Google Cloud.

Switching a project to a different Cloud Billing account shouldn't result in any service interruption or server downtime. However, your projects might be affected in the following ways:

  * **Committed use discounts (CUDs)** : If you purchased [resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for Compute Engine resources in your project, then moving the project has the following effects on your CUDs:

    * For any commitments in the project that you're moving, you receive CUDs only in the destination Cloud Billing account.

    * If the destination Cloud Billing account doesn't have CUD sharing enabled, then CUDs from resource-based commitments in the project that you're moving apply to eligible usage only in that project. You can [enable CUD sharing by updating the CUD scope for the destination Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).

    * If the destination Cloud Billing account already has CUD sharing enabled, then any resource-based CUDs from commitments in the project that you're moving apply to eligible usage across all projects in the destination Cloud Billing account.

    * Even if you enabled CUD sharing in the original Cloud Billing account, resource-based CUDs from the project that you're moving won't apply anymore to projects linked to that Cloud Billing account.

    * If you set up prioritized attribution for the commitment, you might need to update the prioritized attribution configuration after you change the project's Cloud Billing account.

[Learn about setting up prioritized attribution for your commitments](https://docs.cloud.google.com/docs/cuds-attribution#select-prioritized-attribution-resource-based).

    * After you change the Cloud Billing account for the project, any resource-based CUDs start applying to the new Cloud Billing account at midnight in the US and Canadian Pacific Standard Time (UTC-8) time zone.

    * Some usage costs are owned by the Cloud Billing account and aren't included in a project (for example, Support costs). To identify these charges before you switch your projects to a different Cloud Billing account, view the Cost table report or cost Reports:

      * Cost table report: [View the report using the default report settings](https://docs.cloud.google.com/billing/docs/how-to/cost-table#access-report) and then expand the hierarchical cost data in the _[Charges not specific to a project]_ row.
      * Cost Reports: [Access the Reports page](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) as a user with full Cloud Billing account permissions. Configure your report to [**group by SKU**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) and [**filter by Projects**](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-projects), selecting only the _[Charges not specific to a project]_ option.
  * **Google Cloud Marketplace customers** : If you've made purchases from Google Cloud Marketplace in your project, consider the following before you move a project to a different Cloud Billing account:

    * If you have Google Cloud Marketplace purchases attached to a project, then you can't migrate that project until you transfer your purchases. [Learn about the steps you must take to transfer your purchases](https://docs.cloud.google.com/marketplace/docs/offers/change-billing-account). Follow the transfer steps to prevent your project from being disabled or losing data as a result of missing required resources.
    * When switching Cloud Billing accounts, resources beyond those in Google Cloud Marketplace might also require your action to complete the migration.
    * To learn about how you're billed for Cloud Marketplace purchases, see [the Cloud Marketplace documentation](https://docs.cloud.google.com/marketplace/docs/manage-billing).
  * **Cloud Armor customers** : If your Cloud Billing account is subscribed to Cloud Armor Enterprise Annual, and you migrate your project from that billing account to another, but your new Cloud Billing account _isn't_ subscribed to Cloud Armor Enterprise Annual, your project reverts to Cloud Armor Standard after the migration completes. [Learn how to keep your project in Cloud Armor Enterprise Annual without downtime](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#migration).

  * **Google AI Studio customers** : If you change the Cloud Billing account that is linked to your project, you might be prompted to [configure a Prepay account](https://ai.google.dev/gemini-api/docs/billing#prepay) and buy credits before you can use Gemini API in AI Studio services.




### Permissions required for this task

To change the Cloud Billing account for a project, you need to be able to move a project from one Cloud Billing account to another. To accomplish this task, you need permissions to _unlink_ the project from the current Cloud Billing account AND to _link_ the project to the target Cloud Billing account.

You need both project permissions and billing account permissions. These predefined roles have adequate permissions to perform this task:

On the project  
---  
[ Project Billing Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) \+ [ Project Browser](https://docs.cloud.google.com/iam/docs/roles-permissions/browser#browser) \+ [ Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) | **_OR_** | [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)  
  
**_AND_**

On the current and target Cloud Billing accounts  
---  
[ Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) \+ [ Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer) | **_OR_** | [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)  
**Using an Organization?** If you're set up to use an [ Organization](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) to manage your Google Cloud resources and manage Organization billing accounts, then the Billing Account Administrator role granted at the _Organization level_ will have adequate permissions to perform this task.

Specifically, to perform this task, you must have the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing). 

**Action** | **Permission** | **Roles with permission** | **Resource**  
---|---|---|---  
**View projects** and Cloud Billing account associations | [ `billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Browser, Project Viewer, Project Editor, or Project Owner | Project  
**Unlink** project from its current Cloud Billing account | [ `billing.resourceAssociations.delete`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Administrator | Current billing account  
OR  
[ `resourcemanager.projects.deleteBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
**Link** project to the target Cloud Billing account | [ `billing.resourceAssociations.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account User or Billing Account Administrator | Target billing account  
AND  
[ `serviceusage.services.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)  
[ `serviceusage.effectivepolicy.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Service Usage Viewer, Project Viewer, Project Editor, or Project Owner | Project  
[ `resourcemanager.projects.createBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
  
### How to change the project's billing account

To change the project's Cloud Billing account, do the following.

  1. In the **Billing** section of the Google Cloud console, locate the project using one of the following methods:

Method 1: Start with your list of projects | Method 2: Start with a billing account  
---|---  
Access the **My Projects** page to view a list of _all of your projects_ and their _associated Cloud Billing account_. This method works best if you have the Project Owner, Project Editor, Project Viewer, or Project Billing Manager IAM role on the project you want to manage. To view a list of _all of your projects_ and their _associated Cloud Billing account_ , take the following steps:
     1. In the Google Cloud console, go to the **My Projects** page in the **Billing** section. [Go to My Projects in Cloud Billing](https://console.cloud.google.com/billing/projects)
     2. From the list of projects, locate the project you want to manage.
| Open the **Account management** page for a _selected billing account_ to view the list of all the _projects linked_ to the Cloud Billing account. This method works well when you have access to an _active_ Cloud Billing account that you know by name. To view the list of projects linked to a _specific billing account_ , take the following steps:
     1. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account. [Go to Account Management in Cloud Billing](https://console.cloud.google.com/billing/manage)
     2. At the prompt, choose the Cloud Billing account you want to view.
     3. On the **Account management** page, from the list of projects, locate the project that you want to manage.  
**Note** : If you see a padlock icon displayed lock next to a project, this indicates that the link between the project and its Cloud Billing account is locked. Before you can change the project's Cloud Billing account, you must first [ unlock the link](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link#unlock-link).
  2. In the project row, open the **Actions** menu (more_vert), select **Change billing** , then choose the destination Cloud Billing account. **Note:** If you can't select _Change billing_ , you don't have the permissions needed to make this change. See Permissions required for this task for more information.
  3. Click **Set account**.
  4. (Optional) After you link a project to a billing account, you can [lock the link](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link) to prevent the project from unintentionally being moved (linked) to a different billing account or the project link being deleted from the billing account.



### About project charges after the billing account is changed

After you change the Cloud Billing account on a project, charges already incurred _prior to moving the project_ are billed to the _former_ Cloud Billing account. This can include charges that haven't yet been reported in the [transaction history](https://docs.cloud.google.com/billing/docs/how-to/view-history). Depending on the service, it might take up to two days for charges to be reported to the transaction history. For example: If you move your project from Account A to Account B on May 15, charges incurred May 1 to May 15 will be billed to Account A (old), and charges incurred May 16 to May 31 will be billed to Account B (new).

## Enable billing for a project

How you enable billing depends on whether you're creating a new project or you're enabling billing for an existing project, and which platform you are on when you enable billing.

### Enable billing for a new project

Depending on which platform you are using when you create a new project, during the project creation process, you might be prompted to link a billing account to the project to enable billing. | Project-creation platform | Billing account linked? | Description  
---|---|---  
**Google Cloud console** | Yes | From the **Google Cloud console** , when you create a _new_ Google Cloud project for use with **Google Cloud** or **Google Maps Platform** products and services, you're prompted to choose which of your Cloud Billing accounts you want to link to the project. If you have only one Cloud Billing account, that account is automatically linked to your project. If you don't have a Cloud Billing account, you must create one and enable billing for your project before you can use many Google Cloud and Google Maps Platform services. To create a new Cloud Billing account and enable billing for your project, follow the instructions in [ Create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).  
**Firebase console** | No | From the **Firebase** console, when you create a _new_ [ project to use for Firebase](https://firebase.google.com/docs/projects/learn-more), you create a new Google Cloud project that isn't linked to a Cloud Billing account. By default, new projects that are created in the Firebase console are connected to the [ no-cost _Spark plan_](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans), which provides full usage of free services, plus limited usage and quota for paid Firebase services.  
**Google AI Studio console** | No | From the **Google AI Studio** console, when you [ create a _new_ project](https://ai.google.dev/gemini-api/docs/api-key#google-cloud-projects) for your Gemini API in AI Studio usage, you create a new Google Cloud project that isn't linked to a Cloud Billing account. By default, new projects begin on the [ Free tier](https://ai.google.dev/gemini-api/docs/billing#about-billings), which allows access to [ certain models](https://ai.google.dev/gemini-api/docs/pricing) in the Gemini API in AI Studio, up to the models' [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits).  
  
### Enable billing for an existing project

To use Google Cloud and Google Maps Platform resources and services in a project, billing must be enabled on the project.

For Firebase, billing must be enabled on the project to upgrade to the [pay-as-you-go Blaze plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans), to access more services and higher usage levels.

For Google AI Studio, billing must be enabled on the project to upgrade to a [paid tier](https://ai.google.dev/gemini-api/docs/billing), to access higher rate limits and use advanced Gemini API models.

Billing is enabled when the project is linked to an _active_ Cloud Billing account in good standing. Billing can become disabled on a project for one of the following reasons:

  * The project is unlinked from its billing account, disabling billing on the project.
  * The [Cloud Billing account that is linked to the project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) is closed or suspended.
  * The project was [shut down (deleted)](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) and then [restored within the 30-day recovery period](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project).



If you have a project where billing has been disabled, for Google Cloud and Google Maps Platform, all billable services within that project are stopped; for Firebase and Google AI Studio, your usage is downgraded to the limited free use plans. Re-enable billing on the project to restart the resources or continue to access the elevated features of a paid plan.

  * After billing is re-enabled, it might take up to 24 hours for the resources to start up again.
  * Some services might need to be restarted manually. For more information, see [Restarting Google Cloud Services](https://docs.cloud.google.com/billing/docs/how-to/restart-services).
  * While billing is disabled on a project, some resources might be deleted and might not be fully recoverable. [Learn about data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion#deletion_timeline).



### Permissions required for this task

To enable billing for a project, you need permissions to _link_ the project to the target Cloud Billing account.

You need both project permissions and billing account permissions. These predefined roles have adequate permissions to perform this task:

On the project  
---  
[ Project Billing Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) \+ [ Project Browser](https://docs.cloud.google.com/iam/docs/roles-permissions/browser#browser) \+ [ Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) | **_OR_** | [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)  
  
**_AND_**

On the target Cloud Billing account  
---  
[ Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) \+ [ Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer) | **_OR_** | [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)  
**Using an Organization?** If you're set up to use an [ Organization](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) to manage your Google Cloud resources and manage Organization billing accounts, then the Billing Account Administrator role granted at the _Organization level_ will have adequate permissions to perform this task.

Specifically, to perform this task, you must have the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing). 

**Action** | **Permission** | **Roles with permission** | **Resource**  
---|---|---|---  
**View projects** and Cloud Billing account associations | [ `billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Browser, Project Viewer, Project Editor, or Project Owner | Project  
**Link** project to the target Cloud Billing account | [ `billing.resourceAssociations.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account User or Billing Account Administrator | Target billing account  
AND  
[ `serviceusage.services.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)  
[ `serviceusage.effectivepolicy.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Service Usage Viewer, Project Viewer, Project Editor, or Project Owner | Project  
[ `resourcemanager.projects.createBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
  
### How to enable billing on an existing project

You can follow the procedure described here to access the Google Cloud console to enable billing on any of your Google Cloud projects.

Alternatively, for your Firebase and AI Studio projects, you can access those platforms directly to enable billing on your projects:

  * Firebase: [Enable billing to upgrade your project to the Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered)
  * Google AI Studio: [Learn how to set up billing for your projects and API keys](https://ai.google.dev/gemini-api/docs/billing#setup-billing)



In the Google Cloud console, to enable billing on a project, do the following:

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. Select the **My projects** tab to view a list of projects and the associated Cloud Billing account for each project.

  3. From the list of projects, locate the project for which you want to re-enable billing. Tip: In the **Billing account** column, for projects that aren't linked to a billing account, look for "Billing is disabled".

  4. In the project row, open the **Actions** menu (more_vert), select **Change billing** , then choose the destination Cloud Billing account.

**Note:** If you can't select _Change billing_ , you don't have the permissions needed to make this change. See Permissions required for this task for more information.
  5. Click **Set account**.

  6. (Optional) After you link a project to a billing account, you can [lock the link](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link) to prevent the project from unintentionally being moved (linked) to a different billing account or the project link being deleted from the billing account.




#### Error when attempting to re-enable billing

If you're re-enabling billing on a recently [restored project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project), you might encounter an error similar to: `User missing permission 'resourcemanager.projects.createBillingAssignment' to link a billing account to project. The attempted action failed, please try again.`

Due to latency issues during the project recovery process, it might take some time for the _restored_ project to propagate to the Cloud Billing system. You can't successfully link a Cloud Billing account to a restored project until the project is fully propagated to the billing system.

If you receive an error message when attempting to link a billing account to a newly restored project, retry after about 10 minutes. If it still doesn't work, wait a few hours to assign billing. In rare instances, it might take up to 36 hours before you can re-enable billing on a restored project.

## Disable billing for a project

To stop automatic payments for a project, you can disable billing for the project by unlinking the project from the billing account. You're still responsible for all outstanding charges for the project. Your listed form of payment on your Cloud Billing account is used to pay for any outstanding charges.

### What's the impact of disabling billing on a project?

Your projects and services are impacted in different ways when you disable billing, based on the services in use in your projects.

#### Google Cloud and Google Maps Platform services:

  * **Limitation** : You can't disable billing on a project if you have any active or pending committed-use discounts (CUDs) in that project.
  * When you disable billing for a project, all of your Google Cloud and Google Maps Platform services are stopped and billing on that project stops.
  * When billing is disabled for a project, some of your Google Cloud resources might be removed and become non-recoverable. We recommend backing up any data that you have in the project.
  * If you disable billing for a project that hosts a Shared VPC, services in the service project which depend on the Shared VPC are also disabled. For example, if you have three service projects linked to the Shared VPC, all Compute Engine instances that use the Shared VPC as the network interface are shut down, which affects all three service projects.



#### Firebase services:

  * When you disable billing on a Firebase project, the project is downgraded from the [_Blaze plan_](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#blaze-pricing-plan) to the [no-cost _Spark plan_](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans), which provides full usage of free services, plus limited usage and quota for paid Firebase services.
  * When you downgrade, you might find that you've exceeded your no-cost quota limits for a product, causing the project's usage of that specific product to be shut off for the remainder of the month. [Learn more about the Spark plan limitations](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#important-facts-spark).



#### Gemini API in AI Studio services:

  * When you disable billing on an AI Studio project, the project's billing tier is downgraded to the [_Free_ usage tier](https://ai.google.dev/gemini-api/docs/billing), which allows limited free access to certain Gemini API models.
  * [Learn more about Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing).



### Permissions required for this task

To disable billing for a project, you need permissions to _unlink_ the project from the Cloud Billing account.

You need both project permissions and billing account permissions. These predefined roles have adequate permissions to perform this task:

On the project  
---  
[ Project Billing Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) \+ [ Project Browser](https://docs.cloud.google.com/iam/docs/roles-permissions/browser#browser) | **_OR_** | [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)  
  
**_AND_**

On the target Cloud Billing account  
---  
[ Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer) | **_OR_** | [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)  
**Using an Organization?** If you're set up to use an [ Organization](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) to manage your Google Cloud resources and manage Organization billing accounts, then the Billing Account Administrator role granted at the _Organization level_ will have adequate permissions to perform this task.

Specifically, to perform this task, you must have the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing). 

**Action** | **Permission** | **Roles with permission** | **Resource**  
---|---|---|---  
View projects and Cloud Billing account associations | [ `billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Browser, Project Viewer, Project Editor, or Project Owner | Project  
**Unlink** project from a Cloud Billing account | [ `billing.resourceAssociations.delete`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Administrator | Billing account  
OR  
[ `resourcemanager.projects.deleteBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
  
### How to disable billing for a project

To disable billing for a project, do the following:

  1. In the **Billing** section of the Google Cloud console, locate the project using one of the following methods: 

Method 1: Start with your list of projects | Method 2: Start with a billing account  
---|---  
Access the **My Projects** page to view a list of _all of your projects_ and their _associated Cloud Billing account_. This method works best if you have the Project Owner, Project Editor, Project Viewer, or Project Billing Manager IAM role on the project you want to manage. To view a list of _all of your projects_ and their _associated Cloud Billing account_ , take the following steps:
     1. In the Google Cloud console, go to the **My Projects** page in the **Billing** section. [Go to My Projects in Cloud Billing](https://console.cloud.google.com/billing/projects)
     2. From the list of projects, locate the project you want to manage.
| Open the **Account management** page for a _selected Cloud Billing account_ to view the list of all the _projects linked_ to the billing account. This method works well when you have access to an _active_ Cloud Billing account that you know by name. To view the list of projects linked to a _specific billing account_ , take the following steps:
     1. In the Google Cloud console, go to the **Account management** page for the **Cloud Billing account**. [Go to Account Management in Cloud Billing](https://console.cloud.google.com/billing/manage)
     2. At the prompt, choose the Cloud Billing account you want to view.
     3. On the **Account management** page, from the list of projects, locate the project that you want to manage.  
**Tip** : If you see a padlock icon displayed lock next to a project, this indicates that the link between the project and its Cloud Billing account is locked. Before you can disable billing on the project, you must first [ unlock the link](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link#unlock-link).  
  2. In the project row, open the **Actions** menu (more_vert), and then select **Disable billing**. You're prompted to confirm that you want to disable billing for this project.

**Note:** If you can't select _Disable billing_ , you don't have the permissions needed to make this change. See Permissions required for this task for more information.
  3. Click **Disable billing**.

**Caution:** If you disable billing for a project where your [permissions on the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) are limited, you might not have the required permissions needed to later re-enable billing. For more information, see Enable billing for an existing project.



### About project charges after billing is disabled

After you disable billing on a project, usage charges that accrue _prior to disabling billing on the project_ are billed to the _previously linked_ Cloud Billing account. This can include charges that haven't yet been reported in the [transaction history](https://docs.cloud.google.com/billing/docs/how-to/view-history). Google Cloud and other eligible products such as Google Maps Platform, Google AI Studio, and Firebase report usage data to Cloud Billing at varying intervals. Due to the complexity of our billing and processing systems, it might take up to two days for usage charges in the project to be reported to the transaction history and billed to the _previously linked_ Cloud Billing account.

## Related topics

  * [View linked projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Create, modify, or close your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * [Change payments contacts and notifications](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
