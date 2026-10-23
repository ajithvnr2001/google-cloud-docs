---
url: https://docs.cloud.google.com/vmware-engine/docs/cud/
title: Committed use discounts \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:43.818272+00:00
---

# Committed use discounts  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Committed use discounts

This page describes committed use discounts (CUDs) for Google Cloud VMware Engine and how to purchase and view them.

VMware Engine CUDs are spend-based billing commitments that provide discounted node pricing in exchange for committing to a consistent level of usage for a one- or three-year term. These discounts are ideal for workloads with predictable resource needs, letting you reduce costs without manually managing capacity.

This guide is for billing administrators, project owners, and users with custom billing roles who make procurement decisions and manage cloud costs. To purchase or view commitments, you must enable the Enterprise Purchasing API and have appropriate billing permissions.

## What are VMware Engine committed use discounts?

_Committed use discounts (CUDs)_ are an optional pricing model for VMware Engine that provide discounted prices in exchange for committing to continuously use VMware Engine nodes in a particular region for a one- or three-year term. Provisioning VMware Engine nodes does not require a CUD, and capacity can always be deployed flexibly on an on-demand basis.

VMware Engine CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in $/hour of equivalent on-demand spend, for a one- or three-year term. In exchange, you receive a discounted rate on the applicable usage your commitment covers.

**Note:** Three-year CUDs are available only for post-paid `ve2` node commitments. All three-year post-paid `ve2` CUDs purchased after May 31, 2026, terminate on October 15, 2028, and three-year CUD pricing applies regardless of the actual term. For `ve1` nodes and eligible pre-paid commitments, only one-year CUDs are available.

## VMware Engine CUD agreement type

VMware Engine gives you the following commitment options for node types:

  * _Portable License commitment_ : includes only VMware Engine nodes. For this commitment type, you need to use your portable VMware Cloud Foundations license to pay for the capacity of node and VMware components. This is the only CUD model available for new purchases.

  * _Fully licensed commitment_ : includes VMware Engine nodes with VMware Cloud Foundations licenses for the capacity of the node and the VMware components. This model is no longer available for sale.

  * _Fully licensed convertible commitment_ : includes VMware Engine with VMware Cloud Foundations licenses for the capacity of the node and the VMware components. This offers the flexibility of CUD conversion. For more information about conversion of CUDs, contact your sales team. This model is no longer available for sale.

  * _Legacy License commitment_ : all commitments purchased prior to July 25, 2024 are considered legacy. These CUDs remain valid until their expiry dates. This model is no longer available for sale.




CUD Analysis is **not supported** for the following agreement types: Fully licensed, Fully licensed convertible, and Portable license commitments.

CUD analysis for upfront legacy CUDs is **not supported** ; ignore any recommendations provided.

See [VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing) for examples of pricing that include CUDs.

## How do CUDs apply to VMware Engine usage?

CUDs automatically apply to aggregate VMware Engine node usage in a region, giving you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility saves you time and helps you to save more by achieving high utilization rates across your commitments.

VMware Engine CUDs apply to all VMware Engine nodes for the region for which you have purchased commitments. VMware Engine CUDs **don't apply** to storage, backups, IP Addresses, network outbound data transfer, or licensing.

## Purchasing VMware Engine commitments

To learn more about purchasing spend-based commitments, see the Google Cloud [Committed use discounts](https://docs.cloud.google.com/docs/cuds) page.

You can purchase CUDs from any Cloud Billing account, and the discount applies to any eligible usage in projects paid for by that Cloud Billing account. Any usage beyond your commitment, or provisioning without an active CUD, is charged at the standard on-demand rate. Before you purchase a commitment, read the [Service specific terms](https://cloud.google.com/terms/service-terms) regarding Committed Units.

**Warning:** Once you purchase a CUD, you **can't** cancel it. 

VMware Engine CUDs are [spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based) and not tied to a specific project or resource. 

**Caution:** Spend-based commitments are purchased at the Cloud Billing account level. You can't cancel these commitments or change the Cloud Billing account that they are associated with.

When you purchase a VMware Engine CUD, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly or upfront, depending on the type of CUD.

## Before you begin

Before you can purchase a CUD, make sure you have the correct Enterprise Discount Program (EDP) and CUD information.

### Enable Enterprise Purchasing API

You must enable the Enterprise Purchasing API to purchase and view CUD details in the VMware Engine portal. If this API isn't enabled, you can't see your VMware Engine CUDs. When you click the **Purchase** button on the **Committed use discounts** page for the first time, you're prompted to enable the API if it's not already enabled.

Make sure that you have the following role or roles on the project: roles/owner, roles/billing.admin 

#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



Alternatively, you can make a purchase with a custom role with the following permissions:

  * `enterprisepurchasing.gcveCuds.list`
  * `enterprisepurchasing.gcveNodePricingInfo.list`
  * `enterprisepurchasing.gcveCuds.create`
  * `billing.accounts.get`
  * `billing.subscriptions.create`
  * `vmwareengine.projectState.get`
  * `consumerprocurement.orders.place`
  * `resourcemanager.projects.get`



See [VMware Engine IAM roles and permissions][vmware engine iam] for more information.

### Purchasing commitments for node types

You can purchase commitments for node types by using the Google Cloud console. After purchasing a CUD, monthly paid CUDs begin within an hour of purchasing, while upfront paid CUDs begin at 12 AM Pacific.

CUDs are automatically applied to eligible usage in the region you specified. If there is no eligible usage in that region, you can add VMware Engine nodes to count towards your commitment by [requesting node quota](https://docs.cloud.google.com/vmware-engine/quotas#requesting_quota).

**Note:** Upfront or prepaid commitments, Legacy license commitments, and Fully licensed convertible commitments are generally not available for new purchases. To find out if you are eligible to purchase or renew one of these commitment types, contact Cloud Customer Care or your Google Cloud account team.

To purchase a VMware Engine spend-based commitment in your project, do the following:

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/vmwareengine/commitments)

  2. Click **Select a project** and then select the organization, folder, or project where you want to purchase the commitment.

  3. Click **Purchase**.

  4. In the **Name** field, provide a name that helps you identify the commitment that you're purchasing.

  5. Select the region where you want to spend towards your commitment.

  6. Choose a subscription type for your commitment.

  7. Choose an Agreement Type.

  8. Choose a commitment duration of 1 or 3 years. Three-year commitments are available only for post-paid `ve2` nodes and terminate on October 15, 2028. For `ve1` nodes and eligible pre-paid commitments, only a one-year duration is available.

  9. Select a node type and node count for your commitment.

  10. Review the information you provided and click **Purchase** to purchase the commitment.




Prices are estimated and might differ from the final price.

For information about how to view the audit logs, see [Committed use discounts audit logging](https://docs.cloud.google.com/vmware-engine/docs/cud-audit-logging).

## Questions and challenges

Consider the following questions and answers in addition to some challenges you might face and how to address them:

### Where do I find discount information?

You can find discount information by doing the following:

  1. Check the contracts signed with Google Cloud.
  2. Talk to your Google account representative.
  3. Check the pricing table found in your billing account and search for VMware Engine SKUs by filtering for the "VMware Engine" service description. The discount column displays your discount percentage.
  4. Check for the **Discount** column VMware Engine pay-as-you-go SKUs. For example, look for "Standard 72 VCPU Node (REGION_NAME)" for ve1 nodes.



### What kind of discount information do I need to know before purchasing CUDs?

Discounts are automatically applied based on the billing account and existing contracts. You can find your discounts on the [pricing page](https://console.cloud.google.com/billing/pricing). Confirm if the shown discounts match your contracts before purchasing.

### More questions and challenges

Question or challenge | How it can be addressed  
---|---  
What happens if the wrong CUD is purchased? | Reach out to your Google representative as soon as possible to facilitate a resolution.  
I am a resold customer and my partner does not have access to my projects. This is stopping the partner from buying commitments. | Create a new project under the same billing account and give access to that project to the partner to access the purchase page. This project is just used for purchasing commitments only.  
  
## CUD Visibility

How can I list all CUDs associated with my Billing Account?

  * Running the following command from the Cloud Shell will return all CUDs associated with the Billing Account of the current project:
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://enterprisepurchasing.googleapis.com/v1alpha/projects/$GOOGLE_CLOUD_PROJECT/locations/global/gcveCuds
        




## What's next

  * [Analyze the effectiveness of your spend-based committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based) CUD analysis is not supported for upfront CUDs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
