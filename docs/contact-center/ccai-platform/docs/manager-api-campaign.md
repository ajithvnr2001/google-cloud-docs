---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-campaign/
title: Campaign endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:33.697747+00:00
---

# Campaign endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api-campaign/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Campaign endpoints Stay organized with collections  Save and categorize content based on your preferences. 

A campaign refers to an outbound auto-dialer feature that sequentially reaches out to a list of contacts, initiates outbound calls, and connects each contact to an available agent. Campaign endpoints provide access to campaign-related data, allowing retrieval of campaign and contact objects.

  * **Campaign object** : represents a single campaign within the platform

  * **Contact object** : represents individual campaign contacts within a specific campaign




See to the following model to determine which fields might contain PII:
    
    
    [
       {
          "campaign_type" : "default",
          "id" : 67,
          "external_campaign_id" : null,
          "max_abandonment_percent" : 3,
          "max_redial_count" : 3,
          "mode" : "preview",
          "name" : "string",
          "overdial_adjustment_multiplier" : 1,
          "queue" : {
             "deleted" : false,
             "hidden" : false,
             "id" : 60,
             "menu_type" : "ivr_menu",
             "name" : "string",
             "output_msg" : null,
             "parent_id" : 59,
             "position" : 4
          },
          "redial_interval_minutes" : 120,
          "status" : "dialing",
          "target_number_to_process" : 1000,
          "created_at" : "2023-04-01T23:23:43.000Z",
          "starts_at" : "2023-04-01T23:28:08.000Z",
          "ends_at" : null,
          "updated_at" : "2023-04-01T23:28:08.000Z",
          "contact_stats" : {
             "Abandoned by Contact" : 0,
             "Abandoned by Dialer" : 0,
             "Average Redials per Number" : 0,
             "Carrier Error" : 0,
             "Completed" : 50,
             "Connected" : 0,
             "Contacts" : 1000,
             "Dialer General Error" : 0,
             "Dialing" : 0,
             "Do Not Call" : 0,
             "Finished" : 40,
             "Invalid Number or Name" : 0,
             "Invalid outbound number" : 0,
             "Not Picked Up" : 0,
             "Not Reached to Contact" : 0,
             "Not reached" : 10,
             "Not yet reached" : 960,
             "Queued" : 0,
             "Reached" : 0,
             "Redial Scheduled" : 0,
             "Redials" : 0,
             "Remaining" : 950,
             "Running" : 0,
             "Skipped" : 0,
             "Skipped & Closed" : 10,
             "Transferred" : 0,
             "Transferred and Finished" : 0,
             "Upcoming" : 950,
             "Voicemail Hung Up" : 0
          }
       }
    ]
    

## Campaign status field

The `status` field can be in any of the following states:

Campaign Status | Description  
---|---  
created | A campaign is created but has not started doing outbound calls.  
started | A campaign has started doing outbound calls has not started dialing (conversation).  
dialing | A campaign is dialing outbound calls.  
pause | A campaign has been paused by an agent or manager.  
finished | A campaign has completed all of its calls.  
  
## Campaign mode field

The `mode` field can be in any of the following values:

Campaign Mode | Description  
---|---  
preview | For a preview campaign, an agent connects to an end-user or chooses what action to take for a given contact. In a preview campaign, the contact or end-user is known.  
predictive | For a predictive campaign, an agent is connected to a reservation call. We turn on machine detection for that call, which tells us whether the response to an outbound call is from a human or a machine (for example, a voicemail), only connecting the agent to a human.  
progressive | For Progressive Campaign, the dialer would first connect to the first available agent. Upon connection, the dialer would call and deliver the first available (a contact that has not been called yet for a given campaign) contact to the agent.  
  
## Campaign type field

The `campaign_type` field can be any of the following values:

Campaign Type | Description  
---|---  
default | Campaign contacts are from user-uploaded CSV files.  
external_list | Campaign contacts are from external or third-party services.  
  
## Campaign list

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/outbound_dialer/campaigns
    

**_More example Requests/Responses:_**

### Example request: Campaign list

**_Query: None_**

**_Body: None_**

### Example response: Campaign list
    
    
    [
        {
            "campaign_type": "default",
            "id": 67,
            "external_campaign_id": null,
            "max_abandonment_percent": 3,
            "max_redial_count": 3,
            "mode": "preview",
            "name": "string",
            "overdial_adjustment_multiplier": 1,
            "queue": {
                "deleted": false,
                "hidden": false,
                "id": 60,
                "menu_type": "ivr_menu",
                "name": "string",
                "output_msg": null,
                "parent_id": 59,
                "position": 4
            },
            "redial_interval_minutes": 120,
            "status": "dialing",
            "target_number_to_process": 1000,
            "created_at": "2023-04-01T23:23:43.000Z",
            "starts_at": "2023-04-01T23:28:08.000Z",
            "ends_at": null,
            "updated_at": "2023-04-01T23:28:08.000Z",
            "contact_stats": {
                "Abandoned by Contact": 0,
                "Abandoned by Dialer": 0,
                "Average Redials per Number": 0,
                "Carrier Error": 0,
                "Completed": 50,
                "Connected": 0,
                "Contacts": 1000,
                "Dialer General Error": 0,
                "Dialing": 0,
                "Do Not Call": 0,
                "Finished": 40,
                "Invalid Number or Name": 0,
                "Invalid outbound number": 0,
                "Not Picked Up": 0,
                "Not Reached to Contact": 0,
                "Not reached": 10,
                "Not yet reached": 960,
                "Queued": 0,
                "Reached": 0,
                "Redial Scheduled": 0,
                "Redials": 0,
                "Remaining": 950,
                "Running": 0,
                "Skipped": 0,
                "Skipped &amp; Closed": 10,
                "Transferred": 0,
                "Transferred and Finished": 0,
                "Upcoming": 950,
                "Voicemail Hung Up": 0
            }
        }
    ]
    

**_Status Code:_** 200

## Single campaign

**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/outbound_dialer/campaigns/\{campaign_id\}
    

**_More example Requests/Responses:_**

### Example request: Single campaign

**_Query:_**

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The ID of the campaign that you want to retrieve  
  
**_Body: None_**

### Example response: Single campaign
    
    
    {
        "campaign_type": "default",
        "id": 67,
        "external_campaign_id": null,
        "max_abandonment_percent": 3,
        "max_redial_count": 3,
        "mode": "preview",
        "name": "string",
        "overdial_adjustment_multiplier": 1,
        "queue": {
            "deleted": false,
            "hidden": false,
            "id": 60,
            "menu_type": "ivr_menu",
            "name": "string",
            "output_msg": null,
            "parent_id": 59,
            "position": 4
        },
        "redial_interval_minutes": 120,
        "status": "dialing",
        "target_number_to_process": 1000,
        "created_at": "2023-04-01T23:23:43.000Z",
        "starts_at": "2023-04-01T23:28:08.000Z",
        "ends_at": null,
        "updated_at": "2023-04-01T23:28:08.000Z",
        "contact_stats": {
            "Abandoned by Contact": 0,
            "Abandoned by Dialer": 0,
            "Average Redials per Number": 0,
            "Carrier Error": 0,
            "Completed": 50,
            "Connected": 0,
            "Contacts": 1000,
            "Dialer General Error": 0,
            "Dialing": 0,
            "Do Not Call": 0,
            "Finished": 40,
            "Invalid Number or Name": 0,
            "Invalid outbound number": 0,
            "Not Picked Up": 0,
            "Not Reached to Contact": 0,
            "Not reached": 10,
            "Not yet reached": 960,
            "Queued": 0,
            "Reached": 0,
            "Redial Scheduled": 0,
            "Redials": 0,
            "Remaining": 950,
            "Running": 0,
            "Skipped": 0,
            "Skipped &amp; Closed": 10,
            "Transferred": 0,
            "Transferred and Finished": 0,
            "Upcoming": 950,
            "Voicemail Hung Up": 0
        }
    }
    

**_Status Code:_** 200

## Contact list

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The ID of the campaign that you want to get the contacts for  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: https://{​{subdomain}​}.{​{domain}​}/manager/api/v1/outbound_dialer/campaigns/\{campaign_id\}/contacts
    

**_More example Requests/Responses:_**

### Example request: Contact list

**_Query:_**

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The ID of the campaign that you want to get the contacts for  
  
**_Body: None_**

### Example response: Contact list
    
    
    [
        {
            "assigned_call_id": 32001,
            "assigned_participant_id": 54321,
            "campaign_id": 240,
            "created_at": "2023-04-01T17:15:38.000Z",
            "id": 16312,
            "name": "string",
            "outbound_number": null,
            "priority": null,
            "status": "Upcoming",
            "unique_id": "string",
            "updated_at": "2023-04-01T17:15:38.000Z"
        },
        {
            "assigned_call_id": 32002,
            "assigned_participant_id": 54330,
            "campaign_id": 240,
            "created_at": "2023-04-01T17:15:38.000Z",
            "id": 16313,
            "name": "string",
            "outbound_number": null,
            "priority": null,
            "status": "Upcoming",
            "unique_id": "string",
            "updated_at": "2023-04-01T17:15:38.000Z"
        }
    ]
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
