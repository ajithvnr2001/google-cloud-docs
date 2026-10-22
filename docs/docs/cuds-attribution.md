---
url: https://docs.cloud.google.com/docs/cuds-attribution/
title: Attribution of committed use discount fees and credits \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:35.195134+00:00
---

# Attribution of committed use discount fees and credits  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-attribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Attribution of committed use discount fees and credits Stay organized with collections  Save and categorize content based on your preferences. 

[Committed use discounts](https://docs.cloud.google.com/docs/cuds) (CUDs) provide a discount in exchange for your commitment to [spend a minimum amount](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) or [use a minimum level of resources](https://docs.cloud.google.com/docs/cuds#resource_based_commitments) for a product for a specified term.

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

Attribution refers to how resource benefits shared at the Cloud Billing account level are divided among [account-level resources](https://docs.cloud.google.com/billing/docs/concepts#gcp_resource_hierarchy_overview), such as projects. Attribution for a subscription, such as your committed use discount subscription, determines how fees and credits are applied to your Cloud Billing account and spread across the account's projects that are eligible to consume them. This is reflected in how the fees and credits appear in Cloud Billing cost management interfaces, such as the usage cost export or the Google Cloud console.

## Types of commitment attribution

Attribution impacts how your committed use discount fees and credits are applied to the projects in your Cloud Billing account, which is reflected in the cost management interfaces. The following are ways in which they can be applied.

### Unattributed

When _unattributed_ , the subscription fees and credits are applied to your Cloud Billing account's projects, as they consume eligible usage. Any subscription fees that are not attributed to a project are charged at the Cloud Billing account level.

This type of attribution can affect the predictability of a project's adjusted costs after applying the commitment fees and credits because of the timing or order of consumption relative to other eligible projects.

### Proportional attribution

_Proportional attribution_ applies the credits and, where appropriate, the subscription fees from your _spend-based_ and _resource-based_ committed use discounts to the projects in your Cloud Billing account, directly in proportion to the amount of total eligible usage consumed by each project.

For example, if project A consumed $75 worth of usage and project B consumed $25, project A would be covered by up to 75% of available credit and project B would be covered by up to 25%.

Any subscription fees that are not attributed to a project are charged at the Cloud Billing account level.

Proportional attribution helps you understand the actual cost of a given project that is consuming the discount by clearly disclosing the following:

  * The project's portion of the total commitment fee
  * The project's SKU-based usage cost
  * The project's CUD credit



For your _resource-based_ committed use discounts to use proportional attribution, Compute Engine discount sharing must be enabled. Depending on your Cloud Billing account's creation date and active commitments, CUD sharing might be enabled by default. For details, see [Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects).

In contrast, spend-based commitments are inherently pooled at the Cloud Billing account level and always use proportional attribution. You don't have a separate CUD sharing configuration for spend-based commitments.

### Prioritized attribution

_Prioritized attribution_ applies the credits and, where appropriate, the subscription fees from your _resource-based committed use discounts_ to the projects in your Cloud Billing account based on the distribution you specify. The total amount of the allotments cannot exceed the commitment amount purchased. Any remaining unprioritized commitment credits and fees are then applied proportionally across all projects.

You can _allocate all of your purchased commitments_ across projects you specify. For example, if you purchased 60 GB of commitments, you can prioritize project A to receive 40 GB of the allotment and project B to receive 20 GB of the allotment. In this case, projects A and B fully reserve the 60 GB of eligible committed usage. Then if project A and B have fully utilized 60 GB of commitment, the other projects in your Cloud Billing account don't receive an allocation of the credits and fees, even if they have eligible usage. But if project A and B have not fully utilized the 60 GB of commitment, other projects will receive the remaining committed usage credits, if they have eligible usage.

You can also _allocate a portion of your purchased commitments_ to certain projects, allowing the remainder to be applied proportionately to the eligible usage in all projects. For example, if you purchased 60 GB of commitments, you can prioritize project A to receive 30 GB of the allotment and allow the remaining 30 GB to be applied proportionately to the eligible usage in your other projects.

You can _select multiple projects for a single prioritized allotment_. In that case, the allotment is shared proportionately between the projects based on their eligible usage.

**Preview:** You can prioritize multiple projects by grouping them in a folder. Credits are applied proportionately across projects in the folder, based on their eligible usage. To request access to prioritized attribution with folders, [complete the interest form](https://forms.gle/9wkzFCAU4pkeVmcE6).

If you don't utilize all of your purchased commitments for the period, the fees are still charged to the prioritized projects. For example, if project A is allotted 30 GB of usage but only uses 10 GB, the project still receives the fee for the full allotment of 30 GB.

You cannot prioritize more commitment resources than what you have purchased.

Prioritized attribution helps you control how your commitments impact each of your projects and their actual cost by clearly disclosing the following:

  * The project's exact portion of the total commitment fee
  * The project's SKU-based usage cost
  * The project's CUD credit



## CUD sharing for resource-based commitments

CUD sharing is a prerequisite for using proportional or prioritized attribution with resource-based commitments.

_CUD sharing_ is only available for Compute Engine resource-based commitments that were purchased for hardware resources. When CUD sharing is enabled, the CUDs from the commitment are shared across all projects in the Cloud Billing account, depending on resource consumption. CUD sharing lets all projects in the Cloud Billing account that have eligible resource usage to consume that commitment's credits and fees. Credits for resource-based CUDs are not tied to the amount spent, but rather to the amount of resources used.

**Caution:** If you have a shared reservation and you enabled CUD sharing for your commitment's Cloud Billing account, then Google recommends that you share your reservation only with projects that are linked to the commitment's Cloud Billing account. Otherwise, when projects outside the Cloud Billing account consume that shared reservation, their usage won't be eligible for this Cloud Billing account's shared CUDs.

### Default CUD sharing configuration

The default CUD scope for all new Cloud Billing accounts is **Billing account** (CUD sharing enabled). On June 16, 2026, the default CUD scope changed from **Project** to **Billing account** for most billing accounts. To prevent any disruption to your active billing configurations with this change, Google Cloud auto-configured your Cloud Billing account's CUD scope in the following way, depending on the account's creation date and the active commitments:

  * **Cloud Billing accounts created on or after June 16, 2026** : The scope is **Billing account** (CUD sharing enabled) by default.
  * **Cloud Billing accounts created before June 16, 2026** : 
    * If the Cloud Billing account had **no active resource-based commitments** on June 16, 2026, then the CUD scope was changed to **Billing account** (CUD sharing enabled) on that date.
    * If the Cloud Billing account had **any active resource-based commitments** on June 16, 2026, then Google Cloud preserved and retained the existing CUD scope (either **Project** or **Billing account**) that was in place on that date.



You can change the setting to enable or disable CUD sharing at any time. For instructions, see [Enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing) or [Disable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-off-committed-use-discount-sharing).

### CUD sharing best practice for prioritized attribution

If CUD sharing is disabled on your Cloud Billing account and you plan to use prioritized attribution, then Google recommends that you first configure the prioritized attribution settings in the Google Cloud console before you enable CUD sharing.

By configuring prioritized settings first, you maintain your existing unattributed costs up until the moment prioritized attribution takes effect. If you enable CUD sharing before you configure prioritized settings, then the credits and fees are temporarily shared proportionally across all projects in that Cloud Billing account, which can make your cost reports appear erratic.

## Choose proportional attribution for spend-based commitments

To keep your project costs predictable, starting from August 2021, the following automatically use _proportional attribution_ when you purchase spend-based commitments:

  * You have an existing Cloud Billing account that has no spend-based commitments.
  * You create a new Cloud Billing account and purchase spend-based commitments.



If your Cloud Billing account existed and you purchased spend-based commitments before or during August 2021, you can request to switch your account to proportional attribution.

#### Select proportional attribution

If you purchased spend-based commitments before or during August 2021, they might be unattributed. You can request that your Cloud Billing account switches to proportional attribution. This action affects your existing spend-based commitments. To do so, submit the requested information in [the proportional attribution opt-in form](https://forms.gle/UEsTuotQsHj5d8qj6).

**Caution:** After you enable proportional attribution for spend-based commitments, you can't disable the setting.

If you're uncertain whether or not your spend-based commitments purchased before or during August 2021 are using proportional attribution, submit the requested information in [the proportional attribution opt-in form](https://forms.gle/UEsTuotQsHj5d8qj6) to verify it is enabled.

## Choose attribution for resource-based commitments

To keep your project costs predictable for resource-based commitments, you can select _prioritized attribution_ or _proportional attribution_. Attribution works in conjunction with _Compute Engine CUD sharing_. To use attribution, CUD sharing must be enabled for your Cloud Billing account. If CUD sharing is disabled, then any attribution preferences that you configure are applied only after you enable CUD sharing. For instructions to enable CUD sharing, see [Enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).

You can update prioritized attribution anytime during the commitment's lifetime. The attribution starts applying to usage starting 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on the following day. The updated attribution setting is only applied moving forward.

To choose the attribution for your resource-based commitment, perform the following steps:

  1. Sign in to your Cloud Billing account in the Google Cloud console.

[Sign in to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to configure attribution. The Billing _Overview_ page opens for the selected Cloud Billing account.

  3. From the Billing navigation menu, select **Committed use discounts** to view the **Committed use discounts (CUDs)** page.

  4. From the **Committed use discounts (CUDs)** page, locate the _resource-based_ commitment for which you want to configure attribution.

  5. Click the **View Analysis** action menu more_vert for the _resource-based_ commitment, then click **Configure Attribution** to view the commitment summary.

  6. Choose between prioritized attribution or proportional attribution.

  7. [Enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing), if you haven't already done so.




### Select prioritized attribution

From the **Configure Attribution** page for your resource-based commitments, you can select _prioritized attribution_ with the following steps:

  1. From the commitment summary, select **Prioritized** to view your active commitments.

  2. Click add **Add Allotment**.

  3. Click **Targets 1** arrow_drop_down to select from your available projects to receive an allotment.

You can select multiple projects for a single allotment. In that case, the allotment is shared proportionately between the projects based on their eligible usage.

  4. In the **Allotment 1** field, enter the amount to be prioritized for the selected targets.

To add additional allotments, click add **Add Allotment**.

  5. Click **Save** to apply your changes.

  6. For your attribution configuration to take effect, verify that your Cloud Billing account has CUD sharing enabled. If CUD sharing is disabled, then you must [enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).




To switch to _proportional attribution_ after selecting _prioritized attribution_ for your resource-based commitments, follow the instructions at select proportional attribution.

The following image is an example of configuring _prioritized attribution_ for a resource-based commitment on the **configure attribution** page.

![Example of configuring prioritized attribution for a resource-based commitment.](https://docs.cloud.google.com/static/billing/docs/images/cud-attribution-prioritized-resource-based.png)

### Select proportional attribution

From the **Configure Attribution** page for your resource-based commitments, you can select _proportional attribution_ with the following steps:

  1. From the commitment summary, select **Proportional (default)**.

  2. Click **Save** to apply your changes.

  3. For proportional attribution settings to take effect, verify that your Cloud Billing account has CUD sharing enabled. If CUD sharing is disabled, then you must [enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).




To switch to _prioritized attribution_ after selecting _proportional attribution_ for your resource-based commitments, follow the instructions at select prioritized attribution.

## View attribution in your reports

You can view the allocation of your committed use discount fees and charges for unattributed, proportional, and prioritized attribution in your billing reports.

When you navigate to the reports page, group by **Project** , and filter by **SKU** , each project displays the subscription fees specifically attributed to it. Any remaining subscription fees that are not associated with a project are unattributed and assigned to **Charges not specific to a project**.

To view the Cloud Billing reports for your Cloud Billing account:

  1. Sign in to your Cloud Billing account in the Google Cloud console.

[Sign in to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to view reports. The Billing _Overview_ page opens for the selected Cloud Billing account.

  3. In the Billing navigation menu, select **Reports**.




For more information on viewing your billing reports, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).

## View attribution in your exported data

You can view the allocation of your committed use discount fees and charges for unattributed, proportional, and prioritized attribution in the Cloud Billing BigQuery usage cost export.

When viewing your exported data in BigQuery, each project consuming credit has a line item corresponding to its portion of the subscription fee, alongside a line item that represents the usage and credit consumed for that project.

If there is any unconsumed credit, where you didn't consume as much as you committed to, then the remaining subscription fees are assigned to **Costs not specific to a project** and not attributed to any projects. The total charges for the SKU remain the same, divided between fees that are assigned proportionally to related projects and unattributed fees that are assigned to **Costs not specific to a project**.

For more information about exporting your cost data to BigQuery, see [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## Related topics

  * [Learn about spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice)
  * [Learn more about committed use discounts](https://docs.cloud.google.com/docs/cuds)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View the credits you are receiving in reports](https://docs.cloud.google.com/billing/docs/how-to/reports#credits)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
