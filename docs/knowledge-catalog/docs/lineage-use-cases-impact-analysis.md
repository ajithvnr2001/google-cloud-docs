---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-impact-analysis/
title: Analyze the impact of data changes on workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:29.952788+00:00
---

# Analyze the impact of data changes on workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-impact-analysis/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Analyze the impact of data changes on workflows Stay organized with collections  Save and categorize content based on your preferences. 

In this scenario, you maintain a database that stores records about how various services provided by a healthcare provider are used. To make the data easier to use, you browse the tables to identify potential changes. Before you implement the changes, you identify if any improvements affect existing workflows and if additional adjustments are necessary.

In this tutorial, use data lineage to identify how data transformations affect downstream resources and the workflows the resources are part of.

## Get started

To complete the use case, first set up the environment and run the data transformations. Use the [prerequisites and setup](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-prerequisites) page to connect a remote repository to Dataform. This repository contains the code necessary to set up the dataset and transform the data.

After you finish the environment setup, use BigQuery and **Lineage Explorer** to track data transformations and the effect they have on the workflows.

## Analyze data transformations with Lineage Explorer

After you prepare the dataset, analyze the impact of the data transformation using the BigQuery **Lineage** tab.

### Verify column data integrity with lineage graphs

In this example, examine the `medicare_participation_indicator` column that indicates whether a physician or supplier agrees to provide services for Medicare. The lineage graph shows how data transformations between the derived tables result in column data type changes:

  1. In Google Cloud console, go to the **BigQuery** page.
  2. Use the search field to find the `physicians_and_other_supplier_2012_original` table.
  3. Click the **Lineage** tab.
  4. In the **Lineage Explorer** pane, do the following: 
     1. In the **Column Level Lineage** section, select the `medicare_participation_indicator` column name from the list.
     2. In the **Direction** section, select the **Downstream** direction.
     3. Click **Apply**.
  5. Expand the lineage path until you reach `vertex_ai_model_final_features`.
  6. Analyze the path changes between the `supplier_stg3` table and the `supplier_transform1` table:

![Lineage tracking for medicare_participation_indicator column.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage-impact-analysis.png)Lineage tracking visualization for `medicare_participation_indicator` column
     * **Exact Copy** path marking indicates that the column is passing through unchanged.
     * **Other** path marking indicates a transformation. In this path, the data type `String` is treated like `Boolean`.



The path shows that the column data types change, which might require adjustments in the workflows that use these tables.

### Identify redundant downstream columns

This example examines the `nppes_credentials` column that lists National Provider Identifiers the practitioners hold in the National Plan and Provider Enumeration System (NPPES):

  1. In Google Cloud console, go to the **BigQuery** page.
  2. Use the search field to find the `physicians_and_other_supplier_2012_original` table.
  3. Click the **Lineage** tab.
  4. In the **Lineage Explorer** pane, do the following: 
     1. In the **Column Level Lineage** section, select the `nppes_credentials` column name from the list.
     2. In the **Direction** section, select the **Downstream** direction.
     3. Click **Apply**.
  5. Expand the path to check if downstream lineage exists leading to `vertex_ai_model_final_features`.



No lineage means that this column might not be relevant in this particular workflow, and can even be deleted.

For more information about visualizing data with data lineage graph, [see the lineage graph view](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-graph-view).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
