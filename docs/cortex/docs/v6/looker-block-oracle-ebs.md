---
url: https://docs.cloud.google.com/cortex/docs/v6/looker-block-oracle-ebs/
title: Looker Block for Oracle EBS \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:25.108414+00:00
---

# Looker Block for Oracle EBS  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/looker-block-oracle-ebs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker Block for Oracle EBS

This page describes the insights you can get from the Cortex Looker Block for Oracle EBS (E-Business Suite) data. Using this Looker Block for Oracle EBS, you can jumpstart your Order-to-Cash (O2C or OTC) operational reports journey on BigQuery in a rapid and cost-effective manner. Use or customize this Looker Block to:

  * Identify trends and patterns in your data.
  * Spot potential problems early on.
  * Make better decisions faster.



## Available insights

The Looker Block for Oracle EBS in Cortex Framework offers the following predefined dashboards:

  * **Order status** : Overview of order-related metrics, including order volume, a breakdown of the order flow status from booking to billing, and an analysis of order status.
  * **Sales performance** : Insights into top sales performers including items, categories, customers, business units, and order sources.
  * **Order fulfillment** : Tracks fulfillment performance over time, highlighting items with the longest average order cycle time and those experiencing fulfillment challenges.
  * **Order line details** : View details of a subset of sales orders satisfying a set of filter criteria. For example, see details of all blocked orders in a given timeframe.
  * **Billing and invoicing** : Overview of invoice volume and amounts including monthly trends. Also highlights customers with highest discounts.
  * **Accounts receivables** : Analyzes current and overdue receivables, identifying customers with highest outstanding amounts and duration of overdue payments.
  * **Invoice line details** : View details of a subset of invoices satisfying a set of filter criteria. For example, see details of all open invoices in a given timeframe.



## Repository

To access the Cortex Looker Block for Oracle EBS, visit its official GitHub repository: [**block-cortex-oracle-ebs**](https://github.com/looker-open-source/block-cortex-oracle-ebs). This repository contains essential views, Explores, and dashboards that enable you to seamlessly integrate Oracle EBS data into your Looker environment. This repository provides a solid foundation for creating custom reports, visualizations, and dashboards tailored to your specific needs.

## Deployment

For instructions about how to deploy the Cortex Looker Block for Oracle EBS, see [Deploy Looker Blocks for Cortex Framework](https://docs.cloud.google.com/cortex/docs/v6/looker-block-deployment).

After completing these instructions, see [Additional specifications for deployment](https://docs.cloud.google.com/cortex/docs/v6/looker-block-sap#additional_specifications_for_deployment) in the following section.

## Additional specifications for deployment

Depending the data source, some Looker Blocks need some specifications to work properly. This section describes special settings for the Cortex Looker Block for Oracle EBS.

### Persistent Derived Tables required

The BigQuery connection used for this block must have [Persistent Derived Tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables) enabled. For more information, see [Enabling PDTs on a Connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#creating_a_temporary_dataset_for_persistent_derived_tables).

### Required user attributes

Some dashboards require several Looker [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) to work properly. User attributes provide a customized experience for each Looker user. A Looker administrator defines a user attribute and then applies a user attribute value to a user group or to individual users. For more information, see [Admin settings - User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

For this Looker Block for Oracle EBS, a Looker Admin should create the following user attributes and set the values **exactly** as follows:

**Required User Attribute Name** | **Label** | **Data Type** | **User Access** | **Hide Value** | **Default Value**  
---|---|---|---|---|---  
`cortex_oracle_ebs_category_set_name` | Cortex Oracle EBS: Category Set Name  | String  | Edit  | No  | Primary Category Set Name used in your EBS system. If using Cortex Test data default value equals `BE_INV_ITEM_CATEGORY_SET`. For more information, see the Test data section.   
`cortex_oracle_ebs_default_language` | Cortex Oracle EBS: Default Language  | String  | Edit  | No  | `US` (or primary language code used in your EBS system). If using Cortex Test data, the available values are `US` (English) and `ES` (Spanish). For more information, see the Test data section.   
`cortex_oracle_ebs_default_currency` | Cortex Oracle EBS: Default Target Currency  | String  | Edit  | No  | `USD` or chosen currency like `EUR, CAD or JPY`.   
`cortex_oracle_ebs_use_test_data` | Cortex Oracle EBS: Use Test Data (`Yes` or `No`)  | String  | Edit  | No  | Enter `Yes` if using Cortex Framework Test data. Otherwise, enter `No`. For more information, see the Test data section.   
  
Each dashboard user can personalize the values of the editable user attributes by following the instructions in [Personalizing user account settings](https://docs.cloud.google.com/looker/docs/user-account).

### Test data

When utilizing the **optional** Test data with this block, consider the following key points:

  * **Timeframe** : The test data covers Sales Orders from January 1, 2021 to April 4, 2024 and Invoices & Payments from January 2, 2021 to March 31, 2024.
  * **Date Adjustment** : When using test data (user attribute `cortex_oracle_ebs_use_test_data` is set to `Yes`), the current date is replaced with March 31, 2024 for calculations. This ensures accurate calculations for dimensions like age of receivables.
  * **Category Set** : The only available `Category Set ID`/`Category Set Name` is `1100000425`/`BE_INV_ITEM_CATEGORY_SET`. The user attribute `cortex_oracle_ebs_category_set_name` should be set to `BE_INV_ITEM_CATEGORY_SET`.
  * **Business Unit** : Test data includes only one Business Unit named `BE1 operating unit`.
  * **Tax amount** : In Sales Invoices and Sales Invoices Daily Agg, the tax amount is 0 for all records.
  * **Intercompany** : For all records `Is_Intercompany` is set to `No`.
  * **Multiple languages and currencies** : To demonstrate different languages and currencies in the test data, during the [deployment of the Cortex Framework](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five) for Oracle EBS, include `USD` and `EUR` as currency conversion targets, and `US` and `ES` as languages. The following is a sample snippet from the `config.json` file used in a deployment:
        
        "OracleEBS": {
              "itemCategorySetIds": [1100000425],
                "currencyConversionType": "Corporate",
                "currencyConversionTargets": ["USD","EUR"],
                "languages": ["US","ES"],
                "datasets": {
                    "cdc": "CORTEX_ORACLE_EBS_CDC",
                    "reporting": "CORTEX_ORACLE_EBS_REPORTING"
                }
            }
        




### Other Considerations

For optimizing the performance and functionality of your Looker Block for Oracle EBS consider the following:

  * **BI Engine Optimization:** Some calculations perform better with [BI Engine Optimization](https://docs.cloud.google.com/bigquery/docs/bi-engine-query) enabled in BigQuery.
  * **Liquid Templating Language** : Some constants, views, Explores and dashboards use liquid templating language. For more information, see Looker's [Liquid Variable Reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) documentation.
  * **Unhide additional dimensions and measures** : Many dimensions and measures are hidden for simplicity. If you find anything valuable missing, set field's `hidden` parameter value to `No` in the relevant views.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
