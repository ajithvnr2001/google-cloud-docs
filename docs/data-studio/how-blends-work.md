---
url: https://docs.cloud.google.com/data-studio/how-blends-work/
title: How blends work in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:09.075859+00:00
---

# How blends work in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/how-blends-work/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  How blends work in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

Blending data lets you create charts, tables, and controls that are based on multiple data sources. You can blend data from up to five data sources in Data Studio or in [Looker reports](https://docs.cloud.google.com/looker/docs/glossary#reports).

For example, you can blend data from different BigQuery tables—say customer information and order details—and visualize that information in a single Data Studio table. As another example, you can plot combined data from your Google Ads and Google Analytics accounts on a time series to see a unified view of your marketing campaign performance.

**Tip:** Blending data can be complex. To get the most from this page, you should be familiar with the following concepts:

  * [Creating and editing data sources](https://docs.cloud.google.com/data-studio/about-data-sources)
  * [Dimensions, metrics, and data modeling](https://docs.cloud.google.com/data-studio/model-your-data)



## Differences between blends and data sources

Blending data creates a resource known as a _blend_. Blends are similar to data sources, in that they provide data for charts and controls in your report. However, blends differ from data sources in some important ways:

  * Blends get their information from multiple data sources.
  * Blends are always embedded into the report in which they are created. You can't make a blend reusable across reports. However, if you copy the report, the blends are copied into the new report, so your charts will continue to work on the blended data.
  * Metrics in the underlying data source become unaggregated numeric dimensions in the blend. See the [Blending tips and advanced concepts](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts) documentation page for more information.
  * Blends have no data freshness or credentials settings of their own. Instead, these settings are inherited from the underlying data sources.



## How blends work

Database programmers use SQL join statements to blend data from different tables. In Data Studio, you can blend data without writing code. Instead, you use the blend editor to configure the join, as shown in the following screenshot:

![The Blend editor displays blend options that appear when you select table and field options.](https://docs.cloud.google.com/static/data-studio/images/blend-ui-map-2022-02-12.png)

Legend:

  1. Tables
  2. Join configuration
  3. **Join another table** button
  4. Blend name
  5. Included dimensions and metrics
  6. Add metrics, date range, and filters
  7. **Hide repeated join fields** option and **SAVE** button



### Tables

Blends are made up of _tables_. When you edit or create a blend, you'll see its tables displayed in the UI. Each table contains a set of fields that are extracted from the underlying data source. A blend can have up to five tables.

Before tables are joined, Data Studio groups and aggregates rows in each table based on the dimensions included in that table. If the dimensions that you select don't include a unique identifier for each record, identical rows are collapsed during this pre-grouping phase. This collapsing can result in a lower row count than you might get from running a SQL join query directly on the same data. To prevent rows from collapsing prematurely, add a unique identifier field (such as a primary key or unique row ID) to the dimensions list for each table in the blend.

To add data to a table, click **Add dimension** or **Add metric**.

Fields used in join conditions are shown with a link icon ![Link icon used to show fields in a join condition.](https://docs.cloud.google.com/static/data-studio/images/gmlinkgmgrey50048dp-2022-02-14.png).

### Join configuration

A _join configuration_ links pairs of tables in a blend. A join configuration consists of an _operator_ , which defines how to combine matching and non-matching records from those tables, and a _condition_ , which is a set of fields that defines how the tables are related to each other.

For example, in the following screenshot, the **Grades** table joins to the **Students** table on the `student_id` field and to the **Classes** table on the `class_id` field. Both join configurations use the left outer operator.

![The Join configuration with a Left outer Join operator selected with the Join conditions set between the fields student_id \(Grades\) and student_id \(Students\).](https://docs.cloud.google.com/static/data-studio/images/join-config-2022-02-14.png)

### Join operators

The join operator determines how the matching and non-matching rows from the tables in the blend are joined together. Data Studio supports the following join operators:

  * **Inner join** : Returns only matching rows from the left and right tables.
  * **Left outer join** : Returns matching rows from the right table, plus non-matching rows from the left tables.
  * **Right outer join** : Returns matching rows from the left tables, plus non-matching rows from the right table.
  * **Full outer join** : Returns all matching rows from the left tables or the right table.
  * **Cross join** : Returns every possible combination of rows from the left and right tables.



Learn more about join operators in the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types).

### Join conditions

A join condition is a field or fields that can be found in each table and can be used to link the records of those tables together. For example, in a blend of Google Analytics and Google Ads charts, if **Campaign Name** exists in both of the extracted tables, Data Studio can use that field to join the data.

For each table in the blend, you'll select which fields to use in the condition. Note that you don't have to use the same fields for every table, nor do the fields have to have the same names, as long as the data in each field is the same. For example, say you want to visualize customers, orders, and items in a single chart. These tables might have the following fields:

**Customers** table

  * `customer_ID`
  * `customer_name`



**Orders** table

  * `cust_id`
  * `order_number`
  * `order_total`



**Items** table

  * `order_number`
  * `SKU`



To blend these tables, you'd join the **Customers** table with the **Orders** table, using the `customer_ID` and `cust_id` fields as the join condition, and you'd join the **Orders** table with the **Items** table using `order_number` as the join condition.

**Note:** Data Studio only supports equality between the fields in the join condition. For example, you can create a join condition for Field A = Field B, but not Field A ≠ Field B, Field A > Field B, or Field A < Field B.

## Included dimensions and metrics

Any field that is used in the join conditions of the blend, plus any additional dimensions or metrics that you add to the blend, are listed in the **Included dimensions and metrics** section. These are the fields that you'll be able to use in any charts that is based on the blend.

### Hide repeated join fields

The **Hide repeated join fields** option excludes duplicated fields that are used in join conditions. To include repeated join fields, clear this option.

For example, say you are joining three tables: **Grades** , **Students** , and **Classes** , using `student_id` and `class_id` fields in the join configuration. With the **Hide repeated join fields** option selected, the blend includes only one instance of `student_id` and `class_id`.

![A blend of the grades, students, and class tables including only one student_id field and only one class_id field.](https://docs.cloud.google.com/static/data-studio/images/hide-join-fields-1-2024-07-10.png)

For the same blend configuration, with the **Hide repeated join fields** option cleared, the blend now includes multiple instances of`student_id` and `class_id`, along with the name of the table in which that field appears, for example, `class_id` (Grades), `class_id` (Classes), `student_id` (Grades), and `student_id` (Students).

![A blend of the grades, students, and class tables including multiple student_id fields and multiple class_id fields.](https://docs.cloud.google.com/static/data-studio/images/hide-join-fields-2-2024-07-10.png)

## Date ranges and filters

You can limit the data in the blend by [applying a date range or filter](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts) to one or more tables.

## Blending example

The [classes, students, and grades blending example](https://docs.cloud.google.com/data-studio/blending-example-classes-students-and-grades) demonstrates how to solve a classic data blending use case.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
