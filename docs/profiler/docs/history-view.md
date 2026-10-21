---
url: https://docs.cloud.google.com/profiler/docs/history-view/
title: Viewing historical trends \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:50.905337+00:00
---

# Viewing historical trends  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/history-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Viewing historical trends

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes Cloud Profiler's history view. It is intended for developers who want to understand how a function's average resource usage changes over time.

## Before you begin

This feature displays data for the most recent 30 days. If your service is newly deployed or if it hasn't been deployed for at least 30 days, these charts might be empty or incomplete.

## Opening the history view

There are different ways you can view the history of resource usage for functions in your service.

### Viewing the history of multiple functions

To display the average usage for multiple functions, click **History** _show_chart_ :

![Display of the filter bar.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-filter-bar.png)

By default, this view displays the history for the 5 functions that have the highest average usage. You can configure this view to display, or to hide, specific functions:

![Display of the default history view.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-history-default.png)

### Viewing the history of a specific function

To view the average usage for a specific function, do one of the following:

  * In the flame graph, place your pointer on a frame that contains the function of interest, and then click **Show History** in the frame's tooltip.
  * Click **List** _list_ , identify the function of interest, select **Actions** _more_vert_ , and then select **Show History**.



## Understanding the charts

Each line in a chart displays the history of resource usage for a specific function. The charts display 30 days of data. The most recent data point on the charts is for the previous day.

The **Value type** menu lets you display the profile data as a percentage of the resource usage for all functions or as the absolute value in the metric's units. The absolute usage for a function is determined by computing the ratio of its total resource usage across all profiles in a 24-hour period to the number of profiles in that period.

The **Show up to** menu lets you configure the maximum number of functions to display. By default, this value is set to 5 functions.

The chart title indicates whether the chart displays the self usage or the total usage. The title also identifies the resource whose history data is displayed. In the previous screenshot, the chart titles indicate that `CPU time` data is shown.

The chart legend lists the names of the functions whose resource usage is displayed.

## Manipulating the chart

To highlight data for a specific function, hold the pointer over the function name in the legend.

To view detailed information about a data point, hold the pointer over the data point to activate the tooltip:

![Display of the default history view tooltip.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-history-tooltip.png)

As illustrated in the previous screenshot, the tooltip displays the following:

  * Function name
  * Function filename
  * Date
  * Absolute usage and percentage usage
  * Number of profiles used to generate the data point



## Filtering the charts

To show or hide functions, you use filters. The filters accept a regular expression as the filter value and the matches are case-sensitive. The regular expression is compared against all function names and all filenames.

To add a filter, click **Add history filter** , select an option from the list, and then enter the value for the filter.

Filter | Description  
---|---  
Show | To display functions whose name or whose filename matches a [RE2](https://github.com/google/re2/wiki/Syntax) regular expression, add this filter with the value set to the regular expression. If you add multiple `Show` filters, then they are joined with a logical `OR`.  
Hide | To hide from the display all functions whose name or whose filename matches a regular expression, add this filter with value set to the regular expression. If you add multiple `Hide` filters, then they are joined with a logical `OR`.  
**Note:** If a function matches the regular expression included in a show-filter and a hide-filter, then the function is hidden. For example, if you add `Show:sort` and `Hide:sort`, then no data is displayed.

## Troubleshooting

This section lists issues that are specific to the history view. For help with other Profiler problems, see the general [Troubleshooting](https://docs.cloud.google.com/profiler/docs/troubleshooting) section.

Behavior | Cause | Solution  
---|---|---  
One or more functions are missing some data points.  | The charts display historical data for 30 days. If data isn't available for a day, no datapoint is added to the chart, and that can result in a partially empty chart.  | Missing data isn't an error condition.   
The chart is blank and the message `No data is available for the filter selections`.  | For a newly deployed service, no historical data is available to be displayed. If filters have been applied, then it's possible that the combination of filters eliminates the display of data for all functions in the service. For example, if the filters `Show:sort` and `Hide:sort` are applied, then no data is displayed. The `Show` filter requires that only functions with `sort` in the name are displayed while the `Hide` filter forces those same functions to be hidden. | For a newly deployed service, the history view is expected to be empty. If filters have been applied, then ensure that the combination of filters doesn't eliminate all possible functions.  
  
## What's next

  * [Select the profiles to analyze](https://docs.cloud.google.com/profiler/docs/selecting-profiles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
