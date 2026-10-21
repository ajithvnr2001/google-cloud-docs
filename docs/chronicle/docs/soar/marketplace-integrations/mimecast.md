---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mimecast/
title: Mimecast \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:16.684176+00:00
---

# Mimecast  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mimecast/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mimecast

This document provides guidance on how to integrate Mimecast with Google SecOps.

## Use Cases

  1. Perform ingestion of the messages
  2. Perform triaging action (Reject/Release/Report message)



## Before you begin

Before proceeding, ensure your Mimecast environment is prepared with the necessary product licenses and administrative roles.

### Required Mimecast products and services

To ensure the Mimecast API 2.0 integration functions correctly, your Mimecast account must have licenses for the following products:

  * [**Account Management**](https://mimecastsupport.zendesk.com/hc/en-us/articles/34000359768083-Account-Settings)
  * [**Data Retention**](https://mimecastsupport.zendesk.com/hc/en-us/articles/34000390522899-Archiving-Understanding-Data-Retention)
  * [**Email Security Cloud Gateway**](https://www.mimecast.com/products/email-security/secure-email-gateway/)
  * [**Policy Management**](https://developer.services.mimecast.com/docs/policymanagement/1/overview)



### Required Permissions for Mimecast role

To configure the Mimecast integration, you must first create a Mimecast Role with the required permissions in the [Mimecast Administration Console](https://login.mimecast.com/u/login/?gta=apps#/login).

The required permissions are as follows:

  * `Account | Dashboard | Read`

  * `Account | Monitoring | Held | Edit`

  * `Archive | Search Logs | Read`

  * `Archive | View Logs | Read`

  * `Gateway | Managed Senders | Edit`

  * `Gateway | Policies | Edit`

  * `Gateway | Policies | Read`

  * `Gateway | Tracking | Read`




## Configure Mimecast integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

**Note:** Information and guidance on obtaining all necessary configuration parameters (`Application ID`, Keys, and `API Root` URL) is available from the following Mimecast resources:

  * [Managing API Applications](https://community.mimecast.com/s/article/Managing-API-Applications-505230018)
  * [API 1.0 to 2.0 Migration Guide (Includes API Base URLs)](https://developer.services.mimecast.com/api-1-0-to-2-0-migration-guide)



This integration relies on three Mimecast API endpoints that don't have public documentation. These endpoints require Mimecast product entitlements to properly function.

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/<<api root>> | Yes | API root of the Mimecast instance.  
Application ID | String | N/A | Yes | Application ID of the Mimecast instance.  
Application Key | Password | N/A | Yes | Application Key of the Mimecast instance.  
Access Key | Password | N/A | Yes | Access Key of the Mimecast instance.  
Secret Key | Password | N/A | Yes | Secret Key of the Mimecast instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Mimecast server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Mimecast with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the Mimecast server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Mimecast server! Error is {0}".format(exception.stacktrace) | General  
  
### Simple Archive Search

#### Description

Search archive emails using defined parameters in Mimecast.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Fields To Return | CSV | attachmentcount,status,subject,  
size,receiveddate,displayfrom,  
displayfromaddress,id,displayto,  
displaytoaddresslist,smash | Yes | Specify a comma-separated list of fields that needs to be returned.  
Mailboxes | CSV | N/A | No | Specify a comma-separated list of mailboxes that need to be searched.  
From | CSV | N/A | No | Specify a comma-separated list of email addresses from which the emails were sent.  
To | CSV | N/A | No | Specify a comma-separated list of email addresses to which the emails were sent.  
Subject | String | N/A | No | Specify a subject that needs to be searched.  
Time Frame | DDL | Last HourPossible Values:Last HourLast 6 HoursLast 24 HoursLast WeekLast MonthCustom | Yes | Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".  
Start Time | String | N/A | No | Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.  
Max Emails To Return | Integration | 50 | No | Specify how many emails to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available(is_success = true):** "Successfully found archive emails for the provided criteria in Mimecast".  
******If data is not available (is_success=true):** "No archive emails were found for the provided criteria in Mimecast"  
****  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Simple Archive Search". Reason: {0}''.format(error.Stacktrace)******If Start Time is empty, when "Time Frame" is "Custom":** "Error executing action "Simple Archive Search". Reason: "Start Time" should be provided, when "Custom" is selected in "Time Frame" parameter."******If fail/errors has values:** Error executing action "Simple Archive Search". Reason: fail/errors/message".  | General  
Case Wall Table | **Name:** Results**Columns:** All keys from the response | General  
  
### Advanced Archive Search

#### Description

Search archive emails using a custom XML query in Mimecast.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
XML Query | XML | N/A | Yes | Specify an XML query that should be used when searching for archive emails. Please visit documentation for more details.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available(is_success = true):** "Successfully found archive emails for the provided criteria in Mimecast".  
******If data is not available (is_success=true):** "No archive emails were found for the provided criteria in Mimecast".  
****  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Advanced Archive Search". Reason: {0}''.format(error.Stacktrace)  
******If fail/errors has values:** Error executing action "Advanced Archive Search". Reason: fail/errors/message".  | General  
Case Wall Table | **Name:** Results**Columns:** All keys from the response | General  
  
### Reject Message

#### Description

Reject message in Mimecast. Note: Only messages with status "Held" can be rejected.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Message ID | String | N/A | Yes | Specify the ID of the message that needs to be rejected.  
Note | String | N/A | No | Specify an additional note containing an explanation regarding why the message was rejected.  
Reason | DLL | Select OnePossible Values:Select OneInappropriate CommunicationConfidential InformationAgainst Email PolicyRestricted Content | No | Specify the reason for rejection.  
Notify Sender | Checkbox | Unchecked | No | If enabled, action will notify the sender about rejection.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**If no "errors" in the response (is_success = true):** "Successfully rejected message with ID "{ID}" in Mimecast".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Reject Message". Reason: {0}''.format(error.Stacktrace)******If fail/errors has values:** Error executing action "Reject Message". Reason: fail/errors/message".  | General  
  
### Release Message

#### Description

Release message in Mimecast. Note: Only messages with status "Held" can be released.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Message ID | String | N/A | Yes | Specify the ID of the message that needs to be released.  
Release to Sandbox | Checkbox | N/A | No | If enabled, action will release the message to the sandbox.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**If no "errors" in the response (is_success = true):** "Successfully released message with ID "{ID}" in Mimecast".  
****  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Release Message". Reason: {0}''.format(error.Stacktrace)******If fail/errors has values:** Error executing action "Release Message". Reason: fail/errors/message".  | General  
  
### Report Message - Deprecated

**Deprecated:** This action is deprecated and no longer supported. 

Report message in Mimecast.

**Note:** Only messages with status "Held", "Archived", or "Bounced" can be reported. 

#### Action inputs

Parameter | Description  
---|---  
`Message IDs` | Required.Specify the ID of the message that needs to be reported.  
`Report as` | Optional.Specify the report type for the message. The possible values are as follows:

  * `Spam`
  * `Malware`
  * `Phishing`

  
`Comment` | Optional.Specify the comment for the report.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False/is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:**

  * **if data is available (is\\_success = true):** print "Successfully reported the following messages with ID "{ID}" in Mimecast".
  * **If fail/errors has values:** print "Error executing action "Report Message". Reason: fail/errors/message".

**The action should fail and stop a playbook execution:**

  * **if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Report Message". Reason: {0}''.format(error.Stacktrace).

| General  
  
### Block Sender

#### Description

Block sender in Mimecast.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Sender | String | N/A | Yes | Specify the email address of the sender to block.  
Recipient | String | N/A | Yes | Specify the email address of the recipient to block.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:**  
**If no "errors" in the response (is_success = true):** "Successfully blocked sender {sender} for recipient {recipient} in Mimecast".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Block Sender". Reason: {0}''.format(error.Stacktrace)******If fail/errors has values:** Error executing action "Block Sender". Reason: fail/errors/message". | General  
  
### Permit Sender

#### Description

Permit sender in Mimecast.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Sender | String | N/A | Yes | Specify the email address of the sender to permit.  
Recipient | String | N/A | Yes | Specify the email address of the recipient to permit.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**If no "errors" in the response (is_success = true):** "Successfully permitted sender {sender} for recipient {recipient} in Mimecast".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Permit Sender". Reason: {0}''.format(error.Stacktrace)******If fail/errors has values:** Error executing action "Permit Sender". Reason: fail/errors/message". | General  
  
### Create Block Sender Policy

Create a Block Sender policy in Mimecast.

#### Run On

This action doesn't run on any entities.

#### Parameters

Parameter Display Name | Type | Default Value | Watermark | Is Mandatory | Description  
---|---|---|---|---|---  
Response | DDL | N/A | N/A | No | Provide the type of response that will be associated with the created policy.  
Description | String | N/A | N/A | Yes | Description for the policy.  
Extracted Data | DDL | N/A | N/A |  | Define from where the information about sender and recipient should be extracted.  
Sender | String | N/A | N/A | No | From whom the message should be sent for it to be blocked. Only needed if "Sender Type" is one of: Email Domain, Email Address, Header Display Name. This parameter is ignored if a different "From Type" value is selected.  
Sender Type | DDL | N/A | N/A | No | Type of the sender for the policy.  
Recipient | String | N/A | N/A | No | To whom the message should be sent for it to be blocked. Only needed if "Recipient Type" is one of: Email Domain, Email Address, Header Display Name. This parameter is ignored if a different "Recipient Type" value is selected.  
Recipient Type | DDL | N/A | N/A | No | Type of the recipient for the policy.  
Comment | String | N/A | N/A | No | Comment for a policy.  
Bidirectional | Bool | N/A | N/A | No | If enabled, the policy will be defined in a bidirectional way.  
Enforced | Bool | N/A | N/A | No | If enabled, the policy is enforced.  
Start Time | String | N/A | N/A | No | Start time for the policy. If nothing is provided, start time will be set to eternal. Expects ISO 8601 format. Example: 2025-03-07T16:03:00Z  
End Time | String | N/A | N/A | No | End time for the policy. If nothing is provided, end time will be set to eternal. Expects ISO 8601 format. Example: 2025-03-07T16:03:00Z  
  
#### Action Results

Type | Available  
---|---  
Script Result | True  
JSON Result | True  
Enrichment Table | False  
Case Wall Table | False  
Case Wall Link | False  
Case Wall Attachment | False  
  
##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
       "option": "block_sender",
       "id": "eNo1jr0OgjAYAN-lqw79QKyYOCCSiCJGqSCjlmqQn2ILNmp8d3Fwv8vdGynOOsnzDE3RSsP4ZTT0tPUMO3DL1pK-LrFZzzfJ9XJTrC78yPZgcc7CW1QdSLuUo11Mfc2rpIsfxlxQHFsDFXKPdkeq10ym7uJeDIKLA6Z66T1NUklI4c3QEDWizNnzVzYnBthDxDrViopLJjLe77iHyAEgjkmgpx9cqlzUaAp_kz4b7vc2YDzCny9vYUEo",
       "policy": {
           "description": "Description",
           "fromPart": "both",
           "from": {
               "type": "individual_email_address",
               "emailAddress": "example@exampl.com"
           },
           "to": {
               "type": "individual_email_address",
               "emailAddress": "exampleto@exampl.com"
           },
           "fromType": "individual_email_address",
           "fromValue": "example@exampl.com",
           "toType": "individual_email_address",
           "toValue": "exampleto@exampl.com",
           "fromEternal": true,
           "toEternal": true,
           "fromDate": "1900-01-01T00:00:00+0000",
           "toDate": "2100-01-01T23:59:59+0000",
           "override": false,
           "bidirectional": false,
           "conditions": {},
           "enabled": true,
           "enforced": true,
           "createTime": "2025-03-27T12:51:46+0000",
           "lastUpdated": "2025-03-27T12:51:46+0000"
       }
    }
    

##### Case Wall

Result Type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:******  
****_If no "errors" in the response (is_success = true):_ ****print "Successfully created a block sender policy in Mimecast".******The action should fail and stop a playbook execution:** ****_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) _If fail/errors has values:_ Error executing action "{action name}". Reason: fail/errors/message".  
  
## Connector

### Mimecast - Message Tracking Connector

#### Description

Pull information about messages from the "Message Tracking" tab in Mimecast. Note: Whitelist works on the "queueDetailStatus/bounceType" parameter.

#### Configure Mimecast - Message Tracking Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Int | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https:/<<api root>> | Yes | API root of the Mimecast instance.  
Application ID | String | N/A | Yes | Application ID of the Mimecast instance.  
Application Key | Password | N/A | Yes | Application Key of the Mimecast instance.  
Access Key | Password | N/A | Yes | Access Key of the Mimecast instance.  
Secret Key | Password | N/A | Yes | Secret Key of the Mimecast instance.  
Domains | CSV | N/A | Yes | A comma-separated list of domains for which to query messages.  
Lowest Risk To Fetch | String | N/A | No | Lowest risk that will be used to fetch messages. Possible values:Negligible, Low, Medium, High.If nothing is provided, the connector will ingest all messages.  
Status Filter | CSV | held |  | A comma-separated list of status filters for the messages. Possible values: delivery, held, accepted, bounced, deferred, rejected, archived. If nothing is provided, the connector will ingest all messages.  
Route Filter | CSV | N/A |  | A comma-separated route filters for the messages. Possible values: internal, outbound, inbound. If nothing is provided, the connector will ingest all messages.  
Queue Reason Filter | CSV | N/A |  | A comma-separated list of queue reasons that should filter the messages. If nothing is provided, this filter is ignored.  
Ingest Messages Without Risk | Checkbox |  |  | If enabled, the connector will ingest messages even if there is no info about risk. Google SecOps Alerts generated from those messages will have priority set to Informational.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch messages. Default: 1 hour. Max: 30 days.  
Max Messages To Return | Integer | 100 | No | How many messages to process per one connector iteration. Default: 100.  
Use whitelist as a blacklist | Checkbox | Checked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Mimecast server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
