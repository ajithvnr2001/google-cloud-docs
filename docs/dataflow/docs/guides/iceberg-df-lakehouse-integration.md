---
url: https://docs.cloud.google.com/dataflow/docs/guides/iceberg-df-lakehouse-integration/
title: Import data from external Iceberg catalogs to borderless Lakehouse using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:18.682746+00:00
---

# Import data from external Iceberg catalogs to borderless Lakehouse using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/iceberg-df-lakehouse-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Import data from external Iceberg catalogs to borderless Lakehouse using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Your use case might require you to connect an external Iceberg REST Catalog (IRC) table to an existing Lakehouse table. Dataflow's job builder UI lets you build a pipeline that migrates your external open source Iceberg catalog tables into Lakehouse in a low-code or no-code way. This process lets you consolidate data into a unified Lakehouse-managed Iceberg format for cross-engine analytics.

Use the following connection details to import data from external Iceberg catalogs.

After you import your table, you have the option to periodically import change data to synchronize the source table updates to the Lakehouse table. For more information, see [Migrate Apache Iceberg change data capture (CDC) data into borderless Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-cdc-df-lakehouse-integration).

## Before you begin

To import data, you need the following:

  1. Connection information for the external Iceberg REST Catalog. For example: catalog name, namespace, table name, account URI, and role to access the catalog.
  2. A Lakehouse Iceberg catalog, namespace, and [table](https://docs.cloud.google.com/biglake/docs/biglake-iceberg-tables) to import the data into.



## Support and limitations

Importing data from external Iceberg catalogs to Lakehouse using Dataflow has the following limitations:

  * This feature supports reading from externally available Iceberg providers that support IRC (Iceberg Rest Catalog) into Lakehouse. Other Iceberg catalog types aren't supported.
  * This feature supports batch and streaming pipelines.



## Import an external Iceberg catalog table

To import an external Iceberg catalog table into Lakehouse, complete the following steps:

  1. In the Google Cloud console, go to the **Lakehouse runtime catalog** page.

[Go to Lakehouse runtime catalog](https://console.cloud.google.com/biglake/metastore/catalogs)

  2. Select the catalog, namespace, and table you want to import data into.

  3. On the **Table details** page, click download**Import table** , and then select **From Apache Iceberg REST Catalog (Batch)**.

The Dataflow **Job builder** page opens.

  4. In the **Sources** section:

     1. To expand the **Iceberg table** source panel, click the arrow_rightexpander arrow.

     2. In the **Iceberg table** field, enter the identifier of the Apache Iceberg table.

     3. In the **Catalog name** field, enter the name of the catalog.

     4. In the **Filter** field, enter the Iceberg filter to use. For example, `id > 5`.

     5. Optional: To specify source table column changes, use the **Keep columns** or **Drop columns** sections.

     6. In the **Catalog type** list of the **Catalog properties** section, select the type of catalog.

     7. In the **Catalog URI** field, enter the URI of the catalog. For example, `http://localhost:8181`.

     8. In the **Warehouse name** field, enter the catalog name.

For some external Iceberg REST Catalog providers, the warehouse is abstracted, and the catalog name is provided as the warehouse name.

     9. In the **Authentication type** list, select the authentication type. For example, `OAUTH2`.

  5. Optional: In the **Transforms** section, add any transforms to the source data.

  6. In the **Sink** section:

     1. Optional: Review the **Lakehouse table** sink panel. The information in this panel, such as the Lakehouse table, catalog name, and warehouse location, is typically prepopulated.
  7. In the **Dataflow options** section, click **Run job**.




## What's next

  * Learn more in the [Introduction to Lakehouse tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/biglake/docs/about-lakehouse-iceberg-rest-catalog-tables).
  * Learn more about periodically [Migrating Apache Iceberg change data capture (CDC) data into Lakehouse](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-cdc-df-lakehouse-integration).
  * Learn about [Change data capture ingestion in Lakehouse](https://docs.cloud.google.com/lakehouse/docs/change-data-capture).
  * Learn more about how to [Create a custom job with the job builder UI](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-custom-job).
  * Read the blog post [BigLake evolved: Build open, high-performance, enterprise Iceberg-native lakehouses](https://cloud.google.com/blog/products/data-analytics/enhancing-biglake-for-iceberg-lakehouses).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
