---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/barge/
title: Barge for calls and chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:44.007037+00:00
---

# Barge for calls and chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/barge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Barge for calls and chat Stay organized with collections  Save and categorize content based on your preferences. 

Barge lets a supervisor join any of their agents' ongoing calls or chats. After barging into a call or chat session, the supervisor has access to the same agent adapter controls as the agent. The supervisor can leave the session and let the agent continue, or the supervisor can stay until the end of the session.

In reports, you can see which calls and chats that barge was used with.

## Barge behavior

Barge behaves as follows:

  * A supervisor can only barge into an active call or chat.

  * A supervisor can only barge into one one call or chat at a time.

  * Multiple supervisors can barge into a single call or chat.




## Configure barge

To use barge, you need to enable it. Enabling barge makes it available to users with barge permissions. The CCAI Platform Admin and Manager roles have barge permissions by default. Users with the Admin role can barge into the call or chat sessions of any agent, while users with the Manager role can only barge into sessions of agents on their team. If you need to create a custom role with barge permissions, see Create a custom role with barge permissions.

### Enable barge

To enable barge, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Operation Management**.

  2. Go to the **Barge** pane.

  3. Do one of the following, or both, depending on your requirements:

     * Click the **Calls** toggle to the on position. This enables barge for calls.

     * Click the **Chats** toggle to the on position. This enables barge for chats.

  4. Click **Save Barge**.




### Create a custom role with barge permissions

The Admin and Manager roles have barge permissions by default. You can create a custom role with barge permissions if you need one.

To create a custom role with barge permissions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users and Teams**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Users and Teams**.

  2. Click the **Roles and Permissions** tab.

  3. Click **Add Roles**.

  4. In the **Add Role** dialog, enter a role name, label name, and optional description for your custom role.

  5. Do one or more of the following, depending on your requirements:

     * To monitor agents and barge into sessions from the **Agents** page: in the **Monitor | Agents** row, select the **View** and **Edit** checkboxes. For more information, see Barge from the Agents page.

     * To monitor and barge into calls from the **Connected Calls** page: in the **Monitor | Calls** row, select the **View** checkbox. For more information, see Barge from the Connected Calls or the Connected Chats page.

     * To monitor and barge into chats from the **Connected Chats** page: in the **Monitor | Chats** row, select the **View** checkbox. For more information, see Barge from the Connected Calls or the Connected Chats page.

  6. In the **Monitor | Agents, Calls, Chats** row, select the **Edit** checkbox. To make barge only available for those calls or chats that are assigned to the user's team, also select the **Assigned teams only** checkbox.

  7. Add any other permissions that you require.

  8. Click **Save**.




## Barge into a call or chat session

You can barge into a call or a chat from the **Agents** page. You can also barge into a call from the **Connected Calls** page and barge into a chat from the **Connected Chats** page.

**Note:** If you're assigned to receive chats, change your status to **Unavailable** to avoid receiving chats after barging in on a call. Conversely, if you're assigned to receive calls, change your status to unavailable to avoid receiving calls after barging in on a chat. For more information, see [Status bar](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-menu-settings).

### Barge from the Agents page

To barge into a call or chat session from the **Agents** page, follow these steps:

  1. In the CCAI Platform portal, click **Agents > Agents**. If you don't see the **Agents** menu, click menu **Menu** , and then click **Agents > Agents**.

  2. In the row for the call or chat that you want to barge into, click more_horiz **More** , and then click **Barge**. The **Call Details** or **Chat Details** dialog appears, depending on context.

  3. In the details dialog, review the session details and click **Barge** to continue.

  4. In the confirmation dialog, click **Barge** to continue. The agent adapter appears and you're connected to the session. You can access the same agent adapter controls that the agent can.

  5. To leave the session, click **End Call** or **End Chat** , depending on context. If the agent is still in the session, the session stays active. If the agent has already left the session, it ends.




For more information, see Behavior after a barge is initiated.

### Barge from the Connected Calls or the Connected Chats page

To barge into a session from the **Connected Calls** or **Connected Chats** page, follow these steps:

  1. Do one of the following:

     * To barge into a call: in the CCAI Platform portal, click **Calls > Connected**. If you don't see the **Calls** menu, click menu **Menu** , and then click **Calls > Connected**.

     * To barge into a chat: in the CCAI Platform portal, click **Chats > Connected**. If you don't see the **Chats** menu, click menu **Menu** , and then click **Chats > Connected**.

  2. In the row for the call or chat that you want to barge into, click more_horiz **More** , and then click **Barge**. The **Call Details** or **Chat Details** dialog appears, depending on context.

  3. In the details dialog, review the session details and click **Barge** to continue.

  4. In the confirmation dialog, click **Barge** to continue. The agent adapter appears and you're connected to the session. You can access the same agent adapter controls that the agent can.

  5. To leave the session, click **End Call** or **End Chat** , depending on context. If the agent is still in the session, the session stays active. If the agent has already left the session, it ends.




For more information, see Behavior after a barge is initiated.

## Behavior after a barge is initiated

The following shows what happens after a supervisor barges into a call or chat:

  * The agent hears a tone and sees a banner that indicates who has joined the session.

  * For calls:

    * The call becomes a conference call that shows each caller and provides the ability to place callers on hold.

    * The end-user is not alerted that another user has joined the call.

  * For chats:

    * The chat becomes a multiparty chat.

    * End-users see a message that indicates that another user has joined the chat.

  * The agent can remain in the session or click **Done** to leave. If the agent leaves, the supervisor remains in the session.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
