---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-reports-ui/
title: Manage security reports in the UI \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:52.956822+00:00
---

# Manage security reports in the UI  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-reports-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage security reports in the UI Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to create and view security reports in Apigee in Cloud console. 

For an overview of security reports, including limitations, see [ Security reports overview](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs).

## Access security reports

To open the **Security reports** view in Apigee in Cloud console, go to the **Advanced API security > Security reports** page.

[Go to Security reports](https://console.cloud.google.com/apigee/apiSecurity/securityReports)

This displays the main **Security reports** view:

![Security reports main window.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/security_report_list.png)

At the top of the page, you can select:

  * The environment in which you want to create a report.
  * The **Report type** filter. The options are: 
    * **All**
    * **Active**
    * **Failed**
    * **Expired**



Below those options, the security reports are displayed in table rows. Each row displays these report details:

  * The **Report Name**. Click the report name to view the report.
  * The report **Status** , which can be one of the following: 
    * **running** : The report is currently running and cannot be viewed yet.
    * **completed** : The report is completed and can be viewed or exported.
    * **expired** : The report has expired and can no longer be viewed or exported in the UI. To view a report after the expiration date, you must export it before that date. After 30 days, the report is removed from the list of available reports.
  * The **Start time** and **End time** display the start and end dates and times for the report.

  * **Submitted date** : The date and time the request for the report was submitted.
  * **Expiration time:** The date and time when the report expires and can no longer be viewed in the Apigee UI. The expiration date is 7 days after the time when you created the report. After 30 days, the report is removed from the list of available reports. You cannot view or export reports in the UI after their expiration date.
  * **File size:** The report file size. You might need to modify the report criteria in order to create a report with a file size below the maximum file size. See [ Limitations on security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#limitations-on-security-reports) for information on the maximum file size and specific ways to reduce the file size.
  * **Export** : Exports/downloads the report in a zip file. Export is only available if the status of the report is **completed**.



## Create a new security report

To create a new security report, start by clicking **+Create** in the **Security reports** view. This opens the **Create Security Report Job** dialog, where you can configure the options for the report as described in the next section.

### Security report options

You can specify the following options for a security report:

  * **Report Name:** A name for the report.
  * **Report Date Range:** Start time and end time for the report. 

**Note:** The start and end times of the report must be in the past, and at most one year in the past when the report is created.

  * **Metrics:** Metric for the report. See [ Metrics and aggregation functions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#metrics_and_aggregation_functions_in_security_reports) for information on available metrics. 
  * **Dimensions:** Dimensions let you group metric values together based on related subsets of the data. See [Dimensions in security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#dimensions_in_security_reports) for information on available dimensions. 

See [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions) for other dimensions supported by Advanced API Security reports.

To add multiple dimensions, click **+Add a Dimension** for each dimension you want to add. You can also change the order in which dimensions appear in the report by clicking the up or down arrows to the right of the dimension field.

**Note:** The order of dimensions does _not_ affect the numerical values shown in the report—only the order in which dimensions are presented in the report.
  * **Filters:** Filters let you restrict results to metrics with specific values. **Important:** Security report jobs that filter on the `incident_id` must include the `incident_id` as a dimension. To create a filter, set the following fields: 
    * Select a name for the filter.
    * Select a comparison operator.
    * Select a value.

See [Filters](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters) for more information on filters. 




After you have selected all the report options, click **Create** to create the report job. You might need to wait for a while until the report is completed. You can click the **Refresh** button at the top right of the pane to see the completed report.

## View a completed report

Once a report is completed, it is displayed in the table as shown below:

![Security report displayed in table.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/security_report_list.png)

To view the report, either:

  * Click the report name.
  * Click **Export** in the row for that report.

**Note:** Bot detection has a processing delay of around 15 to 20 minutes on average.

### Example: bot IP addresses report

The following example creates a report that shows the IP addresses of detected bots. To create the report, use the following configuration:

  * Metric: **bot** , the number of distinct IP addresses identified as sources of bots.
  * Aggregation function: **count_distinct**
  * Dimension: **Resolved Client IP**



The completed report is shown below:

![Security Report bot IP address report](https://docs.cloud.google.com/static/apigee/docs/api-security/images/bot-ip-addresses.png)

Note that the table at the bottom of the report lists IP addresses that Advanced API Security has identified as bots.

### Example: bot traffic by bot reason report

The next example creates a report of bot traffic—the number of requests from IP addresses that have been identified as the sources of bots—by **bot_reason** —the set of detection rules that led to the bot being detected. To create the report, use the following configuration:

  * Metric: **bot_traffic**
  * Aggregation function: **sum**
  * Dimension: **bot_reason**



The completed report is shown below:

![Security Report bot traffic by bot reason \\report](https://docs.cloud.google.com/static/apigee/docs/api-security/images/bot-reason-report.png)

Each **bot_reason** consists of a subset of the individual [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules). As you can see in the graph, The detection rule that contributed to the largest amount of bot traffic is the following set of rules: 

  * Flooder
  * Brute Guessor
  * Robot Abuser



### Example: bot traffic report

The next example creates a report that isn't grouped by a dimension. If you don't want to group data by a dimension, you can set **Dimension** to **environment**. Since data is always restricted to the selected environment, this results in a report that has no grouping of data.

  * Metric: **bot traffic**
  * Aggregation function: **sum**
  * Dimension: **environment**

![Security Report of bot traffic report](https://docs.cloud.google.com/static/apigee/docs/api-security/images/bot-traffic-report.png)

The report displays the total traffic from IP addresses that have been identified as sources of bots, for each one-minute interval throughout the report time range. Note that there is no grouping.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
