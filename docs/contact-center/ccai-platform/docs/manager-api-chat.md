---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-chat/
title: Chat endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:36.238081+00:00
---

# Chat endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The following is a model of the chat resource. Refer to this model to determine which fields might contain PII.
    
    
    [
        {
            "id": 31354,
            "lang": "en",
            "chat_type": "Messaging Inbound (App Chat)",
            "status": "finished",
            "sub_status": "Disconnected by end user",
            "created_at": "2019-07-17T07:27:14.000Z",
            "assigned_at": "2019-07-17T07:27:20.000Z",
            "ends_at": "2019-07-17T07:29:02.000Z",
            "updated_at": "2019-07-17T07:29:02.000Z",
            "first_msg_sent_at": "2019-07-17T07:27:26.000Z",
            "last_msg_sent_at": "2019-07-17T07:27:28.000Z",
            "wait_duration": 0, //Deprecated, use queue_duration instead
            "queue_duration": 0,
            "chat_duration": 0,
            "verified": false,
            "rating": 0,
            "has_feedback": false,
            "out_ticket_id": "string",
            "out_ticket_url": "string",
            "finish_reason": "finish_reason_none",
            "fail_reason": null,
            "message_count": 3,
            "average_response_time": 0,
            "longest_response_time": 0,
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
                "items_count": 1,
                "name": "Ringo",
                "materialized_path": "3389"
            },
            "agent_info": {
              "id": 0,
              "name": "string",
              "last_name": "string",
              "first_name": "string",
              "agent_number": "string",
              "avatar_url": "string"
            },
            "end_user": {
              "id": 0,
              "identifier": "string",
              "out_contact_id": "string"
            },
            "photos": [
              {
                "id": 0,
                "photo_type": "photo",
                "url": "string"
              }
            ],
            "videos": [
              {
                "id": 0,
                "url": "string"
              }
            ],
            "transfers": [
              {
                "id": 0,
                "status": "transferring",
                "fail_reason": "nothing",
                "created_at": "2018-06-07T19:49:52.896Z",
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
                  "name": "string",
                  "last_name": "string",
                  "first_name": "string",
                  "agent_number": "string",
                  "avatar_url": "string"
                },
                "to_agent": {
                  "id": 0,
                  "name": "string",
                  "last_name": "string",
                  "first_name": "string",
                  "agent_number": "string",
                  "avatar_url": "string"
                }
              }
            ],
            "handle_durations": [
                {
                    "agent_id": 0,
                    "acw_duration": 0,
                    "chat_duration" 0,
                    "wait_duration": 0,
                    "menu_path_id": 0,
                    "lang": "en",
                    "transfer": false,
                    "started_at": "2019-07-17T07:27:14.000Z",
                    "ended_at": "2019-07-17T07:27:20.000Z",
                    "event": "chat_finished"
    
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
            ],
            "participants": [
              {
                "id": 0,
                "type": "end_user",
                "status": "waiting",
                "call_id": 0,
                "user_id": 0,
                "end_user_id": 0,
                "call_duration": 0,
                "hold_duration": 0,
                "connected_at": "2018-06-07T19:49:52.896Z",
                "ended_at": "2018-06-07T19:49:52.896Z",
                "fail_reason": "nothing"
              }
            ]
          }
            "offer_type": "cascade",
            "offer_events": [
                {
                    "casting_time": "2019-07-17T07:27:15.000Z",
                    "group": "Group 1"
                }
            ]
        },
    

The service_level_event field can only be one of the following values:

Service Level Event | Description  
---|---  
in_sla | Call was answered within SLA  
not_in_sla | Call was not answered within defined SLA  
excluded | Call was not included in SLA calculation (e.g. if call was abandoned)   
**Note:** `wait_duration` has been deprecated. Use `queue_duration` instead.

## Chats

Parameter | Required | Data Type | Definition  
---|---|---|---  
sort_column | FALSE | String | Sorts response based on any field in the response object.  
sort_direction | FALSE | ASC or DESC | Notes the direction of the sort, whether ascending or descending  
page | FALSE | String | Pairs with per to note what page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.  
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.  
assigned_at[from] | FALSE | Time in UTC | creates a lower bound of the assigned at field. All records returned will be after the inputted value.  
assigned_at[to] | FALSE | Time in UTC | creates an upper bound of the assigned at field. All records returned will be before the inputted value.  
ends_at[from] | FALSE | Time in UTC | creates a lower bound of the ends at field. All records returned will be after the inputted value.  
ends_at[to] | FALSE | Time in UTC | creates an upper bound of the ends at field. All records returned will be before the inputted value.  
updated_at[from] | FALSE | Time in UTC | creates a lower bound of the updated at field. All records returned will be after the inputted value.  
updated_at[to] | FALSE | Time in UTC | creates an upper bound of the updated at field. All records returned will be before the inputted value.  
created_at[from] | FALSE | Time in UTC | creates a lower bound of the created at field. All records returned will be after the inputted value.  
created_at[to] | FALSE | Time in UTC | creates an upper bound of the created at field. All records returned will be before the inputted value.  
rating[from] | FALSE | Number 1-5 or null | creates a lower bound of the rating field. All records returned will be after the inputted value.  
rating[to] | FALSE | Number 1-5 or null | creates an upper bound of the rating field. All records returned will be before the inputted value.  
first_msg_sent_at[from] | FALSE | Time in UTC | creates a lower bound of the first msg sent at field. All records returned will be after the inputted value.  
first_msg_sent_at[to] | FALSE | Time in UTC | creates an upper bound of the first msg sent at field. All records returned will be before the inputted value.  
last_msg_sent_at[from] | FALSE | Time in UTC | creates a lower bound of the last msg sent at field. All records returned will be after the inputted value.  
last_msg_sent_at[to] | FALSE | Time in UTC | creates an upper bound of the last msg sent at field. All records returned will be before the inputted value.  
chat_duration[from] | FALSE | Number | creates a lower bound of the chat duration field. All records returned will be after the inputted value.  
chat_duration[to] | FALSE | Number | creates an upper bound of the chat duration field. All records returned will be before the inputted value.  
message_count[from] | FALSE | Number | creates a lower bound of the message count field. All records returned will be after the inputted value.  
message_count[to] | FALSE | Number | creates an upper bound of the message count field. All records returned will be before the inputted value.  
average_response_time[from] | FALSE | Number | creates a lower bound of the average response time field. All records returned will be after the inputted value.  
average_response_time[to] | FALSE | Number | creates an upper bound of the average response time field. All records returned will be before the inputted value.  
longest_response_time[from] | FALSE | Number | creates a lower bound of the longest response time field. All records returned will be after the inputted value.  
longest_response_time[to] | FALSE | Number | creates an upper bound of the longest response time field. All records returned will be before the inputted value.  
wait_duration[from] | FALSE | Number | creates a lower bound of the wait duration field. All records returned will be after the inputted value.  
wait_duration[to] | FALSE | Number | creates an upper bound of the wait duration field. All records returned will be before the inputted value.  
id[] | FALSE | Array[String] | Array[Strings]. Id of records to search and return  
agent_id[] | FALSE | Array[String] | Filters response by agent id  
end_user_id[] | FALSE | Array[String] | Filters response based on the end user id  
chat_type[] | FALSE | Array[String] | Returns records based on how chat was accessed by the end user. Possible values: Messaging Inbound (App Chat), Messaging Inbound (Web Chat), Messaging (SMS)  
chat_status[] | FALSE | Array[String] | Returns records based on where the user is in the chat lifecycle. Possible values: queued, assigned, finished, canceled, failed, no_response  
verified[] | FALSE | Boolean | Returns records that either have been verified (True) or have not been verified (False)  
chat_fail_reason[] | FALSE | Array[String] | Returns records based on why a chat may have failed. Possible values: nothing, unknown, no_response, expired  
  
The `service_level_event` value can have the following values.

Service Level Event | Description  
---|---  
in_sla | Call was answered within SLA  
not_in_sla | Call was not answered within defined SLA  
excluded | Call was not included in SLA calculation (e.g. if call was abandoned)   
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/chats
    

**_More example Requests/Responses:_**

### Example request: Chats

**_Query:_**

Key | Value | Description  
---|---|---  
updated_at[from] | \\{updated_at\\[from\\]\\} | Time in UTC. creates a lower bound of the updated at field. All records returned will be after the inputted value.  
updated_at[to] | \\{updated_at\\[to\\]\\} | Time in UTC. creates an upper bound of the updated at field. All records returned will be before the inputted value.  
  
**_Body: None_**

### Example response: Chats
    
    
    [
      {
        "id": 1,
        "lang": "en",
        "chat_type": "Messaging Inbound (App Chat)",
        "status": "finished",
        "created_at": "2016-02-26T18:35:54.000Z",
        "assigned_at": "2016-02-26T18:36:05.000Z",
        "ends_at": "2016-02-26T18:37:24.000Z",
        "updated_at": "2016-02-26T18:37:24.000Z",
        "first_msg_sent_at": null,
        "last_msg_sent_at": null,
        "chat_duration": 11,
        "wait_duration": 22,
        "queue_duration": 22,
        "verified": true,
        "rating": 5,
        "has_feedback": false,
        "out_ticket_id": "209",
        "out_ticket_url": null,
        "fail_reason": null,
        "message_count": 0,
        "average_response_time": 0,
        "longest_response_time": 0,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
          "id": 4,
          "agent_number": "007",
          "name": "Storm Trooper 1",
          "last_name": "Storm",
          "first_name": "Trooper 1",
        },
        "end_user": {
          "id": 1,
          "identifier": "Death Star Carpentry",
          "out_contact_id": "360949501087"
        },
        "photos": [
          {
            "id": 3,
            "photo_type": "photo",
            "url": "true"
          }
        ],
        "consumer_handle_durations": [
          {
            "id": 100,
            "chat_duration": 314,
            "message_count": 10,
            "response_count": 6,
            "response_time_total": 85,
            "response_time_max": 25,
            "response_time_avg": 12,
            "started_at":  "2016-02-19T18:50:08.000Z",
            "ended_at": "2016-02-19T18:55:22.000Z"
          }
        ],
        "consumer_event_durations": [
          {
            "id": 11,
            "type": "csat",
            "event": "finished",
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
            "id": 30001,
            "agent_id": 4,
            "acw_duration": 0,
            "chat_duration": 11,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": 0,
            "transfer_id": null,
            "started_at": "2016-03-02T23:24:08.000Z",
            "ended_at": "2016-03-02T23:24:42.000Z",
            "response_count": 11,
            "response_time_total": 259,
            "response_time_max": 29,
            "response_time_avg": 24,
            "assigned_connection_duration": 10
          }
        ],
        "queue_durations": [
          {
            "id": 41234,
            "agent_id": 5,
            "queue_duration": 22,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": 0,
            "transfer_id": null,
            "transfer_cold": 0,
            "started_at": "2016-03-02T23:23:56.000Z",
            "ended_at": "2016-03-02T23:24:08.000Z",
            "service_level_abandon_time_threshold": 10,
            "service_level_event": "not_in_sla",
            "service_level_target_percent": 90,
            "service_level_target_time": 60
          }
        ]
        "videos": [],
        "transfers": [],
        "participants": [],
        "virtual_agent": null,
        "virtual_agent_deflected_escalations": [],
        "virtual_agent_handle_durations": []
      },
      {
        "id": 2,
        "lang": "en",
        "chat_type": "in-app",
        "status": "finished",
        "created_at": "2016-03-02T23:24:05.000Z",
        "assigned_at": "2016-03-02T23:24:08.000Z",
        "ends_at": "2016-03-02T23:24:42.000Z",
        "updated_at": "2016-03-02T23:24:42.000Z",
        "first_msg_sent_at": null,
        "last_msg_sent_at": null,
        "wait_duration": 12,
        "queue_duration": 12,
        "chat_duration": 34,
        "verified": false,
        "rating": 2,
        "has_feedback": false,
        "out_ticket_id": "214",
        "out_ticket_url": null,
        "fail_reason": null,
        "message_count": 0,
        "average_response_time": 0,
        "longest_response_time": 0,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": null,
        "end_user": {
          "id": 1,
          "identifier": "Death Star Carpentry",
          "out_contact_id": "360949501087"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "participants": [],
        "handle_durations": [
          {
            "id": 30001,
            "agent_id": 4,
            "acw_duration": 0,
            "chat_duration": 34,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": 0,
            "transfer_id": null,
            "started_at": "2016-03-02T23:24:08.000Z",
            "ended_at": "2016-03-02T23:24:42.000Z",
            "response_count": 11,
            "response_time_total": 259,
            "response_time_max": 29,
            "response_time_avg": 24,
            "assigned_connection_duration": 10
          }
        ],
        "queue_durations": [
          {
            "id": 41234,
            "agent_id": 5,
            "queue_duration": 12,
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": 0,
            "transfer_id": null,
            "transfer_cold": 0,
            "started_at": "2016-03-02T23:23:56.000Z",
            "ended_at": "2016-03-02T23:24:08.000Z",
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
            "escalation_reason": "by_end_user_message",
            "escalated_at": "2016-03-02T23:23:56.000Z",
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
            "chat_duration": 11,
            "escalation_reason": "by_end_user_message",
            "response_count": 11,
            "response_time_total": 34,
            "response_time_max": 4,
            "response_time_avg": 3,
            "fallback_response_count": 1,
            "initiated_by": "end_user",
            "menu_path_id": 11,
            "menu_path": "Deathstar/Shipping",
            "lang": "en",
            "transfer": false,
            "transfer_id": null,
            "started_at": "2016-03-02T23:23:16.000Z",
            "ended_at": "2016-03-02T23:23:56.000Z"
          }
        ]
      }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
