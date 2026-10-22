---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/calls-connected-queued-completed/
title: Calls: connected, queued, completed \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:37.998255+00:00
---

# Calls: connected, queued, completed  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/calls-connected-queued-completed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Calls: connected, queued, completed Stay organized with collections  Save and categorize content based on your preferences. 

The Calls tab allows for a real-time view of queued, connected, and completed calls. Admins and Managers can view detailed information, listen in on live calls, and view real-time call stats.

Users with the Manager role will have _restricted access_ to only agents on their assigned teams.

## Connected calls

This dashboard displays all interactions in progress.

  1. Click **Calls > Connected** to show calls in progress.

  2. **Search** for agents or queues connected calls by typing in agent name, queue name, or call ID.

  3. Click **Customize Columns** to reorganizing/excluding columns from the page.




**Data Columns:** Lists an overview of connected call information.

**Column Title** | **Description**  
---|---  
Start Time | The time the interaction started.  
Barge | Indicates whether a **barge** is in progress.  
Assigned Agent | The Agent assigned to the interaction.  
Actions | Allows users with appropriate roles to:

  * View Live Call (Monitor)
  * Barge in on the call
  * View connected call details
  * End the Call

  
Call Id | The unique identifier of an interaction.  
Current Handle Time | Length of time the consumer has been on the call.  
Wait | Length of time spent in queue before an agent was assigned.  
Type | Interaction Type  
Queue | For inbound sessions, show the queue the call came in through. Displays the queue name where the interaction waited.  
Verified | Device owner verified via SmartActions.  
Transferred | If the customer has been transferred during the call session.  
  
### Actions

Allows for monitoring a live call or viewing call details.

  1. **See Call Details** : Shows data columns (#4) in quick view mode as well as history of any transfers this session has had.

  2. **Monitor** : Allows for listening to call in real-time. The caller and Agent will not know the call is being monitored.

  3. **Barge:** Join the call. The Agent and the caller will hear you on the call.

  4. **End** : Allows for ending the call. This can also be used when a call is _stuck_.




## Queued calls

This Monitoring Page shows the scheduled calls / queued calls.

1\. Go to **Calls > Queued**

The following options are available:

**Search** : Search for queued calls by agent or queue name.

**Customize Columns** : Reorganize order of data columns.

The Following Data Columns will appear.

**Data Columns** : Lists an overview of queued call information.

**Queue-in/Schedule** : Time call came into the queue or is scheduled for.

**Assigned Agent** : The agent who picked up the call or has been assigned a scheduled call. For non-scheduled calls, this will show momentarily before the call moves to **Calls** > **Connected.**

**Actions** : **View** call details and **End** a call.

**CALL ID** : the call id issued to the call.

**Wait** : Duration of in-queue time.

**Type** : The type of call. See Interaction Call Types in the Data. Dictionary.

**Queue** : The Queue menu selected by a caller.

## Completed calls

  * **Calls > Completed:** Shows history of prior calls.

  * **Search:** Search for call history by agent, queue name, or call ID.

  * **Customize Columns:** Reorganize the order of data columns.




**Data Columns:** Lists an overview of call history information.

**Start time** : Time call began.

**Assigned Agent** : Agent last assigned to call, so if the call was transferred, the last agent to talk to the caller will be listed here.

**Actions** : View call details.

**CALL ID** : CCAI Platform ID number of call.

**CSAT** : Customer rating from Mobile or Web SDK.

**Handle Time** : Call time + hold time.

**Wait** : Length of time spent in queue before reaching an agent.

**Type** : Call type (Mobile, IVR, IVR Callback, Outgoing, Incoming, Scheduled, Voicemail).

**Queue** : Queue menu selected by a customer.

**Queue Priority** : The queue priority routing order. Possible values range from 1-8.

**Answered By** : that it was originally attended by : Human Agent or Virtual Agent.

**Recording Permission** : Identifies whether a consumer opts in or out of the call recording or whether they were asked for consent. Values: Granted, Denied, or Not Asked.

**Granted** : The consumer opted into having the call recorded.

**Denied** : The consumer opted out of having the call recorded.

**Not Asked** : The consumer was not asked if they consented to being recorded.

**Status** : Status of call (finished, abandoned, failed).

**Language** : The language selected by the consumer.

**Verified** : Device owner verified via SmartAction.

**Transferred** : Shows if a customer was transferred to other agent/menu.

**Queue-In Time** : the time the consumer entered the queue, after menu selection.

**End Time** : the time call ended.

**Support Phone Number** : the specific support number the caller dialed.

**Payment Statuses** : Shows if payment was successful or failed (Credit Card Over IVR Setup).

**Deflection** : Shows if the customer was deflected and to which channel.

**Data Columns** : Lists an overview of queued call information.

**Queue-in/Schedule** : Time call came into the queue or is scheduled for.

**Assigned Agent** : The agent who picked up the call or has been assigned a scheduled call. For non-scheduled calls, this will show momentarily before the call moves to **Calls** > **Connected.**

**Actions** : View call details.

**CALL ID** : CCAI Platform ID number of call.

**Wait** : Duration of in-queue time.

**Type** : Call type (Mobile, IVR, IVR Callback, Outgoing, Incoming, Scheduled).

**Queue** : Queue menu selected by a caller.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
