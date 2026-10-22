---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-failed-sessions/
title: Failed sessions dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:54.370565+00:00
---

# Failed sessions dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-failed-sessions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Failed sessions dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With these dashboards, get insight into why your sessions are failing. You can use this information to investigate how to decrease the number of session failures. This could include eliminating technical problems, including poor sound quality, that can lead to premature hang ups. This could also include process improvements for how agents handle calls, making it less likely that end-users end sessions prematurely.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Failed Sessions**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears.

  2. Click **Calls** or **Chats**.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset data range. To do this follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Start Time** and **End Time** : get results from only within this time range

     * **Call ID** : by call ID

     * **Fail Reason** : by a particular failed reason

     * **Interaction Type** : by interaction type—for example, IVR Inbound, IVR Inbound mobile, or Web

     * **Direction** : by the direction of the session

     * **Agent Name** : by agent name

     * **Location** : by location

     * **Teams** : by one or multiple teams

     * **Support Phone Number** : by the support phone number

     * **Phone Number** : by the phone number of the end-user

  5. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

This dashboard contains the following metric tiles for calls:

  * **Total Failed Sessions** : the number of sessions where an error was returned

  * **Agent Errors** : the number of errors associated with an agent leg of a session

  * **Consumer Errors** : the number of errors associated with an end-user leg of a session

  * **Carrier Errors** : the number of errors attributed to a carrier

  * **Deflection Errors** : the number of errors associated with a deflection

  * **Miscellaneous Errors** : the number errors that are undefined

  * **Failed %** : the percentage of sessions that failed

  * **Failed Sessions by 30 minute Interval** : bar charts showing failed sessions by 30 minute intervals. Click a bar chart to display a menu, and then click a menu item to get additional information about failed sessions for that day.

  * **Total Sessions** : the number of sessions that were received

  * **Completed Calls** : the number of received sessions that were successfully handled

  * **Sessions Failure Breakdown** : a pie chart showing the sessions that have failed, by category.




This dashboard contains the following metric tiles for chats:

  * **Total Failed Sessions** : the number of sessions where an error was returned

  * **Consumer Errors** : the number of errors associated with an end-user leg of a session

  * **Carrier Errors** : the number of errors attributed to a carrier

  * **Deflection Errors** : the number of errors associated with a deflection

  * **Miscellaneous Errors** : the number errors that are undefined

  * **Failed %** : the percentage of sessions that failed

  * **Failed Sessions by 30 minute Interval** : bar charts showing failed sessions by 30 minute intervals. Click a bar chart to display a menu, and then click a menu item to get additional information about failed sessions for that day.

  * **Total Sessions** : the number of sessions that were received

  * **Completed Chats** : the number of received sessions that were successfully handled

  * **Sessions Failure Breakdown** : a pie chart showing the sessions that have failed, by category.




## Tables

This dashboard contains the following metrics table. Hold the pointer over a table heading to see its description.

  * **Historical** : displays all of the relevant information relative to the errors.



For more information, see [Use dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-features).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
