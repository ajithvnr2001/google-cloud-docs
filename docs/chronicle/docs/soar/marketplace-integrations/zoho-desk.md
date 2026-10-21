---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zoho-desk/
title: Zoho Desk \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:52.821574+00:00
---

# Zoho Desk  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zoho-desk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zoho Desk

This document provides guidance on how to integrate Zoho Desk with Google SecOps.

## Configure Zoho Desk integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://desk.zoho.{region} | Yes | API root of the Zoho Desk instance.  
Client ID | String | N/A | Yes | Client ID of the Zoho Desk account.  
Client Secret | Password | N/A | Yes | Client Secret of the Zoho Desk account.  
Refresh Token | Password | N/A | No | Refresh Token of the Zoho Desk account. You need to run the action "Get Refresh Token" to generate it.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Zoho Desk server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Get API credentials

  1. Go to the [Zoho Desk API console](https://api-console.zoho.eu/).
  2. Click **Add Client** and select **Self Client**.
  3. In the **Client Secret** tab, copy the value of the "Client ID" and "Client Secret" parameters and paste it into respective fields in the integration configuration window.
  4. In the **Generate Code** tab provide the following scopes: `Desk.tickets.READ,Desk.tickets.CREATE,Desk.tickets.UPDATE,Desk.tickets.DELETE,Desk.settings.READ,Desk.basic.READ,Desk.products.READ,Desk.contacts.READ` and add scope description.
  5. To get an authorization code, click **Create**.
  6. Go back to Google SecOps, simulate a case and navigate to the _Get Refresh Token_ action within the Zoho Desk integration.
  7. To configure the action, enter your authorization code and authorization link.
  8. Copy the token from the action's JSON result, paste it into the respective field in the integration configuration window and run a test.



## Use Cases

Perform triaging action.

## Actions

### Add Comment To Ticket

#### Description

Add a comment to a ticket in Zoho Desk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Specify the ID of the ticket to which you want to add a comment.  
Visibility | DDL | Public Possible Values:

  * Public
  * Private

| No | Specify if the comment should be public or private.  
Type | String | Plain Text Possible Values:

  * Plain Text
  * HTML

| No | Specify the type of the comment.  
Text | String | N/A | No | Specify the content of the comment.  
Wait For Reply | Checkbox | Unchecked | No | If enabled, the action waits for reply.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "content": "zsu[@user:11550965]zsu Please fix this ASAP",
        "commentedTime": "2022-07-01T11:18:43.935Z",
        "modifiedTime": "2022-07-01T11:18:43.935Z",
        "contentType": "plainText",
        "impersonatedUser": null,
        "encodedContent": "zsu&#x5b;&#x40;user&#x3a;11550965&#x5d;zsu Please fix this ASAP",
        "id": "97709000000179081",
        "commenterId": "97709000000092001",
        "commenter": {
            "id": "97709000000092001",
            "name": "TIP Labops",
            "email": "tip.labops@siemplify.co",
            "photoURL": "https://desk.zoho.eu/api/v1/agents/97709000000092001/photo?orgId=20083004796",
            "type": "AGENT",
            "firstName": "TIP",
            "lastName": "Labops",
            "roleName": "CEO"
        },
        "attachments": [],
        "isPublic": false
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the 200 status code is reported (is_success = true):_ "Successfully added comment "{text}" to ticket {ticket id}in Zoho Desk."_Async Message:_ "Waiting for a reply..." **The action should fail and stop a playbook execution:** _If a critical error is reported:_ "Error executing action "Add Comment To Ticket". Reason: {0}''.format(error.Stacktrace) _If errors are reported:_ "Error executing action "Add Comment To Ticket". Reason: {errors/errorMessage} | General  
  
### Create Ticket

#### Description

Create a ticket in Zoho Desk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Title | String | N/A | No | Specify the title for the ticket.  
Description | String | N/A | No | Specify the description of the ticket.  
Department Name | String | N/A | No | Specify the name of the department that should be set for the ticket.  
Contact | String | N/A | No | Specify the email of the contact for the ticket.  
Assignee Type | DDL | Select One Possible values:

  * Select One
  * Agent
  * Team

| No | Specify the type of the assignee. If "Agent" or "Team" is selected, the "Assignee Name" parameter is required.  
Assignee Name | String | N/A | No | Specify the name of the assignee for the ticket. For the agent type you can provide an email address or display name.  
Priority | DDL | Select OnePossible Values:

  * Select One
  * No Priority
  * Low
  * Medium
  * High

| No | Specify the priority for the ticket.  
Сlassification | DDL | Select OnePossible Values:

  * Select One
  * No Classification
  * Question
  * Problem
  * Feature
  * Others

| No | Specify the classification type for the ticket.  
Channel | DDL | Select OnePossible Values:

  * Select One
  * Email
  * Phone
  * Web
  * Twitter
  * Facebook
  * Chat
  * Forums

| No | Specify the channel for the ticket.  
Category | String | N/A | No | Specify the category for the ticket.  
Sub Category | String | N/A | No | Specify the subcategory for the ticket.  
Due Date | String | N/A | No | Specify the due date for the ticket. Format: ISO 8601. Example: 2022-07-06T07:05:43Z.   
Custom Fields | JSON | N/A | No | Specify a JSON object containing the custom fields that need to be updated. **Note:** You need to provide the API names of the keys.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "modifiedTime": "2022-07-01T11:00:33.000Z",
        "subCategory": null,
        "statusType": "On Hold",
        "subject": "Here's your first ticket.",
        "dueDate": null,
        "departmentId": "97709000000007061",
        "channel": "Chat",
        "onholdTime": "2022-07-01T09:32:14.717Z",
        "language": "English",
        "source": {
            "appName": null,
            "extId": null,
            "permalink": null,
            "type": "SYSTEM",
            "appPhotoURL": null
        },
        "resolution": "Koko",
        "sharedDepartments": [],
        "closedTime": null,
        "approvalCount": "0",
        "isOverDue": true,
        "isTrashed": false,
        "createdTime": "2022-06-27T17:02:17.000Z",
        "id": "97709000000160077",
        "isResponseOverdue": false,
        "customerResponseTime": "2022-06-27T17:02:17.000Z",
        "productId": null,
        "contactId": "97709000000160029",
        "threadCount": "1",
        "secondaryContacts": [],
        "priority": null,
        "classification": null,
        "commentCount": "1",
        "taskCount": "0",
        "accountId": "97709000000160001",
        "phone": "1 888 900 9646",
        "webUrl": "https://desk.zoho.eu/support/siemplify/ShowHomePage.do#Cases/dv/97709000000160077",
        "isSpam": false,
        "status": "On Hold",
        "entitySkills": [],
        "ticketNumber": "101",
        "customFields": {},
        "isArchived": false,
        "description": "Hello<",
        "timeEntryCount": "0",
        "channelRelatedInfo": null,
        "responseDueDate": null,
        "isDeleted": false,
        "modifiedBy": "97709000000092001",
        "email": "support@zohosupport.com",
        "layoutDetails": {
            "id": "97709000000023011",
            "layoutName": "Siemplify"
        },
        "channelCode": null,
        "cf": {},
        "slaId": null,
        "layoutId": "97709000000023011",
        "assigneeId": null,
        "teamId": "97709000000182001",
        "attachmentCount": "0",
        "isEscalated": false,
        "category": null
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail** **nor stop a playbook execution:**_If the 200 status code is reported (is_success=true):_ "Successfully created a ticket with ID {ticket id} in Zoho Desk.".**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Create Ticket". Reason: {0}''.format(error.Stacktrace)_If the agent is not found:_ "Error executing action "Create Ticket". Reason: agent {agent_name} wasn't found in Zoho Desk. Please check the spelling."'_If the team is not found:_ "Error executing action "Create Ticket". Reason: team {team_name} wasn't found in Zoho Desk. Please check the spelling."_If "Agent" or "Team" is selected, but the "Assignee Name" parameter is not provided:_ "Error executing action "Create Ticket". Reason: "Assignee Name" needs to be provided."_If the department is not_ _found:_ "Error executing action "Create Ticket". Reason: department {department_name} wasn't found in Zoho Desk."_If the contact is not found:_ "Error executing action "Create Ticket". Reason: contact {contact} wasn't found in Zoho Desk. Please check the spelling."_If the product is not found:_ "Error executing action "Create Ticket". Reason: product {product} wasn't found in Zoho Desk. Please check the spelling." | General  
  
### Get Refresh Token

#### Description

Get a refresh token for the configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Authorization Link | String | https://accounts.zoho.{region} | Yes | Specify the authorization link for the integration.  
Authorization Code | Password | N/A | Yes | Specify the authorization code that was generated in the dev console of Zoho.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "refresh_token": "1000.90567b1fc0c54f540e56200ae4388cef.a8f6b313297d558774bee07d60cc6863"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully generated refresh token. Copy the value into "Refresh Token" parameter in the integration configuration"T**he action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Refresh Token". Reason: {0}''.format(error.Stacktrace)_If an error in reported:_ "Error executing action "Get Refresh Token". Reason: {error}'' | General  
  
### Get Ticket Details

#### Description

Get detailed information about the ticket from Zoho Desk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket IDs | String | N/A | Yes | Specify a comma-separated list of ids for which you want to return details.  
Create Insight | Checkbox | Unchecked | No | If enabled, the action creates an insight containing information about tickets.  
Additional Fields To Return | CSV | contacts, products, assignee, departments, contract, isRead, team, skills | No | Specify the additional fields to return.Possible values: contacts, products, assignee, departments, contract, isRead, team, skills.  
Fetch Comments | Checkbox | Checked | No | If enabled, the action fetches comments related to the tickets.  
Max Comments To Return | Integer | 50 | No | Specify the number of comments to return per ticket. Maximum: 100  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "modifiedTime": "2022-06-27T17:12:35.000Z",
      "subCategory": null,
      "statusType": "Open",
      "subject": "tesa",
      "dueDate": null,
      "departmentId": "97709000000007061",
      "channel": "Phone",
      "onholdTime": null,
      "language": null,
      "source": {
          "appName": null,
          "extId": null,
          "permalink": null,
          "type": "SYSTEM",
          "appPhotoURL": null
      },
      "resolution": null,
      "sharedDepartments": [],
      "closedTime": null,
      "approvalCount": "0",
      "isOverDue": false,
      "isTrashed": false,
      "contact": {
          "firstName": null,
          "lastName": "test",
          "phone": null,
          "mobile": null,
          "id": "97709000000159194",
          "isSpam": false,
          "type": null,
          "email": "test@test.com",
          "account": {
              "website": null,
              "accountName": "test!@test.com",
              "id": "97709000000159182"
          }
      },
      "createdTime": "2022-06-27T17:12:35.000Z",
      "id": "97709000000159224",
      "isResponseOverdue": false,
      "customerResponseTime": "2022-06-27T17:12:35.000Z",
      "productId": null,
      "contactId": "97709000000159194",
      "threadCount": "1",
      "secondaryContacts": [],
      "priority": null,
      "classification": null,
      "commentCount": "0",
      "taskCount": "0",
      "accountId": "97709000000159182",
      "phone": null,
      "webUrl": "https://desk.zoho.eu/support/siemplify/ShowHomePage.do#Cases/dv/97709000000159224",
      "assignee": {
          "photoURL": "https://desk.zoho.eu/api/v1/agents/97709000000092001/photo?orgId=20083004796",
          "firstName": "TIP",
          "lastName": "Labops",
          "id": "97709000000092001",
          "email": "tip.labops@siemplify.co"
      },
      "isSpam": false,
      "status": "Open",
      "entitySkills": [],
      "ticketNumber": "102",
      "sentiment": null,
      "customFields": {},
      "isArchived": false,
      "skillsInfo": [],
      "isRead": false,
      "description": "<div style=\"font-size: 13px; font-family: Regular, Lato, Arial, Helvetica, sans-serif\"><div>tetsta</div></div>",
      "timeEntryCount": "0",
      "channelRelatedInfo": null,
      "responseDueDate": null,
      "isDeleted": false,
      "modifiedBy": "97709000000092001",
      "department": {
          "name": "Siemplify",
          "id": "97709000000007061"
      },
      "followerCount": "0",
      "email": "test@test.com",
      "layoutDetails": {
          "id": "97709000000023011",
          "layoutName": "Siemplify"
      },
      "channelCode": null,
      "product": null,
      "isFollowing": false,
      "cf": {},
      "slaId": null,
      "team": null,
      "layoutId": "97709000000023011",
      "assigneeId": "97709000000092001",
      "createdBy": "97709000000092001",
      "teamId": null,
      "contractId": null,
      "tagCount": "0",
      "attachmentCount": "0",
      "isEscalated": false,
      "category": null
      "comments":          {
                "content": "<div style=\"font-size: 14px; font-family: LatoRegular, Regular, Lato, &quot;Lato 2&quot;, Arial, Helvetica, sans-serif\"><div style=\"font-size: 14px; font-family: LatoRegular, Regular, Lato, &quot;Lato 2&quot;, Arial, Helvetica, sans-serif\"><ul><li>asdasdasdasd<br /></li></ul></div><div><br /></div></div>",
                "commentedTime": "2022-06-29T10:21:24.000Z",
                "modifiedTime": "2022-06-29T10:23:42.000Z",
                "contentType": "html",
                "impersonatedUser": null,
                "encodedContent": "&lt;div style&#x3d;&quot;font-size&#x3a; 14px&#x3b; font-family&#x3a; LatoRegular, Regular, Lato, &amp;quot&#x3b;Lato 2&amp;quot&#x3b;, Arial, Helvetica, sans-serif&quot;&gt;&lt;div style&#x3d;&quot;font-size&#x3a; 14px&#x3b; font-family&#x3a; LatoRegular, Regular, Lato, &amp;quot&#x3b;Lato 2&amp;quot&#x3b;, Arial, Helvetica, sans-serif&quot;&gt;&lt;ul&gt;&lt;li&gt;asdasdasdasd&lt;br &#x2f;&gt;&lt;&#x2f;li&gt;&lt;&#x2f;ul&gt;&lt;&#x2f;div&gt;&lt;div&gt;&lt;br &#x2f;&gt;&lt;&#x2f;div&gt;&lt;&#x2f;div&gt;",
                "id": "97709000000172003",
                "commenterId": "97709000000092001",
                "commenter": {
                    "id": "97709000000092001",
                    "name": "TIP Labops",
                    "email": "tip.labops@siemplify.co",
                    "photoURL": "https://desk.zoho.eu/api/v1/agents/97709000000092001/photo?orgId=20083004796",
                    "type": "AGENT",
                    "firstName": "TIP",
                    "lastName": "Labops",
                    "roleName": "CEO"
                },
                "attachments": [],
                "isPublic": false
            }
    
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for at least one ID (is_success = true):_ "Successfully returned details related to the following tickets in Zoho Desk: {ticket ids}"._If data is not available for at least one ID (is_success=true):_ "Action wasn't able to find details related to the following tickets in Zoho Desk: {ticket ids}"._If data is not available for all IDs (is_success=false):_ "No tickets were found."**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Ticket Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Ticket Details **Table Columns:**

  * Number: ticketNumber
  * Status: status Subject: subject
  * Created Time: createdTime
  * Resolution: resolution
  * Email: email
  * Contact: {firstName} + {lastName}

| General  
  
### Mark Ticket As Spam

#### Description

Mark ticket as spam in Zoho Desk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Specify the ID of the ticket that needs to be marked as spam.  
Mark Contact | Checkbox | Checked | No | If enabled, the contact that created the ticket is marked as spammer.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail** **nor stop a playbook** **execution:**_If the 200 status code is reported (is_success = true):_ "Successfully marked a ticket as spam in Zoho Desk.**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Mark Ticket As Spam". Reason: {0}''.format(error.Stacktrace)_If errors are reported:_ "Error executing action "Mark Ticket As Spam". Reason: {errors/errorMessage} | General  
  
### Ping

#### Description

Test connectivity to Zoho Desk with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:******_If successful (is_success=true):_ ****"Successfully connected to the Zoho Desk server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful (is_success= false):****_"Failed to connect to the Zoho Desk server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Ticket

#### Description

Update a ticket in Zoho Desk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Specify the ID of the ticket that needs to be updated.  
Title | String | N/A | No | Specify the title that should be set for the ticket.  
Description | String | N/A | No | Specify the description for the ticket.  
Department Name | String | N/A | No | Specify the name of the department that should be set for the ticket.  
Contact | String | N/A | No | Specify the email of the contact for the ticket.  
Assignee Type | DDL | Select One Possible values:

  * Select One
  * Agent
  * Team

| No | Specify the type of the assignee. If "Agent" or "Team" is selected, the "Assignee Name" parameter is required.  
Assignee Name | String | N/A | No | Specify the name of the assignee for the ticket. For the agent type you can provide an email address or display name.  
Resolution | String | N/A | No | Specify the resolution for the ticket.  
Priority | DDL | Select OnePossible Values:

  * Select One
  * No Priority
  * Low
  * Medium
  * High

| No | Specify the priority for the ticket.  
Status | DDL | Select OnePossible Values:

  * Select One
  * Open
  * On Hold
  * Escalated
  * Closed

| No | Specify the status for the ticket.  
Mark State | DDL | Select OnePossible values:

  * Select One
  * Read
  * Unread

| No | Specify the mark state for the ticket.  
Classification | DDL | Select OnePossible Values:

  * Select One
  * No Classification
  * Question
  * Problem
  * Feature
  * Others

| No | Specify the classification type for the ticket.  
Channel | DDL | Select OnePossible Values:

  * Select One
  * Email
  * Phone
  * Web
  * Twitter
  * Facebook
  * Chat
  * Forums

| No | Specify the channel for the ticket.  
Category | String | N/A | No | Specify the category for the ticket.  
Sub Category | String | N/A | No | Specify the subcategory for the ticket.  
Due Date | String | N/A | No | Specify the due date for the ticket. Format: ISO 8601. Example: 2022-07-06T07:05:43Z. **Note:** This parameter doesn't have an impact, when the "On Hold" status is set.  
Custom Fields | JSON | N/A | No | Specify a JSON object containing the custom fields that need to be updated. **Note:** You need to provide the API names of the keys.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "modifiedTime": "2022-07-01T11:00:33.000Z",
        "subCategory": null,
        "statusType": "On Hold",
        "subject": "Here's your first ticket.",
        "dueDate": null,
        "departmentId": "97709000000007061",
        "channel": "Chat",
        "onholdTime": "2022-07-01T09:32:14.717Z",
        "language": "English",
        "source": {
            "appName": null,
            "extId": null,
            "permalink": null,
            "type": "SYSTEM",
            "appPhotoURL": null
        },
        "resolution": "Koko",
        "sharedDepartments": [],
        "closedTime": null,
        "approvalCount": "0",
        "isOverDue": true,
        "isTrashed": false,
        "createdTime": "2022-06-27T17:02:17.000Z",
        "id": "97709000000160077",
        "isResponseOverdue": false,
        "customerResponseTime": "2022-06-27T17:02:17.000Z",
        "productId": null,
        "contactId": "97709000000160029",
        "threadCount": "1",
        "secondaryContacts": [],
        "priority": null,
        "classification": null,
        "commentCount": "1",
        "taskCount": "0",
        "accountId": "97709000000160001",
        "phone": "1 888 900 9646",
        "webUrl": "https://desk.zoho.eu/support/siemplify/ShowHomePage.do#Cases/dv/97709000000160077",
        "isSpam": false,
        "status": "On Hold",
        "entitySkills": [],
        "ticketNumber": "101",
        "customFields": {},
        "isArchived": false,
        "description": "Hello<",
        "timeEntryCount": "0",
        "channelRelatedInfo": null,
        "responseDueDate": null,
        "isDeleted": false,
        "modifiedBy": "97709000000092001",
        "email": "support@zohosupport.com",
        "layoutDetails": {
            "id": "97709000000023011",
            "layoutName": "Siemplify"
        },
        "channelCode": null,
        "cf": {},
        "slaId": null,
        "layoutId": "97709000000023011",
        "assigneeId": null,
        "teamId": "97709000000182001",
        "attachmentCount": "0",
        "isEscalated": false,
        "category": null
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the 200 status code is reported (is_success = true):_ "Successfully updated ticket with ID {ticket id} in Zoho Desk.".**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Update Ticket". Reason: {0}''.format(error.Stacktrace) _If the agent is not found:_ "Error executing action "Update Ticket". Reason: agent {agent_name} wasn't found in Zoho Desk. Please check the spelling."'_If the team is not found:_ "Error executing action "Update Ticket". Reason: team {team_name} wasn't found in Zoho Desk. Please check the spelling."_If the department is not found:_ "Error executing action "Update Ticket". Reason: department {department} wasn't found in Zoho Desk. Please check the spelling."'_If the contact is not found:_ "Error executing action "Update Ticket". Reason: contact {contact} wasn't found in Zoho Desk. Please check the spelling."_If the product is not found:_ "Error executing action "Update Ticket". Reason: product {product} wasn't found in Zoho Desk. Please check the spelling."_If "Agent" or "Team" is selected, but the "Assignee Name" parameter is not provided:_ "Error executing action "Update Ticket". Reason: "Assignee Name" needs to be provided." | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
