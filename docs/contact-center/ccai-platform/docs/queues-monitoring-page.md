---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queues-monitoring-page/
title: Queues monitoring page \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:41.203031+00:00
---

# Queues monitoring page  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queues-monitoring-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queues monitoring page Stay organized with collections  Save and categorize content based on your preferences. 

The Queues page gives CCAI Platform Admins and Managers an overview of queue configurations, a live view of the queue activity, as well as data calculated for the past 24 hours. The data includes all activity for Call and/or Chat Queues that have been set up for the Account.

Columns can be customized to show various details such as the number of Agents and those agents' statuses, queue priority, number of calls, and more. You can also perform important actions by adding agents or viewing call volume.

  * Search and channel toggle

  * Calls breakdown

  * Chat queues breakdown 




## Search and channel toggle

  * **Search Queue** \- In the upper/left there is a Search field where you can enter the Queue Name or a partial Queue Name. This will then only show those Queue(s) to make locating specific queues in large organizations much easier.

  * A **Toggle menu** at the top of the Queues page will allow you to switch between Call and Chat queues




## Call queues breakdown

The default view shows information about all of the various Call Queues that have been set up for IVR, In-app, and In-Web.

You may need to scroll to the bottom of the queue list in order to scroll to the right and view additional columns.

**Customize Columns** \- Adjust which columns are shown in what order. The default column order with descriptions is listed below.

Click on the **Gear Icon** to expand the list of Columns. While the default columns 'Column Name', 'Actions', and 'Queue Groups' are static, all other display order of the other columns can be customized.

  * **Queue Name** \- By default, queues are listed in the order they were created. Click the up/down arrow icon to sort the queue list alphabetically either ascending or descending.

The 'Queue Menu Path' is shown along with the 'Queue Menu'. You can click the downward arrow icon to expand the view to show the various Groups that have been set up for this Queue.

  * **Actions** \- Click the **arrow icon** to expand the menu selection to view the available actions.

    * **View Connected Calls** takes you to **Calls** > **Connected Calls** filtered for that specific queue.

    * **View Queued Calls** takes you to **Calls** > **Queued Calls** filtered for that specific queue.

    * **View Completed Calls** takes you to the **Calls** > **Completed Calls** filtered for that specific queue.

  * **Queue Groups** \- Shows the various Groups that you have set up for the queue.

When the 'Queue Menu path' is expanded you can click the upward arrow icon to expand the selection.

    * **Add agents** \- Assign agents to this queue group directly from this view.

    * **View Connected Calls:** takes you to **Calls** > **Connected Calls** filtered for that specific queue.

    * **View Queued Calls:** takes you to **Calls** > **Queued Calls** filtered for that specific queue.

    * **View Completed Calls:** takes you to **Calls** > **Completed Calls** filtered for that specific queue.

  * **Type:** Shows the type of Queue. There are two types:

    * **Cascade:** for more information see Cascade Groups.

    * **Allocation:** For more information see Percent Allocation Groups.

By default, the Type column is sorted based on the default Queue Name column. To sort, click the up/down arrow icon.

  * **Agents:** shows the agents who have been assigned to the queue and the total number of agents that are:

    * * **Assigned** :* total number of Agents currently assigned the queue.

    * * **Busy** :* total number of agents that are not Available, and are also not currently assigned to a call/chat.

Ex**.** an Agent that has a status of 'Meal' would appear in this count.

    * **_Available:_** total number of agents in this queue that currently have a status of 'Available' and they are ready to take a call/chat.

  * **Queue Priority:** Queue Priorities that have been set up for the various queues and the queue languages. For more information see Queue Priority.

  * **Total Offered:** All Calls currently offered or projected to the Queue.

  * **Total Connected:** Total number of calls currently connected to Agents in this Queue.

  * **Total Offered from Another Group** : Finished calls transferred to this Queue from another group.

  * **Type Breakdown:** Percentage of calls by Type. See all session types here: Session Type Terminology.

  * **StatusBreakdown:** Percentage of calls per Call Status (Completed, Queued, Transferring, etc).

  * **Total Volume:** Total number of Connected, Finished, and Failed calls currently in this queue.

  * **Avg. Volume per Hour:** Calculates the average Connected, Finished, and Failed calls per hour during operation hours.

  * **Avg. CSAT** : Calculates the average of all the CSAT scores for completed calls where a CSAT score was logged.

  * **Lowest CSAT:** Lowest CSAT score that was logged.

  * **Avg. Handle Time:** Average duration of all calls handled by agents in this queue.

  * **Longest Handle Time:** Single highest Handle time logged for this queue.

  * **Avg. Wait Time:** Average time that Callers spent waiting in queue.

  * **Longest Wait Time** : Single longest Wait Time value.

  * **Avg. Hold Time:** Average amount of time that a Caller spent on hold.

  * **Longest Hold Time** : Single longest Hold time.

  * **Repeat Contact:** Number of Callers that called back into this same queue.




## Chat queues breakdown

The Chat columns are the same as the Call columns however there are no "Avg/Longest Hold Times" as these two columns have been replaced with "Average/Longest Response Time."

  * **Average Response Time:** shows the average amount of time that it takes for an agent to respond.

  * **Longest Response Time:** shows the single longest Response time experienced.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
