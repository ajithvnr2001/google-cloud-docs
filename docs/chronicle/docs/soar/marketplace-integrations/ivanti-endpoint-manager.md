---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ivanti-endpoint-manager/
title: Ivanti Endpoint Manager \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:40.128782+00:00
---

# Ivanti Endpoint Manager  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ivanti-endpoint-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ivanti Endpoint Manager

This document provides guidance on how to integrate Ivanti Endpoint Manager with Google SecOps.

## Use Cases

  1. Perform enrichment of entities
  2. Perform active actions.



## Configure Ivanti Endpoint Manager integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{ip address}} | Yes | API root of the Ivanti Endpoint Manager instance.  
Username | String | N/A |  | Username of the Ivanti Endpoint Manager.  
Password | Password | N/A |  | Password of the Ivanti Endpoint Manager.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Ivanti Endpoint Manager server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Ivanti Endpoint Manager with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
**if successful:** "Successfully connected to the Ivanti Endpoint Manager server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Ivanti Endpoint Manager server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Ivanti Endpoint Manager. Supported entities: IP Address, Hostname, MAC Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight containing all of the retrieved information about the entity.  
Custom Column Set | String |  | No | If specified, action will also try to return information about endpoints using custom column sets. If not specified, action will only return basic information.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
        "guid": "{3F78627C-A425-4F45-9D82-A037250A8136}",
        "DeviceName": "",
        "DomainName": "",
        "LastLogin": "",
        "IPAddress": "",
        "SubNetMask": "",
        "MACAddress": "",
        "OSName": "",
        "column_set_info": {
            "Computer_DisplayName": "IVANTI-H01"
        }
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
guid | When available in JSON  
DeviceName | When available in JSON  
DomainName | When available in JSON  
LastLogin | When available in JSON  
IPAddress | When available in JSON  
SubNetMask | When available in JSON  
MACAddress | When available in JSON  
OSName | When available in JSON  
column_set_info_Computer_DisplayName | When available in JSON  
  
##### Entity Insight

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available for one(is_success = true):** "Successfully enriched the following entities using information from Ivanti Endpoint Manager: {entity.identifier}".  
******If data is not available for one (is_success=true):** "Action wasn't able to enrich the following entities using information from Ivanti Endpoint Manager: {entity.identifier}"**.****If data is not available for all (is_success=false):** None of the provided entities were enriched.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)******If column set is provided and count is 0 in first response:** "Error executing action "Enrich Entities". Reason: column set '{column set name} is invalid. Please check the spelling or remove it from the action configuration.' | General  
Case Wall Table | **Title:** {entity.identifier} | Entity  
  
### List Column Sets

#### Description

List available column sets in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Column Sets To Return | Integer | 50 | No | Specify how many column sets to return. Default: 50.  
  
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
**if found results (is_success = true):** "Successfully found column sets for the provided criteria in Ivanti Endpoint Manager.  
******if not found results (is_success = true):** "No column sets were found for the provided criteria in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Column Sets". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Column Set Fields

#### Description

List available fields in column sets in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Column Set | String |  | Yes | Specify the name of the column set for which you want to return fields.  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Fields To Return | Integer | 50 | No | Specify how many column sets to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
        "columns": [""Computer"."Display Name"",""Computer"."Type""
    
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully found columns set "{column set name}" fields for the provided criteria in Ivanti Endpoint Manager.  
******if not found results (is_success = true):** "No column set "{columnset name}" fields were found for the provided criteria in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Column Set Fields". Reason: {0}''.format(error.Stacktrace) | General  
  
### Execute Query

#### Description

Execute query in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the name of the query that you want to execute.  
Max Results To Return | Integer | 50 | No | Specify how many results to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "results": [
            {
                "Device_x0020_Name": "IEDM-C",
                "Type": "Virtual Server",
                "OS_x0020_Name": "Microsoft Windows Server 2019, 64-bit"
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully execute query "{query name} in Ivanti Endpoint Manager."  
******if not found results (is_success = true):** "No results were found for the query {query name} in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Query". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Queries

#### Description

List available queries in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Queries To Return | Integer | 50 | No | Specify how many queries to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "queries": [""Computer"."Display Name"",""Computer"."Type""
    
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully found queries for the provided criteria in Ivanti Endpoint Manager.  
******if not found results (is_success = true):** "No queries were found for the provided criteria in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Queries". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Endpoint Vulnerabilities

#### Description

List vulnerabilities on the endpoints in Ivanti Endpoint Manager. Supported entities: IP Address, Mac Address, Hostname.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Severity Filter | CSV |  | No | Specify a comma-separated list of severities that will be used, when returning information about vulnerabilities. If nothing is provided, action will return all vulnerabilities. Possible values:ServicePack, Critical, High, Medium, Low, N/A, Unknown.  
Max Vulnerabilities To Return | Integer | 50 | No | Specify how many vulnerabilities to return per entity. Default: 50.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "Name": "Ivanti 11.0.30 Adaptive Settings",
            "ID": 90
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if vulnerabilities found on at least one entity (is_success = true):** "Successfully found vulnerabilities on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******if no vulnerabilities on some endpoints(is_success = true):** "No vulnerabilities were found on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******If no vulnerabilities found on all endpoints (is_success=true):** "No vulnerabilities were found on the provided entities in Ivanti Endpoint Manager.  
******if some endpoints not found(is_success = true):** "The following entities were not found in Ivanti Endpoint Manager: {entity.identifier}.  
******If all endpoints were found (is_success = false):** "None of the provided entities were found in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Endpoint Vulnerabilities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Scan Endpoints

#### Description

Scan endpoints for vulnerabilities in Ivanti Endpoint Manager. Supported entities: IP Address, Mac Address, Hostname. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Task Name | String | N/A | No | Specify the name of the scan vulnerabilities task. If nothing is provided the action will use the "Google SecOps Scan Endpoints" name.  
Only Initiate | Checkbox |  |  | If enabled, action will only initiate the task execution without waiting for results.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
    "task_id": 1
    }
    
    
    
    [
        "Entity": {
            "status": {TaskMachineData/Status}
        },
    "Entity": {
            "status": Done
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if at least 1 endpoint exists and status is Done (is_success = true):** "Successfully executed vulnerability scan on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******if at least 1 endpoint exists and status is Failed (is_success = true):** "Action wasn't able to execute vulnerability scan on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******if at least 1 endpoint exists and status is Failed for all (is_success = true):** "Action wasn't able to execute vulnerability scan on the provided entities in Ivanti Endpoint Manager.  
******if some endpoints not found(is_success = true):** "The following entities were not found in Ivanti Endpoint Manager: {entity.identifier}.  
******If all endpoints were found (is_success = false):** "None of the provided entities were found in Ivanti Endpoint Manager.  
******if at least 1 endpoint exists and "Only Initiate" is enabled (is_success = true):** "Successfully initiated vulnerability scan on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Scan Endpoints". Reason: {0}''.format(error.Stacktrace)******If timeout:** "Error executing action "Scan Endpoints". Reason: action ran into a timeout during execution. Pending entities: {entities that are still in progress}. Please increase the timeout in IDE or enable "Only Initiate". | General  
  
### Execute Task

#### Description

Execute task in Ivanti Endpoint Manager. Supported entities: Hostname, IP address, MAC Address. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Task Name | String | N/A | No | Specify the name of the task. If nothing is provided the action will use the "Google SecOps Execute Task" name.  
Delivery Method | String | N/A | Yes | Specify the name of the delivery method that will be used during task execution.  
Package | String | N/A | Yes | Specify the name of the package that will be used during task execution.  
Wake Up Machines | Checkbox | Unchecked | Yes | If enabled, action will wake up the machine during task execution.  
Common Task | Checkbox | Unchecked | Yes | If enabled, action will mark this task as common.  
Only Initiate | Checkbox | Checked | Yes | If enabled, action will only initiate the task execution without waiting for results.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
    "task_id": 1
    }
    
    
    
    [
      "Entity": {
            "status": {TaskMachineData/Status}
        },
      "Entity": {
            "status": Done
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if Done status code on one(is_success = true):** "Successfully executed task "{task name}"in Ivanti Endpoint Manager on the following entities: {entities}.  
******if at least 1 endpoint exists and "Only Initiate" is enabled (is_success = true):** "Successfully initiated task on the following entities in Ivanti Endpoint Manager: {entity.identifier}.  
******If Failed status code on one(is_success = false):** Action wasn't able to execute task on the following entities: {entities}  
******If Failed status code on all(is_success = false):** Action wasn't able to execute a task on the provided entities.  
******If at least one entities was not found (is_success = false):** The following entities were not found in Ivanti Endpoint Manager: {entities}  
******If all endpoints were found (is_success = false):** "None of the provided entities were found in Ivanti Endpoint Manager. Task wasn't created.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Task". Reason: {0}''.format(error.Stacktrace)******If timeout:** "Error executing action "Execute Task". Reason: action ran into a timeout during execution. Pending entities: {entities that are still in progress}. Please increase the timeout in IDE or enable "Only Initiate".******If non 200 status code:** "Error executing action "Execute Task". Reason: {response from second request}' | General  
  
### List Delivery Methods

#### Description

List available delivery methods in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Type | DDL | AllPossible Values:Push Pull Push and PullMulticastAll | No | Specify the delivery type that needs to be returned.  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Delivery Methods To Return | Integer | 50 | No | Specify how many delivery methods to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
        "DeliveryMethods": [
            {
                "DeliveryType": "MULTICAST",
                "DeliveryName": "Low-bandwidth distribution preparation",
                "DeliveryDescription": "Leaves package on targets for one week, allowing for a staggered installation."
            },
            {
                "DeliveryType": "PUSHANDPULL",
                "DeliveryName": "Emergency failsafe distribution",
                "DeliveryDescription": "Bandwidth-intensive forced installation of package."
            },
            {
                "DeliveryType": "PUSHANDPULL",
                "DeliveryName": "Standard policy-supported push distribution",
                "DeliveryDescription": "Moderate-speed distribution using bandwidth throttling without Multicast."
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if found results (is_success = true):** "Successfully found delivery methods for the provided criteria in Ivanti Endpoint Manager.  
******if not found results (is_success = true):** "No delivery methods were found for the provided criteria in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Delivery Methods". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** Available Delivery Methods**Columns:** Type NameDescription  | General  
  
### List Packages

#### Description

List available packages in Ivanti Endpoint Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Packages To Return | Integer | 50 | No | Specify how many packages to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Json Result
    
    
    {
        "DistributionPackages": [
            {
                "PackageType": "BATCH",
                "PackageName": "Clear Preferred Servers",
                "PackageDescription": "Batch file that clears the cached preferred servers from the client",
                "PackagePrimaryFile": "..."
            },
            {
                "PackageType": "MAC",
                "PackageName": "Enroll macOS device in Ivanti MDM",
                "PackageDescription": "This package will initiate enrollment of a macOS device in Ivanti MDM",
                "PackagePrimaryFile": "..."
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully found packages for the provided criteria in Ivanti Endpoint Manager.  
******if not found results (is_success = true):** "No packages were found for the provided criteria in Ivanti Endpoint Manager.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Packages". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** Available Packages**Columns:** Type NameDescription Primary File  | General  
  
Delete a Trusted IP List

#### Description

Delete the IPSet specified by the Id.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Detector ID | String | N/A | Yes | Specify the detector ID that should be used to delete an IP set. This parameter can be found in the "Settings" tab.  
Trusted IP List IDs | String | N/A | Yes | Specify the comma-separated list of ids of ips sets. Example: id_1,id_2.  
  
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

  * If successfully (200 response) (is_success = true":  
Print "Successfully deleted the following Trusted IP lists: <ids>"
  * If unsuccessful for some of the ids(is_success = true":  
Print "Action wasn't able to delete the following Trusted IP Lists from AWS GuardDuty:\n{0}.".format(list_of_ids)

**The action should fail and stop a playbook execution:**

  * Invalid detector ID should raise an exception as well, stop the playbook and set is_success to false.
  * If fatal error, SDK error, like wrong credentials, no connection to server, other:   
print "Error executing action "Delete a Trusted IP List". Reason: {0}''.format(error.Stacktrace

| General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
