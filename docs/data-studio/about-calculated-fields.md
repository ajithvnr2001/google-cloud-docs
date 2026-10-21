---
url: https://docs.cloud.google.com/data-studio/about-calculated-fields/
title: About calculated fields \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:28.918628+00:00
---

# About calculated fields  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/about-calculated-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  About calculated fields Stay organized with collections  Save and categorize content based on your preferences. 

Calculated fields let you create new metrics and dimensions that are derived from your data. Calculated fields let you extend and transform the information that flows from your data sources and see the results in reports.

## Watch a video

## How calculated fields work

A calculated field is a formula that performs some action on one or more other fields in your data source. Calculated fields can perform arithmetic and math; manipulate text, date, and geographical information; and use branching logic to evaluate your data and return different results. You can also create custom groups with the [**custom group**](https://docs.cloud.google.com/data-studio/create-a-custom-group) calculated field type, or custom bins with the [**custom bin**](https://docs.cloud.google.com/data-studio/create-a-custom-bin) calculated field type. The output of a calculated field can then be displayed for every row of data in charts that include that field. How this new data is displayed depends on how it's used.

For example, say you create a calculated field called **Total** that multiplies a unit price field (**Price**) by a quantity sold field (**Qty Sold**):

![The Add a field panel displays the formula sum\(Price\) * sum\(Qty Sold\) for a calculated field called Total.](https://docs.cloud.google.com/static/data-studio/images/calc-field-example-2018-09-25-rge.png)

When used in a table, the calculated **Total** field shows the product of that multiplication for each row.

![A table chart displays columns for SKU, Item, Price, and Qty Sold, along with the Total calculated field, which multiplies the Price value by the Qty Sold for each row.](https://docs.cloud.google.com/static/data-studio/images/use-calc-field-table-2018-09-26.png)

When used in scorecard, the **Total** field displays the sum of the products for all rows in which quantity is multiplied by price.

![The Total calculated field metric in a Scorecard chart displays the value 15,488.22 with the field name, Total, in superscript.](https://docs.cloud.google.com/static/data-studio/images/use-calc-field-scorecard-2018-09-26.png)

## Data source versus chart-specific calculated fields

There are two kinds of calculated fields, which are determined by where you create them: in the data source, or in specific charts in a report. Each kind of calculated field offers certain advantages over the other.

### Calculated fields in data sources

When you create a calculated field in a data source, the following actions are available:

  * The calculated field is available in any report that uses that data source.
  * You can use a data source calculated field in charts, controls, and other calculated fields, just like a regular field.
  * You can filter on a data source calculated field, just like a regular field. For example, you could set a filter property to include only items with a combined value of $500 or more:



![A calculated field called  Item Filter with the logic Greater than or equal to 500 is selected as the Filter Control Filter.](https://docs.cloud.google.com/static/data-studio/images/use-calc-field-filter-2018-09-26.png)

#### Limits of data source calculated fields

Calculated fields in data sources have the following limitations:

  * You can't use a data source calculated field with blended data.
  * You must have edit rights to the data source to create or edit calculated fields there.
  * You cannot apply [custom value formatting](https://docs.cloud.google.com/data-studio/format-fields-in-reports) when you create or edit a calculated field in a data source.



You can apply custom value formatting to a data source calculated field in the **Setup** tab of a chart's **Properties** panel.

### Chart-specific calculated fields

You can add calculated fields directly to a chart in your report. These chart-specific (also known as "chart level") calculated fields can do math, use functions, and return results-based CASE statements, just like calculated fields in a data source.

Chart-specific calculated fields offer some advantages over data source calculated fields:

  * You can quickly add fields without needing access to the data source.
  * You can create chart-specific calculated fields that are based on blended data.
  * You can include data source calculated fields in chart-specific calculated fields.
  * You can apply [custom value formatting](https://docs.cloud.google.com/data-studio/format-fields-in-reports) to a chart-specific calculated field during the creation process.



#### Limits of chart-specific calculated fields

  * Chart-specific calculated fields only exist in the chart in which you create them. Creating a field in the chart does not also create it in the chart's data source.
  * You can't reference other chart-specific calculated fields in your formula, even if those fields are defined in the same chart. (If you need to reference other calculated fields, use a data source calculated field.)
  * To be able to create chart-specific calculated fields, you must be an editor of the report.
  * [Field Editing in Reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) must be enabled in the data source.



The following table summarizes the differences between these 2 kinds of calculated fields.

Feature  |  Data source calculated fields  |  Chart-specific calculated fields   
---|---|---  
Who can create?  |  Data source editors  |  Report editors   
Works on blended data?  |  No  |  Yes   
Include other calculated fields?  |  Yes  |  No   
Where can the field be used?  |  Any report based on the data source  |  Only the specific chart in which it was created   
  
## Data type

The data type of a calculated field depends on the functions involved in the formula:

  * Formulas that use arithmetic or aggregation functions, such as `SUM`, `COUNT`, or `MAX`, create **Number** type fields.
  * Formulas that use text functions, such as `CONCAT`, `SUBSTR`, or `LOWER`, create **Text** type fields.
  * Formulas that use date and time functions create **Number** or **Date & Time** types fields, depending on the function used.



You can change the data type of your calculated fields using the **Type** drop-down menu in the data source editor.

Learn more about [data types](https://docs.cloud.google.com/data-studio/data-types).

## Aggregation and calculated fields

Aggregation is the method by which a field's data is summarized. You can construct calculated fields that work on unaggregated, row-by-row values, or on aggregated values.

For example, suppose you have 2 unaggregated numeric dimensions, **Price** and **Quantity Sold** , with the following data:

**Order Date** |  **Item** |  **Quantity Sold** |  **Price**  
---|---|---|---  
10/2/2019  |  Pretty Bird Bird Seed  |  7  |  7.99   
10/3/2019  |  Pretty Bird Bird Seed  |  5  |  7.99   
10/8/2019  |  Pretty Bird Bird Seed  |  3  |  7.99   
10/13/2019  |  Pretty Bird Bird Seed  |  5  |  7.99   
  
To calculate the total value for these orders, you'd multiply _Price_ and _Quantity Sold_ :

`Price * Quantity Sold`

If you create this field in the data source, the result is an unaggregated numeric dimension. Using this in a chart uses the default aggregation of Sum and calculates the total per row of your data.

To create an aggregated calculated metric, include the desired aggregation functions for any of the numeric fields that make up the formula. For example, suppose you want to display your total profit margin in a scorecard. You could do so with a formula like this:

`SUM(Profit) / SUM(Revenue)`

When you explicitly specify the aggregation method, the field's default aggregation is set to `Auto`. This ensures that Data Studio aggregates the formula as intended and prevents your calculated fields from being broken if someone changes the default aggregation.

## What you can do with calculated fields

Calculated fields let you perform these tasks:

  * Do basic math with numeric fields
  * Manipulate your data with functions
  * Use branching logic
  * Create a custom group
  * Create a custom bin



### Do basic math with numeric fields

You can perform arithmetic calculations using the normal operators:

  * Addition: +
  * Subtraction: -
  * Division: /
  * Multiplication: *



You can construct a calculated field using any of these operators in combination with static numeric values and unaggregated numeric fields from your data source. Use parentheses to force calculation order.

**Examples**

`Users / New Users`

`(SUM(Price) * SUM(Quantity)) *.085`

Learn more about [operators](https://docs.cloud.google.com/data-studio/operators).

### Manipulate your data with functions

Functions let you aggregate your data in different ways, apply mathematical and statistical operations, manipulate text, and work with date and geographic information.

**Examples**

```SUM``(Quantity)` \- adds the values in the Quantity field.

```PERCENTILE``(Users per day, 50)` \-- returns the 50th percentile of all values of the Users per day field.

```ROUND``(Revenue Per User, 0)` \-- rounds the Revenue per User field to 0 places.

```SUBSTR``(Campaign, 1, 5)` \-- returns the first 5 characters of the Campaign field.

```REGEXP_EXTRACT``(Pipe delimited values, R'^([a-zA-Z_]*)(\|)')` \-- extracts the first value in a pipe delimited string.

```DATETIME_DIFF``(Start Date, End Date)` \-- calculates the number of days between Start Date and End Date.

```PARSE_DATETIME``("%d/%m/%Y %H:%M:%S", DateTimeText)` \-- create a date from a text field.

```TOCITY``(Criteria ID, "``CRITERIA_ID``")` \-- Display the associated city name from a valid Google Ads Geographical Targeting criteria ID.

[Learn more about using functions](https://docs.cloud.google.com/data-studio/use-functions-in-calculated-fields).

### Use branching logic

CASE  statements let you perform branching "if/then/else" style logic in your calculated fields. For example, the following CASE formula categorizes the specified countries into regions, while grouping unspecified ones into an "Other" category:
    
    
    CASE
        WHEN Country IN ("USA","Canada","Mexico") THEN "North America"
        WHEN Country IN ("England","France") THEN "Europe"
        ELSE "Other"
    END
    

[Learn more about  CASE ](https://docs.cloud.google.com/data-studio/case-searched).

### Create a custom group

Custom groups let you create ad hoc custom groups for dimensions without needing to develop or code `CASE` logic in calculated fields or SQL. This can be helpful when you want to assign fixed labels or category names to values that match specific conditions.

For example, a table chart called **FAA flight count by destination** displays a **Record Count** metric that is grouped by a **DestState** dimension that represents flight destinations.

![](https://docs.cloud.google.com/static/data-studio/images/custom-group-table-before.png)

The report creator wants to view and compare the data by region instead of by individual states, but there is no **Region** dimension available in the data source. The report creator can group specific states or countries into regions by creating a custom group.

The report creator adds a custom group calculated field to the chart by entering the following specifications:

![](https://docs.cloud.google.com/static/data-studio/images/custom-group-example-condition.png)

  * In the **Selected field to group by** field, the report creator selects the **DestState** field.

  * In the **New field name** field, the report creator provides a name for the new group field. It is called **Flight destination region**.

  * In the **Group name** field, the report creator inputs **Pacific Northwest** to represent the states that are grouped in the Pacific Northwest region.

  * In the **Include or Exclude** drop-down menu, the report creator selects **Include**.

  * In the **Condition** drop-down menu, the report creator selects the `In` function so that they can specify specific values for the Pacific Northwest group.

  * In the **Group values** field, the report creator inputs the state abbreviations **OR** , **WY** , **ID, MT,** and **WA.**

  * The report creator wants to see how the Pacific Northwest region compares to the rest of the country. The report creator selects the **Group remaining values as a new group** checkbox.

  * In the **Group name for remaining values** field, the report creator inputs the label **Other US regions** so that all remaining states that are not in the Pacific Northwest group are grouped together under one label.

  * The report editor clicks **Save**.




The resulting table now displays the **Record Count** metric grouped by the new **Flight destination region** dimension groups: **Pacific Northwest** and **Other US regions**.

![](https://docs.cloud.google.com/static/data-studio/images/custom-group-table-result.png)

This table lets users quickly understand how many flight destinations were located in the Pacific Northwest region (4,430,314 flights), compared to other US regions (112,334,509 flights).

[Learn more about custom groups.](https://docs.cloud.google.com/data-studio/create-a-custom-group)

### Create a custom bin

Custom bins let you create ad hoc bins, or numeric tiers, for numeric type dimensions without needing to develop or code `CASE` logic in calculated fields or SQL. The **Bin** calculated field type can be helpful when you want to quickly group values into specific integer ranges to adjust the granularity of your data.

For example, a table chart called **Film releases by year** displays a **Record Count** metric that is grouped by a **year_film** dimension that represents the year that a film was released.

![](https://docs.cloud.google.com/static/data-studio/images/custom-bin-example-1.png)

The report creator wants to view and compare the data by decade instead of by individual years, but there is no **Decade** dimension available in the data source. The report creator can group the years by decades by creating a custom bin.

The report creator adds a custom bin calculated field to the chart by entering the following specifications:

![](https://docs.cloud.google.com/static/data-studio/images/custom-bin-example-2.png)

  * In the **New field name** field, the report creator provides a name for the new group field: **Decade.**

  * In the **Selected field to bin by** field, the report creator selects the **year_film** field.

  * n the **Bin field format** field, the report creator selects the **Interval "[x,y)"** format.

  * In the **Bin type** field, the report creator selects **Equal Sized.**

  * In the **Bin Size** field, the report creator inputs **10** , for the number of years in a decade.

  * In the **Bin min value** , the report creator inputs **1920** to begin the bins at the earliest decade that a film was released in the dataset.

  * In the **Bin max value** , the report creator inputs **2020** , which end the bins at the latest decade that a film was released in the dataset.

  * To account for any extraneous data points, the report creator selects the **Bin remaining values outside the min and max as separate bins** checkbox.

  * The report editor clicks **Save**.




The resulting table now displays the **Record Count** metric grouped by the new **Decade** bin field, to display the number of films that were released each decade.

![](https://docs.cloud.google.com/static/data-studio/images/custom-bin-example-3.png)

[Learn more about custom bins.](https://docs.cloud.google.com/data-studio/create-a-custom-bin)

## Related resources

  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [Dimensions and metrics](https://docs.cloud.google.com/data-studio/model-your-data)
  * [Format fields in reports](https://docs.cloud.google.com/data-studio/format-fields-in-reports)
  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Create a custom group](https://docs.cloud.google.com/data-studio/create-a-custom-group)
  * [Create a custom bin](https://docs.cloud.google.com/data-studio/create-a-custom-bin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
