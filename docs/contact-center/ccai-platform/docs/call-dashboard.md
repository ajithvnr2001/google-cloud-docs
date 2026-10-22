---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-dashboard/
title: Call dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:21.232236+00:00
---

# Call dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call dashboard Stay organized with collections  Save and categorize content based on your preferences. 

For the **Agents Logged In** tile, agent information will not appear until the following:

  * Agents have to have taken a call or chat to show up in the dashboard as logged in agent
  * Agents have to be assigned the default Agent role even if the Custom role they have assigned contains Agent permissions.



The Call dashboard shows both real-time and aggregated data related to your contact center calls. This dashboard is controlled by a group of filters: Queue Group, Queue, Team, and Date. You can also click on certain tiles to see filtered views of the Connected, Queued, or Completed calls pages, as well as the Agent Monitoring page. Shows data from calls coming in from IVR, Mobile SDK, and Web SDK.

## Data refresh rate

The data in the Call dashboard refreshes every 20 seconds.

## View the call dashboard

Go to **Dashboard > Call.**

## Call dashboard metrics

**Note:** Metrics marked with an * are considered LIVE data and are not available when the data filter is used.

  * **Calls:**

    * Includes only inbound call interactions, including scheduled and overcapacity callback calls.

    * Includes all channels (for example, IVR, In-App, In-Web).

    * Excludes short-abandoned calls based on settings in Operation Management.

    * Excludes in-menu abandoned calls.

  * **Call volume chart:** Call interaction volume patterns over time in 15-minute increments.

  * **Filters:**

    * **Queue Group** : Filter by Queue Group.

    * **Queue** :

      * **Language** : If you have multiple languages configured, select the language first, then the queue.

      * **Queue** : For Top-level queues, you can drill down and click **Apply** next to a sub-queue or leaf-queue.

    * **Team** : Filter by user teams. Teams are configured in Settings > Users & Teams.

      * When a top-level team is selected:

        * If the Top-level team is not assigned to a queue, the dashboard will show data aggregated for all of the queues and agents the sub-teams are assigned to.

        * If a top-level team is assigned to a queue, the dashboard will show data aggregated for the queues that the top-level team is assigned to AND all of the queues the sub-teams are assigned to.

      * When a sub-team is selected, the dashboard will show data aggregated for the queues that the team is assigned to.

    * **Date** : Filter by time range. The dashboard shows aggregate data with respect to your computer's time zone. The Date filter does not impact Live metrics (marked with an asterisk, below.) Limited to 90 days of data.

  * **Service Level:** Monitors percentage of calls answered in x amount of seconds. Default and queue level metrics are set in Operations management.

    * When viewing the default view of the dashboard, the globally configured SLA target is displayed.

    * When viewing multiple queues (or a queue group), no target will be displayed when per-queue metrics are set with Queue Level Target Metrics.

  * **Logged in Agent (LIVE)*:** Number of agents logged in broken down by status. Click on the chart to see the Agents in each status.

Agents information will not appear until the following:

    * Agents have to have taken a call or chat to show up in the dashboard as logged in agent

    * Agents have to be assigned the default Agent role even if the custom role they have assigned contains Agent permissions.

  * **Live Call (LIVE)*:** # of calls: ongoing, queued, or in-IVR menu.

  * **Longest Call Waiting (LIVE)*:** Longest ongoing wait time for a call. Calculated with only current queued or ongoing calls and does not include finished calls.

  * **% Transfers:** Percentage of calls that have been transferred. Click on the metrics to see drill-down info.

  * **Volume per Hour:** Average volume of call interactions per hour.

  * **Calls Handled:** Number of finished call interactions. Click on the metrics to see drill-down info.

  * **Average Handle Time:** Average length of interactions [handle time] + [hold time]. Click on the metrics to see drill-down info.

  * **Queue: Most CIQ (LIVE)*:** Queues with highest number of calls waiting to be assigned to an Agent.

  * **Avg Queue Duration:** Average duration a consumer spends waiting for an Agent.

  * **Queues: Longest EWT:** Queues with longest estimated wait time.

  * **Queues: Highest Traffic:** Queues with highest number of interactions in the given time frame, including abandoned and failed calls.

  * **Repeat Contacts:** Number of callers who had multiple incoming sessions that finished in the same queue within the configured repeat contact timeframe set in **Settings > Operation Management > Target Metrics**. Click on the metrics to see more drill-down info.

  * **CSAT:** Average CSAT collected after call sessions.

  * **Status Ratio:** Finished calls broken down by call status broken down by(finished, abandoned, etc).

  * **Voicemail Waiting:** Number of unmanaged voicemails. Only voicemails listened via the Agent Adapter will be marked as read and not counted in this metric.

    * Click **Clear voicemails** to set this metric to 0.
  * **Voicemail Status:** Number of voicemails received broken down by status.

    * **Received** : Number of voicemails received within the filtered time range.

    * **Read** : Voicemails an Agent has listened to via the Agent Adapter.

    * **Waiting** : voicemails received in the last week that have not be listened to via the Agent Adapter.




## Report data versus dashboard data

With so many data points at your fingertips, there is a lot to take in! Below are some guidelines when comparing data across the Contact Center AI Platform (CCAI Platform) real-time and historical reporting features.

  * Reports and dashboards exclude calls abandoned during menu selection.

  * Report data excludes voicemails whereas the call dashboard data includes voicemails.

  * Historical report data generally includes short-abandoned calls, whereas the dashboard may not include this data based on settings in **Settings** > **Operation Management**.

  * Exception for short-abandoned call data if you download a historical report with aggregates of SLA, the short-abandons will not be included in the calculations; however, if you download a raw report of interactions, it will be there.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
