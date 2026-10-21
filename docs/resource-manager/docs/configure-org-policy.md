---
url: https://docs.cloud.google.com/resource-manager/docs/configure-org-policy/
title: Configure organization policies \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:24:10.461377+00:00
---

# Configure organization policies  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/configure-org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)



Send feedback 

#  Configure organization policies Stay organized with collections  Save and categorize content based on your preferences. 

To migrate a project to a new organization resource, you must first apply an organization policy that will define the organization resources to which the project can migrate. You must also set an organization policy in the destination that defines the organization resources from which projects can be imported.

To configure organization policies required for the migration, you must have the `roles/orgPolicy.policyAdmin` role on the parent and the destination organization. For detailed instructions, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

**Caution:** If you do not set the following organization policies, the migration will result in a `FAILED_PRECONDITION` error. You must do the following:

  * On the parent resource of the project you want to migrate between organization resources, set an organization policy that includes the `constraints/resourcemanager.allowedExportDestinations` constraint. This will define the target destination as a valid location to which you can migrate the project.

  * On the destination resource, set an organization policy that includes the `constraints/resourcemanager.allowedImportSources` constraint. This will define the source as a valid location from which you can migrate your project.




For example, say you had a project `my-test-project` that existed under an organization resource with the ID `12345678901`, and you wanted to migrate it to a new organization resource for your secondary business unit, with the ID `45678901234`.

You would set an organization policy on `organizations/12345678901` with the `constraints/resourcemanager.allowedExportDestinations` constraint enforced and `under:organizations/45678901234` set as an **allowed_value**.

Then, set an organization policy on `organizations/45678901234` with the `constraints/resourcemanager.allowedImportSources` constraint enforced and `under:organizations/12345678901` set as an **allowed_value**.

Once these organization policies are enforced, you will be able to migrate `my-test-project` from `organizations/12345678901` to `organizations/45678901234`, assuming you have the permissions noted in [Assign permissions](https://docs.cloud.google.com/resource-manager/docs/assign-iam-roles).

**Note:** Whether you are using [dedicated import and export folders](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan#import_export_folders) or not, it is good practice to remove these organization policies after you are done moving projects across organization resources. You can enforce them again if you need to perform another project migration.

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

  1. You must get the `roles/billing.admin` role on the source and destination organization resources, and the `roles/billing.creator` role on the destination organization resource.

  2. Go to the **Billing page** in the Google Cloud console.  
[Go to the Billing page](https://console.cloud.google.com/billing)

  3. Click on the name of the billing account you want to migrate.

  4. At the top of the **Account Management** page, click **Change organization**.

  5. Select the destination organization resource, and then click **Ok**.




The billing account is now associated with the specified organization resource.

## What's next

To learn about how to handle special cases during project migration, see [Handling special cases](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
