---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-wait-time/
title: Wait time endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:09.815514+00:00
---

# Wait time endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-wait-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Wait time endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides the Wait time endpoint to get the current wait times for queues of different channel types.

## Wait time

Parameter | Required | Data Type | Definition  
---|---|---|---  
lang | TRUE | String | Language code of the queue. (e.g. 'en')  
menu_id | FALSE | Integer | Response will filter all menus in that menu's subtree, including that menu.  
menu_type | FALSE | String | Returns menus of specific types. Possible values: ivr_menu, mobile_menu, web_menu).  
channel_type | FALSE | String | Returns menus of a specific channel. Possible values: voice_call, chat).  
wait[from] | FALSE | Integer | Returns records if they have a wait greater than the value.  
wait[to] | FALSE | Integer | Returns records if they have a wait less than the value.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/wait_times
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Wait times for mobile queues

This example demonstrates how to retrieve the wait times for the mobile queues.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
menu_type | mobile_menu |   
  
**_Body: None_**

##### Response: Wait times for Mobile queues
    
    
    [
        {
            "menu_id": 29,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Laptop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 42,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Desktop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 43,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Smart Phone",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

#### Wait times between wait[from] to wait[to]

This example demonstrates how to retrieve the calls that have wait times between the wait from and wait to values.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
wait[from] | 5 |   
wait[to] | 15 |   
  
**_Body: None_**

##### Response: Wait times between wait[from] to wait[to]
    
    
    [
        {
            "menu_id": 3,
            "menu_type": "web_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Web App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 29,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Laptop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 42,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Desktop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 44,
            "menu_type": "web_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Mobile App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 43,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Smart Phone",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

#### Wait times of the voice call for mobile queues greater than 5 seconds

This example demonstrates how to retrieve the mobile voice calls that have a wait time greater than 5 seconds.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
menu_type | mobile_menu |   
channel_type | voice_call |   
wait[from] | 5 |   
  
**_Body: None_**

##### Response: Wait times of the voice call for Mobile queues greater than 5 seconds
    
    
    [
        {
            "menu_id": 29,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Laptop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 42,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Desktop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 43,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Smart Phone",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

#### Wait times for a specific menu

This example demonstrates how to retrieve the wait times for a specific menu ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
menu_id | 9 |   
  
**_Body: None_**

##### Response: Wait times for a specific menu
    
    
    [
        {
            "menu_id": 9,
            "menu_type": "ivr_menu",
            "voice_call": 10,
            "materialized_path": "Death Star",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

#### Wait times for all voice calls

This example demonstrates how to retrieve the wait times for all current voice calls.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
channel_type | voice_call |   
  
**_Body: None_**

##### Response: Wait times for all voice calls
    
    
    [
        {
            "menu_id": 3,
            "menu_type": "web_menu",
            "voice_call": 10,
            "materialized_path": "Web App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 9,
            "menu_type": "ivr_menu",
            "voice_call": 10,
            "materialized_path": "Death Star",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 29,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Laptop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 41,
            "menu_type": "ivr_menu",
            "voice_call": 10,
            "materialized_path": "Lock Star",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 42,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Desktop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 44,
            "menu_type": "web_menu",
            "voice_call": 10,
            "materialized_path": "Mobile App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 43,
            "menu_type": "mobile_menu",
            "voice_call": 10,
            "materialized_path": "Smart Phone",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

#### Wait times for English queues

This example demonstrates how to retrieve all wait times for the queues that have language of English.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
lang | en |   
  
**_Body: None_**

##### Response: Wait times for English queues
    
    
    [
        {
            "menu_id": 3,
            "menu_type": "web_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Web App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 9,
            "menu_type": "ivr_menu",
            "voice_call": 10,
            "materialized_path": "Death Star",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 29,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Laptop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 41,
            "menu_type": "ivr_menu",
            "voice_call": 10,
            "materialized_path": "Lock Star",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 42,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Desktop",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 44,
            "menu_type": "web_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Mobile App",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        },
        {
            "menu_id": 43,
            "menu_type": "mobile_menu",
            "chat": 10,
            "voice_call": 10,
            "materialized_path": "Smart Phone",
            "logged_in_agents": 3,
            "available_agents": 2,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
