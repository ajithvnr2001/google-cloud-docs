---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-agent-logout/
title: Force agent logout endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:32.153578+00:00
---

# Force agent logout endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-agent-logout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Force agent logout endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The force logout agents endpoint let you forcibly log out online agents. Agents engaged in active calls or chats are logged out automatically when they complete their current interactions. Idle agents are logged out immediately. This endpoint supports forced logouts of specific agents, entire teams, or agents identified by IP addresses with CIDR notation, a list of IPv4/IPv6 addresses, or IP ranges. For a large number of agents, a background job is created to manage the logout process efficiently.

The following are the force agent logout API endpoints:

  * Force logout agents

  * Force logout agent jobs




## Force logout agents

This endpoint provides the ability for the logout of specific agents. Agents can be identified by the following:

  * agent ID.

  * team ID.

  * IP address.




**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/agent_statuses/force_logout
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Body:_**
    
    
    {
        "agent_ids": [
            11,
            12
        ],
        "team_ids": [
            1
        ],
        "ip_addrs": [
            "34.211.11.0/24"
        ]
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Logout agents successfully

This example demonstrates how to log out specific agents based on the agent ID and team ID. In this case they were agent IDs 11 and 12 as well as team ID 1.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "agent_ids": [
            11,
            12
        ],
        "team_ids": [
            1
        ]
    }
    

##### Response
    
    
    [
        {
            "agent_id": 11,
            "name": "Darth Vader",
            "email": "notanakinskywalker@empire.com",
            "agent_number": "Agent No.111",
            "previous_status": "lunch",
            "current_status": "Offline"
        },
        {
            "agent_id": 12,
            "name": "Craig T",
            "email": "craigT@nelson.com",
            "agent_number": "Agent No.112",
            "previous_status": "Unavailable",
            "current_status": "Offline"
        },
        {
            "agent_id": 13,
            "name": "Raymond D",
            "email": "rayd@nelson.com",
            "agent_number": "Agent No.113",
            "previous_status": "Break",
            "current_status": "Offline"
        }
    ]
    

**_Status Code:_** 200

#### Logout agents using IP address successfully

This example demonstrates how to logout agents by specifying an IP address range. In this case the provided IP address range is `34.211.11.0/24`.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "agent_ids": [
            11,
            12
        ],
        "team_ids": [
            1
        ],
        "ip_addrs": [
            "34.211.11.0/24"
        ]
    }
    

**_Status Code:_** 200

#### Logout agent job created

This example demonstrates how to request the agent logouts and the resultant job that is created.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "agent_ids": [
            11,
            12
        ],
        "team_ids": [
            1
        ],
        "ip_addrs": [
            "34.211.11.0/24"
        ]
    }
    

##### Response
    
    
    {
        "ip_addrs": [
            "34.211.11.0/16"
        ]
    }
    

**_Status Code:_** 200

#### In-call or in-chat agents will log out later

This example demonstrates how agents that are in a call or in a chat will be logged out later, after the chat or call is ended.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "agent_ids": [
            11,
            12
        ],
        "team_ids": []
    }
    

##### Response
    
    
    [
        {
            "agent_id": 11,
            "name": "Darth Vader",
            "email": "notanakinskywalker@empire.com",
            "agent_number": "Agent No.111",
            "previous_status": "In-call",
            "current_status": "In-call",
            "message": "will force logout as soon as the ongoing call/chat is completed"
        },
        {
            "agent_id": 12,
            "name": "Craig T",
            "email": "craigT@nelson.com",
            "agent_number": "Agent No.112",
            "previous_status": "In-chat",
            "current_status": "In-chat",
            "message": "will force logout as soon as the ongoing call/chat is completed"
        }
    ]
    

**_Status Code:_** 400

#### Error: cannot find agents

This example demonstrates the failure scenario where the provided agents couldn't be found.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "ip_addrs": [
            "34.211.11.0/24"
        ]
    }
    

##### Response: Error : cannot find any agent by input params
    
    
    {
        "message": "cannot find any agent by input params"
    }
    

**_Status Code:_** 400

## Force agent logout jobs

This endpoint lets you get the status of forced logout request for an agent.
    
    
    {
        "identifier": "string",
        "email": "string",
        "name": "string",
        "phone": "string"
    }
    

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/agent_statuses/force_logout/jobs/:id
    

**_Headers:_**

Key | Value | Description  
---|---|---  
id |  | The job ID of a submitted forced logout request.  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Successfully completed

This example demonstrates how to retrieve a job that has been completed successfully.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**
    
    
    Method: GET
    Type: 
    URL: https://{subdomain}.{domain}/apps/api/v1/agent_statuses/force_logout/jobs/105
    

##### Response
    
    
    {
        "id": 105,
        "status": "completed"
    }
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
