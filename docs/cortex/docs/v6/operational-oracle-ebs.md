---
url: https://docs.cloud.google.com/cortex/docs/v6/operational-oracle-ebs/
title: Integration with Oracle EBS \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:10.373110+00:00
---

# Integration with Oracle EBS  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/operational-oracle-ebs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Oracle EBS

The Oracle EBS (E-Business Suite) integration supports Order to Cash data models with data ingestion using [Incorta](https://www.incorta.com/). Incorta uses a hosted or private instance to ingest the data from Oracle into a BigQuery CDC dataset and handles the CDC processing. From there, Cortex Framework transforms and materializes the CDC data into reporting assets using Managed Service for Apache Airflow to orchestrate BigQuery jobs.

The following diagram describes how Oracle EBS data is available through the Oracle EBS operational workload:

![Oracle EBS data source](https://docs.cloud.google.com/cortex/docs/images/oracle-ebs-overview.png)

**Figure 1**. Cortex Framework-Oracle EBS-Incorta Integration Overview .**Note:** For accessing configuration files, analytical views and models for operational data sources, see the [Cortex Framework Data Foundation repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Deployment configuration

The following table shares the parameters for configuring the Oracle EBS workload: The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to transfer data from any data source, including Oracle EBS. This file contains the following parameters for Oracle EBS:

Parameter | Meaning | Default value | Description | Matching Oracle source field  
---|---|---|---|---  
`OracleEBS.itemCategorySetIDs` | Item category sets | `[1100000425]` | List of sets to use for categorizing items. | `MTL_ITEM_CATEGORIES.CATEGORY_SET_ID`  
`OracleEBS.currencyConversionType` | Currency conversion type | `"Corporate"` | Type of currency conversion to use in aggregate tables. | `GL_DAILY_RATES.CONVERSION_TYPE`  
`OracleEBS.currencyConversionTargets` | Currency conversion targets | `["USD"]` | List of target currencies to include in aggregate tables. | `GL_DAILY_RATES.TO_CURRENCY`  
`OracleEBS.languages` | Languages | `["US"]` | List of languages to present translations of fields like item descriptions. | `FND_LANGUAGES.LANGUAGE_CODE`  
`OracleEBS.datasets.cdc` | CDC dataset | - | CDC dataset. | -  
`OracleEBS.datasets.reporting` | Reporting dataset | `"REPORTING_OracleEBS"` | Reporting dataset. | -  
**Note:** The default values for `itemCategorySetIDs`, `currencyConversionType`, `currencyConversionTargets`, and `languages` work with the test data deployment. However for a production deployment, these values depend on your Oracle EBS instance. For help with determining appropriate values,contact your Oracle administrator.

## Data Ingestion

Reach out to an Incorta representative and refer to [Oracle EBS for Google Cortex Setup Guide](https://docs.incorta.com/latest/blueprints-oracle-ebs-google-cortex-setup-guide) for details on ingesting data from Oracle to BigQuery.

### Recommended configurations

Although Incorta supports scheduling data ingestion jobs at various intervals, for optimal performance and data freshness, we recommend scheduling Incorta data ingestion jobs to run daily. If your use case requires handling deleted data, make sure to enable those by following the instructions in the Incorta documentation, [Handling source deletes](https://docs.incortaops.com/latest/blueprints-oracle-ebs-google-cortex#handling-source-deletes).

## Reporting configurations

This section outlines the necessary reporting configurations for your environment.

### Managed Airflow Airflow connection

Create a BigQuery Airflow connection named `oracleebs_reporting_bq` that will be used by the BigQuery operator to perform reporting transforms. See more details in the [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

### Materializer settings

Find materialization settings in [`src/OracleEBS/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/OracleEBS/config/reporting_settings.yaml). By default the dimension, header, and aggregate tables are materialized daily. The reporting layer tables are also date partitioned. Partitions and clustering can be customized if needed. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings) and [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).

## Data Model

This section describes the Oracle EBS Order to Cash Logical Data Model. Each subsection explains the following Oracle EBS Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for Oracle EBS](https://docs.cloud.google.com/cortex/docs/images/erd_oracle_ebs.png)](https://docs.cloud.google.com/cortex/docs/images/erd_oracle_ebs.png)

**Figure 2**. Oracle EBS: Entity Relationship Diagram.

### Base fact views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases.

### Dimension tables

These are the purple objects in the ERD and contain the relevant dimensional attributes used by the reporting tables. By default, these dimensions are filtered down based on the deployment configuration parameter values where applicable. This integration also uses the Cortex K9 Gregorian calendar dimension for date attributes, which is deployed by default.

### Header tables

These are the green objects in the ERD and contain the joined facts and dimensions that describe business entities like orders and invoices at the header level. The header tables are partitioned by a primary event date corresponding to each entity, for example `ORDERED_DATE` or `INVOICE_DATE`.

#### Nested and repeated Lines

The `SalesOrders` and `SalesInvoices` tables contain [nested repeated fields](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-nested) named `LINES`. These fields group the various order lines and invoice lines under their associated headers. To query these nested fields, use the `UNNEST` operator to [flatten the elements into rows](https://docs.cloud.google.com/bigquery/docs/arrays) as shown in the provided sample scripts (`src/OracleEBS/src/reporting/ddls/samples/`).

**Caution:** Be careful when unnesting repeated fields to avoid double counting the top level measures.

#### Nested and repeated attributes

Some tables contain additional nested repeated fields such as `ITEM_CATEGORIES` or `ITEM_DESCRIPTIONS` where multiple values of the same attribute may apply to the entity. If unnesting these repeated attributes, be sure to filter down to a single attribute value to avoid over counting measures.

#### Applied Receivables

`SalesAppliedReceivables` is a unique table in that the entities can reference either invoices on their own, or an invoice with a cash receipt. As such there are nested (but not repeated) `INVOICE` and `CASH_RECEIPT` fields, where the `CASH_RECEIPT` field is only populated when `APPLICATION_TYPE = 'CASH'`.

### Aggregate tables

These are the red objects in the ERD and aggregate from the header tables up to daily measures. Each of these tables are also partitioned by a primary event date. The aggregate tables only contain additive measures (for example, counts, sums) and don't include measures like averages and ratios. This means that users must derive the non-additive measures to ensure they can be derived appropriately when aggregating up to a higher grain, such as monthly. See sample scripts like `src/OracleEBS/src/reporting/ddls/samples/SalesOrderAggMetrics.sql`.

#### Currency conversion Amounts

Each aggregate table uses the `CurrencyRateMD` dimension to create a nested repeated field of `AMOUNTS` containing currency measures converted into each of the target currencies specified in the deployment configuration. When using these measures, make sure to filter to a single target currency or group on target currencies for reporting to avoid over counting. This can also be seen in the sample scripts like `src/OracleEBS/src/reporting/ddls/samples/SalesOrderAggMetrics.sql`.

#### Nested line attributes and measures

The `SalesOrdersDailyAgg` table contains a nested repeated field named `LINES` to differentiate between line level attributes and measures (for example, `ITEM_CATEGORY_NAME` and `AMOUNTS`) versus header level attributes and measures (for example, `BILL_TO_CUSTOMER_NAME` and `NUM_ORDERS`). Take care to query these grains separately to avoid over counting.

Although invoices also have a notion of headers versus lines, the table `SalesInvoicesDailyAgg` only contains measures at the line level, so it doesn't follow the same structure as `SalesOrdersDailyAgg`.

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
