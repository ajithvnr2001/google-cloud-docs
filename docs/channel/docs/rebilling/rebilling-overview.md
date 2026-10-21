---
url: https://docs.cloud.google.com/channel/docs/rebilling/rebilling-overview/
title: Rebilling overview \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:33.886202+00:00
---

# Rebilling overview  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/rebilling/rebilling-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Rebilling overview Stay organized with collections  Save and categorize content based on your preferences. 

Rebilling is a way to manage billing operations for your Google Cloud customers. The rebilling system assigns Google Cloud product costs to a customer or channel partner and applies a repricing configuration to adjust the final cost. Rebilling also lets partners export their customer data to a BigQuery dataset that they own.

Rebilling consists of two main features:

  * Repricing configurations
  * BigQuery exports



## BigQuery exports

You can export a comprehensive report of your customers' billing usage and cost data to a BigQuery dataset that you own. Since this report includes customer and channel partner costs, along with customer metadata and cost configured using Repricing configurations, you can use the exported data to improve your internal billing processes and financial analytics.

For more information about setting up data exports, see [Set up Channel Services data export to BigQuery](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery).

### Migrating to Channel Services data export

We brought improvements to the data export experience for partners originally integrated with Cloud Billing data export. Benefits of migrating include:

  1. **Expanded data coverage** : Channel Services data exports billing data for both Google Cloud and Google Workspace.
  2. **Centralized data management** : Channel Services data exports centralize billing data across parent billing accounts and product families, making it easier to manage and analyze.

  3. **Channel Services-specific columns** : Channel Services data exports contain additional columns that map to [Partner Sales Console](https://channelservices.cloud.google.com/) entities, such as resource names of customers and entitlements, or CRM IDs. This makes it easier to integrate with Channel Services APIs and your own CRM system.

  4. **Optimized queries** : Channel Services data exports use the `payer_billing_account_id` as the [clustering](https://docs.cloud.google.com/bigquery/docs/clustered-tables) column, so queries for one parent billing account are optimized to reduce the cost of querying data data.

  5. **Support for Repricing** : You can use repricing to take advantage of partner incentives by configuring pricing adjustments for your customers. You can then use the exported data to provide customer-facing invoicing or cost management interfaces, such as via a [Data Studio dashboard](https://docs.cloud.google.com/channel/docs/rebilling/create-customer-cost-dashboards).

  6. **Compatible with Cloud Billing data exports** : The [ Channel Services data export table schema](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery#table_schema) is backward compatible with [Cloud Billing Detailed data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage), so you can migrate your existing data exports.




## Repricing configurations

**Note:** Repricing is only available to Google Cloud partners. Adjustments made in repricing configuration won't change the costs shown to customers in their Google Cloud console. To share a customer's costs with them, consider [creating a Data Studio dashboard](https://docs.cloud.google.com/channel/docs/rebilling/create-customer-cost-dashboards).

Repricing configurations let you adjust the final product costs for your customers and channel partners. You can create and schedule repricing configurations through the [Partner Sales Console](https://channelservices.cloud.google.com/) . For developer integration of repricing, you can use the [Cloud Channel API](https://docs.cloud.google.com/channel/docs/reference).

The following image shows an example of a customer's overview with custom repricing configurations.

![Customers page showing the repricing configurations
tab](https://docs.cloud.google.com/static/channel/docs/images/repricing-overview.png)

While viewing the list of repricing configurations for a customer, you can click **Manage repricing** to view and modify the configurations for a specific entitlement.

You can see an example of custom configurations in the following screenshot.

![Repricing management pane with sample
configurations](https://docs.cloud.google.com/static/channel/docs/images/rebilling-management-pane.png)

[Learn how to create and manage repricing configurations](https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations).

Adjustments made in a repricing configuration can affect your own set costs or Google's published rates for a defined billing period (in months). You can also schedule configurations for a specific customer or channel partner in advance to ease your financial planning operations.

For information on setting up repricing configurations, see [Create and manage repricing configurations](https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
