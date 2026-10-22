---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-campaign/
title: Campaign endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:50.525860+00:00
---

# Campaign endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-campaign/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Campaign endpoints Stay organized with collections  Save and categorize content based on your preferences. 

A campaign refers to an outbound auto-dialer feature that sequentially reaches out to a list of contacts, initiates outbound calls, and connects each contact to an available agent. Campaign endpoints provide access to campaign-related data, allowing retrieval of campaign and contact objects.

  * **Campaign** object represents a single campaign within the platform.

  * **Contact** object represents an individual campaign contact within a specific campaign.




Campaign endpoints let users to add, update, and delete contacts of an existing campaign. The available endpoints include:

  * Add a single contact to a campaign

  * Get contacts for a campaign

  * Import multiple contacts to a campaign

  * Jobs

  * Update single contact

  * Remove single contact




## Campaign contact status

The status field can be in any of the following states:

Campaign Contact Status | Description  
---|---  
Upcoming | Contact is next to be dialed.  
Dialing | Contact is right now being dialed.  
Queued | Call for a given contact is queued.  
Connected | Contact is connected with an agent.  
Finished | Call has completed.  
Transferred | Call has been transferred.  
Transferred and Finished | Call has been transferred and then completed.  
Not Picked Up | No answer from end user or never reached the end user.  
Not Reached to Contact | Call never reached the contact.  
Abandoned by Contact | For preview, end user hangs up before connected to an agent. For both progressive and predictive, end user hangs up the call within 5 seconds after connecting to the agent.  
Skipped | Contact has been skipped by agent and will be available to be connected to another agent.  
Skipped & Closed | On Preview, agent skips and close a contact. This contact should now be always skipped in this campaign.  
Invalid Number | Contact with invalid phone number.  
Carrier Error | This error is driven by carrier.  
Abandoned by Dialer | Contact has been abandoned by dialer.  
Voicemail Hung Up | On Predictive, the dialer determines the end user is a machine (ie. voicemail).  
Dialer General Error | Call failed due to dialer error.  
Redial Scheduled | Temporary status. Redial scheduled in the future.  
Do Not Call | The number was in Do-Not-Call number list.  
Invalid Outbound Number | Contact with invalid outbound number.  
Blocked Phone Number | Contact with invalid/blocked international number.  
  
## Add a single contact to a campaign

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The ID of the campaign to add a contact to.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.​{domain}​/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contacts
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "name": "string",
        "email": "customer@somedomain.com",
        "phone_number": "+1 111-111-1111",
        "outbound_number": "+1 760-867-5309",
        "external_unique_id": "UID_123456"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Add single contact to a campaign

This example demonstrates how to add a contact to a specific campaign ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | integer | The ID of the campaign to add the contact to  
  
**_Body:_**
    
    
    {
        "name": "string",
        "email": "customer@somedomain.com",
        "phone_number": "+1 111-111-1111",
        "outbound_number": "+1 760-867-5309",
        "external_unique_id": "UID_123456"
    }
    

##### Response
    
    
    {
        "valid_contacts": [
            {
                "name": "string",
                "email": "customer@somedomain.com",
                "phone_number": "+1 111-111-1111",
                "outbound_number": "+1 760-867-5309",
                "external_unique_id": "UID_123456"
            }
        ],
        "invalid_contacts": []
    }
    

**_Status Code:_** 200

## Get contacts for a campaign

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The ID of the campaign to retrieve the contacts from.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{subdomain}.​{domain}​/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contacts
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | integer | The ID of the campaign to add the contact to  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Get contacts for a campaign

The following example demonstrates how to retrieve the contacts for the given campaign ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | integer | Campaign ID of the campaign to query  
  
##### Response
    
    
    [
      {
          "name": "string",
          "email": "customer@somedomain.com",
          "phone_number": "+1 111-111-1111",
          "outbound_number": "+1 760-867-5309",
          "external_unique_id": "UID_123456"
      }
    ]
    

**_Status Code:_** 200

## Import multiple contacts to a campaign

Parameter | Required | Data Type | Definition  
---|---|---|---  
file | TRUE | String | json file containing the multiple contacts to add to a campaign.  
campaign_id | TRUE | Integer | The ID of the campaign to add the contacts to.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: FORM DATA
    URL: https://{​subdomain}​.{​domain}​/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contacts/import
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Body:_**

'FORM DATA'

**_File content:_**
    
    
    [
      {
          "name": "string",
          "email": "customer@somedomain.com",
          "phone_number": "+1 111-111-1111",
          "outbound_number": "+1 760-867-5309",
          "external_unique_id": "UID_123456"
      }
    ]
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Import multiple contacts from a file

This example demonstrates the adding of contacts to a campaign based on a file being posted to the endpoint. The file is posted as form data.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | multipart/form-data |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | integer | Campaign ID to add the contacts to  
  
**_File content:_**
    
    
    [
      {
          "name": "string",
          "email": "customer@somedomain.com",
          "phone_number": "+1 111-111-1111",
          "outbound_number": "+1 760-867-5309",
          "external_unique_id": "UID_123456"
      }
    ]
    

##### Response

`None`

**_Status Code:_** 202 (Accepted)

## Jobs

Parameter | Required | Data Type | Definition  
---|---|---|---  
job_id | TRUE | Integer | The job ID that you want to retrieve  
campaign_id | TRUE | Integer | The campaign ID that the job ID belongs to.  
  
**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contacts/jobs/{job_id}
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Successfully completed

The following example demonstrates how to retrieve the job and identify if they have been successfully completed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | 1 | The campaign ID that the job belongs to  
job_id | 530 | The job ID to check the status of  
  
##### Response
    
    
    {
        "id": 530,
        "status": "completed",
        "type": "Jobs::Bulk::Campaign::ParentJob"
    }
    

**_Status Code:_** 200

#### Importing still in progress

The following example demonstrates how to retrieve the job and identify if the importation is still ongoing.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | 1 | The campaign ID that the job belongs to  
job_id | 530 | The job ID to check the status of  
  
##### Response
    
    
    {
        "id": 530,
        "status": "in_progress",
        "type": "Jobs::Bulk::Campaign::ParentJob"
    }
    

**_Status Code:_** 200

#### Failed job

The following example demonstrates how to retrieve the job and identify if the job has failed.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | 1 | The campaign ID that the job belongs to  
job_id | 523 | The job ID to check the status of  
  
##### Response
    
    
    {
        "error_details": "NativePowerDial::ContactService::DuplicateContactPhoneOnCampaign",
        "error_message": "Internal Error",
        "id": 523,
        "status": "failed",
        "type": "Jobs::Bulk::Campaign::StartImport"
    }
    

**_Status Code:_** 200

## Update a single contact

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The campaign ID that the job ID belongs to.  
  
**_Endpoint:_**
    
    
    Method: PATCH
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contact
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contact_id": 16312,
        "name": "string",
        "email": "customer@somedomain.com",
        "phone_number": "+1 111-111-1111",
        "external_unique_id": "UID_123456"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Update a contact for a campaign

This example demonstrates how to update a contact that is in a specific campaign.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contact_id": 7,
        "name": "Bob Smith",
        "email": "customer@somedomain.com",
        "phone_number": "+1 111-111-1111",
        "external_unique_id": "UID_123456"
    }
    

##### Response
    
    
    {
        "id": 7,
        "name": "Bob Smith",
        "campaign_id": 6,
        "assigned_call_id": null,
        "assigned_participant_id": null,
        "outbound_number": "+1-(201)-471-6992",
        "priority": null,
        "created_at": "2024-08-05T14:51:49.000Z",
        "updated_at": "2024-08-05T21:01:16.000Z",
        "status": "Upcoming",
        "user_custom_metadata": {
            "NAME (REQUIRED)": "Bob Smith",
            "PHONE (REQUIRED)": "+1 111-111-1111",
            "EMAIL (REQUIRED)": "customer@somedomain.com"
        }
    }
    

**_Status Code:_** 200

## Remove single contact

Parameter | Required | Data Type | Definition  
---|---|---|---  
campaign_id | TRUE | Integer | The campaign ID that the job ID belongs to.  
  
**_Endpoint:_**
    
    
    Method: DELETE
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/outbound_dialer/campaigns/{campaign_id}/contact
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contact_id": integer,
        "phone_number": "string",
        "external_unique_id": "string"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Remove a contact by contact ID

This example demonstrates how to remove a contact from a campaign based on the contact ID of the contact.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contact_id": 7,
    }
    

**_Query:_**

Key | Value | Description  
---|---|---  
campaign_id | 1 | The campaign ID that the job belongs to  
  
##### Response
    
    
    {
        "id": 7,
        "name": "Bob Smith",
        "campaign_id": 6,
        "assigned_call_id": null,
        "assigned_participant_id": null,
        "outbound_number": "+1-(201)-471-6992",
        "priority": null,
        "created_at": "2024-08-05T14:51:49.000Z",
        "updated_at": "2024-08-05T21:01:16.000Z",
        "status": "Upcoming",
        "user_custom_metadata": {
            "NAME (REQUIRED)": "Bob Smith",
            "PHONE (REQUIRED)": "+1 111-111-1111",
            "EMAIL (REQUIRED)": "customer@somedomain.com"
        }
    }
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
