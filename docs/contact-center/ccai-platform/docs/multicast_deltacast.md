---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast/
title: Multicast and deltacast \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:23.438992+00:00
---

# Multicast and deltacast  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Multicast and deltacast Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) offers multiple features that let you automate call and chat routing between agents and end-users. Routing can decrease end-user wait times and increase agent efficiency.

  * Multicast is the default routing configuration for all _sessions_ , which are communications between an agent and an end-user. Multicast routes sessions to agents assigned to a specified queue. Each has an equal opportunity to answer, and the quickest to respond will get the call or chat.

  * Deltacast is an intelligent routing system unique to CCAI Platform that uses logic to disperse calls to individual agents, rather than giving agents the same opportunity to answer.




## Deltacast for calls

If enabled, deltacast extends to the following:

  * Transfers
  * Scheduled calls
  * Calls routed using Direct Access Points (DAPs)
  * Queues with cascade groups enabled
  * Queues with percent allocation groups



This section outlines deltacast routing logic and describes how to enable this feature.

### Missed call status

The _Missed Call_ agent status is used for sessions with deltacast enabled. Missed calls are deltacast calls that are routed to an agent and not answered within the Deltacast Timeout time threshold. Missed multicast calls don't put an agent in Missed Call status.

If an agent is placed in Missed Call status, they won't be able to receive new calls until either they or an Admin manually change their status back to Available. Admins can see a count of agents in Missed Call status in the Call Dashboard, Agent page, and in reporting. Agent status and activity information is also available using the API. To be placed in Missed Call status, the agent must have been in Available status. If they are in any other status, Missed Call will still show in reporting but not in the agent adapter.

Missed Call status is independent of the Missed Chat threshold. Calls are not projected to agents in Missed Call status; they are only routed to agents in Available or In-chat status.

### Deltacast routing logic for calls

  1. An incoming call is routed to the agent in status Available with the longest duration since they last ended a call.

**Note:** This is reset each time you sign in. If you sign in multiple times within a thirty-minute period, only the first sign-in causes a reset.
  2. If the agent does not answer within the time set in the deltacast timeout setting:

     * If there are remaining deltacast attempt counts for the call, the call is routed to an available agent with the next longest duration.

     * If the deltacast attempt count has run out, the call is routed using multicast to the rest of the agents assigned to that queue menu option.

  3. If a call or chat offer is sent to an agent and it times out, is skipped, or is canceled before they respond, that also resets their timer — even though the agent never actually handled the interaction.




#### If cascade groups are also being used

  1. If a deltacast call is routed to an agent and the agent does not answer within the time set in the deltacast timeout setting:

     1. When deltacast attempt counts remain for the call, it's routed to an available agent with the next longest duration.

     2. When the deltacast attempt count runs out, the call is multicast to all agents assigned to Cascade Group 1.

  2. If the multicast call to Cascade Group 1 remains unanswered in the set amount of seconds, the call is multicast to all of the agents assigned to Cascade Group 1 and Cascade Group 2.

  3. If the multicast call being offered to Groups 1 & 2 is still unanswered in the set amount of seconds, the call is offered using multicast to all agents assigned to Cascade Group 1, Group 2, and Group 3.

  4. Multicast continues to offer the call to successive cascade groups until an agent accepts the call.




#### If auto answer is also being used

An incoming call is routed, using deltacast, to the agent in Available status with the longest duration since they last ended a call. Auto answer immediately connects the call to the agent. The agent is notified with a tone and their call adapter begins the 3-2-1 countdown.

The following diagram shows the deltacast routing flow:

### Turn on deltacast for calls globally

This section shows you how to switch from the default multicast routing to deltacast routing. Global deltacast settings are inherited by all eligible queues, unless you change them at the queue level. You are not required to turn on deltacast globally to turn it on for individual queues. For more information, see Turn on deltacast for calls at the queue level.

To turn on deltacast for calls globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**. The **Operation Management** page displays.

  2. Go to the **Routing** pane.

  3. Under **Call Routing** , select **Deltacast**. The following configuration settings appear:

     * **Auto Answer** : connects incoming calls with an agent without clicking to answer. For more information, see [Turn on auto answer for calls globally](https://docs.cloud.google.com/contact-center/ccai-platform/docs/auto_answer#turn-on-auto-answer-for-calls-globally).
     * **Deltacast Attempt Count** : the number of times deltacast should offer an incoming call to a single, eligible agent before switching to multicast. 
       * **Disable Multicast fallback after all Deltacast attempts** : Select this checkbox to disable multicast fallback after all deltacast attempts. The system only uses deltacast attempts to find an agent. If no agent accepts the deltacast, the call isn't multicasted to all available agents. Instead, it follows your settings for cascade groups or overcapacity deflection. All other deltacast rules, such as maximum queue time, remain in effect.
     * **Deltacast Timeout for calls** : the amount of time, in seconds, that an agent has to pick up a call before it is offered to the next agent or queue. You can configure different time thresholds for agents working at a computer and agents using [twinning](https://docs.cloud.google.com/contact-center/ccai-platform/docs/twinning#twinning-call) to answer calls on a mobile phone. Agents answering on a mobile phone might need more time to answer than agents working at a computer.
     * **Missed Call Threshold** : set the number of consecutive calls that an agent can miss (that is, not pick up within the timeout threshold) before they are placed in [missed call status](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#missed-call-status).
     * **Unresponsive Threshold** : set the number of times that a call is unable to reach an agent's agent adapter before the agent is placed in `Unresponsive` status. 
       * Optional: Select the **Apply unresponsive thresholds when agent is in an active chat or call session** checkbox to apply the unresponsive threshold count to agents that become unresponsive during an active session.
     * **Cascade Timer selection** : select this checkbox to skip the cascade group timer if no agents are available in the cascade group.
  4. Configure your deltacast settings, and then click **Save routing**.




### Turn on deltacast for calls at the queue level

Deltacast settings for queues are automatically inherited from the global settings unless you change them for individual queues. You don't need to turn on deltacast globally to turn it on for specific queues.

To turn on deltacast for calls at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.

  2. Depending on the type of queue that you want to edit, click **Edit / View** in either the **IVR (Interactive Voice Response)** , **Mobile** , or **Web** pane.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Routing** section. Under **Routing** , each routing capability is marked with either a **Global** or a **Queue** label. These labels indicate whether this capability is configured globally or at the queue level.

  5. Click **Configure**.

  6. In the **Routing** pane, go to the **Call Routing** section, and then click **Deltacast**. The following configuration settings appear:

     * **Auto Answer** : connects incoming calls with an agent without clicking to answer. For more information, see [Turn on auto answer for calls at the queue level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/auto_answer#turn-on-auto-answer-for-calls-at-the-queue-level).
     * **Deltacast Attempt Count** : the number of times deltacast should offer an incoming call to a single, eligible agent before switching to multicast. 
       * **Disable Multicast fallback after all Deltacast attempts** : Select this checkbox to disable multicast fallback after all deltacast attempts. The system only uses deltacast attempts to find an agent. If no agent accepts the deltacast, the call isn't multicasted to all available agents. Instead, it follows your settings for cascade groups or overcapacity deflection. All other deltacast rules, such as maximum queue time, remain in effect.
     * **Deltacast Timeout for calls** : the amount of time, in seconds, that an agent has to pick up a call before it is offered to the next agent or queue. You can configure different time thresholds for agents working at a computer and agents using [twinning](https://docs.cloud.google.com/contact-center/ccai-platform/docs/twinning#twinning-call) to answer calls on a mobile phone. Agents answering on a mobile phone might need more time to answer than agents working at a computer.
     * **Missed Call Threshold** : set the number of consecutive calls that an agent can miss (that is, not pick up within the timeout threshold) before they are placed in [missed call status](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#missed-call-status).
     * **Unresponsive Threshold** : set the number of times that a call is unable to reach an agent's agent adapter before the agent is placed in `Unresponsive` status. 
       * Optional: Select the **Apply unresponsive thresholds when agent is in an active chat or call session** checkbox to apply the unresponsive threshold count to agents that become unresponsive during an active session.
     * **Cascade Timer selection** : select this checkbox to skip the cascade group timer if no agents are available in the cascade group.
  7. Configure your deltacast settings, and then click **Save**.




### Optional: Skip cascade group timer

The **skip cascade group timer** capabilities let you bypass the cascade timer settings and route a call or chat to the next available agent, regardless of your cascade group. With this feature enabled, the call is routed to agents immediately if they are available in the next cascade group.

When disabled, the platform will adhere to the cascade timer settings and wait for the specified time before proceeding to the next group.

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management** > **Routing**.

  2. Under **Cascade Timer selection** , select the **Skip Cascade Group Timer** checkbox. By default, this checkbox is unchecked.

  3. Click **Save Routing**.




### Monitoring and reporting for calls

Admins and managers can see agents in Missed Call status in the **Logged in agent** section of the call dashboard. Agents in Missed Call status are also visible on the **Settings > Agents > Agent** page. You can click the **Filter Settings** menu on this page to filter on agent status.

#### View deltacast and multicast call data

All notifications offered, pickup attempts, and successfully answered calls are logged and can be viewed in reports and reporting APIs. The following reports are available:

  * Agent Activity - Summary Report

  * Agent Activity - Timeline Report




To download a report, follow these steps:

  1. Go to **Reports > Agents & Teams**.

  2. Choose an agent or team for which you want to see data.

  3. Under **Select Session Type** , select **Calls**.

  4. Under **Select Reports Desired** , select the report type(s) that you want.

  5. Select the **Timeframe** and **Timezone**.

  6. Click **Download**. Deltacast metrics are labeled in the downloaded report.




## Deltacast for chat

If enabled, deltacast extends to every channel and every queue that uses chat. It applies to all chat types and the following chat flows:

  * Transfers
  * Chats routed through Direct Access Points (DAPs)
  * Queues with cascade groups enabled
  * Queues with percent allocation groups enabled



### Eligible agents

To receive a deltacast call, an agent must fulfill one of following requirements:

  * Status is set to Available.

  * Status is In-chat and the agent has not reached the chat concurrency threshold.

    * Chat concurrency is configured globally in **Settings > Chat** and individually in **Settings > Users & Teams > Edit a user (pencil icon)**.
    * If the agent is assigned to both chat and call sessions, a call counts as one chat toward the chat threshold.



### Missed chat status

The agent status Missed Chat is used for sessions with Deltacast enabled. Missed chats are defined as Deltacast chats routed to an agent and not answered within the _Deltacast Timeout_ time threshold. Missed Multicast chats don't count toward Missed Chat.

If an agent is placed in Missed Chat status, they won't be able to receive new chats until either they or an Admin manually change their status back to Available. Admins can see a count of agents in Missed Chat status in the Chat Dashboard, Agent page, and in reporting. Agent status and activity information is also available using the API. To be placed in Missed Chat status, the agent must have been in Available status. If they are in any other status, Missed Chat still shows in reporting but not in the agent adapter.

Missed Chat status is independent of the Missed Call threshold. Chats are not projected to agents in Missed Chat status; they are only routed to agents in Available or In-chat status.

### Deltacast routing logic for chat

Deltacast routing logic determines which eligible agent is selected each time deltacast offers a chat.

#### Basic routing without queue groups

When a chat enters the queue, deltacast routes it as follows:

  1. The chat is offered to one eligible agent. The system chooses the agent based on one of the following routing options:

     * **Longest idle routing**. Distributes workload equally among agents.

     * **Fewest agents routing**. Maximizes utilization and call availability. This option routes chats to agents who already have chats, without exceeding concurrency limits. This keeps more agents available for calls or other work.

  2. If the agent doesn't answer the chat within the configured deltacast timeout for chats, one of the following occurs:

     * If deltacast attempt counts remain, the chat is routed to the next eligible agent based on the same routing logic.

     * If no attempt counts remain, the chat is offered using multicast to all eligible agents assigned to that queue.




##### Longest idle routing

Longest idle routing distributes workload more evenly. The routing behavior is as follows:

  * If multiple agents are available, the system routes the chat to the agent with the longest duration since they were last in a chat.

  * If all assigned agents are in a call or a chat, the system routes the chat to the agent who has the fewest concurrent chats. If an agent is on a call, the call counts as the number of chats specified by the administrator.

  * If multiple agents have the same number of concurrent chats, the system routes the chat to the agent with the longest duration since they received or were offered a chat.


**Note:** This is reset each time you sign in. If you sign in multiple times within a thirty-minute period, only the first sign-in causes a reset.

##### Fewest agents routing

Fewest agents routing concentrates chats on agents who are already handling chats, while respecting concurrency thresholds. The routing behavior is as follows:

  * The system prefers routing to eligible agents who are already in a chat and under their maximum chat threshold.

  * Among those agents, the system prioritizes agents who have a higher number of concurrent chats, so fewer agents are used overall.

  * If no eligible agents are available, or if they are all at the maximum chat threshold, routing falls back to normal eligibility—for example, choosing among available agents.




**Important** : Fewest agents routing changes which agent is selected. Other deltacast mechanics, such as attempts, timeout, fallback to multicast, and the missed chat threshold, remain the same.

#### Routing with cascade groups

Routing with cascade groups works as follows:

  1. The chat is offered to an eligible agent in Cascade Group A for the duration of the **Deltacast Timeout for Chats** timer. If it isn't answered:

     1. If there are remaining deltacast attempt counts for the chat, the chat is routed to an eligible agent with the next longest duration.

     2. If the deltacast attempt count has run out, then the chat is offered using multicast to all agents in Cascade Group A, both in Available and In-chat statuses, including the original agent routed the chat (if they did not reach the Missed Chat threshold).

  2. If no agents pick up the chat and the cascade group timer expires: The chat is offered using multicast to all agents in Cascade Group A in either Available and In-Chat status, including the original agent routed the chat.

  3. If no agents pick up the chat and the cascade group timer expires: The chat is offered using multicast to all eligible agents in Cascade Group B, and continues to offer the chat using multicast to all eligible agents in Cascade Group A.

  4. If the cascade group timer expires, and Group B is the last group: The chat continues to be routed using multicast until the unanswered chat expiration timer expires, as set in **Settings > Chat**.




#### Routing with auto answer enabled

When auto answer is enabled, incoming chats are routed using deltacast to an eligible agent using the previously described routing logic. Auto answer starts the chat in the agent adapter. The agent hears a tone, and the **New Chat** tab flashes red.

### Turn on deltacast for chat globally

This section shows you how to switch from the default multicast routing to deltacast routing. Global deltacast settings are inherited by all eligible queues, unless you change them at the queue level. You are not required to turn on deltacast globally to turn it on for individual queues. For more information, see Turn on deltacast for chat at the queue level.

To turn on deltacast for chat globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Routing** pane.

  3. In the **Chat Routing** section, select **Deltacast**. The deltacast settings appear.

  4. To automatically connect chats to agents without clicking to answer (for queues with deltacast enabled), click the **Auto Answer** toggle to the on position.

  5. In the **Deltacast Attempt Count** section, set the number of times deltacast should offer an incoming chat to a single, eligible agent before switching to multicast.

     * Optional: Select the **Disable Multicast fallback after all Deltacast attempts** checkbox to prevent routing to multicast.
  6. In the **Deltacast Routing Logic** section, do the following:

     1. Select one of the following routing options:

**Longest Idle Routing to distribute workload equally between agents**. Distributes workload equally between agents.

**Fewest Agents Routing to maximize utilization and call availability**. Routes chats to agents who already have chats.

For more information, see Basic routing with queue groups.

     2. Set the number of concurrent chats that a call should count as.

  7. In the **Deltacast Timeout for chats** section, set the deltacast timeout. Google recommends setting this to at least 10 seconds to allow enough time for the chat to connect.

**Important:** Set the deltacast timeout value lower than the **Percent Allocation Group** and **Cascade Group** values. These settings are in the **Group Settings** section of this pane.
  8. In the **Missed Chat Threshold** section, set the missed chat threshold.

  9. In the **Unresponsive Threshold** section, set the unresponsive threshold.

Optional: Select the **Apply unresponsive thresholds when agent is in an active chat or call session** checkbox.

  10. Optional: In the **Cascade Timer selection** section, select the **Skip Cascade Group Timer when agents are not available in the cascade group** checkbox.

  11. Click **Save Routing**.




### Turn on deltacast for chat at the queue level

Deltacast settings for queues are automatically inherited from the global settings unless you change them for individual queues. You don't need to enable deltacast globally to configure it for specific queues.

To turn on deltacast for chat at the queue level, follow these steps:

  1. Go to **Settings > Queues > {Web or Mobile channel} > {`QUEUE_NAME`}**.

  2. Go to the **Routing** section. If you have global deltacast settings enabled, a **Global** tag appears. All queues automatically inherit global deltacast settings unless you change them at the queue level.

  3. Click **Configure** , and then click **Deltacast** to enable it for this queue.

  4. Set your deltacast configuration values, and then click **Save**. For more information about deltacast configuration settings, see Turn on deltacast for chat globally.




### Monitoring and reporting for chat

Admins and managers can see agents in Missed Chat status in the **Logged in Agent** section of the CCAI Platform Chat Dashboard in the CCAI Platform portal. Agents in Missed Chat status are also visible in the CCAI Platform portal in the **Agents > Agent** page. You can click the **Filter Settings** menu at the top of this page to filter on agent status.

#### View deltacast and multicast chat data

All notifications offered, pickup attempts, and successfully answered chats are logged and can be viewed in reports and reporting APIs. The following reports are available:

  * Agent Activity - Summary Report
  * Agent Activity - Timeline Report



To download a report, follow these steps:

  1. Go to **Reports > Agents & Teams**.

  2. Choose an agent or team for which you want to see data.

  3. Under **Select Session Type** , select **Chats**.

  4. Under **Select Reports Desired** , select the report type(s) that you want.

  5. Select the **Timeframe** and **Timezone**.

  6. Click **Download**. Deltacast metrics are labeled in the downloaded report.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
