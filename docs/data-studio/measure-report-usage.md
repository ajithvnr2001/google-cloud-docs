---
url: https://docs.cloud.google.com/data-studio/measure-report-usage/
title: Measure report usage \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:04.492703+00:00
---

# Measure report usage  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/measure-report-usage/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Measure report usage Stay organized with collections  Save and categorize content based on your preferences. 

Google Analytics is a free digital analytics service that lets you measure how your websites and mobile apps are being used. You can use Analytics to gather anonymous usage data on your Data Studio reports to answer questions such as the following:

  * How many views are my reports getting?
  * How are users finding my reports?
  * Where are my report viewers coming from?



You can also get automated insights and use Google Analytics Explorations to dig deeper into your data.

## Add your Google Analytics measurement ID to a report

To begin measuring your Data Studio report usage, follow these steps to add your Google Analytics 4 (GA4) measurement ID to a report:

  1. Edit the report that you want to measure.
  2. Select **File > Report settings.**
  3. In the bottom of the **Report Settings** panel, enter your measurement or tracking ID.



Google Analytics 4 measurement IDs begin with "G-". [Learn how to find your GA4 ID](https://support.google.com/analytics/answer/9304153#other).

**Tip:** New to Google Analytics? [Learn how to set up Google Analytics 4 for a website or app](https://support.google.com/analytics/answer/9306384).

## See your data in Google Analytics 4

It may take up to 24 hours before data from your reports begins to show up in Google Analytics.

Use the [Reports snapshot](https://support.google.com/analytics/answer/10668965) to get a quick overview of your Data Studio traffic. You can also test your implementation with the help of the [Realtime](https://support.google.com/analytics/answer/9271392) report. And to get deeper insights from your data, you can use any of the available [exploration](https://support.google.com/analytics/answer/7579450) techniques.

## See your data in Data Studio

To see your Data Studio traffic data in Data Studio, [create a Google Analytics data source](https://docs.cloud.google.com/data-studio/connect-to-google-analytics) connected to the GA4 property that you set up for that purpose.

## Limits of report measurement

  * Your reports can have only one Google Analytics 4 measurement ID.
  * Google Analytics collects only the `duplicate_report` event. Data Studio sends this event when a user copies (duplicates) a report.
  * When visualizing Google Analytics 4 data with a stacked bar chart, you may encounter data discrepancies if filters are applied and the chart uses a date dimension such as `Day`. Discrepancies can occur because Data Studio is unable to push down all filters to Google Analytics for certain chart configurations, which can lead to incorrect re-aggregation of data in Data Studio. 

To work around this limitation, edit the data source and change the data type of the date dimension (for example, `Day`) to `Text`. If this change impacts other charts in your report, you can create a separate Google Analytics data source with this modification to be used by the stacked bar chart only.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
