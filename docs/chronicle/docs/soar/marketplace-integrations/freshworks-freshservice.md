---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/freshworks-freshservice/
title: Freshworks Freshservice \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:09.705574+00:00
---

# Freshworks Freshservice  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/freshworks-freshservice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Freshworks Freshservice

This document describes how to integrate Freshworks Freshservice with Google Security Operations.

## Use Cases

Integration with service desk.

## Freshservice Configuration

Freshservice Google Security Operations integration is working based on Freshservice API Keys.

## How to get the API Key of the account in Freshservice

  1. Login to your Freshservice Support Portal
  2. Click on account profile picture on the top right corner of your portal
  3. Go to Profile settings Page
  4. Account API key will be available below the change password section to your right
  5. Save this API key, you will need it for the Google SecOps integration configuration.



## Configure Freshworks Freshservice integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://yourdomain.freshservice.com | Yes | Freshservice instance API Root URL.  
API Key | Password | N/A | Yes | Freshservice API Key to use in integration.  
Verify SSL | Checkbox | Checked | No | If enabled, the integration verifies that Root URL is configured with a valid certificate.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Freshservice instance with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** "Successfully connected to the Freshservice instance with the provided connection parameters!"

******The action should fail and stop a playbook execution:if critical error, like wrong credentials or lost connectivity:** "Failed to connect to the Freshservice instance! Error is {0}".format(exception.stacktrace) | General  
  
### List Tickets

#### Description

List Freshservice tickets based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket Type | DDL | All | No | Specify ticket type to return.  
Requester | String | N/A | No | Specify the requester email of the tickets to return.  
Include Stats | Checkbox | Unchecked | No | If enabled, action will return additional stats on the tickets.  
Search for Last X Hours | Integer | N/A | No | Specify the timeframe to search tickets for.  
Rows per Page | Integer | 30 | No | Specify how many tickets should be returned per page for Freshservice pagination.  
Start at Page | Integer | 1 | No | Specify starting from which page tickets should be returned with Freshservice pagination.  
Max Rows to Return | Integer | 30 | No | Specify how many tickets action should return in total.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "tickets": [
            {
                "subject": "Support Needed...",
                "group_id": null,
                "department_id": null,
                "category": null,
                "sub_category": null,
                "item_category": null,
                "requester_id": 17000032840,
                "responder_id": null,
                "due_by": "2021-07-08T21:00:00Z",
                "fr_escalated": false,
                "deleted": false,
                "spam": false,
                "email_config_id": null,
                "fwd_emails": [],
                "reply_cc_emails": [],
                "cc_emails": [],
                "is_escalated": false,
                "fr_due_by": "2021-07-01T18:00:00Z",
                "id": 7,
                "priority": 1,
                "status": 2,
                "source": 2,
                "created_at": "2021-06-29T08:56:24Z",
                "updated_at": "2021-06-29T10:04:51Z",
                "to_emails": null,
                "type": "Incident",
                "description": "<div>Details about the issue...</div>",
                "description_text": "Details about the issue...",
                "custom_fields": {},
                "requester": {
                    "email": "dana@example.com",
                    "id": 17000032840,
                    "mobile": "dana@example.com",
                    "name": "Dana",
                    "phone": null
                }
            }
        ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If found tickets (is_success = true):** "Successfully fetched Freshservice tickets."
  * **If no tickets returned (is_success = false):** "No tickets were found for the provided input parameters."
  * **If got an API error getting tickets (is_success = false):** "Failed to list tickets with the provided input parameters. Error is: {error from the API}"  
****

**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Tickets". Reason: {0}''.format(error.Stacktrace) | General  
Table | **Table Name:** Freshservice Tickets Found**Table Columns:** IDTypeSubjectDescriptionRequester EmailCategoryStatusPrioritySourceCreated DateUpdated DateDue DateEscalatedDeleted | General  
  
### Create Ticket

#### Description

Create a Freshservice ticket.

**Note:** As of now, Freshservice API supports only creation of tickets with the type "Incident".

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Subject | String | N/A | Yes | Specify subject field for created ticket.  
Description | String | N/A | Yes | Specify description field for created ticket.  
Requester Email | String | N/A | Yes | Specify requester email for created ticket.  
Agent Assign To | String | N/A | No | Specify the agent email to assign the ticket to.  
Group Assign To | String | N/A | No | Specify the group name to assign the ticket to.  
Priority | DDL | Medium | Yes | Specify priority to assign to the ticket.  
Urgency | DDL | Medium | No | Specify urgency to assign to the ticket.  
Impact | DDL | Medium | No | Specify impact to assign to the ticket.  
Tags | String | N/A | No | Specify tags to assign to the ticket. Parameter accepts multiple values as a comma separated string.  
Department Name | String | N/A | No | Specify the name of the department that will own or manage the ticket.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the ticket. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
File Attachments to Add | String (CSV) | N/A | No | Specify the full path for the file to be uploaded with the ticket. Parameter accepts multiple values as a comma separated string. The total size of the attachments must not exceed 15MB.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "ticket": {
            "cc_emails": [],
            "fwd_emails": [],
            "reply_cc_emails": [],
            "fr_escalated": false,
            "spam": false,
            "email_config_id": null,
            "group_id": null,
            "priority": 2,
            "requester_id": 17000032840,
            "responder_id": null,
            "source": 2,
            "status": 2,
            "subject": "Support Needed 4...",
            "to_emails": null,
            "department_id": null,
            "id": 10,
            "type": "Incident",
            "due_by": "2021-07-02T18:00:00Z",
            "fr_due_by": "2021-06-30T20:00:00Z",
            "is_escalated": false,
            "description": "<div>Details about the issue...</div>",
            "description_text": "Details about the issue...",
            "category": null,
            "sub_category": null,
            "item_category": null,
            "custom_fields": {
                "test": "very_test"
            },
            "created_at": "2021-06-30T08:01:30Z",
            "updated_at": "2021-06-30T08:01:30Z",
            "tags": [
                "test"
            ],
            "attachments": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true):** New freshservice ticket created.
  * **If action failed to run because of the provided parameters(is_success =false):** Failed to create new ticket with the provided parameters, error is: <error text>.****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Ticket". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Ticket

#### Description

Update a Freshservice ticket based on provided action input parameters. Note that if new tags for the ticket are provided, due to the Freshservice API limitations action replaces existing tags in the ticket, not appending new ones to existing.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket id to update.  
Status | DDL | Not changed | No | Specify new status for the ticket.  
Subject | String | N/A | No | Specify subject field to update.  
Description | String | N/A | No | Specify description field to update.  
Requester Email | String | N/A | No | Specify requester email to update.  
Agent Assign To | String | N/A | No | Specify the agent email to update.  
Group Assign To | String | N/A | No | Specify the group name to update.  
Priority | DDL | Not Changed | No | Specify priority to update.  
Urgency | DDL | Not Changed | No | Specify urgency to update.  
Impact | DDL | Not Changed | No | Specify impact to update.  
Tags | String | N/A | No | Specify tags to to replace in the ticket. Parameter accepts multiple values as a comma separated string. Note that due to the Freshservice API limitations action replaces existing tags in the ticket, not appending new ones to existing.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the ticket. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
File Attachments to Add | String (CSV) | N/A | No | Specify the full path for the file to be uploaded with the ticket. Parameter accepts multiple values as a comma separated string. The total size of the attachments must not exceed 15MB.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "ticket": {
            "cc_emails": [],
            "fwd_emails": [],
            "reply_cc_emails": [],
            "spam": false,
            "email_config_id": null,
            "fr_escalated": false,
            "group_id": 17000034192,
            "priority": 1,
            "requester_id": 17002188556,
            "responder_id": 17002188556,
            "source": 2,
            "status": 2,
            "subject": "Support Needed 9...",
            "description": "Details about the issue...",
            "description_text": "Details about the issue...",
            "category": null,
            "sub_category": null,
            "item_category": null,
            "custom_fields": {
                "test": "very_test"
            },
            "id": 12,
            "type": "Incident",
            "to_emails": null,
            "department_id": 17000016543,
            "is_escalated": false,
            "tags": [
                "test"
            ],
            "due_by": "2021-07-09T17:00:00-04:00",
            "fr_due_by": "2021-07-02T14:00:00-04:00",
            "created_at": "2021-06-30T08:36:43Z",
            "updated_at": "2021-06-30T09:39:12Z",
            "attachments": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Freshservice ticket <ticket id> is updated.
  * **If action failed to run because of the provided parameters(is_success =false)**
    * Failed to update ticket <ticket_id> with the provided parameters, error is: <error text>.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Update Ticket". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Ticket Conversations

#### Description

List Freshservice tickets conversations based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to return conversations for.  
Rows per Page | Integer | 30 | No | Specify how many ticket conversations should be returned per page for Freshservice pagination.  
Start at Page | Integer | 1 | No | Specify starting from which page ticket conversations should be returned with Freshservice pagination.  
Max Rows to Return | Integer | 30 | No | Specify how many ticket conversations action should return in total.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "conversations": [
            {
                "id": 17014994010,
                "user_id": 17000032840,
                "to_emails": [],
                "body": "<div>This is a test note!</div>",
                "body_text": "This is a test note!",
                "ticket_id": 12,
                "created_at": "2021-07-05T06:58:32Z",
                "updated_at": "2021-07-05T06:58:32Z",
                "incoming": false,
                "private": false,
                "support_email": null,
                "source": 2,
                "from_email": null,
                "cc_emails": [],
                "bcc_emails": null,
                "attachments": []
            },
            {
                "id": 17014993985,
                "user_id": 17000032840,
                "to_emails": [
                    "dana@example.com"
                ],
                "body": "<div>We are working on this issue. Will keep you posted.</div>",
                "body_text": "We are working on this issue. Will keep you posted.",
                "ticket_id": 12,
                "created_at": "2021-07-05T06:57:27Z",
                "updated_at": "2021-07-05T06:57:27Z",
                "incoming": false,
                "private": false,
                "support_email": "helpdesk@siemplifyservicedesk.freshservice.com",
                "source": 0,
                "from_email": "helpdesk@siemplifyservicedesk.freshservice.com",
                "cc_emails": [],
                "bcc_emails": [],
                "attachments": []
            }
        ],
        "meta": {
            "count": 2
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If found ticket conversations (is_success = true):**  
****"Successfully fetched Freshservice ticket <ticket id> conversations."
  * **If no ticket conversations are returned (is_success = false):**  
****"No ticket conversations were found for the ticket <ticket id>"
  * **If provided ticket id was not found (is_success = false):**  
****"Ticket <ticket id> was not found in Freshservice.
  * **If got an API error getting tickets (is_success = false):** "Failed to list ticket conversations with the provided input parameters. Error is: {error from the API}"  
****  
****

**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Ticket Conversations". Reason: {0}''.format(error.Stacktrace) | **General**  
Table | **Table Name:** Freshservice Ticket <ticket id> Conversations **Table Columns:** IDTypeVisibilityUser EmailTextFrom EmailTo EmailCC EmailBCC Email | General  
  
### Add a Ticket Reply

#### Description

Add a reply to a Freshservice ticket. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to return conversations for.  
Reply Text | String | N/A | Yes | Specify reply text to add to ticket.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
        "conversation": {
            "id": 17014998560,
            "user_id": 17000032840,
            "from_email": "helpdesk@siemplifyservicedesk.freshservice.com",
            "cc_emails": [],
            "bcc_emails": [],
            "body": "<div>We are working on this issue. Will keep you posted.2</div>",
            "body_text": "We are working on this issue. Will keep you posted.2",
            "ticket_id": 12,
            "to_emails": [
                "dana@example.com"
            ],
            "attachments": [],
            "created_at": "2021-07-05T09:19:02Z",
            "updated_at": "2021-07-05T09:19:02Z"
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * New reply is added to ticket <ticket id>.
  * **If provided ticket id was not found (is_success = false):**
    * "Ticket <ticket id> was not found in Freshservice.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Add a Ticket Reply". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add a Ticket Note

#### Description

Add a note to a Freshservice ticket. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to return conversations for.  
Note Type | DDL | Private | No | Specify the type of note action should add to the ticket.  
Note Text | String | N/A | Yes | Specify note text to add to ticket.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "conversation": {
            "id": 17014999107,
            "incoming": false,
            "private": false,
            "user_id": 17000032840,
            "support_email": null,
            "body": "<div>This is a test note2!</div>",
            "body_text": "This is a test note2!",
            "ticket_id": 12,
            "to_emails": [],
            "attachments": [],
            "created_at": "2021-07-05T09:35:28Z",
            "updated_at": "2021-07-05T09:35:28Z"
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * New <note type> note is added to ticket <ticket id>.
  * **If provided ticket id was not found (is_success = false):**
    * "Ticket <ticket id> was not found in Freshservice.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Add a Ticket Note". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Agents

#### Description

List Freshservice agents based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Agent Email | String | N/A | No | Specify the email address to return agent records for.  
Agent State | DDL | ALL | No | Specify agent states to return.  
Include not Active Agents | Checkbox | Unchecked | No | If enabled, results will include not active agent records.  
Rows per Page | Integer | 30 | No | Specify how many agent records should be returned per page for Freshservice pagination.  
Start at Page | Integer | 1 | No | Specify starting from which page agent records should be returned with Freshservice pagination.  
Max Rows to Return | Integer | 30 | No | Specify how many agent records action should return in total.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "agents": [
            {
                "active": true,
                "address": null,
                "background_information": null,
                "can_see_all_tickets_from_associated_departments": false,
                "created_at": "2021-06-29T10:37:36Z",
                "custom_fields": {},
                "department_ids": [
                    17000016543
                ],
                "email": "dana@example.com",
                "external_id": null,
                "first_name": "dmitry",
                "has_logged_in": false,
                "id": 17002188556,
                "job_title": null,
                "language": "en",
                "last_active_at": null,
                "last_login_at": null,
                "last_name": "s",
                "location_id": null,
                "mobile_phone_number": null,
                "occasional": true,
                "reporting_manager_id": null,
                "role_ids": [
                    17000023339
                ],
                "roles": [
                    {
                        "role_id": 17000023339,
                        "assignment_scope": "entire_helpdesk",
                        "groups": []
                    }
                ],
                "scopes": {
                    "ticket": null,
                    "problem": null,
                    "change": null,
                    "asset": null,
                    "solution": null,
                    "contract": null
                },
                "scoreboard_level_id": 1,
                "signature": "<p> </p>\n",
                "time_format": "12h",
                "time_zone": "American Samoa",
                "updated_at": "2021-06-29T10:37:36Z",
                "work_phone_number": null,
                "group_ids": [
                    17000034192
                ],
                "member_of": [
                    17000034192
                ],
                "observer_of": []
            },
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If found agents (is_success = true):** "Successfully fetched Freshservice agents."
  * **If no agents returned (is_success = false):** "No agents were found for the provided input parameters."
  * **If got an API error getting agents (is_success = false):** "Failed to list agents with the provided input parameters. Error is: {error from the API}"  
****

**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Agents". Reason: {0}''.format(error.Stacktrace) | General  
Table  
****| **Table Name:** Freshservice Agents Found**Table Columns:** IDEmailFirst NameLast NameRolesGroupsDepartmentsLocationActiveOccasionalCustom FieldsCreated DateUpdated DateLast Active DateLast Login Date | General  
  
### List Requesters

#### Description

List requesters registered in Freshservice based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Requester Email | String | N/A | No | Specify the email address to return requester records for.  
Rows per Page | Integer | 30 | No | Specify how many agent records should be returned per page for Freshservice pagination.  
Start at Page | Integer | 1 | No | Specify starting from which page agent records should be returned with Freshservice pagination.  
Max Rows to Return | Integer | 30 | No | Specify how many agent records action should return in total.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "requesters": [
            {
                "active": true,
                "address": null,
                "background_information": null,
                "can_see_all_tickets_from_associated_departments": false,
                "created_at": "2020-07-06T08:07:30Z",
                "custom_fields": {
                    "test": null
                },
                "department_ids": [],
                "external_id": null,
                "first_name": "Dana",
                "has_logged_in": false,
                "id": 17000038164,
                "job_title": null,
                "language": "en",
                "last_name": "Doe",
                "location_id": null,
                "mobile_phone_number": null,
                "primary_email": "dana@example.com",
                "reporting_manager_id": null,
                "secondary_emails": [],
                "time_format": "12h",
                "time_zone": "Eastern Time (US & Canada)",
                "updated_at": "2020-07-06T08:07:30Z",
                "work_phone_number": null
            }
        ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If found requesters (is_success = true):**  
****"Successfully fetched Freshservice registered requesters."
  * **If no requesters returned (is_success = false):**  
****"No requesters were found for the provided input parameters."
  * **If got an API error getting requesters (is_success = false):** "Failed to list requesters with the provided input parameters. Error is: {error from the API}"  
****

**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Requesters". Reason: {0}''.format(error.Stacktrace) | General  
Table  
****| **Table Name:** Freshservice Requester Found**Table Columns:** IDEmailFirst NameLast NameDepartmentsLocationActiveCustom FieldsCreated DateUpdated Date | General  
  
### Create Agent

#### Description

Create a new Freshservice Agent. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Email | String | N/A | Yes | Specify the email of the agent to create.  
First Name | String | N/A | Yes | Specify the first name of the agent to create.  
Last Name | String | N/A | No | Specify the last name of the agent to create.  
Is occasional | Checkbox | Unchecked | No | If enabled, agent will be created as an occasional agent, otherwise full-time agent will be created.  
Can See All Tickets From Associated Departments | Checkbox | Unchecked | No | If enabled, agent will be able to see all tickets from Associated departments.  
  
Departments | CSV | N/A | No | Specify department names associated with the agent. Parameter accepts multiple values as a comma separated string.  
Location | String | N/A | No | Specify location name associated with the agent.  
Group Memberships | CSV | N/A | No | Specify group names agent should be a member of.  
Roles | CSV | N/A | Yes | Specify roles to add to agent. Parameter accepts multiple values as a comma separated string.Example: {"role_id":17000023338,"assignment_scope": ""}  
Job Title | String | N/A | No | Specify agent job title.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the agent. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "agent": {
            "active": true,
            "address": null,
            "background_information": null,
            "can_see_all_tickets_from_associated_departments": false,
            "created_at": "2021-07-06T05:40:41Z",
            "custom_fields": {
                "test": "testvalue"
            },
            "department_ids": [],
            "email": "rolanda.hooch@hogwarts.edu",
            "external_id": null,
            "first_name": "Rolanda",
            "has_logged_in": false,
            "id": 17002198254,
            "job_title": "Flying Instructor",
            "language": "en",
            "last_active_at": null,
            "last_login_at": null,
            "last_name": "Hooch",
            "location_id": null,
            "mobile_phone_number": "553632",
            "occasional": true,
            "reporting_manager_id": null,
            "role_ids": [
                17000023338
            ],
            "roles": [
                {
                    "role_id": 17000023338,
                    "assignment_scope": "entire_helpdesk",
                    "groups": []
                }
            ],
            "scopes": {
                "ticket": null,
                "problem": null,
                "change": null,
                "asset": null,
                "solution": null,
                "contract": null
            },
            "scoreboard_level_id": 1,
            "signature": null,
            "time_format": "12h",
            "time_zone": "Eastern Time (US & Canada)",
            "updated_at": "2021-07-06T05:40:41Z",
            "work_phone_number": "443532",
            "group_ids": [
                17000034192
            ],
            "member_of": [
                17000034192
            ],
            "observer_of": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * New freshservice agent created.
  * **If action failed to run because of the provided parameters(is_success =false)**
    * Failed to create new agent the provided parameters, error is: <error text>.

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Agent". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Agent

#### Description

Update existing Freshservice Agent. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Agent ID | Integer | N/A | Yes | Specify agent id to update.  
Email | String | N/A | No | Specify the email of the agent to update.  
First Name | String | N/A | No | Specify the first name of the agent to update.  
Last Name | String | N/A | No | Specify the last name of the agent to update.  
Is occasional | Checkbox | Unchecked | No | If enabled, agent will be updated as an occasional agent, otherwise it will be a full-time agent.  
Can See All Tickets From Associated Departments | Checkbox | Unchecked | No | If enabled, agent will be able to see all tickets from Associated departments.  
  
Departments | CSV | N/A | No | Specify department names associated with the agent. Parameter accepts multiple values as a comma separated string.  
Location | String | N/A | No | Specify location name associated with the agent.  
Group Memberships | CSV | N/A | No | Specify group names agent should be a member of.  
Roles | CSV | N/A | No | Specify roles to add to agent. Parameter accepts multiple values as a comma separated string.Example: {"role_id":17000023338,"assignment_scope": "entire_helpdesk"}  
Job Title | String | N/A | No | Specify agent job title.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the agent. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "agent": {
            "active": true,
            "address": null,
            "background_information": null,
            "can_see_all_tickets_from_associated_departments": false,
            "created_at": "2021-07-06T05:40:41Z",
            "custom_fields": {
                "test": "testvalue"
            },
            "department_ids": [],
            "email": "rolanda.hooch@hogwarts.edu",
            "external_id": null,
            "first_name": "Rolanda",
            "has_logged_in": false,
            "id": 17002198254,
            "job_title": "Flying Instructor",
            "language": "en",
            "last_active_at": null,
            "last_login_at": null,
            "last_name": "Hooch",
            "location_id": null,
            "mobile_phone_number": "553632",
            "occasional": true,
            "reporting_manager_id": null,
            "role_ids": [
                17000023338
            ],
            "roles": [
                {
                    "role_id": 17000023338,
                    "assignment_scope": "entire_helpdesk",
                    "groups": []
                }
            ],
            "scopes": {
                "ticket": null,
                "problem": null,
                "change": null,
                "asset": null,
                "solution": null,
                "contract": null
            },
            "scoreboard_level_id": 1,
            "signature": null,
            "time_format": "12h",
            "time_zone": "Eastern Time (US & Canada)",
            "updated_at": "2021-07-06T05:40:41Z",
            "work_phone_number": "443532",
            "group_ids": [
                17000034192
            ],
            "member_of": [
                17000034192
            ],
            "observer_of": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Freshservice agent <agent_id> is updated.
  * **If action failed to run because of the provided parameters(is_success =false)**
    * Failed to update freshservice agent <agent_id> with the provided parameters, error is: <error text>.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Update Agent". Reason: {0}''.format(error.Stacktrace) | General  
  
### Deactivate Agent

#### Description

Deactivate Freshservice agent. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Agent ID | Integer | N/A | Yes | Specify agent id to deactivate.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "agent": {
            "active": false,
            "address": null,
            "background_information": null,
            "can_see_all_tickets_from_associated_departments": false,
            "created_at": "2021-07-06T05:40:41Z",
            "custom_fields": {
                "test": "testvalue3"
            },
            "department_ids": [],
            "email": "rolanda.hooch@hogwarts.edu",
            "external_id": null,
            "first_name": "Rolanda",
            "has_logged_in": false,
            "id": 17002198254,
            "job_title": "Flying Instructor",
            "language": "en",
            "last_active_at": null,
            "last_login_at": null,
            "last_name": "Hooch",
            "location_id": null,
            "mobile_phone_number": "553632",
            "occasional": true,
            "reporting_manager_id": null,
            "role_ids": [
                17000023338
            ],
            "roles": [
                {
                    "role_id": 17000023338,
                    "assignment_scope": "entire_helpdesk",
                    "groups": []
                }
            ],
            "scopes": {
                "ticket": null,
                "problem": null,
                "change": null,
                "asset": null,
                "solution": null,
                "contract": null
            },
            "scoreboard_level_id": 2,
            "signature": "<p> </p>\n",
            "time_format": "24h",
            "time_zone": "Eastern Time (US & Canada)",
            "updated_at": "2021-07-06T06:26:59Z",
            "work_phone_number": "443532",
            "group_ids": [],
            "member_of": [],
            "observer_of": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Freshservice agent <agent_id> is deactivated.
  * **If action failed to run because of the 404 error (is_success =false)**
    * Failed to find freshservice agent <agent_id> to deactivate.
  * **If action failed to run because of the 403 error (is_success =false)**
    * Failed to deactivate freshservice agent <agent_id>, may be it was already deactivated? API response: "code": "access_denied","message": "You are not authorized to perform this action."

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Deactivate Agent". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Requester

#### Description

Create a new Freshservice requester. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Email | String | N/A | Yes | Specify the email of the requester to create.  
First Name | String | N/A | Yes | Specify the first name of the requester to create.  
Last Name | String | N/A | No | Specify the last name of the requester to create.  
Can See All Tickets From Associated Departments | Checkbox | Unchecked | No | If enabled, requester will be able to see all tickets from Associated departments.  
  
Departments | CSV | N/A | No | Specify department names associated with the requester . Parameter accepts multiple values as a comma separated string.  
Location | String | N/A | No | Specify location name associated with the requester .  
Job Title | String | N/A | No | Specify requester job title.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the requester. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "requester": {
            "active": true,
            "address": null,
            "background_information": null,
            "can_see_all_tickets_from_associated_departments": false,
            "created_at": "2021-07-06T08:12:47Z",
            "custom_fields": {
                "test": "testvalue"
            },
            "department_ids": [],
            "external_id": null,
            "first_name": "Rolanda",
            "has_logged_in": false,
            "id": 17002198308,
            "job_title": "Flying Instructor",
            "language": "en",
            "last_name": "Hooch",
            "location_id": null,
            "mobile_phone_number": null,
            "primary_email": "rolanda.hooch2@hogwarts.edu",
            "reporting_manager_id": null,
            "secondary_emails": [],
            "time_format": "12h",
            "time_zone": "Eastern Time (US & Canada)",
            "updated_at": "2021-07-06T08:12:47Z",
            "work_phone_number": null
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * New freshservice requester created.
  * **If action failed to run because of the provided parameters(is_success =false)**
    * Failed to create new requester the provided parameters, error is: <error text>.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Requester". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Requester

#### Description

Update existing Freshservice Requester. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Requester ID | Integer | N/A | Yes | Specify requester id to update.  
Email | String | N/A | No | Specify the email of the requester to update.  
First Name | String | N/A | No | Specify the first name of the requester to update.  
Last Name | String | N/A | No | Specify the last name of the requester to update.  
Can See All Tickets From Associated Departments | Checkbox | Unchecked | No | If enabled, requester will be able to see all tickets from Associated departments.  
  
Departments | CSV | N/A | No | Specify department names associated with the requester. Parameter accepts multiple values as a comma separated string.  
Location | String | N/A | No | Specify location name associated with the requester.  
Job Title | String | N/A | No | Specify requester job title.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the requester. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "agent": {
            "active": true,
            "address": null,
            "background_information": null,
            "can_see_all_tickets_from_associated_departments": false,
            "created_at": "2021-07-06T05:40:41Z",
            "custom_fields": {
                "test": "testvalue"
            },
            "department_ids": [],
            "email": "rolanda.hooch@hogwarts.edu",
            "external_id": null,
            "first_name": "Rolanda",
            "has_logged_in": false,
            "id": 17002198254,
            "job_title": "Flying Instructor",
            "language": "en",
            "last_active_at": null,
            "last_login_at": null,
            "last_name": "Hooch",
            "location_id": null,
            "mobile_phone_number": "553632",
            "occasional": true,
            "reporting_manager_id": null,
            "role_ids": [
                17000023338
            ],
            "roles": [
                {
                    "role_id": 17000023338,
                    "assignment_scope": "entire_helpdesk",
                    "groups": []
                }
            ],
            "scopes": {
                "ticket": null,
                "problem": null,
                "change": null,
                "asset": null,
                "solution": null,
                "contract": null
            },
            "scoreboard_level_id": 1,
            "signature": null,
            "time_format": "12h",
            "time_zone": "Eastern Time (US & Canada)",
            "updated_at": "2021-07-06T05:40:41Z",
            "work_phone_number": "443532",
            "group_ids": [
                17000034192
            ],
            "member_of": [
                17000034192
            ],
            "observer_of": []
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Freshservice requester <requester_id> is updated.
  * **If action failed to run because of the provided parameters(is_success =false)**
    * Failed to update freshservice requester <requester_id> with the provided parameters, error is: <error text>.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Update Requester". Reason: {0}''.format(error.Stacktrace) | General  
  
### Deactivate Requester

#### Description

Deactivate Freshservice requester. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Requester ID | Integer | N/A | Yes | Specify requester id to deactivate.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Freshservice requester <requester_id> is deactivated.
  * **If action failed to run because of the 404 error (is_success =false)**
    * Failed to find freshservice requester <requester_id> to deactivate.
  * **If action failed to run because of the 405 error (is_success =false)**
    * Failed to deactivate freshservice requester <requester_id>, maybe it was already deactivated? API response: "message": "DELETE method is not allowed. It should be one of these method(s): GET"

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Deactivate Requester". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Ticket Time Entries

#### Description

List Freshservice tickets time entries based on the specified search criteria. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to return time entries for.  
Agent Email | String | N/A | Yes | Specify agent email to list ticket time entries for.  
Rows per Page | Integer | 30 | No | Specify how many ticket time entries should be returned per page for Freshservice pagination.  
Start at Page | Integer | 1 | No | Specify starting from which page ticket time entries should be returned with Freshservice pagination.  
Max Rows to Return | Integer | 30 | No | Specify how many ticket time entries action should return in total.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "time_entries": [
           {
               "id": 17000399635,
               "created_at": "2021-07-08T06:26:47Z",
               "updated_at": "2021-07-08T06:26:47Z",
               "start_time": "2021-07-08T06:26:47Z",
               "timer_running": false,
               "billable": true,
               "time_spent": "01:00",
               "executed_at": "2021-07-08T06:26:47Z",
               "task_id": null,
               "note": "test_entry2",
               "agent_id": 17002188556,
               "custom_fields": {}
           }
       ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If found ticket time entries (is_success = true):**  
****"Successfully fetched Freshservice ticket <ticket id> time entries."
  * **If no ticket time entries are returned (is_success = false):**  
****"No ticket time entries were found for the ticket <ticket id>"
  * **If provided ticket id was not found (is_success = false):**  
****"Ticket <ticket id> was not found in Freshservice.
  * **If no agent id was found for the provided agent email (is_success = false):**  
****"Agent <agent_email> was not found in Freshservice.
  * **If got an API error getting ticket time entries (is_success = false):** "Failed to list ticket time entries with the provided input parameters. Error is: {error from the API}"  
****  
****

**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Ticket Time Entries". Reason: {0}''.format(error.Stacktrace) | General  
Table | **Table Name:** Freshservice Ticket <ticket id> Time Entries **Table Columns:** Time Entry IDAgent EmailNoteBillableTime SpentTask IDCustom FieldsTimer RunningCreated TimeUpdated Time Start TimeExecuted Time | General  
  
### Add Ticket Time Entry

#### Description

Add a time entry to a Freshservice ticket. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to add a time entry for.  
Agent Email | String | N/A | Yes | Specify agent email for whom to add a ticket time entry.  
Note | String | N/A | No | Specify a note to add to the ticket time entry.  
Time Spent | String | N/A | Yes | Specify time spent for ticket time entry. Format: {hh:mm}  
Billable | Checkbox | False | No | If enabled, ticket time entry will be marked as billable.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the ticket time entry. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "time_entry": {
           "id": 17000405061,
           "created_at": "2021-07-10T18:22:18Z",
           "updated_at": "2021-07-10T18:22:18Z",
           "start_time": "2021-07-10T18:22:18Z",
           "timer_running": false,
           "billable": true,
           "time_spent": "01:00",
           "executed_at": "2021-07-10T18:22:18Z",
           "task_id": null,
           "note": "test_entry3",
           "agent_id": 17002188556,
           "custom_fields": {
               "test": "very_test"
           }
       }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * New time entry is added to ticket <ticket id>.
  * **If provided ticket id was not found (is_success = false):**
    * "Ticket <ticket id> was not found in Freshservice.
  * **If provided agent email was not found (is_success = false):**
    * "Agent with email <agent_email> was not found in Freshservice.
  * **If provided time spent has a wrong format (is_success = false):**
    * "Specified time spent value <time_spent> is in incorrect format, it should be in the 'hh:mm' format.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Add Ticket Time Entry". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Ticket Time Entry

#### Description

Update a time entry for a Freshservice ticket. Note that action is not working on Google SecOps entities

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to update a time entry for.  
Time Entry ID | Integer | N/A | Yes | Specify time entry ID to update.  
Agent Email | String | N/A | No | Specify agent email for whom to change a ticket time entry.  
Note | String | N/A | No | Specify a note for the ticket time entry.  
Time Spent | String | N/A | No | Specify time spent for ticket time entry. Format: {hh:mm}  
Billable | Checkbox | False (unchecked) | No | If enabled, ticket time entry will be marked as billable.  
Custom Fields | JSON | N/A | No | Specify a JSON object that contains custom fields to add to the ticket time entry. Acton appends new custom fields to any existing for a ticket. Example format: {"key1":"value1", "key2":"value2"}  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "time_entry": {
            "id": 17000405061,
            "created_at": "2021-07-10T18:22:18Z",
            "updated_at": "2021-07-10T18:30:54Z",
            "start_time": "2021-07-10T18:22:18Z",
            "timer_running": false,
            "billable": false,
            "time_spent": "03:30",
            "executed_at": "2021-07-10T18:22:18Z",
            "task_id": null,
            "note": "test_entry_updated",
            "agent_id": 17002188556,
            "custom_fields": {
                "test": "very_test2"
            }
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Time entry <time_entry_id> is updated for the ticket <ticket id>.
  * **If provided ticket id or time entry id was not found (is_success = false):**
    * "Provided ticket id <ticket_id> or time entry id <time_entry id> was not found in Freshservice.
  * **If provided agent email was not found (is_success = false):**
    * "Agent with email <agent_email> was not found in Freshservice.
  * **If provided time spent has a wrong format (is_success = false):**
    * "Specified time spent value <time_spent> is in incorrect format, it should be in the 'hh:mm' format.
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Update Ticket Time Entry". Reason: {0}''.format(error.Stacktrace) | General  
  
### Delete Ticket Time Entry

#### Description

Delete a time entry for a Freshservice ticket. Note that action is not working on Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Ticket ID | Integer | N/A | Yes | Specify ticket ID to delete a time entry for.  
Time Entry ID | Integer | N/A | Yes | Specify time entry ID to delete.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If action run successfully:(is_success=true)**
    * Time entry <time_entry_id> is deleted for the ticket <ticket id>.
  * **If provided ticket id or time entry id was not found (is_success = false):**
    * "Provided ticket id <ticket_id> or time entry id <time_entry id> was not found in Freshservice
****

**The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Ticket Time Entry". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connector

### Freshservice Tickets Connector

#### Description

Connector can be used to fetch Freshservice tickets to create Google SecOps alerts from. Connector whitelist can be used to ingest only specific types of tickets - Incidents or Service Requests.

**Note:** There is an issue with Google SecOps versions 5.6.0-5.6.2 that affects the functionality of the connector. To ensure that the connector works properly, upgrade Google SecOps to version 5.6.2 Hot Fix 3 or newer.

#### Configure Freshservice Tickets Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Freshworks Freshservice | Yes |   
Event Field Name | String | "type" | Yes |   
Environment Field Name | String | "" | No | No  
Environment Regex Pattern | String | .* | No | No  
API Root | String | https://yourdomain.freshservice.com | Yes | Freshservice instance API Root URL.  
API Key | Password | N/A | Yes | Freshservice API Key to use in integration.  
Verify SSL | Checkbox | Checked | No | If enabled, integration will try to verify that Root URL is configured with a valid certificate.  
Offset time in hours | Integer | 24 | Yes | Fetch tickets from X hours backwards.  
Max Tickets Per Cycle | Integer | 30 | Yes | How many tickets should be processed during one connector run.  
Minimum Priority to Fetch | String | Medium | No | Minimum priority of the ticket to be ingested to Google SecOps, for example, Low or Medium. Possible values: Low, Medium, High, Urgent  
Tickets Status to Fetch | CSV | Open, Closed | No | Ticket statuses to be ingested to Google SecOps. Parameter accepts multiple values as a comma separated string. Possible values: Open, Pending, Resolved, Closed  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

## Jobs

### Freshservice Sync Tickets Closure Job

#### Description

Close tickets in Freshservice if corresponding Google SecOps alerts were closed.

**Note:** The job supports Google SecOps SOAR cases with the `"Freshservice"` tag only.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://yourdomain.freshservice.com | Yes | Freshservice instance API Root URL.  
API Key | Password | N/A | Yes | Freshservice API Key to use in integration.  
Verify SSL | Checkbox | Checked | No | If enabled, integration will try to verify that Root URL is configured with a valid certificate.  
Offset time in hours | Integer | 24 | Yes | Sync tickets closure from X hours backwards.  
Default Ticket Description | String | Ticket is closed by the Siemplify Freshservice Sync Tickets Closure Job. | Yes | Specify the description that should be added to the ticket if ticket doesn't have the description, so the ticket can be closed in Freshservice, as the description field is mandatory for Freshservice.  
  
### Freshservice Sync Tickets Conversations Job

#### Description

Sync conversations (considered both replies and notes) between Google SecOps alert's case and corresponding Freshservice ticket. Sync mechanism works in both ways, Google SecOps → Freshservice and Freshservice → Google SecOps.

**Note:** The job supports Google SecOps cases with the "Freshservice" tag only.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://yourdomain.freshservice.com | Yes | Freshservice instance API Root URL.  
API Key | Password | N/A | Yes | Freshservice API Key to use in integration.  
Verify SSL | Checkbox | Checked | No | If enabled, integration will try to verify that Root URL is configured with a valid certificate.  
Offset time in hours | Integer | 24 | Yes | Sync tickets conversations from X hours backwards  
Siemplify Comment Prefix | String | SIEMPLIFY: | Yes | Prefix that will be added by the sync job to comments created for Freshservice tickets.  
Freshservice Comment Prefix | String | Freshservice Comment Sync Job: | Yes | Prefix that will be added by the sync job to the Google SecOps alert's case comments.  
Conversation Types To Sync | CSV | Replies, Notes | Yes | Specify Freshservice conversation types job should sync. Parameter accepts multiple values as a comma-separated string.  
Fetch Private Notes? | Checkbox | Checkbox Unchecked (false) | No | If enabled, will fetch both public and private notes for related Freshservice tickets.  
Sync Comment from Siemplify as X | String | Private Note | Yes | Specify which conversation type job should use to add a comment from Google SecOps. Possible values: Private Note, Public Note, Reply.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
