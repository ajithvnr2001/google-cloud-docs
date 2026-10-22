---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/percent_allocation_groups/
title: Configure percent allocation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:30.826877+00:00
---

# Configure percent allocation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/percent_allocation_groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure percent allocation Stay organized with collections  Save and categorize content based on your preferences. 

You can distribute incoming contacts to allocation groups based on percentages that you specify. For example, you might have multiple contact centers or teams that have varying levels of expertise. Using allocation groups, you could specify that team 1 gets 60% of incoming calls for a queue, while team 2 gets 40% of incoming calls for that queue. Another use case for allocation groups is directing a contractually mandated amount of traffic to a third-party support team.

You can configure a timer for how long an incoming contact can sit in an allocation group of a queue. If the timer expires and the incoming contact remains unanswered, then the incoming contact becomes available to all allocation groups of the queue. You can apply timers globally or at the queue level.

## Configure allocation groups

To configure allocation groups, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click **Edit / View** for **IVR (Interactive Voice Response)** , **Mobile** , or **Web** , depending on the channel you want.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to **Channel Settings**.

  5. For **Human Agents** , click **Edit Human Agent Assignments**.

  6. Click **Percent Allocation Group**

  7. To configure **Allocation Group 1** , do the following:

     1. For **Allocation Group 1** , enter the percentage of incoming contacts that you want to allocate to this group.

     2. To add the teams or agents that you want in this group, follow these steps:

        1. In the **Enter agent or team name** field, enter a team or an agent that you want in this group. As you type, a list of valid team names or agent names appears.

        2. Click the team or agent that you want. The team or agent that you click resolves in the field.

        3. Optional: To add more teams or agents, repeat these steps.

  8. To add **Allocation Group 2** , do the following:

     1. Click **Add New Allocation Group**.

     2. For **Allocation Group 2** , enter the percentage of incoming contacts that you want to allocate to this group.

     3. To add the teams or agents that you want in this group, follow these steps:

        1. In the **Enter agent or team name** field, enter a team or an agent that you want in this group. As you type, a list of valid team names or agent names appears.

        2. Click the team or agent that you want. The team or agent that you click resolves in the field.

        3. Optional: To add more teams or agents, repeat these steps.

     4. Optional: to add more allocation groups, repeat these steps.

  9. Click **Save**.




## Set an allocation group timer globally

To set an allocation group timer globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **Group Settings**.

  3. Click the **Percent Allocation Group** toggle to the on position.

  4. Under **Percent Allocation Group** , set the number of seconds after which all groups are offered the call.

  5. Click **Save General**.




## Set an allocation group timer at the queue level

To set an allocation group timer at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. Depending on the type of queue you are editing, click either **IVR (Interactive Voice Response)** , **Mobile** , or **Web**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane for your queue, go to the **Routing** section, and then click **Configure**.

  5. Click the **Percent Allocation Group Timer** toggle to the on position.

  6. Under **Percent Allocation Group Timer** , set the number of seconds after which all groups are offered the call.

  7. Click **Save**.




## Routing details

Call routing rules apply to groups first based on percentages that you set.

Example: Two groups are set up for a queue, Group 1 (60%) and Group 2 (40%).

  * 60% of calls will be routed to Group 1.

  * 40% of calls will be routed to Group 2.




Percent allocation is the first leg of the call routing journey. After a group is chosen based on the percent, then calls are routed using the Deltacast and Multicast settings you have configured.

### After percent allocation

Depending on your call routing settings, the following might take place after the initial percent allocation of incoming traffic occurs:

**Example 1** : _Deltacast Timeout_ is before the _Percent Allocation_ timeout.

  * The call gets routed to the longest-idle agent in the chosen group (Deltacast)

  * If the agent does not pick up the call before the assigned Deltacast timeout the call will stay in the Deltacast queue and broadcast to the rest of the selected group for the duration of the percent allocation timer.

  * If none of the agents from the selected group pick up the call and the setting is enabled, the call will then be Multicast to all groups.




**Example 2** : _Deltacast Timeout_ is after the _Percent Allocation_ timeout.

  * The call gets routed to the longest-idle agent in the chosen group (Deltacast).

  * If the agent does not pick up the call before the assigned Deltacast timeout set in Operation Management it will stay in the Deltacast queue and broadcast to the longest idle agent of each group assigned to the queue for the duration of the Deltacast timer.

  * If none of the Deltacast agents from the assigned groups pick up the call, the call will be Multicast to all members of all groups.




**Example 3** : Deltacast is not enabled.

  * The call will be Multicast to all agents assigned to the selected group.

  * If none of the agents pick up the call before the configured timeout, the call is then broadcast to all members of all assigned groups.




**Example 4** : **Percent Allocation > Routing Options** is not enabled.

  * The call gets Deltacast or Multicast as configured within the assigned group.

  * The call is not broadcast to any other groups assigned to the queue.


**Note:** If an agent is assigned to multiple groups in the same queue, they will receive calls based on the highest priority group they are a member of.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
