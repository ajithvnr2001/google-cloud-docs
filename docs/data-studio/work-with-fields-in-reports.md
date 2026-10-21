---
url: https://docs.cloud.google.com/data-studio/work-with-fields-in-reports/
title: Work with fields in reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:07:27.324219+00:00
---

# Work with fields in reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/work-with-fields-in-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Work with fields in reports Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how dimensions and metrics are handled in reports. It may be helpful to also read about [how to model your data](https://docs.cloud.google.com/data-studio/model-your-data) before or after reading this page.

In Data Studio, a [chart](https://docs.cloud.google.com/data-studio/chart) displays data from one or more fields. These fields are the dimensions and metrics provided by the data source attached to that chart. How the data appears depends on the type of chart and how you've styled it.

## How data appears in your charts

In **table charts** , the data appears in rows and columns, such as in this example based on a Google Analytics data source:

Browser  |  Sessions  |  Avg. Session Duration  |  Bounce Rate   
---|---|---|---  
Chrome  |  3,340  |  00:03:35  |  22.90%   
Safari  |  209  |  00:02:33  |  15.79%   
Firefox  |  202  |  00:02:20  |  19.80%   
Internet Explorer  |  64  |  00:02:21  |  17.19%   
Edge  |  37  |  00:05:37  |  16.22%   
...  |  |  |   
  
In **Cartesian charts** , dimensions are typically laid out along the horizontal (X) axis, while metrics values provide the vertical (Y) axis positioning. In a time series, the date range dimension provides the X axis and a breakdown dimension provides the data series.

![Two charts: A column chart with web browser types on the X axis and session count on the Y axis, and a time series chart with dates on the X axis and session counts on the Y axis.](https://docs.cloud.google.com/static/data-studio/images/bar-line-chart-example-2018-01-02.png)

In a **pie chart** , a dimension defines the number of segments, while a metric determines the size of each segment.

![](https://docs.cloud.google.com/static/data-studio/images/pie-example-gray-2017-12-18.png)

**Geo charts** use a dimension that contains geographic information (such as a country code, latitude and longitude, or Google Ads Criteria ID) to display your data on a map. The relative values of the metric determine the intensity of color on the chart, as show in this example showing that the majority of website sessions occurred in the United States:

![A geo map of the world displays web sessions per country with the United States highlighted in dark gray, and a gray gradient scale underneath from light gray to dark and a range of 1 to 51,857.](https://docs.cloud.google.com/static/data-studio/images/geo-example-gray-2017-12-18.png)

[Learn more about the charts you can use in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts).

## Use breakdown dimensions to group data

Many charts allow you to group your data by multiple dimensions. Each dimension you add to the chart groups the data into ever finer levels of detail. The first dimension in the chart is the primary; additional dimensions are called _breakdown_ _dimensions_ (because they allow you to breakdown or sub-categorize your data into smaller chunks).

For example, in the following table, the primary dimension is _Country_ , and the breakdown dimension is _Year_. The metrics in the table are aggregated first by country, then by year.

Country  |  Year  |  Population  |  Internet Users  |  Internet %   
---|---|---|---|---  
Iceland  |  2013  |  323,764  |  312,583  |  96.55%   
Iceland  |  2012  |  320,716  |  308,560  |  96.21%   
Bermuda  |  2013  |  65,001  |  61,945  |  95.30%   
Norway  |  2013  |  5,079,623  |  4,828,354  |  95.05%   
Iceland  |  2011  |  319,014  |  302,488  |  94.82%   
...  |  |  |  |   
  
Making sense of multi-dimensional data in a table can be challenging. Using other visualization types, such as this stacked bar chart, can help make sense of complex data. For example, a stacked column chart can be used to display a comparison of internet users in China, the United States, Japan, India, Brazil, Germany, Russia, the United Kingdom, France, and the Republic of Korea by year.

![](https://docs.cloud.google.com/static/data-studio/images/internet-usage-bar-chart-2016-06-09.png)

**Tip:** To see this data story told even better, check out the [World Population Sample Report](https://datastudio.google.com/c/#/org/UTgoe29uR0C3F1FBAYBSww/reporting/0B_U5RNpwhcE6bzVYT2FSNmRBUWc).

## How metrics are calculated

In Data Studio, metrics are calculated in two basic ways:

#### As overview totals

Metrics can be displayed as a summary statistic for the entire column (field) in your dataset using the [Scorecard](https://docs.cloud.google.com/data-studio/scorecard-reference) chart.

The following example shows simplified data from Google Analytics. Here, the _Avg. Time on Site_ metric is summarized for all users, regardless of any other consideration, such as whether they are new or returning visitors. The calculations for time on site are computed using the time difference between each user's initial session and the exit, with the sum of each session length averaged across three sessions.

![A scorecard chart displays the overview metric for Avg. Time on Site for all users as the value 210.](https://docs.cloud.google.com/static/data-studio/images/metric-info-graphic-1-2016-06-07.png)

#### In association with one or more dimensions

Metric values can be qualified by selected dimension(s). All the other chart types fall into this category.

In the following example, the bar chart pairs the _Avg. Time On Site_ metric with the _User Type_ dimension. This visualization lets you analyze this metric through _returning_ verses _new_ users, where the calculations are modified by the requested dimension.

![A scorecard chart displays the overview metric for Avg. Time on Site split between the User Types Returning Users \(135\) and New Users \(360\).](https://docs.cloud.google.com/static/data-studio/images/metric-info-graphic-2-2016-06-07.png)

Adding multiple dimensions to a chart refines your view of the data. For example, suppose you use both the _User Type_ dimension and the _Language_ dimension in a table to analyze time on site for your website. In this case, the calculation for _new_ versus _returning_ users is the same, but that calculation is aggregated per language. Your table might look like this:

User Type  |  Language  |  Avg. Session Duration   
---|---|---  
Returning Visitor  |  zh-tw  |  00:04:54   
New Visitor  |  zh-tw  |  00:04:02   
Returning Visitor  |  en-us  |  00:03:51   
New Visitor  |  en-us  |  00:03:45   
Returning Visitor  |  en-gb  |  00:03:33   
...  |  |   
  
## Related resources

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
