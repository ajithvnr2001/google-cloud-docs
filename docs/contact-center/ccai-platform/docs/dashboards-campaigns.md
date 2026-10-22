---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-campaigns/
title: Campaigns dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:46.307910+00:00
---

# Campaigns dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-campaigns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Campaigns dashboard Stay organized with collections  Save and categorize content based on your preferences. 

With the **Campaigns** dashboard, get real-time and historical performance metrics for call campaigns, including call outcomes, campaign volumes, and agent metrics. Managers can use this information to monitor call campaigns and make data-driven decisions to improve campaign performance.

## Use the dashboard

To use the dashboard, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Campaigns**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range. To do this, follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

If you select a date range that includes historical data (anything other than **Today**), the dashboard displays call data only for calls that are completed.

     * Specify a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can enter your date range or click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Campaign Mode** : Filter by campaign dialer mode.

     * **Queue Name** : Filter by the queue that the campaign is associated with.

     * **Language** : Filter by the language assigned to the queue.

     * **Campaign ID** : Filter by the campaign ID.

     * **Campaign Status Outcome** : Filter by the status of the campaign.

     * **Agent Name** : Filter by agent name.

     * **Agent ID** : Filter by agent ID.

     * **Agent Email** : Filter by an agent's email address.

     * **Custom Agent ID** : Filter by an agent's custom ID.

     * **Agent Location** : Filter by agent location.

  5. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

This dashboard contains the following metrics tiles:

  * **Success Rate** : the percentage of calls that ended in `Finished` status

  * **Campaign Volume** : the total number of calls attempted in the campaign

  * **Calls Answered by Customers** : the number of calls that ended in `Finished` status

  * **Total Failed** : the number of failed calls

  * **Call Status Outcomes** : a bar chart that displays how calls concluded, by call status

  * **Live Calls** : the number of calls that are in progress. This tile displays data only if the **Date** filter is set to **Today**.

  * **Campaign Volume Remaining** : the number of calls in the campaign that haven't been attempted yet

  * **Total Abandons** : the number of calls that were abandoned by the customer before connecting to an agent

  * **Voicemail Hung Up** : the number of calls that ended after reaching voicemail

  * **Disposition Breakdown** : a chart that displays the breakdown of completed calls by the disposition assigned to each call

  * **Avg BCW** (average before contact work): the average amount of time that agents spent acknowledging contact details in the CRM before their calls were connected

  * **Avg Hold Time** : the average amount of time that customers were on hold

  * **Avg Handle Time** : the average amount of handle time for all calls. Handle time starts when an agent accepts a call and ends when they finish wrap-up. Average handle time = (before contact work (BCW) + hold time + talk time + wrap-up time) / total handled calls.

  * **Avg Talk Time** : the average amount of time that agents spent talking to customers. This excludes before contact work (BCW), hold time, talk time, and wrap-up time.

  * **Avg Wrap-Up Time** : the average amount of time that agents spent in `Wrap-up` status

  * **Avg Attempts Until Consumer Reached** : the average number of call attempts that were required to reach a customer




## Tables

This dashboard contains the following metrics table. Hold the pointer over the column headings to see their descriptions.

  * **Historical** : displays performance metrics for historical call campaigns



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
