---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-sms/
title: SMS endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:41:32.762445+00:00
---

# SMS endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-sms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SMS endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides the Outbound SMS endpoint for the SMS channel.

## Outbound SMS

Parameter | Required | Data Type | Definition  
---|---|---|---  
chat_type | TRUE | String | Chat type to create. "Messaging (API)", "SMS" (deprecated) are available for now | Messaging (API)  
end_user_number | TRUE | String | Number the text message is to be sent to | `{end_user_number}`  
outbound_number | TRUE | String | Outbound phone number to be used for sending the SMS message | `{outbound_number}`  
message | TRUE | String | SMS message to be sent to consumer | `{message}`  
ticket_id | FALSE | String | CRM ticket ID that will be associated with session | `{ticket_id}`  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/sms
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    
    

### Example requests and responses

The following sections provide example requests to the endpoint.

#### Create an outbound SMS chat with ticket ID

This example demonstrates how to create an outbound SMS to an end-user that is associated with a ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Create an outbound SMS chat with ticket_id
    
    
    {
      "id": 114,
      "lang": "en",
      "chat_type": "Messaging (SMS)",
      "status": "selecting",
      "created_at": "2021-10-04T17:20:51.000Z",
      "queued_at": null,
      "assigned_at": null,
      "ends_at": null,
      "wait_duration": 0,
      "chat_duration": 0,
      "rating": null,
      "has_feedback": false,
      "out_ticket_id": null,
      "out_ticket_url": null,
      "verified": false,
      "disconnected_by": "disconnected_by_unknown",
      "fail_reason": null,
      "selected_menu": null,
      "menu_path": null,
      "agent_info": null,
      "end_user": {
        "id": 87,
        "identifier": null,
        "out_contact_id": null
      },
      "photos": [],
      "videos": [],
      "transfers": [],
      "participants": [
        {
          "id": 205,
          "type": "end_user",
          "status": "connected",
          "chat_id": 114,
          "user_id": null,
          "end_user_id": 87,
          "chat_duration": null,
          "connected_at": "2021-10-04T17:20:51.000Z",
          "ended_at": null,
          "fail_reason": "nothing"
        }
      ],
      "offer_type": null,
      "offer_events": [],
      "answer_type": "manual",
      "outbound_number": "+16285550199"
    }
    

**_Status Code:_** 200

#### Create an outbound SMS chat and assign it to an agent using agent ID

This example demonstrates how to create an outbound SMS that is assigned to an agent based on the provided agent ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "agentId": 1
    }
    

##### Response: Create an outbound SMS chat and assign it to an agent using agentId
    
    
    {
        "id": 114,
        "lang": "en",
        "chat_type": "Messaging (SMS)",
        "status": "assigned",
        "created_at": "2021-10-04T17:20:51.000Z",
        "queued_at": null,
        "assigned_at": "2021-10-04T17:20:53.000Z",
        "ends_at": null,
        "wait_duration": 0,
        "chat_duration": 0,
        "rating": null,
        "has_feedback": false,
        "out_ticket_id": null,
        "out_ticket_url": null,
        "verified": false,
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
            "id": 1,
            "agent_number": 9,
            "email": "john.doe@foo.com",
            "name": "John Doe",
            "first_name": "John",
            "last_name": "Doe",
            "avatar_url": "https://foobar.com/johndoe"
        },
        "end_user": {
            "id": 87,
            "identifier": null,
            "out_contact_id": null
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "participants": [
            {
                "id": 205,
                "type": "end_user",
                "status": "connected",
                "chat_id": 114,
                "user_id": null,
                "end_user_id": 87,
                "chat_duration": null,
                "connected_at": "2021-10-04T17:20:51.000Z",
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 206,
                "type": "agent",
                "status": "connected",
                "chat_id": 114,
                "user_id": 1,
                "end_user_id": null,
                "chat_duration": null,
                "connected_at": "2021-10-04T17:20:53.000Z",
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+16285550199"
    }
    

**_Status Code:_** 200

#### Create an outbound SMS chat and assign it to an agent email

This example demonstrates how to create an outbound SMS chat session and associate it with an agent based on providing the agent email address.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "agentEmail": "john.doe@foo.com"
    }
    

##### Response: Create an outbound SMS chat and assign it to an agent using agentId
    
    
    {
        "id": 114,
        "lang": "en",
        "chat_type": "Messaging (SMS)",
        "status": "assigned",
        "created_at": "2021-10-04T17:20:51.000Z",
        "queued_at": null,
        "assigned_at": "2021-10-04T17:20:53.000Z",
        "ends_at": null,
        "wait_duration": 0,
        "chat_duration": 0,
        "rating": null,
        "has_feedback": false,
        "out_ticket_id": null,
        "out_ticket_url": null,
        "verified": false,
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": null,
        "end_user": {
            "id": 87,
            "identifier": null,
            "out_contact_id": null
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "participants": [
            {
                "id": 205,
                "type": "end_user",
                "status": "connected",
                "chat_id": 114,
                "user_id": null,
                "end_user_id": 87,
                "chat_duration": null,
                "connected_at": "2021-10-04T17:20:51.000Z",
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 206,
                "type": "agent",
                "status": "connected",
                "chat_id": 114,
                "user_id": 1,
                "end_user_id": null,
                "chat_duration": null,
                "connected_at": "2021-10-04T17:20:53.000Z",
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+16285550199"
    }
    

**_Status Code:_** 200

#### Create an outbound SMS chat without ticket ID

This example demonstrates how to create an outbound SMS without associating it to a ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Create an outbound SMS chat without ticket_id
    
    
    {
      "id": 114,
      "lang": "en",
      "chat_type": "Messaging (SMS)",
      "status": "selecting",
      "created_at": "2021-10-04T17:20:51.000Z",
      "queued_at": null,
      "assigned_at": null,
      "ends_at": null,
      "wait_duration": 0,
      "chat_duration": 0,
      "rating": null,
      "has_feedback": false,
      "out_ticket_id": null,
      "out_ticket_url": null,
      "verified": false,
      "disconnected_by": "disconnected_by_unknown",
      "fail_reason": null,
      "selected_menu": null,
      "menu_path": null,
      "agent_info": null,
      "end_user": {
        "id": 87,
        "identifier": null,
        "out_contact_id": null
      },
      "photos": [],
      "videos": [],
      "transfers": [],
      "participants": [
        {
          "id": 205,
          "type": "end_user",
          "status": "connected",
          "chat_id": 114,
          "user_id": null,
          "end_user_id": 87,
          "chat_duration": null,
          "connected_at": "2021-10-04T17:20:51.000Z",
          "ended_at": null,
          "fail_reason": "nothing"
        }
      ],
      "offer_type": null,
      "offer_events": [],
      "answer_type": "manual",
      "outbound_number": "+16285550199"
    }
    

**_Status Code:_** 200

#### Error : chat_type needs to be provided

This example demonstrates the failure scenario where the 'chat_type' was not provided but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : chat_type needs to be provided
    
    
    {
        "message": "chat_type needs to be provided"
    }
    

**_Status Code:_** 400

#### Error : valid chat type needs to be provided

This example demonstrates the failure scenario where the chat type needs to be provided but was missing.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "In-app",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : valid chat type needs to be provided
    
    
    {
        "message": "valid chat type needs to be provided"
    }
    

**_Status Code:_** 400

#### Error : SMS is not enabled

This example demonstrates the failure scenario where an outbound SMS is initiated but SMS is not enabled.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

#### Response: Error : SMS is not enabled
    
    
    {
        "message": "SMS is not enabled"
    }
    

**_Status Code:_** 400

#### Error : Outbound SMS is not enabled

This example demonstrates the failure scenario where an SMS session is initiated but fails as the SMS channel is not enabled.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

#### Response: Error : Outbound SMS is not enabled
    
    
    {
        "message": "Outbound SMS is not enabled"
    }
    

**_Status Code:_** 400

#### Error : end-user number is required

This example demonstrates the failure scenario where the end-user number was not provided but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

#### Response: Error : end_user_number is required
    
    
    {
        "message": "end_user_number is required"
    }
    

**_Status Code:_** 400

#### Error : End-user number is invalid

This example demonstrates the failure scenario where the provided end-user number is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "12345",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

#### Response: Error : end_user_number is invalid
    
    
    {
        "message": "end_user_number is invalid"
    }
    

**_Status Code:_** 400

#### Error : Non-US phone number not allowed

This example demonstrates the failure scenario where the provided number is not a US phone number and is prohibited.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+82 000-000-0000",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : Non-US phone number not allowed
    
    
    {
        "message": "Non-US phone number not allowed"
    }
    

**_Status Code:_** 400

#### Error : Outbound number is required

This example demonstrates the failure scenario where the outbound number was not provided but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : outbound_number is required
    
    
    {
        "message": "outbound_number is required"
    }
    

**_Status Code:_** 400

#### Error : Outbound number is invalid

This example demonstrates the failure scenario where the provided outbound number is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "12345",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : outbound_number is invalid
    
    
    {
        "message": "outbound_number is invalid"
    }
    

**_Status Code:_** 400

#### Error : outbound_number is not found

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : outbound_number is not found
    
    
    {
        "message": "outbound_number is not found"
    }
    

**_Status Code:_** 400

#### Error : message is required

This example demonstrates the failure scenario where the message was not provided in the requires but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : message is required
    
    
    {
        "message": "message is required"
    }
    

**_Status Code:_** 400

##### Error : Outbound SMS failed. Consumer is already in an active SMS session.

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "chat_type": "Messaging (SMS)",
        "end_user_number": "+1 415-555-0100",
        "outbound_number": "+1 628-555-0199",
        "message": "lorem ipsum",
        "ticket_id": "5006x00000XXxxxXXX"
    }
    

##### Response: Error : Outbound SMS failed. Consumer is already in an active SMS session.
    
    
    {
        "message": "Outbound SMS failed. Consumer is already in an active SMS session."
    }
    

**_Status Code:_** 400

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
