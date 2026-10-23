---
url: https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals/
title: Add comparison metrics and running totals \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:50.182864+00:00
---

# Add comparison metrics and running totals  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add comparison metrics and running totals Stay organized with collections  Save and categorize content based on your preferences. 

You can add comparison metrics and running calculations to your Data Studio charts to analyze data with greater depth. Comparison metrics help you evaluate how individual row values contribute to overall column totals. You can also use running calculations to track cumulative trends and changes over time.

## Add comparison metrics to a chart

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart.
  3. In the **Properties** panel, select the **SETUP** tab.
  4. Choose a metric and click the edit edit option.
  5. Click the **Comparison calculation** menu, and then select a comparison.
  6. To display the base value of the metric, change the **Comparison calculation** selection to **None**.



![The metric configuration options dialog, where you can edit the field name, change the aggregation and field type, and apply a comparison or running calculation.](https://docs.cloud.google.com/static/data-studio/images/metric-types-comparison-running-calcs-menu-2023-05-09.png)

### Compare to total

You can compare each row of data to the overall total for that field:

  * **Percent of total** shows the current row's value divided by the column total.
  * **Difference from total** shows the column total minus the current row's value.
  * **Percent difference from total** shows the column total minus the current row's value divided by the column total.



For each of these total comparisons, you can also select **Ignore canvas filters in total** to compute the total value without applying viewer-applied filters, such as [controls](https://docs.cloud.google.com/data-studio/about-controls). Total rows still include [filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties).

### Example

The following table shows the results of applying different "compare to total" options to the **Order value** field.This lets you evaluate each order's contribution to overall sales.

Item  |  Quantity sold  |  Order value  |  Percent of total  |  Difference from total  |  Percent difference from total   
---|---|---|---|---|---  
Pretty Bird Bird Seed  |  20  |  31.96  |  12.79%  |  -217.85  |  -87.21%   
Healthy Dog Dog Food  |  16  |  79.96  |  32.01%  |  -169.85  |  -67.99%   
Playful Puppy Toy  |  11  |  17.97  |  7.19%  |  -231.84  |  -92.81%   
Parrot Perch  |  8  |  74.97  |  30.01%  |  -174.84  |  -69.99%   
Happy Cat Catnip  |  4  |  14.97  |  5.99%  |  -234.84  |  -94.01%   
Hungry Kitty Cat Food  |  3  |  29.98  |  12%  |  -219.83  |  88%   
**Grand total** |  **62** |  **249.81** |  **100%** |  **0** |  **0%**  
  
### Compare to max

You can compare each row of data to the maximum value for that field:

  * **Percent of max** shows the current row's value divided by the maximum value.
  * **Difference from max** shows the current row's value minus the maximum value.
  * **Percent difference from max** shows the current row's value minus the maximum value divided by the maximum value.



### Example

The following table shows the results of applying different "compare to max" options to the **Order value** field. This lets you see how each order compares to the maximum order.

Item  |  Quantity sold  |  Order value  |  Percent of max  |  Difference from max  |  Percent difference from max   
---|---|---|---|---|---  
Pretty Bird Bird Seed  |  20  |  31.96  |  39.97%  |  -48  |  -60.03%   
Healthy Dog Dog Food  |  16  |  79.96  |  100%  |  0  |  0%   
Playful Puppy Toy  |  11  |  17.97  |  22.47%  |  -61.99  |  -77.53%   
Parrot Perch  |  8  |  74.97  |  93.76%  |  -4.99  |  -6.24%   
Happy Cat Catnip  |  4  |  14.97  |  18.72%  |  -64.99  |  -81.28%   
Hungry Kitty Cat Food  |  3  |  29.98  |  37.49%  |  -49.98  |  -62.51%   
  
### Relative comparison

When your chart includes a comparison date range, you can apply the comparison function to either the base data or to the corresponding comparison date range.

For example, consider a time series chart that compares the current 28 days to the previous 28 days. The maximum value of **Sessions** for the current period was 1,947 on June 26. The maximum value of **Sessions** for the previous period was 1,571 on June 4.

![Time series chart tooltip making two data comparisons: the first between June 26 and May 29, and the second between July 2 and June 4.](https://docs.cloud.google.com/static/data-studio/images/base-data-2019-07-10.png)

If you apply the **Percent of max** function relative to base data, then every data point for the previous period will be divided by the maximum value of the current period (1,947). For the data point on June 4, the **Percent of max** relative to base data would be: 1571/1947 = 80.69%.

![Time series chart tooltip with percent of max function applied relative to the base data displaying the percentage of max value for June 4.](https://docs.cloud.google.com/static/data-studio/images/percent-of-max-relative-to-base-2019-07-10.png)

If you instead apply the **Percent of max** function relative to corresponding data, then every data point for the previous period will be divided by the maximum value of the previous period (1,571). For the data point on June 4, the **Percent of max** relative to corresponding data would be: 1571/1571 = 100%.

![Time series chart tooltip with percent of max function applied relative to corresponding data displaying the percentage of max value for June 4.](https://docs.cloud.google.com/static/data-studio/images/percent-of-max-relative-to-corresponding-2019-07-10.png)

## Apply running calculations

Running calculations compute summary results across a collection of values. Running calculations return a value for each row of input, expressing that row's relation to the collection as a whole.

The following example shows the application of two running calculations to the **Users** metric:

  * **Running sum**
  * **Running delta**



### Example

Date  |  Source  |  Users  |  Running sum of users  |  Running delta of users   
---|---|---|---|---  
May 7, 2018  |  google  |  1,400  |  1,400  |  1,400   
May 8, 2018  |  google  |  1,856  |  3,256  |  456   
May 9, 2018  |  google  |  1,748  |  5,004  |  -108   
May 10, 2018  |  google  |  2,046  |  7,050  |  298   
May 11, 2018  |  google  |  1,497  |  8,547  |  -549   
May 12, 2018  |  google  |  1,094  |  9,641  |  -403   
  
See a [demonstration report](https://datastudio.google.com/reporting/1DA4qG1pPOqc4KwQz0QpN1rskVGaCdH5I/page/1PzS?utm_source=hc&utm_medium=link&utm_campaign=article&utm_content=demo-reports) here.

Data Studio supports the following running calculations:

  * Running sum
  * Running average
  * Running min
  * Running max
  * Running count
  * Running delta
  * Running percentage delta



### To apply a running calculation

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart.
  3. In the **Properties** panel, select the **SETUP** tab.
  4. Add a metric to chart, and then click the edit edit option.
  5. Click the **Running calculation** menu, and select a function.
  6. To remove a running calculation, change the **Running calculation** option to **None**.



> To display the original metric and the metric comparison or running calculation in the same chart, add a second instance of the original metric by dragging it from the **Available Fields** panel. (You can't add a duplicate field using the metric or dimension picker.)

## Differences between running calculations and calculated fields

Calculated fields work on the data in your charts on a row-by-row basis. Running calculations work across rows, enabling you to show complex data relationships without having to code custom SQL queries in your dataset. Such queries would be difficult if not impossible to replicate in a calculated field in your data source.

However, unlike with calculated fields, you can't edit the formulas of running calculations.

## Limitations of comparison metrics

The **[Group others](https://docs.cloud.google.com/data-studio/table-reference#number_of_rows)** option is not compatible with comparison metrics. To use comparison metrics on a chart, disable the **Group others** option.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
