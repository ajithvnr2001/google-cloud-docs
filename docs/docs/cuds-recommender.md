---
url: https://docs.cloud.google.com/docs/cuds-recommender/
title: Get recommendations for committed use discounts (CUDs) \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:12.464667+00:00
---

# Get recommendations for committed use discounts (CUDs)  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Get recommendations for committed use discounts (CUDs) Stay organized with collections  Save and categorize content based on your preferences. 

[Committed use discount (CUD)](https://docs.cloud.google.com/docs/cuds) recommendations help you optimize the resource costs of the projects in your Cloud Billing account. CUD recommendations are automatically generated using a formula that analyzes historical and recent usage metrics gathered by Cloud Billing, and includes usage covered by existing commitments. You can apply these recommendations to purchase additional commitments and further optimize your Google Cloud costs.

Recommendations are available for a [subset of resource-based commitments](https://docs.cloud.google.com/docs/cuds-recommender#supported-resource-types-recommendation) and a [subset of spend-based commitments](https://docs.cloud.google.com/docs/cuds-recommender#supported-spend-types-recommendation) for [eligible products](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) , including [Compute flexible commitments](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

Refer to the guides on this page to learn about the following tasks:

  * [Understand commitment recommendations](https://docs.cloud.google.com/docs/cuds-recommender#understanding-recommendations)
  * [Set permissions to access recommendations](https://docs.cloud.google.com/docs/cuds-recommender#permissions)
  * [View recommendations](https://docs.cloud.google.com/docs/cuds-recommender#viewing-recommendations)
  * [Interpret the recommendation summary](https://docs.cloud.google.com/docs/cuds-recommender#understanding-summary-cards)
  * [Simulate scenarios for spend-based CUDs savings](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios)
  * [Apply recommendations to purchase additional commitments](https://docs.cloud.google.com/docs/cuds-recommender#purchasing-recommendations)
  * [Dismiss recommendations](https://docs.cloud.google.com/docs/cuds-recommender#dismissing-recommendations)
  * [Configure recommendation settings](https://docs.cloud.google.com/docs/cuds-recommender#configure-recommendation)



For more information about the Recommender service, see the [Recommender overview](https://docs.cloud.google.com/recommender/docs/overview).

## Understand commitment recommendations

Committed use discount recommendations let you identify spending and usage patterns in your Google Cloud projects. Your spending patterns generate recommendations for [spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based), including [Compute flexible commitments](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based), and your usage patterns on Compute Engine generate recommendations for [resource-based commitments](https://docs.cloud.google.com/docs/cuds#resource_based_commitments). The recommendations for resource-based commitments also account for your use of [custom machine types on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type). Purchasing the recommended commitments helps you optimize your Google Cloud costs.

## How recommendations are calculated

Google Cloud analyzes your usage history over the previous 30 days to generate commitment recommendations. The recommendations are based on two logical model types that analyze your consumption:

  * **Recommendations for stable usage** : Calculates the recommended commitment quantity by analyzing resources that were continuously active over the 30-day period. These commitments cover steady-state workloads.
  * **Recommendations for optimal savings** : Calculates the recommended commitment quantity to maximize overall net savings. This model also considers periods of bursting or intermittent usage. This model recommends commitments for usage periods that exceed a financial break-even threshold, which represents the point where your discount outweighs the commitment cost compared to standard rates. For example, if a commitment offers a 30% discount, then an instance needs to run for more than 70% of the month to break even. Because this model maximizes overall net savings, recommended commitment quantities might sometimes exceed your uncommitted usage on specific days or hours.



Usage is considered uncommitted and eligible if the following is true:

  * The instance's uptime during the 30-day period met or exceeded the financial break-even threshold.
  * The resource belongs to a [machine series or resource type that is eligible for resource-based CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#about-resource-based-commitments).
  * The resource belongs to a machine series or resource type that supports CUD recommendations.
  * The instance's usage was not already covered by an existing commitment.



You can view commitment recommendations on the **FinOps hub** or the **Recommendations** page. For detailed steps on accessing these pages, see View recommendations. After you select a specific recommendation, you can also create a scenario to simulate specific conditions and customize your recommendation.

## Limitations

  * Spend-based CUD recommendations are available only on the Google Cloud console. However, you can view resource-based CUD recommendations by using the Google Cloud console, [Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), and the [Recommender API](https://docs.cloud.google.com/recommender/docs/overview).
  * CUD recommendations are not available for the A3 Ultra, A4, A4X, and A4X Max machine series.
  * CUD recommendations are not available for Cloud TPUs.



## Supported resources and services

This section describes the resources and services for which you can receive CUD recommendations.

### Resource-based CUD recommendations

Resource-based CUDs are available only for Compute Engine. These CUDs are available for both hardware resources (such as vCPUs, memory, GPUs, and Local SSD disks) as well as software resources (such as OS licenses). Resource-based CUD recommendations are available for the following hardware and software resources:

#### Hardware resources

The following table lists the hardware various Compute Engine machine series, resource types, and commitment types for which you get CUD recommendations.

For all GPU types and most Local SSD disks, you must manually create and attach reservations when you purchase the recommended resource-based commitments. For more information, see [Combine reservations with commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

General-purposeCompute-optimizedMemory-optimizedAccelerator-optimizedGraphics-optimizedStorage-optimized

A2C2C2DC3C3DC4C4AC4DE2G2G4H3H4DM1M2M3M4N1N2N2DN4N4AN4DTau T2DX4Z3

Clear all

Supported machine series | Supported commitment type | Supported resources  
---|---|---  
[C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) | General-purpose C3 | vCPUs, memory, and Local SSD disks  
[C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series) | General-purpose C3D | vCPUs, memory, and Local SSD disks  
[C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) | General-purpose C4 | vCPUs, memory, and Local SSD disks  
[C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) | General-purpose C4A | vCPUs, memory, and Local SSD disks  
[C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) | General-purpose C4D | vCPUs, memory, and Local SSD disks  
[E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) | General-purpose E2 | vCPUs and memory  
[N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) | General-purpose N1 | vCPUs, memory, GPUs, and Local SSD disks  
[N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) | General-purpose N2 | vCPUs, memory, and Local SSD disks  
[N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) | General-purpose N2D | vCPUs, memory, and Local SSD disks  
[N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) | General-purpose N4 | vCPUs and memory  
[N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) | General-purpose N4A | vCPUs and memory  
[N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series) | General-purpose N4D | vCPUs and memory  
[Tau T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) | General-purpose Tau T2D | vCPUs and memory  
[C2](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) | Compute-optimized C2 | vCPUs, memory, and Local SSD disks  
[C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_series) | Compute-optimized C2D | vCPUs, memory, and Local SSD disks  
[H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series) | Compute-optimized H3 | vCPUs and memory  
[H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) | Compute-optimized H4D | vCPUs, memory, and Local SSD disks  
[M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_series), [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_series) | Memory-optimized M1/M2 | vCPUs, memory, and Local SSD disks (M2 only)  
[M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series) | Memory-optimized M3 | vCPUs, memory, and Local SSD disks  
[M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) | 

  * Memory-optimized M4
  * Memory-optimized M4 6TB

| vCPUs and memory  
[X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series) | 

  * Memory-optimized X4 6TB
  * Memory-optimized X4 8TB
  * Memory-optimized X4 12TB
  * Memory-optimized X4 16TB
  * Memory-optimized X4 24TB
  * Memory-optimized X4 32TB

| vCPUs and memory  
[A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2_vms) | Accelerator-optimized A2 | vCPUs, memory, GPUs, and Local SSD disks  
[G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) | Graphics-optimized G2 | vCPUs, memory, GPUs, and Local SSD disks  
[G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) | Graphics-optimized G4 | vCPUs, memory, GPUs, and Local SSD disks  
[Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series) | Storage-optimized Z3 | vCPUs, memory, and Local SSD disks  
  
**Note:** For C4, C4A, C4D, G4, H4D, and Z3 series, when you specify Local SSD disks in your commitments, you don't need to attach reservations for those disks. However, for Local SSD disks for use with all other machine series and for all GPUs, you must also reserve those resources and attach the reservations to your commitment.

For more information, see [Hardware commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#hardware-commitments).

#### Software resources

Compute Engine offers software resource-based CUDs for specific operating system (OS) licenses. Resource-based CUD recommendations are available for the following OS licenses:

  * SUSE Linux Enterprise Server (SLES)
  * SLES for SAP
  * Red Hat Enterprise Linux (RHEL)



For more information, see [Software license commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchaselicensecommitment).

### Spend-based CUD recommendations

Spend-based CUD recommendations are available only for the following services:

  * AlloyDB for PostgreSQL
  * Backup and DR Service
  * Dataflow Streaming CUD Subscription
  * Memorystore
  * Spanner
  * Cloud SQL
  * Compute flexible CUDs
  * Google Cloud VMware Engine
  * Google Cloud NetApp Volumes



For more information, see [Spend-based commitments](https://docs.cloud.google.com/docs/cuds#spend_based_commitments).

## Permissions required to view and modify recommendations

Depending on your needs, ask your administrator to assign the following predefined IAM roles:

  * If your Cloud Billing account has [resource-based CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing) enabled, then you need one of these roles on the Cloud Billing account:

    * To view recommendations only, assign the **Billing Account Viewer** (`roles/billing.viewer`) role.
    * To view and modify recommendations, assign the **Billing Account Administrator** (`roles/billing.admin`) role.

[Learn how to assign these roles to manage access to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing).

  * If your Cloud Billing account does _not_ have [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing) for resource-based commitments, you need one of these roles on each project attached to your Cloud Billing account that has purchased committed use discounts:

    * To view recommendations only, assign the **Viewer** (`roles/viewer`) role on the projects.
    * To view and modify recommendations, assign the **Owner** (`roles/owner`) or **Editor** (`roles/editor`) role on the projects.

[Learn how to assign these roles to manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




If you are using custom roles, update the custom role to include the following individual permissions:

#### (Click to expand) Permissions required for custom roles

### Permissions to simulate scenarios for CUD savings

  * To simulate scenarios based on list prices, you need `billing.cudrecommendations.generateDefaultPriceSavingRecommendation`
  * If you have a custom pricing contract, you need `billing.cudrecommendations.generateCustomPriceSavingRecommendation` to simulate scenarios based on your custom prices.



### Permissions to view recommendations

To view _spend-based_ CUD recommendations:

  * `recommender.spendBasedCommitmentRecommendations.get`
  * `recommender.spendBasedCommitmentRecommendations.list`
  * `recommender.spendBasedCommitmentInsights.get`
  * `recommender.spendBasedCommitmentInsights.list`
  * `recommender.spendBasedCommitmentRecommenderConfig.get`



To view _resource-based_ CUD recommendations:

  * `recommender.usageCommitmentRecommendations.get`
  * `recommender.commitmentUtilizationInsights.get`
  * `recommender.usageCommitmentRecommendations.list`
  * `recommender.commitmentUtilizationInsights.list`



### Permissions to modify recommendations

To modify _spend-based_ CUD recommendations:

  * `recommender.spendBasedCommitmentRecommendations.update`
  * `recommender.spendBasedCommitmentInsights.update`
  * `recommender.spendBasedCommitmentRecommenderConfig.update`



To modify _resource-based_ CUD recommendations:

  * `recommender.usageCommitmentRecommendations.update`
  * `recommender.commitmentUtilizationInsights.update`

**Note:** Granting your users these permissions might give them a partial view of the resource for which the recommendation is generated. For more information, see the Recommender [Overview](https://docs.cloud.google.com/recommender/docs/overview). 

## View recommendations

There are different ways to view your committed use discount recommendations, depending on the commitment type:

  * **Spend-based CUD recommendations** : Available only in the Google Cloud console.
  * **Resource-based CUD recommendations** : Available in the Google Cloud console, through [Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), and through the [Recommender API](https://docs.cloud.google.com/recommender/docs/overview).



### View recommendations in the Google Cloud console

Commitment recommendations are available on two pages in the Billing section of the Google Cloud console:

  * **[FinOps hub](https://console.cloud.google.com/billing/optimize)** : Displays only the top recommendations that yield the highest estimated savings, which are typically the optimal savings recommendations.
  * **Recommendations page** : Displays all available recommendations, which includes both stable usage and optimal savings recommendations. You can also view commitment recommendations for specific services or projects.



To view the committed use discount recommendations for your Cloud Billing account, do one of the following:

View recommendations for maximum savings | View all available recommendations | View recommendations for a specific service or project  
---|---|---  
  
If you have Cloud Billing account permissions, you can view the commitment recommendations that provide the highest estimated savings on the **FinOps hub** page of the Google Cloud console.
  1. In the Google Cloud console, open the FinOps hub. [ Go to FinOps hub](https://console.cloud.google.com/billing/optimize)
  2. At the prompt, choose the Cloud Billing account for which you want to view recommendations. If there are CUD recommendations available for your Cloud Billing account, then you see them in the **Top recommendations** section. 
  3. To view detailed information about a recommendation, in the **Potential savings/month** column, click the recommendation that you want.

| 

If you have Cloud Billing account permissions, you can view the complete list of available recommendations (both stable usage and optimal savings recommendations) by using the **Recommendations** page. You can access this page from either the **CUD analysis** page or the **Committed use discounts** page, as follows. 
  1. In the Google Cloud console, open the Committed use discounts page. [ Go to Committed use discounts](https://console.cloud.google.com/billing/reports/commitments)
  2. In the toolbar, click **Recommendations**. The **Recommendations** page appears.
  3. To view detailed information about a recommendation, in the **Potential savings/month** column, click the recommendation that you want.

| 

If you have Cloud Billing account permissions, you can view the complete list of available recommendations (both stable usage and optimal savings recommendations) by using the **Recommendations** page. You can access this page from either the **CUD analysis** page or the **Committed use discounts** page, as follows. 
  1. In the Google Cloud console, open the Committed use discounts page. [ Go to Committed use discounts](https://console.cloud.google.com/billing/reports/commitments)
  2. In the toolbar, click **Recommendations**. The **Recommendations** page appears.
  3. To view recommendations for a specific service, in the **Services** menu, select the service name.
  4. To view recommendations for a specific project, in the **Projects** menu, select the project name.
  5. To view detailed information about a recommendation, in the **Potential savings/month** column, click the recommendation that you want.

  
  
## Interpret the recommendation summary

The following is an example of a recommendation summary for a spend-based CUD recommendation, with the chart that shows how the recommendation is calculated. At a high level, the recommendation is based on your resource utilization, how much of your usage you want to cover with CUDs, and your existing CUDs. The chart shows you the level of utilization at which you'll save costs by signing up for a commitment.

![Example of a spend-based committed use discount recommendation summary.](https://docs.cloud.google.com/static/billing/docs/images/cud-recommendations-summary.png)

**Note:** The preceding screenshot shows the recommendation summary page in [the new CUDs model](https://docs.cloud.google.com/docs/cuds-multiprice). In the legacy CUDs model, the recommendation summary page has the following differences: 

  * The **Estimated cost with recommended CUD** field is **Estimated CUD cost** instead.
  * The **Usage Insights** description is different, for example it would be "If $1.02/hr is spent for at least 263 days (72% of 1 year), you will break even with this CUD purchase." instead.



### Estimate your optimal usage

#### Usage insights

For a brief explanation of how your spend-based recommendation was calculated, see the **Usage insights** section of the recommendation. Usage insights explains the break-even point for your commitment purchase. For example, your usage insight will look similar to this, depending on the details of your CUD recommendation:

"With the recommended CUD coverage of $90.00/hr, savings will remain positive even if eligible usage drops by 54%."

**Note:** In the legacy CUDs model, the usage insight detail would be different.

#### Example of how to calculate your optimal usage

**Note:** The calculations in this example are based on covering 100% of your eligible usage with a commitment purchase. If you choose a lower percentage of coverage, your recommended CUD might change. Learn how to configure the usage that you want your recommendations to cover.

To estimate the resource utilization at which you'll break even on your costs, subtract the CUD discount percentage from 100. For example, if you get a recommendation for a 1-year Cloud SQL CUD with a discount of 25%, the resource utilization at which you'll break-even is `100% - 25% = 75%`.

To understand the estimate, consider Cloud SQL usage of $100 at list price. If your Cloud SQL instances run at 100% uptime, and you sign up for a 1-year spend-based CUD at a 25% discount, you'll pay `$100 - (25% of $100) = $75` for your usage.

If the uptime for your Cloud SQL instances reduces to 80%, your list price is $80, but with a commitment, you'd pay $75 for your usage, which still gives you a `($80 - $75) / $80 = 0.0625` or a `6.25%` discount on the list price.

Similarly, at 75% uptime, your costs are the same as if you were paying the list price, and at less than 75% uptime, you no longer save money by signing up for a commitment.

For a brief explanation of how your spend-based recommendation was calculated, see the **Usage insights** section of the recommendation.

## Simulate scenarios for CUDs savings

In the FinOps hub, you can use a _spend-based_ or _resource-based_ CUD recommendation as a starting point to simulate various usage scenarios, and customize the recommendation to purchase a commitment that maximizes your savings. You can do the following as part of your scenario modeling:

  * Toggle between 1-year and 3-year commitment terms.
  * Adjust your coverage threshold.
  * Choose a different usage period to calculate your recommendation.
  * Opt to ignore atypical usage history.



[Go to FinOps hub](https://console.cloud.google.com/billing/optimize)

### Create a CUD scenario model

  1. To start customizing a recommendation in the FinOps hub, click the **recommendation** you want to model.
  2. On the recommendation's details page, click **Create a scenario**.
  3. In the scenario modeling tool, use the options that best reflect your usage. Some of the ways you can customize the recommendation are as follows:

     * **Recommendation based on usage history** section: By default, the recommendation is based on the last 30 days of usage. To analyze your usage over a longer time, change the number of days of history to consider.

To exclude dates where you might have had atypical usage, such as a period where you had unusually high demand, enable **Ignore usage history from specific days** , and specify a time range.

The recommendation is recalculated based on the number of days that you select and the dates that you exclude.

     * **Eligible usage covered** section: You can model the amount of usage covered by a CUD, depending on the CUD type:

       * For spend-based CUDs, you can set a percentage of spend per hour.
       * For resource-based CUDs, you can set a number of resource units used.

To help you model your real-world usage more accurately, this section includes a message that shows your actual stable usage for the model's date range.

**Note:** You might notice a discrepancy in _Savings_ and _Recommended purchase_ values between a standard recommendation and a scenario model, even when using identical coverage. This is because scenario modeling uses the most recent data available but the standard recommendations use pre-calculated daily snapshots, which might have older data.
     * **CUD term** section: You can select a 1-year or 3-year term for the CUD scenario model. The recommendation is recalculated if you change the selected term.




For example, the following screenshot shows a CUD scenario model recommendation for the purchase of a 3-year Compute flexible commitment, based on the previous 30 days of usage.

![Example of a committed use discounts scenario.](https://docs.cloud.google.com/static/billing/docs/images/cud-scenario-model.png)

**Note:** The preceding screenshot shows the recommendation summary page in [the new CUDs model](https://docs.cloud.google.com/docs/cuds-multiprice). In the legacy CUDs model, the recommendation summary page has the following differences: 

  * The is **Cost of usage without CUD scenario model** field is not present.
  * The **Estimated cost with CUD scenario model** field is **Estimated CUD cost** instead.
  * The **Usage Insights** description is different, for example it might be similar to "Historically this billing account has spent the recommended amount of $2.20/hr for 31 out of last 53 days, on resources covered by this CUD." and "If $1.02/hr is spent for at least 263 days (72% of 1 year), you will break even with this CUD purchase." instead.



#### Usage insights in the scenario model

In the _CUD scenario model_ , the **Usage insights** section provides a brief explanation of how your spend-based recommendation was calculated. Usage insights for the scenario include your historical spending patterns for the recommended amount, and explains the break-even point for your commitment purchase. For example, your usage insights will look similar to this, depending on the details of your CUD scenario model:

  * "With the CUD scenario model coverage of $0.07/hr, savings will remain positive even if eligible usage drops by 47%."



### Share the CUD scenario model

To share the scenario's configuration with others, click link**Copy to clipboard** to copy a link that you can share. When your recipients open the link, they see the scenario with the parameters that you chose, and with updated information about additional usage that occurs before they open the link.

## Apply recommendations to purchase additional commitments

After you've reviewed the recommendation and selected the options that meet your needs, you can start the purchase process.

**Warning:**

Before applying and purchasing recommended commitments, ensure that the commitments are assessed by a reviewer. The reviewer should have the knowledge to assess usage patterns identified in recommendations, as well as effects specific to your infrastructure and business.

The reviewer should understand the following about commitments:

  * Committed use discounts apply only to the [ specific resources](https://docs.cloud.google.com/docs/cuds#commitment_types) in scope for the commitment you are purchasing.
  * When you purchase a commitment, you agree to pay the applicable [ monthly fees](https://docs.cloud.google.com/docs/cuds#pricing) for the term of the commitment. These monthly fees _cannot be cancelled_ , and apply regardless of actual usage. [ Learn more](https://docs.cloud.google.com/docs/cuds)
  * Before purchasing the recommended commitments, review the Google Cloud [ Service Specific Terms](https://cloud.google.com/terms/service-terms#pricing-and-billing-terms) for Pricing and Billing, regarding Committed Units.



### Review and purchase recommendations

To purchase a recommended commitment, open the recommendation's details page and do the following, depending on whether the recommendation is for resource-based or spend-based CUDs:

###  Spend-based 

  1. While viewing your commitment recommendations, click the recommendation that you want to purchase.

  2. Click **Review and purchase** at the bottom of the page.

  3. In the **Purchase a committed use discount** pane that appears, verify the pre-populated fields for accuracy.

If your Cloud Billing account is billed in non-USD currency, then your cost and savings estimates are displayed in both USD and your billing currency.

  4. Review the information about eligible resource types, monthly fees, and and [service specific terms](https://cloud.google.com/terms/service-terms).

  5. To complete the purchase of your recommended commitment, click **Purchase**.




[Learn more about spend-based commitments, including Compute flexible commitments](https://docs.cloud.google.com/docs/cuds-spend-based).

###  Resource-based 

  1. While viewing your commitment recommendations, click the recommendation that you want to purchase.

  2. Click **Review and purchase** at the bottom of the page.

You are redirected to the Compute Engine section of the Google Cloud console, where you can complete your purchase by using the **Purchase a commitment** page.

  3. If prompted, select a project. This is the project where your recommended resource-based commitment is purchased. Make sure that you meet the following requirements:

     * You enabled the Compute Engine API in the selected project.
     * You have sufficient permissions on the project to purchase resource-based commitments.
     * You have sufficient [quota for the commitments and the committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota_requirements).
  4. On the **Purchase a commitment** page, verify that the prefilled values for the commitment properties are accurate:

     * **Software license commitments** : By default, Compute Engine preselects the latest available version of the license. If you need a different matching license, then you must manually update the selection.

For example, consider a commitment recommendation for SLES licenses that cover 1-2 vCPUs. For this recommendation, Compute Engine preselects **SLES 15 for SAP** as the license option. If you instead want to purchase the commitment for **SLES 12 for SAP** , then you must manually update the selection.

     * **Hardware commitments** : Verify the resource types and numbers.

  5. If your CUD recommendation includes GPU or Local SSD disk usage, then carefully review the following requirements:

     * **Commitments for GPUs** : When you purchase a resource-based commitment for any GPU type, you must reserve those GPUs and attach the reservations to your commitment.

     * **Commitments for Local SSD disks** : For most machine series (and their corresponding commitment types), when you purchase resource-based commitments for Local SSD disks, you must reserve those disks and attach the reservations to your commitment.

       * This requirement doesn't apply to local Titanium SSD disks for use with C4, C4A, C4D, G4, H4D, or Z3 series. For commitment types in these machine series, you don't need to attach reservations for your committed disks. If your recommended commitment is for one of these commitment types, then Compute Engine pre-selects that commitment type for you.

       * However, this requirement applies to Local SSD disks for use with all other machine series. For commitment types in these machine series, you must reserve your committed disks and attach the reservations to your commitment. If your recommended commitment is for one of these commitment types, then Compute Engine pre-selects **General-purpose N1** as the commitment type. You can update the commitment type as necessary.

     * **Manually attach reservations** : When you purchase commitments for GPUs or Local SSD disks from a recommendation, attached reservations for these commitments are not prefilled. You must manually attach new or existing reservations to your commitment. For detailed steps, see [Attach reservations to your commitment](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

  6. In the **Summary** pane, review your commitment details and any potential quota limitations.

**Note:** The monthly estimate of the **Committed use discount** value that you see in this section might be different from the **Estimated savings** that is projected by your recommendation. The savings value in your recommendation is calculated by using your actual usage patterns, whereas the value in the commitment purchase summary is based on the [list prices](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) and assumes a 100% resource utilization rate.

  7. Review the **Disclosures** section that contains information about fees, discount eligibility, and terms and conditions.

  8. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

  9. To complete the purchase of your recommended commitment, click **Purchase**.




[Learn more about resource-based commitments for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

## Dismiss recommendations

To no longer see a particular recommendation, you can **dismiss** it. This prevents all users from seeing the recommendation in Cloud Billing FinOps hub or Active Assist pages.

To dismiss recommendations for your Cloud Billing account, follow these steps:

  1. In the Google Cloud console, open the **FinOps hub** for your Cloud Billing account.

[Go to FinOps hub](https://console.cloud.google.com/billing/optimize)

  2. At the bottom of the **Potential savings/month** section, click **View all recommendations**.

  3. In the list of recommendations, click more_vert**Actions** , then select **Dismiss**.




## Configure your default CUD recommendation settings

To customize the CUD recommendations that you get, configure your recommendation settings using the following steps. Your configuration settings are applied within one business day.

  1. Go to the [**Committed use discounts (CUDs)**](https://console.cloud.google.com/billing/reports/commitments) page in the Billing section of the Google Cloud console.

  2. In the action bar, click settings**CUD settings**. The **CUD settings** page appears.

  3. In the **Get customized CUD recommendations to maximize your savings** section, enter your preferred coverage threshold as a percentage.

  4. Select your preferred commitment term duration(s).

  5. Click **Save**.




To view your recommendations, visit the [**FinOps hub page**](https://console.cloud.google.com/billing/optimize).

## Related topics

  * [Learn more about committed use discounts](https://docs.cloud.google.com/docs/cuds)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View the credits you are receiving in reports](https://docs.cloud.google.com/billing/docs/how-to/reports#credits)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
