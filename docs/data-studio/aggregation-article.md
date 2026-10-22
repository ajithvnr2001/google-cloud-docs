---
url: https://docs.cloud.google.com/data-studio/aggregation-article/
title: Aggregation \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:47.969909+00:00
---

# Aggregation  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/aggregation-article/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Aggregation Stay organized with collections  Save and categorize content based on your preferences. 

You can use aggregation to reduce and summarize tabular data, making complex information easier to understand. In Data Studio, aggregation helps you visualize trends, compare performance, and make data-driven decisions in your reports and dashboards.

For example, consider the following list of numbers:

> 100, 200, 300, 400, 500

Using this example, you can state the following facts that illustrate the concept of aggregation:

Fact  |  Aggregation   
---|---  
There are 5 numbers.  |  Count   
The smallest number is 100  |  Minimum   
The largest number is 500  |  Maximum   
The average of the numbers is 300 **** |  Average   
The sum of the numbers is 1500  |  Sum   
  
There are other ways you can aggregate data, including calculating the median, count distinct, quartiles, percentiles, etc.

## Dimensions and aggregation

The previous example is based on a single set of numbers, but that's almost never what you see in the real world. In the real world, your data is typically organized into dimensions and metrics. Dimensions provide a way to categorize and group your data, while metrics measure that data.

In Data Studio, aggregation **always** takes place in the context of a set of dimensions. That set of dimensions can be:

  * Every dimension, which lets you see the raw data.
  * A subset of your dimensions, which lets you see data broken down (grouped) by the dimensions you select.
  * The empty set, which lets you see a summary of the entire dataset.



For example, here are the same five numbers presented as daily stock prices. _Date_ and _Ticker_ are dimensions, _Price_ is a metric.

**Date** |  **Ticker** |  **Price**  
---|---|---  
January 1  |  GOOG  |  100   
January 1  |  AAPL  |  200   
January 2  |  GOOG  |  300   
January 2  |  AAPL  |  400   
January 3  |  GOOG  |  500   
  
You can now use the dimensions to group the data in different ways. For example:

**By Ticker**

**Ticker** |  **Price**  
---|---  
GOOG  |  ?   
AAPL  |  ?   
  
**By Date**

**Date** |  **Price**  
---|---  
January 1  |  ?   
January 2  |  ?   
January 3  |  ?   
  
In these examples, the metric values depend on what you want to know about the data. For example, to calculate the average price for each company, apply the Average aggregation in conjunction with the _Ticker_ dimension:

**Ticker** |  **Average of Price**  
---|---  
GOOG  |  (100 + 300 + 500) / 3 = 300   
AAPL  |  (200 + 400) / 2 = 300   
  
To see how many companies had stock information on a given day, you would use the _Date_ dimension and the Count aggregation:

**Date** |  **Count of Price**  
---|---  
January 1  |  2   
January 2  |  2   
January 3  |  1   
  
Now, consider what happens when you use both the _Date_ and _Ticker_ dimensions in the stock table:

**Date** |  **Ticker** |  **AVG(Price)** |  **SUM(Price)**  
---|---|---|---  
January 1  |  GOOG  |  100  |  100   
January 1  |  AAPL  |  200  |  200   
January 2  |  GOOG  |  300  |  300   
January 2  |  AAPL  |  400  |  400   
January 3  |  GOOG  |  500  |  500   
  
When you create a group that includes all the available dimensions, the result is identical to the original data. **This is still an aggregation,** just not an interesting one, since every aggregation gives the same result. In Data Studio, if you make a table and show every dimension, you're still able to set the aggregation type but it won't do anything.

## Aggregation in Data Studio

There are several ways to apply an aggregation method to your data in Data Studio:

**In the data source.** A field's default aggregation determines how that metric is displayed in charts. See Default aggregation for more information.

**In a chart**. Report editors can override the default aggregation and apply a different one to the metric on a chart by chart basis. Learn how to [add and edit data in charts](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

**In a calculated field**. You can use specific aggregation functions within a calculated field formula to produce aggregated metrics. [See the list of functions](https://docs.cloud.google.com/data-studio/function-list).

### Default aggregation

You can apply the following default aggregations to fields in data sources.

Aggregation Method  |  Abbreviation  |  Description   
---|---|---  
Sum  |  SUM  |  The field values are added together.   
Average  |  AVG  |  The field values are averaged.   
Count  |  CT  |  Each field value is counted.   
Count Distinct  |  CTD  |  Only unique field values are counted.   
Min  |  MIN  |  The field displays the minimum value.   
Max  |  MAX  |  The field displays the maximum value.   
Auto  |  AUT  |  You can't apply this method directly. The aggregation method is supplied by the underlying data set, or as the result of a calculated field.  You can't change the Auto aggregation method.   
None  |  |  No aggregation is applied. The field is treated as a dimension, even if it contains numeric data.  **Note** This method only appears in the data source. The default aggregation for metrics in reports is Sum.   
  
#### **Change the aggregation method**

To change the field's aggregation method, edit the data source, then use the **Default aggregation** drop-down menu..

### Auto aggregation

Some data sources, such as Google Analytics and Google Ads, show Auto as the only available aggregation type for metrics. These data sets are already aggregated, reducing a potentially massive list of numbers to single values. The aggregations used can be simple, like sum or count, or more complex, like percentile. You can't change Auto aggregated metrics to a different aggregation type, since doing so would require Data Studio to have access to the raw, unaggregated data.

You'll also see Auto aggregation applied to calculated fields based on other data sources, such as Sheets. In this case, the aggregation is a direct result of using an aggregation function in the formula, such as `AVG(Price)`. Again, you can't change the Auto aggregation here, because that would conflict with the output of the AVG function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
