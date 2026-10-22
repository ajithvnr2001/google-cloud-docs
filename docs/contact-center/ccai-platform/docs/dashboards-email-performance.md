---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-email-performance/
title: Email dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:54.035982+00:00
---

# Email dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-email-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Email dashboard Stay organized with collections  Save and categorize content based on your preferences. 

With the **Email** dashboard, get insights into email operations with metrics like sessions completed, sessions unopened, and average first time to respond.

## Email terminology

Here are some key terms for the email dashboard:

  * **Session** : a session is synonymous with an email thread. It is composed of one or more interactions

  * **Interaction** : a single email message within a session. This can be a message from the end-user to the agent, or a message from the agent to the end-user




## Use the dashboard

To use the dashboard, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Email**. The dashboard appears.

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

     * **Email In-box Address** : by the email inbox address

     * **Queue Name** : by the queue name

  5. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

This dashboard contains the following metrics tiles:

  * **Total Sessions** : the total number of sessions
  * **Sessions Unopened** : the number of sessions that have not been opened yet
  * **Sessions Paused** : the number of emails that are in the `Paused` status. An agent can apply this status to an email session with an unresponsive end-user. This status is automatically applied to an email session with no activity for email exchange for 10 consecutive days.
  * **Sessions Completed** : the number of sessions that have been closed or resolved
  * **Sessions Assigned** : the number of sessions that are assigned to an agent
  * **Sessions Un-assigned** : the number of sessions that are not assigned to an agent
  * **Avg Time to First Response** : the average time until the first response to an email. Sessions can consist of multiple interactions, but this measures only the first response from the agent.
  * **Avg Handle Time** : the average handle time across all interactions within a session 



## Tables

This dashboard contains the following metrics table. Hold the pointer over a table heading to see its description.

  * **Interactions Detail** : data about email interactions

  * **Queue Transfers Detail** : email transfer information at the instance, queue, and session levels




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
