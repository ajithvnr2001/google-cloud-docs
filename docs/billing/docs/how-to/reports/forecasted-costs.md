---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/forecasted-costs/
title: Billing reports: View your forecasted costs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:15.214179+00:00
---

# Billing reports: View your forecasted costs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/forecasted-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: View your forecasted costs Stay organized with collections  Save and categorize content based on your preferences. 

In [Cloud Billing cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can use the forecast feature to see how your costs are trending and how much you're projected to spend, up to 12 months in the future.

If you're viewing your Cloud Billing report using a date range that ends in a _future_ date, your Cloud Billing report chart displays both actual costs and forecasted costs:

  * The report header above the chart provides a split view of cost: actual cost-to-date calculated from the starting date, and the total forecasted cost for the entire date range.
  * Your forecasted cost is indicated in the chart using light grey in the stacked bar or line chart.

**Note:** The cost forecast is an approximation based on your historical trends and uses advanced machine learning to provide more accurate cost predictions.

![Google Cloud Billing report showing forecasted costs.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports7.png)

### How to view your cost forecasts

In the **Billing** section of the Google Cloud console, [access the cost report](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) for the Cloud Billing account you want to analyze.

In reports, forecasts are available for:

  * Any combination of [filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping), _except_ for the following:

    * When using a _Billing period_ (formerly _Invoice month_) **Time range**.
    * When **filtering** on _Products_ , _Originating products_ , _Spend-based CUDs_ , or _Originating services_.
  * Any _Charge period_ (formerly _Usage date_) **Time range** that ends with a _future_ date. (Forecasts aren't available for a _Billing period_ (formerly _Invoice month_) **Time range**.)

    * If you're viewing the report for the **Current month** time range, the default end date is the _last day of the current month_.
    * If you choose to specify a **custom date range** , select **By charge period** , and configure a date range with the **To:** date set for a _future_ date.

You can see your forecasted spend up to 12 months in the future.




### The cost prediction is driven by AI

The cost forecasting model applies advanced machine learning techniques designed to understand complex cost patterns and handle real-world data imperfections to provide you with more reliable and actionable cost predictions. The cost trend is determined by:

  1. **Gathering historical data** : Based on the report filters you select, the forecasting model collects all of your historical Google Cloud spend.
  2. **Smart data preparation** : Using a comprehensive suite of data pre-processing steps, high-quality data is prepared that intelligently handles outlier costs (such as unexpected cost spikes), more accurately fills in gaps in usage data, and detects significant shifts in your spending patterns to adapt the forecast accordingly (for example, due to new project launches or major architectural changes).
  3. **Accounting for seasonality and trends** : The machine learning engine is designed to recognize and adapt to multiple layers of seasonality and underlying trends in your cost data, detecting and modeling various recurring patterns, such as daily, weekly, and monthly cycles in your cloud spend.
  4. **Comprehensive data regularization** : The forecasting model consistently structures your cost data over time, enabling reliable time-series analysis by our machine learning models. This generates a forecast that intelligently captures complex trends, multiple seasonalities, and handles data anomalies.



**The total forecasted cost combines the following costs:**

  * The total _actual_ cost to date for the selected time period.
  * The predicted cost for each future day in the selected time period.

**Note:** The _Charge period_ (formerly _Usage date_) _Time range_ that you select for the report doesn't limit what data is used to generate the cost trend and forecast. For example, if you're viewing a report for the current month, cost data from previous months is included in the forecasting model for the calculation of predicted cost.

## Related topic

  * [Analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
