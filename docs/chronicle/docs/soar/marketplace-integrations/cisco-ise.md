---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-ise/
title: Cisco ISE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:05.142823+00:00
---

# Cisco ISE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-ise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco ISE

This document describes how to integrate Cisco ISE with Google Security Operations.

## Configure Cisco ISE to work with Google Security Operations

To enable External RESTful Services (ERS) and create a Cisco ISE service account to use for connecting to API, see the [Cisco ISE documentation](https://developer.cisco.com/docs/identity-services-engine/3.0/#!setting-up/enable-ers-port-9060). Sometimes you need to log into the Cisco ISE UI with the service account first, and then the API or Google SecOps integration starts working properly using the same credentials that were failing previously.

## Configure Cisco ISE integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Enrich Endpoint

#### Description

Enrich endpoint by data from Cisco ISE.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get Endpoints

#### Description

Get requested endpoint data from the endpoints monitored by Cisco ISE.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get Sessions

#### Description

Get a list of active sessions.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Quarantine Address

#### Description

Quarantine an endpoint by MAC address.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Policy name to attach the endpoint to.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Terminate Session

#### Description

Session disconnect through an API call.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Node Server Name | String | N/A | Yes | ISE node server name.  Example: ciscoISE  
Calling Station ID | String | N/A | Yes | The ID value of the calling station. Example: 1  
Terminate Type | String | N/A | No | Terminate Type value is an integer between 0 and 2.Example: 0 Possible Values:

  * 0=DYNAMIC_AUTHZ_PORT_DEFAULT
  * 1=DYNAMIC_AUTHZ_PORT_BOUNCE
  * 2=DYNAMIC_AUTHZ_PORT_SHUTDOWN

  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Unquarantine Address

#### Description

Unquarantine endpoint by MAC address.

#### Parameters

N/A

#### Run On

This action runs on the Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Update Endpoint

#### Description

Update an endpoint object.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Description | String | N/A | No | Endpoint's description  
Group ID | String | N/A | No | Endpoint's property to update.  
Portal User | String | N/A | No | Endpoint's property to update.  
Identity Store | String | N/A | No | Endpoint's property to update.  
Identity Store ID | String | N/A | No | Endpoint's property to update.  
Custom Attributes | String | N/A | No | Custom attributes are added to the entity object.Example: {'param':'val'}  
MDM Server Name | String | N/A | No | Endpoint's property to update.  
MDM Reachable | String | N/A | No | Endpoint's property to update, e.g. true or false.  
MDM Enrolled | String | N/A | No | Endpoint's property to update, e.g. true or false.  
MDM Compliance Status | String | N/A | No | Endpoint's property to update, e.g. true or false.  
MDM OS | String | N/A | No | Endpoint's property to update.  
MDM Manufacturer | String | N/A | No | Endpoint's property to update.  
MDM Model | String | N/A | No | Endpoint's property to update.  
MDM Encrypted | String | N/A | No | Endpoint's property to update.  
MDM Pinlock | String | N/A | No | Endpoint's property to update, e.g. true or false.  
MDM Jail Broken | String | N/A | No | Endpoint's property to update, e.g. true or false.  
MDM IMEI | String | N/A | No | Endpoint's property to update.  
MDM Phone Number | String | N/A | No | Endpoint's property to update.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List Endpoint Identity Group

#### Description

List available endpoint entity groups in Cisco ISE.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select OnePossible Values:

  * Select One
  * Name

| No | Specify the key that needs to be used to filter endpoint entity groups.  
Filter Logic | DDL | Not SpecifiedPossible Values:

  * Not Specified
  * Equal
  * Contains

| No | Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify the value that should be used in the filter.If "Equal" is selected, the action tries to find the exact match among results. If "Contains" is selected, the action tries to find results that contain the specified substring.If nothing is provided in this parameter, the filter is not applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 100 | No | Specify the number of records to return. If nothing is provided, action will return 100 records. Maximum: 100  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "id": "73d1a120-ab0f-11ec-ae96-76398204b317",
            "name": "Windows11-Workstation",
            "description": "Identity Group for Profile: Windows11-Workstation",
        {
            "id": "21fa0600-f947-11eb-953e-0050568fa723",
            "name": "OS_X_BigSur-Workstation",
            "description": "Identity Group for Profile: OS_X_BigSur-Workstation",
        },
        {
            "id": "3b76f840-8c00-11e6-996c-525400b48521",
            "name": "Workstation",
            "description": "Identity Group for Profile: Workstation",
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success=true):_ "Successfully found endpoint entity groups for the provided criteria in Cisco ISE."_If data is not available (is_success=false):_ "No endpoint entity groups were found for the provided criteria in Cisco ISE."_If the "Filter Value" parameter is empty (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value."  
  
**The action should fail and stop a playbook execution:**_If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":_ "Error executing action "List Endpoint Identity Group". Reason: you need to select a field from the "Filter Key" parameter."_If invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "List Endpoint Identity Group". Reason: "Invalid value was provided for "Max Records to Return": . Positive number should be provided."_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "List Endpoint Identity Group". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available Endpoint Entity Groups **Table Columns:**

  * Name - name
  * Description - description

| General  
  
### Add Endpoint To Endpoint Identity Group

#### Description

Add an endpoint to the endpoint identity group in Cisco ISE.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Endpoint Identity Group Name | String | N/A | Yes | Specify the name of the endpoint identity group to which you want to add the endpoint.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "UpdatedFieldsList": {
            "updatedField": [
                {
                    "field": "groupId",
                    "oldValue": "73d1a120-ab0f-11ec-ae96-76398204b317",
                    "newValue": "3b76f840-8c00-11e6-996c-525400b48521"
                }
            ]
        }
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully added the following endpoints to the "{group name}" Endpoint Identity Group in Cisco ISE: {entity.identifier}"._If endpoint is not found (is_success=true):_ "Action wasn't able to find the following endpoints in Cisco ISE: {entity.identifier}"_If all endpoints are not found (is_success=false):_ "None of the provided endpoints were found."**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) _If the group is not found:_ "Error executing action "{action name}". Reason: Endpoint Identity Group "{group name}" wasn't found in Cisco ISE. Please check the spelling." | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
