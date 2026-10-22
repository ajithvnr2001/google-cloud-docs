---
url: https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps/
title: Manage spend cap budgets \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:09.625235+00:00
---

# Manage spend cap budgets  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Manage spend cap budgets Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create, edit, and delete spend cap budgets on projects linked to a Cloud Billing account.

In this document, you can learn about the following:

  * About spend cap budgets

To learn about _alerts-only_ budgets, see [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

  * How spend cap budgets work to help you control spend

  * Services that are eligible for spend cap budgets

  * Limitations of spend cap budgets

  * Configure a spend cap budget

  * View spend cap budgets

  * Manually lift an enforced spend cap

  * Edit a spend cap budget

  * Delete a spend cap budget

  * Create and manage spend cap budgets using an API




## About spend cap budgets

Spend Caps in Cloud Billing Budgets help reduce unexpected or runaway costs for eligible services. To help you stay informed about how your spend is tracking against your budget, alert emails are sent when your spend exceeds 50%, 80%, and 100% of your spend cap budget amount.

The spend cap is enforced when your _gross, estimated_ usage costs exceed 100% of your budget amount. When a spend cap budget is enforced, usage of your specified services is automatically paused for the remainder of the _budget period_ unless you _manually_ lift the spend cap. At the start of the next budget period, enforced spend cap budgets are lifted automatically, resuming any paused services and resetting the spend amount to zero.

Enforcement also triggers alerts, including email notifications and banners in the billing console UI, with information and guidance about how to manually lift the cap.

## How spend cap budgets work to help you control spend

Spend cap budgets use _gross, estimated_ costs to trigger alerts and enforce spend limits, blocking usage and cost accrual until the spend cap is lifted.

### Faster spend calculations using estimated costs

For faster enforcement of a spend cap amount, spend cap budgets use _gross, estimated_ costs to trigger alerts and enforce the spend cap. The estimated costs are calculated based on the list price of services and don't include savings and credits.

When viewing a spend cap budget, the _estimated_ costs are displayed on the budget's _Spend and budget amount_ progress bar, and in the _Spend amount_ field that is viewable when you are editing a spend cap budget.

### Automatic pause of usage and cost accrual when the spend cap is triggered

In the specified project, when your _gross, estimated_ usage costs for the specific service exceed your budget target amount, the spend cap is triggered and enforced for the remainder of the budget period. While enforced, all _new_ usage for the specific service in the specified project is paused, including on-demand, pay-as-you-go usage and usage covered by commitments such as [Committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) and [Provisioned Throughput (PT)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput). Any _in-flight_ requests of the specified service are processed to completion, accruing charges as applicable.

Spend caps don't pause any on-going, fixed usage associated with _persistent_ resources (such as compute and storage services), which remain active and continue to accrue charges.

### Lift an enforced spend cap to restore services and spending

When a spend cap is enforced, usage of the specific service in the specified project is blocked until the spend cap is lifted. You can lift a spend cap in the following ways:

  * **Automatically lift a spend cap** : An enforced spend cap is automatically lifted at the start of the next budget period (typically the first day of the next month). When a spend cap is automatically lifted, the spend amount of the budget resets to zero, the spend cap status resets to _Configured_ , and the specified services are unblocked, restoring normal function to the API calls.
  * **Manually lift a spend cap** : If you need to reverse a usage block during the same budget period when the spend cap is enforced, you can edit the budget to _manually lift_ the spend cap. Manually lifting a spend cap has the following results:

    * Manually lifting a spend cap restores normal function to the API calls and changes the spend cap status to _Lifted_ for the remainder of the budget period.
    * After manually lifting the cap, a spend cap won't trigger again for the rest of the budget period, unless you edit the budget to increase the spend cap amount.
    * At the start of the next budget period (typically the first day of the next month), the spend cap budget automatically resets, setting the spend amount to zero and the spend cap status to _Configured_.



After a spend cap is lifted, services might take up to one hour to fully return to normal function.

### Alerts sent when the spend cap is triggered

When a spend cap is triggered, an email alert is sent to all billing account administrators and project owners with details about how to lift the cap. You'll also see banners in the billing console UI, on the Budgets page and the Billing Overview page.

### Automatic reset of spend cap budgets

At the start of the next budget period (typically the first day of the next month), all spend cap budgets automatically reset, setting the _gross, estimated_ spend amount to zero and the spend cap status to _Configured_.

If a spend cap was enforced in the previous budget period, the specified service is unblocked, and normal function is restored to the service.

## Services that are eligible for spend cap budgets

Spend caps are available for the following API-based services:

Service | Service ID | API service name  
---|---|---  
[Gemini API](https://ai.google.dev/gemini-api/docs) | AEFD-7695-64FA | generativelanguage.googleapis.com  
[ Gemini Enterprise Agent Platform (formerly Vertex AI)](https://cloud.google.com/products/gemini-enterprise-agent-platform) | C7E2-9256-1C43 | aiplatform.googleapis.com  
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | 152E-C115-5142 | run.googleapis.com  
[Cloud Run functions](https://docs.cloud.google.com/run/docs/functions-with-run) | 29E7-DA93-CA13 | cloudfunctions.googleapis.com  
  
## Limitations of spend cap budgets

Spend cap budgets are subject to the following limitations:

  * Spend caps are limited to budgets that are scoped to a _single_ Google Cloud project and a _single_ eligible service within the specified project.
  * The time range budget period for a spend cap budget is limited to _Monthly_ , starting on the first day of each month (such as May 1).
  * The cost calculations for spend caps are based on _gross, estimated_ costs and don't include savings and credits.
  * Folders, Organizations, Labels, and multi-project or multi-service budgets are out of scope.
  * Spend cap budgets are limited to first-party Google Cloud customers. Reseller accounts are out of scope.
  * Spend caps apply to on-demand, pay-as-you-go usage and usage covered by commitments such as [Committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) and [Provisioned Throughput (PT)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput). Subscription-based costs (such as for [Gemini Enterprise subscriptions](https://docs.cloud.google.com/gemini/enterprise/docs/licenses)) are out of scope.
  * Faster enforcement, delayed reporting: Since spend caps are enforced using _gross, estimated_ costs, alerts and caps are triggered much faster than the _actual_ costs that appear on billing reports. Due to the complexity of our billing and processing systems, your _actual_ cost details are typically available within a day, but can sometimes take more than 24 hours to process and appear on billing reports.

**Note:** Even though faster than reports, the enforcement of spend caps isn't instant and any cost overages are billed as normal.



## Permissions required to manage spend cap budgets

To configure, edit, and lift spend cap budgets, you need specific permissions that allow you to access a Cloud Billing account, to view and create budgets, and to configure spend cap budgets. The required permissions vary depending on whether you manage budgets and spend caps at the billing account level (using full billing account permissions) or at the project level (using project-scoped billing permissions).

If you are using custom roles to grant permissions to manage budgets, update your custom roles to include these permissions for managing _spend cap_ budgets:

  * **Billing Account level** : `billing.budgets.configureSpendCap` on the Cloud Billing account.

  * **Project level** : `billing.resourcebudgets.configureSpendCap` on the project.




###  Full billing account permissions

Cloud Billing account permissions are granted using roles on the billing account. To manage alerts-only budgets and _spend cap_ budgets for your Cloud Billing account, you need a role on your _Cloud Billing account_ that includes all of the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.get`
  * `billing.accounts.getIamPolicy`
  * [ `billing.accounts.getSpendingInformation`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#cost_information) to view costs and usage for a billing account
  * [ `billing.budgets.get` and `billing.budgets.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) to view all budgets for the Cloud Billing account.
  * [ `billing.budgets.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) to create a new budget.
  * [ `billing.budgets.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) to modify an existing budget.
  * [ `billing.budgets.delete`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) to delete a budget.
  * [ `billing.budgets.configureSpendCap`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) to configure, edit, and lift _spend cap_ budgets.



To gain these permissions using a predefined role, ask your administrator to grant the following [ Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) role on your Cloud Billing account: 

  * [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)



You can also use a combination of billing account and project roles to gain the required permissions to manage spend cap budgets:

  * [ Billing Account Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.costsManager) on the Cloud Billing account.   
and
  * [ Editor role](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) on each project where you want to configure spend cap budgets.



###  Project-scoped billing permissions

By using billing-specific permissions on a project, you can manage budgets for the projects that you own, one project at a time.

For more information about project-limited permissions for managing budgets and alerts in Cloud Billing accounts, see [ project-scoped access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#project-permissions).

Access a billing account for _multiple_ Google Cloud projects  | Access billing for an _individual_ Google Cloud project  
---|---  
You can manage budgets for your authorized Google Cloud projects, one project at a time. When you have multi-project-scoped access to a Cloud Billing account through a _combination_ of project and billing account permissions, on the Budgets page, you can use a project selector to switch between your billing-authorized projects.

  * **Projects** : You need billing-specific permissions on _each Google Cloud project_. Project permissions are granted with roles on the _Google Cloud project or folder_. To manage spend cap budgets, at a minimum, you need the following [ permissions](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on each project:
    * `resourcemanager.projects.get`
    * `billing.resourceCosts.get` (optional)*
    * `billing.resourcebudgets.read`
    * `billing.resourcebudgets.write`
    * `billing.resourcebudgets.configureSpendCap`
  * **Cloud Billing account** : You need project-scoped billing permissions on the _Cloud Billing account_ that is [ linked to your authorized projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). You grant billing account permissions using IAM roles on the _Cloud Billing account_. For multi-project-scoped access to the billing account ([Preview](https://cloud.google.com/products/#product-launch-stages)), you need the following role on the _Cloud Billing account_ :
    * [ Project Billing Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectCostsManager)

Learn more about the [ permissions required for _multi-project-scoped access_ to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#required-permissions). |  To access Cloud Billing to manage budgets for an _individual_ Google Cloud project, one project at a time, you only need _billing-specific_ permissions on the _Google Cloud project_.

  * **Projects** : You need billing-specific cost view permissions on _each Google Cloud project_ for which you want to manage budgets and alerts. Project permissions are granted with roles on the _Google Cloud project or folder_. To manage spend cap budgets, at a minimum, you need the following [ permissions](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on each project:
    * `resourcemanager.projects.get`
    * `billing.resourceCosts.get` (optional)*
    * `billing.resourcebudgets.read`
    * `billing.resourcebudgets.write`
    * `billing.resourcebudgets.configureSpendCap`
  * **Cloud Billing account permissions aren't required** : If you are viewing billing information for one project at a time, you don't need permissions on the Cloud Billing account that is [ linked to your authorized Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/view-linked). 

Learn more about the [ _project_ permissions required for _single-project-scoped access_ to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#project-permissions).  
*** Optional project permission:** A user with the `billing.resourceCosts.get` permission on the project can view the costs for the project, including [reports](https://docs.cloud.google.com/billing/docs/how-to/reports) and the [cost trend chart](https://docs.cloud.google.com/billing/docs/how-to/budgets#cost-trend-chart) that displays on the budget **create** or **edit** pages. You can omit this permission if you want to limit a user to managing budgets for the specific project without allowing them to view the costs for the project.   
  
## Configure a spend cap budget

Complete the following steps to create a spend cap budget:

  1. In the Google Cloud console, navigate to the **Budgets & alerts** page using the [procedure that fits your level of access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/budgets#add-new-budget).

  2. On the **Budgets & alerts** page, click **Create new budget**.

**Note:** You can't edit an existing _alerts-only_ budget to convert it to a spend cap enforcement budget. To set a spend cap budget with a similar scope, delete the _alerts-only_ budget and then create a new _spend cap_ budget.

![Step 1: Define - select spend cap enforcement and name the budget.](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-define-sm.png)**1** : Select spend cap enforcement and name the budget. 

![](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-define.png)

### **Define** section

  1. Select the **Spend cap enforcement** option (instead of _Alerts only_).
  2. Enter a **Name** for your budget, then click **Next**.



![Step 2: Scope - select project and service for the spend cap budget.](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-scope-sm.png)**2** : Select the project and service for the budget. 

![](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-scope.png)

### **Scope** section

  1. For spend cap budgets, the **Time range** selector is automatically set to _Monthly_. You can't edit this setting.
  2. Select a _single_ **Project** and a _single_ eligible **Service** for the spend cap.
  3. For spend cap budgets, you can't edit the **Savings** settings.

     * For certain services, we can estimate directional costs faster than we can calculate the actual costs. For those services, the spend amount we use to enforce a spend cap budget is based on gross, estimated costs, excluding savings.
     * For the remaining services, we calculate the spend amount using actual costs, inclusive of all savings.
  4. Click **Next**.




![Step 3: Amount - set spend cap amount.](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-amount-sm.png)**3** : Set the amount of the spend cap. 

![](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-amount.png)

### **Amount** section

  1. For spend cap budgets, the **Budget type** selector is automatically set to _Specified amount_. You can't edit this setting.
  2. Enter the **Target amount** of the spend cap.

     * When this spending threshold is reached, usage for the selected service is paused.
     * Due to latency in usage and cost reporting, spend cap enforcement isn't instantaneous. Consider setting your budget slightly below your absolute limit. You remain responsible for any overage costs accrued due to reporting latency.
  3. Click **Next**.




![Step 4: Actions are automatically configured. Select Finish to save
      the spend cap budget.](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-actions-sm.png)**4** : Select Finish to save the spend cap budget. 

![](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-actions.png)

### **Actions** section

  1. **Spend cap notifications** are automatically configured to notify all billing administrators and project owners at 50%, 80%, and 100% of the budget amount.
  2. For spend cap budgets, the alerts and recipients can't be customized.
  3. Click **Finish** to save and enable your spend cap budget.



## View a list of budgets

After budgets are created, you can [view the Budgets dashboard](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets) to see a list of budgets for a Cloud Billing account. Each budget in the list includes an overview of the budget settings and a **Spend and budget amount** progress bar—a visual gauge of how your Google Cloud spend is tracking against the target amount of the budget. For spend cap budgets, the progress bar shows your _gross, estimated_ costs, which might differ from your actual costs.

To help you understand the status of your budgets, refer to the **Spend cap status** column in the Budgets dashboard. Possible values include:

  * **Not applicable** – For _Alerts-only_ budgets that don't trigger a spend cap.
  * **Configured** – For Spend cap budgets that are active during the budget time period, but not yet enforced.
  * **Enforced** – For Spend cap budgets that are triggered during the budget time period when the _gross, estimated_ usage costs exceed the budget's _Target amount_. When enforced, the specified services are paused during the remainder of the budget time period unless you manually lift the cap.
  * **Lifted** – For Spend cap budgets that were enforced during the budget time period and then manually lifted to continue using the services that were paused.

    * For a budget in a _Lifted_ state, the spend cap won't trigger again for the rest of the budget period, unless you edit the budget to increase the target amount of the spend cap.
    * After lifting the spend cap, the affected services might take up to one hour to fully return to normal function.
    * After a spend cap is manually lifted, at the start of the next budget period, the spend cap budget automatically resets, setting the spend amount to zero and the spend cap status to _Configured_.



## Manually lift an enforced spend cap

When a spend cap budget is triggered, _new_ usage for the specific service is blocked until the spend cap is lifted. You'll receive email notifications and see banners in the billing console, as described in the How spend cap budgets work section. Lifting the cap restores normal function to the API calls.

During the budget period when a spend cap is enforced, you can unblock usage by manually lifting an enforced spend cap. If you take no action, an enforced spend cap is automatically lifted at the start of the next budget period.

To manually lift a spend cap, **edit the budget** where the spend cap is enforced.

![Edit a budget to lift an enforced spend cap.](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-lift-spend-cap.png)Lift an enforced spend cap. 

![](https://docs.cloud.google.com/static/billing/docs/images/cap-budget-lift-spend-cap.png)

  1. In the Google Cloud console, navigate to the **Budgets & alerts** page using the [procedure that fits your level of access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/budgets#to_modify_or_delete_a_budget_do_the_following).

  2. On the **Budgets & alerts** page, look for the spend caps informational banner, and select **View spend cap details** to view the Budgets dashboard filtered to display the spend cap budgets that are enforced.

  3. Click the **budget name** to open the budget for edit.

  4. On the **Edit budget** page, select **Lift spend cap** to unpause services and restart usage.

  5. Click **Confirm** to lift the spend cap.

     * If the cap was enforced and manually lifted within the same budget period, it won't trigger again for the rest of the budget period, unless you edit the budget to increase the target amount of the spend cap.
     * At the start of the next budget period, the spend cap budget is automatically reset and will trigger again if your costs breach the budget threshold in the current budget period.

**Note:** After you lift the cap, services might take up to one hour to fully return to normal function.



## Edit a spend cap budget

You can edit a spend cap budget to change the _budget name_ , _target amount_ , _project_ , or _eligible service_, or to manually lift an enforced spend cap. You can't edit other settings for a spend cap budget.

**Important:** You can't edit the settings of a spend cap budget while it's enforced. Before editing the budget settings, you must first manually lift the enforced spend cap.

  1. To edit a spend cap budget, **view the Budgets dashboard** using the [procedure that fits your level of access to Cloud Billing accounts and budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#to_modify_or_delete_a_budget_do_the_following).
  2. On the **Budgets & alerts** page, click the **budget name** of the spend cap budget you want to edit. This opens the **Edit budget** page.
  3. On the **Edit budget** page, modify the settings you want to change, and then click **Save**.



## Delete a spend cap budget

**Important:** You can't delete a spend cap budget while it's enforced. Before deleting a spend cap budget, you must first manually lift the enforced spend cap.

**Caution:** Deleted budgets can't be recovered.

  1. To delete a spend cap budget, **view the Budgets dashboard** using the [procedure that fits your level of access to Cloud Billing accounts and to delete budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#to_modify_or_delete_a_budget_do_the_following).
  2. On the **Budgets & alerts** page, **check the box** next to the **budget name** of the spend cap budget you want to delete.
  3. Click delete **Delete**.
  4. At the prompt, confirm this action.



## Create and manage spend cap budgets using an API

With the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap), you can view, create, and manage spend cap budgets programmatically at scale. This is especially useful if you're creating a large number of spend cap budgets across your organization.

## Frequently asked questions (FAQ)

  * What are spend caps?
  * What can I set spend caps on?
  * Will my resources or data be deleted when a cap triggers?
  * What happens to my in-flight requests?
  * How am I billed during a spend cap?
  * For spend caps, are there any changes to the cost reporting latency?
  * What happens if multiple users create overlapping spend caps from the budgets tool?
  * What is the difference between the spend capped budget available within AI Studio and the Cloud Billing console?
  * What happens if a user creates a spend capped budget for Gemini API from both AI Studio and the Cloud Billing console?
  * What happens if a project with a spend cap is moved from one billing account to another?



What are spend caps?
    

Spend caps are a cost control mechanism. A spend cap is enforced when usage costs exceed your budget target amount. When enforced, any new request to the eligible service(s), within the specified project, are paused and no further usage costs are accrued. No other projects or other services are impacted.

Spend caps typically use _estimated costs_ to trigger the alerts and caps, enforcing a cap much faster than the _actual costs_ are processed and appear on billing reports. Even though faster than reports, the enforcement of spend caps isn't instant and any cost overages are billed as normal.

Back to FAQ

What can I set spend caps on?
    

In your Cloud Billing account, you can set a cap on your budgets that are scoped to specific eligible services within a project. Spend cap budgets can only be set on one project and one service at a time. In this release, the eligible services include Gemini API, Agent Platform (formerly known as Vertex AI), Cloud Run, and Cloud Run functions. Additional services will be included in subsequent releases.

Back to FAQ

Will my resources or data be deleted when a cap triggers?
    

No, resources or data aren't deleted. Only usage of specific services is paused when the cap triggers. All other services and projects should work as normal.

Back to FAQ

What happens to my in-flight requests?
    

Only _new_ usage is blocked when the spend cap is enforced. In-flight usage is processed to completion.

Back to FAQ

How am I billed during a spend cap?
    

Any overage due to cost reporting latency is billed as usual. Additionally, any ongoing fixed costs needed to retain the services are billed as normal.

Back to FAQ

For spend caps, are there any changes to the cost reporting latency?
    

For certain services, we're able to estimate directional costs faster than the actual costs. For these services, we enforce the spend cap if the estimated directional costs reach the budget target amount. Directional costs don't appear on the cost reports. The actual costs for these services are published on cost reports, subject to the [same latency](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#delayed-billing) as today. Services for which we don't have estimated directional costs follow the regular cost reporting latency.

Back to FAQ

What happens if multiple users create overlapping spend caps from the budgets tool?
    

We have a deduplication policy that prevents users from creating more than one budget with the same scope.

Back to FAQ

What is the difference between the spend capped budget available within AI Studio and the Cloud Billing console?
    

Spend caps on Google Cloud Budgets brings the same spending protection offered in AI Studio, and expands it to the broader cloud platform with spend cap coverage on additional services.

Additionally, spend cap budgets in Cloud Billing trigger spending alerts as your accrued costs reach 50%, 80%, and 100% of your target budget amount.

Back to FAQ

What happens if a user creates a spend capped budget for Gemini API from both AI Studio and the Cloud Billing console?
    

If a user or multiple users create spend capped budgets from both AI Studio and the Cloud Billing console, the budget that receives usage cost faster is triggered first. However, regardless of where the cap is triggered from, usage for Gemini API is blocked for the project, across all platforms.

Back to FAQ

What happens if a project with a spend cap is moved from one billing account to another?
    

On the old billing account, all spend cap budgets for the project are deleted. To be active within the new billing account, the spend caps on the project must be re-created in the new billing account. If the project is moved while the spend cap is in an enforced state, the spend cap is automatically lifted, restoring normal function to the API calls that were paused, and enabling new charges to accrue.

Back to FAQ

## What's next

  * [Learn more about managing alerts-only budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets)
  * [Learn more about spend caps in AI Studio](https://ai.google.dev/gemini-api/docs/billing#spend-caps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
