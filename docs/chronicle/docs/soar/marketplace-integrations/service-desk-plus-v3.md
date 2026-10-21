---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus-v3/
title: ServiceDesk Plus V3 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:56.242662+00:00
---

# ServiceDesk Plus V3  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus-v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ServiceDesk Plus V3

This document provides guidance on how to integrate ServiceDesk Plus V3 with Google SecOps.

## Configure ServiceDesk Plus V3 to work with Google Security Operations

### How to generate API Token

  1. Go to your admin user console.

![ServiceDesk Plus V3
console](https://docs.cloud.google.com/static/chronicle/images/integrations/service-desk-plus-v3-console.png)

  2. Click on it, and then click **Generate API Key**.

![Generate API Key in ServiceDesk Plus V3
console](https://docs.cloud.google.com/static/chronicle/images/integrations/service-desk-plus-v3-generate-api-key.png)

  3. A dialog shows your key generation status.

     * If you have already generated the key, make sure to keep it somewhere safe, otherwise, you will have to regenerate.
     * If not, click **Generate key** and the API key will be shown right away.

![Regenerate API Key in ServiceDesk Plus V3
    console](https://docs.cloud.google.com/static/chronicle/images/integrations/service-desk-plus-v3-regenerate-api-key.png)




## Configure ServiceDesk Plus V3 integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | http://{IP OR FQDN}:8080/api/v3/ | Yes | API Root of ServiceDesk Plus.  
Api Token | String | N/A | Yes | API token of the ServiceDesk Plus. (also called "Technician Key")  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the ServiceDesk Plus server is valid.  
  
## Actions

### Ping

#### Description

Test connectivity to ServiceDesk Plus V3 with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use cases

The action is used to test connectivity at the integration configuration page on the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully connected to the ServiceDesk Plus V3 with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the ServiceDesk Plus V3! Error is {0}".format(exception.stacktrace) | General  
  
### Add Note

#### Description

Add a note to a request.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The requests' ID.  
Note | String | N/A | Yes | The note's content.  
Show To Requester | Checkbox | Unchecked | No | Specify whether the note should be shown to the requester or not.  
Notify Technician | Checkbox | Unchecked | No | Specify whether the note should be shown to the requester or not.  
Mark as First Response | Checkbox | Unchecked | No | Specify whether this note should be marked as the first response.  
Add to linked Requests | Checkbox | Unchecked | No | Specify whether this note should be added to the linked requests.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "response_status": {
            "status_code": 2000,
            "status": "success"
        },
        "request_note": {
            "created_time": {
                "display_value": "Nov 10, 2020 01:14 AM",
                "value": "1690499678XXX"
            },
            "request": {
                "subject": "New Subject Dropdown",
                "id": "00"
            },
            "show_to_requester": false,
            "description": "New Note",
            "id": "23",
            "created_by": {
                "email_id": null,
                "name": "administrator",
                "is_vipuser": false,
                "id": "4",
                "department": null
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully added note to ServiceDesk Plus request. Request ID: {ID} , note ID: {note.id}."___If the "Request ID" parameter is not found:_ "Action wasn't able to add note to request with ID {ID} in ServiceDesk Plus. Reason: Request with ID {ID} wasn't found."******The action should fail and stop a playbook execution:******_If not successful:_ ****"Error executing action "Add Note action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Close Request

#### Description

Close a request.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The request's ID.  
Comment | String | N/A | Yes | Closing comment.  
Resolution Acknowledged | Checkbox | Unchecked | No | Whether the resolution of the request is acknowledged or not.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "response_status": {
            "status_code": 2000,
            "messages": [
                {
                    "status_code": 2000,
                    "type": "success",
                    "message": "Request(s) closed successfully."
                }
            ],
            "status": "success"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ Print "Successfully closed ServiceDesk Plus request with ID {ID} ."___If Request ID not found:_ Print "Action wasn't able to close request with ID {ID} in ServiceDesk Plus. Reason: Request with ID {ID} wasn't found."******The action should fail and stop a playbook execution:******_If not successful:_ Print "Error executing action "Close Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Note and Wait for Reply

#### Description

Add a note to a request.

**Note:** Update the actual time you would like the action to run in the IDE timeout section for this action.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The requests' ID.  
Note | String | N/A | Yes | The note's content.  
Show To Requester | Checkbox | Unchecked | No | Specify whether the note should be shown to the requester or not.  
Notify Technician | Checkbox | Unchecked | No | Specify whether the note should be shown to the requester or not.  
Mark as First Response | Checkbox | Unchecked | No | Specify whether this note should be marked as first response.  
Add to linked Requests | Checkbox | Unchecked | No | Specify whether this note should be added to the linked requests.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "response_status": {
            "status": "Success",
            "statuscode": "2000"
        },
        "request_note": {
            "id": "1",
            "description": "Need more info on this topic. Please contact me.",
            "created_by": {
                "id": "4",
                "name": "administrator"
            },
            "show_to_requester": true,
            "request": {
                "id": "2"
            },
            "created_time": {
                "value": 1455520864880,
                "display_value": "Feb 15, 2016 12:51 PM"
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully added note to ServiceDesk Plus request. Request ID: {ID} , note ID: {note.id}."_If the "Request ID" parameter is not found:_ "Action wasn't able to add note to request with ID {ID} in ServiceDesk Plus. Reason: Request with ID {ID} wasn't found."**The action should fail and stop a playbook execution:******_If not successful:_ ****"Error executing action "Add Note action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Alert Request

#### Description

Create a request related to a Google SecOps alert.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subject | String | N/A | Yes | The subject of the request.  
Requester | String | User of the API key | Yes | The requester of the request. If not specified, set to the user of the API key.  
Assets | String | N/A | No | Names of Assets to be associated with the request.  
Status | String | N/A | No | The status of the request.  
Technician | String | N/A | No | The name of the technician assigned to the request.  
Priority | String | N/A | No | The priority of the request.  
Urgency | String | N/A | No | The urgency of the request.  
Category | String | N/A | No | The category of the request.  
Request Template | String | N/A | No | The template of the request.  
Request Type | String | N/A | No | The type of the request.Example: Incident, Service Request  
Due By Time (ms) | String | N/A | No | The due date of the request in milliseconds.  
Mode | String | N/A | No | The mode in which this request is created.  
Example: E-mail  
Level | String | N/A | No | The level of the request.  
Site | String | N/A | No | Denotes the site to which this request belongs.  
Group | String | N/A | No | Group to which this request belongs.  
Impact | String | N/A | No | The impact of the request.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "request": {
            "ola_due_by_time": null,
            "subject": "Test request number 2",
            "resolution": {
                "submitted_on": {
                    "display_value": "Oct 28, 2020 09:31 PM",
                    "value": "1603945909120"
                },
                "submitted_by": {
                    "email_id": null,
                    "name": "administrator",
                    "is_vipuser": false,
                    "id": "4",
                    "department": null
                },
                "resolution_attachments": [],
                "content": "Mail Fetching Server problem has been fixed"
            },
            "linked_to_request": null,
            "mode": null,
            "lifecycle": null,
            "reason_for_cancel": null,
            "assets": [
                {
                    "name": "servicedesk.workgroup",
                    "id": "24"
                }
            ],
            "is_trashed": false,
            "id": "6",
            "assigned_time": null,
            "group": null,
            "requester": {
                "email_id": null,
                "name": "administrator",
                "is_vipuser": false,
                "id": "4",
                "department": null
            },
            "cancel_requested_by": null,
            "email_to": [],
            "created_time": {
                "display_value": "Oct 28, 2020 09:31 PM",
                "value": "1603945909120"
            },
            "item": null,
            "level": null,
            "has_resolution_attachments": false,
            "approval_status": null,
            "impact": null,
            "service_category": null,
            "sla": null,
            "priority": null,
            "created_by": {
                "email_id": null,
                "name": "administrator",
                "is_vipuser": false,
                "id": "4",
                "department": null
            },
            "scheduled_end_time": null,
            "tags": [],
            "first_response_due_by_time": null,
            "last_updated_time": null,
            "has_notes": false,
            "impact_details": "Routine tasks are pending due to mail server problem",
            "subcategory": null,
            "email_cc": [],
            "status": {
                "color": "#0066ff",
                "name": "Open",
                "id": "2"
            },
            "scheduled_start_time": null,
            "template": {
                "is_service_template": false,
                "name": "Default Request",
                "id": "1"
            },
            "email_ids_to_notify": [],
            "request_type": {
                "name": "Incident",
                "id": "1"
            },
            "cancel_requested_time": null,
            "description": "I am unable to fetch mails from the mail server",
            "has_dependency": false,
            "has_conversation": false,
            "callback_url": null,
            "chat_type": 0,
            "is_service_request": false,
            "urgency": null,
            "is_shared": false,
            "cancel_requested": false,
            "has_request_initiated_change": false,
            "request_template_task_ids": [],
            "department": null,
            "is_reopened": false,
            "has_draft": false,
            "has_attachments": false,
            "has_linked_requests": false,
            "is_overdue": false,
            "technician": null,
            "has_request_caused_by_change": false,
            "has_problem": false,
            "due_by_time": null,
            "has_project": false,
            "is_first_response_overdue": false,
            "cancel_requested_is_pending": false,
            "category": null
        },
        "response_status": {
            "status_code": 2000,
            "status": "success"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully created ServiceDesk Plus request"**The action should fail and stop a playbook execution:******_If not successful:_ ****"Error executing action "Create Alert Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Request

#### Description

Create a new request.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subject | String | N/A | Yes | The subject of the request.  
Requester | String | User of the API key | Yes | The requester of the request. If not specified, set to the user of the API key.  
Description | String | N/A | No | The description of the request.  
Assets | String | N/A | No | Names of Assets to be associated with the request.  
Status | String | N/A | No | The status of the request.  
Technician | String | N/A | No | The name of the technician assigned to the request.  
Priority | String | N/A | No | The priority of the request.  
Urgency | String | N/A | No | The urgency of the request.  
Category | String | N/A | No | The category of the request.  
Request Template | String | N/A | No | The template of the request.  
Request Type | String | N/A | No | The type of the request.Example: Incident, Service Request  
Due By Time (ms) | String | N/A | No | The due date of the request in milliseconds.  
Mode | String | N/A | No | The mode in which this request is created.  
Example: E-mail  
Level | String | N/A | No | The level of the request.  
Site | String | N/A | No | Denotes the site to which this request belongs.  
Group | String | N/A | No | Group to which this request belongs.  
Impact | String | N/A | No | The impact of the request.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully created ServiceDesk Plus request"******The action should fail and stop a playbook execution:**_If not successful:_ "Error executing action "Create Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Request

#### Description

Retrieve information about a request In ServiceDesk Plus.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The ID of the request.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully fetched ServiceDesk Plus request with ID {ID} ."_If the "Request ID" parameter is not found:_ "Action wasn't able fetch request with ID {ID} in ServiceDesk Plus. Reason: Request with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_If not successful:_ "Error executing action "Get Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Wait for Field Update

#### Description

Wait for a field of a request to update to a desired value.

**Note:** Update the actual time you would like the action to run in the IDE timeout section for this action.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The ID of the request.  
Field Name | String | N/A | Yes | The name of the field to be updated.  
Values | String | N/A | Yes | Desired values for the given field.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successfully created a wait (async action) task for the field:_ "Created analysis tasks for the field: {0}".format([fields_list])._If fail to create an analysis task for all of the provided fields:_ "No ServiceDesk Plus analysis tasks were created."_If still waiting for field to be updated:_ "Action waiting for the next update"**Action should fail and stop playbook execution:**_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the ServiceDesk service! Error is {0}".format(exception.stacktrace) | General  
  
### Update Request

#### Description

Update a ServiceDesk Plus request through it's ID.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | True | The ID of the request to update.  
Subject | String | N/A | No | The subject of the request.  
Requester | String | N/A | No | The requester of the request.If not specified, set to the user of the API key.  
Description | String | N/A | No | The description of the request.  
Assets | String | N/A | No | Names of Assets to be associated with the request.The parameter can also get a list of comma separated strings with names of assets.  
Status | String | N/A | No | The status of the request.  
Technician | String | N/A | No | The name of the technician assigned to the request.  
Priority | String | N/A | No | The priority of the request.  
Urgency | String | N/A | No | The urgency of the request.  
Category | String | N/A | No | The category of the request.  
Request Template | String | N/A | No | The template of the request.  
Request Type | String | N/A | No | The type of the request. Example: Incident, Service Request  
Due By Time (ms) | String | N/A | No | The due date of the request in milliseconds.  
Mode | String | N/A | No | The mode in which this request is created.  
Example: E-mail  
Level | String | N/A | No | The level of the request.  
Site | String | N/A | No | Denotes the site to which this request belongs.  
Group | String | N/A | No | Group to which this request belongs.  
Impact | String | N/A | No | The impact of the request.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully updated ServiceDesk Plus request with ID {ID} ."_If the "Request ID" parameter is not found:_ "Action wasn't able update request with ID {ID} in ServiceDesk Plus. Reason: Request with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_If not successful:_ "Error executing action "Update Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
### Wait for Status Update

#### Description

Wait for the status of a request ot update to a desired status.

**Note:** Update the actual time you would like the action to run in the IDE timeout section for this action.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Request ID | String | N/A | Yes | The ID of the request.  
Values | String | N/A | Yes | Desired values for the given field.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successfully created a wait (async action) task for the field:_ "Created analysis tasks for the field: {0}".format([fields_list])._If failed to create analysis task for all of the provided field:_ "No ServiceDesk Plus analysis tasks were created."_If still waiting for field to be updated:_ "Action waiting for the next update"**Action should fail and stop playbook execution:**_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the ServiceDesk service! Error is {0}".format(exception.stacktrace) | General  
  
### Create Request - Drop Down Lists

#### Description

Create a new request.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subject | String | N/A | Yes | The subject of the request.  
Requester | String | N/A | No | The requester of the request. If not specified, set to the user of the API key.  
Assets | String | N/A | No | Names of Assets to be associated with the request.The parameter can also get a list of comma-separated strings with names of assets.  
Description | String | N/A | No | The description of the request.  
Status | DDL | N/A | No | The status of the request.  
Technician | String | N/A | No | The name of the technician assigned to the request.  
Priority | DDL | N/A | No | The priority of the request.  
Urgency | DDL | N/A | No | The urgency of the request.  
Category | DDL | N/A | No | The category of the request.  
Request Template | String | N/A | No | The template of the request.  
Request Type | DDL | N/A | No | The type of the request.Example: Incident, Service Request  
Due By Time (ms) | String | N/A | No | The due date of the request in milliseconds.  
Mode | DDL | N/A | No | The mode in which this request is created.  
Example: E-mail  
Level | DDL | N/A | No | The level of the request.  
Site | String | N/A | No | Denotes the site to which this request belongs.  
Group | String | N/A | No | Group to which this request belongs.  
Impact | DDL | N/A | No | The impact of the request.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ "Successfully created ServiceDesk Plus request"******The action should fail and stop a playbook execution:**_If not successful:_ "Error executing action "Create Request action". Reason: {0}''.format(error.Stacktrace) | General  
  
## Jobs

### Sync Closed Requests By Tag

#### Description

Synchronizes ServiceDesk Plus V3 requests that are created within the Google SecOps Case playbook and Google SecOps cases.

**Note:** In ServiceDesk Plus V3, the "Cancelled", "Closed", and "Resolved" statuses are treated as closed. Additionally, the case needs to have two tags for the job to work. The first tag should be "ServiceDesk Plus" and the second tag should start with the "ServiceDesk Plus Requests:{request id}" prefix.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | http://{IP OR FQDN}:8080/api/v3/ | Yes | API root of the ServiceDeskPlus instance.  
Api Key | Password | N/A | Yes | API key of the ServiceDeskPlus instance.  
Max Hours Backwards | Integer | 24 | No | Specify the number of hours backwards to synchronize statuses.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the ServiceDeskPlus server is valid.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
