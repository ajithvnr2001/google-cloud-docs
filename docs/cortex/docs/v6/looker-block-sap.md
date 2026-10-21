---
url: https://docs.cloud.google.com/cortex/docs/v6/looker-block-sap/
title: Looker Block for SAP \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:23.988952+00:00
---

# Looker Block for SAP  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/looker-block-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker Block for SAP

This page describes the insights you can get from the Cortex Looker Block for SAP data with some additional information for its deployment. Using this Looker Block for SAP, you can gain faster insights into your Order to Cash, Finance, and Inventory data based on the SAP Cortex Framework.

## Available insights

The Looker block for SAP in Cortex Framework offers the following insights.

### Order to Cash

  * **Order fulfillment** : Monitor current delivery status, highlight late deliveries, and compare pending deliveries with current stock.
  * **Order snapshot** : Monitor the health of the orders including product delivery efficiency.
  * **Order details** : See line item details for orders.
  * **Sales performance** : Review the sales performance of products, divisions, sales organizations, and distribution channels.
  * **Billing and pricing** : Review price variations by customer and product.



### Finance

  * **Accounts receivable** : Analyze total receivables, overdue receivables, days outstanding, and top companies with highest receivables.
  * **Accounts payable** : Find financial information such as accounts payable, accounts payable turnover, overdue payables, accounts payable aging, and cash discount utilization.
  * **Vendor performance** : Analyze vendor performance including delivery, lead time, price variance, and purchase order status.
  * **Spend analysis** : Review Key Performance Indicators (KPIs) like total spend, active vendor count, and cleared invoices. Breakdown spend by purchase organization, purchase group, vendor country, and material type.
  * **Balance sheet** : View the balance sheet as of a selected fiscal period. Compare it to the same period last year, the previous fiscal period, or a different fiscal period. And display multiple levels of the selected hierarchy for a user-specified chart of accounts and company. Two dashboards using different table styles are included. If using this block with the SAP Finance test harness data, only company code C006 balances to zero. This is expected.

**Note:** Balance Sheet only works with [Cortex Framework 5.3](https://docs.cloud.google.com/cortex/docs/release-notes#release_53) and later.
  * **Income statement** : View the income statement for selected fiscal periods, individually or combined. Compare the timeframe to the same timeframe a year ago or the preceding fiscal timeframe, and display multiple levels of the GL Account hierarchy. Two dashboards using different table styles are included. If using this block with SAP Finance test harness data, company code C006 provides the best illustration of Income Statement.

**Note:** Income Statement only works with [Cortex Framework 5.4](https://docs.cloud.google.com/cortex/docs/release-notes#release_54) and later.



### Inventory

  * **Inventory management** : Review inventory value over time (in total and by material type). Highlight other important KPIs including:

    * Inventory Turn
    * Days of Supply
    * Obsolete Inventory Value
    * Slow Moving Inventory Value



## Repository

To access the Cortex Looker Block for SAP, visit its official GitHub repository: [**block-cortex-sap**](https://github.com/looker-open-source/block-cortex-sap). This repository contains essential views, Explores and dashboards that enable you to seamlessly integrate SAP data into your Looker environment. This repository provides a solid foundation for creating custom reports, visualizations, and dashboards tailored to your specific needs.

## Deployment

For instructions about how to deploy the Cortex Looker Block for SAP, see [Deploy Looker Blocks for Cortex Framework](https://docs.cloud.google.com/cortex/docs/looker-block-deployment). After completing these instructions, see Additional specifications for deployment in the following section.

## Additional specifications for deployment

Depending the data source, some Looker Blocks need some specifications to work properly. This section describes special settings for the Cortex Looker Block for SAP.

### Persistent Derived Tables required

The BigQuery connection used for this block must have [Persistent Derived Tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables) enabled. For more information, see [Enabling PDTs on a Connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#creating_a_temporary_dataset_for_persistent_derived_tables).

### Required user attributes

Some dashboards require several Looker [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) to work properly. User attributes provide a customized experience for each Looker user. A Looker administrator defines a user attribute and then applies a user attribute value to a user group or to individual users. For more information, see [Admin settings - User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

For this Looker Block for SAP, a Looker Admin should create the following user attributes and set the values **exactly** as follows:

**Required User Attribute Name** | **Label** | **Data Type** | **User Access** | **Hide Value** | **Default Value**  
---|---|---|---|---|---  
`locale` | `locale` | String  | View  | No  | English (`en`).   
`default_value_currency_required` | SAP default currency to display  | String  | Edit  | No  | `USD` or chosen currency like `EUR, CAD or JPY`.   
`client_id_rep` | SAP Client Id (`mandt`) for Reporting  | String  | Edit  | No  | Enter your _SAP Client ID_ or `100` if using the provided test data.   
`sap_use_demo_data` | Using sample Data `Yes` or `No` | String  | Edit  | No  | Enter `Yes` if using the provided test data. Otherwise, enter `No`.   
`sap_sql_flavor` | SAP: SQL Flavor (`ECC` or `S4`)  | String  | View  | No  | Enter `ECC` or `S4` as required for your SAP system.   
  
Each dashboard user can personalize the values of the editable user attributes by following the instructions in [Personalizing user account settings](https://docs.cloud.google.com/looker/docs/user-account).

### Language

SAP Explores filter language based on a user's [locale](https://docs.cloud.google.com/looker/docs/model-localization#assigning_users_to_a_locale) or use English as a fallback if no locale value is found. The Balance Sheet and Income Statement Explores further restrict the locale to those also found in the source tables, using English if there are no matches.

### Report Table Visualization from Marketplace

The Balance Sheet and Income Statement dashboards come in two different styles:

  1. Looker's Table Visualization with subtotals.
  2. Report Table Visualization from Looker Marketplace.



The [Report Table](https://marketplace.looker.com/marketplace/detail/viz-report_table) provides an easy-to-read table style designed especially for finance reports. A Looker Admin must install the visualization from the Marketplace to use this table style. Refer to Looker documentation for [Using Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).

### Other Considerations

For optimizing the performance and functionality of your Looker Block for SAP consider the following:

  * **BI Engine Optimization:** Some calculations perform better with [BI Engine Optimization](https://docs.cloud.google.com/bigquery/docs/bi-engine-query) enabled in BigQuery.
  * **Liquid Templating Language** : Some constants, views, Explores and dashboards use liquid templating language. For more information, see Looker's [Liquid Variable Reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) documentation.
  * **Unhide additional dimensions and measures** : Many dimensions and measures are hidden for simplicity. If you find anything valuable missing, update the field's `hidden` parameter value to **No** in the relevant views.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
