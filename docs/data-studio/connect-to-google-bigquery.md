---
url: https://docs.cloud.google.com/data-studio/connect-to-google-bigquery/
title: Connect to Google BigQuery \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:15:22.728195+00:00
---

# Connect to Google BigQuery  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-bigquery/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

BigQuery is Google's fully managed, petabyte-scale, low-cost analytics data warehouse. The Data Studio BigQuery connector lets you access and visualize data from your BigQuery tables, views, and custom SQL queries directly within Data Studio.

## Before you begin

To access BigQuery data in Data Studio, you must provide a Google Cloud project that has an associated [Google Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

BigQuery is a paid analytics platform. You might incur query processing or storage costs when you access BigQuery data through Data Studio reports. For details on query and capacity pricing, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

### Required roles

To query BigQuery data in Data Studio, you need permission to read data and run query jobs. Grant the following IAM roles on your Google Cloud project or dataset:

  * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`): Allows reading data and metadata from tables or views.
  * **BigQuery Job User** (`roles/bigquery.jobUser`): Allows running query jobs in the billing project.



Who needs these roles depends on the data credentials mode that you choose for your data source:

  * **Owner's credentials (default):** Only the data source owner needs these roles. Report viewers can view charts without needing their own access to BigQuery.
  * **Viewer's credentials:** Every report viewer must have these roles to view data in the report.
  * **Service account credentials:** Only the service account needs these roles. To configure a service account, see [Set up a Google Cloud service account for Data Studio](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account).



* * *

## How to connect to BigQuery

Follow these steps to connect your BigQuery data to a Data Studio report:

### Steps to connect

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** and then select **Report**.
  3. The report editor opens along with the **Add data to report** panel.
  4. To create a new embedded [data source](https://docs.cloud.google.com/data-studio/data-source), select the **BigQuery** [connector](https://docs.cloud.google.com/data-studio/connector). 
     * _Alternative:_ To use an existing reusable data source, click the **My data sources** tab and select a data source of any type that you previously created or that has been shared with you.
  5. Configure access to your database by using one of the connection options.
  6. Click **Add**.



In a moment, a table that is connected to the data source appears on the report canvas.

* * *

## Connection options

A BigQuery data source can fetch data from a table or view, or from a custom SQL query.

### Connect to a BigQuery table, view, or graph

A BigQuery [table](https://docs.cloud.google.com/bigquery/docs/tables) stores data in rows and columns (_fields_). A BigQuery [view](https://docs.cloud.google.com/bigquery/docs/views) is a virtual table defined by a SQL query that runs dynamically inside the BigQuery console or by using the BigQuery API. A [BigQuery graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) lets you model relationships in your data by defining nodes and edges based on existing tables.

To connect to a table, view, or graph, specify the following connection parameters:

  * A BigQuery project
  * A dataset
  * A specific table, view, or graph. Data Studio also supports connecting to date-partitioned and multi-day tables.



#### Select a project

Projects organize your Google Cloud resources and determine where query costs are billed when your reports exceed BigQuery's free limits. You can query data in one project while billing costs to a different project. Learn more about [Google Cloud projects](https://docs.cloud.google.com/docs/overview#projects).

Choose one of the following options in the connector configuration panel:

  * **RECENT PROJECTS:** Shows projects that you opened recently in the Google Cloud console. You can also enter the project ID manually. The selected project is used for both billing and data access.
  * **MY PROJECTS:** Shows all projects that you have access to. If a project is missing from the list, type the exact project ID into the entry field.
  * **SHARED PROJECTS:** Shows projects shared across departments or organizations. You can designate different projects for data selection and billing execution.



#### Select a dataset

[Datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) organize and control access for groups of tables and views. Select a dataset from the list or search by dataset ID.

[BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data) are free sample datasets shared globally across Google. To query public data, you must choose a billing project to pay for query processing costs.

#### Connect to date-partitioned tables

Data Studio supports [BigQuery date-partitioned tables](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables) (`DATE`, `DATETIME`, or `TIMESTAMP`). When you select a table partitioned by `DATE`, `DATETIME`, or `TIMESTAMP`, you can set the partition column as the main date filter for your charts. Using partitioned tables helps your charts render more quickly while minimizing query costs.

[Learn more about connecting to BigQuery date partitioned tables](https://docs.cloud.google.com/data-studio/connect-to-bq-partitioned-tables).

#### Connect to multi-day tables (`YYYYMMDD` prefix)

BigQuery supports [querying across multiple sharded tables](https://docs.cloud.google.com/bigquery/query-reference#tablewildcardfunctions) where each table stores data for a single day and ends with `YYYYMMDD` (for example, `[prefix]_YYYYMMDD`).

When Data Studio encounters tables formatted with the `YYYYMMDD` suffix during table selection, it groups the daily tables under clean prefix names (`[prefix]_YYYYMMDD`). When you create a chart from a multi-day table, Data Studio automatically queries only the last 28 days of data. You can change this date window anytime by editing the **Date Range** properties in the chart **Setup** tab.

* * *

### Connect to BigQuery by using a custom SQL query

The **CUSTOM QUERY** option lets you connect to your data by writing SQL. Custom query syntax follows the [Standard SQL dialect](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql). To use the legacy SQL syntax, select **Use Legacy SQL**.

We recommend composing and testing your query directly inside the [BigQuery console](https://console.cloud.google.com/bigquery) first, then copying and pasting the verified SQL script into the Data Studio custom query editor box.

#### Override the billing project

The **Billing Project** setting lets you specify which Google Cloud project pays for custom query execution costs. If your organization operates across many projects, you can manually enter the billing project ID in the field.

To query data inside one project while billing another, specify the billing project in this field and explicitly reference the data project inside the `FROM` clause of your query (`FROM project_id.dataset_id.table_id`).

![Example of a BigQuery custom query configuration, with the billing project set to Looker Studio Project, while the query specifies a BigQuery public data set in the querys FROM clause.](https://docs.cloud.google.com/static/data-studio/images/bq-billing-custom.png)

#### Use query parameters

Parameters let you build more responsive, customizable reports. You can pass parameters in a BigQuery data source back to the underlying query. To use a parameter in your custom query, follow the syntax guidelines for [running parameterized queries](https://cloud.google.com/bigquery/docs/parameterized-queries) in BigQuery.

For complete setup instructions, parameter syntax rules, and row-level security configuration by using parameters (`@DS_START_DATE`, `@DS_END_DATE`, `@DS_USER_EMAIL`), see [Use parameters in a custom query](https://docs.cloud.google.com/data-studio/use-parameters-in-a-custom-query).

* * *

## Notes and tips

Following are some notes and tips to help you get the most from your BigQuery data sources.

### New to Data Studio?

To learn more about core reporting capabilities in Data Studio, try the following resources:

**Get to know Data Studio**

  * Use the [toolbar](https://docs.cloud.google.com/data-studio/toolbar) to add charts, date ranges, and filters to your report canvas.
  * Use the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel) to customize fields and styling for your charts.
  * Check out the [quick start guide](https://docs.cloud.google.com/data-studio/quick-start-guide).
  * Take the [Create a report tutorial](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).



### BigQuery integrations

Some Google products and external tools export data directly into BigQuery tables. When you connect Data Studio to BigQuery, Data Studio automatically calculates standard metrics and formats field names:

  * **Explore BigQuery data in Data Studio:** Data analysts can explore BigQuery data by using Data Studio directly from within the BigQuery console. Run your query or select a table, and then select **Explore in Data Studio** to visualize the data in an interactive report. For more information, see [Analyze data with Data Studio](https://cloud.google.com/bigquery/docs/visualize-data-studio).
  * **Google Analytics BigQuery export:** When Data Studio encounters a table that is generated by [Google Analytics BigQuery Export](https://help.google.com/analytics/topic/3416089?ref_topic=2430414), the table displays a Google Analytics icon next to it. When you connect a table, Data Studio automatically creates many of the standard metrics that are found in Google Analytics as calculated fields.



### Record Count metric

Every BigQuery data source automatically includes a **Record Count** metric in your field list. Use `Record Count` inside charts to count records or verify the total rows returned by your query.

### Visualize BigQuery GEOGRAPHY polygons

You can display geospatial boundaries (`GEOGRAPHY` polygon spatial data) from BigQuery by using Google Maps in your report. For a step-by-step tutorial using public census tract data, see [Visualize BigQuery GEOGRAPHY polygons with Data Studio](https://docs.cloud.google.com/data-studio/visualize-bigquery-geography-polygons).

### Troubleshoot errors and review limitations

If your charts fail to load or return configuration warnings, consult the [Troubleshoot BigQuery connector errors and limitations](https://docs.cloud.google.com/data-studio/bigquery-connector-troubleshooting) guide.

* * *

## Related resources

  * [Create a data source in Data Studio](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Identity and Access Management roles and permsissions](https://docs.cloud.google.com/iam/docs/roles-overview)
  * [Google BigQuery documentation home](https://docs.cloud.google.com/bigquery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
