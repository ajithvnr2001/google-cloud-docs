---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-dictionary/
title: Raw data export dictionary \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:11.050377+00:00
---

# Raw data export dictionary  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-dictionary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Raw data export dictionary Stay organized with collections  Save and categorize content based on your preferences. 

The data exporter application delivers data to a configured Amazon S3 or Cloud Storage object. The data deliveries happen every 15 minutes, but if a prior delivery is still running, a new delivery may be skipped. 

The two types of file delivery are delta and full. A delta file type includes all the data since last execution. Identifiers seen in previous files can be repeated if those records have had an update. A full file type consists of the complete dataset. This is used on tables that don't get very large, but are still relevant to the overall understanding of data being delivered.

This dictionary is divided into two sections: Data and Metrics.

## Data

### call_participants

File type: Delta

Each member of a call gets recorded as a `call_participant`. If the same user leaves and rejoins a new `call_participant` record is created. These records are stateful and typically not used for metrics.

#### id

Primary key identifier for records.

#### call_id

References the **calls** records primary key **id**.

#### client_muted

Whether the participant's client is capturing audio.

#### connected_at

Timestamp of when the participant was connected into the call.

#### created_at

Timestamp when this record was created at.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### ended_at

Timestamp when the participant ended their engagement with the call.

#### hold

Boolean indicating whether this participant is currently experiencing hold. Typically these impact only end-user, consumer, records.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Waiting   
1  | Connecting   
2  | Connected   
3  | Reconnecting   
4  | Finished   
5  | Failed   
6  | Adding party   
11  | IVR CSAT in progress   
12  | Post session in progress   
90  | Action only   
100  | Voicemail finished   
  
#### type

Enum value.

Value  | Meaning   
---|---  
0  | End-user   
1  | Agent   
2  | Third party   
3  | Virtual agent   
4  | Campaign contact   
5  | Task virtual agent   
  
#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

#### placed_hold

Boolean indicating whether this participant is imposing hold on an end-user participant. These are only agent participant types.

#### phone_number

The caller ID of the end-user participant. Not all end-user calls can properly capture the caller ID and this data is only available on platforms that have been explicitly enabled to preserve this information for the data feed.

#### user_id

References the users table by primary key **id**.

#### virtual_agent_id

References the virtual agents table by primary key **id**.

### call_recordings

File type: Delta

Calls can have zero or many recordings per call and are logged in these record sets.

#### id

Primary key identifier for records.

#### call_id

References the calls records primary key **id**.

#### conference_sid

Unique identifier used at the telephony side for this recording.

#### created_at

Timestamp when this record was created at.

#### duration

Duration in seconds of the recording

#### recording_type

Enum value.

Value  | Meaning   
---|---  
0  | Default   
1  | Voicemail   
2  | CSAT voice memo   
3  | Virtual agent   
  
#### redaction_times

This is a string representing the start and stop times for when call redaction was enabled. Example structure showing two redaction windows:

* * *

  * :start: 2023-07-17 17:18:55.966329000 Z

:start_agent_id: 1

:end: 2023-07-17 17:19:14.840824000 Z

:duration: 18.874

:end_agent_id: 1

  * :start: 2023-07-17 17:20:55.966329000 Z

:start_agent_id: 1

:end: 2023-07-17 17:21:14.840824000 Z

:duration: 18.874

:end_agent_id: 1




#### s3_path

Deprecated.

#### started_at

The start time of the recording.

#### url

The URL of the recording. This will be either a link to the file in a configured CRM, external storage, or if using both whichever is dictated by external storage configurations.

#### voip_store

Stateful value from the carrier indicating the location of the recording. When recordings are completely processed this value will be NULL.

#### extra

Deprecated

#### recording_sid

Unique identifier on the carrier's side of the recording entity.

### calls

File type: Delta

Each call is represented by a single record in this set. Metrics are typically not derived from data on this table as it is stateful in nature.

#### id

Primary key identifier for records. Commonly linked in other tables by call_id or a composite key of **comm_id** and **comm_type** where **comm_type** equals "Calls".

#### agent_id

References the users table by primary key **id**.

#### answer_type

Enum value.

Value  | Meaning   
---|---  
0  | Manual   
1  | Automatic   
  
#### answered_by

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Human agent   
2  | Virtual agent   
  
#### assigned_at

Deprecated. The timestamp the call was assigned to an agent at. Use **perf_call_queue_durations** records timestamps.

#### auto_answered

Boolean indicating whether the call was auto answered.

#### connected_at

Deprecated. Derived from **perf_call_handle_durations** records using **started_at** plus the time in seconds in the **wait_duration** value.

#### created_at

Timestamp when this record was created at.

#### deflection

Enum value.

Value  | Meaning   
---|---  
0  | No deflection   
1  | Deflecting   
2  | Over capacity to phone   
3  | Over capacity to voicemail   
4  | Over capacity to callback   
5  | Over capacity to continue waiting   
6  | Over capacity play message   
8  | Over capacity to queue   
100  | After hours to voicemail   
101  | After hours to phone   
102  | After hours play message only   
103  | After hours to queue   
104  | After hours play message   
200  | Temporary redirection to phone   
201  | Temporary redirection to message   
202  | Temporary redirection to voicemail   
203  | Temporary redirection to queue   
205  | Temporary redirection to SIP   
300  | IVR pre-session deflection   
400  | Virtual agent redirection to phone   
401  | Virtual agent redirection to SIP   
  
#### disconnected_by

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Human agent   
2  | End-user   
3  | Virtual agent   
4  | System   
  
#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### ends_at

Timestamp when the call ended.

#### fail_reason

Enum value.

Value  | Meaning   
---|---  
0  | No failures   
10001  | Unknown   
11001  | Expired   
11002  | Transfer expired   
20001  | End-user cancelled   
20002  | End-user rejected   
20003  | End-user abandon   
20004  | End-user in menu abandon   
20005  | End-user repeat voicemail   
20006  | End-user repeat callback   
21001  | End-user busy   
21002  | End-user wrong number   
21003  | End-user no answer   
22001  | End-user notification failed   
23001  | End-user phone number denied   
30001  | Agent cancelled   
30002  | Agent ignored   
31001  | Agent mic no device   
31002  | Agent mic denied   
32001  | Invalid outbound phone number   
32002  | Dialed number blocked   
32003  | Connection declined   
41001  | VOIP Twilio error   
42001  | VOIP Tokbox error   
43001  | VOIP invalid token   
44001  | VOIP connection general   
44002  | VOIP connection timeout   
44003  | VOIP connection signal   
45001  | VOIP Nexmo error   
50001  | Stuck due to API error   
50002  | Group deleted without substitute specified   
50003  | Menu deleted   
60001  | Direct PSTN call to fallback number   
70001  | Campaign paused   
70002  | Campaign had queue reassigned   
70003  | Campaign no incoming contacts   
70004  | Campaign call cancelled   
80001  | Force ended by user   
80002  | Stuck call forcefully failed   
90001  | Audio not received by carrier   
90002  | Audio device unable to start   
  
#### fail_details

String containing more context about call failures. Null when the call did not fail.

#### finish_reason

Enum value.

Value  | Meaning   
---|---  
0  | No reason   
10001  | Agent hung-up to callback   
20001  | Virtual agent escalation unsuccessful   
30001  | IVR pre-session deflection completed   
30002  | Internal call declined by agent   
40001  | Force ended by administrator   
40002  | Stuck call force ended   
  
#### in_queue_priority

The priority value for this call while it was enqueued.

#### lang

ISO 639-1 language locale codes.

#### materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### menu_id

Relationship to menus using the primary key **id**

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### menu_type

String with the following possible values

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * email_menu




#### parent_id

References the same calls data by primary key **id**. Seen in callback scenarios where the callback is mappable to a previous call.

#### queue_priority_level

The priority level of the menu the call enqueued into.

#### rating

CSAT rating for this call.

#### recording_permission

Boolean indicating whether permission to record was granted.

#### repeated

Boolean whether this end-user appears to be a repeat entry.

#### scheduled_at

Timestamp when a scheduled callback is assigned to.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### smart_action_enabled

Boolean indicating if smart actions were enabled for this call.

#### status

Stateful enum values.

Value  | Meaning   
---|---  
0  | Scheduled   
1  | Queued   
2  | Assigned   
3  | Connecting   
4  | Switching   
5  | Connected   
8  | Finished   
9  | Failed   
10  | Recovered   
11  | Deflected   
12  | Selecting   
13  | Virtual agent assigned   
14  | Virtual agent connected   
15  | Preview pending   
16  | Preview ready   
17  | Campaign connecting   
18  | Campaign connected   
19  | Re-queued   
20  | Predictive waiting   
21  | Progressive waiting   
22  | Preview waiting   
23  | Campaign dialing   
30  | Action only   
31  | Action only finished   
80  | Voicemail   
81  | Voicemail received   
82  | Voicemail read   
86  | Voicemail finished   
  
#### support_number

Dialed phone number for inbound call.

#### transfer_count

Deprecated. Count of transfers. Use **perf_call_queue_durations** where transfer = 1

#### type

String with the possible values of

  * IncomingCall

  * NumberedIncomingCall

  * IvrCall

  * InAppIvrCall

  * AppsApiNumberedIncomingCall

  * ScheduledCall

  * NumberedScheduledCall

  * AppsApiNumberedScheduledCall

  * DirectCall

  * SessionInitiatedCall

  * InternalCall




#### voicemail_reason

Enum values.

Value  | Meaning   
---|---  
0  | Not voicemail   
1  | Temporary redirection   
2  | After hours deflection   
3  | Overcapacity deflection   
4  | No input   
5  | No agent   
  
#### out_ticket_id_ext

External configured CRM ticket ID referencing this call.

### chat_participants

File type: Delta

Each member of a chat gets recorded as a **chat_participant**. If the same user leaves and rejoins a new **chat_participant** record is created. These records are stateful and typically not used for metrics.

#### id

Primary key identifier for records.

#### chat_id

References the chats records primary key **id**.

#### connected_at

Timestamp the participant connected into the chat.

#### created_at

Timestamp when this record was created at.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### finished_at

Timestamp when the participant left the chat.

#### status

Enum values.

Value  | Meaning   
---|---  
0  | Connecting   
1  | Invited   
2  | Connected   
3  | Wrapping up   
4  | Finished   
5  | Failed   
6  | Resuming   
7  | Post session in progress   
  
#### type

Enum values.

Value  | Meaning   
---|---  
0  | End-user   
1  | Agent   
2  | Manager   
3  | Virtual agent   
4  | External agent   
5  | Task virtual agent   
  
#### lang

ISO 639-1 language locale codes.

#### **menu_path_id**

References the **menu_paths** table by primary key **id**.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

#### user_id

References the users table by primary key **id**.

#### virtual_agent_id

References the virtual agents table by primary key **id**.

### chats

File type: Delta

Each chat is represented by a single record in this set. Metrics are typically not derived from data on this set as it is stateful in nature.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### assigned_at

Deprecated. The timestamp the chat was assigned to an agent at. Use **perf_chat_queue_durations** records ended_at timestamps.

#### canceled_at

Timestamp the chat was canceled by an end-user. NULL if never canceled.

#### created_at

Timestamp when this record was created at.

#### device_id

Reference to a device if a device is present.

#### disconnected_by

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Human agent   
2  | End-user   
3  | Virtual agent   
  
#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### ends_at

Timestamp when the chat ended.

#### fail_reason

Enum value.

Value  | Meaning   
---|---  
0  | No failure   
1  | Unknown   
2  | No response   
3  | Expired   
4  | After hours   
31  | Expired menu selection   
41  | End-user opt out   
50001  | Overcapacity to email   
60001  | Queue group deleted without substitute   
70000  | Pre-session deflection unknown   
70001  | Pre-session deflection timeout   
70002  | Pre-session deflection message delivery failed   
80000  | SMS error   
90000  | Force ended   
  
#### finish_reason

Enum value.

Value  | Meaning   
---|---  
0  | No specific reason   
1  | No response   
2  | Timeout waiting for agent message   
3  | Timeout waiting for end-user message   
4  | Timeout agent stopped   
5  | Timeout end-user stopped   
6  | End-user opt out   
  
#### first_msg_sent_at

Timestamp when the first chat message was sent.

#### in_queue_priority

The priority value for this chat while it was enqueued.

#### lang

ISO 639-1 language locale codes.

#### last_agent_msg_sent_at

Deprecated.

#### last_end_user_msg_sent_at

Deprecated.

#### last_msg_sent_at

Timestamp when the last chat message was sent by any participant.

#### materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### menu_id

Relationship to menus using the primary key **id**

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### out_ticket_id

External configured CRM ticket ID referencing this chat.

#### out_ticket_url

External configured CRM ticket URL referencing this chat.

#### rating

CSAT rating for this chat.

#### repeated

Boolean whether this end-user appears to be a repeat entry.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Queued   
1  | Assigned   
2  | Finished   
3  | Canceled   
4  | Failed   
10  | Dismissed   
11  | Selecting   
20  | Virtual agent assigned   
21  | Virtual agent dismissed   
  
#### timeout_at

Timestamp when the chat last timed out.

#### type

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Mobile   
2  | Web   
3  | Session initiated   
4  | SMS   
5  | Whatsapp   
  
#### verifiable

Boolean indicating whether the device has support for verification by fingerprint.

#### verified

End-user has been verified.

#### transcript_sent

If the end-user has requested a transcript be emailed this will have the timestamp of that delivery.

#### dismissed_count

Number of times this chat has been dismissed.

#### auto_answered

Boolean indicating whether the call was auto answered.

#### answer_type

Enum value.

Value  | Meaning   
---|---  
0  | Manual   
1  | Automatic   
2  | Outbound   
3  | Deflection   
  
#### after_hours

Set to true if this chat was created after hours.

### comm_escalations

File type: Delta

Tracks the escalation details for wait-time virtual agents.

#### id

The primary key ID for this record.

#### call_id

The call ID.

#### created_at

The time when this record was created.

#### in_queue_wait_time_va_start

The time when the wait-time virtual agent began waiting in queue for this call.

#### in_queue_wait_time_va_end

The time when the wait-time virtual agent finished waiting in queue for this call.

#### in_queue_wait_time_va_duration

The duration in seconds that the wait-time virtual agent waited in queue for this call.

#### wait_time_va_event_count

The number of events sent to wait-time virtual agent while it waited in queue for this call.

### comm_transfers

File type: Delta

Each transfer is represented by a single record in this set. Metrics are typically not derived from data on this table as it is stateful in nature.

#### id

Primary key identifier for records.

#### answer_type_path

Enum value.

Value  | Meaning   
---|---  
0  | Manual to manual   
1  | Manual to auto   
2  | Auto to manual   
3  | Auto to auto   
  
#### assigned_at

Deprecated. The timestamp the chat was assigned to an agent at. Use **perf_chat_queue_durations** records ended_at timestamps.

#### cold

Boolean indicating if this was a cold transfer or not.

#### comm_id

Used as a composite key with **comm_type**. 

#### comm_type

The type of communication channel this references. It is used as a composite key used to join the correct type of data using **comm_id**.

Value  | Composite Key   
---|---  
Call  | Use **comm_id** to join to calls data on the primary key **id**   
Chat  | Use **comm_id** to join to chats data on the primary key **id**   
Session  | Use **comm_id** to join to sessions data on the primary key **id**   
  
#### connected_at

Deprecated. Derived from **perf_call_handle_durations** or **perf_chat_handle_durations** records using started_at plus the time in seconds in the **wait_duration** value. Depends on the value of **comm_type** to dictate which handle durations dataset should be referenced.

#### created_at

Timestamp when this record was created at.

#### current

Boolean indicating that this transfer is ongoing.

#### deflection

Enum value.

Value  | Meaning   
---|---  
0  | No Deflection   
1  | Deflecting   
2  | Over capacity to phone   
3  | Over capacity to voicemail   
4  | Over capacity to callback   
5  | Over capacity to continue waiting   
6  | Over capacity play message   
7  | Over capacity announce estimated wait   
8  | Over capacity to queue   
100  | After hours to voicemail   
101  | After hours to phone   
102  | After hours play message only   
103  | After hours to queue   
104  | After hours play message   
200  | Temporary redirection to phone   
201  | Temporary redirection to message   
202  | Temporary redirection to voicemail   
203  | Temporary redirection to queue   
205  | Temporary redirection to SIP   
300  | IVR pre-session deflection   
400  | Virtual agent redirection to phone   
401  | Virtual agent redirection to SIP   
  
#### fail_reason

Enum value.

Value  | Meaning   
---|---  
0  | No failure   
1  | Timeout   
2  | Canceled   
10  | Agent connection timeout   
20  | Virtual agent failure   
  
#### from_agent_id

References the users table by primary key **id**. Agent the interaction is being transferred from.

#### **from_menu_path_id**

References the **menu_paths** table by primary key **id**. Menu path this transfer comes from.

#### from_queue_priority_level

The priority level of the menu the transfer came from.

#### queue_priority_level

The priority level of the menu the transfer enqueued into.

#### session_id

Calls and chants are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Transferring   
1  | Transferred   
2  | Failed   
3  | Deflected   
  
#### to_agent_id

References the users table by primary key **id**. Agent is being transferred to if direct to agent transfer.

#### to_**menu_path_id**

References the **menu_paths** table by primary key **id**. Menu path this transfer is going to.

#### updated_at

Timestamp when this last record was updated.

#### to_virtual_agent_id

References the **virtual_agents** table by primary key **id**. Virtual agent being transferred to.

#### to_lang

ISO 639-1 language locale codes. The language transferred to.

#### from_lang

ISO 639-1 language locale codes. The language transferred from.

### company_locations

File type: Full

This is associative data for users to tie them to a particular location.

#### id

Primary key identifier for records.

#### created_at

Timestamp when this record was created at.

#### lang

ISO 639-1 language locale codes.

#### location

The name of the location.

#### updated_at

Timestamp when this last record was updated.

#### pop_settings

JSON data specifying PoP overrides for various telephony carriers.

### deflection_history_logs

File type: Delta

Whenever a deflection takes place within the platform it is logged in this set.

#### id

Primary key identifier for records.

#### call_id

References the calls records primary key **id**.

#### created_at

Timestamp when this record was created at.

#### deflection

Enum value.

Value  | Meaning   
---|---  
0  | No deflection   
1  | Deflecting   
2  | Over capacity to phone   
3  | Over capacity to voicemail   
4  | Over capacity to callback   
5  | Over capacity to continue waiting   
6  | Over capacity play message   
7  | Over capacity play estimated wait   
8  | Over capacity to queue   
100  | After hours to voicemail   
101  | After hours to phone   
102  | After hours play message only   
103  | After hours to queue   
104  | After hours play message   
200  | Temporary redirection to phone   
201  | Temporary redirection to message   
202  | Temporary redirection to voicemail   
203  | Temporary redirection to queue   
205  | Temporary redirection to SIP   
300  | IVR pre-session deflection   
400  | Virtual agent redirection to phone   
401  | Virtual agent redirection to SIP   
  
#### details

JSON data with extra context of the deflection.

#### from_lang

ISO 639-1 language locale codes. The language deflected from.

#### from_materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **from_menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### from_materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **from_menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### from_menu_path_id

References the **menu_paths** table by primary key **id**. The menu path deflected from.

#### to_lang

ISO 639-1 language locale codes. The language deflected to.

#### to_materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **to_** menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### to_materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **to_** menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### to_menu_path_id

References the **menu_paths** table by primary key **id**. The menu path deflected to.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

### deflection_sip_uris

File type: Full

SIP URI that are used for deflection.

#### id

Primary key identifier for records.

#### uri

String value for this record.

### deflection_urls

File type: Full

URLs used for deflection.

#### id

Primary key identifier for records.

#### url

String value for this record.

### disposition_agent_inputs

File type: Delta

When an agent submits a disposition it gets recorded in this set.

#### id

Primary key identifier for records.

#### comm_id

Used as a composite key with **comm_type**.

#### comm_type

The type of communication channel this references. It is used as a composite key used to join the correct type of data using **comm_id**.

Value  | Relationship  | Composite Key   
---|---|---  
Call  | calls  | Use **comm_id** to join to calls data on the primary key **id**.   
Call  | `call_participants`  | Use **comm_id** to join to `call_participants` on the primary key **id**.   
Chat  | chats  | Use **comm_id** to join to chats data on the primary key **id**.   
Chat  | chat_participants  | Use **comm_id** to join to chat_participants on the primary key **id**.   
Session  | sessions  | Use **comm_id** to join to sessions data on the primary key **id**.   
  
#### user_id

References the users table by primary key **id**.

#### participant_id

Used as a composite key with **comm_type**.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

#### code_id

References the **disposition_codes** table by primary key **id**.

#### crm_reference_id

Deprecated.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

### disposition_codes

File type: Full

Actual disposition codes selected by agents when completing a disposition input.

#### id

Primary key identifier for records.

#### name

Name of the disposition code.

#### deleted_at

Timestamp when the code was soft deleted.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

#### enabled

Whether the disposition code is currently enabled.

### email_accounts

File type: Full

Configurations of email accounts used for email channel types.

#### id

Primary key identifier for records.

#### email_service

One of the following values:

  * genericIMAP

  * oauthIMAP




#### incoming_server_host

IMAP mail server host.

#### incoming_server_port

IMAP mail server port.

#### sender_server_host

SMTP host for sending email

#### sender_server_port

SMTP post for sending email

#### has_folder

#### email_id

References the email address the consumer sent their email to.

#### status

One of the following values:

  * valid

  * invalid




### imap_sync_info

JSON data detailing where IMAP sync process is currently at for mailbox, email, and message UID.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

#### deleted_at

Timestamp when this record was soft deleted.

#### oauth_linked

Boolean indicating that this server is authenticating with oAuth.

### email_supports

File type: Delta

Each email used in email channel types gets a record in this table. This is a stateful table used to ensure emails are assigned and handled accordingly.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### session_id

Emails are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### email_account_id

References the email_accounts table by primary key **id**.

#### priority

Email message's priority value enqueued for a response.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### out_ticket_id

External configured CRM ticket ID referencing this email.

#### out_ticket_url

External configured CRM ticket URL referencing this email.

#### latest_email_thread_id

Current email thread ID

#### transfer_count

Deprecated. Count of transfers. Use **perf_email_queue_durations** where transfer = 1

#### total_thread_numbers

Total threads for this email.

#### in_queue_priority

The priority value for this email while it was enqueued.

#### menu_id

Relationship to menus using the primary key **id**

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### menu_type

String with the following possible values

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * email_menu




#### lang

ISO 639-1 language locale codes.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Unopened   
1  | Active   
2  | Paused   
3  | Resolved   
4  | Closed   
5  | Reopened   
  
#### finished_at

Timestamp this email support was finished.

#### queue_priority_level

The priority level of the menu the email support enqueued into.

#### user_priority

The priority level of the end-user that created the email support.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

#### materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### is_out_ticket_account

Boolean dictating whether CRM integrations are working with a ticket or contact entity. When false it is doing the default CRM integration with tickets. When true it is a contact object that is being updated.

### end_user_activity_logs

File type: Delta

All end-users have a variety of interactions while their inquiries traverse the platform. Each notable interaction is logged here.

#### id

Primary key identifier for records.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### activity

Enum value.

Value  | Meaning   
---|---  
100100  | Deflected to after hours queue   
100101  | Deflected to after hours message   
100102  | Deflected to after hours scheduled call   
100103  | Deflected to after hours phone   
100104  | Deflected to after hours email   
100106  | Deflected to after hours voicemail   
100200  | Deflected to manual redirection queue   
100201  | Deflected to manual redirection message   
100204  | Deflected to manual redirection phone   
100205  | Deflected to manual redirection URL   
100206  | Deflected to manual redirection voicemail   
100209  | Deflected to manual redirection SIP   
100300  | Deflected to cver capacity queue   
100301  | Deflected to over capacity message   
100302  | Deflected to over capacity scheduled call   
100303  | Deflected to over capacity email   
100304  | Deflected to over capacity phone   
100306  | Deflected to over capacity voicemail   
100307  | Deflected to over capacity callback   
100308  | Deflected to over capacity keep waiting   
100400  | Deflected to virtual agent redirection phone   
100401  | Deflected to virtual agent redirection SIP   
100800  | Deflected to pre-session SMS   
101000  | Email sent   
101001  | Email sent after hours   
101003  | Email sent over capacity   
103001  | Call scheduled after hours   
103003  | Call scheduled over capacity   
104001  | Phone dialed after hours   
104002  | Phone dialed manual redirection   
104003  | Phone dialed over capacity   
104004  | Phone dialed virtual agent redirection   
105001  | Voicemail left after hours   
105002  | Voicemail left manual redirection   
105003  | Voicemail left over capacity   
106010  | Link clicked after hours message   
106020  | Link clicked manual redirection message   
106021  | Link clicked manual redirection URL   
106030  | Link clicked over capacity message   
107000  | External deflection link selected   
107001  | External deflection link selected after hours   
107003  | External deflection link selected over capacity   
108002  | SIP dialed manual redirection   
108003  | SIP dialed virtual agent redirection   
200100  | Email selected   
  
#### created_at

Timestamp when this record was created at.

#### lang

ISO 639-1 language locale codes.

#### menu_type

String with the following possible values:

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * email_menu




#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### call_id

References the calls records primary key **id**.

#### chat_id

References the chats records primary key **id**.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### to_url_id

References the **deflection_urls** table by primary key **id**.

#### to_email

If the end-user was deflected to an email address it is stored here.

#### to_menu_type

String with the following possible values:

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * email_menu




#### to_menu_path_id

References the **menu_paths** table by primary key **id**. Menu path the end user was directed to.

#### to_materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using to_**menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### to_materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using to_**menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### to_phone_number

Phone number the end-user was deflected to.

#### to_sip_uri_id

References the **deflection_sip_uris** table by primary key **id**.

### end-users

File type: Delta

A record representing a unique end-user.

#### id

Primary key identifier for records.

#### created_at

Timestamp when this record was created at.

#### identifier

Unique external identifier provided.

#### need_assignment

Boolean indicating if this end-user needs assignment to an external CRM as a contact.

#### out_contact_id

External CRM ID for this end-user.

#### out_contact_type

Enum value.

Value  | Meaning   
---|---  
0  | Normal (CRM Lookup)   
1  | SIP lookup   
2  | External API lookup   
  
#### to_be_deleted

Boolean indication if the end-user flagged for permanent deletion.

#### updated_at

Timestamp when this last record was updated.

### menu_channel_assignments

File type: Full

Relational data between users, teams, and menus.

#### assignee_id

Used as a composite key with **assignee_type**.

#### assignee_type

The type of assignee this references. It is used as a composite key used to join the correct type of data using **assignee_id**.

Value  | Composite Key   
---|---  
User  | Use **assignee_id** to join to users data on the primary key **id**.   
Team  | Use **assignee_id** to join to teams data on the primary key **id**.   
  
#### channel_type

Enum value.

Value  | Meaning   
---|---  
0  | Session   
1  | Chat   
2  | Voice call   
3  | Video call   
4  | Voicemail   
5  | Email   
  
#### group_id

Relationship to **menu_queue_groups** using the primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_id

Relationship to menus using the primary key **id**

### menu_queue_groups

File type: Full

Cascade and percent allocation group configurations for menus.

#### id

Primary key identifier for records.

#### channel

Enum value.

Value  | Meaning   
---|---  
0  | Session   
1  | Chat   
2  | Voice call   
3  | Video call   
4  | Voicemail   
5  | Email   
  
#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### group_level

Nested level of group where 0 is no cascade groups and any positive value represents level of cascade.

#### lang

ISO 639-1 language locale codes.

#### menu_id

Relationship to menus using the primary key **id**

#### percent

If this record is a percent allocation group the percentage is represented here.

#### routing_algorithm

Enum value. Indicates the type of menu assignment.

Value | Meaning  
---|---  
0 | `assignment_based`  
1 | `skills_based`  
  
### menu_path_items

File type: Full

Individual components of a **menu_path**.

#### id

Primary key identifier for records.

#### menu_id

Relationship to menus using the primary key **id**

#### path_id

Relationship to **menu_paths** using the primary key **id**

#### position

Hierarchical position with 0 being a leaf menu.

### menu_paths

File type: Full

Menu paths are at the core of queue level metrics. They represent materialized paths based on their hierarchical configuration. A queue is a combination of the **menu_path_id** and lang when it comes to generated queue level metrics.

As an example, two menus are configured for English and are called shipping and order tracking. Both initially exist without any parent menu. As traffic enters these queues they will have a menu path materialize.

If order tracking is moved to be under shipping it will generate shipping or order tracking which forms a third menu path. All the metrics that were associated with shipping and order tracking will still remain associated with their former menu paths. Shipping or order tracking will start generating new metrics for that specific menu path.

#### id

Primary key identifier for records. Commonly referenced in other datasets as **menu_path_id**.

#### items_count

The number of menus in the hierarchy.

#### materialized_path

Menu ID representation of the complete menu path

#### name

Menu name representation of the complete menu path. It is not recommended to use this value when dealing with multiple menu languages.

### menu_settings

File type: Full

Menu settings contain many configurations, but one of the most important for reporting is that each menu and language combination generates one record. This means when determining metrics for a queue joining to this table on menu_id and lang to get the language specific name is necessary.

#### id

Primary key identifier for records.

#### after_hours

JSON containing menu after hours settings.

#### auto_answer_enabled

Boolean indicating this menu has auto answer enabled.

#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### enabled

Boolean indicating this menu and its ancestors are enabled.

#### enabled_self

Boolean indicating this menu is enabled.

#### hidden

Boolean to configure whether this menu is presented to end-users for selection.

#### lang

ISO 639-1 language locale codes.

#### menu_id

Relationship to menus using the primary key **id**

#### name

Language specific name for this menu.

#### output_msg

Deprecated

#### over_cap_deflection

JSON containing over capacity deflection settings.

#### redaction_enabled

Boolean controlling whether this menu should support redaction.

#### redirection

Deprecated. See redirection_v2.

#### redirection_v2

JSON containing redirection settings.

#### sms_smart_action_enabled

Boolean controlling whether this menu should support SMS smart actions.

#### updated_at

Timestamp when this last record was updated.

#### use_queue_priority

For communications enqueued to this menu this will dictate whether the queue priority should be applied.

#### use_voice_file

Configuration to play voice file upon menu selection or not.

#### voice_file

URL location of the voice file.

#### wait_time_sms

JSON configuration for wait time over SMS.

#### wait_time_sms_enabled

Boolean controlling if wait time for SMS is enabled.

#### collect_email_for_call

Boolean controlling the collection of end-user email for calls.

#### collect_email_for_chat

Boolean controlling the collection of end-user email for chats.

#### sms

JSON for SMS settings.

### menus

File type: Full

Menus are language entries representing each menu. Language specifications are noted in **menu_settings**.

#### id

Primary key identifier for records.

#### children_count

The number of child menus nested in this menu.

#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### hidden

Deprecated. See **menu_settings.hidden**

#### name

Deprecated. See **menu_settings.name**

#### output_msg

Deprecated. See **menu_settings.output_msg**

#### parent_id

References the same menus data by primary key **id**.

#### position

Hierarchical position with 0 being a leaf menu.

#### type

String with the following possible values

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * whats_app_menu

  * email_menu




#### updated_at

Timestamp when this last record was updated.

### native_campaigns

File type: Full

Dialer campaigns and their configurations.

#### id

Primary key identifier for records. 

#### queue_id

Relationship to menus using the primary key **id**.

#### mode

Enum value.

Value  | Meaning   
---|---  
0  | Progressive   
1  | Preview   
2  | Predictive   
  
#### name

Name of the campaign.

#### starts_at

Timestamp when the campaign starts.

#### ends_at

Timestamp when the campaign ends.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Created   
1  | Started   
2  | Dialing   
3  | Pause   
4  | Finished   
5  | Deleted   
  
#### target_number_to_process

The number of contacts outstanding to be dialed.

#### ringing_timeout

Timeout in seconds to wait for ringing.

#### overdial_adjustment_multiplier

The amount we multiply the current over-dial rate by when re-calculating the over-dial rate.

#### max_abandonment_percent

The maximum percent ratio of abandoned by dialer contacts divided by successfully reached contacts including abandoned by dialer contacts. Prevents over-dialing when abandonment percentage is breached.

#### abandoned_by_dialer_audio_setting

JSON container data about audio to play when a contact answers without an available agent.

#### redial_interval_minutes

The number of minutes between redials.

#### max_redial_count

Maximum redials of a contact for this campaign

#### campaign_type

Enum value.

Value  | Meaning   
---|---  
0  | Default   
1  | External list   
  
#### external_campaign_id

When the campaign type is an external list this references the external campaign ID.

#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### updated_at

Timestamp when this last record was updated.

#### lang

ISO 639-1 language locale codes.

### perf_call_campaign_contact_details

File type: Delta

Part of interaction based reporting. References the details of a contact in an outbound dialer campaign.

#### id

Primary key identifier for records.

#### call_id

References the calls records primary key **id**.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### event_id

Deprecated. References null entity

#### campaign_id

References the native_campaigns records primary key **id**.

#### contact_id

References contacts table that is not included. Data point only.

#### status

Enum value.

Value  | Meaning   
---|---  
2  | Not picked up   
5  | Not reachable   
6  | Finished   
7  | Canceled   
8  | Do not call   
9  | Invalid phone number   
11  | Carrier error   
12  | Transferred   
13  | Abandoned by dialer   
14  | Machine detected   
15  | General error   
16  | Finished after transfer   
18  | Do not call number   
19  | Invalid outbound number   
20  | Blocked phone number   
  
#### redial_attempts

Number of total redial attempts.

#### active_talk_duration

The duration in seconds both the agent and end-user were connected.

#### abandoned_call_message_played_at

Timestamp when the abandoned call message was played.

#### speak_started_at

Timestamp when end-user speaking began upon initial answer. If the answering machine was detected the duration of the message is added to this timestamp.

#### speak_ended_at

Timestamp when end-user speaking ended upon initial answer.

#### ended_at

Timestamp when the contact ended the call.

#### connected_at

Timestamp when the contact entered the call.

#### dialed_at

Timestamp when the contact was dialed.

#### created_at

Timestamp when this record was created at.

### perf_call_cobrowse_details

File type: Delta

Part of interaction based reporting. Each record is a single Screen Share interaction.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### call_id

References the calls records primary key **id**.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### started_by

NULL when started by an End-user, otherwise the value represents the users record that started this Screen Share session. Joined by primary key **id** of users.

#### ended_by

NULL when started by an end-user, otherwise the value represents the users record that ended this Screen Share session. Joined by primary key **id** of users.

#### started_at

Timestamp when the Screen Share session started.

#### ended_at

Timestamp when the Screen Share session ended.

#### remote_controlled

Boolean indicating whether remote control was used during the session.

#### device_name

Device name from client SDK from Screen Share.

### perf_call_handle_durations

File type: Delta

Part of interaction based reporting. Each record is a unique agent interaction on a call. Commonly used for metrics such as hold duration, handle time, talk time, and after or before call work.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
0  | Call finished   
1  | Call abandoned   
2  | Call failed   
3  | ACW ended   
4  | BCW ended   
  
#### call_duration

For event types of 0, 1, and 2 this is the duration of seconds between started_at and ended_at

#### acw_duration

For event types of 3 this is the duration of seconds between started_at and ended_at

#### bcw_duration

For event types of 4 this is the duration of seconds between started_at and ended_at

#### barged

Boolean indicating if this interaction was barged by another user.

#### campaign_mode

Enum value.

Value  | Meaning   
---|---  
0  | Progressive   
1  | Preview   
2  | Predictive   
  
#### network_quality_score

Integer score of 1 through 5 where 5 is the best describing the agent connectivity quality during the call.

#### breakthrough_projection

Boolean that if true would mean this interaction was answered through breakthrough projection.

#### status_id_before_breakthrough

Status ID of the agent prior to breakthrough. See breakthrough_projection

#### call_id

References the calls records primary key **id**.

#### origin_call_id

References the calls records primary key **id**. Reflects a parent call record.

#### call_type

A string with the following possible values:

  * `**IncomingCall**`. An inbound call from a support number.
  * `**NumberedIncomingCall**`. An inbound call from a support number to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**IvrCall**`. An inbound call from an ordinary phone dial, handled by an IVR entry point.
  * `**InAppIvrCall**`. An inbound call initiated in-app, handled by an IVR entry point.
  * `**AppsApiNumberedIncomingCall**`. An inbound call, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**ScheduledCall**`. A callback scheduled for later.
  * `**NumberedScheduledCall**`. A scheduled callback to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**AppsApiNumberedScheduledCall**`. A scheduled callback, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**DirectCall**`. A call that bypasses IVR or queue entry and is directed to a specific agent or endpoint.
  * `**InternalCall**`. An internal agent-to-agent or agent-to-conference call.



#### inbound

Boolean that if true would indicate this was an inbound call interaction.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### transfer_cold

Boolean that indicates a transfer to have been cold if true.

#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### agent_id

References the users table by primary key **id**.

#### started_at

Timestamp when the interaction started.

#### ended_at

Timestamp when the interaction ended.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### hold_duration

The sum of time in seconds that this agent had placed an end-user on hold.

#### scheduled_at

If applicable, timestamp when this call interaction was scheduled.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### wait_duration

The duration in seconds that it took the agent to become connected into the call once being assigned to it.

### perf_call_presession_deflections

File type: Delta

Part of interaction based reporting. Reports on end-user interactions that switched communication channels prior to session with an agent on the original communication channel.

#### id

Primary key identifier for records.

#### event_id

Deprecated. References null entity

#### call_id

References the calls records primary key **id**.

#### call_menu_path_id

References the **menu_paths** table by primary key **id**. The original call's menu path prior to deflection.

#### call_lang

ISO 639-1 language locale codes. The original call's language prior to deflection.

#### to_comm_id

Used as a composite key with **comm_type**.

#### to_comm_type

The type of communication channel this references. It is used as a composite key used to join the correct type of data using **comm_id**.

Value  | Composite Key   
---|---  
Call  | Use **comm_id** to join to calls data on the primary key **id**   
Chat  | Use **comm_id** to join to chats data on the primary key **id**   
Session  | Use **comm_id** to join to sessions data on the primary key id   
  
#### to_menu_path_id

References the **menu_paths** table by primary key **id**. Menu path deflected to.

#### to_lang

ISO 639-1 language locale codes. The language deflected to.

#### deflection_channel

Enum value.

Value  | Meaning   
---|---  
0  | SMS   
  
#### status

Enum value.

Value  | Meaning   
---|---  
0  | Declined   
1  | Invalid or no input   
2  | Finished   
3  | Failed   
  
#### fail_reason

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Message delivery failed   
2  | Timeout   
3  | Invalid configuration   
  
#### started_at

Timestamp when the pre-session deflection interaction began.

#### ended_at

Timestamp when the pre-session deflection interaction ended.

#### duration

Duration in seconds that the interaction lasted for.

### perf_call_queue_durations

File type: Delta

Part of interaction based reporting. Queue level interactions that are used for metrics such as SLA, queue duration, and abandonment rates. Note that **agent_id** is present on queued interactions as a signal to how the interaction terminated. The agent has no responsibility to any of the metrics.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
0  | Answered   
1  | Recovered   
2  | Deflected   
3  | Abandoned   
4  | Failed   
  
#### call_id

References the calls records primary key **id**.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### **menu_path_id**

References the **menu_paths** table by primary key **id**.

#### cold_transfer

Boolean that indicates a transfer to have been cold if true.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### queue_duration

Duration in seconds this interaction was enqueued.

#### started_at

Timestamp when the interaction was enqueued

#### ended_at

Timestamp when the interaction ended.

#### agent_id

References the users table by primary key **id**.

#### call_type

A string with the following possible values:

  * `**IncomingCall**`. An inbound call from a support number.
  * `**NumberedIncomingCall**`. An inbound call from a support number to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**IvrCall**`. An inbound call from an ordinary phone dial, handled by an IVR entry point.
  * `**InAppIvrCall**`. An inbound call initiated in-app, handled by an IVR entry point.
  * `**AppsApiNumberedIncomingCall**`. An inbound call, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**ScheduledCall**`. A callback scheduled for later.
  * `**NumberedScheduledCall**`. A scheduled callback to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**AppsApiNumberedScheduledCall**`. A scheduled callback, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**DirectCall**`. A call that bypasses IVR or queue entry and is directed to a specific agent or endpoint.
  * `**InternalCall**`. An internal agent-to-agent or agent-to-conference call.



#### fail_reason

Deprecated. Use **calls.fail_reason**

#### fail_details

Deprecated. Use **calls.fail_details**

#### service_level_abandon_time_threshold

This is a snapshot of the short abandon threshold when this record had enqueued.

#### service_level_target_time

The duration in seconds that this record's **queue_duration** would need to meet to be considered in SLA snapshotted at the time this record was created.

#### service_level_event

Enum value.

Value  | Meaning   
---|---  
0  | Excluded   
1  | In SLA   
2  | Not In SLA   
  
#### service_level_target_percent

This is a snapshot of the target percentage when this record was enqueued.

### perf_call_smart_actions

File type: Delta

Part of interaction based reporting. Smart actions during a call have their interactions recorded here.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### call_id

References the calls records primary key **id**.

#### type

Enum value.

Value  | Meaning   
---|---  
0  | Verification   
1  | Photo   
2  | Video   
3  | Screenshot   
4  | Text   
5  | Payment   
6  | Cobrowse   
7  | Task virtual agent   
  
#### sub_type

Enum value.

Value  | Meaning  | 0  | In Session   
---|---  
1  | Pre-session   
  
#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### number_of_photos

Sum of photos sent during smart action interaction.

#### result

Enum value.

Value  | Meaning   
---|---  
0  | Triggered   
1  | Finished   
2  | Failed   
3  | Canceled   
4  | Notified   
  
#### duration

Duration in seconds the smart action interaction took place.

#### end_user_input_duration

Duration in seconds the smart action interaction after the end-user was sent the notification of the smart action.

#### notification_duration

Duration in seconds it took for the end-user to receive the notification.

#### lang

ISO 639-1 language locale codes.

#### started_at

The timestamp when the smart action interaction began.

#### ended_at

The timestamp when the smart action interaction ended.

#### interaction_started_at

The timestamp when the parent interaction began.

#### interaction_ended_at

The timestamp when the parent interaction ended.

### perf_call_va_deflected_escalations

File type: Delta

Part of interaction based reporting. When a Virtual Agent escalates to a queue but then experiences a queue deflection an interaction is logged here.

#### id

Primary key identifier for records.

#### call_id

References the calls records primary key **id**.

#### deflection

Enum value.

Value  | Meaning   
---|---  
0  | No deflection   
1  | Over capacity   
2  | Over capacity email   
3  | Over capacity virtual agent   
4  | Over capacity human agent   
10  | After hours   
11  | After hours email   
12  | After hours virtual agent   
20  | Over capacity to voicemail   
21  | Over capacity to phone   
22  | Over capacity to callback   
23  | Over capacity to wait   
24  | Over capacity to play message   
25  | Over capacity to queue   
30  | After hours voicemail   
31  | After hours phone   
32  | After hours message only   
33  | After hours message   
34  | After hours queue   
39  | Temporary redirection   
40  | Temporary redirection to phone   
41  | Temporary redirection to message   
42  | Temporary redirection to voicemail   
43  | Temporary redirection to queue   
44  | Temporary redirection to SIP   
50  | IVR pre-session deflection   
60  | Virtual agent redirection to phone   
61  | Virtual agent redirection to SIP   
  
#### escalation_id

References contacts table that is not included. Data point only.

#### escalation_reason

String enum value

Value  | Meaning   
---|---  
0  | Unknown   
1  | By end-user ask   
2  | By end-user message   
3  | By virtual agent   
4  | Payload failure   
5  | Could not resume   
6  | By human agent   
7  | Invalid Queue   
8  | Dismissed   
  
#### event

Enum value.

Value  | Meaning   
---|---  
0  | Virtual agent escalation deflected   
  
#### event_id

Deprecated. References null entity

#### lang

ISO 639-1 language locale codes.

#### **menu_path_id**

References the **menu_paths** table by primary key **id**.

#### time

Timestamp of the event being taking place.

#### virtual_agent_id

References the virtual agents table by primary key **id**.

### perf_call_va_handle_durations

File type: Delta

Part of interaction based reporting. Virtual agent interactions with end-users and agents.

#### id

Primary key identifier for records.

#### call_duration

Duration of seconds between **started_at** and **ended_at**.

#### call_id

References the calls records primary key **id**.

#### call_type

A string with the following possible values:

  * `**IncomingCall**`. An inbound call from a support number.
  * `**NumberedIncomingCall**`. An inbound call from a support number to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**IvrCall**`. An inbound call from an ordinary phone dial, handled by an IVR entry point.
  * `**InAppIvrCall**`. An inbound call initiated in-app, handled by an IVR entry point.
  * `**AppsApiNumberedIncomingCall**`. An inbound call, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**ScheduledCall**`. A callback scheduled for later.
  * `**NumberedScheduledCall**`. A scheduled callback to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**AppsApiNumberedScheduledCall**`. A scheduled callback, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**DirectCall**`. A call that bypasses IVR or queue entry and is directed to a specific agent or endpoint.
  * `**InternalCall**`. An internal agent-to-agent or agent-to-conference call.



#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### ended_at

The timestamp when the interaction ended.

#### escalation_reason

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | By end-user ask   
2  | By end-user message   
3  | By virtual agent   
4  | Payload failure   
5  | Could not resume   
6  | By human agent   
7  | Invalid queue   
8  | Dismissed   
  
#### event

Enum value.

Value  | Meaning   
---|---  
0  | Call finished   
1  | Call failed   
2  | Post session finished   
3  | Post session failed   
  
#### event_id

Deprecated. References null entity

#### fallback_response_count

Deprecated.

#### finish_reason

Enum value.

Value  | Meaning   
---|---  
0  | Undefined   
1  | Resolved   
2  | Unexpectedly ended   
3  | Escalated   
4  | Failed   
5  | Consumer ended   
  
#### initiated_by

Enum value.

Value  | Meaning   
---|---  
0  | End-user   
1  | Human agent   
2  | Post session   
  
#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### response_count

The count of responses made by the virtual sgent to the end-user inputs.

#### sentiment

Sentiment score of the interaction.

#### started_at

The timestamp when the interaction began.

#### time

The timestamp when the interaction was recorded.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### transfer_id

References the **comm_transfers** table by primary key **id**.

#### virtual_agent_id

References the **virtual_agents** table by primary key **id**.

### perf_chat_cobrowse_details

File type: Delta

Part of interaction based reporting. Each record is a single Screen Share interaction.

#### agent_id

References the users table by primary key **id**.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### chat_id

References the chats records primary key **id**.

#### session_id

Chats are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### started_by

NULL when started by an end-user, otherwise the value represents the users record that started this Screen Share session. Joined by primary key **id** of users.

#### ended_by

NULL when started by an end-user, otherwise the value represents the users record that ended this Screen Share session. Joined by primary key **id** of users.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

#### remote_controlled

Boolean indicating whether remote control was used during the session.

#### device_name

Device name from client SDK from Cobrowse.

### perf_chat_deflected_escalations

File type: Delta

Part of interaction based reporting. When a virtual agent escalates to a queue but then experiences a queue deflection an interaction is logged here.

#### id

Primary key identifier for records.

#### chat_id

References the chats records primary key **id**.

#### event

String value describing the event that triggered the deflection.

#### time

Timestamp of the deflected escalation.

#### virtual_agent_id

References the **virtual_agents** table by primary key **id**.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### deflection

Enum value.

Value  | Meaning   
---|---  
0  | No deflection   
1  | Over capacity   
2  | Over capacity email   
3  | Over capacity virtual agent   
4  | Over capacity human agent   
10  | After hours   
11  | After hours email   
12  | After hours virtual agent   
20  | Over capacity to voicemail   
21  | Over capacity to phone   
22  | Over capacity to callback   
23  | Over capacity to wait   
24  | Over capacity to play message   
25  | Over capacity to queue   
30  | After hours voicemail   
31  | After hours phone   
32  | After hours message only   
33  | After hours message   
34  | After hours queue   
39  | Temporary redirection   
40  | Temporary redirection to phone   
41  | Temporary redirection to message   
42  | Temporary redirection to voicemail   
43  | Temporary redirection to queue   
44  | Temporary redirection to SIP   
50  | IVR pre-session deflection   
60  | Virtual agent redirection to phone   
61  | Virtual agent redirection to SIP   
  
#### escalation_reason

Enum value.

Value  | Meaning  |   
---|---|---  
0  | Unknown  |   
1  | By end-user ask  |   
2  | By end-user message  |   
3  | By virtual agent  |   
4  | Payload failure  |   
5  | Could not resume  |   
6  | By human agent  |   
7  | Invalid queue  |   
8  | Dismissed  |   
  
### perf_chat_handle_durations

File type: Delta

Part of interaction based reporting. Each record is a unique agent interaction on a call. Commonly used for metrics such as response count/duration, handle time, and after call work.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
0  | Chat finished   
1  | Chat abandoned   
2  | Chat failed   
3  | ACW ended   
  
#### chat_duration

For event types of 0, 1, and 2 this is the duration of seconds between started_at and ended_at

#### acw_duration

For event types of 3 this is the duration of seconds between started_at and ended_at

#### chat_id

References the chats records primary key **id**.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### agent_id

References the users table by primary key **id**.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

#### reactivated

Boolean indicating if this interaction was reactivated after dismissal.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### response_count

The count of agent responses to end-user chats.

#### response_time_avg

The average time agent responses took after the previous end-user message.

#### response_time_max

The maximum time agent responses took after the previous end-user message.

#### response_time_total

The total time agent responses took after the previous end-user message.

#### session_id

Chats are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### type

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Mobile   
2  | Web   
3  | Session initiated   
4  | SMS   
5  | Whatsapp   
  
#### wait_duration

The duration in seconds that it took the agent to become connected into the chat once being assigned to it.

#### inbound

Boolean that if true would indicate this was an inbound interaction.

#### sub_type

Enum value.

Value  | Meaning   
---|---  
0  | End-user initiated   
1  | Agent initiated   
2  | API initiated   
  
### perf_chat_queue_durations

File type: Delta

Part of interaction based reporting. Queue level interactions that are used for metrics such as SLA, queue duration, and abandonment rates. Note that **agent_id** is present on queued interactions as a signal to how the interaction terminated. The agent has no responsibility to any of the metrics.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
0  | Answered   
1  | Abandoned   
2  | Failed   
  
#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### chat_id

References the chats records primary key **id**.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### queue_duration

Duration in seconds this interaction was enqueued.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

#### reactivated

Boolean indicating if this interaction was reactivated after dismissal.

#### agent_id

References the users table by primary key **id**.

#### type

Enum value.

Value  | Meaning   
---|---  
0  | Unknown   
1  | Mobile   
2  | Web   
3  | Session initiated   
4  | SMS   
5  | Whatsapp   
  
#### fail_reason

Deprecated. Use chats.fail_reason

#### service_level_abandon_time_threshold

When this record is enqueued this is a snapshot of the short abandon threshold.

#### service_level_target_time

The duration in seconds that this record's queue_duration would need to meet to be considered in SLA snapshotted at the time this record was created.

#### service_level_event

Enum value.

Value  | Meaning   
---|---  
0  | Excluded   
1  | In SLA   
2  | Not in SLA   
  
#### service_level_target_percent

When this record is enqueued this is a snapshot of the target percentage.

### perf_chat_smart_actions

File type: Delta

Part of interaction based reporting. Smart actions during a call have their interactions recorded here.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### chat_id

References the chats records primary key **id**.

#### type

Enum value.

Value  | Meaning   
---|---  
0  | Verification   
1  | Photo   
2  | Video   
3  | Screenshot   
4  | Text   
5  | Payment   
6  | Cobrowse   
7  | Task virtual agent   
  
#### sub_type

Enum value.

Value  | Meaning   
---|---  
0  | In session   
1  | Pre-session   
  
#### number_of_photos

Quantity of photos sent in smart action.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### result

Enum value.

Value  | Meaning   
---|---  
0  | Triggered   
1  | Finished   
2  | Failed   
3  | Canceled   
4  | Notified   
  
#### duration

Duration in seconds the smart action interaction took place.

#### end_user_input_duration

Duration in seconds the smart action interaction after the end-user was sent the notification of the smart action.

#### notification_duration

Duration in seconds it took for the end-user to receive the notification.

#### lang

ISO 639-1 language locale codes.

#### started_at

The timestamp when the smart action interaction began.

#### ended_at

The timestamp when the smart action interaction ended.

#### interaction_started_at

The timestamp when the parent interaction began.

#### interaction_ended_at

The timestamp when the parent interaction ended.

### perf_chat_va_handle_durations

File type: Delta

Part of interaction based reporting. Virtual agent interactions with end-users and agents.

#### id

Primary key identifier for records.

#### chat_id

References the chats records primary key **id**.

#### chat_duration

Duration in seconds of the virtual agent interaction.

#### ended_at

The timestamp when the interaction ended.

#### escalation_reason

String enum value

Value  | Meaning   
---|---  
unknown  | Unknown   
by_end_user_ask  | By End-user ask   
by_end_user_message  | By End-user Message   
by_virtual_agent  | By virtual agent   
payload_failure  | Payload failure   
could_not_resume  | Could not resume   
by_human_agent  | By human agent   
invalid_queue  | Invalid queue   
dismissed  | Dismissed   
  
#### event

Enum value.

Value  | Meaning   
---|---  
0  | Chat finished   
1  | Chat failed   
2  | Post session finished   
3  | Post session failed   
  
#### event_id

Deprecated. References null entity.

#### finish_reason

String enum value.

Value  | Meaning   
---|---  
undefined  | Undefined   
resolved  | Resolved   
unexpectedly_ended  | Unexpectedly ended   
escalated  | Escalated   
failed  | Failed   
consumer_ended  | Consumer ended   
  
#### initiated_by

Enum value.

Value  | Meaning   
---|---  
0  | End-user   
1  | Human agent   
2  | Post session   
  
#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### reactivated

Boolean indicating if this interaction was reactivated after dismissal.

#### started_at

The timestamp when the interaction began.

#### time

The timestamp when the interaction was recorded.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### virtual_agent_id

References the virtual_agents table by primary key **id**.

#### response_count

The count of virtual agent responses to end-user chats.

#### response_time_avg

The average time virtual agent responses took after the previous end-user message.

#### response_time_max

The maximum time virtual agent responses took after the previous end-user message.

#### response_time_total

The total time virtual agent responses took after the previous end-user message.

#### fallback_response_count

The quantity of times the virtual agent couldn't understand and responded with a fallback message.

### perf_chat_va_skipped_assignments

File type: Delta

Part of interaction based reporting. Interactions for when a Virtual Agent couldn't be assigned to a chat.

#### id

Primary key identifier for records.

#### chat_id

References the chats records primary key **id**.

#### reason

Enum value.

Value  | Meaning   
---|---  
0  | User segment bypass   
1  | Virtual agent failed   
  
#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### time

Timestamp when the event was recorded.

#### event_id

Deprecated. References null entity.

#### event

String of the event that triggered the recording.

### perf_chat_virtual_agent_summaries

File type: Delta

Deprecated and replaced by **perf_chat_va_handle_durations**.

#### id

Primary key identifier for records.

#### chat_id

References the chats records primary key **id**.

#### chat_type

String enum value.

Value  | Meaning   
---|---  
unknown  | Unknown   
mobile  | Mobile   
web  | Web   
session_initiated  | Session initiated   
sms  | SMS   
whatsapp  | Whatsapp   
  
#### ended_at

The timestamp when the interaction ended.

#### lang

ISO 639-1 language locale codes.

#### virtual_agent_id

References the virtual_agents table by primary key **id**.

#### response_count

The count of virtual agent responses to end-user chats.

#### response_time_total

The total time virtual agent responses took after the previous end-user message.

#### fallback_response_count

The quantity of times the virtual agent couldn't understand and responded with a fallback message.

### perf_consumer_call_in_menu_durations

File type: Delta

Part of interaction based reporting. Time an end-user spent in IVR menu selection.

#### id

Primary key identifier for records.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### call_id

References the calls records primary key **id**.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### event

Enum value.

Value  | Meaning   
---|---  
0  | Finished   
1  | Abandoned   
  
#### call_type

A string with the following possible values:

  * `**IncomingCall**`. An inbound call from a support number.
  * `**NumberedIncomingCall**`. An inbound call from a support number to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**IvrCall**`. An inbound call from an ordinary phone dial, handled by an IVR entry point.
  * `**InAppIvrCall**`. An inbound call initiated in-app, handled by an IVR entry point.
  * `**AppsApiNumberedIncomingCall**`. An inbound call, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**ScheduledCall**`. A callback scheduled for later.
  * `**NumberedScheduledCall**`. A scheduled callback to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**AppsApiNumberedScheduledCall**`. A scheduled callback, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**DirectCall**`. A call that bypasses IVR or queue entry and is directed to a specific agent or endpoint.
  * `**InternalCall**`. An internal agent-to-agent or agent-to-conference call.



#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### in_menu_duration

Duration in seconds the end-user was in IVR selection.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

### perf_email_handle_durations

File type: Delta

Part of interaction based reporting. Each record is a unique agent interaction on an email. Commonly used for metrics such as Handle Time.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
4  | Email support transferred   
5  | Email support unassigned   
6  | Email support paused   
8  | Email support resolved   
9  | Email support closed   
10  | Email support reopened   
11  | Email agent first replied   
12  | Email agent replied   
  
#### email_duration

Duration in seconds of this interaction.

#### email_support_id

References email_supports by primary key **id**.

#### inbound

Boolean that if true would indicate this was an inbound interaction.

#### transfer

Boolean that if true would indicate this interaction began as the result of a transfer.

#### transfer_id

References the comm_transfers table by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### agent_id

References the users table by primary key **id**.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Unopened   
1  | Active   
2  | Paused   
3  | Resolved   
4  | Closed   
5  | Reopened   
  
#### assignment_type

Enum value.

Value  | Meaning   
---|---  
0  | Automatic   
1  | Manual   
  
#### attachments_count

Count of attachments on this email interaction.

### perf_email_queue_durations

File type: Delta

Part of interaction based reporting. Queue level interactions that are used for metrics such as SLA, queue duration, and abandonment rates. Note that **agent_id** is present on queued interactions as a signal to how the interaction ended. The agent has no responsibility to any of the metrics.

#### id

Primary key identifier for records.

#### event

Enum value.

Value  | Meaning   
---|---  
3  | Email support assigned   
  
#### email_support_id

References email_supports by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### queue_duration

Duration in seconds this interaction was enqueued.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

#### agent_id

References the users table by primary key **id**.

#### inbound

Boolean that if true would indicate this was an inbound interaction.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Unopened   
1  | Active   
2  | Paused   
3  | Resolved   
4  | Closed   
5  | Reopened   
  
#### assignment_type

Enum value.

Value  | Meaning   
---|---  
0  | Automatic   
1  | Manual   
  
#### service_level_target_time

The duration in seconds that this record's queue_duration would need to meet to be considered in SLA snapshotted at the time this record was created.

#### service_level_event

Enum value.

Value  | Meaning   
---|---  
0  | Excluded   
1  | In SLA   
2  | Not in SLA   
  
#### service_level_target_percent

When this record is enqueued this is a snapshot of the target percentage.

### perf_third_party_call_handle_durations

File type: Delta

Part of interaction based reporting. Each record is a unique third party interaction on a call.

#### id

Primary key identifier for records.

#### participant_id

References `call_participants` by the primary key **id**.

#### call_id

References the calls records primary key **id**.

#### origin_call_id

References the calls records primary key **id**. Reflects a parent call record.

#### session_id

Calls are superseded by a session. This links to the sessions dataset by the primary key **id**.

#### call_type

A string with the following possible values:

  * `**IncomingCall**`. An inbound call from a support number.
  * `**NumberedIncomingCall**`. An inbound call from a support number to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**IvrCall**`. An inbound call from an ordinary phone dial, handled by an IVR entry point.
  * `**InAppIvrCall**`. An inbound call initiated in-app, handled by an IVR entry point.
  * `**AppsApiNumberedIncomingCall**`. An inbound call, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**ScheduledCall**`. A callback scheduled for later.
  * `**NumberedScheduledCall**`. A scheduled callback to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**AppsApiNumberedScheduledCall**`. A scheduled callback, created by the apps API, to a numbered entry point. Used by CCAI Platform for DNIS-based routing.
  * `**DirectCall**`. A call that bypasses IVR or queue entry and is directed to a specific agent or endpoint.
  * `**InternalCall**`. An internal agent-to-agent or agent-to-conference call.



#### call_duration

Duration in seconds of this third party interaction.

#### hold_duration

Unused. It isn't possible to record a third party's hold imposed on an end-user.

#### started_at

The timestamp when the interaction began.

#### ended_at

The timestamp when the interaction ended.

### queue_report_group_histories

File type: Delta

Queue report groups are a way of bundling metrics together by a combination of queues. The data in this table represents the historical assignment of queues to queue report groups.

#### id

Primary key identifier for records.

#### group_id

References queue_report_groups by primary key id.

#### lang

ISO 639-1 language locale codes.

#### menu_id

Relationship to menus using the primary key **id**

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### menu_type

String with the following possible values:

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * whats_app_menu

  * email_menu




#### started_at

The timestamp when the menu membership to a queue report group began.

#### ended_at

The timestamp when the menu membership to a queue report group ended.

### queue_report_group_items

File type: Full

Queue report groups are a way of bundling metrics together by a combination of queues. Each item is a current queue assignment to a queue report group.

#### id

Primary key identifier for records.

#### group_id

References **queue_report_groups** by primary key **id**.

#### lang

ISO 639-1 language locale codes.

#### menu_id

Relationship to menus using the primary key **id**.

### queue_report_groups

File type: Full

Queue report groups are a way of bundling metrics together by a combination of queues. These are the groups themselves.

#### id

Primary key identifier for records.

#### name

Name assigned to the queue report group.

#### comm_type

Call, chat, or email.

#### hidden

The visibility of this queue report group on Contact Center AI Platform dashboards.

#### hidden_productive_agents

The visibility of production agent data on Contact Center AI Platform dashboards.

#### user_statuses

The user statuses that are included in the definition of productive.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

### sessions

File type: Delta

Sessions are a parent channel to calls, chats, and emails and have no specific use.

#### id

Primary key identifier for records.

#### agent_id

References the users table by primary key **id**.

#### created_at

Timestamp when this record was created at.

#### end_user_id

Relationship to end-users using the primary key **id**. Commonly referred to as consumers.

#### finished_at

The timestamp for this session was completed.

#### in_queue_priority

The priority value for this session while it was enqueued.

#### lang

ISO 639-1 language locale codes.

#### materialized_menu_path

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_ids** separated by "/" noting the queue hierarchy.

#### materialized_menu_path_name

Deprecated in favor of interaction based reporting that joins data from the **menu_paths** , **menu_path_items** , **menus** , and **menus datasets** using **menu_path_id**. String of **menu_names** separated by "/" noting the queue hierarchy.

#### menu_id

Relationship to menus using the primary key **id**

#### menu_path_id

References the **menu_paths** table by primary key **id**.

#### menu_type

String with the following possible values:

  * ivr_menu

  * sms_menu

  * web_menu

  * mobile_menu

  * whats_app_menu

  * email_menu




#### out_ticket_id

External configured CRM ticket ID referencing this session.

#### out_ticket_url

External configured CRM ticket URL referencing this session.

#### queue_priority_level

The priority level of the menu the transfer enqueued into.

#### rating

CSAT rating for this session.

#### status

Enum value.

Value  | Meaning   
---|---  
0  | Ongoing   
10  | Finished   
  
#### transfer_count

Deprecated. Count of transfers. Use **queue_durations** suffixed records where transfer = 1

#### user_priority

The priority level of the end-user that created the email support.

#### verifiable

Boolean indicating whether the device has support for verification by fingerprint.

#### verified

End user has been verified.

### skills

File type: Full

#### id

The primary key ID for this record.

#### created_at

The time when this record was created.

#### name

The name of the skill.

#### updated_at

The time when this record was last updated.

### team_hierarchies

File type: Full

Used to map team hierarchies. Both **ancestor_id** and **descendant_id** refer to the team's record.

#### ancestor_id

Relationship to teams using the primary key **id**

#### descendant_id

Relationship to teams using the primary key **id**

#### generations

Indicates whether the descendent is directly assigned to the menu.

### team_memberships

File type: Full

Current user and team memberships.

#### id

Primary key identifier for records.

#### created_at

Timestamp when this record was created at.

#### team_id

Relationship to teams using the primary key **id**

#### updated_at

Timestamp when this last record was updated.

#### user_id

References the users table by primary key **id**.

#### membership_type

Enum value.

Value  | Meaning   
---|---  
0  | Supervisor   
1  | Subordinate   
  
### teams

File type: Full

Current teams in the platform.

#### id

Primary key identifier for records.

#### agents_count

Number of agents in this team.

#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### name

Name of the team.

#### parent_id

References the same teams data by primary key **id**.

#### position

Hierarchical position with 0 being a leaf team.

#### updated_at

Timestamp when this last record was updated.

### user_activity_logs

File type: Delta

Each specific agent activity within the platform will generate a log. Most are point in time logs with some, like user status changed containing a duration.

#### id

Primary key identifier for records.

#### activity

Enum value.

Value  | Meaning   
---|---  
1  | Login   
2  | Logout   
3  | Online   
4  | Offline   
10000  | Call notification offered   
10001  | Call pick up attempt   
10002  | Call picked up   
10003  | Call outbound dialing   
10004  | Call outbound API triggered   
10005  | Call internal dialing   
10006  | Call internal missed   
11000  | Deltacast call notification offered   
11001  | Deltacast call pick up attempt   
11002  | Deltacast call picked up   
11003  | Deltacast call projected   
11004  | Deltacast call missed   
11005  | Deltacast call bounced   
11006  | Deltacast call canceled   
11007  | Deltacast call missed poor network   
11008  | Deltacast call breakthrough offered   
11009  | Deltacast call breakthrough answered   
11010  | Deltacast call breakthrough missed   
11100  | Auto answered call notification offered   
11102  | Auto answered call picked up   
12000  | Multicast call notification offered   
12001  | Multicast call pick up attempt missed   
12002  | Multicast call picked up   
12003  | Multicast call breakthrough offered   
12004  | Multicast call breakthrough answered   
12005  | Multicast call breakthrough missed   
13000  | Call agent exceeded wrap-up time   
14000  | Call notification sent on agent app   
14001  | Call notification received on agent app   
20000  | User status changed   
20001  | Next status applied   
20100  | User status inherited from CRM   
20101  | Next status applied by CRM   
20201  | Next status applied by System   
20300  | Forward calls to phone On   
20301  | Forward calls to phone Off   
20400  | Forward calls to agent app On   
20401  | Forward calls to agent app Off   
20500  | User status inherited from CCaaS   
20501  | Next status applied by CCaaS   
30000  | Chat notification offered   
30001  | Chat pickup attempt   
30002  | Chat picked up   
30003  | Chat agent unresponsive   
31000  | Deltacast chat notification offered   
31001  | Deltacast chat pick Up attempt   
31002  | Deltacast chat picked up   
31003  | Deltacast chat projected   
31004  | Deltacast chat missed   
31005  | Deltacast chat bounced   
31006  | Deltacast chat canceled   
31007  | Deltacast chat missed poor network   
31100  | Auto answered chat notification offered   
31102  | Auto answer chat picked up   
32000  | Multicast notification offered   
32001  | Multicast chat pick up attempt   
32002  | Multicast chat picked up   
33000  | Emergency services outbound dialed   
33001  | Emergency services conference dialed   
33002  | Emergency services conference joined   
33003  | Emergency services conference failed   
34000  | Chat agent exceeded wrap-up time   
35000  | User break from external campaign   
36000  | Send chat notification on agent app   
36001  | Receive chat notification on agent app   
  
#### call_id

References the calls records primary key **id**.

#### chat_id

References the chats records primary key **id**.

#### duration

User status changed activities log a start and ending date. This duration is the time in seconds spent in the status.

#### ended_at

The timestamp when the interaction ended. Applies to activity 20000 for tracking agent statuses and the windowed duration of they are in a given status.

#### user_status_id

Zero or less values represent default platform statuses while positive integers have a relationship to **user_statuses** on primary key **id**.

Value  | Meaning   
---|---  
0  | Available   
-1  | Unavailable   
-2  | Break   
-3  | Special task   
-4  | Meal   
-5  | Missed call   
-6  | Wrap-up   
-7  | In-call   
-8  | In-chat   
-10  | Offline   
-11  | Unresponsive   
-12  | Missed chat   
-13  | Wrap-up exceeded   
  
#### started_at

The timestamp when the interaction began.

#### user_id

References the users table by primary key **id**.

### user_projections

File type: Delta

#### id

The primary key ID for this record.

#### call_id

The call ID.

#### chat_id

The chat ID.

#### ended_at

The time when the projection ended.

#### matching_skills_payload

JSON representing what skill condition was matched.

#### projected_at

The time of the projection.

#### result

Enum value.

Value | Meaning  
---|---  
0 | `in_progress`: The projection is in progress.  
1 | `picked_up`: The agent picked up the call. It might not be the projected call.  
2 | `ignored`: The agent was available during the projection but didn't pick up the call.  
3 | `skipped`: The call was skipped.  
4 | `canceled`: The projection was canceled due to the cancellation of the transfer.  
  
#### user_id

The user ID.

### user_queue_histories

File type: Delta

Historical association of users and queues.

#### id

Primary key identifier for records.

#### channel

Enum value.

Value  | Meaning   
---|---  
0  | Session   
1  | Chat   
2  | Voice call   
3  | Video call   
4  | Voicemail   
5  | Email   
  
#### end_event

Enum value.

Value  | Meaning   
---|---  
0  | None   
1  | Team destroyed   
2  | Team parent changed   
3  | Team membership created   
4  | Team membership destroyed   
5  | User destroyed   
6  | Menu parent changed   
7  | Menu destroyed   
8  | Queue assignment created   
9  | Queue assignment destroyed   
10  | Queue group type changed   
11  | Queue group created   
12  | Queue group destroyed   
13  | User role changed   
  
#### ended_at

The timestamp when the membership a user had with a menu ended.

#### group_id

Relationship to **menu_queue_groups** using the primary key **id**

#### lang

ISO 639-1 language locale codes.

#### level

Deprecated.

#### menu_id

Relationship to menus using the primary key **id**

#### start_event

Enum value.

Value  | Meaning   
---|---  
0  | None   
1  | Team destroyed   
2  | Team parent changed   
3  | Team membership created   
4  | Team membership destroyed   
5  | User destroyed   
6  | Menu parent changed   
7  | Menu destroyed   
8  | Queue assignment created   
9  | Queue assignment destroyed   
10  | Queue group type changed   
11  | Queue group created   
12  | Queue group destroyed   
13  | User role changed   
  
#### started_at

The timestamp when the membership a user had with a menu began.

#### user_id

References the users table by primary key **id**.

#### current

Active user queue association.

### user_skills

File type: Delta

#### id

The primary key ID for this record.

#### created_at

The time when this record was created.

#### learning

Enum value. Indicates if the skill is marked as `learning` for the agent.

Value | Meaning  
---|---  
0 | `FALSE`  
1 | `TRUE`  
  
#### skill_id

The skill ID.

#### skill_level

The skill level of the user.

#### updated_at

The time when this record was last updated.

#### user_id

The user ID.

### user_statuses

File type: Full

Customer configured user statuses.

#### id

Primary key identifier for records.

#### deleted_at

Timestamp when this record was soft deleted at.

#### name

Name of the user status.

### user_team_histories

File type: Delta

Historical association of users and team.

#### id

Primary key identifier for records.

#### end_event

Enum value.

Value  | Meaning   
---|---  
0  | None   
1  | Team destroyed   
2  | Team parent changed   
3  | Team membership created   
4  | Team membership destroyed   
5  | User destroyed   
  
#### ended_at

The timestamp when the membership a user had with a team ended.

#### start_event

Enum value.

Value  | Meaning   
---|---  
0  | None   
1  | Team destroyed   
2  | Team parent changed   
3  | Team membership created   
4  | Team membership destroyed   
5  | User destroyed   
  
#### started_at

The timestamp when the membership a user had with a team began.

#### team_id

Relationship to teams using the primary key **id**

#### user_id

References the users table by primary key **id**.

#### current

Active user team association.

### users

File type: Full

User records in the platform. All user types are returned and not solely agents.

#### id

Primary key identifier for records.

#### agent_number

Customer provided identifier for users.

#### assigned_skills

JSON data that contains the skills assigned to the user, including `skill_id`, `skill_level`, and `learning`.

#### call_queue_assigned

Boolean indicating the user is associated with a call queue.

#### chat_auto_answer

#### chat_queue_assigned

Boolean indicating the user is associated with a chat queue.

#### created_at

Timestamp when this record was created at.

#### deleted_at

Timestamp when this record was soft deleted at.

#### email

Email address of user.

#### first_name

First name of user.

#### ignored_projection_count

Current counter of ignored projections.

#### last_login_time

Timestamp of the last login.

#### last_name

Last name of user.

#### location_id

Relationship to **company_locations** using the primary key **id**.

#### location

Same value from relationship on company_locations.

#### max_chat_limit

Maximum concurrent chats.

#### max_chat_limit_enabled

Boolean enabling concurrent chats.

#### permissions

Deprecated.

#### repr_status_name

Current user status name.

#### roles

Deprecated.

#### skill_level_average

The user's skill level average.

#### status_after_inquiries_id

Next user status after current.

#### status_after_inquiries_by

Enum value.

Value  | Meaning   
---|---  
0  | Agent   
1  | CRM   
2  | System   
3  | CCaaS   
  
#### repr_status_id

Current user status ID.

### virtual_agents

File type: Full

Virtual agents configured in the platform.

#### id

Primary key identifier for records.

#### avatar

URL of avatar image.

#### chatbot_workflow_id

#### deleted_at

Timestamp when this record was soft deleted at.

#### enabled

Current enabled status of the virtual agent.

#### langs

Supported ISO 639-1 language locale codes.

#### menu_types

Bitmask values.

  * 0 = no menu types

  * 1 = Mobile

  * 2 = Web

  * 3 = Mobile + Web

  * 4 = IVR

  * 5 = Mobile + IVR

  * 6 = Web + IVR

  * 7 = Mobile + Web + IVR


Value  | Meaning   
---|---  
1  | Mobile   
2  | Web   
4  | IVR   
  
#### name

Name of the virtual agent.

#### created_at

Timestamp when this record was created at.

#### updated_at

Timestamp when this last record was updated.

#### channel_types

Bitmask values.

  * 0 = no channel types

  * 1 = chat only

  * 2 = voice_call only

  * 3 = both chat and voice_call


Value  | Meaning   
---|---  
1  | chat   
2  | voice_call   
  
#### agent_type

Enum value.

Value  | Meaning   
---|---  
0  | Support   
1  | Task   
  
## Metrics

### Handle time

#### Calls
    
    
    SELECT SUM(call_duration) + SUM(acw_duration) + SUM(bcw_duration)
    
    FROM perf_call_handle_durations
    
    WHERE event IN (0, 1, 2, 3, 4)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

#### Chats
    
    
    SELECT SUM(chat_duration) + SUM(acw_duration)
    
    FROM perf_chat_handle_durations
    
    WHERE event IN (0, 1, 2, 3)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

#### Email
    
    
    SELECT SUM(email_duration)
    
    FROM perf_email_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

### Hold Time

#### Calls
    
    
    SELECT SUM(hold_duration)
    
    FROM perf_call_handle_durations
    
    WHERE event IN (0, 1, 2)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

### Talk Time

#### Calls
    
    
    SELECT SUM(call_duration) - SUM(hold_duration)
    
    FROM perf_call_handle_durations
    
    WHERE event IN (0, 1, 2)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

### After Call Work

#### Calls
    
    
    SELECT SUM(acw_duration)
    
    FROM perf_call_handle_durations
    
    WHERE event IN (3)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

#### Chats
    
    
    SELECT SUM(acw_duration)
    
    FROM perf_chat_handle_durations
    
    WHERE event IN (3)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

### Before Call Work

#### Calls
    
    
    SELECT SUM(bcw_duration)
    
    FROM perf_call_handle_durations
    
    WHERE event IN (4)
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `agent_id` for agent metrics.

### SLA

#### Calls
    
    
    SELECT SUM(service_level_event IN(1)) / SUM(service_level_event IN (1, 2)) * 100
    
    FROM perf_call_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

#### Chats
    
    
    SELECT SUM(service_level_event IN(1)) / SUM(service_level_event IN (1, 2)) * 100
    
    FROM perf_chat_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

#### Email
    
    
    SELECT SUM(service_level_event IN(1)) / SUM(service_level_event IN (1, 2)) * 100
    
    FROM perf_email_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

### Queue duration

#### Calls
    
    
    SELECT SUM(queue_duration)
    
    FROM perf_call_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

#### Chats
    
    
    SELECT SUM(queue_duration)
    
    FROM perf_chat_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

#### Email
    
    
    SELECT SUM(queue_duration)
    
    FROM perf_email_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

### Abandonment %

#### Calls
    
    
    SELECT SUM(event IN (3) AND service_level_event <> 0) AS total_abandoned,
    
     SUM(service_level_event <> 0) AS total_queued_interactions,
    
     SUM(event IN (3) AND service_level_event <> 0) 
    
       / SUM(service_level_event <> 0) 
    
       * 100 AS abandon_percent
    
    FROM perf_call_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

#### Chats
    
    
    SELECT SUM(event IN (1) AND service_level_event <> 0) AS total_abandoned,
    
     SUM(service_level_event <> 0) AS total_queued_interactions,
    
     SUM(event IN (1) AND service_level_event <> 0) 
    
       / SUM(service_level_event <> 0) 
    
       * 100 AS abandon_percent
    
    FROM perf_chat_queue_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

### Virtual agent handle time

#### Calls
    
    
    SELECT SUM(call_duration)
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(chat_duration)
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

### Virtual agent started by consumer

#### Calls
    
    
    SELECT SUM(initiated_by = 0)
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(initiated_by = 0)
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

### Virtual agent started by agent

#### Calls
    
    
    SELECT SUM(initiated_by = 1)
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(initiated_by = 1)
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

### Virtual agent abandons

#### Calls
    
    
    SELECT SUM(finish_reason IN (5))
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(finish_reason IN ('undefined', 'unexpectedly_ended'))
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

### Virtual agent escalation counts

#### Calls
    
    
    SELECT SUM(
    
     finish_reason IN (3) 
    
     AND escalation_reason IN (1,2)
    
    )
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(
    
     finish_reason = 'escalated' 
    
     AND escalation_reason IN ('by_end_user_ask', 'by_end_user_message')
    
    )
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

### Virtual agent planned transfers

#### Calls
    
    
    SELECT SUM(
    
     finish_reason IN (3) 
    
     AND escalation_reason IN (3)
    
    )
    
    FROM perf_call_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

#### Chats
    
    
    SELECT SUM(
    
     finish_reason = 'escalated' AND escalation_reason = 'by_virtual_agent'
    
    )
    
    FROM perf_chat_va_handle_durations
    

Group data by `**menu_path_id**` and `lang` for queue metrics.

Group data by `virtual_agent_id` for virtual agent metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
