---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-dictionary/
title: Data dictionary and references \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:34.058929+00:00
---

# Data dictionary and references  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-dictionary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Data dictionary and references Stay organized with collections  Save and categorize content based on your preferences. 

The **Data Dictionary** provides the definition of metric and additional details if applicable.

Additional details can include: formatting, aggregates, `GROUP BY`, `calculations`, tips and examples.

## A

### Abandoned call

The sum of interactions that were waiting in queue and were disconnected by the caller before being accepted by an agent. **Excludes** In-menu and Short Abandons.

Calculation: `Count of Calls Abandoned`

### Abandoned chat

The sum of interactions that were waiting in queue and were disconnected by the consumer before being accepted by an agent. **Excludes Short Abandons**.

Calculation: `Count of Chats Abandoned`

### Abandoned % call

The total queue abandons as a percentage of the total queue interactions for the given period. Failed calls are not treated as abandoned.

Calculation: `Count of Calls Abandoned / (Count of Inbound Calls Handled + Count of Calls Abandoned)`

### Abandoned % chat

Percentage of chats abandoned in the queue. Calculation: `Count of Chats Abandoned / (Count of Chats Handled + Count of Chats Abandoned)`

### Active calls (real-time)

The total of calls that are active.

### ACW

See Wrap-up Time (Interaction Metric).

### ACW end date

The date and time when after call work (ACW) ended.

### ACW start date

The date and time when after call work (ACW) started.

### Agent assigned team

The selection of individuals that form a team for calls and chats.

### Agent email

The email address of the agent assigned to the interaction.

### Agent ID

The system generated unique identifier for the agent.

### Agent name

The name of the agent assigned to the interaction.

### Agent location

The location assigned to the agent as per the administrator configuration.

### Agent roles

The roles assigned to the agent.

### Agent status

The status of the agent.

### Agent team

The teams the agent is assigned to.

### Agent type

The type or category of the agent (for example: Agent, Supervisor).

### Answer type

Indicates how the interaction can be answered. The following values can appear:

Calls or Chats:

  * Manual

  * Auto




Additionally for Chats, the following values can appear:

  * Deflection

  * Outbound




### Answered by

The agent or system entity that answered the interaction.

### Assigned agent

Indicates the most recent Agent assigned to the interaction. For example, if Agent A transfers to Agent B, this column row will display Agent B's name.

### Assignment type

The type of assignment or allocation (for example: manual, automatic).

### Attachments count

The sum of attachments associated with the interaction.

### Auto answer count

The count of interactions that were auto answered.

### Available time

The total length of time (SUM) the agent has been logged in and in the _Available_ status within the Agent Adapter.

### Average abandon time (Calls/Chats)

The average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent.

### Average agent connection time

The average time it took for the agent to accept the interaction. This can format as H:M:S or S (seconds).

**Note:** This is not queue time, but the connection time to the agent.

### Average agent response time

The average time across all interactions that it took for agents or consumers to respond to the other party's previous message calculated by: `Total Response Time / Total Response Count`

`GROUP BY` Agent metrics for responses can be grouped by **menu_path_id** (menu path), **language** , **agent** , or **chat**.

`GROUP BY` Consumer metrics for responses can be grouped by **consumer** , **menu_path_id** (menu path), **language** , **agent** , or **chat**.

### Average callback time

The average amount of time it takes for a customer service representative to return a call to a customer after a callback request has been made. This metric is calculated by dividing the total time spent on callback requests by the number of callback requests during a specific period.

### Average chat time

The average amount of time agents spend in a chat with a consumer.

`GROUP BY` This metric can be grouped by `chat`, `agent id`, `menu_path_id` (menu path) or `language`.

### Average first time to response: Email

Measures the average time it takes to first respond to the email. Emails can consist of multiple interactions, but this is measuring only the first response from the agent.

### Average handle time (AHT)

#### Average handle time: Call

The average call duration (in seconds) plus the average time spent in wrap-up time. The average amount of time that elapsed from when an agent accepts a call / chat to when they end their wrap-up phase for a given date range. AHT starts when the call is assigned to the agent, not when the call is connected to the agent.

Calculation: `Sum of (BCW Duration + Call Duration + ACW Duration) / Total Handled Calls`

#### Average handle time: Chat

The average amount of time that elapsed from when an agent was assigned a chat to when they ended the wrap-up phase.

`GROUP BY` Average handle duration can be grouped by `menu_path_id` (menu path), `language`, `agent,` and `Call ID` or `Chat ID`.

### Average handle time: Email

Measures the average handle time across all email interactions within an email session, in which each email sent by the consumer or the support agent represents an interaction.

### Average hold time

_(Other Name: Average Hold Duration)_

The average time the consumer was placed in a hold status by the agent.

Calculation: `SUM (hold_duration) / Count of Handled Call Interactions`

### Average current queue time

This is a real-time metric. The current average amount of time that elapsed when calls or chats spend time in a queue waiting for agent assignment.

### Average queue time (Calls or Chats)

_Other Names: Average Queue Duration, Average Wait Time_

The average amount of time that elapsed when calls or chats spend time in a queue waiting for agent assignment.

### Average session handled per hour

Other names: Average call volume per hour Display the average sessions handled per hour by signed-in agents.

### Average speed of answer (ASA)

Average Speed of Answer (ASA) is the average time an interaction remains in the queue until it is assigned to an agent. ASA is only measured in instances where the interaction is ultimately handled by an agent.

### Average time in status (Live)

The average amount of time that agents' spend in the current working status. This can format as seconds (s) or hours, minutes, and seconds.

### Average wrap-up time - Calls

The average time spent in after call wrap-up (ACW).

Calculation: `Sum of ACW Duration/Total Handled Calls`

### Average wrap-up time - Chat

The average time spent in chat wrap-up (ACW).

Calculation: `Sum of ACW Duration/Total Handled Chats`

## B

### Before call work (BCW)

BCW is defined as the time an agent was utilized on a call, but when no consumer is yet present. It is a metric **only captured for Dialer Campaigns**. Each campaign type may have a slightly different definition of the start and stop times for BCW.

#### Preview BCW

The time the agent spends researching the consumer and / or previewing information / notes in the CRM.

#### Predictive BCW

The time the agent is waiting for the consumer to join the call.

**Example:**

To further understand how BCW appears depending on the selected dialer mode (preview or predictive); see how it appears in the Handle Time calculation.

Preview BCW (Preview Campaign Mode)

As part of the Handle Time calculation, **BCW is not included in the interaction time**.`Handle Time = BCW + Interaction Time + Wrap-up Time`

Predictive BCW (Predictive Campaign Mode)

BCW is captured as a subset of the I**nteraction Time calculation** because the call has already started. `Handle Time = Interaction Time {including BCW} + Hold Time + Wrap-up Time`

## C

### Call

A call is a single voice session that is comprised of many interactions.

### Call or chat attempted count

This is a count of times an agent attempts to answer an interaction. This includes attempt to pick up Deltacast or Multicast.

### Call or chat missed

If an agent misses a call or a chat, this is the status they will be issued.

### Call or chat queue assigned

Indicates whether the call or chat was assigned to a queue. This will be YES or NO.

### Callback

A callback is offered.

This occurs when the call is deflected because over capacity has been reached in the queue. The caller is offered a callback.

The call is marked as a deflected call. The queue position is maintained and once the interaction reaches the top of the queue the callback is made to the consumer.

### Callbacks waiting (Real-time)

The number of interactions that are queued and classified as callbacks.

### Callbacks wait time

The amount of time from when the consumer entered a queue to when the callback was initiated.

### Call bounced

The total number of interactions that were not answered and have rerouted to the next longest idle available agent.

### Call connected

_Other Names: Calls Connected_

This signifies that the interaction is connected (in a _Connected_ status). This indicates that the call contains both an Agent and a Consumer.

### Call date 30 minute interval

The interval of 30 minutes within which the call occurred.

### Call or chat duration

See Handle time for call duration or chat duration and Average handle time for average call or chat duration.

### Call or chat ID

The unique identifier for the call or chat interaction.

### Call notification

This is a notification that will be shown on the Agent Adapter. This informs the agent that a call has been assigned to them.

### Call status

The call status represents the stage of a call within the platform. The following values are available:

  * `scheduled (0)`: The call is scheduled to take place at a specific time in the future.

  * `queued (1)`: The call is waiting in a queue, ready to be assigned to an available agent.

  * `assigned (2)`: The call has been assigned to a specific agent for handling.

  * `connecting (3)`: The agent is in the process of establishing a connection with the call.

  * `switching (4)`: Indicates the call is transitioning between different states.

  * `connected (5)`: A successful connection has been established between the agent and the consumer.

  * `finished (8)`: The call has been completed.

  * `failed (9)`: The call has failed and the specific failure reason code is provided.

  * `recovered (10)`: A previously failed call has been retried and successfully completed.

  * `deflected (11)`: The call has been completed with a deflection.

  * `selecting (12)`: The call is in the process of selecting options from a menu before being queued (applies to IVR calls only).

  * `va_assigned (13)`: The call has been assigned to a virtual agent for handling.

  * `va_connected (14)`: The call has been successfully connected to a virtual agent.

  * `preview_pending (15)`: The initial status for a campaign call, indicating connection with the dialer for previewing customer data.

  * `preview_ready (16)`: Indicates that data has been received from preview dialer and the call is ready for further processing.

  * `campaign_connecting (17)`: The adapter has notified that the agent intends to take the campaign call, and the connection process is underway.

  * `campaign_connected (18)`: Confirmation that the campaign call connection has been successfully established.

  * `requeued (19)`: A call that was previously handled by an agent but failed and has been added to a queue for handling again.

  * `predictive_waiting (20)`: The agent is waiting for a predictive campaign call to be connected.

  * `progressive_waiting (21)`: The agent is waiting for a progressive campaign call to be connected.

  * `preview_waiting (22)`: The agent is waiting for a preview campaign call to be connected.

  * `campaign_dialing (23)`: The agent's campaign call is in the process of dialing out to the end user.

  * `voicemail (80)`: The call is in a voicemail state.

  * `voicemail_received (81)`: Voicemail has been received from the caller and recorded.

  * **voicemail_read (82)** : The voicemail has been assigned to an agent.




### Call transfers (Real-time)

The total number of transfers that relate to the live call.

### Call or chat type

See the call or chat types listed under Interaction type.

### Campaign name

The name of the campaign as entered in the Campaign Manager settings (**Campaign Name**).

### Campaign status

The progress of the campaign that is in live production.

The possible statuses (values) that can appear:

  * **Completed** : The Campaign has finished.

  * **Paused** : The Campaign is paused or suspended.

  * **Ready** : The Campaign ready to begin.

  * **Running** : The Campaign is in progress.




### Chat

A chat is a single session that is comprised of many interactions.

### Chat bounced

The total number of interactions that were not answered and have rerouted to the next longest idle available agent.

After three bounced activity attempts, the agent will be marked as unavailable. The agent will need to return to being available to receive new conversations.

### Chat concurrency

In chat utilization, the number of overlapping chats being handled by an agent at any given time.

### Chat response time

The time it took for the agent to respond to the consumer's most recent communication (the last message the consumer sent).

### Chat status

The chat status represents the stage of a chat within the platform. The following values are available:

  * `queued (0)`: The chat is waiting in a queue, ready to be assigned to an available agent.

  * `assigned (1)`: The chat has been assigned to an agent.

  * `finished (2)`: The chat is complete.

  * `canceled (3)`: The chat was canceled.

  * `failed (4)`: The chat failed and a failure reason is provided.

  * `dismissed (10)`: The chat was dismissed.

  * `selecting (11)`: The consumer is in the process of selecting a chat queue.

  * `va_assigned (20)`: A virtual agent was assigned to the chat.

  * `va_dismissed (21)`: A virtual agent dismissed the chat.




### Chat time

The amount of time agents spend in a chat with a consumer. Excludes the Agent's Wrap-up Time.

Aggregates: Average (Average Chat Time), Total, Maximum (Longest Segment Time, Longest Interaction Time)

`GROUP BY` This metric can be grouped by `chat`, `agent id`, `menu_path_id` (menu path), or `language`.

### Chat transfers (Real-time)

The total number of transfers that relate to the live chat.

### Consumer ended

The sum of chat or calls where the consumer decided to end the session before it was resolved by the virtual agent.

### Conversation start time

The start timestamp of when the agent interacted with the consumer.

### Conversation end time

The end timestamp of when the agent interacted with the consumer (this includes call or chat time and hold time).

### Count in SLA

Count of chat queue durations where queued time is less than the SLA threshold

### Count out SLA

Count of call queue durations where queued time is equal to or greater than the SLA threshold.

### CSAT

The customer satisfaction scores (CSAT) awarded to the interaction. These are captured after an interaction ends.

### Current agent network quality

Indicates a rating of the Agent's network quality during calls.

Possible values are:

  * **5** : Excellent

  * **4** : Good

  * **3** : Average

  * **2** : Poor

  * **1** : Unusable




Found: Agent Monitoring Dashboard

### Current sentiment score

The current sentiment score will be the average sentiment score for the latest segment of a call.

### Current status time (Real-time)

The Total Time that elapsed since the last status change. This can format as H:M:S or Seconds (S).

### Current max queue time (Real-time)

The current longest amount of time elapsed while calls or chats spend time in a queue waiting for agent assignment.

### Custom agent ID

A custom identifier associated with the agent (if applicable).

## D

### Date

The date of the interaction or event.

### Deflection

A state that occurs based on the queue configuration for overcapacity queues or after hour calls. Displays if the customer was deflected and to which channel.

Deflection options include voicemail, schedule call among others.

Deflection will vary based on channel (Web, IVR, Mobile).

### Deltacast

The method of projecting calls, one at a time, to agents in a queue cascade group.

### Deltacast calls attempted

The count of times the agent was selected for Deltacast.

### Deltacast calls connected

The count of times the agent answered the Deltacast call.

### Deltacast calls offered

The count of times the agent was selected for Deltacast and received the call notification in the adapter.

### Direction

The direction of the interaction, the possible values include: Inbound, Outbound, Campaign Outbound, or Internal.

### Disconnect status

The action that ended the segment. The possible outcomes are:

  * Agent disconnect

  * Consumer disconnect

  * Error




### Disconnected by {disconnected-by}

The entity that ended the interaction.

### Disposition

The code that the agent applies to the interaction when it is finished, identifying the call or chat subject or the outcome.

Disposition code are configured in **Settings > Operations Management**.

### Dismissal (Chat)

A chat dismissal occurs when a consumer becomes unresponsive for a given amount of time as configured in your portal settings.

### Dismissed chat count

The sum of chat dismissals.

### Dismissed time

The sum of time that the chat was in a dismissed state. A dismissed state ends when the chat is reactivated or ended.

## E

### Email ID

The unique identifier for the email interaction.

### Email inbox address

The email address associated with the inbox.

### Email inbox created at date

The date and time when the email inbox was created.

### Email inbox username

The username associated with the email inbox.

### Ended at date {ended-at-date}

The date and time when the interaction ended.

### End time

The end timestamp of the interaction (in some cases the date will also appear).

### Escalated

This metric represents the sum of interactions where the virtual agent was unable to handle the issue and escalates it to a queue where a human agent is assigned.

### Event status

The category of the interaction.

For Calls or Chats the possible values include: Call Finished, ACW Ended, BCW Ended, Chat Finished, ACW Ended.

For Queues the possible values include: Answered, Abandoned, Deflected, Failed.

## F

### Failed

Other Names: Total Failed

Refers to a call or chat that is not successfully connected to an agent or representative.

This can occur due to various reasons such as expired transfer, no answer, or declined by consumer.

### Failed interactions

The total count of failed interactions.

### Fail reason

The reason for the fail if applicable.

### Fail reason code

The error code associated with the failed interaction.

### Failed reason description

The description of the reason for the failure.

### Fallback response count

This metric indicates the total number of virtual agent default fallback responses. It represents the sum of interactions where the virtual agent was unable to understand the consumer's query and had to fallback to a default response.

### Fallback response rate %

This metric represents the percentage of virtual agent interactions where the virtual agent states that they did not understand the consumer's query, and the interaction resulted in a fallback response. It is calculated as the number of default fallback responses divided by the total number of virtual agent responses, multiplied by 100.

### From agent name {from-agent-name}

The name of the agent that transferred the interaction.

### From agent ID / From agent custom ID

The unique ID or unique custom ID of the agent that transferred the interaction.

### From agent email

The email of the agent that transferred the interaction.

### From agent role

The roles of the agent from which the interaction originated.

### From language

The language used by the agent from which the interaction originated.

### From queue name

The name of the queue where the interaction originated. For an outbound call, the queue name won't display.

## H

### Handled

The sum of interactions (call or chat) handled by an agent.

This includes work that an agent receives from a queue and work that was directly allocated to an agent and never entered a queue.

Calculation: `Count of all Call interactions where Event = Finished or Failed (Failed being long deprecated)`

### Handle Time

The amount of time that elapsed from when an agent was assigned a call, including before call work (BCW) for preview campaign calls, to when they ended the wrap-up phase.

Aggregates: Average

`GROUP BY`: Handle duration can be grouped by `menu_path_id`(menu path), `language`, `agent`, and `Call ID` or `Chat ID`.

### Hold instances

The number of hold instances that were initiated by the agent.

### Hold time

The sum of time (in seconds) an agent placed a consumer on hold during an interaction. Hold is recorded in total for a single interaction. An agent that places a consumer on hold multiple times will only show the total hold duration for that interaction. When that agent transfers the call out, this would start a new interaction which would track its own hold time.

Calculation: `SUM (hold_duration)`

Aggregates: Average, Maximum

### I

### In-call time

Other name: In Call Status Time

### Interaction

An interaction is a single leg of a session.

For Example: A call enters a queue and is answered by an agent. The call is then transferred to another queue and finished by another agent. In this example there were two (2) queued interactions, two (2) handled interactions by agents and one (1) consumer interaction. All the interactions form a session.

### Interaction time

The sum of the time from when the interaction started to when the interaction ended.

### Interaction types (session, call, and chat types)

Call types:

  * **Voice Inbound** : Standard PSTN calls.

  * **Voice Inbound (IVR using App)** : Fallback PSTN calls made from the Mobile SDK.

  * **Voice Inbound (App)** : Placed by consumers using an installed Mobile SDK.

  * **Voice Callback (Web)** : Initiated from the Web SDK.

  * **Voice Inbound(API)** : Initiated using API.

  * **Voice Scheduled (App)** : Scheduled using an installed Mobile SDK.

  * **Voice Scheduled (Web)** : Scheduled using an installed Web SDK.

  * **Voice Outbound** : Initiated by an Agent by dialing a number.

  * **Voice Outbound (API)** : Initiated using API.

  * **Voice Campaign** : Initiated using an Outbound Dialer (Campaign).




Chat types:

  * **Messaging (Whatsapp)** : Initiated using Whatsapp.

  * **Messaging (SMS)** : Initiated or received using SMS.

  * **Messaging (Web)** : Initiated using an installed Web SDK.

  * **Messaging (App)** : Initiated using an installed Mobile SDK.




#### Call or chat type

  * **Co-browse session** : Initiated by either the agent or end user, and can be a separate session which occurs as part of a call or part of a chat.



### Is call queue

Indicates if the interaction is related to a call queue.

### Is chat queue

Indicates if the interaction is related to a chat queue.

## L

### Language

The language as assigned (configured) to the queue.

### Last closed at date

The date and time when the interaction was last closed.

### Last sign-in at date

The date and time of the agent's last sign-in.

### Last resolved at date

The date and time when the interaction was last resolved.

### Long abandons

Long abandons are interactions that have entered a queue but are terminated by the consumer after a set number of seconds as configured by the customer (in the CCAI Platform portal).

## M

### Maximum agent response time

The maximum recorded response time by agent or consumer across matching interactions.

### Maximum callback wait

The longest amount of time an agent had to wait for a consumer to pick up after performing a callback.

### Maximum chat time

The longest recorded amount of time an agent spent in a chat with a consumer.

`GROUP BY` This metric can be grouped by `chat`, `agent id`, `menu_path_id` (menu path), or `language`.

### Maximum hold time

_(Other Name: Longest Hold Duration)_

The maximum duration (longest time) that a consumer was placed on hold by an Agent.

### Group by

Hold Time, Average Hold time, and Max. Hold Time can be grouped by **menu_path_id** (menu path), **language** , **agent** , and **Call ID** or **Chat ID.**

### Maximum queue time

_(Other Name: Max. Wait Time, Max. Queue Duration)_

The maximum amount of time that elapsed when calls or chats spend time in a queue waiting for agent assignment.

Does not consider whether or not the call was answered.

Calculation: `max (queue_duration)`

### Maximum speed of answer

The maximum time that elapsed from when an interaction entered a queue and when it got assigned to an agent. Speed of Answer metrics only measure in instances where the call is _ultimately handled by an agent_.

### Maximum wrap-up time

_(other names: Longest Wrap-up Time)_

The maximum length of time when the agent was in wrap-up status for the given time range.

`GROUP BY` Wrap-up time for interactions can be grouped by `menu_path_id` (menu path), `language`, `call` or `chat`, and `agent`.

### Menu (including menu type)

The leaf node of a menu path, with the menu type indicating which channel the interaction was routed using.

### Menu path ID

The ID which represents a unique materialized menu path. A materialized menu path is the tree of queue IDs that a call goes through (for example: 1/2/3).

### Missed calls due to network quality

Displays the total number of calls that were offered to the agent but were missed while the agent's network quality was poor or unusable.

## N

### Name

The generic name or identifier associated with the interaction.

### Next status

This is the next status that the agent will be in (for example, if the agent is in-call and then selects break as their next status).

## O

### Occupancy

This formula calculates the ratio of the total time an agent spends actively handling customer interactions (in-call or in-chat) to the total time the agent is either handling interactions or available to take calls. This metric provides an indicator of how efficiently an agent is utilizing their time, with a higher occupancy indicating that the agent is spending more time actively engaged with customers.

Calculation `[Total time Agent status = In-Call or In-Chat] / [Total time Agent status = In-Call or In-Chat or Available]`

### Outbound

A call or a chat that was initiated by an agent and not a consumer.

### Outbound handled calls

The sum of outbound call interactions that were handled by an agent.

### Outbound phone number

This is the Agent's outbound phone number as found in the Individual Call History Report. The number from which the Agent is dialing.

### Overall SLA %

Refers to the total Service Level Agreement percentage, which measures the percentage of calls or interactions that are answered within a specified timeframe based on your configuration.

To calculate the overall SLA % for a contact center, you would typically divide the number of calls answered within the specified timeframe by the total number of calls received during the measurement period, then multiply by 100 to get the percentage.

For example, if during a week the contact center received 1000 calls and 800 of them were answered within 20 seconds, the SLA% would be:

Calculation: `text{SLA%} = left(frac{800}{1000} right) times 100 = 80%`

This means that 80% of the calls were answered within the specified time-frame, meeting the SLA.

## P

### Payment statuses

The status of the payment. Possible values include:

  * Success

  * Failed




### Planned transfer

Indicates when the voice virtual agent transferred the call to a human agent through planned interaction.

For example, the virtual agent understood what the consumer was requesting and sent them to the proper queue, agent, phone number, or SIP endpoint.

This is formatted as True or False.

## Q

### Queue abandons

Other Names: Total Queue Abandons

The total number `[sum]` of interactions that failed while waiting in queue to be assigned to an agent.

### Queue abandon rate % {queue-abandon-rate-percent}

See Abandoned % call or Abandoned % chat.

### Queue abandoned time

The amount of time that calls waited in a queue before disconnecting without being accepted by an agent.

Aggregates: Average (Average Abandon Time)

### Queue entry

The distinct count of an entire session. A session could consist of multiple interactions, however, a queue entry is only counting this once.

This only counts the first queue entry for the interaction.

### Queue end date

The date and time when the queue session ended.

### Queue group

The group or category to which the queue belongs.

### Queue interactions

The sum of all inbound interactions that have entered a queue, this number includes all transfers, escalations, and deflections to another queue.

Calculation: `Queue Interactions = (Abandoned + Inbound Handled + Failed)`. Includes Callbacks.

### Queue name

The name of the queue associated with the interaction.

### Queued now

The total number of chats or calls are that are queued.

### Queue start date

The date and time when the queue started.

### Queue time

_Other Name: Queue Duration_

The total amount of time that elapsed from when a call or chat entered a queue to when it was accepted by an agent or the caller abandoned.

Aggregates: Average, Maximum, Total

`GROUP BY` This metric can be grouped by `call` or `chat ID`, `menu_path_id` (menu path), and `language`.

## R

### Recording permission

Recording permission is captured for the entire session of a call and is stored along with the call record itself.

Under the Recording Permission column in Historical Reporting the following values can appear:

  * Granted: The consumer opted into having the call recorded.

  * Denied: The consumer opted out of having the call recorded.

  * Not Asked: The consumer was not asked if they consented to being recorded.




For more information on how to view in standard reporting, see [Tutorial: View data on recording permission in standard reporting](https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports.md).

### Resolution rate %

This metric represents the percentage of virtual agent calls or chats exchanges that were successfully resolved by the virtual agent. Calculated as the sum of resolved interactions divided by the total virtual agent interactions.

### Resolved by virtual agent

This metric indicates the number of call or chat interactions that were resolved by the virtual agent, meaning without escalation.

### Response (Time and count)

The time in a given interaction that it took an agent or consumer to respond to a chat message (from the other party).

Aggregates: Average, Maximum, Total

`GROUP BY` Consumer metrics for responses can be grouped by `consumer`, `menu_path_id`(menu path), `language`, `agent`, or `chat`.

`GROUP BY`Agent metrics for responses can be grouped by **menu_path_id** (menu path), **language** , **agent** , or **chat**.

#### Example: Understanding response count and response time

  * Consumer sends message at 10:00:00 AM

  * Agent responds to message at 10:00:05 AM

  * Agent sends another message at 10:00:06 AM

  * Consumer responds to message at 10:00:09 AM




From this example, we would have a **Response Count** of 1 and **Response Time** of 3 seconds for the consumer because the consumer had only responded to the message at 10:00:06 AM.

The agent would have a **Response Count** of 1 with a **Response Time** of 5 seconds while the second message sent by the agent has no impact on response due to not directly preceding a message from the consumer.

### Returning users count

_(Other Names: Repeat Contacts)_

The count of returning users. A returning user contacts the same queue two or more times within a timeframe configured by the customer. The timeframe is set in **Settings > Operation Management**.

### Role

Other names: _Agent roles_ , _Custom roles_.

This is the list of roles that are assigned to this single agent.

## S

### Service-level calls

Calls meeting service-level criteria.

### Session

A session is one single communication stream.

This example is encompassing one session. Sessions have multiple interactions

For Example:

  * Call enters queue

  * Answered by an Agent

  * Transferred to another queue

  * Finished by another Agent




### Sessions assigned: Email

The total number of sessions that have been assigned to an agent.

### Sessions completed: Email

The total sum of sessions that have been closed or resolved.

### Sessions paused

The total number of emails that are in a Paused status. Applied by the agent when the email session is put on hold due to unresponsive consumers. The status is automatically applied by the system when an email session is in the active state with no activity or email exchange for 10 consecutive days.

### Session unassigned

Displays the total sum of sessions that are unassigned.

### Sessions unopened

The total sum of threads that have not yet been opened.

### Short abandons

Short Abandons are interactions that have entered a queue but are disconnected by the consumer before a set number of seconds as configured by the customer.

### Show phone number

Indicates if the phone number should be displayed.

### Sign-in

The time and date at which the agent signed into the Agent Adapter.

### SLA %

**Note:** SLA metrics are queue-based metrics and not something that can be assigned to an agent.

Of all the interactions that entered the queue, the percentage of interactions that started an active conversation with an agent within the configured SLA threshold. If short abandons are excluded in your SLA configuration, interactions that abandon within the configuration abandon threshold aren't counted.

Due to Recovered Calls being factored out, if the divisor is lower than the dividend then we set the dividend to equal the divisor creating a cap at 100%.

### SLA calls calculation:

Numerator: `Count of call queue durations`

Denominator: `Count of call queue durations In SLA + Count of call queue durations Out SLA -Recovered Calls queue durations)`

Calculation: `Count of calls In SLA /(Count of call queue durations In SLA + count of call queue durations Out SLA - Recovered Calls queue durations)`

### SLA chats calculation:

Numerator: `Count of chat queue durations`

Denominator: `Count of chat queue durations In SLA + count of chat queue durations Out SLA`

Calculation: `Count of chat queue durations In SLA / (Count of chat queue durations In SLA + count of chat queue durations Out SLA)`

#### Count in SLA

Count of chat queue durations where queued time is less than the SLA threshold

#### Count out SLA

Count of call queue durations where queued time is equal to or greater than the SLA threshold.

### SMS volume

The total number (count) of SMS interactions.

### Started at date

The date and time when the interaction started.

### Status change date

The date and time of the last status change for the agent.

### Status label

The label indicating the status of the interaction.

### Support number

The public number as assigned to the queue that a consumer will contact. This is _Inbound_ only.

## T

### Talk time

The total time that the Agent spent talking to a consumer. This excludes BCW and ACW.

Calculation: `Interaction duration minus hold duration.`

### Target-level service percent

Represents the percentage of interactions that are resolved or handled by agents within a predetermined target time as configured in the platform settings.

### Team name

The name of the team associated with the interaction.

### Third-party start time

The timestamp of when the third-party joined the interaction.

### Third party end time

The timestamp that the third party left the interaction.

### Third party time

The total time that the third party has spent in the interaction.

### To agent email

The email address of the agent that received the transferred interaction.

### To agent ID / To agent custom ID

The ID or custom ID of the agent that received the transferred interaction.

### To agent name

The name of the agent that received the transferred interaction.

### To agent role

The roles or responsibilities of the agent to which the interaction is directed.

### To language

The language used by the agent to which the interaction is directed.

### To queue name

This is the name of the queue where the interaction was transferred to.

### Total abandons: VA

This metric indicates the sum of interactions that were disconnected by the consumer during the interaction with the VA.

### Total agents (Real-time)

The current total number of agents that are signed into the adapter.

### Total agent Unavailable time

The total length of time (SUM) the agent has been signed-in and in the Unavailable status in the Agent Adapter.

### Total available time

The total length of time the agent has been logged in and in the Available status within the Agent Adapter.

### Total chat time

The total amount of time agents spend in chats with a consumer.

`GROUP BY` This metric can be grouped by `chat`, `agent id`, `menu_path_id` (menu path) or `language`.

### Total consumer initiated interactions

This metric displays the sum of interactions that were started by the consumers themselves.

### Total-Deltacast missed call-status count

The number of times the Agent was moved into the actual missed-call user status by missing a Deltacast projection.

### Total finished

The total number of sessions that did not fail and were handled.

### Total human agent initiated interactions

This metric shows the sum of interactions that were transferred from the virtual agent to a human agent for further assistance.

### Total logged in time

The total amount of time that an agent spends logged in and available to handle customer interactions.

### Total number of Deltacast call notifications offered

When an agent is selected for Deltacast, they receive a notification of a projected call. They send an acknowledgment back to the server to indicate that they received the notification.

It is only counted as a Notification Offered when the notification is received by their agent adapter.

### Total number of Deltacast calls resulting in missed call due to poor network

Displays the total number of Deltacast calls that were offered to the agent but were missed while the agent's network quality was poor or unusable.

### Total number of Deltacast calls to agent

The number of times the agent was selected for a Deltacast projection.

### Total offered

The sum of projections offered to an agent for a call or chat queue.

**Note:** Deltacast offerings go to one agent at a time.

Multicast offerings go to multiple agents.

Both are confined within cascade groups.

### Total queue time

_(Other Names: Total Wait Time, Total Queue Duration)_

The total amount of time that elapsed when calls or chats spend time in a queue waiting for agent assignment.

### Total queue abandons

The total number of interactions that failed while waiting in queue to be assigned to an agent.

### Total response count

The sum of all responses by agents or consumers during matching interactions.

### Total response time

The sum of all response time by agents or consumers during matching interactions. For agent response times, this would be the total amount of time the consumer was waiting for agent response to their previous message.

### Total sessions: Email

The total sum of email threads that have been received. This is not the individual exchanges.

### Total time in status (Real-time)

The total amount of time that agents' spend in the current working status. This can format as seconds (s) or hours, minutes, and seconds.

### Total transfers (historical)

The total number of call or chat transfers that occurred.

### Total transfers (real-time)

The total current number of transfers that relate to the live call or chats.

### Total unavailable time

The total length of time the agent has been logged in and in the Unavailable status within the Agent Adapter.

### Total virtual agent Interactions

This metric shows the sum of interactions in which the virtual agent was offered to consumers.

For example, if a consumer contacts a support center and interacts with one VA and then is transferred to another queue where they interact with another VA, then that is two VA interactions.

### Total volume

The sum of all interactions that have come into the portal using a queue, agent, or outbound calling (inbound and outbound). This includes Callbacks, Failed, Abandoned, and Handled.

### Total wrap-up time

The total of Wrap-up Time (when the agent was in wrap-up status) for the interactions.

### Transfer

Indicates if the interaction was transferred.

### Transfer connected date

The date and time when the transfer was connected.

### Transfer type

The type of transfer; possible values include cold or warm.

## U

### User status

The label for the User Status to which the Agent has been assigned.

### User Status Time

The total time the Agent spent in a user status. This includes custom status and default statuses.

### Utilization

Measures how much of the time the agent spent ready to take a call, chat, or interaction. This is divided by the total shift time.

For example:

Calculation: `5 hours (total logged in time) ÷ 8 hours (total shift) = 0.625 x 100 = 62.5%`

The utilization: 62.5%. Out of utilization: 37.5%.

## V

### Virtual agent assigned to queue

The name of the Virtual Agent assigned to a specific queue.

### Virtual agent call time

_Other Names: VA Call Duration, VA Handle Time_

This is the Virtual Agent's Handle Time.

### Virtual agent chat time

Other names: VA Handle Time, VA Chat Duration

The amount of time a virtual agent spends in a chat with a consumer.

### Virtual agent CSAT

A score indicating a consumer's level of satisfaction with the interaction with the Virtual Agent.

### Virtual agent deflection

This occurs when the Virtual Agent has answered a call or chat from the queue and escalates to a Human Agent in the same queue.

However, the queue is configured to deflect the interaction. For example, callback deflection, voicemail, after hours.

### Virtual agent escalation

Due to the Virtual Agent's inability to handle the issue, the virtual agent escalates to a queue where a human agent is assigned.

### Virtual agent fallback response

In the event that VA has not understood the question, there is a generic fallback response configured.

For example, please repeat the question since I did not understand it.

### Virtual agent (Virtual agent) ID

The unique identifier for the virtual agent.

### Virtual agent initiated by

Indicates who initiated the interaction. Possible values include a Virtual or Human Agent.

For example, a consumer enters a queue and is assigned a Virtual Agent. Or, a Human Agent transfers to a queue that also has a Virtual Agent.

### Virtual agent interaction

A single engagement using the Virtual Agent for a call or chat.

### Virtual agent interaction per hour

The average number (count) of interactions the Virtual Agent has handled per hour.

### Virtual agent name

The name of the virtual agent.

### Virtual agent: Average messages per session

This metric calculates the average number of messages exchanged throughout an entire virtual agent session across all of the sessions.

### Virtual agent: Average messages per interaction

This metric calculates the average number of messages exchanged within each individual interaction.

### Virtual agent resolution rate

Displayed with Top Virtual Agents, virtual agent resolution rate is calculated by the total VA interactions divided into the VA interactions that were resolved by the virtual agent.

`GROUP BY` This count of VA resolutions or the resolution rate by VA can be grouped by `call` or `chat`, `virtual agent`, `menu_path_id`, or `language`.

### Virtual agent resolved

The number of virtual agent call interactions that the virtual agent resolved. Usually a resolved call is one where the virtual agent resolves the issue from the consumer and gets some acknowledgment in the call that it has done so.

### Virtual agent response count

The number of times (count) the Virtual Agent responded to the consumer's most recent communication.

### Virtual agent response time

The time it takes the Virtual Agent to respond to the consumer's most recent communication (the last message the consumer sent). Chat only. Aggregates: Min, Max, Average

### Virtual agent returning users count

_(Other Names: VA Repeat Contacts)_

The count of returning users. A returning user contacts the same queue two or more times within a timeframe configured by the customer. The timeframe is set in **Settings > Operation Management**.

### Virtual agent status

The status of the virtual agent.

### Virtual agent volume

The amount of interactions that were handled by a virtual agent.

### Virtual agent total abandon time

This metric calculates the total amount of time that calls or chats waited in the queue before being disconnected by the caller without being accepted by a virtual agent.

This can format as seconds (s) or hours, minutes, and seconds.

### Verified

Indicates whether the device owner or end user verified through a SmartAction.

### Volume

_Other Names: Call Count, Chat Count_

The total sum of a collection of interactions.

### Voicemail read

When a customer leaves a recorded message, an agent is assigned to the interaction. Voicemail Read indicates _only_ whether the voicemail was assigned to an agent.

**Important:** The term read is used in the Voicemail Details report. Since the recordings are stored in the customer CRM, from a reporting perspective there is no way to acknowledge that a recording was listened to. Therefore, read-only means that an agent was _assigned_.**Note:** If there is an error with the voicemail recording, the columns **Voicemail Received** and **Voicemail Read** will both display FALSE.

### Voicemail received

When a customer leaves a recorded message, an agent is assigned to the interaction. Voicemail Received indicates _only_ whether the voicemail was received.

This formats as True or False.

**Note:** If there is an error with the voicemail recording, the columns **Voicemail Received** and **Voicemail Read** will both display FALSE.

## W

### Wait time

_(Other name: Wait Duration)_

**Note:** Metric name being deprecated.

See Queue time for wait time, Average queue time for average wait time and Maximum queue time for maximum or longest wait time.

### Work offered

The total number of interactions offered to the agent. This includes:

  * Deltacast call notification offered

  * Auto answered call notification offered

  * Multicast call notification offered




### Wrap-up time

Wrap-up Time can be broken up into two types; as an **interaction metric** and **agent time in status**.

### Wrap-up time (Interaction Metric)

_(Other Names: After Call Work ACW)_

The sum of total time (in seconds) the agent has had the wrap-up interface open for a given call or chat. When the agent clicks to End Wrap-up is when the timer stops. Each handled interaction will have a separate event tracked capturing this wrap-up time.

Calculation: `SUM (ACW Duration) from handle_durations tables`

Aggregates: Average, Maximum, Total

### Wrap-up time (Agent Status)

The time that an agent is in the actual Wrap-up status is tracked separately from the interaction metric outlined in the previous entry. For chats, an agent may not always transition into the Wrap-up status due to other ongoing chats or calls which makes the interaction based timer a better representation of Wrap-up Time.

Calculation: `SUM (duration) from user_activity_logs WHERE status = -6 AND activity = 20000`

`GROUP BY` Wrap-up time for agent time in status can be grouped by `Agent`.

### Wrap-up exceeded

Wrap-up exceeded can be found in reporting as a _status_ and a _metric_.

### Wrap-up exceeded (Agent Status)

Wrap-up Exceeded is a system-set status that provides the ability to transition agents into a wrap-up exceeded status once they have gone beyond a wrap-up threshold time and have cleared all ongoing sessions. When an agent transitions to Wrap-up Exceeded status, an agent-level notification appears.

In the **Activity Timeline Report** , wrap-up exceeded appears as a status value under **Activity log**.

### Wrap-up exceeded (Metric)

This can appear as a count in the Interactions Summary by Agent Report or a boolean in the individual call or chat history report (TRUE or FALSE).

(Count) The total number of times the agent goes into _Wrap-up Exceeded_ status.

(Boolean - TRUE or FALSE) Indicates whether a wrap-up exceeded status occurred.

### Total Wrap-up Exceeded Time

The total time the agent was in _Wrap-up Exceeded_ status. This is calculated as the time from when the wrap-up timer elapses to when the agent submits the wrap-up.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
