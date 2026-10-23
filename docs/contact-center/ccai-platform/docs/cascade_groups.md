---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cascade_groups/
title: Cascade groups \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:22.232632+00:00
---

# Cascade groups  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cascade_groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Cascade groups Stay organized with collections  Save and categorize content based on your preferences. 

Cascade groups allow multiple sets of teams or agents to answer calls for a specific queue. It also allows for tiered routing by notifying Group 1 first, then the next group or groups sequentially.

If your call isn't answered by one agent or group of agents, you can set up a custom routing configuration to make sure it's taken care of by the right agents. Cascade groups operate the same with human and virtual agents.

## Cascade group behavior

Groups are notified in numerical order. Group 1 will be notified first, then Group 2, then Group 3. Each group in the process will be notified along with previous groups after the time limit selected in **Operation Management** > **Group Settings**. The setting affects the entire environment (all queues and channels).

If a call has moved to the next group but an agent from a higher level group becomes available, the call will always go to the agent in the highest level group. If no agents are available in the first group, the first group is skipped and the call is offered to the second group. If there are no agents assigned to the first group, the group will be skipped until Contact Center AI Platform (CCAI Platform) finds a queue with agents assigned.

Groups of agents receiving notifications will continue to receive them after more groups are notified until the call is answered. The Estimated Wait Time (EWT) is calculated based on all assigned cascade group agents.

When [Scheduled Calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#scheduled_calls) are enabled for a queue with cascade groups, the first available agent from any cascade group will be offered the call if no agents are available to assign a call to.

When cascade groups are used with [Deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#multicast_and_deltacast) routing, the deltacast timer and the cascade group timer start at the same time. The call will only be routed using deltacast for the first attempt and will subsequently alert all agents using multicast until the call is answered.

## Cascade condition

Another option is available to help configure cascade logic to take multiple factors into consideration when determining whether to cascade calls to another group. The configuration can include any or all of the following: SLA, agent availability, and queue length. You can also apply `AND` or `OR` operators to determine how these considerations are made.

  * These settings are available starting with the 2nd cascade group. The 1st cascade group can't have these conditions applied.

  * These selections affect both multicast and deltacast.

  * If a group is protected by a condition, we don't cascade to the deeper groups until the respective cascade time cycle elapses, or the respective timers were skipped because of the **Skip cascade group timer** option.

    * If the **Skip cascade group timer** is on and there are no available agents in a given group, the next group can be checked immediately without waiting for the timer to elapse.
  * For the **Agent availability check** option, agents with the breakthrough status are included as available.

  * The queue assigned to the SLA threshold in cascade condition can't be blank. If an administrator removes a queue assigned as an SLA threshold in **Edit IVR menu structure** , there will be a notification dialog message to inform that this queue is assigned in the SLA threshold settings, so they can either assign a new queue or disable this option as part of the cascade condition settings.




The following table clarifies the expected behavior when different combinations of cascade group settings are enabled in combination with the cascade condition settings.

Settings selected | Expected behavior  
---|---  
Cascade condition = OFF  
Skip cascade group timer = OFF  | Cascading will continue to work as implemented today.  
Cascade condition = OFF  
Skip cascade group timer = ON  |  Skip cascade group timer will operate as it does, without any changes. Check if there are available agents in the next group

  * If yes: cast to the next group
  * If no: open the next group and skip the cascade group timer

  
Cascade condition = ON |  Whenever the cascade group timer elapses for a call/chat, check thresholds for all selected options for cascade condition of the next group.

  * If it passes: ("AND" operator and all options success) or ("OR" operator and at least 1 success): cast the call/chat to agents in that group
  * If it fails: wait for the next cascade group timer to elapse

When cascading to the next group, we also cast (re-check condition) for the previous groups if those groups have conditions.  
Cascade condition = ON  
Agent availability = ON  |  While waiting for the next cascade group timer and when an agent in the previous (open) groups becomes available, check if the available agent count for that group meets or exceeds the threshold and the combined conditions are also met.

  * If yes: cast to that group
  * If no: wait for the next cascade group timer or next agents to be available

  
Cascade condition = ON  
Skip cascade group timer = ON  |  If a call comes in and there is no available agent in Group 1, skip the cascade group timer. Whenever the cascade group timer is skipped:

  1. Check if there are available agents in the next group
  2. If yes, check if the cascade condition for that group meets the set conditions:


  * If yes: cast to the next group
  * If no: start cascade group timer
  * Otherwise, open that group and skip the cascade group timer.

  
  
Cascade group behavior will change depending on the selections made.

## Create groups and assign agents

  1. In the CCAI Platform portal, go to **Settings** > **Queue**.

  2. Under **IVR** , click **Edit / View**.

  3. Select the queue you want to add a cascade group to.

     * Only leaf queues with no sub-queues can use cascade groups.

     * Parent queues cannot use cascade groups.

  4. In the **Settings** panel that appears, scroll to **Channel Settings** and click either **Assign Virtual Agent** or **Assign Human Agent**.

  5. Click **Add New Cascade Group** to create a cascade group. Each time you create a new group, it is added in sequence. Enter the names of agents or teams to add them to the group.

  6. Click **Save**.




## Configure a cascade group globally

To configure a cascade group globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Operation Management**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings** > **Operation Management**.

  2. In the **General** pane, go to **Group Settings**.

  3. Under **Cascade Group** , set the number of seconds after which the next group is offered the call.

**Note:** This value must be greater than highest deltacast timeout value in any of your queues. For more information, see [Multicast and deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#multicast_and_deltacast).
  4. Click **Save General**.




## Configure a cascade group at the queue level

To configure cascade group at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. Depending on the type of queue you are editing, click either **IVR (Interactive Voice Response)** , **Mobile** , or **Web**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane for your queue, go to the **Routing** section, and then click **Configure**.

  5. In the **Cascade Group Timer** section, set the number of seconds after which the next group is offered the call.

**Note:** This value must be greater than highest deltacast timeout value in this queue and any of its child queues. For more information, see [Multicast and deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#multicast_and_deltacast).
  6. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
