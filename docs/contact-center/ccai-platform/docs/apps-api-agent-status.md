---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-agent-status/
title: Agent status endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:51:12.007137+00:00
---

# Agent status endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-agent-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent status endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The agent status API endpoints provide access to the agent status objects. An agent object is created for each user that is configured in Contact Center AI Platform (CCAI Platform) that has a role including an agent permission.

The following are the agent status API endpoints:

  * Update agent statuses

  * Get agent statuses




Agent status endpoints let you modify the status of agents. They enable changes from **Available** to any custom status. Transitions to and from system-defined statuses like **In-Call** trigger an error. In addition, these endpoints supports bulk updates, simultaneously allowing status modifications for entire teams or selected groups of agents.

## Update agent status

This endpoint lets you update the status of agents. The following table shows the properties in the JSON body:

Property | Required | Data Type | Definition  
---|---|---|---  
status | TRUE | String | The status to set the agents to, for example available.  
agent_ids | TRUE | Arry Integer | ARRAY of agent IDs.  
team_ids | TRUE | Array Integer | ARRAY of team IDs.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/agent_statuses
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "status": "Available",
        "agent_ids": [
            11,
            12
        ],
        "team_ids": []
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Change agent statuses successfully

The following example demonstrates the request and associated response of changing some agents status where the action was successful.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "status": "Available",
        "agent_ids": [
            11,
            12
        ],
        "team_ids": [
            1
        ]
    }
    

##### Response:
    
    
    [
        {
            "agent_id": 11,
            "name": "Darth Vader",
            "email": "notanakinskywalker@empire.com",
            "agent_number": "Agent No.111",
            "previous_status": "lunch",
            "current_status": "Available"
        },
        {
            "agent_id": 12,
            "name": "Craig T",
            "email": "craigT@nelson.com",
            "agent_number": "Agent No.112",
            "previous_status": "In-call",
            "current_status": "In-call",
            "message": "Agent can't be changed from system status 'In-call'"
        },
        {
            "agent_id": 13,
            "name": "Raymond D",
            "email": "rayd@nelson.com",
            "agent_number": "Agent No.113",
            "previous_status": "Offline",
            "current_status": "Offline",
            "message": "Agent's status can't be changed if they are offline or logged out"
        }
    ]
    

**_Status Code:_** 200

#### Status does not exist

This example shows the request and associated response where the provided status does not exist and as such is considered invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    Body
    {
        "status": "Napping",
        "agent_ids": [
            11,
            12
        ],
        "team_ids": []
    }
    

##### Response: Error: status 'Napping' does not exist
    
    
    {
        "message": "status 'Napping' does not exist"
    }
    

**_Status Code:_** 400

#### Status set to system status

This example shows the request and response where the status is set to a system status, in this case "in-call". It is not possible to set the status of an agent to a status that is managed by the system.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    Body
    {
        "status": "In-call",
        "agent_ids": [
            11,
            12
        ]
    }
    

##### Response: Error: Agent can't be changed to system status 'In-call
    
    
    {
        "message": "Agent can't be changed to system status 'In-call'"
    }
    

**_Status Code:_** 400

## Get agent statuses

This endpoint lets you retrieve the status of agents. The following table shows the properties in the JSON body:

Property | Required | Data Type | Definition  
---|---|---|---  
status | TRUE | String | The status to set the agents to, for example available.  
agent_ids | FALSE | Arry Integer | ARRAY of agent IDs.  
team_ids | FALSE | Array Integer | ARRAY of team IDs.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/agent_statuses
    

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
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Get the status specific agents and teams

This example shows how to get the status of agents with IDs 11 and 12 and any agent on the team with ID 1.

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
    

##### Response: Status of requested agents
    
    
    [
        {
            "agent_id": 11,
            "name": "Darth Vader",
            "email": "notanakinskywalker@empire.com",
            "agent_number": "Agent No.111",
            "status": "lunch",
            "ip_addrs": [
                "34.211.11.101"
            ]
        },
        {
            "agent_id": 12,
            "name": "Craig T",
            "email": "craigT@nelson.com",
            "agent_number": "Agent No.112",
            "status": "In-call",
            "ip_addrs": [
                "34.211.11.102"
            ]
        },
        {
            "agent_id": 13,
            "name": "Raymond D",
            "email": "rayd@nelson.com",
            "agent_number": "Agent No.113",
            "status": "Offline",
            "ip_addrs": [
                "34.211.11.103"
            ]
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
