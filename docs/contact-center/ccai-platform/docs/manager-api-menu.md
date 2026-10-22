---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-menu/
title: Menu endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:13.637177+00:00
---

# Menu endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-menu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Menu endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Menus represent a queue that an agent may be assigned to, and options that an end user may select when reaching out to an agent. Each object represents a single menu.

There are seven menu endpoints:

  * `/menu` \- pulls a list of menus.

  * `/menu/tree` \- pulls menus in a tree structure, which mimics the path an end user would use to get in touch with an agent.

  * `/menu/{:id}` \- pulls a single menu resource.

  * `/menu/current_status` \- Returns current queue status for menus with consumers waiting in queue.

  * `/menu/sla` \- Returns an SLA for all menu paths from now through the previous specified number of minutes.

  * `/menu/sla_by_queue_group` \- Returns an SLA for all queue groups from now through the previous specified number of minutes.

  * `/menus/operation_hours` \- Returns the hours of operation of the menu.




Refer to the following model to determine which fields might contain PII:
    
    
       {
        "id": 0,
        "name": "string",
        "parent_id": 0,
        "position": 0,
        "deleted": true,
        "hidden": "string",
        "menu_type": "ivr_menu",
        "output_msg": "string",
        "agent_assignments": [
          {
            "lang": "en",
            "queue_level": "primary",
            "channel_type": "chat",
            "assignee": {
              "id": 0,
              "name": "string", // This may be considered PII
              "last_name": "string", // This may be considered PII
              "first_name": "string", // This may be considered PII
              "agent_number": "string",
              "avatar_url": "string"
            }
          }
        ],
        "team_assignments": [
          {
            "lang": "en",
            "queue_level": "primary",
            "channel_type": "chat",
            "team": {
              "id": 0,
              "name": "string",
              "parent_id": 0,
              "position": 0,
              "deleted": true,
              "agents_count": 0,
              "assignees": {
                "id": 0,
                "name": "string", // This may be considered PII
                "last_name": "string", // This may be considered PII
                "first_name": "string", // This may be considered PII
                "agent_number": "string",
                "avatar_url": "string"
              }
            }
          }
        ]
      }
    

## Menu list

Parameter | Required | Data Type | Definition  
---|---|---|---  
sort_column | FALSE | String | Sorts response based on any field in the response object.  
sort_direction | FALSE | ASC or DESC | Notes the direction of the sort, whether ascending or descending  
page | FALSE | String | Pairs with per to note what page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
id[] | FALSE | Array[String] | Array[Strings]. Id of records to search and return  
name[] | FALSE | Array[String] | Returns records based on name of resource.   
parent_id[] | FALSE | Array[String] | Returns records based on the parent id of the given records  
position[] | FALSE | Array[String] | Returns records based on what position a menu is in  
menu_type[] | FALSE | Array[String] | Returns records based on the type of menu. Possible values: ivr_menu, mobile_menu, web_menu  
hidden[] | FALSE | Boolean | Returns records that have been hidden (True) or not including records that have been hidden (False)  
with_deleted | FALSE | Boolean | Returns records that have been deleted (True) or not including records that have been deleted (False)  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus
    

**_More example Requests/Responses:_**

### Example request: Menu list

**_Body: None_**

### Example response: Menu list
    
    
    [
        {
            "id": 1693,
            "name": "Death Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You have reached the Death Star",
            "hidden": false,
            "agent_assignments": [
                {
                    "lang": "en",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "assignee": {
                        "id": 97,
                        "agent_number": 97,
                        "name": "Darth Vader",
                        "last_name": "Darth",
                        "first_name": "Vader"
                    }
                },
                {
                    "lang": "it",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "assignee": {
                        "id": 1407,
                        "agent_number": 123,
                        "name": "Moff Tarkin",
                        "last_name": "Moff",
                        "first_name": "Tarkin"
                    }
                }
            ],
            "team_assignments": [
                {
                    "lang": "en",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "team": {
                        "id": 10,
                        "name": "Storm Troopers",
                        "parent_id": null,
                        "position": 1,
                        "agents_count": 48,
                        "deleted": false,
                        "assignees": [
                            {
                                "id": 1,
                                "agent_number": null,
                                "name": "Storm Troooper 1",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            },
    {
                                "id": 2,
                                "agent_number": null,
                                "name": "Storm Troooper 2",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            },
    {
                                "id": 3,
                                "agent_number": null,
                                "name": "Storm Troooper 3",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            }
                        ]
                    }
                }
            ]
        }]
    

**_Status Code:_** 200

## Menu tree

Parameter | Required | Data Type | Definition  
---|---|---|---  
menu_type | FALSE | Array[String] | Returns records based on the type of menu. Possible values: ivr_menu, mobile_menu, web_menu  
lang | FALSE | String | Returns records that have a specific language property. Possible Values: en, es, fr, de  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/tree
    

**_More example Requests/Responses:_**

### Example request: Menu tree

**_Body: None_**

### Example response: Menu tree
    
    
    [
        {
            "id": 2029,
            "name": "Mobile 1",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "mobile_menu",
            "output_msg": null,
            "hidden": false,
            "children": []
        },
        {
            "id": 2024,
            "name": "Death Star Venting System",
            "parent_id": null,
            "position": 1,
            "deleted": false,
            "menu_type": "mobile_menu",
            "output_msg": null,
            "hidden": false,
            "children": []
        },
        {
            "id": 2025,
            "name": "Droid Repair",
            "parent_id": null,
            "position": 2,
            "deleted": false,
            "menu_type": "mobile_menu",
            "output_msg": null,
            "hidden": false,
            "children": []
        },
        {
            "id": 2049,
            "name": "Emperor's Hotline",
            "parent_id": null,
            "position": 3,
            "deleted": false,
            "menu_type": "mobile_menu",
            "output_msg": null,
            "hidden": false,
            "children": []
        },
        {
            "id": 2026,
            "name": "Storm Trooper Armor",
            "parent_id": null,
            "position": 4,
            "deleted": false,
            "menu_type": "mobile_menu",
            "output_msg": null,
            "hidden": false,
            "children": [
                {
                    "id": 2036,
                    "name": "Armor Polishing Team",
                    "parent_id": 2026,
                    "position": 0,
                    "deleted": false,
                    "menu_type": "mobile_menu",
                    "output_msg": null,
                    "hidden": false,
                    "children": []
                }
            ]
        }]
    

**_Status Code:_** 200

## Single menu

Parameter | Required | Data Type | Definition  
---|---|---|---  
record_id | FALSE | String | Returns specific record based on id  
with_deleted | FALSE | Boolean | Returns records that have been deleted (True) or not including records that have been deleted (False)  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/{​{menu_id}​}
    

**_More example Requests/Responses:_**

### Example request: Single menu

**_Body: None_**

### Example response: Single menu
    
    
    [
        {
            "id": 1693,
            "name": "Death Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You have reached the Death Star",
            "hidden": false,
            "agent_assignments": [
                {
                    "lang": "en",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "assignee": {
                        "id": 97,
                        "agent_number": 97,
                        "name": "Darth Vader",
                        "last_name": "Darth",
                        "first_name": "Vader"
                    }
                },
                {
                    "lang": "it",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "assignee": {
                        "id": 1407,
                        "agent_number": 123,
                        "name": "Moff Tarkin",
                        "last_name": "Moff",
                        "first_name": "Tarkin"
                    }
                }
            ],
            "team_assignments": [
                {
                    "lang": "en",
                    "queue_level": "primary",
                    "channel_type": "voice_call",
                    "team": {
                        "id": 10,
                        "name": "Storm Troopers",
                        "parent_id": null,
                        "position": 1,
                        "agents_count": 48,
                        "deleted": false,
                        "assignees": [
                            {
                                "id": 1,
                                "agent_number": null,
                                "name": "Storm Troooper 1",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            },
    {
                                "id": 2,
                                "agent_number": null,
                                "name": "Storm Troooper 2",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            },
    {
                                "id": 3,
                                "agent_number": null,
                                "name": "Storm Troooper 3",
                                "last_name": "Storm ",
                                "first_name": "Admin1",
                                "avatar_url": "https://subdomain.somedomain.com/data_uri_upload20171201-21853-1ijzccm.png"
                            }
                        ]
                    }
                }
            ]
        }]
    

**_Status Code:_** 200

## Menus current status

Menus Current Status returns all menus with queued calls or chats with additional data on durations of those queued items.

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/current_status
    

**_More example Requests/Responses:_**

### Example request: Menus current status

**_Body: None_**

### Example response: Menus current status
    
    
    [
        {
            "menu_id": 10,
            "lang": "en",
            "menu_path_id": 5,
            "menu_path": "zdco IVR Support/1 Day Shipping",
            "comm_type": "Call",
            "in_queue_count": 2,
            "oldest_in_queue": "2021-05-10T22:17:21.000Z",
            "oldest_duration_in_queue": 300,
            "total_queue_duration": 400,
            "average_queue_duration": 200
        }
    ]
    

**_Status Code:_** 0

## Menu SLA

Parameter | Required | Data Type | Definition  
---|---|---|---  
channel | TRUE | String | String. Values accepted: call, chat  
minutes | TRUE | String | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/sla
    

**_Query params:_**

Key | Value | Description  
---|---|---  
channel | {channel} | String. Values accepted: call, chat  
minutes | {minutes} | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_More example Requests/Responses:_**

### Example request: Menu SLA

**_Query:_**

Key | Value | Description  
---|---|---  
channel | {channel} | String. Values accepted: call, chat  
minutes | {minutes} | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_Body: None_**

### Example response: Menu SLA
    
    
    [
        {
            "menu_path_id": 100,
            "lang": "en",
            "menu_path": "Support/1 Day Shipping",
            "sla": 96.5
        },
        {
            "menu_path_id": 100,
            "lang": "es",
            "menu_path": "Support/1 Day Shipping Spanish",
            "sla": 99.0
        },
        {
            "menu_path_id": 101,
            "lang": "en",
            "menu_path": "Support/3 Day Shipping",
            "sla": 0.0
        }
    ]
    

**_Status Code:_** 200

## Queue groups SLA

Parameter | Required | Data Type | Definition  
---|---|---|---  
channel | TRUE | String | String. Values accepted: call, chat  
minutes | TRUE | String | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/sla_by_queue_groups
    

**_Query params:_**

Key | Value | Description  
---|---|---  
channel | {channel} | String. Values accepted: call, chat  
minutes | {minutes} | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_More example Requests/Responses:_**

### Example request: Queue groups SLA

**_Query:_**

Key | Value | Description  
---|---|---  
channel | {channel} | String. Values accepted: call, chat  
minutes | {lminutes} | String. The number of minutes to look back from now when calculating SLA. Example, a value of 15 would be requesting SLA for the last 15 minutes for each menu path  
  
**_Body: None_**

### Example response: Queue groups SLA
    
    
    [
        {
            "queue_group_id": 20,
            "queue_group_name": "Shipping",
            "sla": null
        },
        {
            "queue_group_id": 24,
            "queue_group_name": "Customer Support",
            "sla": 99.2
        },
        {
            "queue_group_id": 29,
            "queue_group_name": "Escalations",
            "sla": 98.3
        }
    ]
    

**_Status Code:_** 200

## Menu operation hours

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/menus/operation_hours
    

**_Query params: None_**

**_More example Requests/Responses:_**

### Example request: Menu operation hours

**_Query: None_**

**_Body: None_**

### Example response: Menu operation hours
    
    
    [
        {
            "created_at": "2020-07-31T03:08:29.000Z",
            "fri_end_time": 86400,
            "fri_start_time": 0,
            "holidays": [],
            "id": 1,
            "mon_end_time": 86400,
            "mon_start_time": 0,
            "sat_end_time": 86400,
            "sat_start_time": 0,
            "sun_end_time": 86400,
            "sun_start_time": 0,
            "thu_end_time": 86400,
            "thu_start_time": 0,
            "time_zone": "Africa/Cairo",
            "tue_end_time": 86400,
            "tue_start_time": 0,
            "updated_at": "2021-03-24T13:23:43.000Z",
            "wed_end_time": 86400,
            "wed_start_time": 0
        },
        {
            "created_at": "2022-08-01T11:33:21.000Z",
            "fri_end_time": 28800,
            "fri_start_time": 21600,
            "holidays": [],
            "id": 2,
            "mon_end_time": 28800,
            "mon_start_time": 21600,
            "sat_end_time": 0,
            "sat_start_time": 0,
            "sun_end_time": 0,
            "sun_start_time": 0,
            "thu_end_time": 28800,
            "thu_start_time": 21600,
            "time_zone": "Europe/Helsinki",
            "tue_end_time": 28800,
            "tue_start_time": 21600,
            "updated_at": "2022-11-09T10:47:20.000Z",
            "wed_end_time": 28800,
            "wed_start_time": 21600
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
