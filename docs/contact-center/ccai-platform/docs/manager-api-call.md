---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-call/
title: Call endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:17.723396+00:00
---

# Call endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call endpoints Stay organized with collections  Save and categorize content based on your preferences. 

A call object is created for every call that is to or from Contact Center AI Platform (CCAI Platform). See the following model to determine which fields might contain PII.
    
    
    [
     {
        "id": 0,
        "parent_id": 0,
        "lang": "en",
        "call_type": "Voice Inbound (App)",
        "status": "scheduled",
        "sub_status": "Scheduled: Disconnected by unknown",
        "created_at": "2018-06-07T19:49:52.896Z",
        "queued_at": "2018-06-07T19:49:52.896Z",
        "assigned_at": "2018-06-07T19:49:52.896Z",
        "connected_at": "2018-06-07T19:49:52.896Z",
        "ends_at": "2018-06-07T19:49:52.896Z",
        "scheduled_at": "2018-06-07T19:49:52.896Z",
        "updated_at": "2018-06-07T19:49:52.896Z",
        "wait_duration": 0, //Deprecated, use queue_duration instead
        "queue_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": 0,
        "has_feedback": true,
        "voip_provider": "voip_provider_twilio",
        "out_ticket_id": "string",
        "out_ticket_url": "string",
        "verified": true,
        "recording_url": "string",
        "recording_permission": "not_asked",
        "voicemail_reason": "not_voicemail",
        "deflection": "no_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "finish_reason": "no_reason",
        "fail_details": "string",
        "fail_reason": "nothing",
        "adapter_fail_code": null,
        "adapter_fail_message": null,
        "support_number": "string",
        "selected_menu": {
          "id": 0,
          "name": "string",
          "parent_id": 0,
          "position": 0,
          "deleted": true,
          "hidden": "string",
          "menu_type": "ivr_menu",
          "output_msg": "string"
        },
        "menu_path": {
          "items_count": 0,
          "name": "string",
          "materialized_path": "string"
        },
        "agent_info": {
          "id": 0,
          "name": "string", //This may be considered PII
          "last_name": "string", //This may be considered PII
          "first_name": "string", //This may be considered PII
          "agent_number": "string",
          "avatar_url": "string"
        },
        "end_user": {
          "id": 0, //This may be considered PII
          "identifier": "string", //This may be considered PII
          "out_contact_id": "string" //This may be considered PII
        },
        "photos": [
          {
            "id": 0, //This may be considered PII
            "photo_type": "photo", //This may be considered PII
            "url": "string" //This may be considered PII
          }
        ],
        "videos": [
          {
            "id": 0, //This may be considered PII
            "url": "string" //This may be considered PII
          }
        ],
        "transfers": [
          {
            "id": 0,
            "status": "transferring",
            "fail_reason": "nothing",
            "created_at": "2018-06-07T19:49:52.896Z",
            "call_duration": 300,
            "wait_duration": 40,
            "assigned_at": "2018-06-07T19:50:32.896Z",
            "connected_at": "2018-06-07T19:50:35.896Z",
            "updated_at": "2018-06-07T19:55:35.896Z",
            "deflection": 0,
            "from_menu": {
              "items_count": 0,
              "name": "string",
              "materialized_path": "string"
            },
            "to_menu": {
              "items_count": 0,
              "name": "string",
              "materialized_path": "string"
            },
            "from_agent": {
              "id": 0,
              "name": "string", //This may be considered PII
              "last_name": "string", //This may be considered PII
              "first_name": "string", //This may be considered PII
              "agent_number": "string",
              "avatar_url": "string"
            },
            "to_agent": {
              "id": 0,
              "name": "string", //This may be considered PII
              "last_name": "string", //This may be considered PII
              "first_name": "string", //This may be considered PII
              "agent_number": "string",
              "avatar_url": "string"
            }
          }
        ],
        "handle_durations": [
            {
                "agent_id": 0,
                "acw_duration": 0,
                "call_duration" 0,
                "menu_path_id": 0,
                "wait_duration": 0,
                "lang": "en",
                "transfer": false,
                "started_at": "2019-07-17T07:27:14.000Z",
                "ended_at": "2019-07-17T07:27:20.000Z",
                "event": "call_finished"
            }
        ],
        "queue_durations": [
            {
                "agent_id": 0,
                "queue_duration" 0,
                "menu_path_id": 0,
                "lang": "en",
                "transfer": false,
                "started_at": "2019-07-17T07:27:14.000Z",
                "ended_at": "2019-07-17T07:27:20.000Z",
                "service_level_abandon_time_threshold": 10,
                "service_level_event": "not_in_sla",
                "service_level_target_percent": 90,
                "service_level_target_time": 60,
                "event": "answered"
            }
        ]
        "participants": [
          {
            "id": 0,
            "type": "end_user",
            "status": "waiting",
            "call_id": 0,
            "user_id": 0, //This may be considered PII
            "end_user_id": 0, //This may be considered PII
            "call_duration": 0,
            "hold_duration": 0,
            "connected_at": "2018-06-07T19:49:52.896Z",
            "ended_at": "2018-06-07T19:49:52.896Z",
            "fail_reason": "nothing",
            "adapter_fail_code": null,
            "adapter_fail_message": null
          },
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": null,
        "wait_time_sms": [],
        "in_call_sms": []
        ]
      }
    ]
    

The status field can be in any of the following states:

Call Status | Description  
---|---  
Selecting | State that occurs when an end user has called into the contact center, but is still navigating the menu options prior to call request from a leaf node.  
Queued | State that occurs after the end user has selected a leaf menu node and initiated a call request to be deltcasted or multicasted to an agent.  
Assigned | State that occurs when an agent is selected to received the end user call. This occurs when an agent picks up a call.  
Connecting | State that occurs after an agent is assigned, and is waiting to be establish a connection between the end user and agent.  
Connected | State that occurs when the call has established a connection and the agent and end user are both placed into a call.  
Finished | State that occurs when an agent and end user's conversation ends a call without any errors.  
Failed | State that occurs when a call ends because of an error. When this status is rendered, a failed reason will also be provided for more context  
Switching | State that occurs when a call fails while trying to connect and CCAI Platform attempts to connect the call with a different VOIP provider.  
Recovered | State that occurs when a failed call is called back. This new call is a child to the original call. Recovered notes that the call back is finished without error.  
Scheduled | State that occurs when an end user has chosen to be called in the future as part of a deflection option or has selected to be called in the future using In-Web or In-App.  
Action Only | State that occurs when a call that is handled by our client's own telephony provider is connected to our iOS or Android SDK.  
Action Only Finished | State that occurs when a call that is handled by our client's own telephony provider is connected to our iOS or Android SDK and finishes  
Deflected | State that occurs based on the configuration for overcapacity queues or after hour calls. Deflection options include voicemail, schedule call among others. Deflection will vary based on channel (In-app, IVR, In-web)  
Voicemail | State that occurs when an end user is deflected to a voicemail option, and opts to leave a voicemail message to listened to later. This state is present when the end user is leaving the voicemail  
Voicemail Received | State that occurs after an end user has left a voicemail and an agent has not listened to the voicemail  
Voicemail Read | State that occurs when an agent has opened the voicemail to listen to.  
  
The call_type field can only be one of the following values

Call type | Description  
---|---  
Voice Inbound (IVR) | Incoming PSTN call from an end user's phone.  
Voice Inbound (App) | Incoming call made from within an iOS or Android application that uses our Mobile SDK.   
Voice Callback (Web) | Incoming call request made from within our Web SDK   
Voice Scheduled (App) | Call made from an agent to an end user that was pre-scheduled using the Mobile SDK scheduling capability.  
Voice Scheduled (Web) | Call made from an agent to an end user that was pre-scheduled using our Web SDK scheduling capability  
Voice Outbound | Call made from an agent to an end user dialed using the dial pad or other method to call an outside phone line.   
  
The `service_level_event` field can only be one of the following values:

Service Level Event | Description  
---|---  
in_sla | Call was answered within SLA  
not_in_sla | Call was not answered within defined SLA  
excluded | Call was not included in SLA calculation (e.g. if call was abandoned)   
  
The `adapter_fail_code` and `adapter_fail_message` fields can only be one of the following values if not null:

Adapter fail code | Adapter fail message  
---|---  
10001 | This call encountered an unexpected error.  
11001 | This call expired while waiting in queue.  
20001 | This call was cancelled by the customer.  
20002 | This call was rejected by the customer.  
20003 | This call was abandoned by the customer.  
20004 | This call was abandoned by the customer during menu selection.  
21001 | The call couldn't be connected; the customer's line is busy.  
21002 | The dialed phone number is invalid.  
21003 | This call was was not answered by the customer.  
22001 | The push notification to start this call failed to send.  
30001 | This call was cancelled.  
30002 | This expired call was not attended.  
31001 | Unable to detect microphone. Please check your device settings and try again.  
31002 | Unable to access microphone. Please check your device permissions and try again.  
32001 | The selected outbound number is invalid.  
32002 | Unable to connect call to the dialled phone number.  
41001 | An unexpected error occurred with the call connection.  
42001 | An unexpected error occurred with the call connection.  
43001 | This call has encountered an unexpected error.  
44001 | This call has encountered an unexpected error.  
44002 | This call is terminated because the connection timed out.  
44003 | This call has encountered an unexpected error.  
90001 | This call is terminated because no audio was detected.  
90002 | Unable to start the audio device. Please check your audio device permissions and try again.  
**Note:** `wait_duration` has been deprecated. Use `queue_duration` instead.

## Calls

Parameter | Required | Data Type | Definition  
---|---|---|---  
connected_at[from] | FALSE | Time in UTC | creates a lower bound of the connected at field. All records returned will be before the inputted value.  
connected_at[to] | FALSE | Time in UTC | creates an upper bound of the connected at field. All records returned will be before the inputted value.  
updated_at[from] | FALSE | Time in UTC | creates a lower bound of the updated at field. All records returned will be after the inputted value.  
updated_at[to] | FALSE | Time in UTC | creates an upper bound of the connected at field. All records returned will be before the inputted value.  
queued_at[from] | FALSE | Time in UTC | creates a lower bound of the queued at field. All records returned will be after the inputted value.  
queued_at[to] | FALSE | Time in UTC | creates an upper bound of the queued at field. All records returned will be before the inputted value.  
rating[from] | FALSE | Number 1-5 or null | creates a lower bound of the rating field. All records returned will be after the inputted value.  
rating[to] | FALSE | Number 1-5 or null | creates an upper bound of the rating field. All records returned will be before the inputted value.  
call_duration[from] | FALSE | Number | creates a lower bound of the call duration field. All records returned will be after the inputted value.  
call_duration[to] | FALSE | Number | creates an upper bound of the call duration field. All records returned will be before the inputted value.  
hold_duration[from] | FALSE | Number | creates a lower bound of the hold duration field. All records returned will be after the inputted value.  
hold_duration[to] | FALSE | Number | creates an upper bound of the hold duration field. All records returned will be before the inputted value.  
id[] | FALSE | Array[String] | Array of strings. ID of records to search and return.  
agent_id[] | FALSE | Array[String] | Filters response by agent id  
end_user_id[] | FALSE | Array[String] | Filters response based on the end user id  
call_status[] | FALSE | Array[String] | Return records of a given state in the call lifecycle. The possible values are: scheduled, queued, assigned, connecting, switching, connected, finished, failed, recovered, deflected, selecting, action_only, action_only_finished, voicemail, voicemail_received, voicemail_read   
call_fail_reason[] | FALSE | Array[String] | Returns records that have failed in a certain way. The possible values are: nothing, unknown, expired, eu_canceled, eu_rejected, eu_abandoned, eu_in_menu_abandoned, eu_busy, eu_wrong_number, eu_no_answer, eu_noti_failed, ag_canceled, ag_ignored, ag_mic_no_device, ag_mic_denied, voip_twilio_error, voip_tokbox_error, voip_invalid_token, voip_conn_general, voip_conn_timeout, voip_conn_signal  
verified[] | FALSE | Boolean | Returns records that either have been verified (True) or have not been verified (False)  
call_type[] | FALSE | Array[String] | Returns records of a given call type. The possible values are: IncomingCallApp, ScheduledCallApp, OutboundCall, AgentScheduledCall, IvrCall, IncomingCallWeb, ScheduledCallWeb, ActionOnlyCall  
support_number[] | FALSE | Array[String] | Filter by the phone number end user used to contact (only for IVR call)  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/calls
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_More example Requests/Responses:_**

### Example request: Calls

**_Body: None_**

### Example response: Calls
    
    
    [
      {
        "id": 1,
        "lang": "en",
        "call_type": "Voice Inbound (App)",
        "status": "finished",
        "created_at": "2016-02-19T18:53:56.000Z",
        "queued_at": "2016-02-19T18:53:57.000Z",
        "assigned_at": "2016-02-19T18:53:58.000Z",
        "connected_at": "2016-02-19T18:54:18.000Z",
        "ends_at": "2016-02-19T18:54:39.000Z",
        "updated_at": "2016-02-19T18:54:39.000Z",
        "scheduled_at": null,
        "queue_duration": 22,
        "wait_duration": 22,
        "call_duration": 21,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
        "voip_provider": "voip_provider_twilio",
        "out_ticket_id": null,
        "out_ticket_url": null,
        "verified": false,
        "recording_url": null,
        "recording_permission": "not_asked",
        "voicemail_reason": "not_voicemail",
        "deflection": "no_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": "nothing",
        "fail_details": null,
        "recordings": [
            {
                "id": 7,
                "call_id": 1,
                "conference_sid": "CF50ec183fafcff801226b6fc332EC02ba7c4",
                "duration": 20,
                "recording_type": "default",
                "redaction_times": [
                    {
                        "start": "2016-02-19T18:54:23.000Z",
                        "end": "2016-02-19T18:54:25.000Z",
                        "duration": 2.000,
                        "start_agent_id": 2,
                        "end_agent_id": 2
                    }
                ],
                "started_at": "2016-02-19T18:54:18.000Z"
            }
        ],
        "support_number": "+12128675309",
        "selected_menu": {
          "id": 11,
          "name": "Carpentry",
          "parent_id": 1,
          "position": 1,
          "deleted": false,
          "hidden": false,
          "menu_type": "ivr_menu",
          "output_msg": "Thanks for calling Death Star Carpentry"
        },
        "menu_path": {
          "items_count": 1,
          "name": "Carpentry",
          "materialized_path": "Death Star/Carpentry"
        },
        "queue_priority_level": 0,
        "end_user": {
          "id": 3,
          "identifier": "Death Star Carpentry Union",
          "out_contact_id": "363876643527"
        },
        "photos": [{
          "id": 0,
          "photo_type": "photo",
          "url": "www.photolocation.co/photo/123456868686"
        }],
        "videos": [{
          "id": 0,
          "url": "www.videolocation.co/video/123456868686"
        }],
        "transfers": [{
          "id": 11,
          "status": "transferring",
          "fail_reason": "nothing",
          "created_at": "2016-02-19T18:58:18.000Z",
          "from_menu": {
            "items_count": 2,
            "name": "Cabinetry",
            "materialized_path": "Death Star/Cabinetry"
          },
          "to_menu": {
            "items_count": 2,
            "name": "Carpentry",
            "materialized_path": "Death Star/Carpentry"
          },
          "from_agent": {
            "id": 2,
            "name": "San Holo",
            "last_name": "San",
            "first_name": "Holo",
            "agent_number": "6",
            "avatar_url": "www.avatarurl.co/avatar/1234543"
          },
          "to_agent": {
            "id": 0,
            "name": "Farrison Hord",
            "last_name": "Farrison",
            "first_name": "Hord",
            "agent_number": "12",
            "avatar_url": "www.avatarurl.co/avatar/1234545"
          }
        }],
        "participants": [
          {
            "id": 5,
            "type": "end_user",
            "status": "finished",
            "call_id": 3,
            "user_id": null,
            "end_user_id": 3,
            "call_duration": 21,
            "hold_duration": null,
            "connected_at": "2016-02-19T18:54:18.000Z",
            "ended_at": "2016-02-19T18:54:39.000Z",
            "fail_reason": "nothing"
          },
          {
            "id": 3,
            "type": "agent",
            "status": "finished",
            "call_id": 3,
            "user_id": 5,
            "end_user_id": null,
            "call_duration": 21,
            "hold_duration": null,
            "connected_at": "2016-02-19T18:54:18.000Z",
            "ended_at": "2016-02-19T18:54:39.000Z",
            "fail_reason": "nothing"
          },
          {
            "id": 6,
            "type": "agent",
            "status": "finished",
            "call_id": 3,
            "user_id": 12,
            "end_user_id": null,
            "call_duration": 21,
            "hold_duration": null,
            "connected_at": "2016-02-19T18:54:18.000Z",
            "ended_at": "2016-02-19T18:54:39.000Z",
            "fail_reason": "nothing"
          }
        ],
        "offer_type": "cascade",
        "offer_events": [
          {
            "casting_time": "2018-11-12T15:52:38.000Z",
            "group": "Group 1"
          }
        ],
        "answer_type": "manual",
        "outbound_number": null,
        "dispositions": [
            {
                "user_id": 3,
                "participant_id": 225,
                "code": "Product question"
            },
            {
                "user_id": 3,
                "transfer_id": 1,
                "participant_id": 226,
                "code": "Requires follow up"
            }
        ],
        "consumer_handle_durations": [
          {
            "id": 100,
            "call_duration": 314,
            "hold_duration": 3,
            "started_at":  "2016-02-19T18:50:08.000Z",
            "ended_at": "2016-02-19T18:55:22.000Z"
          }
        ],
        "consumer_in_menu_durations": [
          {
            "id": 100,
            "event": "finished",
            "duration": 238,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "started_at":  "2016-02-19T18:50:08.000Z",
            "ended_at": "2016-02-19T18:54:06.000Z"
          }
        ],
        "consumer_event_durations": [
          {
            "id": 10,
            "type": "payment",
            "event": "finished",
            "duration": 20,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "started_at": "2016-02-19T18:54:38.000Z",
            "ended_at": "2016-02-19T18:54:58.000Z"
          },
          {
            "id": 11,
            "type": "csat",
            "event": "abandoned",
            "duration": 4,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "started_at": "2016-02-19T18:54:39.000Z",
            "ended_at": "2016-02-19T18:54:43.000Z"
          }
        ],
        "handle_durations": [
          {
            "id": 10001,
            "agent_id": 5,
            "acw_duration": 0,
            "bcw_duration": 0,
            "call_duration": 21,
            "assigned_connection_duration": 10,
            "hold_duration": 3,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "barged": 0,
            "transfer": 0,
            "transfer_id": null,
            "transfer_cold": 0,
            "started_at": "2016-02-19T18:54:18.000Z",
            "ended_at": "2016-02-19T18:54:39.000Z",
            "scheduled_at": null
          },
          {
            "id": 10002,
            "agent_id": 5,
            "acw_duration": 25,
            "bcw_duration": 0,
            "call_duration": 0,
            "assigned_connection_duration": 0,
            "hold_duration": 0,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "barged": 0,
            "transfer": 0,
            "transfer_id": null,
            "transfer_cold": 0,
            "started_at": "2016-02-19T18:54:39.000Z",
            "ended_at": "2016-02-19T18:55:04.000Z",
            "scheduled_at": null
          },
          {
            "id": 10003,
            "agent_id": 12,
            "acw_duration": 1,
            "bcw_duration": 0,
            "call_duration": 21,
            "assigned_connection_duration": 5,
            "hold_duration": 0,
            "menu_path_id": 4,
            "menu_path": "Deathstar/Returns",
            "lang": "en",
            "barged": 0,
            "transfer": 1,
            "transfer_id": 11,
            "transfer_cold": 0,
            "started_at": "2016-02-19T18:54:18.000Z",
            "ended_at": "2016-02-19T18:54:39.000Z",
            "scheduled_at": null
          }
        ],
        "queue_durations": [
          {
            "id": 20011,
            "agent_id": 5,
            "queue_duration": 12,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": 0,
            "transfer_id": null,
            "transfer_cold": 0,
            "started_at": "2016-02-19T18:54:06.000Z",
            "ended_at": "2016-02-19T18:54:18.000Z",
            "service_level_abandon_time_threshold": 10,
            "service_level_event": "in_sla",
            "service_level_target_percent": 90,
            "service_level_target_time": 60
          },
          {
            "id": 20012,
            "agent_id": 12,
            "queue_duration": 10,
            "menu_path_id": 21,
            "menu_path": "Deathstar/Returns",
            "lang": "en",
            "transfer": 1,
            "transfer_id": 11,
            "transfer_cold": 0,
            "started_at": "2016-02-19T18:54:08.000Z",
            "ended_at": "2016-02-19T18:54:18.000Z",
            "service_level_abandon_time_threshold": 10,
            "service_level_event": "not_in_sla",
            "service_level_target_percent": 90,
            "service_level_target_time": 60
          }
        ],
        "virtual_agent": {
          "id": 10,
          "name": "D2-R2"
        },
        "virtual_agent_deflected_escalations": [
          {
            "id": 1,
            "deflection": "after_hours",
            "escalation_id": 1,
            "escalation_reason": "by_end_user_message",
            "escalated_at": "2016-02-19T18:54:06.000Z",
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "virtual_agent": {
              "id": 10,
              "name": "D2-R2"
            }
          }
        ],
        "virtual_agent_handle_durations": [
          {
            "id": 1,
            "virtual_agent": {
              "id": 10,
              "name": "D2-R2"
            },
            "call_duration": 11,
            "escalation_reason": "by_end_user_message",
            "sentiment": 85,
            "response_count": 11,
            "fallback_response_count": 1,
            "initiated_by": "end_user",
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": false,
            "transfer_id": null,
            "started_at": "2016-02-19T18:52:36.000Z",
            "ended_at": "2016-02-19T18:54:06.000Z"
          }
        ]
      }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
