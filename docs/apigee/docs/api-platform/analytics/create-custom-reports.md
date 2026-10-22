---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports/
title: Creating and managing custom reports \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:02.131382+00:00
---

# Creating and managing custom reports  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Creating and managing custom reports Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Custom reports enable you to drill down into specific API metrics and view the exact data that you want to see. You can create a custom report by using any of the [metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics) and [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions) built into Apigee. 

There are two types of custom reports:

  * _Real-time reports_ (also called _synchronous reports_): When you specify the report parameters in the Apigee UI, real-time reports are displayed in the Apigee UI within a couple of minutes.
  * _Report jobs_ (also called _asynchronous reports_): For custom report jobs you request the report and retrieve the results at a later time.



See Real-time reports versus report jobs.

## Availability of custom reports

If you are an Apigee Subscription customer, access to Apigee API Analytics and the custom report functionality is included in your [subscription entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) and automatically enabled for each of your Apigee environments. 

If you are a [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) customer, you must enable Apigee API Analytics as a paid add-on to access analytics and generate custom reports. For more information on enabling the Apigee API Analytics add-on for your Intermediate or Comprehensive Apigee environments, see [ Manage the Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on).

If you are unsure whether you are using a Subscription or Pay-as-you-go Apigee organization, contact your Apigee organization administrator.

## About custom reports

When building a custom report, you'll select the data you want to see ([metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics)), group the data in meaningful ways ([dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions)), and optionally limit the data returned based on specific characteristics ([filters](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters)) of the data. 

You can also set the chart type displayed in the custom report as a column or line chart. The following images show chart examples for the transactions per second metric grouped by the API proxy dimension: 

  * Column - each API proxy is represented by a different column:

![Custom column chart](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/custom_col_chart_ex.png)

  * Line - each API is represented by a different line:

![Custom line chart](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/custom_line_chart_ex.png)




### Setting metrics and dimensions

The [metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics) you choose for your custom report specify the data you are trying to measure. Common metrics include: 

  * Transactions per second
  * Response time
  * Policy errors



In addition to the standard metrics and dimensions, you can also create custom reports for custom data you collect using the DataCapture policy. See [Collecting custom data with the DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture).

Some metrics let you set an _aggregation function_ to run against the metric. For example, you can use the following aggregation functions with the response time metric:

  * `avg`: Returns the average response time.
  * `min`: Returns the minimum response time.
  * `max`: Returns the maximum response time.
  * `sum`: Returns the sum of all response times.



Not all metrics support all aggregation functions. The documentation on [metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics) contains a table that specifies the metric name and the function (`sum`, `avg`, `min`, `max`) supported by the metric.

The [dimension](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions) specifies how to group the metrics data. For example, you want to create a custom report showing the response time metric. You can use dimensions to group the metrics data by API product, API proxy, or AppGroup:

  * The response time per **API product**
  * The response time per **API proxy**
  * The response time per **AppGroup**



The way the dimension is displayed in the chart of the custom report depends on the chart type:

  * Column: Each column corresponds to a different dimension value.
  * Line: Each line in the chart corresponds to a different dimension value, and the x-axis represents time. 



### Setting filters

A [filter](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters) lets you limit the metrics data displayed in the custom report by setting specific characteristics on the metrics data to return. For example, you can create a filter so that you see metrics data only for a response time greater than a specific value or only for an API proxy with a specific name.

You can build complex filters using conditional syntax and operators such as `eq`, `ne`, `gt`, `lt`, and more.

### Custom report examples

In the simplest type of custom report, you specify a single metric and a single dimension. For example, you define a custom report with the following settings: 

  * type = Column
  * metric = Average transactions per second
  * dimension = API Proxy



The custom report contains a column chart with the "Average transactions per second" metric data grouped by the API proxy dimension:

![Custom report tps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/cust_report_tps_proxy.png)

You can add multiple metrics to a custom report. For example, you define a custom report with two metrics: 

  * type = Column
  * metric = Average transactions per second
  * metric = Policy Errors
  * dimension = API Proxy



The custom report contains a separate chart for each metric:

![Custom report two metrics](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/cust_report_tps_policy_proxy.png)

You can add multiple dimensions to a custom report. For example, you define a custom report with the following settings that includes two metrics and two dimensions: 

  * type = Column
  * metric = Average transactions per second
  * metric = Policy errors
  * dimension = API Proxy
  * dimension = Request verb



## Real-time reports versus report jobs

Apigee Analytics lets you run a _real-time report_ or a _report job_.

  * For real-time reports, you request the report and it is displayed as soon as the analytics server provides a response. However, because a report might need to process a large amount of data (for example, 100's of GB), a real-time report might fail because of a time out.

A real-time report can have a maximum time range of 92 days. If you select a time range greater than this, the report is run as a report job. 

See Run a custom report.

  * For a report job, you request the report and retrieve the results at a later time. Some situations when a report job might be a good alternative include:

    * Analyzing and creating reports that span large time intervals.
    * Analyzing data with a variety of grouping dimensions and other constraints that add complexity to the query.
    * Managing queries when you find that data volumes have increased significantly for some users or organizations.
**Note:** Report jobs have the following limits: 
    * Maximum time range is 365 days.
    * 32 MB size limit on the results of a query.

You can also run a report job using the API, as described in [Using the asynchronous custom reports API](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/asynch-reports-api). See View a report job.




## Open the Custom Reports page

In the Google Cloud console, go to the **Apigee > Analytics > Custom reports ** page.

[Go to Custom reports](https://console.cloud.google.com/apigee/analytics/custom-reports)

![Custom reports dashboard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/custom-reports-cloud-console.png)

The Custom Reports page has two tabs:

  * **Reports** : Displays real-time reports.
  * **Report Jobs** : Displays report jobs.



See Real-time reports versus report jobs.

Both tabs display a list of the reports or report jobs that have already been created. To view a report or report job, click the name of the report. See Run a report for an example.

### **Reports**

The **Reports** tab displays the following information about each report:

  * **Display Name** : The name of the report.
  * **Dimensions** : The dimensions included in the report.
  * **Metrics** : The metrics and aggregation functions (such as **sum**) included in the report.
  * **Last Modified** : The last time and date when the report was run.



### **Report Jobs**

The **Report Jobs** tab displays the following information about each report job:

  * **Report Name** : The name of the report.
  * **Start Time Range (UTC)** : The start time of the report job.
  * **End Time Range (UTC)** : The end time of the report job.
  * **Status** : The status of the report job, which can be **running** , **completed** , or **expired**.
  * **Submitted** : The date and time when the report job was submitted.



The Custom Reports page enables you to:

  * View a custom report and report job.
  * Create a custom report or report job.
  * Run a report.
  * Edit a custom report or report job.
  * Delete a custom report or report job.



## Create a custom report

This section explains how to create a custom report.

**Note:** Free and trial accounts cannot create custom report jobs. For more information, see [Apigee pricing plans](https://apigee.com/api-management/#/pricing). 

In the Custom Reports page, you can create either a real-time report or a report job. To do so:

  1. Open the Custom Reports page.
  2. Click **\+ Create**. 
     * To create a real-time report, select **Custom Report**.
     * To create a report job, select **Custom Report Job**.
  3. In the **Basic** section, enter the following information: 
     * **Report Name** : Name of the report.
     * For a real-time report only, you can also enter an optional **Description** of the report.
  4. The following sections depend on whether you are creating a real-time report of a report job: 
     * **For real-time reports only:**

After **Chart Type** , select the style of chart to present your data: 

       * Column: X-axis represents groups designated by dimensions.
       * Line: X-axis represents time.
     * **For report jobs only:**
       * **Report Details** : In the **Environment** field, select the environment in which you want to run the report. Note that for real-time reports, you can select the environment in the report page, after the report has run.
       * **Report Date Range** : Select the **Start time** and **End time** for the report. 

**Note:** The maximum date range for a report job is 365 days. For reports requiring date ranges precise to the second, use the [ Custom Reports API](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/asynch-reports-api#about-request-body) to create the report job. The API accepts date range inputs that include seconds.

  5. In the **Metrics** section: 
     1. Select the metric that you want to analyze.
     2. Select an **Aggregate function** to display the Sum, Average, Min, or Max values.
     3. Click **Done**.

**Note:** In addition to the standard metrics and dimensions, you can also select metrics or dimensions corresponding to [custom data collected with the DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture).

  6. In the **Dimensions** field, select a dimension, such as "Proxy", to constrain the data set used to generate the reports. You can add additional dimensions to further constrain the data.
  7. In the **Filter** section, you can further narrow the data displayed by adding filters to your report definition. For example, you could add a filter that excludes data for the weather API proxy or developer jane@example.com.

First, click **Add a Filter** to open the **New Filter** section.

     1. Select the name of the entity you want to filter on, which can be a metric or a dimension.
     2. Select an operator such as = or !=, and a Value.
     3. Enter a value for the metric or dimension.
     4. Click **Done** to add the filter.
  8. Click **Save** to save the report.



## Run a report

To run a real-time report:

  1. Open the Custom Reports page. 
  2. In the **Reports** tab, select the report to run.



When the report is ready, it is displayed:

![Custom report displayed.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/custom-report-example.png)

The report displays a chart of the data and a summary table.

**Note:** The report only displays one dimension at a time. If the report has multiple dimensions, you can select the dimension to display in the **Dimension** field.

In the report page, you can select the following options for the report:

  * **Environment** : The environment in which to run the report.
  * A time period for the report. **Note:** The maximum time range for a custom report is 92 days. To create a report with a longer time range, you must submit it as a report job.
  * **Dimension** : A dimension for the report. Only one dimension can be displayed at a time.
  * **Value** : A specific value for the dimension, or **All** to display all values.



You can also choose the following options at the top of the report page:

  * **Edit** : Edit the details of the report.
  * **Export** : Download the data for the report in a CSV file.
  * **Submit Job** : Submit the report as a report job. When you click **Submit Job** , a dialog opens giving you the options that are described in Create a custom report. After you have entered the options, click **Create** to create the report job.

**Note:** Custom ranges cannot exceed 92 days for real-time custom reports and 365 days for report jobs.

See View a report job for more information about report jobs.

## View a report job

To view a report job, select the **Report Jobs** tab at the top of the Custom Reports page. 

The **Report Jobs** tab is displayed:

![Report jobs](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/report-jobs-cloud-console.png)

The Report Jobs page enables you to:

  * View all report jobs that have been submitted in the last 7 days.

**Note:** Report jobs results are deleted after 7 days.
  * Select the environment for which you want to display report jobs.

  * Search the list of custom reports by entering all or part of a relevant string in the search box; all displayed fields are searched for the string.




To view the custom report, make sure its **Status** is completed. Then click the report name to view the report.

**Note:**

You cannot view a report job that:

  * Is still running.
  * Exceeds the maximum view size of 2MB.



## Edit a custom report

To edit a custom report:

  1. Open the Custom Reports page. 
  2. Click the three-dot menu under **Actions**.
  3. Select **Edit**. This opens the **Edit custom report** dialog, where you can edit the options for the report. The options are described in Create a custom report.
  4. Click **Update** to save your changes.



## Delete a custom report

To delete a custom report:

  1. Open the Custom Reports page. 
  2. Click the three-dot menu under **Actions**.
  3. Click **Delete** to delete the report.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
