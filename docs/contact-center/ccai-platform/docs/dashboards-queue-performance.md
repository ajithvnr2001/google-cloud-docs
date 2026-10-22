---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-performance/
title: Queue Performance dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:33.815282+00:00
---

# Queue Performance dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue Performance dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Queue Performance - Calls** and **Queue Performance - Chats** dashboards, get performance metrics by queue for your call and chat sessions. This includes queue interaction volume, abandons, handle time, callbacks, sentiment, and CSAT.

Data appears only for capabilities enabled on your instance. For example, **Consumer phone number** values appear only if the legal addendum for viewing customer phone numbers has been signed for your account.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Queue Performance**. The **Queue Performance / Calls** dashboard appears.

  2. To view the **Queue Performance / Chats** dashboard, click the **Chats** tab.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Queue Name**. Filter by queue name.

     * **Child Queues**. Specify whether to include child queues.

     * **Queue Group**. Filter by queue group.

     * **Language**. Filter by the language assigned to the queue.

     * **Location**. Filter by one or multiple locations.

     * **Direction** (chats only). Filter by the direction of the session.

     * **Call ID** (calls only). Filter by call ID.

     * **Chat ID** (chats only). Filter by chat ID.

     * **Interaction Type**. Filter by interaction type.

     * **Disposition Code**. Filter by disposition code.

     * **Consumer Phone Number** (calls only). Filter by the phone number that the user used to call in.

     * **VA Escalation in Queue** (calls only). Filter by whether there was a virtual agent escalation in the queue.

     * **Support Phone Number** (calls only). Filter by the support phone number.

  5. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Reload**.




## Tiles

These dashboards contain the following metrics tiles:

  * **SLA %** : the percentage of interactions that an agent started within the SLA threshold that you configured

  * **Total Queue Interactions** : the number of interactions that were waiting in queue to be connected to an agent

  * **Total Queue Abandons** : the number of interactions that were waiting in queue and abandoned before being connected to an agent

  * **Avg Queue Abandon Time** : the average time a user waited in queue before abandoning the interaction

  * **Abandonment Rate %** : the percentage of interactions users abandoned in the queue over the specified time period

  * **Average Handle Time** : the average time from when agents were assigned a call to when they completed wrap-up

  * **Sentiment Score** : a quantitative measure of the emotional tone and subjective opinion conveyed in a customer interaction

  * **CSAT** : the average customer satisfaction score awarded by users in the specified time period

  * **Total Failed** : the total number of failed interactions

  * **Total Queue Answered** (calls only): the total number of calls answered in the queue

  * **Total VA In-Queue Interactions** (calls only): the number of calls where virtual agents were active while end-users were in a queue

  * **Avg VA In-Queue Time** (calls only): the average time that virtual agents were active while end-users were in a queue

  * **Total VA In-Queue Time** (calls only): the total time that virtual agents were active while end-users were in a queue

  * **Total Callbacks Completed** (calls only): the number of callbacks completed

  * **Total Rolled Over Completed Callbacks** (calls only): the number of rolled-over completed callbacks

  * **Total Rolled Over Pending Callbacks** (calls only): the number of rolled-over pending callbacks




## Tables

These dashboards contain the following metrics tables. Hold the pointer over a` column heading to see its description.

  * **Queue Summary Table** : session metrics summary

  * **Queue Detailed Table** : session interaction details. To access a call recording from your CRM, click a link in the **Call ID** column. To access a chat transcript from your CRM, click a link in the **Chat ID** column.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
