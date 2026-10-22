---
url: https://docs.cloud.google.com/docs/cuds-multiprice/
title: Spend-based committed use discounts \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:51.773860+00:00
---

# Spend-based committed use discounts  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-multiprice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Spend-based committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

Spend-based committed use discounts (CUDs) provide a discount in exchange for your commitment to spend a minimum amount per hour for a product. The discount applies to the set of eligible resources for the product. For other types of CUDs, see [Committed use discounts](https://docs.cloud.google.com/docs/cuds).

**Important:** This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. To understand the changes and determine if there is required action on your part, see CUD program changes.

## Products covered by spend-based commitments

You must purchase separate spend-based commitments for each Google Cloud product that CUDs are available for. The CUDs apply to eligible usage in any projects that the Cloud Billing account pays for.

The following table shows which CUDs migrated to the new consumption model (direct discount, no credits) and which remain on the legacy credit model (list price charge + credit offset). This doesn't apply to [Resource-based CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) (for example, specific machine type commitments).

**Affected CUDs** (new CUD model using _discounts_) |  **Unaffected CUDs** (legacy CUD model using _credits_)  
---|---  
[ Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#applicable_discounts)  
 _(covers eligible spend on Compute Engine, Google Kubernetes Engine, and Cloud Run)_ |  [ All VMware Engine CUDs](https://docs.cloud.google.com/vmware-engine/docs/cud)  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/cud) |  [ Backup and DR (for VMware Engine)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud)  
[ Backup and DR (for Oracle)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) |  [NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/cuds)  
[BigQuery](https://docs.cloud.google.com/bigquery/docs/bigquery-cud) |  [ Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud)  
 _(no longer available for purchase)_  
[Bigtable](https://docs.cloud.google.com/bigtable/docs/cuds) |   
[Cloud SQL](https://docs.cloud.google.com/sql/cud)  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/cuds) |   
[Firestore](https://docs.cloud.google.com/firestore/docs/cuds) |   
[Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds)  
[Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/cuds) |   
[Spanner](https://docs.cloud.google.com/spanner/docs/cuds) |   
[Cloud Run](https://docs.cloud.google.com/run/cud)  
 _(no longer available for purchase)_ |   
[ Google Kubernetes Engine (GKE) Autopilot](https://docs.cloud.google.com/kubernetes-engine/cud)  
 _(no longer available for purchase)_ |   
  
## How spend-based CUDs work

When you purchase a commitment, you are committing to a specific hourly spend amount. The system checks your usage every hour to apply the discount. It is crucial to understand the boundaries of CUDs, specifically overage and underutilization scenarios.

**Important:** You **cannot cancel** the commitments you have purchased. You must pay the agreed-upon monthly amount for the duration of the commitment. Your commitment and the resources covered by it are not affected by future changes to the standard prices for those resources. If you accidentally purchased a commitment or made a mistake configuring your commitment, contact **Cloud Billing Support** for help.

### Overutilized CUDs (exceeding your commitment)

If your eligible usage in a given hour exceeds the amount you committed to, the CUD covers usage up to your limit, and the remainder is billed at the standard rate.

  * **Mechanism** : The system applies the CUD discount to the first block of usage equal to your commitment.
  * **Cost** : Any usage _beyond_ that limit is charged at the standard **on-demand price** (the "Default" consumption model). You don't receive any discount on the overage.



### Underutilized CUDs (not meeting your commitment)

If your eligible usage in a given hour is less than your committed amount, you are still responsible for the full cost of the commitment.

  * **No rollover** : Unused commitment does _not_ carry over to the next hour.
  * **Cost** : You pay for the full commitment amount you purchased.
  * **In the new consumption model** : Because you did not fully use the commitment, the FEE_UTILIZATION_OFFSET credit won't be large enough to fully negate the $1 CUD fee SKU. The remaining balance on the fee SKU represents your cost for the unused commitment.



The following screenshot shows how an underutilized CUD might appear in the **Cost breakdown** report.

![View of the underutilized cud](https://docs.cloud.google.com/static/docs/images/cuds-underutilized-view.png)

### Commitment amount and usage billing calculations

The CUD model determines how your commitment amount and usage billing is calculated, including how your savings are displayed:

|  **Affected CUDs** (new CUD model using discounts) |  **Unaffected CUDs** (legacy CUD model using credits)  
---|---|---  
  
**Commitment amount** |   
You commit to the **discounted spend** (the actual amount you pay). |   
You commit to the **on-demand spend** (the list price value).  
  
**Usage charges** |   
Usage is billed directly at the **discounted rate**. |   
Usage is billed at **list price** ; a credit offsets the cost.  
  
**Savings display** |   
Reports show **net savings** (calculated difference). |   
Reports show the **gross credit** amount.  
  
## Consumption models

The new CUD program introduces the concept of consumption models. In Cloud Billing, a consumption model represents the price you pay for a certain amount of SKU usage within a certain context. A SKU can have several consumption models, but only one applies to any given amount of usage at a particular time. Each SKU has at least one consumption model, whose description is `Default`.

Consumption models often represent various kinds of discounted SKU usage, such as committed use discounts (CUDs). For example, if a one year Flex CUD covers a particular VM usage, then the consumption model that applies to that SKU usage has the description `Compute Flexible CUD - 1 Year`.

For spend-based CUDs, consumption models replace the legacy system of using credits to offset usage costs calculated at list price. The new model also changes how commitments are purchased.

To support consumption models, several fields were added or updated in the Cloud Billing data model.

For each SKU, a new metadata field, `Consumption Model`, represents the price of usage for that SKU. This price applies when the system monetizes usage for that SKU under this particular consumption model. For example, if a 1-Year Flex CUD covers VM usage, then the consumption model of the usage has a value of `1 Year Flex CUD`.

Each commitment consumption model corresponds to a specific offer ID. For a list of the offer IDs, see the [Use the API to purchase a spend-based commitment](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing) page or the [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration) page. For details about how the data model uses these IDs, see [Offers and consumption model IDs](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#offer-consumption-ids).

### SKU and fee structure changes

The new CUD model introduces structural changes to how SKUs appear in your data and how fees are calculated.

  * **Usage list prices vs. Fee list prices** : The list price of your SKU _usage_ (for example, the cost of running a VM) has **not** changed. However, the list price of the _Fee SKUs_ has changed to **$1**. This is a structural change to the data model to support the new discount method.
  * **Direct comparison** : Because the Fee SKUs are now $1 (unlike the old model where they were priced lower to reflect the discount), you cannot compare the raw Fee SKU costs directly between models. To get an accurate comparison of your costs, you must calculate the total net cost including credits.
  * **Savings calculation formula** : In the new model, the Cost Management user interface reflects your savings using this formula: `Cost at on-demand rates - Cost at CUD consumption rate + CUD Fees`
  * **Fee utilization offset** : When you use your CUD, the system applies a credit called FEE_UTILIZATION_OFFSET that specifically negates the cost of the CUD fee SKU. If you are fully utilizing a CUD, the fee SKU will have a zero net cost.

The following screenshot shows how a fully utilized CUD might appear in your reports.

![View of the fully utilized cud](https://docs.cloud.google.com/static/docs/images/cuds-fully-utilized-view.png)

  * **Consumption models for usage** : A single SKU (for example, a specific VM instance type) can now have multiple consumption models.

    * **Default** : Represents the standard list price.
    * **CUD model** : Represents the discounted price (for example, "Compute Flexible CUD - 1 Year").
    * **Logic** : The system automatically applies the correct consumption model to your usage. If a 1-year Flex CUD covers a particular VM, that usage is recorded under the "1 Year Flex CUD" consumption model rather than "Default".



### New CUD fee SKUs

The existing CUD fee SKUs are replaced with new SKUs. These SKUs are priced at $1/hr, unlike the existing SKUs, which are priced at a lower rate to indicate the CUD benefit. The CUD benefit is now reflected using the consumption model prices described in Consumption models. This doesn't affect your costs.

New Offer IDs and Consumption model IDs are shared for all [in-scope CUDs](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds#affected-cuds).

## Flexible Savings Plans

A Flexible Savings Plan (FSP) is a type of spend-based commitment that lets you commit to a minimum monthly spend on a collection of eligible products. Unlike standard spend-based CUDs that use an hourly entitlement window, FSPs use a monthly entitlement window.

For more information, see [Flexible Savings Plans](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans).

## Common spend-based CUD tasks

For the most common spend-based CUD tasks, see the following:

  * Purchase spend-based commitments.
  * [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).
  * [Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts).
  * [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

**Important:** You **cannot cancel** the commitments you have purchased. You must pay the agreed-upon monthly amount for the duration of the commitment. Your commitment and the resources covered by it are not affected by future changes to the standard prices for those resources. If you accidentally purchased a commitment or made a mistake configuring your commitment, contact **Cloud Billing Support** for help.

## Purchase spend-based commitments

Before purchasing, review these details to ensure the commitment aligns with your situation.

  * **Region specificity** : Most spend-based CUDs are restricted to the region you select during purchase. Eligible usage in other regions will **not** count toward the commitment and will be charged at on-demand rates.
  * **Billing account scope** : Commitments are tied to the specific billing account used for purchase. You **cannot share** the discount across different billing accounts, even if they belong to the same organization.
  * **Irreversibility** : Once purchased, you **cannot cancel** a commitment. You are obligated to pay the agreed-upon amount for the full duration of the term (1 or 3 years), regardless of changes in your business needs or usage patterns.
  * **No modifications** : You cannot lower your commitment amount or change the region or term after purchase. However, you can purchase _additional_ CUDs to stack on top of existing ones if your usage grows.



You can purchase spend-based CUDs in the Google Cloud console.

### Permissions required

To purchase or manage spend-based CUDs for your billing account, you must be a **Billing Account Administrator**.

### Steps to purchase

  1. Sign in to the Google Cloud console.
  2. Open the **Navigation menu** and select **Billing**.
  3. If you have multiple billing accounts, select **Go to linked billing account** or **Manage billing accounts** to choose the correct one.
  4. From the Cloud Billing menu, select **Committed use discounts (CUDs)**.
  5. Select **Purchase CUD** in the action bar.
  6. Select the **Product** (for example, Compute Engine).
  7. Enter a **Name** for your commitment.
  8. Choose a **Commitment term** (1 or 3 years).
  9. **Enter your hourly commitment amount.**
     * **For new model CUDs** : Enter the **equivalent discounted spend**.
     * **For legacy model CUDs** : Enter the **equivalent on-demand spend**.
     * Use the **CUD recommendations tool** in the console. It automatically calculates the correct amount based on your historical usage.
  10. Review the **Commitment summary**.
  11. Click **Purchase** to preview, and then click **Purchase** again to confirm.



### CUD activation time

After purchase, the commitment goes into effect based on the time of purchase:

  * **Purchased at :00 to :49 (first 50 minutes of the hour)** : Starts at the beginning of the _next_ hour.
  * **Purchased at :50 to :59 (last 10 minutes of the hour)** : Skips an hour and starts at the beginning of the _hour after next_.



## CUD program changes

As part of the CUD migration, the majority of spend-based CUDs have moved to a new consumption model that charges the discounted price directly. However, a small subset of CUDs remain on the legacy credit-based model. Existing CUD customers might need to take action to adopt the new CUD program.

The changes include:

  * **Simplified billing** : Google Cloud uses discounted prices to represent savings from spend-based CUDs, making it easier for you to calculate the total cost of your CUDs and savings. This moves away from the legacy concept of offering credits to offset costs.
  * **Greater flexibility** : Expands the scope for some spend-based CUDs. As a result, a larger portion of your usage might be eligible for discounts. These changes don't increase your total costs.
  * **Added consumption models** : A better way to understand and track your cloud spending, especially concerning promotional offers and discounts. For more information, see consumption models.
  * **Expanded product coverage for CUDs**. For more information, see affected CUDs.
  * **Changed display of direct savings** : We now display the direct CUD savings on your bill. For more information, see [Understand how CUDs impact your bill](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds#credits-display-change).
  * **Simplified CUD fee SKUs** : New CUD fee SKUs replace existing CUD fee SKUs. The price for these new SKUs is $1. For more information, see Simplified CUD fee SKUs.
  * **Updates to the CUD purchasing experience** : Your hourly commitment amount is now the discounted price instead of the on-demand price. For more information, see [CUD purchasing experience](https://docs.cloud.google.com/docs/cuds-spend-based#steps_to_purchase).
  * **New CUD metadata export** to BigQuery. For more information, see [CUD metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).



### Determine any required action

Depending on your configuration, you might need to take action to ensure compatibility with the CUD data model:

  * **For BigQuery users** : If you export Cloud Billing data to BigQuery, you must update any internal systems that depend on the previous data schema. This includes updating FinOps cost management reporting dashboards to match the new schema.
  * **For[Cloud Commerce Consumer Procurement API](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing) users**: The API is updated to enable purchasing of CUDs in the new model. It requires you to update any code that automates purchases of spend-based CUDs to use the new offer names and commitment amounts.



### Helpful resources

Use the following resources to update your internal systems that might be affected by the CUD data model:

  * **[Spend-based CUDs data model updates](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel)** : Details about the spend-based CUD data model changes and tools to help you adopt the changes.
  * **[Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)** : Explains how to view and confirm your discount percentages, savings, and ROI after migration.
  * **[CUD KPI example queries](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#cud-kpis)** : Example queries that show how to use Key Performance Indicators (KPIs) metrics to validate that your systems are functioning well with the CUD data model.
  * **[List of new CUD fields](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#cud-product-info)** : Descriptions of new fields, such as CUD Fee SKU IDs, offer names, and consumption model IDs.
  * **[Migrated CUD SKUs, offers, and new consumption models](https://docs.cloud.google.com/docs/cuds-migration)** : Information on migrated CUD SKUs, offers, and consumption model IDs within the new program data model.
  * **[CUD metadata export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export)** : Provides a daily snapshot of your spend-based CUDs commitment metadata to a BigQuery table.



## Billing user interface improvements

We improved the [Billing section](https://console.cloud.google.com/billing/overview) of the Google Cloud console to better enable accurate cost management and optimization experiences for CUDs.

To see the list of improvements to the Cloud Billing user interface, see [Billing user interface improvements](https://docs.cloud.google.com/docs/cuds-billing-ui-improvements).

## Get support

If you have questions regarding how CUDs appear on your bill or need assistance with the data model, contact **Cloud Billing** support.

## Next steps

  * [Determine your commitment amount](https://docs.cloud.google.com/docs/cuds-choose-correctly)



## Related topics

  * [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration)
  * [Committed use discounts](https://docs.cloud.google.com/docs/cuds)
  * [Flexible Savings Plans](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans)
  * [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds)
  * [Verify your discounts](https://docs.cloud.google.com/docs/cuds-verify-discounts)
  * [View the credits you are receiving in reports](https://docs.cloud.google.com/billing/docs/how-to/reports#credits)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
