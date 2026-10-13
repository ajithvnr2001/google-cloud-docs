---
url: https://docs.cloud.google.com/looker/docs/forecasting-in-visualizations/
title: Forecasting in visualizations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:12.237296+00:00
---

# Forecasting in visualizations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/forecasting-in-visualizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Forecasting in visualizations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

Forecasting lets analysts quickly add data projections to new or existing Explore queries to help users predict and monitor specific data points. Forecasted Explore results and visualizations can be [added](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore) to dashboards and saved as [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore). Forecasted results and visualizations can also be created and viewed on [embedded](https://docs.cloud.google.com/looker/docs/private-embedding) Looker content.

You can forecast data if you have [permission to create forecasts](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_create_forecast).

## How forecasted results are created and displayed

The **Forecast** feature uses the data results in an Explore's data table to calculate future data points. Forecast calculations include only the displayed results of an Explore query; any results that are not displayed because of row limits are not included. For more information about the algorithm that is used to calculate forecasts, see the ARIMA algorithm section on this page.

Forecasted results display as a continuation of existing Explore visualizations and are subject to configured visualization [settings](https://docs.cloud.google.com/looker/docs/creating-visualizations#customizing_visualizations_with_chart_settings). Forecasted data points are distinguished from non-forecasted data points in the following ways:

![](https://docs.cloud.google.com/static/looker/docs/images/forecast-data-display-2414.png)

  1. In supported Cartesian charts, forecasted data points are differentiated from non-forecasted data points by rendering in a lighter shade or by dashed lines.
  2. In supported text and table chart types, forecasted data points are italicized and appended with an asterisk.



Forecasted data is also explicitly identified in the tooltip that appears when you hover your cursor over a forecasted data point.

![](https://docs.cloud.google.com/static/looker/docs/images/forecast-data-display-tooltip-2114.png)

Only certain types of visualizations support forecasted data, as discussed in the following section.

### ARIMA algorithm

Forecasting leverages an AutoRegressive Integrated Moving Average (ARIMA) algorithm to create an equation that best matches the data that is input into a forecast. To find the best match for the data, Looker runs ARIMA with a set of initial variables, creates a list of variations of the initial variables, and runs ARIMA again with those variations. If any of the variations create an equation that better fits the input data, Looker uses those variations as the new initial variables and creates additional variations that are then evaluated. Looker continues to repeat this process until the best variables are identified or until all options or the allocated compute time are exhausted.

This process can be thought of as a [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm), where individuals throughout hundreds of generations create 1 to 10 offspring each (variations of variables based on the parent), and the best offspring survive to potentially create "better" generations. The way Looker uses many invocations of ARIMA in a genetic algorithm approach is called _AutoARIMA_.

For additional details about AutoARIMA, see the [Tips to using `auto_arima`](https://alkaline-ml.com/pmdarima/tips_and_tricks.html) section of the _pmdarima User Guide_. Although this is not the library that Looker uses to run AutoARIMA, pmdarima provides the best explanation of the process and the different variables that are used.

## Supported visualization types

The following Cartesian visualization types support rendering forecasted data:

  * [Column](https://docs.cloud.google.com/looker/docs/column-options)
  * [Bar](https://docs.cloud.google.com/looker/docs/bar-options)
  * [Scatterplot](https://docs.cloud.google.com/looker/docs/scatter-options)
  * [Line](https://docs.cloud.google.com/looker/docs/line-options)
  * [Area](https://docs.cloud.google.com/looker/docs/area-options)



The following text and table chart types support rendering forecasted data:

  * [Table](https://docs.cloud.google.com/looker/docs/table-options)
  * [Table Legacy](https://docs.cloud.google.com/looker/docs/legacy-table-options)
  * [Single record](https://docs.cloud.google.com/looker/docs/single-record-options)
  * [Word cloud](https://docs.cloud.google.com/looker/docs/word-cloud-options)



Other visualization types, including [custom visualizations](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations), cannot currently render forecasted data.

## Explore query requirements for forecasting

To create a forecast, an Explore must meet these requirements:

  * Include exactly one dimension, which must be a timeframe dimension, with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) enabled
  * Include at least one measure or [custom measure](https://docs.cloud.google.com/looker/docs/custom-fields) (a forecast can include up to five measures or custom measures)
  * [Sort](https://looker/docs/creating-and-editing-explores#sorting_data) results by the timeframe dimension in _descending_ order



### Things to consider

The following are additional criteria to consider when you create a new Explore query to forecast or add a forecast to an existing Explore query:

  * **Pivots** — Forecasts can be performed on [pivoted](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) Explores, as long as the preceding requirements are met.
  * **Row totals and subtotals** — [Row totals and subtotals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) do not include forecasted values; we don't recommend using subtotals or row totals with forecasting, as this can produce unexpected numbers.
  * **Filters that include incomplete timeframes** — For accurate projections, forecasting should only be used in conjunction with a **complete** timeframe logic in [Explore filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#filtering_data_overview) when Explores include data for incomplete timeframes. For example, if a user forecasts data for a month into the future while an Explore is filtered to display data for the past three months, the Explore includes the data for the current incomplete month. The forecast will incorporate the incomplete data into its calculation and display more unreliable results. Instead, use filter logic such as **in the past 3 complete months** , rather than **in the past 3 months** , when an Explore includes incomplete timeframes (for example, when an Explore includes incomplete monthly data for the current month) to ensure a more accurate forecast.
  * **Table calculations** — [Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) that are based on one or more forecasted measures will automatically be included in a forecast.
  * **Row limits** — Explore how [row limits](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting_data) apply to the entire data table, including forecasted rows.



For additional tips and troubleshooting resources, see the **Common issues and things to know** section on this page.

Typically, a dataset with more rows, in conjunction with a shorter forecast length, will result in a more accurate forecast.

## Forecast menu options

You can use the options in the **Forecast** menu — located on the Explore **Visualization** tab — to customize forecasted data. The **Forecast** menu includes the following options:

  * **Select field**
  * **Length**
  * **Prediction Interval**
  * **Seasonality**



### Select field

The **Select field** drop-down menu displays the measures or custom measures in the Explore query that are available for forecasting. Up to five measures or custom measures may be selected.

### Length

The **Length** option indicates the number of rows, or the length of time, for which to forecast data values. The forecast duration interval is automatically populated based on the timeframe dimension in the Explore query.

Typically, a dataset with more rows, in conjunction with a shorter forecast length, results in a more accurate forecast.

### Prediction Interval

The **Prediction Interval** option lets analysts express some uncertainty in forecasts to aid in accuracy. When enabled, the **Prediction Interval** option lets you select the bounds of the forecasted data values. For example, a prediction interval of 95% indicates a 95% chance that forecasted measure values will fall between the upper and lower bounds of the forecast.

The larger the selected prediction interval, the wider the upper and lower bounds.

### Seasonality

The **Seasonality** option lets analysts account for known cycles or repetitive data trends in a forecast, and it refers to the number of rows of data in the cycle. For example, if an Explore data table has one row per hour and the data cycles daily, the seasonality is 24.

With default forecast settings, Looker references the date dimension in an Explore and scans several possible seasonality cycles to find the best match for the final forecast. For example, when using hourly data, Looker may try daily, weekly, and four-week seasonality cycles. Looker also takes into account the frequency of the dimension — if a dimension represents a six-hour period, Looker knows there will only be four rows in a day and will adjust the seasonality accordingly.

For common use cases, the **Automatic** option detects the best seasonality for a given dataset. If you are aware of specific cycles in the dataset, the **Custom** option lets you specify the number of rows that make up a cycle for individual measures in a forecast.

When forecasting data values for multiple measures, you can select different seasonality options, including none, for each individual measure. The **Seasonality** drop-down menu has several options:

  * Automatic
  * Custom
  * None



> Forecasting applies the **Automatic** seasonality option to forecasts by default, even when the **Seasonality** option is not enabled.

#### Automatic

With the **Automatic** seasonality option, Looker selects the best option for your data from multiple common seasonality periods, such as daily, hourly, monthly, and so on.

#### Custom

When you know the specific number of rows that make up each season or cycle in your dataset, you can specify the number in the **Period** field. It may be helpful to select **Custom** if you know that your data cycles in a specific number of rows.

When you are working with data that cycles in months but is expressed in greater granularity (for example, using a **date** or **week** granularity in an Explore), generally a 4-week or 30-day period fits monthly cycles.

#### None

Seasonality is a powerful component of forecasting; however, depending on the input data, it's not always recommended. If there are no predictable cycles in the data, enabling seasonality can occasionally lead to inaccurate forecasts when the algorithm will attempt to find a pattern and then attempt to fit the false pattern to the forecast. This can result in an obscure prediction.

When you are forecasting data values for multiple measures and want to enable **Seasonality** only for one or a few, you can select **None** for all measures for which you _don't_ want to enable **Seasonality**.

## Creating a forecast

Only users with [permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_create_forecast) can create forecasts.

To create a forecast, follow these steps:

  1. Ensure that your Explore meets the forecast requirements. As an example, a user wants to create a forecast for an Explore query with **Users Created Month** , **Users Count** , and **Orders Count** that is sorted by **Users Created Month** in descending order. The results display data through December 2019.

![](https://docs.cloud.google.com/static/looker/docs/images/how-to-forecast-1-3-2310.png)

  2. Click **Forecast** on the Explore **Visualization** tab to open the **Forecast** menu.

  3. Click the **Select field** drop-down menu to choose up to five measures or custom measures to forecast. The user in the example selects **Users Count** and **Orders Count**.

![](https://docs.cloud.google.com/static/looker/docs/images/how-to-forecast-4-2308.png)

  4. Enter the length of time in the future that you want to forecast in the **Length** field. The user in the example enters **6** months.

  5. Optionally, click either the **Prediction Interval** or the **Seasonality** switch to enable either function and customize the associated options. The user in the example does not enable either option.

  6. Click the **x** in the menu tab next to **Forecast** to save your settings and exit the menu.

  7. Click **Run** to re-run the Explore query. (You must re-run the Explore after making any changes to the forecast.)




Your Explore results and visualization will now display forecasted values for the length of time specified. With the specified options, the example Explore displays forecasted data for **Users Count** and **Orders Count** for six months from 2020-01 to 2020-06.

![](https://docs.cloud.google.com/static/looker/docs/images/how-to-forecast-result-2414.png)

Because forecasted calculations are dependent on the order in which data is sorted, sorting is **disabled** once a forecasted query has run.

## Editing a forecast

Only users with [permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_create_forecast) can edit forecasts.

To edit a forecast:

  1. Optionally, edit the Explore query as needed to add or remove different measures or timeframe fields. Ensure that your Explore meets the forecast requirements.
  2. Click **Forecast** on the Explore **Visualization** tab to open the **Forecast** menu.
  3. Click the **Select field** drop-down menu to make changes to the forecasted fields. To remove forecasted fields: 
     * Click the boxes next to the forecasted fields in the expanded **Select field** drop-down menu to remove the fields from the forecast.
     * Alternatively, click the **x** next to the field name in the collapsed **Select field** menu.
  4. Edit the specified length of time in the future to forecast in the **Length** field, as desired.
  5. Optionally, click either the **Prediction Interval** or the **Seasonality** switch to enable either function and customize the associated options. 
     * If either **Prediction Interval** or **Seasonality** was already enabled, the customizations will be displayed. Edit custom settings as desired, or select the switch to remove the function from the forecast.
  6. Click the **x** in the menu tab next to **Forecast** to save your settings and exit the menu.
  7. Click **Run** to re-run the Explore query. (You must re-run the Explore after making any changes to the forecast.)



Your Explore results and visualization will now display the amended forecast. Because forecasted calculations are dependent on the order in which data is sorted, sorting is **disabled** once a forecasted query has run.

## Removing a forecast

Only users with [permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_create_forecast) can remove forecasts.

To remove a forecast from an Explore:

  1. Click **Forecast** on the Explore **Visualization** tab to open the **Forecast** menu.
  2. Click **Clear** at the top of the **Forecast** menu.



The query will automatically re-run to produce the results without a forecast applied.

## Common issues and things to know

### How accurate is it?

The accuracy of a forecast depends on the input data. Looker's AutoARIMA implementation can make incredibly accurate predictions that successfully combine many nuances from the input data. There are also cases in which the algorithm gets caught up in odd patterns in the input data and overemphasizes them in the prediction. Make sure that enough data is provided and that the data is as accurate as possible to get the most out of forecasting.

### A forecast could not be generated

There are legitimate reasons that a forecast cannot be generated. These usually have to do with the amount of input data being too little or the requested length of forecast being too large. There is no specific limit to either factor, and there is no exact ratio of required input data for a certain length of forecast. The more scattered and unpredictable the input data, the more difficult it will be for the AutoARIMA algorithm to find a match. The most effective way to generate a forecast is to increase the amount of clean input data, make sure the seasonality settings are correct, and reduce the forecast length to only what's needed. When using the **Prediction Interval** option, it may help to choose a lower interval.

Cleaning input data can involve:

  * Trimming leading or trailing rows that are for time periods that do not contain data
  * Reducing noise in the dataset by choosing a larger date dimension
  * Changing filter outliers that don't benefit the prediction



### The query result returned without forecasts, and I received an obscure error

This should not occur; if it does, try removing the measure or measures from the forecast config and then re-adding them.

### The forecast displays but it is obviously wrong or unhelpful

The best thing to do in this case is to add more input data, clean it up as much as possible, and potentially set a custom seasonality (if you are aware of specific cycles in the data) or disable the **Seasonality** option altogether by selecting **None**.

Cleaning input data can involve the following tasks:

  * Trimming leading or trailing rows that are for time periods that do not contain data
  * Reducing noise in the dataset by choosing a larger date dimension
  * Changing filter outliers that don't benefit the prediction



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
