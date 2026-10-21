---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-set-alerts-based-on-percentage-changes/
title: Setting alert conditions based on percentage changes of data values \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:40.796464+00:00
---

# Setting alert conditions based on percentage changes of data values  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-set-alerts-based-on-percentage-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Setting alert conditions based on percentage changes of data values Stay organized with collections  Save and categorize content based on your preferences. 

You can create an [alert](https://docs.cloud.google.com/looker/docs/alerts-overview) to send an email or a Slack notification whenever the results from a query-based or Look-linked dashboard tile meet or exceed a specified threshold. Looker creates alerts based on comparisons of whole number and decimal data values. Using the workaround described on this page, you can also set alerts based on percentage changes of data values. 

> To set an alert condition based on a percentage change in data values, your query must contain a date field. 

To receive an alert notification when a percentage change in data values has met or exceeded a specified threshold:: 

  * Create a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) to compare percent values. 
  * [Create a new alert](https://docs.cloud.google.com/looker/docs/creating-alerts) to trigger based on the difference in values. 



## Example

For example, a user wants to compare the percent change in average temperature in San Francisco each hour. The goal is to send an alert each time the temperature increases by more than two percent. 

If the current period's average temperature is 100, then that alert would be triggered if the temperature becomes greater than 102, a change of more than two percent. If the 102+ then increases by more than two percent again, then another alert will be triggered. 

To compare percent values, create a table calculation and use it to set the alert: 

  1. Create a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) that computes the percent change row over row. 

` (${measure_name} - offset(${measure_name},1))/offset(${measure_name},1) `

> You can also use the [**% change from previous row**](https://docs.cloud.google.com/looker/docs/table-calculations#%-change-from-previous-row) shortcut calculation. 

  2. Set the table calculation **Format** to **Percent** and specify the number of **Decimals** to show. 
  3. **Save** the table calculation. 

![The data table shows Average Temperature by Hour, pivoted by City. A new table calculation shows the percentage temperature change row over row.](https://docs.cloud.google.com/static/looker/docs/images/alerts-percent-calc-2210.png)
  4. [Save the Explore as a dashboard tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore), if it is not already saved to a dashboard. 
  5. [Create a new alert](https://docs.cloud.google.com/looker/docs/creating-alerts) based on the new table calculation. In the alert [creation dialog](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_conditions), select **greater than** and enter "0.02". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
