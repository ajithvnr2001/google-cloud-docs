---
url: https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations/
title: Create and manage repricing configurations \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:34.414505+00:00
---

# Create and manage repricing configurations  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Create and manage repricing configurations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Repricing is only available to Google Cloud partners. Adjustments made in repricing configuration won't change the costs shown to customers in their Google Cloud console. To share a customer's costs with them, consider [creating a Data Studio dashboard](https://docs.cloud.google.com/channel/docs/rebilling/create-customer-cost-dashboards).

This document explains repricing configurations and how to use them with your partner accounts.

You can use custom repricing configurations to markup or discount direct customer costs, list prices, and specific SKU groups by a set percentage. These adjustments are reflected in the final billing cost for a customer or channel partner and are included as part of [BigQuery data exports](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery).

The Repricing section of the [Partner Sales Console Customers page](https://channelservices.cloud.google.com/customers) shows active and upcoming repricing configurations for your customers' Google Cloud subscriptions.

## Rebilling Basis

Rebilling Basis is the relative price point against which repricing rule multipliers (and conditional overrides) are applied. The RESELLER_MARGIN credit is always hidden from end customers and channel partners. Other credits may be repriced or completely hidden based on the Rebilling Basis selection.

We support these possible values for Rebilling Basis:

  * **Direct Customer Cost** \- Uses the actual cost and all discounts, except Reseller Margin.

  * **List Price** \- Uses the list_price of each sku and hides all credits(including CUDs) from end customer costs.




For example, consider a Repricing Rule of `List Price -17% with an override for BigQuery: Direct Customer Cost +20%`. The resulting data in Rebilling BQ Export looks like the following:

sku | list_price | cost | customer_cost | credit.type | credit.amount | credit.customer_amount | Partner Cost (cost + SUM(credit.amount)) | End Customer Cost (customer_cost + SUM(credit.customer_amount))  
---|---|---|---|---|---|---|---|---  
Compute | 120 | 100 | 99.6 (120*.83) |  RESELLER_MARGIN COMMITTED_USAGE_DISCOUNT |  -10 -10 |  0 (margin hidden) 0 (hidden due to list price) | 80 | 99.6  
BigQuery | 120 | 100 | 120 (100*1.2) |  RESELLER_MARGIN COMMITTED_USAGE_DISCOUNT |  -10 -10 |  0 (margin hidden) -12 (DCC+20%) | 80 | 108  
**Note:** If an entitlement does not have any repricing configuration specified, then it defaults to **Direct Customer Cost + 0%** , which implies no modifications to the cost (except removal of RESELLER_MARGIN).

## View repricing configurations

To view more details about the current repricing configurations for a customer, navigate to the [**Customers** page](https://channelservices.google.com/customers) of the **Partner Sales Console** and select the customer's **Name** to view their details. Click **Repricing** then select **Manage repricing** to view the current configurations for each entitlement.

The repricing management pane has a table with the following columns:

  * **Active on** : The date an upcoming configuration becomes active, the date the current configuration became active, and the date when past configurations were active.
  * **Base rule** : The value affected by the configuration, either **Direct customer cost** or **List price**.
  * **Overrides** : Lists any overrides applied to a SKU group to activate as part of the configuration.



## Export SKU groups

If you want a general overview of the SKU groups available per platform across all of your customers, you can export CSV file from the Repricing section of the Customers page. While on the **Manage repricing** page, click **View SKU Groups** , search for the required SKU group and then click download next to the platform you want to export. The exported CSV file contains the SKU Name, SKU ID, Service Name, and Service ID for each public SKU available and private SKU used by your customers.

You can also export SKU groups using the API, with the [List SKU groups](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.skuGroups/list) and [List billable SKUs in a SKU group](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.skuGroups.billableSkus/list) endpoints.

![Export SKU groups](https://docs.cloud.google.com/static/channel/docs/images/export-sku-groups.png)

## Create repricing configurations

To create a new repricing configuration, follow these steps:

  1. In the Partner Sales Console, open the [**Customers** page](https://channelservices.cloud.google.com/customers)

  2. Select **Repricing**.

  3. Click **Manage repricing** to open the configurations pane.

  4. Click **Add repricing configuration**.

  5. Select the start date for your new configuration.

  6. Set the configuration's value:

     1. Select **List price** or **Direct customer cost** as a base rule.
     2. Select **-** for a discount, or **+** for a markup.
     3. Select the percentage (up to 100% for discounts and 1000% for markups) to apply to the final cost.
  7. Click **Save** to finish.




This new configuration affects all of your available SKUs. If you want to set discounts on a per-SKU basis, you can add overrides to your configuration.

### Add overrides to a custom rule

You can use overrides to set repricing configurations for specific SKU groups ([Learn more about SKU Groups](https://docs.cloud.google.com/channel/docs/concepts/sku-groups)). These overrides go live with the main configuration when that configuration becomes active. These overrides can be re-ordered to prioritize rules for SKUs that may appear in multiple groups. These override rules are evaluated top-down approach ([Examples](https://docs.cloud.google.com/channel/docs/rebilling/repricing-configurations-example)). You can add overrides when creating a new rule or when modifying an existing rule.

**Note:** SKUs could be in multiple SKU groups. Overlapping configurations on the same sku on lower ranked sku group will be ignored. [See examples](https://docs.cloud.google.com/channel/docs/rebilling/repricing-configurations-example) to understand more.

To set an override while viewing a configuration's details, follow these steps:

  1. Click **Add override rule**.
  2. Select a SKU group to apply the override to.
  3. Set the override's value: 
     1. Select **List price** or **Direct customer cost** as a base rule.
     2. Select **-** for a discount, or **+** for a markup.
     3. Select the percentage (up to 100% for discounts and 1000% for markups) to apply to the final cost.
  4. Click **Save** to finish.



You can use drag_indicator or expand_more/expand_less

to change the ordering of overrides. You can only add _10 override rules_ for any given repricing configuration.

## Modify and update configurations

You can update active configurations for a customer or channel partner _up to 10 times_ for any given invoice month. Creating too many mid-month updates might cause unpredictable billing results for the ongoing month for customers, so we recommend updating configurations mid-month only when absolutely necessary.

Updates to pricing configurations might take up to 24 hours to take effect.

**Note:** If you edit an active configuration in the middle of an invoice month then you might have to manually adjust the invoices for that month, to account for different billing rules applied at different times in the month.

To update a configuration from the **Manage repricing** pane, follow these steps:

  1. Click edit next to the rule you want to modify.
  2. A dialog is displayed showing the rule you're about to edit along with important notes about that configuration. Click **Continue**.
  3. Make any changes to your base rule, edit existing overrides, add new overrides, or remove existing overrides.
  4. Click **Save** to finish your updates.



## Delete configurations

You can only remove configurations before their selected invoice month begins.

To remove a custom rule, click delete next to the rule you want to remove.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
