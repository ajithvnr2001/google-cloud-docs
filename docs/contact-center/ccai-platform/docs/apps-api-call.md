---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-call/
title: Call endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:22.912456+00:00
---

# Call endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The call API endpoints provide access to the call objects. A call object is created for every call that is made to and from Contact Center AI Platform (CCAI Platform).

The following are the call API endpoints:

  * Outbound call - `end_user_number`

  * Outbound call - `ticket_id`

  * Incoming call

  * Scheduled call

  * Update reserved data attributes during a call

  * Get reserved data attributes during a call

  * Pass data parameters to virtual agents mid-session


**Note:** The `lang` parameters in the API requests specifies the language of the call uses ISO 639-1 codes. (Default: "en"). It should be noted that these are case sensitive, for example fr-CA instead of fr-ca.

## Call object

The following is an example of the call object:
    
    
    [
      {
        "id": 0,
        "parent_id": 0,
        "lang": "en",
        "call_type": "Voice Scheduled (API)",
        "status": "scheduled",
        "created_at": "2018-06-07T19:49:52.896Z",
        "queued_at": "2018-06-07T19:49:52.896Z",
        "assigned_at": "2018-06-07T19:49:52.896Z",
        "connected_at": "2018-06-07T19:49:52.896Z",
        "ends_at": "2018-06-07T19:49:52.896Z",
        "scheduled_at": "2018-06-07T19:49:52.896Z",
        "wait_duration": 0,
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
        "fail_details": "string",
        "fail_reason": "nothing",
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
    ]
    

### Call status definitions

The status field can be in any of the following states:

Call Status | Description  
---|---  
Selecting | State that occurs when an end user has called into the contact center, but is still navigating the menu options prior to being placed in a leaf menu.  
Queued | State that occurs after the end user has selected a leaf menu node and initiated a call request to be deltcasted or multicasted to an agent.  
Assigned | State that occurs when an agent is selected to receive the end user call. This occurs when a call is picked up by an agent.  
Connecting | State that occurs after an agent is assigned, and a connection is being established between the end user and the agent.  
Connected | State that occurs when the call has established a connection and the agent and end user are both placed into a call.  
Finished | State that occurs when a call ends after it has been connected.  
Failed | State that occurs when a call ends before it was successfully connected. A fail reason will also be provided for additional details.  
Switching | State that occurs when a call fails while trying to connect and CCAI Platform attempts to connect the call with a different VOIP provider.  
Recovered | State that occurs when a failed call is called back. This new call is a child to the original call. Recovered notes that the call back is finished without error.  
Scheduled | State that occurs when an end-user has scheduled a future call using In-Web or In-App.  
Action Only | State that occurs when a call that is handled by our client's own telephony provider is connected to our iOS or Android SDK.  
Action Only Finished | State that occurs when a call that is handled by our client's own telephony provider is connected to our iOS or Android SDK and finishes  
Deflected | State that occurs based on the configuration for overcapacity queues or after hour calls. Deflection options include voicemail, schedule call among others. Deflection will vary based on channel (In-app, IVR, In-web)  
Voicemail | State that occurs when an end user is deflected to a voicemail option, and opts to leave a voicemail message to listened to later. This state is present when the end user is leaving the voicemail  
Voicemail Received | State that occurs after an end user has left a voicemail and an agent has not listened to the voicemail  
Voicemail Read | State that occurs when an agent has opened the voicemail to listen to.  
  
### Call type definitions

The `call_type` field can only be one of the following values:

Call Type | Description  
---|---  
Voice Outbound (API) | Call made from Outbound Call API.  
Voice Inbound (API) | Call made from Incoming Call API.  
Voice Scheduled (API) | Call made from Scheduled Call API.  
  
### Common API response codes

The following are the most common API Responses:

Response Code | Meaning  
---|---  
201 | The API request has been successful and will create a call  
202 | The API request has been successful, but manual intervention is required inside of the widget to complete the action  
400 | invalid call type - ensure call_type is supported  
400 | Agent is not available to take this call  
400 | Missing parameter - check to ensure that the required parameters have been added  
404 | Resource not found - Please check your subdomain  
  
## Outbound call - end_user_number

Parameter | Required | Data Type | Definition  
---|---|---|---  
call_tye | TRUE | String | Call tye to create. "Voice Outbound (API)", "OutboundCall" (deprecated) are available for now  
agent_email | TRUE | String | Email address for the agent who will be assigned to the outbound call.  
ticket_id | FALSE | String | CRM ticket ID and it will dial to the end user who is tied to the ticket.  
end_user_number | FALSE | String | End user phone number which will be dialing. ticket_id has a higher priority than end_user_number.  
outbound_number | FALSE | String | Well-formed outbound number which is managed from Settings > Phone Numbers > Phone Number Management. Default outbound number will be used when empty  
lang | FALSE | String | Language of the call. Uses ISO 639-1 codes. (Default: "en")  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/calls
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "agent@somedomain.com",
        "outbound_number": "+1 760-867-5309",
        "end_user_number": "123123",
        "lang": "en"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Error : Agent is not available to take this call

This example demonstrates the failure scenario when the agent is not available to receive the call.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "agent@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Agent is not available to take this call
    
    
    {
        "message": "Agent is not available to take this call"
    }
    

**_Status Code:_** 400

#### Create an outbound call with end-user number

This example demonstrates how to make an outbound call for a specific end-user number.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 859-657-9625",
        "outbound_number": "+1 339-219-5276",
        "lang": "en"
    }
    

##### Response: Create an outbound call with end_user_number
    
    
    {
        "id": 397,
        "lang": "en",
        "call_type": "Voice Outbound (API)",
        "status": "assigned",
        "created_at": "2019-06-07T01:27:30.406Z",
        "queued_at": null,
        "assigned_at": "2019-06-07T01:27:30.441Z",
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
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
        "support_number": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
            "id": 1,
            "agent_number": null,
            "name": "Admin UJET",
            "last_name": "UJET",
            "first_name": "Admin",
            "avatar_url": "https://somedomain.com/avatar.jpg"
        },
        "end_user": null,
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 610,
                "type": "agent",
                "status": "waiting",
                "call_id": 397,
                "user_id": 1,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 611,
                "type": "end_user",
                "status": "waiting",
                "call_id": 397,
                "user_id": null,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Create an outbound call with ticket ID

This example demonstrates the creation of an outbound call with a specific ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "agent@somedomain.com",
        "ticket_id": "71450",
        "outbound_number": "+1 339-219-5276",
        "lang": "en"
    }
    

##### Response: Create an outbound call with ticket_id
    
    
    {
        "id": 398,
        "lang": "en",
        "call_type": "Voice Outbound (API)",
        "status": "assigned",
        "created_at": "2019-06-07T01:28:47.955Z",
        "queued_at": null,
        "assigned_at": "2019-06-07T01:28:47.971Z",
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
        "voip_provider": "voip_provider_twilio",
        "out_ticket_id": "71450",
        "out_ticket_url": null,
        "verified": false,
        "recording_url": null,
        "recording_permission": "not_asked",
        "voicemail_reason": "not_voicemail",
        "deflection": "no_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": "nothing",
        "fail_details": null,
        "support_number": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
            "id": 1,
            "agent_number": null,
            "name": "Admin UJET",
            "last_name": "UJET",
            "first_name": "Admin",
            "avatar_url": "https://somedomain.com/avatar.png"
        },
        "end_user": {
            "id": 67,
            "identifier": null,
            "out_contact_id": "381630957514"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 612,
                "type": "agent",
                "status": "waiting",
                "call_id": 398,
                "user_id": 1,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 613,
                "type": "end_user",
                "status": "waiting",
                "call_id": 398,
                "user_id": null,
                "end_user_id": 67,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Error : ticket ID or end-user number required

This example demonstrates the failure case where the ticket ID or end-user number are required but not provided.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

#### Response: Error : ticket_id or end_user_number required
    
    
    {
        "message": "ticket_id or end_user_number required"
    }
    

**_Status Code:_** 400

#### Error : Not a valid agent email

This example demonstrates the failure when the provided email address for an agent is not valid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

#### Response: Error : Not a valid agent email
    
    
    {
        "message": "Not a valid agent email"
    }
    

**_Status Code:_** 400

#### Error : Agent email required

This example demonstrates the failure when an email address is not provided for the agent.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

#### Response: Error : Agent email required
    
    
    {
        "message": "Agent email required"
    }
    

**_Status Code:_** 400

#### Error : Agent does not have access to make calls

This example demonstrates the failure when the specified agent is not permitted to be able to make outgoing calls.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Agent does not have access to make calls
    
    
    {
        "message": "Agent does not have access to make calls"
    }
    

**_Status Code:_** 400

#### Error : end_user_number is not well-formed

This example demonstrates the failure scenario where the provided end-user number is not correctly formatted.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response: Error : end_user_number is not well-formed
    
    
    {
        "message": "end_user_number is not well-formed"
    }
    

**_Status Code:_** 400

#### Error : Contact not found

This example demonstrates the failure scenario where the provided contact does not exist.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "ticket_id": 1,
        "lang": "en"
    }
    

##### Response: Error : Contact not found
    
    
    {
        "message": "Contact not found"
    }
    

**_Status Code:_** 400

#### Accepted : Need to choose an outbound number

In this example, the outbound call is accepted but the agent must choose the outbound number to use before the call is placed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "agent@somedomain.com",
        "outbound_number": "+1 760-867-5309",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

**_Status Code:_** 200

#### Error : Invalid call type

This example demonstrates the failure scenario where the call type provided is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response: Error : Invalid call type
    
    
    {
        "message": "Invalid call type"
    }
    

**_Status Code:_** 400

#### Prompt the call adapter by multiple outbound numbers

In this scenario the call adapter is prompted with multiple outbound numbers.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "agent@somedomain.com",
        "outbound_number": "+1 760-867-5309",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 859-657-9625",
        "lang": "en"
    }
    

**_Status Code:_** 200

#### Accepted : Agent must make an outbound call with ticket ID

This example demonstrates a request where the agent must make an outbound call based on the provided ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

**_Status Code:_** 202

## Outbound Call - ticket_id

Parameter | Required | Data Type | Definition  
---|---|---|---  
call_type | TRUE | String | Call type to create. "Voice Outbound (API)", "OutboundCall" (deprecated) are available for now  
agent_email | TRUE | String | Email address for the agent who will be assigned to the outbound call.  
ticket_id | FALSE | String | CRM ticket ID and it will dial to the end user who is tied to the ticket.  
end_user_number | FALSE | String | End user phone number which will be dialing. ticket_id has a higher priority than end_user_number.  
outbound_number | FALSE | String | Well-formed outbound number which is managed from Settings > Phone Numbers > Phone Number Management. Default outbound number will be used when empty  
lang | FALSE | String | Language of the call. Uses ISO 639-1 codes. (Default: "en")  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}​/apps/api/v1/calls
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-867-5309",
        "ticket_id": "123123",
        "lang": "en"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Error : ticket ID or end-user number required

In this example the failure scenario of the ticket ID or end-user number are missing but required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

#### Response: Error : ticket_id or end_user_number required
    
    
    {
        "message": "ticket_id or end_user_number required"
    }
    

**_Status Code:_** 400

#### Error : Agent email required

In this example we show the failure scenario where the agent email is not provided but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Agent email required
    
    
    {
        "message": "Agent email required"
    }
    

**_Status Code:_** 400

#### Create an outbound call with end-user number

In this example we show how to create an outbound call by providing the end-user number.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 859-657-9625",
        "outbound_number": "+1 339-219-5276",
        "lang": "en"
    }
    

##### Response: Create an outbound call with end_user_number
    
    
    {
        "id": 397,
        "lang": "en",
        "call_type": "Voice Outbound (API)",
        "status": "assigned",
        "created_at": "2019-06-07T01:27:30.406Z",
        "queued_at": null,
        "assigned_at": "2019-06-07T01:27:30.441Z",
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
        "voip_provider": "voip_provider_twilio",
        "out_ticket_id": null,
        "out_ticket_url": null,
        "verified": false,
        "recording_url": null,
        "recording_permission": "not_asked",
        "voicemail_reaso": "not_voicemail",
        "deflection": "n_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": "nothing",
        "fail_details": null,
        "support_number": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
            "id": 1,
            "agent_number": null,
            "name": "Admin UJET",
            "last_name": "UJET",
            "first_name": "Admin",
            "avatar_url": "https://somedomain.com/default-profile.png"
        },
        "end_user": null,
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 610,
                "type": "agent",
                "status": "waiting",
                "call_id": 397,
                "user_id": 1,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 611,
                "type": "end_user",
                "status": "waiting",
                "call_id": 397,
                "user_id": null,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Error : Invalid call type

In this example we show the failure scenario where the call type provided is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "ScheduledCall",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response: Error : Invalid call type
    
    
    {
        "message": "Invalid call type"
    }
    

**_Status Code:_** 400

#### Prompt the call adapter by multiple outbound numbers

In this example we show how to prompt the call adapter with multiple outbound phone numbers.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 859-657-9625",
        "lang": "en"
    }
    

**_Status Code:_** 202

#### Accepted : Agent must make an outbound call with ticket ID

In this example we show how to make an outbound call with a ticket ID and the agent accepts the request.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
***Body:*** ```json { "call_type": "Voice Outbound (API)", "agent_email": "allen@somedomain.com", "end_user_number": "+1 205-123-4567", "lang": "en" } ``` ***Status Code:*** 202 #### Error : Agent does not have access to make calls In this example we show the failure scenario where a call creation request is submitted but the agent does not have access to be able to make outbound calls. ##### Request ***Headers:*** Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Agent does not have access to make calls
    
    
    {
        "message": "Agent does not have access to make calls"
    }
    

**_Status Code:_** 400

#### Create an outbound call with ticket ID.

In this example we show the scenario of creating an outbound call with a ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "ticket_id": "71450",
        "outbound_number": "+1 339-219-5276",
        "lang": "en"
    }
    

##### Response: Create an outbound call with ticket_id
    
    
    {
        "id": 398,
        "lang": "en",
        "call_type": "Voice Outbound (API)",
        "status": "assigned",
        "created_at": "2019-06-07T01:28:47.955Z",
        "queued_at": null,
        "assigned_at": "2019-06-07T01:28:47.971Z",
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
        "voip_provider": "voip_provider_twilio",
        "out_ticket_id": "71450",
        "out_ticket_url": null,
        "verified": false,
        "recording_url": null,
        "recording_permission": "not_asked",
        "voicemail_reason": "not_voicemail",
        "deflection": "no_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": "nothing",
        "fail_details": null,
        "support_number": null,
        "selected_menu": null,
        "menu_path": null,
        "agent_info": {
            "id": 1,
            "agent_number": null,
            "name": "Admin UJET",
            "last_name": "UJET",
            "first_name": "Admin",
            "avatar_url": "https://somedomain.com/default-profile.png"
        },
        "end_user": {
            "id": 67,
            "identifier": null,
            "out_contact_id": "381630957514"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 612,
                "type": "agent",
                "status": "waiting",
                "call_id": 398,
                "user_id": 1,
                "end_user_id": null,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            },
            {
                "id": 613,
                "type": "end_user",
                "status": "waiting",
                "call_id": 398,
                "user_id": null,
                "end_user_id": 67,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": null,
        "offer_events": [],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Accepted : Need to choose an outbound number

In this example we show the scenario where an outbound call request is created with the need to choose an outbound number and then is accepted.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

**_Status Code:_** 202

#### Error : Agent is not available to take this call

In this example we show the failure scenario where a call is created but the agent is not available to accept the call.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Agent is not available to take this call
    
    
    {
        "message": "Agent is not available to take this call"
    }
    

**_Status Code:_** 400

#### Error : end-user number is not well-formed

In this example we show the failure scenario where the provided end-user phone number is incorrectly formed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "end_user_number": "123123",
        "lang": "en"
    }
    

##### Response: Error : end_user_number is not well-formed
    
    
    {
        "message": "end_user_number is not well-formed"
    }
    

**_Status Code:_** 400

##### Error : Not a valid agent email

In this example we show the failure scenario where the provided agent email is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "admin@somedomain.com",
        "end_user_number": "+1 205-123-4567",
        "lang": "en"
    }
    

##### Response: Error : Not a valid agent email
    
    
    {
        "message": "Not a valid agent email"
    }
    

**_Status Code:_** 400

#### Error : Contact not found

In this example we show the failure scenario where the provided contact couldn't be located.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Outbound (API)",
        "agent_email": "allen@somedomain.com",
        "outbound_number": "+1 760-410-8538",
        "ticket_id": 1,
        "lang": "en"
    }
    

##### Response: Error : Contact not found
    
    
    {
        "message": "Contact not found"
    }
    

**_Status Code:_** 400

## Incoming Call

Parameter | Required | Data Type | Definition  
---|---|---|---  
call_type | TRUE | String | Call type to create. Use "Voice Inbound (API)" or "IncomingCall" (deprecated) to create an incoming call.  
menu_id | TRUE | Integer | The ID of the menu to attribute the call to. Only IVR and Web menu IDs are accepted.  
end_user_number | TRUE | String | The end user phone number that will be dialed. If both a ticket_id and end_user_number are passed in, the ticket_id will take precedence.  
lang | FALSE | String | Language of the call. Uses ISO 639-1 codes. (Default: "en")  
ticket_id | FALSE | String | CRM ticket ID. The end user phone number tied to the ticket will be dialed. If both a ticket_id and end_user_number are passed in, the ticket_id will take precedence.  
outbound_number | FALSE | String | The outbound phone number to be used for the call. The default global outbound phone number will be used if input is not passed in or invalid. Outbound numbers are managed from Settings > Queue > EDIT / VIEW > Select a queue > Outbound Phone Numbers.  
recording_permission | FALSE | String | The value is only evaluated if the "Call Recording Options" feature is set to "Ask User for Permission to Record". Configurable at Settings > Queue > EDIT / VIEW > Select a queue > Call Recording Options. If the value is either "recording_permission_not_asked" (default) or "recording_permission_denied", the call won't be recorded. If the value is "recording_permission_granted", the call will be recorded.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/calls
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "ticket_id": "76517",
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Error : end-user number is not well formed

In this example we show the failure scenario where an incoming call is created but that the provided end-user number is incorrectly formed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 999-657-12",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : end_user_number is not well formed
    
    
    {
        "message": "end_user_number is not well formed"
    }
    

**_Status Code:_** 400

#### Error : Menu is in 'manual redirection' state, can't accept calls

In this example we show the failure scenario where a call is routed to a menu ID but that the menu is in manual redirection state and as such cannot receive incoming calls.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Menu is in 'manual redirection' state, can't accept calls
    
    
    {
        "message": "Menu is in 'manual redirection' state, can't accept calls"
    }
    

**_Status Code:_** 400

#### Error : Invalid call type

In this example we show the failure scenario where an incoming call is created but the provided call type is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "InvalidCallType",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Invalid call type
    
    
    {
        "message": "Invalid call type"
    }
    

**_Status Code:_** 400

#### Error : menu ID is required

In this example we show the failure scenario where an incoming call is created but the provided menu ID is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu_id is required
    
    
    {
        "message": "menu_id is required"
    }
    

**_Status Code:_** 400

#### Error : Only IVR and mobile menu IDs are permitted

In this example we show the failure scenario where an incoming call is created but the provided menu ID is not an IVR or mobile menu ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 50,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Only IVR and mobile menu IDs are permitted
    
    
    {
        "message": "Only IVR and mobile menu IDs are permitted"
    }
    

**_Status Code:_** 400

#### Create an incoming call with end-user number

This example demonstrates how to create an incoming call with a specific end-user number.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+82-10-6861-2345",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Create an incoming call with end_user_number
    
    
    {
        "id": 515,
        "lang": "en",
        "call_type": "Voice Inbound (API)",
        "status": "queued",
        "created_at": "2019-09-10T00:19:14.000Z",
        "queued_at": "2019-09-10T00:19:14.421Z",
        "assigned_at": null,
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
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
        "support_number": null,
        "selected_menu": {
            "id": 9,
            "name": "Lock Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You selected Lock Star.",
            "hidden": false
        },
        "menu_path": {
            "items_count": 1,
            "name": "Lock Star",
            "materialized_path": "9"
        },
        "agent_info": null,
        "end_user": {
            "id": 75,
            "identifier": null,
            "out_contact_id": "389391400633"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 820,
                "type": "end_user",
                "status": "waiting",
                "call_id": 515,
                "user_id": null,
                "end_user_id": 75,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": "cascade",
        "offer_events": [
            {
                "casting_time": "2019-09-10T00:19:14.000Z",
                "group": "Group 1"
            }
        ],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Error : Menu is in 'after hours' state, can't accept incoming calls

This example demonstrates the failure when the provided menu ID is in after hours state.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Menu is in 'after hours' state, can't accept incoming calls
    
    
    {
        "message": "Menu is in 'after hours' state, can't accept incoming calls"
    }
    

**_Status Code:_** 400

#### Error : Language is not available

This example demonstrates the failure request when the specified language is not available.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "fr",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Language is not available
    
    
    {
        "message": "Language 'fr' is not available"
    }
    

**_Status Code:_** 400

#### Create an incoming call with ticket ID

This example demonstrates the request to create an incoming call with an associated ticket ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "ticket_id": "76517",
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Create an incoming call with ticket_id
    
    
    {
        "id": 519,
        "lang": "en",
        "call_type": "Voice Inbound (API)",
        "status": "queued",
        "created_at": "2019-09-10T05:12:26.000Z",
        "queued_at": "2019-09-10T05:12:26.295Z",
        "assigned_at": null,
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": null,
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
        "out_ticket_id": "76517",
        "out_ticket_url": null,
        "verified": false,
        "recording_url": null,
        "recording_permission": "not_asked",
        "voicemail_reason": "not_voicemail",
        "deflection": "no_deflection",
        "disconnected_by": "disconnected_by_unknown",
        "fail_reason": "nothing",
        "fail_details": null,
        "support_number": null,
        "selected_menu": {
            "id": 9,
            "name": "Lock Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You selected Lock Star.",
            "hidden": false
        },
        "menu_path": {
            "items_count": 1,
            "name": "Lock Star",
            "materialized_path": "9"
        },
        "agent_info": null,
        "end_user": {
            "id": 75,
            "identifier": null,
            "out_contact_id": "389391400633"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 826,
                "type": "end_user",
                "status": "waiting",
                "call_id": 519,
                "user_id": null,
                "end_user_id": 75,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": "cascade",
        "offer_events": [
            {
                "casting_time": "2019-09-10T05:12:26.000Z",
                "group": "Group 1"
            }
        ],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

##### Error : Language is not found

This example demonstrates the failure when the provided language is not found.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "xy",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Language is not found
    
    
    {
        "message": "Language 'xy' is not found"
    }
    

**_Status Code:_** 400

#### Error : menu_id is not found

This example demonstrates the failure when the provided menu ID is not found.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9999,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu_id is not found
    
    
    {
        "message": "menu_id 9999 is not found"
    }
    

**_Status Code:_** 400

#### Error : menu_id is not well formed

This example demonstrates the failure when the provided menu ID is not correct.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": "menu_999",
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu_id is not well formed
    
    
    {
        "message": "menu_id is not well formed"
    }
    

**_Status Code:_** 400

#### Error : end-user number is required

In this example we show the failure scenario where an incoming call is created but the end-user phone number was not provided.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Inbound (API)",
        "lang": "en",
        "menu_id": 9,
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : end_user_number is required
    
    
    {
        "message": "end_user_number is required"
    }
    

**_Status Code:_** 400

## Scheduled call

Parameter | Required | Data Type | Definition  
---|---|---|---  
call_type | TRUE | String | Call type to create. Use "Voice Scheduled (API)" or "ScheduledCall" (deprecated) to create an scheduled call.  
menu_id | TRUE | Integer | The ID of the menu to attribute the call to. Only Mobile and Web menu IDs are accepted.  
call_id | FALSE | Integer | Call ID of previous call, which will be linked as the parent call of the new created scheduled call. When call ID is being used, menu_id can be optional.  
end_user_number | TRUE | String | The end user phone number that will be dialed. If both a ticket_id and end_user_number are passed in, the ticket_id will take precedence.  
lang | FALSE | String | Language of the call. Uses ISO 639-1 codes. (Default: "en")  
ticket_id | FALSE | String | CRM ticket ID. The end user phone number tied to the ticket will be dialed. If both a ticket_id and end_user_number are passed in, the ticket_id will take precedence.  
scheduled_at | TRUE | String | Scheduled time of the call. Uses ISO 8601 format to a valid future time.  
recording_permission | FALSE | String | The value is only evaluated if the "Call Recording Options" feature is set to "Ask User for Permission to Record". Configurable at Settings > Queue > EDIT / VIEW > Select a queue > Call Recording Options. If the value is either "recording_permission_not_asked" (default) or "recording_permission_denied", the call won't be recorded. If the value is "recording_permission_granted", the call will be recorded.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/calls
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "ticket_id": "76517",
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Error : end_user_number is not well formed

This example demonstrates the failure due to the end_user_namber not being correctly formatted.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 999-657-12",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : end_user_number is not well formed
    
    
    {
        "message": "end_user_number is not well formed"
    }
    

**_Status Code:_** 400

#### Error : Menu is in 'manual redirection' state, can't accept calls

This example demonstrates the failure when the specified menu ID is set to menu redirection and is unable to accept calls.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Menu is in 'manual redirection' state, can't accept calls
    
    
    {
        "message": "Menu is in 'manual redirection' state, can't accept calls"
    }
    

**_Status Code:_** 400

#### Error : Invalid call type

This example demonstrates the failure when a request is made and the call type is invalid. 

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "InvalidCallType",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Invalid call type
    
    
    {
        "message": "Invalid call type"
    }
    

**_Status Code:_** 400

#### Error : menu_id is required

This example demonstrates the request and response when a menu ID is not provided but is required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu_id is required
    
    
    {
        "message": "menu_id is required"
    }
    

**_Status Code:_** 400

#### Error : Only mobile and web menu IDs are permitted

This example demonstrates a request that fails when a menu ID is provided that is not a web or mobile menu ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 50,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Only mobile and web menu IDs are permitted
    
    
    {
        "message": "Only mobile and web menu IDs are permitted"
    }
    

**_Status Code:_** 400

#### Create a scheduled call with menu ID

This example demonstrates how to create a scheduled call with a specific menu ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+82-10-6861-2345",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Create an scheduled call with menu ID
    
    
    {
        "id": 515,
        "lang": "en",
        "call_type": "Voice Inbound (API)",
        "status": "queued",
        "created_at": "2019-09-10T00:19:14.000Z",
        "queued_at": null,
        "assigned_at": null,
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
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
        "support_number": null,
        "selected_menu": {
            "id": 9,
            "name": "Lock Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You selected Lock Star.",
            "hidden": false
        },
        "menu_path": {
            "items_count": 1,
            "name": "Lock Star",
            "materialized_path": "9"
        },
        "agent_info": null,
        "end_user": {
            "id": 75,
            "identifier": null,
            "out_contact_id": "389391400633"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 820,
                "type": "end_user",
                "status": "waiting",
                "call_id": 515,
                "user_id": null,
                "end_user_id": 75,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": "cascade",
        "offer_events": [
            {
                "casting_time": "2019-09-10T00:19:14.000Z",
                "group": "Group 1"
            }
        ],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Create a scheduled call with call ID

This example demonstrates how to create a scheduled call with a specific call ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "call_id": 514,
        "end_user_number": "+82-10-6861-2345",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Create an scheduled call with call ID
    
    
    {
        "id": 515,
        "lang": "en",
        "call_type": "Voice Inbound (API)",
        "status": "queued",
        "created_at": "2019-09-10T00:19:14.000Z",
        "queued_at": null,
        "assigned_at": null,
        "connected_at": null,
        "ends_at": null,
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "wait_duration": 0,
        "call_duration": 0,
        "hold_duration": 0,
        "rating": null,
        "has_feedback": false,
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
        "support_number": null,
        "selected_menu": {
            "id": 9,
            "name": "Lock Star",
            "parent_id": null,
            "position": 0,
            "deleted": false,
            "menu_type": "ivr_menu",
            "output_msg": "You selected Lock Star.",
            "hidden": false
        },
        "menu_path": {
            "items_count": 1,
            "name": "Lock Star",
            "materialized_path": "9"
        },
        "agent_info": null,
        "end_user": {
            "id": 75,
            "identifier": null,
            "out_contact_id": "389391400633"
        },
        "photos": [],
        "videos": [],
        "transfers": [],
        "deflection_details": [],
        "participants": [
            {
                "id": 820,
                "type": "end_user",
                "status": "waiting",
                "call_id": 515,
                "user_id": null,
                "end_user_id": 75,
                "call_duration": null,
                "hold_duration": null,
                "connected_at": null,
                "ended_at": null,
                "fail_reason": "nothing"
            }
        ],
        "offer_type": "cascade",
        "offer_events": [
            {
                "casting_time": "2019-09-10T00:19:14.000Z",
                "group": "Group 1"
            }
        ],
        "answer_type": "manual",
        "outbound_number": "+1 339-219-5276"
    }
    

**_Status Code:_** 201

#### Error : Menu is in 'after hours' state, can't accept incoming calls

In this example we show the failure scenario where a scheduled call is created but that the provided menu is out of hours and as such cannot receive incoming calls.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Menu is in 'after hours' state, can't accept incoming calls
    
    
    {
        "message": "Menu is in 'after hours' state, can't accept incoming calls"
    }
    

**_Status Code:_** 400

#### Error : Language is not available

This example demonstrates the failure when the specified language is invalid.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "fr",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Language is not available
    
    
    {
        "message": "Language 'fr' is not available"
    }
    

**_Status Code:_** 400

#### Error : Language is not found

In this example we show the failure scenario where a scheduled call is created but that the language is invalid or not available.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "xy",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : Language is not found
    
    
    {
        "message": "Language 'xy' is not found"
    }
    

**_Status Code:_** 400

#### Error : menu ID is not found

In this example we show the failure scenario where a scheduled call is created but that the provided menu ID is invalid and not found.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9999,
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu ID is not found
    
    
    {
        "message": "menu_id 9999 is not found"
    }
    

**_Status Code:_** 400

#### Error : menu ID is not well formed

In this example we show the failure scenario where a scheduled call is created but that the provided menu ID is incorrectly formed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": "menu_999",
        "end_user_number": "+1 859-657-9625",
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : menu_id is not well formed
    
    
    {
        "message": "menu_id is not well formed"
    }
    

**_Status Code:_** 400

#### Error : end-user number is required

In this example we show the failure scenario where a scheduled call is created but that the end-user number was not provided.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "scheduled_at": "2019-09-15T00:19:14.421Z",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : end_user_number is required
    
    
    {
        "message": "end_user_number is required"
    }
    

**_Status Code:_** 400

#### Error : scheduled_at is required

In this example we show the failure scenario where a scheduled call is created but that scheduled at value is missing but required.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_type": "Voice Scheduled (API)",
        "lang": "en",
        "menu_id": 9,
        "end_user_number": "+1 859-657-9625",
        "recording_permission": "recording_permission_granted"
    }
    

##### Response: Error : scheduled_at is required
    
    
    {
        "message": "scheduled_at is required"
    }
    

**_Status Code:_** 400

## Get reserved data attributes during a call

**Endpoint**
    
    
    Method: GET
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/calls/:id/customer_flag
    

### Example request and responses

This section contains an example request and response for the endpoint.

#### Success

This example shows a successful call.

##### Request

**URL variables**

Key | Value | Description  
---|---|---  
id | integer | (Required)  
  
##### Response
    
    
    {
        "verified_customer": "boolean",
        "bad_actor": "boolean",
        "repeat_customer": "boolean"
    }
    

**Status code** 0

## Update reserved data attributes during a call

**Endpoint**
    
    
    Method: PATCH
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/calls/:id/customer_flag
    

**URL variables**

Key | Value | Description  
---|---|---  
id | integer | (Required)  
  
**Body**
    
    
    {
        "verified_customer": "boolean",
        "bad_actor": "boolean",
        "repeat_customers": "boolean"
    }
    

## Pass data parameters to virtual agents mid-session

To use the apps API to pass data parameters to virtual agents in the middle of a call session, see [Pass data parameters to virtual agents mid-session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#virtual-agent-custom-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
