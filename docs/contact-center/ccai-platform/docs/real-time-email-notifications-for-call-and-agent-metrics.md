---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/real-time-email-notifications-for-call-and-agent-metrics/
title: Real-Time email notifications for call and agent metrics \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:59.892589+00:00
---

# Real-Time email notifications for call and agent metrics  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/real-time-email-notifications-for-call-and-agent-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Real-Time email notifications for call and agent metrics Stay organized with collections  Save and categorize content based on your preferences. 

To help support your Real-Time Management operation, you can actively track metrics and send you and your team email notifications. Multiple notifications rules can run at any given time and alert you without needing to actively watch dashboard metrics.

## Feature specifics

  * Notifications cover agent status durations and call queue data

  * Chat queues are currently not supported

  * Notification time frame: when a given event occurs once, or more, within the specified time frame, a single notification for that event is sent when it first occurs. Example below:

    * If a notification is set to trigger when agent John Doe is in Break status for more than 30 min within a 4-hour time frame, as soon as John Doe's break time exceeds 30 minutes a notification is sent.

    * If the agent exceeds 30 minutes in Break status again within 4 hours no additional notification is sent.

    * If the agent takes another break longer than 30 min, 5 hours after the first one, a new notification would be sent.




## Example notification rules

  * Exceeding 15 minutes in Break status for an agent or team of agents in an 8-hour time frame

  * A queue exceeds an average wait time of 5 minutes

  * The average CSAT for your operation is 4 or lower in a 4-hour timeframe




## Create new notification rules

  1. Click on the **bell icon** , then click on **View all Notification Rules**.

  2. Click **Add New Notification Rule.**

  3. Choose if you want the rule to be for all (any) agents, teams, or queues in your environment, or a specific agent, queue, or team.

  4. Select the **Metric**. Options vary based on the target metric to watch:

     * **Agent**

       * Average CSAT

       * Available Time

       * Unavailable Time

       * Break Time

       * Meal Time

       * Special Task Time

     * **Team**

       * Average CSAT

       * Average Call Duration

     * **Queue**

       * Average CSAT

       * Average Call Duration

       * Average Wait Time

  5. Choose the **Operator** (>, <, =<, or =>), and **Value** (time frame or CSAT stars) to monitor.

  6. Select or enter which users should receive an email if the set threshold is reached in the given time frame.

     1. **Myself** : sends an email to the email associated with the currently logged in account

     2. **Specific** : Enter the specific Manager/Admin names, or team names

     3. **All Managers and Admins** : All users with the manager and Admin roles

  7. Click **Apply Rules** to save.




## Edit existing notification rules

  1. Click on the **bell icon** in the top bar, then click on **View all Notification Rules.**

  2. Locate the rule you would like to edit and click on the **edit** (pencil) icon.

  3. Make updates to the rule settings.

  4. Click **Apply Rules** to save.




## Delete existing rules

  1. Click on the **bell icon** , then click on **View all Notification Rules**.

  2. Locate the rule you would like to delete and click on the **X** at the end of the row.

  3. Confirm by clicking **OK** on the confirmation pop-up.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
