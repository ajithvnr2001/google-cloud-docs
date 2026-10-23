---
url: https://docs.cloud.google.com/data-studio/what-does-the-unable-to-aggregate-ratio-metrics-error-mean/
title: What does the 'Unable to aggregate ratio metrics' error mean? \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:36.100143+00:00
---

# What does the 'Unable to aggregate ratio metrics' error mean?  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/what-does-the-unable-to-aggregate-ratio-metrics-error-mean/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  What does the 'Unable to aggregate ratio metrics' error mean? Stay organized with collections  Save and categorize content based on your preferences. 

## At a glance

Have you seen this error message?

**Unable to aggregate ratio metrics in the request. Please select another metric.**

This error means that you've asked Data Studio to do something with an already [aggregated](https://docs.cloud.google.com/data-studio/aggregation) ratio metric that it can't do. For example, you've applied a filter based on a calculated field to a chart that contains a ratio metric.

The solution is to select a non-ratio field in the chart (for example, use **Impressions** instead of **CTR**), or remove or change the filter.

## In depth

Ratio metrics show the relative sizes of two or more values. For example, the Google Ads metric, **Clickthrough rate** ([CTR](https://support.google.com/google-ads/answer/2615875)), is the number of clicks that your ad receives divided by the number of times your ad is shown. In Google Analytics, [**Engagement rate**](https://support.google.com/analytics/answer/12195621) is the percentage of engaged sessions on your website or mobile app, while [**Bounce rate**](https://support.google.com/analytics/answer/12195621) is the opposite of the engagement rate. The bounce rate is the percentage of sessions that were not engaged.

In Data Studio, you get the prior error when you filter a chart that includes ratio metrics in a way that requires the product to recalculate the ratios.

### Here are 3 things to help you understand this issue:

  1. Data from data sets such as Google Analytics, Google Ads, YouTube, and Google Marketing Platforms products is already aggregated by the time it gets to Data Studio. For example, when Data Studio requests a Google Ads metric such as **CTR** (click-through rate), the data is already processed into the appropriate aggregation type.

  2. Because of the previous point, calculated field functions are applied to your data post-aggregation. It's not possible (nor would it generally make sense) to go back into the raw data and look at every unique instance of that metric. For example, if you try to create a calculated field with the formula `SUM( Impressions )` in a Google Ads data source, you'll get the following error:

`Re-aggregating metrics is not supported`.

That's because **Impressions** is already aggregated (and its aggregation type, **Auto** , can't be changed).

**Note:** This isn't necessarily the case with data sources such as Google Sheets, MySQL, or BigQuery, where you are able to send non-aggregated data to Data Studio. For example, if you had raw impression data in a Sheet, you could use functions like the SUM function to add it all up and the AVG function to generate the average.
  3. For consistency, all calculated field functions in Data Studio are available for use with all data source types, even if the underlying system doesn't natively support that function. For example, you can use the CONCAT function to join multiple values in any data source, even if the underlying system doesn't have a CONCAT function of its own. Instead of "pushing down" the CONCAT function to the underlying system, Data Studio requests the data and performs the concatenation itself.




## Aggregation failure example

So what does all that have to do with the `Unable to aggregate ratio metrics` error? This example goes a little deeper with the CONCAT example to help you find out.

Suppose you create a calculated field called **Campaign : Click Type** in a Google Ads data source, using the following formula:

`CONCAT(Campaign, " : ", Click Type)`

Data Studio issues queries for **Campaign** and **Click Type** individually, and then performs the concatenation. The results are grouped, so there is no duplication of records.

You can now use that concatenated field in your charts, and the metrics you include are aggregated properly. For example, we could use **Campaign : Click Type** as the dimension and **CTR** as the ratio metric in a table:

![A table chart displays the metric CTR grouped by the concatenated field Campaign : Click Type.](https://docs.cloud.google.com/static/data-studio/images/reag-example-1-2017-06-04.png)

But now, suppose you apply a filter to show only those records where the value of **Click Type** is `Headline`:

![A filter uses the Campaign : Click Type concatenated field to display concatenated values that contain the string Headline.](https://docs.cloud.google.com/static/data-studio/images/reag-example-3-2017-06-04.png)

This will break the chart:

![A broken chart tile displays the text Configuration error with a See Details link to view more details.](https://docs.cloud.google.com/static/data-studio/images/reag-example-4-2017-06-04.png)

## Why it breaks

The filter asks Data Studio to include each record returned by the **Campaign : Click Type** if it contains the string `Headline`. That field is a concatenation of two dimensions; to fulfill this request, Data Studio has to refetch those dimensions, and then apply the filter. The problem is the presence in the table of the ratio metric, **CTR**. Google Ads ratio metrics are computed before Data Studio requests them. Data Studio has no way to access the raw data and recompute the new ratios for the records that contain only the string `Headline` in the concatenated field.

## The solution

The solution in cases like this depends on the data you are trying to show. In this example, you could either replace the **CTR** metric with a non-ratio metric, such as **Impressions**. Or, instead of filtering on the concatenated **Campaign : Click Type** field, put the filter on the standard **Click Type** field, which would achieve the same result.

![A filter uses the Click Type field to display values that contain the string Headline.](https://docs.cloud.google.com/static/data-studio/images/reag-example-5-2017-06-04.png)

The chart now works:

![A table chart with CTR grouped by the Campaign : Click Type concatenated field displays values that include the string Headline.](https://docs.cloud.google.com/static/data-studio/images/reag-example-6-2017-06-04.png)

## Related resources

  * [Google Analytics Dimensions & Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets)
  * [Google Ads Glossary](https://support.google.com/google-ads/topic/3121777)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
