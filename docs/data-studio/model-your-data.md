---
url: https://docs.cloud.google.com/data-studio/model-your-data/
title: Model your data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:20.663920+00:00
---

# Model your data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/model-your-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Model your data Stay organized with collections  Save and categorize content based on your preferences. 

Data modeling helps you shape your data in Data Studio to create insightful and focused reports. This process involves configuring data and metadata to align with your business goals by refining how Data Studio organizes data into dimensions, metrics, and calculated fields. You can apply these modeling techniques at three distinct levels: within a report, in the data source, or directly in the underlying dataset.

Use data modeling features to adjust field properties, create calculated fields, and apply filters. These capabilities empower you to transform raw data, derive new insights, and control data access, ultimately enhancing the relevance and clarity of your Data Studio reports.

## Before you begin

To get the most from this page, you should be familiar with the following topics:

  * [How to edit a data source](https://docs.cloud.google.com/data-studio/edit-a-data-source)
  * [How to configure report components](https://docs.cloud.google.com/data-studio/properties-panel)



## How Data Studio organizes your data

Before you delve into the specifics of data modeling, it's useful to understand how Data Studio organizes your data. Every chart and table that you create in Data Studio is built from a tabular data structure that's made up of columns and rows. The columns—called _fields_ —define the data that is contained in each row. The information that defines your data is known as _metadata_.

There are two types of fields in Data Studio:

  * **Dimensions** are your categories or labels. Dimensions describe _what_ you are measuring. For example: 
    * Country
    * Product Name
    * Date
  * **Metrics** are your measurements. Metrics tell you _how much_ of something there is. For example: 
    * Sales
    * Pageviews
    * Number of Clicks



When you create a data source, you'll see dimensions and metrics that are provided by the connector that you used to connect to the underlying dataset. In addition to these default fields, you can create these other types of fields:

  * **Calculated fields** use formulas to create new metrics or dimensions that are derived from your data. For example:

    * `Price * Discount`
    * `TODAY() - 7`
    * `IF(FINAL GRADE > 35, "PASS", "FAIL")`

[Learn more about calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields).

  * **Parameters** and **variables** let you personalize your reports based on user input. [Learn more about parameters](https://docs.cloud.google.com/data-studio/parameters).




Together, these fields—dimensions, metrics, calculated fields, parameters and variables—are the building blocks of your reports. Data modeling lets you fine tune these building blocks to help you build insightful Data Studio reports.

## Where you can model your data

There are three levels at which you can model your data:

  * In the report
  * In the data source
  * In the underlying dataset

You can think of these modeling levels like an upside-down pyramid. You can mix and match these levels. Where you model your data depends on what you need.




![Data modeling levels represented as an upside-down pyramid: Report at the top, Data Source in the middle, and Dataset at the bottom. A downward pointing arrow indicates greater control when modeling at the data source level. An upward pointing arrow indicates greater flexibility at the report level.](https://docs.cloud.google.com/static/data-studio/images/modeling-layer-pyramid-arrows-reverse-2.png)

Modeling data at the dataset level occurs outside of Data Studio. Here, the focus shifts from balancing flexibility versus control to ensuring that your data and metadata are precisely as you intend _before_ they even reach Data Studio.

The following sections explain these modeling levels in more detail.

### Report-level modeling

Modeling data at the report level offers the most flexibility to report editors to modify and explore data as they see fit, much like playing freely with the building blocks.

When modeling data at the report level, keep the following points in mind:

  * Modeling features applied while editing a report reside exclusively within that report, so different reports may show different insights even if they use the same data source.
  * Report-level modeling provides the least degree of control over your data. Report editors can see and edit fields from embedded data sources.
  * Report viewers are able to see certain modeling configurations. See data modeling and data access for more details.



### Data source-level modeling

Modeling data at the data source level lets you exert more control over the data. You can restrict who can edit the data source and prevent modifications to fields within the report. Data source-level modeling helps ensure that all your reports are based on a single source of truth.

When modeling data at the data source level, keep the following points in mind:

  * Modeling features that are applied while editing a data source reside within that data source.
  * Data source-level modeling makes the model available to every chart and report that uses it.
  * Some data modeling features are available only at the data source level. For example, you can add field descriptions only in the data source. Conversely, except for reports that use the [Looker connector](https://docs.cloud.google.com/data-studio/connect-to-looker), you can apply filters only at the report level.
  * Report viewers are able to see certain data source-level modeling configurations. For more details, see data modeling and data access.



### Model data in the underlying dataset

Modeling data in the underlying dataset ensures that every connected data source receives the precise data it needs. This approach is often preferred when preparing data _before_ it reaches Data Studio.

For example, writing a SQL query directly in the BigQuery connector can be more efficient and effective than using Data Studio functions or filters for complex data transformations.

Dataset-level modeling provides the highest degree of security for your data. Data source editors cannot access the underlying dataset unless they have been explicitly granted direct permissions.

## How to model your data

You can model your data by using the following features:

  * Adjusting field properties, such as name, data type, or aggregation
  * Creating calculated fields that extend or transform the base data
  * Applying filters to the data to include or exclude certain values



### Adjust field properties

Fields in your data source have a default set of properties that are provided by the connector that's used to create that data source, as shown in the following table.

#### See the field properties that you can edit

**Property** | **Description**  
---|---  
Field name  | The field name appears as the **Field** column in the data source and as the **Display name** in the field chip in the report properties panel.   
Data type  | The data type appears as the **Type** column in the data source and as the **Data type** in the field chip in the report properties panel.  The data type property tells Data Studio what kind of data to expect when processing the field. Data type determines how the data appears in your reports along with which operations are allowed for it and which are not. For example, you can't apply an arithmetic function to a **Text** field or use a **Number** field as the date range dimension in a report.  [Learn more about data types](https://docs.cloud.google.com/data-studio/data-types).   
Aggregation  | Aggregation appears as the **Default Aggregation** column in the data source and as **Aggregation** column in the field chip in the report properties panel.  Aggregation summarizes a field's data. Three default methods are available, depending on the data's source and how it's defined in the dataset:

  1. **None** is the default aggregation for all dimensions that contain non-numeric data. Fields with an aggregation of **None** are treated as dimensions in Data Studio. You can create metrics from dimensions by applying an aggregation function in a calculated field. For example, `COUNT(Customer Name)` returns the number of non-unique customers in your data. You can't, however, apply math functions to non-numeric dimensions: for example, `SUM(Customer Name)` returns an error. 
  2. **Sum** is the default way to combine raw numbers for dimensions. It applies to number columns in data tables like Google Sheets, CSV files, and BigQuery tables. Fields set to **Sum** can be used as either dimensions or metrics in Data Studio.
  3. **Auto** is applied to metrics that come from the dataset, the connector, or a calculated field. _Auto means that the field's aggregation method is fixed and can't be changed._ Fields that are set to **Auto** are always metrics in Data Studio.

  
Description  | The **Description** column in the data source lets you add annotations to individual fields. You can't change a field description at the report level.  Some connectors, such as [Looker](https://docs.cloud.google.com/data-studio/connect-to-looker) and [Search Ads 360](https://docs.cloud.google.com/data-studio/connect-to-search-ads-360-deprecated), provide field descriptions automatically.  To display field descriptions in [table charts](https://docs.cloud.google.com/data-studio/table-reference), enable the **Show field descriptions** style option in the table's properties. **Show field descriptions** is automatically enabled for charts that are connected to a [Looker](https://docs.cloud.google.com/data-studio/connect-to-looker) or [Search Ads 360](https://docs.cloud.google.com/data-studio/connect-to-search-ads-360-deprecated) data source.   
Display format  | The **Display format** property lets you change how a number or date field is displayed in a chart. **Display format** appears only in the field chip in the report properties panel.   
Comparison calculation  | The **Comparison calculation** property lets you compare each row of data to the overall total for that field. **Comparison calculation** appears only in the field chip in the report properties panel.  [Learn more about comparison calculations](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals).   
Running calculations  | The **Running calculation** property lets you compute cumulative results for your data. **Running calculation** appears only in the field chip in the report properties panel.  [Learn more about running calculations](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals#apply_running_calculations).   
  
To change field properties at the data source level, [edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).

**Caution:** Changing field properties at the data source level affects every chart, in every report, that uses the changed field.

To change field properties at the report level, follow these steps:

  1. [Edit the report](https://docs.cloud.google.com/data-studio/edit-a-report) and then select a chart.
  2. In the chart properties panel, hover over the field's data type icon. The data type icon changes to the edit pencil icon.
  3. Click the edit pencil edit.
  4. In the dialog that appears, edit the field properties.

**Note:** Changing field properties in a chart affects only that chart. Other instances of that field in other charts or reports are not affected.

To prevent report editors from changing field properties, edit the data source and turn off **Field editing in reports**. Learn more [about editing fields](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

## Model data with calculated fields

Calculated fields let you create new fields that are derived from your data. Calculated fields appear in the field list with an **fx** symbol.

Calculated fields that you create in the data source are available to all reports that use that data source. Calculated fields that you create in a chart in the report are available only in that chart.

Learn more [about calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields).

## Apply filters

You can limit the data in a report by applying a filter to narrow down the information that's shown to viewers. Filters help you focus on the most important data, making your reports more relevant to your audience.

You can apply filters to a single component, a group of components, a whole page, or the entire report.

Learn more [about filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties).

## Data modeling and data access

A report's metadata includes the display settings of report-level modeling features, such as filter configuration, or the names of calculated fields that are created from the property panel. Report metadata is visible to anyone with view access to the report who examines the report's network requests or makes a copy of the report.

Only data source editors can see the display settings of data source-level modeling features, such as field descriptions, or the names of calculated fields that are created within the data source. However, some aspects of the data source model, like the connector type and column names of the data source schema, are always accessible to users.

**Important:** Report viewers **cannot** access additional data by editing the model configuration. Viewers can access the model, but **can't use a manipulated model to fetch new data**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
