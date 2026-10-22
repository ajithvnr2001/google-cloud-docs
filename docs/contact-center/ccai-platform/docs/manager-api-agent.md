---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-agent/
title: Agent endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:16.924461+00:00
---

# Agent endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Agent endpoints provide a means to get agent objects. Each agent object represents a single agent inside of Contact Center AI Platform (CCAI Platform). Review the following model to see which fields might contain personally identifiable information (PII).
    
    
    [
      {
        "id": 0,
        "email": "string",
        "created_at": "2018-05-30T20:46:31.333Z",
        "last_login_time": "2018-05-30T20:46:31.333Z",
        "first_name": "string",
        "middle_name": "string",
        "last_name": "string",
        "avatar_url": "string",
        "agent_number": "string",
        "status": {
          "id": 0,
          "name": "string",
          "color": "string"
        },
        "status_updated_at": "2018-05-30T20:46:31.333Z",
        "crm_authenticated": true,
        "online": true,
        "wrap_up": true,
        "call_count": 0,
        "chat_count": 0,
        "location": "string",
        "roles": [
          "agent"
        ],
        "teams": [
          {
            "id": 0,
            "name": "string",
            "parent_id": 0,
            "position": 0,
            "deleted": true,
            "agents_count": 0
          }
        ],
        "channels": [
          {
            "channel_type": "chat",
            "menu": {
              "id": 0,
              "name": "string",
              "parent_id": 0,
              "position": 0,
              "deleted": true,
              "hidden": "string",
              "menu_type": "ivr_menu",
              "output_msg": "string"
            }
          }
        ]
      }
    ]
    

## Agents

Parameter | Required | Data Type | Definition  
---|---|---|---  
page | FALSE | String | Pairs with per to note what page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
per | FALSE | String | Pairs with page to note how many records would be included in a page of records. For example if per is made to be 200 and page is 2, the response would contain record 201-400, as page 1 would contain 1-200.   
id[] | FALSE | Array[String] | Array[Strings]. Id of records to search and return  
agent_number[] | FALSE | Array[String] | Agent numbers as assigned by the administrator at the time of creating an agent  
status_id[] | FALSE | Array[String] | Filters by agent status   
online[] | FALSE | Boolean | Filter by if agents are online or not  
wrap_up[] | FALSE | Boolean | Filter by if agents are in wrap up status  
location[] | FALSE | Array[String] | Filters by agent location  
last_login_time[from] | FALSE | Time in UTC | creates a lower bound of the last login time field. All records returned will be after the inputted value.  
last_login_time[to] | FALSE | Time in UTC | creates a upper bound of the last login time field. All records returned will be before the inputted value.  
status_updated_at[from] | FALSE | Time in UTC | creates a lower bound of the status updated at field. All records returned will be after the inputted value.  
status_updated_at[to] | FALSE | Time in UTC | creates a upper bound of the status updated at field. All records returned will be before the inputted value.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/agents
    

**_More example Requests/Responses:_**

### Example request: Agents example

**_Body: None_**

### Example response: Agents example
    
    
    [
      {
        "id": 45,
        "email": "craigT@nelson.com",
        "roles": [
          "agent"
        ],
        "first_name": "Craig T",
        "middle_name": null,
        "last_name": "Nelson",
        "avatar_url": "https://subdomain.somedomain.com/default-profile.png",
        "agent_number": null,
        "crm_authenticated": false,
        "status": {
          "id": -6,
          "name": "Wrap-up",
          "color": "purple",
        },
        "online": false,
        "wrap_up": false,
        "call_count": 0,
        "chat_count": 0,
        "location": null,
        "created_at": "2016-11-10T00:15:04.000Z",
        "last_login_time": "2016-11-10T00:17:57.000Z",
        "status_updated_at": null,
        "teams": [
          {
            "id": 163,
            "name": "team CTN",
            "parent_id": null,
            "position": 11,
            "agents_count": 12,
            "deleted": false
          }
        ],
        "channels": [
          {
            "channel_type": "voice_call",
            "menu": {
              "id": 2029,
              "name": "Mobile Queue",
              "parent_id": null,
              "position": 0,
              "deleted": false,
              "menu_type": "mobile_menu",
              "output_msg": null,
              "hidden": false
            }
          }
        ]
      },
      {
        "id": 60,
        "email": "notanakinskywalker@empire.com",
        "roles": [
          "agent"
        ],
        "first_name": "Darth",
        "middle_name": null,
        "last_name": "Vader",
        "avatar_url": "https://subdomain.somedomain.com/default-profile.png",
        "agent_number": null,
        "crm_authenticated": false,
        "status": {
          "id": -7,
          "name": "In-call",
          "color": "light_blue",
        },
        "online": false,
        "wrap_up": false,
        "call_count": 0,
        "chat_count": 0,
        "location": null,
        "created_at": "2017-02-03T19:44:14.000Z",
        "last_login_time": "2017-02-03T20:05:31.000Z",
        "status_updated_at": "2017-02-04T12:36:11.000Z",
        "teams": [],
        "channels": [
          {
            "channel_type": "voice_call",
            "menu": {
              "id": 1693,
              "name": "Premium Support",
              "parent_id": null,
              "position": 0,
              "deleted": false,
              "menu_type": "ivr_menu",
              "output_msg": "You selected premium support",
              "hidden": false
            }
          }
        ]
      },
      {
        "id": 81,
        "email": "email@email.com",
        "roles": [
          "agent"
        ],
        "first_name": "Barry",
        "middle_name": null,
        "last_name": "Allen",
        "avatar_url": "https://subdomain.somedomain.com/default-profile.png",
        "agent_number": null,
        "crm_authenticated": false,
        "status": {
          "id": -10,
          "name": "Offline",
          "color": "grey",
        },
        "online": false,
        "wrap_up": false,
        "call_count": 0,
        "chat_count": 0,
        "location": null,
        "created_at": "2017-03-13T23:47:39.000Z",
        "last_login_time": "2017-03-13T23:48:17.000Z",
        "status_updated_at": "2017-03-13T23:56:04.000Z",
        "teams": [],
        "channels": [
          {
            "channel_type": "voice_call",
            "menu": {
              "id": 2028,
              "name": "Speed Issues",
              "parent_id": 2027,
              "position": 0,
              "deleted": false,
              "menu_type": "mobile_menu",
              "output_msg": null,
              "hidden": false
            }
          }
        ]
      }
    ]
    

**_Status Code:_** 200

## Agents current status

Agents Current Status returns all logged in agents and their current status, how long they have been in that status, and additional information to indicate if the agent is on hold and for how long.

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/agents/current_status
    

**_More example Requests/Responses:_**

### Example Request: Agents Current Status

**_Body: None_**

### Example Response: Agents Current Status
    
    
    [
      {
        "id": 1,
        "status": "Available",
        "status_id": 0,
        "status_updated_at": "2021-05-10T17:45:01.000Z",
        "on_hold": false,
        "on_hold_duration": 0
      }
    ]
    

**_Status Code:_** 0

## Expect unrecognized JSON keys in API responses

All API updates are backward compatible. We reserve the right to introduce new JSON keys in existing API responses at any time. We recommend handling responses defensively by disregarding any unrecognized keys to maintain continued functionality.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
