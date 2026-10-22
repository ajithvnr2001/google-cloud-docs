---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chats-connected-queued-and-completed/
title: Chats: connected, queued, and completed \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:33.234147+00:00
---

# Chats: connected, queued, and completed  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chats-connected-queued-and-completed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chats: connected, queued, and completed Stay organized with collections  Save and categorize content based on your preferences. 

The Chats menu covers all the real-time views for your chat operation. The 3 views are Queued, Connected, and Completed, separating the chats based on waiting in-queue, connected to an agent, or finished. Each page has generally the same layout and functionality with slight variations depending on the chat status. The most notable variation is the ability to view live chats from the Chats > Connected page as described in View Connected Chats.

**All Chat pages show chats for the current day based on the timezone of your computer.**

**Chat monitoring pages are also subject to Roles & Permissions settings**.

## Data columns

Each of the 3 pages shows data columns that are relevant for the selected chat status. Some of the below data columns may not be on each page.

You can reorganize the order of data columns by clicking on **Customize Columns** (). Your settings will be saved for that page.

  1. **Queue In Time:**(Queued chats only) Time chat entered the queue

  2. **Start time:** Time the chat was connected to the end-user

  3. **Assigned Agent:** Name of the last agent assigned to the chat. If the chat was transferred, this shows only the last agent assigned.

  4. **Actions:** View finished chat details.

  5. **CHAT ID:** CCAI Platform ID number for a chat. With no CRM configured, the CHAT ID links point to external storage. With a CRM configured, the links point to the CRM.

  6. **CSAT:** Satisfaction rating left by the customer via Mobile SDK or Web SDK.

  7. **Handle Time:** Total time from connecting to the agent to the end of the chat.

  8. **Wait:** Length of time spent in queue before connecting to an agent.

  9. **Queue:** Queue menu selected by the customer or placed in via a DAP.

  10. **Status:** Status of chat. Many statuses are set by the Chat Expiration or Chat Timeout, which can be set in **Settings > Chats**

**Finished:** completed chat, ended by consumer or Agent

**Timeout Agent No Message** : chat timed out due to the assigned agent not sending a message

**Timeout End User No Message** : Timed out due to the consumer not sending a message.

**Timeout Agent Stopped** : Timed out due to a lack of messages from Agent.

**End User Stopped** : Timed out due to a lack of messages from the consumer.

**Abandoned** : Chat was abandoned before connecting to an Agent.

**Deflected** : Chat was deflected based on your Automatic Redirection settings.

**Failed** : Failed for various reasons.

**Expired** : Chat expiration threshold was met. Expiration is set in **Settings > Chat**.

  11. **Language** : The language selected by the consumer when multiple languages are used.

  12. **Verified** : When using the Mobile SDK, the device owner verified through their passcode using SmartActions.

  13. **Transferred** : Shows if a consumer was transferred to other agent or queue.

  14. **Queue-In Time** : Time consumer entered the queue.

  15. **End Time** (Completed chats only): Time chat ended.




## Connected chats

Active chats that are connected to an agent.

  1. From the CCAI Platform portal, go to **Chats > Connected.**

  2. To locate specific chats, use the **search field** for finished chats by agent, queue name, or chat ID.

  3. Click on the Actions icon to view the connected chat or to see details about the chat.

     1. **View Live Chat** : Shows the connected chat in real-time. See View Connected Chats.

     2. **See chat details** : Shows the following details about the call.




## Queued chats

Chats that are in the queue waiting to be connected to an agent. When using the Dismiss Inactive feature, Chats that are restarted by the consumer sending a response are placed back in the queue and will show in Chats > Queued as well.

  1. Go to **Chats > Queued**: Shows chats waiting in queue to talk to an agent.

  2. To locate specific chats, use the **search field** for finished chats by agent, queue name, or chat ID.

  3. Reorganize order of data columns by clicking on **Customize Columns**.

  4. Click on the **Actions** arrow to view details about the chat.




## Completed chats

Chats that have ended or are Dismissed when using Dismiss Inactive Chats. The status for dismissed chats on the Completed Chats page is _Dismissed - Inactive End user_.

  1. Go to **Chats > Completed**.

  2. To locate specific chats, use the **search field** for finished chats by agent, queue name, or chat ID.

  3. Click on the **Actions** arrow to view details about the chat.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
