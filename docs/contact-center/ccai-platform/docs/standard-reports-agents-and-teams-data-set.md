---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-agents-and-teams-data-set/
title: Standard Reports: Agent and Teams Datasets \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:38:46.362213+00:00
---

# Standard Reports: Agent and Teams Datasets  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-agents-and-teams-data-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Standard Reports: Agent and Teams Datasets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the standard reports available for Agent and Teams datasets.

## Performance Metrics Report

From the Reports tab, one of the report options is the **Performance Metrics report**. When selected, a list of available metrics is displayed based on the dataset selected. For example, the Agent & Teams option has different available metrics when Calls are selected than you will see for Chats.

### Metric definitions

When the Performance Metrics checkbox is selected, you are presented with options for which metrics to include in the report. The available metrics will vary based on the selected report and session types.

#### Summary Metrics

**Service Level** : Count of interactions that were answered by an Agent before the service level target has been reached / Count of offered interactions that are eligible for service level.

Interactions that are "service level eligible" are based on your configuration settings.

All SLA calculations exclude in-menu/pre-queue abandonments.

**Occupancy** : [Total time Agent status = In-Call or In-Chat or Wrap-up] / [Total time agent status = Available]

**Volume per Hour** : Average volume of interactions per hour (per hour referenced as 24 hours in a day, regardless of hours of operation)

**Handle Time:**

Calls: average (call duration + hold time + default wrap-up status associated with a Call ID)

Chats: average chat duration only (no wrap-up status applied)

**Longest Handle Time** : Longest call or chat duration

Calls: `max(call duration + average default wrap-up status associated with an interaction ID)`

Chats: max chat duration only (no wrap-up status applied)

**Hold Time** : Average duration (in seconds) that a consumer was placed on hold by an Agent.

**Longest Hold Time** : Max duration (in seconds) that a consumer was placed on hold by an Agent

**Wait Time** : Average time a consumer spends in the queue.

`Average(Connected [to agent] DateTime - Call Queued DateTime)`

**Longest Wait Time** : Max time a consumer spends in the queue.

`Max(Connected [to agent] DateTime - Call Queued DateTime)`

**Longest Segment Time** : Max time for an Agent interaction. For calls, this includes hold time.

**CSAT Rating** : Average of consumer ratings using IVR, Mobile SDK, or Web SDK.

**Lowest CSAT Rating** : Lowest CSAT given by a consumer using IVR, Mobile SDK, or Web SDK

**Avg. Wrap-up Time** : Average time an agent spent in Wrap-up status. Calculation: total of acw_duration over the count of perf_call_handle_durations

#### Aggregate Metrics

**Total Volume** : Total count of interactions offered including finished and failed interactions.

**Total Handle Time** : Total amount of time spent in interactions. Includes wrap-up time.

**Total Active Talk Time** : Total handle time excluding hold time and wrap-up time.

**Total Hold Time:** Total time consumers were placed on hold by Agents.

**Total Available Time** : Total amount of time in available status.

**Total Wrap up Time** : Total amount of time in Wrap-up status.

**Total Deltacast Missed Call Status Count** : (Calls only) Total number of times an Agent is placed in Missed Call status. This is different from Total Deltacast Missed as it varies based on the Missed Call threshold set in Settings > Operation Management.

**Total Deltacast Missed** : Number of Deltacast calls missed.

**Total Auto Answered Calls:** Total number of interactions that were assigned to Agents using auto answer.

**Repeat Contact** : # of callers that had multiple incoming sessions that finished in the same queue within the configured repeat contact timeframe set in **Settings** > **Operation** Management.

**Total Preset SMS Sent:** Total number of preset SMS sent by Agents using SMS Blending features like In Call and Wait Time SMS.

**Total Custom SMS Sent:** Total number of custom SMS sent by Agents using SMS Blending features.

**Total SMS Received:** Total number of SMS sent by consumers using SMS Blending features.

**Total Wrap-up Time** : Total time agents spent in Wrap-up status. _Calculation: total of acw_duration on perf_call_handle_durations._

#### Assignments

**AssignedQueues** : Queues Agent is assigned to.

**Queue Priority by Language:** List of assigned queues including the language and specific queue priority for each queue assigned.

**AssignedTeams** : Teams the Agent belongs to.

#### Breakdowns

**Type Breakdown** : % of different call or chat types (For example, IVR, Mobile).

**Status Breakdown** : % of different call or chat statuses (finished, abandoned, failed).

**Voicemail Breakdown:**

**Voicemail Received** : Number of voicemails received within the filtered time range.

**Voicemail Read** : Voicemails an Agent has listened to on the Agent Adapter.

**Waiting** : Voicemails received in the last week that have not been listened to on the Agent Adapter.

**SMS Sent Breakdown** : (Calls only) Total number of SmartActions sent by SMS using SMS Blending features.

## All Active Users Report

The **All Active Users Report** provides data on current active users.

Potential use cases are aiding with bulk updates, import or export activities, and user audits.

To create a report:

Go to **Reports > Agents and Teams**

Step 1: Select Agents and Team. Options include select All Agents or enter specific Agents, Teams, or both.

Step 2: Select Session Type. Select the type of session for which agent and team reports should be generated. Options include Call or Chat.

Step 3: Select Reports Desired. Choose the reports you want to download and the data columns to include.

Check the checkbox next to **All Active Users**.

Step 4: Choose Filters. Choose to filter the reports by **timeframe** or **timezone**.

Click **Download**.

The following metrics are available in the **All Active Users** report.

Metric Name | Definition | Type  
---|---|---  
Agent ID | The unique identifier assigned to the Agent. | Attribute  
Agent Number | A custom name or number that can be assigned to the Agent for identification purposes. | Attribute  
Last Name | The last name of the Agent. | Attribute  
First Name | The first name of the Agent. | Attribute  
Email Address | The email address of the Agent. | Attribute  
Roles | Indicates the Roles assigned to the Agent. | Attribute  
Channels | Indicates the Channels assigned to the Agent. | Attribute  
Teams | Indicates the Team (s) to which the Agent is assigned. | Attribute  
Max Concurrent Chats | The maximum number of chats the user is able to take as configured under Settings > Users > Teams. This field always displays the value set at the individual agent level an does not show the global concurrency setting, even if the concurrency limit is disabled for a user. | Attribute  
Max Concurrent Chats Limit Enabled | Indicates if a max chat limit is enabled at Settings > Users & Teams > Edit User. This formats as a TRUE (yes enabled) or FALSE (not enabled). | Attribute  
Last Login | The date of the user's last login. Includes logins using the Portal or Agent Adapter. | Timestamp  
  
## Deactivated Users Report

The **Deactivated Users Report** provides data on deactivated users.

Potential use cases are aiding with bulk updates, import or export activities, and user audits.

To create a report:

Go to **Reports > Agents and Teams**

Step 1: Select Agents and Team. Options include select All Agents or enter specific Agents, Teams, or both.

Step 2: Select Session Type. Select the type of session for which agent and team reports should be generated. Options include Call or Chat.

Step 3: Select Reports Desired. Choose the reports you want to download and the data columns to include.

Check the checkbox next to **Deactivated Users**.

Step 4: Choose Filters. Choose to filter the reports by **timeframe** or **timezone**.

Click **Download**.

The following metrics are available in the **Deactivated Users Report**.

Metric Name | Definition | Type  
---|---|---  
Agent ID | The unique identifier assigned to the Agent. | Attribute  
Agent Number | A custom name or number that can be assigned to the Agent for identification purposes. | Attribute  
Last Name | The last name of the Agent. | Attribute  
First Name | The first name of the Agent. | Attribute  
Email Address | The email address of the Agent. | Attribute  
Roles | Indicates the Roles assigned to the Agent. | Attribute  
Channels | Indicates the Channels assigned to the Agent. | Attribute  
Max Concurrent Chats | The maximum number of chats the user is able to take as configured under Settings > Users > Teams. This field always displays the value set at the individual agent level an does not show the global concurrency setting, even if the concurrency limit is disabled for a user. | Attribute  
Max Concurrent Chats Limit Enabled | Indicates if a max chat limit is enabled at Settings > Users & Teams > Edit User. This formats as a TRUE (yes enabled) or FALSE (not enabled). | Attribute  
Last Login | The date of the Agent's last login. Includes logins using the Portal or Agent Adapter. | Timestamp  
Deactivated Date and Timestamp | The date and timestamp of when the Agent was deactivated. | Date and Timestamp  
  
## Agent Status Summary and Timeline Report

Agent statuses, also known as Aux codes, are used to track time spent on different tasks and make agents available for calls or chats.

For a summary of time spent in each status, pull the Agent Activity Summary Report.

The downloaded report will show the fields that apply to the agent in the specified timeframe.

For a detailed timeline view of when and for how long an agent was in each status, as well as other detailed actions, pull the Agent Activity Timeline Report.

To create a report:

Step 1: Select Agents and Team. Options include select All Agents or enter specific Agents, Teams, or both.

Step 2: Select Session Type. Select the type of session for which agent and team reports should be generated. Options include Call or Chat.

Step 3: Select Reports Desired. Choose the reports you want to download and the data columns to include. Check the checkbox next to **Agent Status Summary** Report, **Agent Activity - Timeline Report** , or both.

Step 4: Choose Filters. Choose to filter the reports by timeframe or timezone. Click Download.

The downloaded report will show the fields that apply to the agent in the specified timeframe.

### Emergency Services

Agents can make Emergency Calls, exclusively in the United States. Agents can add-party dial, and warm transfer an emergency call.

Consumers can join an agent-initiated conference call with 911 emergency services and stay connected after the agent leaves.

Emergency Services can receive the call with a validated emergency address and dial back to the call back number.

These emergency calling related event types will be displayed in the column Activity Log (Agent Status Summary Report).

  * Emergency Services - Outbound Dialed: The emergency call was dialed by the agent.

  * Emergency Services - Conference Added: The emergency call was added to an existing call.

  * Emergency Services - Conference Joined: The emergency call joined the existing call.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
