---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-transfers/
title: Transfers dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:24.235137+00:00
---

# Transfers dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Transfers dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Transfers - Calls** and **Transfers - Chats** dashboards, get an overview of transfer interactions, including queue name, agent name, time spent in third-party interactions, and whether transfers are warm or cold.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Transfers / Calls** or **Transfers / Chats**. The dashboard appears.

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

     * **Start Time** and **End Time**. Get results from only within this time range.

     * **From Queue Name**. Filter by the queue that the contact was transferred from.

     * **To Queue Name**. Filter by the queue that the contact was transferred to.

     * **Call ID** or **Chat ID**. Filter by the session ID.

     * **Location**. Filter by one or more locations.

     * **Interaction Type**. Filter by the type of interaction.

     * **Answered by (To Agent)** (calls only). Filter by the type of agent that answered the call.

     * **From Agent Name** , **From Agent ID** , **From Agent Email** , **From Custom Agent ID** , **To Agent Name** , **To Agent ID** , **To Agent Email** , **To Custom Agent ID**. Filter by the agent that the session was transferred from.

     * **From Agent Name** , **From Agent ID** , **From Agent Email** , **From Custom Agent ID** , **To Agent Name** , **To Agent ID** , **To Agent Email** , **To Custom Agent ID**. Filter by the agent that the session was transferred to.

     * **Transfer Type**. Filter by transfer type.

     * **Direction**. Filter by the direction of the interaction.

  5. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles.

  * **Total Transfers** : the number of interactions that were transferred to another queue or directly to an agent

  * **Queue Interactions** : the number of times that an interaction entered a queue. This includes the first time that the interaction entered a queue and subsequent entries to a queue after the work was accepted by an agent.

  * **Inbound Handled** : the number of inbound interactions handled by an agent. This includes work that an agent receives from a queue and work that was directly allocated to an agent and never entered a queue.

  * **Outbound Handled** : the number of outbound interactions handled by an agent

  * **Total Abandons** : the number of interactions that were abandoned in queue before connecting with an agent

  * **Failed Interactions** : a call or chat that is not successfully connected to an agent or representative. This can occur for reasons such as expired transfer, no answer, or declined by the end-user.

  * **Avg Queue Abandon Time** : the average amount of time, across all queue abandons, that calls waited before disconnecting without being accepted by an agent

  * **Avg Queue Time** : the average amount of time, across all Queued Interactions, that elapsed from when a call or chat entered a queue to when it was accepted by an agent or the caller abandoned.

  * **Queue Interactions Tranferred In (Top 10)** : displays the top 10 queue transfers from highest to lowest




## Tables

These dashboards contains the following metrics tables. Hold the pointer over a table heading to see its description.

  * **Call Transfers** or **Chat Transfers** : displays the metrics for the selected interaction type. Here is additional information about a column heading in this table:

    * **Hold Time (H:M:S)** : the amount of time (in hours, minutes, and seconds) that an agent placed a consumer on hold during an interaction. Hold is recorded in total for a single interaction. An agent that places a consumer on hold multiple times will only show the total hold duration for that interaction. When that agent transfers the call out, this starts a new interaction which tracks its own hold time.
  * **Third Party Interactions** : the metrics for the third party interactions. Here is additional information about column headings in this table:

    * **Agent Name** : the name of the last agent assigned to the chat. If the chat was transferred, this shows only the last agent assigned.

    * **Interaction Type** : the type of interaction

      * **Call Types** :

        * Voice Inbound: Standard PSTN calls

        * Voice Inbound (IVR by Mobile): Fallback PSTN calls made from the Mobile SDK

        * Voice Inbound (Mobile): Placed by end-users through an installed Mobile SDK

        * Voice Callback (Web): Initiated from the Web SDK

        * Voice Inbound (API): Initiated through the API

        * Voice Scheduled (Mobile): Scheduled through an installed Mobile SDK

        * Voice Scheduled (Web): Scheduled through an installed Web SDK

        * Voice Outbound: Initiated by an Agent by dialing a number

        * Voice Outbound (API): Initiated through the API

        * Voice Campaign: Initiated through an Outbound Dialer (Campaign)

        * Voice Internal (Inbound Call): Agent to agent call. This call type is available in session data and dashboard data.

      * **Chat Types** :

        * Messaging (Whatsapp): Initiated through Whatsapp.

        * Messaging Inbound (SMS)

        * Messaging Outbound (SMS)

        * Messaging Outbound (SMS through the API)

        * Messaging (Web): Initiated through an installed Web SDK.

        * Messaging (Mobile): Initiated through an installed Mobile SDK.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
