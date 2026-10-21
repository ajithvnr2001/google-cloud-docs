---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-chat-response-time/
title: Agent chat response time \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:14.614588+00:00
---

# Agent chat response time  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-chat-response-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent chat response time Stay organized with collections  Save and categorize content based on your preferences. 

When an agent is in an active chat session and receives a message from the consumer, a timer will begin and a series of UI cues to prompt the agent to respond within a response threshold. Admins can set the threshold that the agent has to reply to messages and also report on the number of instances when the threshold is exceeded.

## Feature benefits

  * For Managers and Admins

    * Automatically remind agents to respond promptly to conversations
  * For Agents

    * Visually shows which chat needs their attention first
  * For end-users

    * Less waiting time and quicker resolution time



## Feature details

  * The response timer starts when the agent is assigned and the consumer has sent a message and applies even if an agent has not yet sent a message

  * If the agent responds, the counter won't begin again until the consumer replies.

  * When the target response time is met, chats won't end

    * Chats end when:

      * Agent manually clicks **end chat**

      * The consumer:

        * Closes the active tab

        * Navigates away from the page the chat session started on

        * Clicks **x** on the chat session

      * When the chat timeout threshold is reached




## CCAI Platform portal configuration

The following sections provide configuration information for agent target response time.

### Enabling global target response time

  1. Go to **Settings** > **Chat**.

  2. Mark the checkbox next to **Agent target chat response time** , and set the response target duration.

  3. Mark the checkbox next to **Apply target chat response setting to every chat queue**.

  4. Click **Set global chat settings**.




### Enabling queue-level target response time

  1. From the CCAI Platform portal, go to **Settings** > **Chat**.

  2. Mark the checkbox next to Agent target Chat Response time, and set the response target duration.

  3. Don't mark the checkbox next to **Apply target chat response setting to every chat queue**.

  4. Navigate to **Settings** > **Queue** > **Mobile** OR **Web** , depending on where you are using chat.

  5. Click a queue that has chat enabled.

  6. On the right, navigate to the **Agent Target Chat Response Time** setting.

  7. Click to toggle the setting to **On**.

  8. Enter the chat response target time in minutes.

  9. Click **Set customer chat configuration** to save.




## Agent experience

When you configure target response times, the behavior of the agent chat adapter changes in the following ways:

  * Active chat indicators display a target response timer. The timer indicates how much time has elapsed since the end-user's last message.

  * The timer display one of the following colors to indicate how much of the target response time remains:

    * **Yellow** : more than 45 seconds remain until the target response time expires

    * **Orange** : between 45 and 15 seconds remain until the target response time expires

    * **Red** : less than 15 seconds remain until the target response time expires




If the target response time expires, the active chat indicator continues to display red until the agent responds. At that time, the response timer resets. For more information, see [Answer the chat request](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat#answer-the-chat-request).

## Reporting details

  * When the timer hits 00 seconds, an event is logged that notes that the agent exceeded the target chat response time and can be seen in the 2 Agent Activity reports.

Example of how to select Agent Activity reports in **Reports** > **Users & Teams:**

    * Available in Agent Activity Summary report (**Reports** > **Users & Teams** > **Agent Activity - Summary Report)** as "Agent exceeded target chat response time."

    * Available in Agent Timeline report (**Reports** > **Users & Teams** > **Agent Activity - Timeline Report)** as "Agent exceeded target chat response time."

  * When chats are dismissed, chat status will show as **Dismissed - inactive end-user**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
