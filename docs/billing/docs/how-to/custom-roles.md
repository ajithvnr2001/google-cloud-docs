---
url: https://docs.cloud.google.com/billing/docs/how-to/custom-roles/
title: Create custom roles for Cloud Billing accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:17.060694+00:00
---

# Create custom roles for Cloud Billing accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/custom-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Create custom roles for Cloud Billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) includes fine-grained permissions, which lets you grant or revoke access to specific actions for individual users. To simplify the process of assigning permissions to users, IAM roles combine these fine-grained permissions into related groups. Billing has [predefined roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access), such as Billing Account Administrator or Billing Account Viewer, which work for most users. But, if they don't fit your needs, custom roles let you to grant more specific sets of permissions.

## Create a custom role

Custom roles are created on the organization, and then are applied to any billing account in the organization. [Creating and Managing Custom Roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) in the IAM documentation describes how to configure a custom role, including which permissions are necessary.

**Caution:** When you create a custom role, you're prompted to specify _Project_ or _Organization_. You must select _Organization_. Project roles can't be applied to billing accounts.

After custom roles are created, you can grant custom roles to users just like standard, predefined roles. [Learn how to update billing permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access#update_billing_permissions).

## Example custom role

Imagine you want to give someone the ability to edit cost management features, such as budget alerts and billing export. In addition to the basic permissions required to access and view the billing account, the relevant permissions for budgets and export are:

  * `billing.budgets.create`
  * `billing.budgets.update`
  * `billing.accounts.updateUsageExportSpec`



With the predefined roles, to apply these permissions you need to grant the Billing Account Administrator role. But that role also includes permission to delete resource associations, cancel subscriptions, and close the billing account. If you didn't want your users to have those capabilities, you could instead [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with only the three necessary permissions and name it _Cost Management Administrator_. Then, you could apply that custom role in combination with the Billing Account Viewer role to any users that should have broad cost management permissions but no ability to edit other account properties.

## Permission association and inheritance

You can grant billing permissions at the billing account level or at the project level. Most billing permissions belong on the billing account, so roles containing those permissions should be associated with the billing account. Other billing permissions instead belong on a project and need to be associated with the project instead of the billing account.

For example, associating a project with a billing account requires the `billing.resourceAssociations.create` permission on the billing account and also the `resourcemanager.projects.createBillingAssignment` permission on the project. This is because project permissions are required for actions where project owners control access, while billing account permissions are required for actions where billing account administrators control access. When both are involved, both permissions are necessary.

Just like other IAM permissions, all billing permissions inherit from higher levels of the billing hierarchy. For example, a user with a role containing `billing.accounts.close` on an organization can close any billing account within that organization. However, some permissions only apply at higher levels. For example, the `billing.accounts.list` permission doesn't do anything when applied to an individual billing account, but a user with a role containing `billing.accounts.list` on an organization can list all billing accounts within that organization.

## Billing activities

The following tables describe common billing activities, the permissions required to perform those activities, and the resource that those permissions apply to.

### Account management

**Action** | **Permission** | **Resource**  
---|---|---  
Get basic account information (for example, account name, currency, or if the account is open or closed) | `billing.accounts.get` | Billing account  
Upgrade from free trial | `billing.accounts.update` | Billing account  
Rename account | `billing.accounts.update` | Billing account  
Change purchase order number | `billing.accounts.update` | Billing account  
Close account | `billing.accounts.close` | Billing account  
Reopen closed account | `billing.accounts.reopen` | Billing account  
**Key Point:** Most billing actions require `billing.accounts.get`. You might consider giving a role with this permission to all users who need billing account access.

### Billing account hierarchy

**Action** | **Permission** | **Resource**  
---|---|---  
List accounts in organization | `billing.accounts.list` | Organization  
Create accounts in organization | `billing.accounts.create` | Organization  
Move account into organization | `billing.accounts.create` | Organization  
`billing.accounts.move` | Billing account  
Move account between organizations | `billing.accounts.removeFromOrganization` | Old organization  
`billing.accounts.create` | New organization  
`billing.accounts.move` | Billing account  
  
### Cost information

Cost view permissions can be limited to specific projects, or granted on a billing account to view all costs for a billing account.

**Action** | **Permission** | **Resource**  
---|---|---  
View costs and usage for a billing account* | `billing.accounts.getSpendingInformation` | Billing account  
View costs and usage for a project* | `billing.resourceCosts.get` | Project  
`resourcemanager.projects.get` | Project  
*** Note:** A user with `billing.accounts.getSpendingInformation` permission on the billing account can view costs for the entire billing account including _all_ of its projects. If you want to limit a user to viewing the costs only for specific projects, give the user the `billing.resourceCosts.get` and `resourcemanager.projects.get` permissions on each project instead of setting the billing account level permission. 

### Payment information

The payment profile includes customer name, address, and payment method.

**Action** | **Permission** | **Resource**  
---|---|---  
View payment profile | `billing.accounts.getPaymentInfo` | Billing account  
Update payment profile | `billing.accounts.updatePaymentInfo` | Billing account  
View prices only for the SKUs that have incurred usage | `billing.accounts.getPricing` | Billing account  
View custom contract prices per SKU for a billing account | `billing.accounts.getPricing` | Billing account  
View costs and usage for a billing account | `billing.accounts.getSpendingInformation` | Billing account  
  
### Resource associations

Moving a project between billing accounts requires the same permissions as removing it from the original billing account and associating it with the new one.

**Action** | **Permission** | **Resource**  
---|---|---  
View project associations | `billing.resourceAssociations.list` | Billing account  
`resourcemanager.projects.get` | Project  
Associate project with billing account | `billing.resourceAssociations.create` | Billing account  
`serviceusage.services.list` | Project  
`serviceusage.effectivepolicy.get` | Project  
`resourcemanager.projects.createBillingAssignment` | Project  
Remove project from billing account | `billing.resourceAssociations.delete` | Billing account  
`resourcemanager.projects.deleteBillingAssignment` | Project  
  
### Budgets and spending alerts

**Action** | **Permission** | **Resource**  
---|---|---  
View the list of budgets for a Cloud Billing account  | `billing.budgets.get` | Billing account  
`billing.budgets.list` | Billing account  
Update a budget that's scoped to a Cloud Billing account | `billing.budgets.update` | Billing account  
Create a budget for a Cloud Billing account | `billing.budgets.create` | Billing account  
Delete a budget for a Cloud Billing account | `billing.budgets.delete` | Billing account  
Configure, edit, and lift a spend cap budget on a project in a Cloud Billing account | `billing.budgets.configureSpendCap` | Billing account  
View the list of budgets that are scoped to a single project | `resourcemanager.projects.get` | Project  
`billing.resourceCosts.get` | Project  
`billing.resourcebudgets.read` | Project  
Update a budget that's scoped to a single project | `resourcemanager.projects.get` | Project  
`billing.resourceCosts.get` | Project  
`billing.resourcebudgets.read` | Project  
`billing.resourcebudgets.write` | Project  
Create a budget that's scoped to a single project | `resourcemanager.projects.get` | Project  
`billing.resourceCosts.get` | Project  
`billing.resourcebudgets.read` | Project  
`billing.resourcebudgets.write` | Project  
Configure, edit, and lift a spend cap budget that's scoped to a single project | `resourcemanager.projects.get` | Project  
`billing.resourceCosts.get` | Project  
`billing.resourcebudgets.read` | Project  
`billing.resourcebudgets.write` | Project  
`billing.resourcebudgets.configureSpendCap` | Project  
**Key Point:** A user with billing-account-level permissions on the billing account can manage budgets for the entire billing account, including _any_ of its projects. If you want to limit a user to managing budgets that are scoped only to a single project, give the user project-level permissions on the project instead of setting billing-account-level permissions. For more information, see [ Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

### Credits and promotions

**Action** | **Permission** | **Resource**  
---|---|---  
View credits list, including original and remaining amount | `billing.credits.list` | Billing account  
Redeem a promotional code | `billing.accounts.redeemPromotion` | Billing account  
`billing.accounts.update` | Billing account  
  
### Policy

The policy defines which users have access to which resources on a billing account. For information on creating or modifying custom roles, see the Create a Custom Role section.

**Action** | **Permission** | **Resource**  
---|---|---  
View roles on account, including associated usernames | `billing.accounts.getIamPolicy` | Billing account  
Give roles to users on account | `billing.accounts.setIamPolicy` | Billing account  
  
### Export specifications

The export specification defines where to send a copy of all usage-related data, and can contain the name of a [BigQuery dataset](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

**Action** | **Permission** | **Resource**  
---|---|---  
View current export specification (Cloud Storage bucket or BigQuery dataset to export usage data to) | `billing.accounts.getUsageExportSpec` | Billing account  
Modify export specification | `billing.accounts.updateUsageExportSpec` | Billing account  
  
## Related topics

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Cloud Billing API access control](https://docs.cloud.google.com/billing/v1/how-tos/access-control)
  * [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
