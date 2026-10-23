---
url: https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source/
title: Tutorial: Create a Google Sheets data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:51.239783+00:00
---

# Tutorial: Create a Google Sheets data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Create a Google Sheets data source Stay organized with collections  Save and categorize content based on your preferences. 

A data source provides the data for a Data Studio report. In this lesson, you'll create a data source that connects to one of your own Google Sheets.

## Step 0: Prepare your data

Complete the following sections to make working with your Sheets data in Data Studio easier:

### Use a separate worksheet for Data Studio data

Spreadsheets let you store and analyze your data in a flexible format that might be difficult to model in Data Studio. We recommend creating a separate worksheet for the data you want to see in Data Studio.

**Tip:** You can automate getting data from one worksheet into another using Google Sheets functions. For example:

`='Worksheet 1'!A1` — copies the contents of cell A1 in Worksheet 1.

Sheets provides others ways of fetching data from one cell or range of cells into another, including:

  * [VLOOKUP](https://support.google.com//docs/answer/3093318)
  * [HLOOKUP](https://support.google.com//docs/answer/3093281)
  * [QUERY](https://support.google.com//docs/answer/3093331)



### Table format

  * The worksheet or range you connect to should have a simple tabular format. Each column should contain only single cells: merged cells may cause your data to appear incorrectly.
  * Cells should only contain data: you can't import graphs or images, for example.
  * The first row of the worksheet provides the field names in your data source.



### Date format

  * Dates in your Google Sheet should contain the full day, month, and year. For example, 9/22/2020 or 2020-09-22.

  * If you have time data, it should be combined with the date field. For example, 9/22/2020 11:55:30.

  * Date fields should be formatted as dates (using the **Format > Number > Date** menu option in Sheets).




Other ways of handling dates are possible, but may require more work on your part.

[Learn more about handling dates and times in Data Studio](https://docs.cloud.google.com/data-studio/dates-and-times).

### Data structure

Organizing your data in certain ways can make it easier to work with in Data Studio. For example:

**Long is better than wide.** Limit the number of dimensions by grouping data into categories, rather than having columns for each possible value. For example, if you are measuring sales of fruit from a grocery store, doing this:

Date  |  Fruit  |  Quantity Sold   
---|---|---  
2017-07-06  |  Apples  |  100   
2017-07-06  |  Oranges  |  75   
2017-07-06  |  Bananas  |  150   
2017-07-07  |  Apples  |  80   
2017-07-07  |  Oranges  |  95   
2017-07-07  |  Bananas  |  175   
  
_Long table example_

...is better than this:

Date  |  Apples  |  Oranges  |  Bananas   
---|---|---|---  
2017-07-06  |  100  |  75  |  150   
2017-07-07  |  80  |  95  |  175   
  
_Wide table example_

In the long table example, your data source only requires one dimension for the Fruit category, whereas the wide table example requires one dimension for each type of fruit. If you sold 100 varieties of fruit, you'd need 100 dimensions to measure them all using the second example. This would be impossible to display in a Data Studio chart.

Grouping your data series into dimensions also makes [filtering](https://docs.cloud.google.com/data-studio/about-filter-properties) in Data Studio easier. For example, in the long table example, it's possible to build a filter on Fruit = "Apples." In the wide table example, you can't filter by type of fruit.

**Understand your aggregations.** If your Sheet includes aggregated data, such as sums, averages, medians, etc., be careful not to mix that data with unaggregated data in Data Studio charts. If you do, the numbers in those charts might not be correct. For example, say the wide table example included a Totals row:

Date  |  Apples  |  Oranges  |  Bananas   
---|---|---|---  
2017-07-06  |  100  |  75  |  150   
2017-07-07  |  80  |  95  |  175   
**Totals** |  **180** |  **170** |  **325**  
  
_Wide table with totals_

Scorecards in Data Studio would display inflated numbers for each of the fruit dimensions (because it adds the totals to the un-aggregated metrics):

Apples  360  |  Oranges  340  |  Bananas  650   
---|---|---  
  
_Scorecard examples_

In this case, it's best to not include the totals row in the data source and instead, let Data Studio calculate the totals.

## Step 1: Connect to Google Sheets

The first step in creating a data source is to connect to your [dataset](https://docs.cloud.google.com/data-studio/dataset).

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. In the _connectors panel_ , select **Google Sheets.**
  4. Select a **Spreadsheet** and **Worksheet.**
  5. Optionally, clear **Use first row as headers**. The fields in your data source will instead use the default Sheets column labels: "A," "B," "C," etc.
  6. Optionally, clear **Include hidden and filtered cells.** These will now be excluded from the data source
  7. Optionally, specify a **range of cells**. Otherwise, the entire worksheet is used.
  8. Click **CONNECT** in the upper right. The _fields_ _panel_ appears.



## Step 2: Configure the data source

The data source configuration page contains all the dimensions (the green chips) and metrics (the blue chips) from the data set. You can fine-tune the data source by renaming or disabling fields, adding calculated fields, and changing the aggregation and data type.

Learn more about [modeling your data](https://docs.cloud.google.com/data-studio/model-your-data).

![The fields panel displays the Index, Field, Type, Default Aggregation, and Description settings for data source fields.](https://docs.cloud.google.com/static/data-studio/images/data-source-fields-panel-sheets.png)

### Add a metric

You can add a [metric](https://docs.cloud.google.com/data-studio/metric) to the data source by clicking ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) next to a dimension and selecting one of the available functions. You'll need at least one metric to chart your data in Data Studio.

![A user selects a Date field's three-dot menu on the Edit Connection panel to display the metric options Count, Count Distinct, Duplicate, and Disable that are available for that field.](https://docs.cloud.google.com/static/data-studio/images/count-field-2017-07-07.png)

## Step 3: Rename your data source

![](https://docs.cloud.google.com/static/data-studio/images/rename-datasource-2015-10-16.png)

Data Studio automatically names your data source the same as your dataset name. If you want to change that, click the name in the upper left and enter a new name.

You can also rename the data source later from the DATA SOURCES home page by clicking the context menu and selecting **Rename**.

## Step 4: Share the data source

You can let other editors add this data source to reports by sharing it with them.

### To share a data source

  1. In the upper right, click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**.

  2. Enter the email addresses or Google Groups that you want to share with.

  3. For each person or group, select the access (permissions). Permissions determine what other people can do with the data source. Your choices are as follows:

     * **Can view**. People with this permission can view but not edit the data source.

     * **Can edit**. People with this permission can both view and edit the data source.




## Step 5: Use this data source in reports

![The CREATE REPORT button on the edit connection page.](https://docs.cloud.google.com/static/data-studio/images/create-report.png)

You can now create reports that get their data from your Google Sheet:

  1. Click **CREATE REPORT** in the upper right
  2. You'll see the report editor tool, and a table appears with fields from that data source. 
     1. Use the properties panel on the right to change the data and style.
  3. In the top left, name your report by clicking _Untitled Report_.



## Related resources

  * [Google Sheets connector](https://docs.cloud.google.com/data-studio/connect-to-google-sheets)
  * [Report tutorials](https://docs.cloud.google.com/data-studio/tutorial-report-intro)
  * [Share a data source](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Copy a data source](https://docs.cloud.google.com/data-studio/copy-a-data-source)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data source credentials](https://docs.cloud.google.com/data-studio/data-credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
