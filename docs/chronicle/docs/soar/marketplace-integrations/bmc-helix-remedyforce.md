---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bmc-helix-remedyforce/
title: BMC Helix Remedyforce \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:56.805661+00:00
---

# BMC Helix Remedyforce  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bmc-helix-remedyforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BMC Helix Remedyforce

This document describes how to integrate BMC Helix Remedyforce with Google Security Operations.

## Use Cases

  1. Perform ingestion of the Incidents
  2. Perform triaging action (Update/Create/Delete Records)



## How to configure OAuth authentication

Sometimes the basic authentication method using username + password will not work. This can happen, when MFA is enabled for the account. In those situations, you need to configure OAuth authentication.

**Steps:**

  1. Navigate to Setup -> App Manager.
  2. Press on the "New Connected App" button.
  3. Provide "Connected App Name", "API Name", "Contact Email".
  4. "Enable OAuth Settings" should be set to true.
  5. Set "Callback URL" to "https://localhost".
  6. Add "**full** " and "**refresh_token** " scopes. Both of them are needed to access the API.
  7. Save the app.
  8. Open the app configuration and copy "Consumer Key" and "Consumer Secret". "Consumer Key" is "Client ID" and "Consumer Secret" is Client Secret in the integration configuration.
  9. Go to action "Get OAuth Authorization Code". "Redirect URL" is "Callback URL".
  10. Execute action. In the JSON result you will have an authorization URL. You need to copy and paste it in your browser. In the end you will be redirected and your URL will look like this: "<https://localhost/?code=aPrxyeILZDvX2Hhmz2gymvtuE4aow6hMnAKw_98FyXJvaN7l69bJZFr1z.ylZ3qXd0KZlXjn0g%3D%3D>". You need to copy everything after "code=" and make sure to perform URL decoding. %3D is a "=" character.
  11. Go to action "Get OAuth Refresh Token". "Redirect URL" is "Callback URL" and "Authorization Code" is the "code" from the previous request.
  12. If everything was done correctly, you will see in the JSON result "refresh_token".
  13. Copy this refresh token into integration configuration and perform a test run.



## Configure BMC Helix Remedyforce integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{{yourinstance}}.my.salesforce.com | Yes | API root of the BMC Helix Remedyforce instance.  
Username | String | N/A | No | BMC Helix Remedyforce username.  
Password | Password | N/A | No | BMC Helix Remedyforce password.  
Client ID | String | N/A | No | BMC Helix Remedyforce client ID of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.  
Client Secret | Password | N/A | No | BMC Helix Remedyforce client secret of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.  
Refresh Token | Password | N/A | No | Refresh token for the OAuth authorization.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the BMC Helix Remedyforce server is valid.  
Login API Root | String | https://login.salesforce.com | Yes | API root that is used to authenticate in BMC Helix Remedyforce.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Create Record

#### Description

Create a record in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify the type of the record that needs to be created. If you don't know what kind of records are available, please execute action "List Record Types".  
Record Payload | JSON | {"field":"value"} | Yes | Specify a JSON object containing all of the needed fields and values.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "id": "0015e000005dVbKAAU",
        "success": true,
        "errors": []
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if 201 (is_success = true):** "Successfully created {record type} record in BMC Helix Remedyforce.". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Create Record". Reason: {0}''.format(error.Stacktrace) **If 400:** "Error executing action "Create Record". Reason: {message}. **If record type wasn't found:** Error executing action "Create Record". Reason: {Record Type} wasn't found in BMC Helix Remedyforce. Please use the action "List Record Types" to get a list of available record types. **If invalid JSON payload:** "Error executing action "Create Record". Reason: Invalid JSON payload provided in the parameter "Record Payload". Please check the structure. | General  
  
### Delete Record

#### Description

Delete a record in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify the type of the record that needs to be deleted. If you don't know what kind of records are available, please execute action "List Record Types".  
Record ID | String | N/A | Yes | Specify the id of the record that needs to be deleted.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if 204 (is_success = true):** "Successfully deleted {Record Type} record with ID {record id} in BMC Helix Remedyforce. **If 404 (is_success=true):** "{Record Type} Record with ID {record id} doesn't exist in BMC Helix Remedyforce. **The action should fail and stop a playbook execution:** **if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Record". Reason: {0}''.format(error.Stacktrace) **If record type wasn't found:** Error executing action "Delete Record". Reason: {Record Type} wasn't found in BMC Helix Remedyforce. Please use the action "List Record Types" to get a list of available record types. | General  
  
### Execute Custom Query

#### Description

Execute a custom SOQL query in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
SOQL Query | String | N/A | Yes | Specify what query should be executed.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "attributes": {
            "type": "BMCServiceDesk__Incident__c",
            "url": "/services/data/v51.0/sobjects/BMCServiceDesk__Incident__c/a2U5e000000kl6NEAQ"
        },
        "Id": "a2U5e000000kl6NEAQ",
        "OwnerId": "00G5e000001mqf7EAA",
        "IsDeleted": false,
        "Name": "00000002",
        "CreatedDate": "2021-05-10T19:00:26.000+0000",
        "CreatedById": "0055e000001zFloAAE",
        "LastModifiedDate": "2021-05-10T19:00:26.000+0000",
        "LastModifiedById": "0055e000001zFloAAE",
        "SystemModstamp": "2021-05-10T19:00:26.000+0000",
        "LastActivityDate": null,
        "LastViewedDate": "2021-05-14T10:26:38.000+0000",
        "LastReferencedDate": "2021-05-14T10:26:38.000+0000",
        "BMCServiceDesk__ACApprovalStatus__c": null,
        "BMCServiceDesk__ACSeverity__c": null,
        "BMCServiceDesk__Actual_Outage_Time_Hours__c": 0.0,
        "BMCServiceDesk__Additional_email_information__c": null,
        "BMCServiceDesk__AllTaskCloseController__c": false,
        "BMCServiceDesk__Approved__c": false,
        "BMCServiceDesk__BLANK__c": null,
        "BMCServiceDesk__Category_ID__c": "Hardware",
        "BMCServiceDesk__RecurringParentRecordId__c": null,
        "BMCServiceDesk__RequestDetailCloneId__c": null,
        "BMCServiceDesk__VIP_Client__c": "-",
        "BMCServiceDesk__WorkflowController__c": null,
        "BMCServiceDesk__actualDuration__c": null,
        "BMCServiceDesk__actualOutageDuration__c": null,
        "BMCServiceDesk__call__c": 1.0,
        "BMCServiceDesk__clientEmail__c": "bmcremedyforcetrial@example.com",
        "BMCServiceDesk__Deep_View__c": "<a href=\"/apex/BMCServiceDesk__DeepView?id=a2U5e000000kl6N\" target=\"_blank\"><img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/deep-view.png\" alt=\" \" style=\"height:18px; width:18px;\" border=\"0\"/></a>",
        "BMCServiceDesk__RF_TimeToClose__c": null,
        "BMCServiceDesk__RF_FKLayout__c": null,
        "BMCServiceDesk__RF_LTEC__c": null,
        "BMCServiceDesk__RF_SkipTriggerExecution__c": false,
        "BMCServiceDesk__Categorization_Mode__c": null,
        "BMCServiceDesk__RF_Attachments__c": null,
        "BMCServiceDesk__RF_HasAttachments__c": null,
        "BMCServiceDesk__RF_IntegrationData__c": null
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if found at least one (is_success = true):** "Successfully returned results for the query "{query}" in BMC Helix Remedyforce. **If nothing was found(is_success=true):** "No results were found for the query "{query}" in BMC Helix Remedyforce" **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Custom Query". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Results | General  
  
### Execute Simple Query

#### Description

Execute a SOQL query based on parameters in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify what record type should be queried.  
Where Filter | String | N/A | No | Specify the WHERE filter for the query that needs to be executed. Note: You don't need to provide time filter, limiting and sorting. Also, you don't need to provide WHERE string in the payload.  
Time Frame | DDL | Last Hour Possible Values: Last Hour Last 6 Hours Last 24 Hours Last Week Last Month Custom | No | Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.  
Fields To Return | CSV | N/A | No | Specify what fields to return. If nothing is provided action will return all fields.  
Sort Field | String | CreatedDate | No | Specify what parameter should be used for sorting.  
Sort Order | DDL | ASC Possible Values: ASC DESC | No | Specify the order of sorting.  
Max Results To Return | Integer | 50 | No | Specify how many results to return. Default: 50. Maximum is 200.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "attributes": {
            "type": "BMCServiceDesk__Incident__c",
            "url": "/services/data/v51.0/sobjects/BMCServiceDesk__Incident__c/a2U5e000000kl6NEAQ"
        },
        "Id": "a2U5e000000kl6NEAQ",
        "OwnerId": "00G5e000001mqf7EAA",
        "IsDeleted": false,
        "Name": "00000002",
        "CreatedDate": "2021-05-10T19:00:26.000+0000",
        "CreatedById": "0055e000001zFloAAE",
        "LastModifiedDate": "2021-05-10T19:00:26.000+0000",
        "LastModifiedById": "0055e000001zFloAAE",
        "SystemModstamp": "2021-05-10T19:00:26.000+0000",
        "LastActivityDate": null,
        "LastViewedDate": "2021-05-14T10:26:38.000+0000",
        "LastReferencedDate": "2021-05-14T10:26:38.000+0000",
        "BMCServiceDesk__ACApprovalStatus__c": null,
        "BMCServiceDesk__ACSeverity__c": null,
        "BMCServiceDesk__Actual_Outage_Time_Hours__c": 0.0,
        "BMCServiceDesk__Additional_email_information__c": null,
        "BMCServiceDesk__AllTaskCloseController__c": false,
        "BMCServiceDesk__Approved__c": false,
        "BMCServiceDesk__BLANK__c": null,
        "BMCServiceDesk__Category_ID__c": "Hardware",
        "BMCServiceDesk__RecurringParentRecordId__c": null,
        "BMCServiceDesk__RequestDetailCloneId__c": null,
        "BMCServiceDesk__VIP_Client__c": "-",
        "BMCServiceDesk__WorkflowController__c": null,
        "BMCServiceDesk__actualDuration__c": null,
        "BMCServiceDesk__actualOutageDuration__c": null,
        "BMCServiceDesk__call__c": 1.0,
        "BMCServiceDesk__clientEmail__c": "bmcremedyforcetrial@example.com",
        "BMCServiceDesk__Deep_View__c": "<a href=\"/apex/BMCServiceDesk__DeepView?id=a2U5e000000kl6N\" target=\"_blank\"><img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/deep-view.png\" alt=\" \" style=\"height:18px; width:18px;\" border=\"0\"/></a>",
        "BMCServiceDesk__RF_TimeToClose__c": null,
        "BMCServiceDesk__RF_FKLayout__c": null,
        "BMCServiceDesk__RF_LTEC__c": null,
        "BMCServiceDesk__RF_SkipTriggerExecution__c": false,
        "BMCServiceDesk__Categorization_Mode__c": null,
        "BMCServiceDesk__RF_Attachments__c": null,
        "BMCServiceDesk__RF_HasAttachments__c": null,
        "BMCServiceDesk__RF_IntegrationData__c": null
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if found at least one (is_success = true):** "Successfully returned results for the query "{query}" in BMC Helix Remedyforce. **If nothing was found(is_success=true):** "No results were found for the query "{query}" in BMC Helix Remedyforce" **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Simple Query". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Results | General  
  
### Get Record Details

#### Description

Get detailed information about the record from BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify the type of the record for which you want to retrieve details. If you don't know what kind of records are available, please execute action "List Record Types".  
Record IDs | CSV | N/A | Yes | Specify the ids of records for which you want to return details.  
Fields To Return | CSV | N/A | No | Specify what fields to return. If none of the provided fields were found, action will fail. If nothing is provided, action will return all fields.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "attributes": {
            "type": "BMCServiceDesk__Incident__c",
            "url": "/services/data/v51.0/sobjects/BMCServiceDesk__Incident__c/a2U5e000000kl6NEAQ"
        },
        "Id": "a2U5e000000kl6NEAQ",
        "OwnerId": "00G5e000001mqf7EAA",
        "IsDeleted": false,
        "Name": "00000002",
        "CreatedDate": "2021-05-10T19:00:26.000+0000",
        "CreatedById": "0055e000001zFloAAE",
        "LastModifiedDate": "2021-05-10T19:00:26.000+0000",
        "LastModifiedById": "0055e000001zFloAAE",
        "BMCServiceDesk__Total_Duration__c": 0.0,
        "BMCServiceDesk__Incorrect_category__c": false,
        "Client_VIP__c": false,
        "BMCServiceDesk__Incorrect_owner__c": false,
        "BMCServiceDesk__LockedRecordTimestamp__c": null,
        "BMCServiceDesk__Queue__c": "Incident Queue",
        "BMCServiceDesk__Reassigned_Count__c": null,
        "BMCServiceDesk__isServiceRequest__c": false,
        "BMCServiceDesk__Approval_Status__c": null,
        "Alternate_Contact_Name__c": null,
        "Alternate_Contact_Number__c": null,
        "Client_Phone__c": null,
        "External_Ticket_Ref__c": null,
        "Affected_Application__c": null,
        "Affected_Hardware__c": null,
        "BMCServiceDesk__Deep_View__c": "<a href=\"/apex/BMCServiceDesk__DeepView?id=a2U5e000000kl6N\" target=\"_blank\"><img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/deep-view.png\" alt=\" \" style=\"height:18px; width:18px;\" border=\"0\"/></a>",
        "BMCServiceDesk__RF_TimeToClose__c": null,
        "BMCServiceDesk__RF_FKLayout__c": null,
        "BMCServiceDesk__RF_LTEC__c": null,
        "BMCServiceDesk__RF_SkipTriggerExecution__c": false,
        "BMCServiceDesk__Categorization_Mode__c": null,
        "BMCServiceDesk__RF_Attachments__c": null,
        "BMCServiceDesk__RF_HasAttachments__c": null,
        "BMCServiceDesk__RF_IntegrationData__c": null
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data is available for at least one id(is_success = true):** "Successfully returned details regarding record type {Record Type} for the following ids: {record ids}". **If data is not available for at least one id (is_success=true):** "Action wasn't able to find details regarding record type {Record Type} for the following ids: {record ids}". **If data is not available for all (is_success=false):** No records were found. **The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Record Details". Reason: {0}''.format(error.Stacktrace) **If record type wasn't found:** Error executing action "Get Record Details". Reason: {Record Type} wasn't found in BMC Helix Remedyforce. Please use the action "List Record Types" to get a list of available record types. **If none of the fields provided in "Fields To Return" were found:** "Error executing action "Get Record Details". Reason: none of the provided fields were found. Please check the spelling.'' | General  
Case Wall Table | **Name:** Record {record Id}Details **Columns:** Key Value | General  
  
### Get OAuth Authorization Code

#### Description

Generate an OAuth authorization code in BMC Helix Remedyforce. Please refer to the documentation portal for more information.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Redirect URL | String | https://localhost | Yes | Specify the redirect URL that was used when the "Connector App" was created.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** "Successfully generated Authorization code URL in BMC Helix Remedyforce. Please copy paste it in the browser. After that, copy the "code" part from the URL. This authorization code is used in action "Get OAuth Refresh Token." | General  
Link | **Name:** Authorization Code Link   
**URL:** {generated link} |   
  
### Get OAuth Refresh Token

#### Description

Generate the refresh token that is needed for the integration configuration. Authorization code can be generated using "Get OAuth Authorization Code". Please refer to the documentation portal for more information.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Redirect URL | String | https://localhost | Yes | Specify the redirect URL that was used when the "Connector App" was created.  
Authorization Code | String | N/A | Yes | Specify the authorization code from action "Get OAuth Authorization Code".  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "access_token": "00D090000083B1p!ARkAQHJhzO.oDwNuldyoWlNDlLV9805VyWlZmcBvMF7qetVGpQWXi6pND0riSCiFs4fnrxmuVjBv.Io..ooN_JAIlGdGT_Gk",
        "signature": "6+xAwCccuYI0ivDbXtZzlguynNuKGRHaj+HpyZXM6ms=",
        "scope": "refresh_token api full",
        "instance_url": "https://202107220535170700.my.salesforce.com",
        "id": "https://login.salesforce.com/id/00D090000083B1pEAE/00509000007hMVJAA2",
        "token_type": "Bearer",
        "issued_at": "1626958668640"
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if 200 (is_success = true):** "Successfully generated refresh token in BMC Helix Remedyforce.". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get OAuth Refresh Token". Reason: {0}''.format(error.Stacktrace) **If non 200 status code:** "Error executing action "Get OAuth Refresh Token". Reason: {0}''.format(error_description) | General  
  
### List Record Types

#### Description

List available record types from BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | Equal DDL Equal Contains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among record types and if "Contains" is selected, action will try to find record types that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Record Types To Return | Integer | 50 | No | Specify how many record types to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if found at least one (is_success = true):** "Successfully listed available record types based on the provided criteria in BMC Helix Remedyforce. **If nothing was found(is_success=true):** "No record types were found based on the provided criteria in BMC Helix Remedyforce" **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Record Types". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Available Record Types **Columns:** Name Label Custom  | General  
  
### Ping

#### Description

Test connectivity to BMC Helix Remedyforce with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** "Successfully connected to the BMC Helix Remedyforce server with the provided connection parameters!" **The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to connect to the BMC Helix Remedyforce server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Record

#### Description

Update record in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify the type of the record that needs to be updated. If you don't know what kind of records are available, please execute action "List Record Types".  
Record ID | String | N/A | Yes | Specify the id of the record that needs to be updated.  
Fields To Update | JSON | {"field":"value"} | Yes | Specify a JSON object containing all of the needed fields and values that need to be updated.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if 204 (is_success = true):** "Successfully updated {record type} record with {record id} in BMC Helix Remedyforce.". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Update Record". Reason: {0}''.format(error.Stacktrace) **If 404 or 400:** "Error executing action "Update Record". Reason: {message}. **If record type wasn't found:** Error executing action "Update Record". Reason: {Record Type} wasn't found in BMC Helix Remedyforce. Please use the action "List Record Types" to get a list of available record types. **If invalid JSON payload:** "Error executing action "Update Record". Reason: Invalid JSON payload provided in the parameter "Fields To Update". Please check the structure. | General  
  
### Wait For Fields Update

#### Description

Wait for fields update in BMC Helix Remedyforce.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record Type | String | N/A | Yes | Specify the type of the record for which you are waiting an update. If you don't know what kind of records are available, please execute action "List Record Types".  
Record ID | String | N/A | Yes | Specify the ID of the record that needs to be updated.  
Fields To Check | JSON | {"field":"value"} | Yes | Specify a JSON object containing all of the needed fields and values.  
Fail If Timeout | Checkbox | Checked | Yes | If enabled, action will be failed, if not all of the fields were updated.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "attributes": {
            "type": "BMCServiceDesk__Incident__c",
            "url": "/services/data/v51.0/sobjects/BMCServiceDesk__Incident__c/a2U5e000000kl6NEAQ"
        },
        "Id": "a2U5e000000kl6NEAQ",
        "BMCServiceDesk__FKImpact__c": "a2M5e000000l1HxEAI",
        "BMCServiceDesk__FKIncident__c": null,
        "BMCServiceDesk__FKLead__c": null,
        "BMCServiceDesk__FKOpenBy__c": "0055e000001zFloAAE",
        "BMCServiceDesk__FKPriority__c": "a2h5e000000nHTnAAM",
        "BMCServiceDesk__FKRequestDefinition__c": null,
        "BMCServiceDesk__FKRequestDetail__c": null,
        "BMCServiceDesk__FKServiceOffering__c": null,
        "BMCServiceDesk__FKStatus__c": "a3w5e000000U1xcAAC",
        "BMCServiceDesk__FKTemplate__c": null,
        "BMCServiceDesk__actualOutageDuration__c": null,
        "BMCServiceDesk__call__c": 1.0,
        "Client_VIP__c": false,
        "BMCServiceDesk__Incorrect_owner__c": false,
        "BMCServiceDesk__LockedRecordTimestamp__c": null,
        "BMCServiceDesk__Queue__c": "Incident Queue",
        "BMCServiceDesk__Reassigned_Count__c": null,
        "BMCServiceDesk__isServiceRequest__c": false,
        "BMCServiceDesk__Approval_Status__c": null,
        "Alternate_Contact_Name__c": null,
        "Alternate_Contact_Number__c": null,
        "Client_Phone__c": null,
        "External_Ticket_Ref__c": null,
        "Affected_Application__c": null,
        "Affected_Hardware__c": null,
        "BMCServiceDesk__Deep_View__c": "<a href=\"/apex/BMCServiceDesk__DeepView?id=a2U5e000000kl6N\" target=\"_blank\"><img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/deep-view.png\" alt=\" \" style=\"height:18px; width:18px;\" border=\"0\"/></a>",
        "BMCServiceDesk__RF_TimeToClose__c": null,
        "BMCServiceDesk__RF_FKLayout__c": null,
        "BMCServiceDesk__RF_LTEC__c": null,
        "BMCServiceDesk__RF_SkipTriggerExecution__c": false,
        "BMCServiceDesk__Categorization_Mode__c": null,
        "BMCServiceDesk__RF_Attachments__c": null,
        "BMCServiceDesk__RF_HasAttachments__c": null,
        "BMCServiceDesk__RF_IntegrationData__c": null
    }
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if 201 (is_success = true):** "{record type} record with ID {record id} was updated in BMC Helix Remedyforce.". **If one of the fields were not updated and Fail if timeout is not enabled (is_success=false):** "The following fields were not updated for {record type} record with ID {record id} in BMC Helix Remedyforce: {fields that were not updated}" **Async Message:** Waiting for the following fields to be updated for {record type} record with ID {record id} in BMC Helix Remedyforce: {fields that were not updated} **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Wait For Fields Update". Reason: {0}''.format(error.Stacktrace) **If some fields were not found:** "Error executing action "Wait For Fields Update". Reason: the following fields were not found in the structure of record: {fields that were not found}. **If record type wasn't found:** Error executing action "Wait For Fields Update". Reason: {Record Type} wasn't found in BMC Helix Remedyforce. Please use the action "List Record Types" to get a list of available record types. **If one of the fields were not updated and Fail if timeout is enabled (is_success=false):** "Error executing action "Wait For Fields Update". Reason: The following fields were not updated for {record type} record with ID {record id} in BMC Helix Remedyforce: {fields that were not updated}" **If invalid JSON payload:** "Error executing action "Wait For Fields Update". Reason: Invalid JSON payload provided in the parameter "Fields To Check". Please check the structure. | General  
  
## Connector

### BMC Helix Remedyforce - Incidents Connector

#### Description

Pull information about incidents from BMC Helix Remedyforce.

#### Configure BMC Helix Remedyforce - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | BMCServiceDesk__Type__c | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{{yourinstance}}.my.salesforce.com | Yes | API root of the BMC Helix Remedyforce instance.  
Username | String | N/A | Yes | BMC Helix Remedyforce username.  
Password | Password | N/A | Yes | BMC Helix Remedyforce password.  
Lowest Priority To Fetch | Integer | 5 | No | Lowest priority that will be used to fetch incidents. Maximum: 5. Minimum: 1. If nothing is provided, the connector will ingest all incidents.  
Ingest Empty Priority Incidents | Checkbox | Checked | No | If enabled, the connector will fetch incidents that don't have priority. Google SecOps Alerts created in this manner will have priority set to 'Informational'  
Type Filter | CSV | Incident,Service Request | No | Type filter for the incidents. If nothing is provided, the connector will ingest all incidents. Example: Incident, Service Request.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch incidents.  
Max Incidents To Fetch | Integer | 10 | No | How many incidents to process per one connector iteration. Maximum is 200.  
Use whitelist as a blacklist | Checkbox | Checked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the BMC Helix Remedyforce server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Client ID | String | N/A | No | BMC Helix Remedyforce client ID of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.  
Client Secret | Password | N/A | No | BMC Helix Remedyforce client secret of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.  
Login API Root | String | https://login.salesforce.com | Yes | API root that is used to authenticate in BMC Helix Remedyforce.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
