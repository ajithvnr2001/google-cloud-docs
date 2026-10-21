---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/appsheet/
title: Integrate AppSheet with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:41.113018+00:00
---

# Integrate AppSheet with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/appsheet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AppSheet with Google SecOps

This document explains how to integrate AppSheet with Google Security Operations (Google SecOps).

## Use Cases

Perform CRUD actions.

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.appsheet.com | Yes | API root of the AppSheet instance.  
App ID | String | N/A | Yes | ID of the AppSheet application.  
Access Token | Password | N/A | Yes | Access Token of the AppSheet application.  
Verify SSL | Checkbox | Checked | Yes | If selected, the integration validates the SSL certificate when connecting to the AppSheet server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Record

Add a record to a table in AppSheet.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Table Name | String | N/A | Yes | Specify the name of the table to which you want to add a new record.  
Record JSON Object | JSON |  | Yes | Specify the JSON object of the record that needs to be added.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success = true):_ "Successfully added new record in table "{table}" in AppSheet. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Record". Reason: {0}''.format(error.Stacktrace) _If no data in response:_ "Error executing action "Add Record". Reason: Invalid payload was provided. Please check the spelling of Table Name and structure of the JSON object of the record.' _If "Message" in the response:_ "Error executing action "Add Record". Reason: {0}''.format(Message) _Invalid JSON object:_ Error executing action "Add Record". Reason: Invalid JSON object provided. Please check the structure. | General  
  
### Delete Record

Delete a record in a table in AppSheet.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Table Name | String | N/A | Yes | Specify the name of the table in which you want to delete a record.  
Record JSON Object | JSON |  | Yes | Specify the JSON object of the record that needs to be deleted. You only need to provide the unique identifier key of the record.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success = true):_ "Successfully deleted record in table "{table}" in AppSheet. _If status code 200, but rowNumber is null (is_success=true):_ Provided record didn't exist in table "{table}" in AppSheet. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Delete Record". Reason: {0}''.format(error.Stacktrace) _If no data in response:_ "Error executing action "Delete Record". Reason: Invalid payload was provided. Please check the spelling of Table Name and structure of the JSON object of the record.' _If "Message" in the response:_ "Error executing action "Delete Record". Reason: {0}''.format(Message) Error executing action "Delete Record". Reason: Invalid JSON object provided. Please check the structure. | General  
  
### List Tables

List available tables in an app in AppSheet.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | Equal Possible values:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Tables To Return | Integer | 50 | No | Specify how many tables to return. Default: 50.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON result
    
    
    {
        "Tables": [
            {
                "name": "Hash identificiation",
                "id": "Hash identificiation"
            }
        ]
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If found results (is_success = true):_ "Successfully found tables for the provided criteria in AppSheet. _If not found results (is_success = true):_ "No tables were found for the provided criteria in AppSheet. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Tables". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** Available Tables **Columns:**

  * ID
  * Name

| General  
  
### Ping

Test the connectivity to AppSheet.

#### Parameters

None.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the AppSheet server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the AppSheet server! Error is {0}".format(exception.stacktrace) | General  
  
### Search Records

Search records in a table in AppSheet.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Table Name | String | N/A | Yes | Specify the name of the table for which you want to retrieve details.  
Selector Query | String | N/A | No | Specify the selector query, which will be used to limit results. If nothing is provided, action will return all records.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success = true):_ "Successfully retrieved records based on the provided criteria from table "{table}" in AppSheet. _If no data is available (is_success=false):_ No records were found based on the provided criteria in table "{table}" in AppSheet. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Search Records". Reason: {0}''.format(error.Stacktrace) _If "Message" in the response:_ "Error executing action "Search Records". Reason: {0}''.format(Message) | General  
Case Wall Table | **Name:** Records | General  
  
### Update Record

Update a record in a table in AppSheet.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Table Name | String | N/A | Yes | Specify the name of the table in which you want to update a record.  
Record JSON Object | JSON |  | Yes | Specify the JSON object of the record that needs to be updated. You need to provide the unique identifier key and fields that you want to update.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success = true):_ "Successfully updated record in table "{table}" in AppSheet. **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to server, other:_ "Error executing action "Update Record". Reason: {0}''.format(error.Stacktrace) _If no data in response:_ "Error executing action "Update Record". Reason: Invalid payload was provided. Please check the spelling of Table Name and structure of the JSON object of the record.' _If "Message" in the response:_ "Error executing action "Update Record". Reason: {0}''.format(Message) Error executing action "Update Record". Reason: Invalid JSON object provided. Please check the structure. | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
