---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/wait-time-va-calls/
title: Wait-time virtual agents for calls \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:21:10.548111+00:00
---

# Wait-time virtual agents for calls  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/wait-time-va-calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Wait-time virtual agents for calls Stay organized with collections  Save and categorize content based on your preferences. 

Wait-time virtual agents improve the customer experience by actively engaging end-users while they wait for a human agent to join their call. You configure wait-time virtual agents to provide update announcements and handle various call scenarios. You can set announcement intervals globally or at the queue level to control how often the virtual agents play announcements.

A wait-time virtual agent's workflow includes putting incoming calls into a queue, providing periodic announcements to end-users based on system events, and responding to end-users' requests for status information. The virtual agent also responds to overcapacity conditions. When a human agent becomes available, the virtual agent connects the agent to the call and then leaves.

## Configure the announcement interval

You can configure the interval that your wait-time virtual agent sends announcements to end-users waiting for a human agent. You can configure this at the global or queue level. For more information, see Play periodic update announcements.

### Configure the announcement interval at the global level

To configure the announcement interval at the global level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Caller Announcements** pane.

  3. For **Universal Caller Announcement Intervals** , set the announcement interval, and then click **Save Caller Announcements**.




### Configure the announcement interval at the queue level

Configuring the announcement interval at the queue level overrides the global setting.

To configure the announcement interval at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Caller Announcements** section.

  5. For **General** , click **Configure**.

  6. For **Caller Announcement Intervals** , set the announcement interval, and then click **Save**.




## Wait-time virtual agent workflow

This section contains the steps that a wait-time virtual agent takes from the time that it puts an incoming call into a queue to the time it connects an agent to the end-user and then leaves the call. You must configure your wait-time virtual agents to do the actions described in this workflow.

### Put an incoming call into a queue

Your wait-time virtual agent puts an incoming call into a queue using a Dialogflow custom payload. You can configure the payload so that the virtual agent stays on the call with the end-user while they wait in the queue for a human agent.

**Important:** Be sure to put the call into a queue with human agents assigned to it. If you attempt to put a call to a queue with no human agents assigned, no escalation occurs and the call ends.

**Custom payload example**

The following is an example of a custom payload that escalates an incoming call into a queue:
    
    
    {
      "ujet": {
        "type": "action",
        "action": "escalation",
        "escalation_reason": "by_virtual_agent",
        "menu_id": "QUEUE_ID",
        "language": "LANGUAGE",
        "preserve_va": true,
        "recording_permission_granted": RECORDING_PERMISSION_GRANTED_BOOLEAN
      }
    }
    

Replace the following:

  * `QUEUE_ID`: the ID of the leaf queue that the call is escalated to. Wait-time virtual agents work only with calls escalated to leaf queues. If you specify a branch queue, the call is escalated, but the wait-time virtual agent leaves the call.

  * `LANGUAGE`: the two-letter language code for the virtual agent

  * `RECORDING_PERMISSION_GRANTED_BOOLEAN`: indicates whether permission to record the call session was granted by the end-user. If you want to record the call session, configure your wait-time virtual agent to ask the end-user for consent to record. Your instance must be configured for [call recording](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording). The following are possible values:

    * `true`: The end-user granted consent to record the call session.

    * `false`: The end-user didn't grant consent to record the call session.

Setting the `preserve_va` property to `true` activates the wait-time capabilities of the virtual agent and keeps the wait-time virtual agent on the call with the waiting end-user.




This payload does the following:

  * Puts the call in the queue that you specify, where the end-user waits until a human agent is assigned to the call.

  * Connects the wait-time virtual agent with the caller so the virtual agent can provide interactive updates to the end-user.




### Play periodic update announcements

Your wait-time virtual agent plays periodic update announcements for the end-user waiting in a queue. To enable this, configure your virtual agent to listen for the `interval_ewt_announce` event, which your instance emits according to the schedule that you set up in Configure the announcement interval. You also need to configure your virtual agent to play announcements to the end-user based on the information in the `interval_ewt_announce` event.

#### interval_ewt_announce event

The `interval_ewt_announce` event contains the following information:

  * Call ID
  * Queue ID
  * Language
  * Wait time in queue (`wait_duration_in_queue`)
  * Estimated wait time
  * Position of call in the queue



**Example message**

You can configure your wait-time virtual agent to play a message like the following for a waiting end-user, based on information in the `interval_ewt_announce` event: "Thank you for waiting. The current estimated wait time is five minutes, and you are third in line."

### Respond to overcapacity conditions

Your wait-time virtual agent responds to overcapacity conditions. To enable this, configure your virtual agent to listen for the `interval_ewt_announce_ocd` event, which your instance emits when overcapacity conditions have been met. You also need to configure your virtual agent to take the following actions when it receives the `interval_ewt_announce_ocd` event:

  1. Play a message to the waiting end-user that does the following:

     * Informs the end-user about high volume or overcapacity conditions.

     * Presents a choice of actions for the end-user to take, such as transfer to a different queue, transfer to a department, or keep waiting.

  2. Respond to the end-user's choice. Possible responses to end-user choices include the following:

     * **Transfer to a different queue** : Your wait-time virtual agent uses a Dialogflow custom payload to escalate the call to a specific queue. For more information, see [Escalation to the targeted queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#escalation-to-targeted-queue).

     * **Transfer to a department** : Your wait-time virtual agent uses a Dialogflow custom payload to escalate the call to a phone number or SIP URI for a department in your company. For more information, see [Transfer a call to a phone number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#transfer-to-phone-number) and [Transfer a call to a SIP endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#transfer-to-SIP-endpoint).

     * **Keep waiting** : Your wait-time virtual agent doesn't escalate the call. The end-user continues waiting.




#### interval_ewt_announce_ocd event

The `interval_ewt_announce_ocd` event contains the following information:

  * Call ID
  * Queue ID
  * Language



### Respond to update requests from the end-user

Your wait-time virtual agent responds to an end-user who requests information about their wait—for example, "What's my wait time now?". To enable this, configure your virtual agent to listen for end-user requests for wait time information. You also need to configure your virtual agent to call the **Get Call Status in Queue** API in response to an end-user request for wait time information. This API returns the user's position in the queue and their estimated wait time. Configure your virtual agent to play a message to the end-user that contains the wait information.

To get the queue status for a call, send a `GET` request to the following endpoint:
    
    
    https://YOUR_CCAAS_HOST/apps/api/v1/calls/CALL_ID/queue_status
    

Replace the following:

  * `YOUR_CCAAS_HOST`: your CCAI Platform host

  * `CALL_ID`: the caller's call ID




The response is similar to the following:
    
    
    {
      "call_id": 1357,
      "menu_id": 6,
      "lang": "en",
      "position_in_queue": 3,
      "wait_duration_in_queue": 10,
      "ewt": 400
    }
    

### Connect an agent to the call

The following sequence of events leads to your wait-time virtual agent connecting an agent to a call:

  1. An agent who is assigned to the queue that the call is waiting in becomes available.

  2. The system assigns the call to the agent.

  3. The agent clicks **Answer** in the call adapter to accept the call. The agent sees the **Connecting** screen while they wait to be connected to the end-user.

  4. Your instance automatically sends an `agent_available` event to your virtual agent to indicate that an agent is available to take the call. The event includes the following data that your wait-time virtual agent can use to customize a transition message for the end-user:

     * `queueName`

     * `agentAlias`

     * `agentFirstName`

  5. Your wait-time virtual agent connects the agent to the call. To enable this, configure your virtual agent to listen for the `agent_available` event, and upon receiving it, to do the following:

     1. Interrupt any active messages.

     2. Play a transition message to the end-user—for example, "An agent is ready, I'll connect you now."

     3. Connect the end-user to the available agent using a Dialogflow custom payload.

**Custom payload example**

The following is an example of a custom payload that connects the end-user with the available agent:
            
            {
              "ujet": {
                "type": "action",
                "action": "connect_end_user"
              }
            }
            

     4. Leave the call.




## Queue behavior with an active wait-time virtual agent

This section explains how queue behavior changes when a wait-time virtual agent is active on an incoming call. A wait-time virtual agent becomes active on an incoming call when the payload that escalates the call to a queue contains the following property: `"preserve_va": true`. For more information, see Put an incoming call into a queue.

### Queue-based announcements are deactivated

When a wait-time virtual agent is active on an incoming call, all announcements that are configured for the caller's queue are deactivated. These include estimated wait time, position-in-queue, and patience messages. Your wait-time virtual agent is responsible for all announcements to the end-user while they wait to be connected to an agent. For information about configuring your wait-time virtual agent to handle announcements, see Wait-time virtual agent workflow.

### Queue-based overcapacity deflection is deactivated

When a wait-time virtual agent is active on an incoming call, all deflection actions that are configured for the caller's queue are deactivated. Your wait-time virtual agent is responsible for all announcements and actions related to overcapacity deflection. For more information, see Respond to overcapacity conditions.

### After hours deflection

When after hours conditions are met for the queue, the system does the following:

  1. Disconnects the wait-time virtual agent from the call.

  2. Redirects the call according to the after hours deflection settings for the queue.




For more information, see [Hours of operation settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation#hours-of-operation-settings).

### Automatic redirection

Incoming calls that are automatically redirected to redirection groups are unaffected by wait-time virtual agents. For more information, see [Automatic redirection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection).

### Reporting

Wait-time virtual agent reporting data is available in the [Virtual agent dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
