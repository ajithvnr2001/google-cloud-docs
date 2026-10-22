---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-session-data-feed/
title: Session data feed \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:00.086858+00:00
---

# Session data feed  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-session-data-feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Session data feed Stay organized with collections  Save and categorize content based on your preferences. 

A session data feed captures the stream of data that is generated when events take place during a session. These events are actions taken by agents, end-users, and Contact Center AI Platform (CCAI Platform). You can analyze session data feeds to get insights into user experience, customer engagement, agent performance, and more.

The **Session Data Feed** widget is available when you [create a desktop layout](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts), so you can include a panel in your desktop layouts that contains the session data feed. As your session progresses, the session data feed captures event data and displays it in the panel. To save session data feeds without a CRM, you need to configure [External storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage).

## Turn on the session data feed

To use the session data feed, you need to turn it on.

To turn on the session data feed, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Session Data Feed** , select the **Use session data feed** checkbox.

  4. Click **Save Agent Desktop**.




## Session data feed events

Here is a list of the events for which the session data feed captures data. This list contains the type of data collected and includes example data.

**Call started**

Voice Outbound

  * Contact Center AI Call ID: 6679
  * Language: English (US)
  * Time: July 2, 2024 at 7:06:15 PM PDT
  * Outbound number: +1 234 567 8910



**Chat started**

Messaging Inbound (Web Chat)

  * Contact Center AI Chat ID: 3034
  * Language: English (US)
  * Menu: Orders/Returns 
  * Time: July 4, 2024 at 2:23:16 PM GMT+7
  * Device: Browser



**Call ended**

  * Contact Center AI Call ID: 6722
  * Disconnected By Agent
  * Time of call: July 4, 2024 at 2:41:02 PM GMT+7
  * Length of call: 00:21



**Chat ended**

  * Contact Center AI Chat ID: 3036
  * Disconnected by End User
  * Time of chat: July 4, 2024 at 2:35:34 PM GMT+7



**Custom data from the customer has arrived**

  * membershipNumber: 21754
  * model: 1234
  * purchaseDate: Invalid DateTime
  * temperature: 70.5
  * osVersion: 17.3.1
  * lastTransactionId: FEBA4C32-1DD5-4C0A-985C-78FB7A61A166
  * dashboardUrl: http://internal.dashboard.com/1234
  * location: Location not available
  * bluetooth: Bluetooth state unknown



**Callback number**

  * Incoming phone number: +1 800 555 0175
  * Callback number: +1 800 555 0100



**Text attachment uploaded**

Virtual agent transcript

  * CRM link: https://example.com/attachments/token/...



**API DAP Response**

(Loanne: True)

API Response key value list

  * key: zulu
  * priority: 1
  * user_type: shopper



API Response Json

{

"key": "zulu",

"priority: 1,

"user_type": "shopper"

}

Request parameters passed to API DAP

Request parameters passed:

{

"fixed_parameter": "abcxyz",

"abc": 1

}

**Verified**

Verified by Alex B

**Payment Data**

  * Product Name: sample product name
  * Amount Charged: 10.00 USD
  * Payment Status: Success
  * Transaction ID: ch_3PYlfT
  * Agent: Alex B
  * Timestamp: July 4, 2024 at 4:09:32 PM GMT+7



**Customer rating received**

  * Customer rating feedback received: 5
  * Customer text feedback received: very good



**Call Redacted**

  * Start: July 5, 2024 at 11:28:48 AM GMT+7
  * End: July 5, 2024 at 11:35:33 AM GMT+7
  * Duration: 06:45



**Chat transcript uploaded**

Chat message history

  * CRM link: https://example.com/attachments/token/...



**Photos uploaded**

A screenshot is uploaded

  * screenshot External storage link: https://example.com/attachments/token/...



**Video uploaded**

A video is uploaded

  * External storage link: https://example.com/attachments/token/...



**Text note received from customer**

Text note received from customer

Hello

**Survey was answered**

  * Question: Star Rating Question
  * Stars: 5
  * Question: CSAT Question
  * Rating: 4
  * CRM link: https://example.com/attachments/token/...



**Transfer began**

Call transfer from SUPPORT_T1/PN/PN 1 to ORDERS_RETURNS/PN PN 2 began

**Transfer finished**

Call transfer from SUPPORT_T1/PN/PN 1 to ORDERS_RETURNS/PN PN 2 finished

**Transfer failed**

Call transfer from SUPPORT_T1/PN/PN 1 to ORDERS_RETURNS/PN PN 2 failed

**Adding participant began**

  * PN 1 started adding PN (*1234) to the call



**Participant Finished**

  * Consumer (+1-(800)-555-0175) was added to the call by Alex B ()



**Addition of participant failed**

  * The attempt to add PN (*1234) to the call by PN 1 failed
  * Reason: agent (PN) did not pick up the call



**Co-browse data uploaded**

  * CRM link: https://example.com/attachments/token/...



**Agent Assist auto-generated Summary**

  * Summary: The customer wants to know where San Francisco is. No agent action.
  * Agent: Alex B



**Emergency Services**

Ariel attempts to add Emergency Services to this call.

**Content Card button was selected**

End User selected the button Primary with reply 1 from the Title 1 card

**Call transfer redirected to external SIP**

  * SIP destination: sip:returns@returns.onsip.com 
  * Data parameters passed:
  * userName: Alex B



**Virtual Agent call recording**

Virtual Agent call recording is not available for consumer privacy reasons

**Virtual Agent transcript**

Virtual Agent call transcript is not available for consumer privacy reasons

**VA URL Links**

URL Links from Virtual Agent Returnsbot

  * https://example.com/returns/...



**Captured VA session variables**

  * Chat ID: 3070
  * Menu: In-App Support (QUEUE qca02)/Support/PN/PN 1
  * Chatbot Platform: Virtual Agent PN
  * Chatbot Workflow: Post Session Transfer - Chat
  * Virtual Agent: Virtual Agent PN - Chat
  * Intent: Captured At: July 5, 2024 at 3:08:39 PM GMT+7 Captured Variables
  * agentHelpfulness: 4
  * issueResolution: yes
  * agentComprehension: 5
  * openFeedback: nothing



**Co-browse session started**

  * Screen Share session was started by Agent
  * Time of start: July 5, 2024 at 3:16:54 PM GMT+7



**Co-browse session ended**

  * Screen Share session was ended by Agent
  * Time of end: July 5, 2024 at 3:19:31 PM GMT+7



**Co-browse remote control requested**

Screen Share remote control was requested

**Co-browse remote control accepted**

Screen Share remote control was accepted

**Co-browse remote control rejected**

Screen Share remote control was rejected

**Co-browse full device control requested**

Screen Share full device control was requested

**Co-browse full device control accepted**

Screen Share full device control was accepted

**Co-browse full device control rejected**

Screen Share full device control was rejected

**Session sentiment score**

Average sentiment score for the segment: 52

**Customer email collected**

Customer email: 222larabrown@gmail.com

**Realtime Transcript**

Call ID: 6800 | July 5, 2024 at 4:23:03 PM GMT+7 | 00:25

\----------------------------------------

[July 5, 2024 at 4:23:05 PM GMT+7 Virtual Agent PN - Voice] Hello, I am CX Agent Number 1.

How can I help you?

\----------------------------------------

[July 5, 2024 at 4:23:10 PM GMT+7 Consumer] human agent

\----------------------------------------

**Virtual Agent Transcript**

Call ID: 6800 | July 5, 2024 at 4:23:03 PM GMT+7 | 00:25

\----------------------------------------

[July 5, 2024 at 4:23:05 PM GMT+7 Virtual Agent PN - Voice] Hello, I am CX Agent Number 1.

How can I help you? 

\----------------------------------------

[July 5, 2024 at 4:23:10 PM GMT+7 Consumer] human agent

\----------------------------------------

**Live Translation was used**

Spanish (Spain) and English (US) were used for translation

**Data parameters passed to Virtual Agent**

Data parameters passed to Virtual Agent PN - Chat

  * Data parameters passed:
  * order: yes
  * product: books
  * queueId: 502
  * queueLanguage: en



**Pre-session SMS deflection**

Pre-session SMS deflection was offered in ORDERS_RETURNS/PN/PN 1

  * Pre-session SMS deflection was accepted



**Dispositions**

  * Code: test001
  * Custom Code ID: 123
  * UJET Code ID: 3
  * Note: Okee
  * List: Custom
  * Custom List ID: 2222
  * UJET List ID: 3
  * Agent: Alex B



**CCAI Insight chat history uploaded**

GCS URL: gs://example-insights/oem/... 

**CCAI Insight call recording uploaded**

GCS URL: gs://example-insights/oem/... 

**Call recording**

  * CRM link: https://example.com/attachments/token/...
  * External storage link: https://example.com/v1/download/092a5b64-067b-...



**Inbound sip headers**

Data parameters passed:

  * xTwilioAccountSid: AC78449ee33...
  * xInboundVpsip: true
  * xTwilioCallSid: CAe63b...



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
