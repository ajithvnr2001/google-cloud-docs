---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-groups/
title: Queue Groups \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:37.472889+00:00
---

# Queue Groups  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue Groups Stay organized with collections  Save and categorize content based on your preferences. 

Queue Groups allow you to organize queues. Use this function to group together related queues, such as those handled by the same BPO, market, or supervisor.

You can then **view data** specific to a Queue Group in real-time reporting. On the Call and Chat Dashboards as well as the Agent Monitoring page, you can filter by Queue Groups.

## Queue Groups configuration details

  * Consist of a collection of top-level, sub-queues, and leaf-level/end-queues

  * Be created by any user that has the Report Configuration permission assigned

  * Once a queue group is created, all CCAI Platform users with access will see all queue groups

  * Queue groups can be edited after they are created both the name, queue assignments and assigned _Productive Agents_

  * Can **only contain either call or chat queues** , the two types cannot be combined.




## Add a Queue Group

The following steps enable a queue group to be created:

**Important:** Queue groups must be configured before they are accessible for reporting.

  1. In the CCAI Platform portal, go to **Settings** > **Queue Group Settings**.

  2. Click **Add Queue Group**.

  3. Enter a name in `Enter Queue Group Name`

  4. Set the Queue Group to **On**.

Queue Groups that are **off** will not display in reporting.

  5. Select a Channel: **Call** or **Chat**.

**Note:** A Queue Group can only be used for one session type.
  6. Add the queue you would like to add to your Queue Group by searching in the **Add Queue**.




`. Select **Show Productive Agents**. _(Optional)_ See productive agents explanation.
    
    
    If checked, the **number of Productive Agents** will display on the
    Queue Reports dashboard.
    

  1. You can configure which statuses are considered productive by clicking on the gear icon.

![product status configuration](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632c99ccc3b69.png)

Statuses configured to be _productive_ will have extra visibility on the Queue Groups dashboard.

  2. Click **Save**.




### Productive Agents

Productive Agent statuses can be configured for each Queue Group and give added visibility to the selected Agent statuses. When a status is marked as Productive, a detailed breakdown showing these statuses will be available on the [Queue Report dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-reports-dashboard).

Productive agents are represented in a column in the Queue Report dashboard. To see the breakdown of the agents in each productive status, hold the pointer over the value in the dashboard.

## Edit a Queue Group

Click the **pencil icon** next to the Queue Group you want to edit in the Queue Group overview.

## Viewing in Monitoring and Reporting

In Real-time reporting, you can view data specific to a Queue Group. You can filter by Queue Groups on the Call and Chat Dashboards, as well as the Agent Monitoring page.

**Note:** **Queue Groups** must be configured before they are accessible for reporting.

## Filter by Queue Group on Call and Chat Dashboard

  1. In the CCAI Platform portal, go to **Dashboards > Call** or alternatively **Dashboards > Chat**.

  2. Filter by available **Queue Groups**.

  3. Click the gear icon to go to **Queue Groups Settings** to add or edit a queue group.




## Filter by queue group on Agent Monitoring Page

  1. In the CCAI Platform portal, go to **Agents**.

  2. Expand the **Filter Settings** by clicking on the drop-down arrow next to the name.

  3. Select **\+ Add Filters**.




![Add filters display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632c99ccc4b16.png)

  1. Select **Queue Groups**.

  2. Click **Save**.




## Group global settings

Group settings let you further customize call and chat routing to queues. You can configure the behavior of group settings for both chat and calls.

To configure group settings, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Operation Management**.

  2. In the **General pane** , go to **Flexible Accounts/Records Assignment**.

  3. For **Group Settings** , click the **Percent Allocation Group** toggle to the on position.

  4. For **Percent Allocation Group** , configure the pick up time limit in seconds.

  5. For **Cascade Group** , configure the pick up time limite in seconds.

  6. Click **Save General**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
