---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/logpoint/
title: Logpoint \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:16.424286+00:00
---

# Logpoint  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/logpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Logpoint

This document provides guidance on how to integrate Logpoint with Google SecOps.

## Use Cases

Perform active actions - execute queries to get more information about the entities.

## Configure Logpoint integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IP Address | String | https://x.x.x.x | Yes | IP address of the Logpoint instance.  
Username | String | N/A | Yes | Username of the Logpoint account.  
Secret | Password | N/A | Yes | Secret API Key of the Logpoint account  
CA Certificate File | String | N/A | No | Base64 encoded CA certificate file.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Logpoint server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Logpoint with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

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
**if successful:** "Successfully connected to the Logpoint server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Logpoint server! Error is {0}".format(exception.stacktrace) | General  
  
### Execute Query

#### Description

Execute search query in Logpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query that needs to be executed in Logpoint.  
Time Frame | DDL | Last 24 HoursPossible Values:  
Last HourLast 12 HoursLast 24 HoursLast 30 DaysLast 365 DaysCustom  | Yes | Specify the time frame for the query. If "Custom" is selected, you need to also provide start time and end time.  
Start Time | String | N/A | No | Specify the start time for the query. Format:YYYY-MM-DDThh:mm:ssZ or timestamp.  
End Time | String | N/A | No | Specify the end time for the query.Format:YYYY-MM-DDThh:mm:ssZ or timestamp. If nothing is provided action will use current time as end time.  
Repos | CSV | N/A | No | Specify a comma-separated list of names of the repos. If nothing is provided, action will search in all repos.  
Max Results To Return | Integer | 100 | No | Specify how many results should be returned.  
  
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
        "query_type": "simple",
        "rows": [
            {
                "msg": "2021-01-10 10:27:50 Benchmarker; reporting speed; service=norm_front; actual_mps=1; doable_mps=19096;",
                "log_ts": 1610274470,
                "actual_mps": "1",
                "doable_mps": "19096",
                "_type_str": "_tz device_name msg source_name col_type object norm_id service collected_at label device_ip
        _enrich_policy action _fromV550 repo_name logpoint_name",
        "device_name": "localhost",
                "_offset": 48317,
                "logpoint_name": "Logpoint",
                "action": "reporting speed",
                "repo_name": "_logpoint",
                "source_name": "/opt/immune/var/log/benchmarker/norm_front.log",
                "col_ts": 1610274470,
                "_tz": "UTC",
                "norm_id": "Logpoint",
                "_identifier": "0",
                "collected_at": "Logpoint",
                "device_ip": "127.0.0.1",
                "service": "norm_front",
                "_fromV550": "t",
                "_enrich_policy": "None",
                "_type_num": "actual_mps doable_mps col_ts sig_id log_ts _offset _identifier",
                "_type_ip": "device_ip",
                "sig_id": "10505",
                "col_type": "filesystem",
                "object": "Benchmarker",
                "_labels": [
                    "Logpoint",
                    "Benchmarker"
                ]
            }
        ],
        "version": 6,
        "extracted_terms": [],
        "time_range": [
            1609496280,
            1610274480
        ],
        "orig_search_id": "9acac4a0-e530-4a19-a446-e17d4d9f8aae",
        "success": true,
        "final": true,
        "totalPages": 1,
        "estim_count": 185003,
        "complete": true,
        "status": {
            "Logpoint": {
                "default": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 3,
                    "final": true
                },
                "_logpoint": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 185000,
                    "final": true
                },
                "LogSource1": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 0,
                    "final": true
                },
                "_LogpointAlerts": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 0,
                    "final": true
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if success == true for all requests (is_success = true):** "Successfully executed query and retrieved results from Logpoint".  
******If success == true for all requests but no results (is_success=false):** "No data was found for the provided query."  
******If success == false for at least one request (is_success = false):** "Action wasn't able to successfully execute query and retrieve results from Logpoint. Reason: {0}".format(message)  
******Async message** "Waiting for query to finish processing in Logpoint."  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Query". Reason: {0}''.format(error.Stacktrace)  
******If timeout:** Error executing action "Execute Query". Reason: Action reached a timeout. Please narrow down the time frame or lower the amount of results to return.  
******If at least one repo is not found:** "Error executing action "Execute Query". Reason: The following repos were not found in Logpoint: {0}. Please make sure that all of the repos are available.".format(comma-separated list of repos that were not found)  
******If "Custom" is selected, but "Start Time" is not provided:** "Error executing action "Execute Query". Reason: you need to provide "Start Time", if "Custom" is selected for time frame." | General  
Case Wall Table | **Table Name:** "Results"  
  
****All of the columns from the response will be used as table columns. | General  
  
### Execute Entity Query

#### Description

Execute query in Logpoint based on the entities. Currently supported entity types: User, IP, Email Address, URL, File Hash, Hostname. Note: Email Address is a User entity that matches the format of email address.

#### How to work with action parameters

This action gives an ability to easily retrieve information related to entities. For example, it's possible to solve the use case, where you want to see the amount of logs of the endpoints affected by the provided hash without any complicated query building.

In order to solve this problem in the Logpoint you would need to prepare the following query: `("device_ip"="10.0.0.1" or "device_ip"="10.0.0.2") and ("hash"="7694f4a66316e53c8cdd9d9954bd611d" or "hash"="8264ee52f589f4c0191aa94f87aa1aeb") | chart count() by device_ip`

In order to create the same query using "Execute Entity Query" action, you need to fill out the action parameters in the following way:

Query | | chart count() by device_ip  
---|---  
IP Entity Key | device_ip  
File Hash Entity Key | hash  
Cross Entity Operator | AND  
  
All of the other fields can be left empty.

If the use case is to see how many endpoints were affected by the provided hashes, then the configuration of the "Execute Entity Query" will have the following look.

Query | | chart count() by device_ip  
---|---  
File Hash Entity Key | hash  
  
"Cross Entity Operator" in this situation won't have an impact, because it only affects the query, when multiple "Entity Keys" are provided.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String |  | Yes | Specify the query that needs to be executed. Please refer to the action documentation for details.  
Time Frame | DDL | Last 24 HoursPossible Values:  
Last HourLast 12 HoursLast 24 HoursLast 30 DaysLast 365 DaysCustom  | Yes | Specify the time frame for the query. If "Custom" is selected, you need to also provide start time, end time by default will use current time.  
Start Time | String |  | No | Specify the start time for the query. Format:YYYY-MM-DDThh:mm:ssZ or timestamp.  
End Time | String |  | No | Specify the end time for the query.Format:YYYY-MM-DDThh:mm:ssZ or timestamp. If nothing is provided action will use current time as end time.  
Repos | CSV |  | No | Specify a comma-separated list of names of the repos. If nothing is provided, action will search in all repos.  
IP Entity Key | String |  | No | Specify what key should be used with IP entities. Please refer to the action documentation for details.  
Hostname Entity Key | String |  | No | Specify what key should be used with Hostname entities, when preparing the . Please refer to the action documentation for details.  
File Hash Entity Key |  |  | No | Specify what key should be used with File Hash entities. Please refer to the action documentation for details.  
User Entity Key |  |  | No | Specify what key should be used with User entities. Please refer to the action documentation for details.  
URL Entity Key |  |  | No | Specify what key should be used with URL entities. Please refer to the action documentation for details.  
Email Address Entity Key |  |  | No | Specify what key should be used with Email Address entities. Please refer to the action documentation for details.  
Stop If Not Enough Entities | Checkbox | Checked | Yes | If enabled, action will not start execution, unless all of the entity types are available for the specified ".. Entity Keys". Example: if "IP Entity Key" and "File Hash Entity Key" are specified, but in the scope there are no file hashes then if this parameter is enabled, action will not execute the query.  
Cross Entity Operator | DDL | ORPossible Values:ORAND | Yes | Specify what should be the logical operator used between different entity types.  
Max Results To Return | Integer | 100 | No | Specify how many results should be returned.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * User
  * Hash
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "query_type": "simple",
        "rows": [
            {
                "msg": "2021-01-10 10:27:50 Benchmarker; reporting speed; service=norm_front; actual_mps=1; doable_mps=19096;",
                "log_ts": 1610274470,
                "actual_mps": "1",
                "doable_mps": "19096",
                "_type_str": "_tz device_name msg source_name col_type object norm_id service collected_at label device_ip
        _enrich_policy action _fromV550 repo_name logpoint_name",
        "device_name": "localhost",
                "_offset": 48317,
                "logpoint_name": "Logpoint",
                "action": "reporting speed",
                "repo_name": "_logpoint",
                "source_name": "/opt/immune/var/log/benchmarker/norm_front.log",
                "col_ts": 1610274470,
                "_tz": "UTC",
                "norm_id": "Logpoint",
                "_identifier": "0",
                "collected_at": "Logpoint",
                "device_ip": "127.0.0.1",
                "service": "norm_front",
                "_fromV550": "t",
                "_enrich_policy": "None",
                "_type_num": "actual_mps doable_mps col_ts sig_id log_ts _offset _identifier",
                "_type_ip": "device_ip",
                "sig_id": "10505",
                "col_type": "filesystem",
                "object": "Benchmarker",
                "_labels": [
                    "Logpoint",
                    "Benchmarker"
                ]
            }
        ],
        "version": 6,
        "extracted_terms": [],
        "time_range": [
            1609496280,
            1610274480
        ],
        "orig_search_id": "9acac4a0-e530-4a19-a446-e17d4d9f8aae",
        "success": true,
        "final": true,
        "totalPages": 1,
        "estim_count": 185003,
        "complete": true,
        "status": {
            "Logpoint": {
                "default": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 3,
                    "final": true
                },
                "_logpoint": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 185000,
                    "final": true
                },
                "LogSource1": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 0,
                    "final": true
                },
                "_LogpointAlerts": {
                    "@class": "com.logpoint.libcommon.merger.api.SimpleStatus",
                    "estim_count": 0,
                    "final": true
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if success == true for all requests (is_success = true):** "Successfully executed query and retrieved results from Logpoint".  
******If success == true for all requests but no results (is_success=false):** "No data was found for the provided query."  
******If success == false for at least one request (is_success = false):** "Action wasn't able to successfully execute query and retrieve results from Logpoint. Reason: {0}".format(message)  
******Async message** "Waiting for query to finish processing in Logpoint."  
******If "Stop If Not Enough Entities" is enabled and not enough entity types are available for the provided "Entity Keys" (is_success=false):** Action wasn't able to build the query, because not enough entity types were supplied for the specified ".. Entity Keys". Please disable "Stop If Not Enough Entities" parameter or provide at least one entity for each specified ".. Entity Key".  
****  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Entity Query". Reason: {0}''.format(error.Stacktrace)  
**If timeout:** Error executing action "Execute Entity Query". Reason: Action reached a timeout. Please narrow down the time frame or lower the amount of results to return.******If at least one repo is not found:**  
****"Error executing action "Execute Entity Query". Reason: The following repos were not found in Logpoint: {0}. Please make sure that all of the repos are available.".format(comma-separated list of repos that were not found)  
******If no "Entity" keys are specified:** Error executing action "Execute Entity Query". Reason: Please specify at least one ".. Entity Key" parameter.******If "Custom" is selected, but "Start Time" is not provided:** "Error executing action "Execute Entity Query". Reason: you need to provide "Start Time", if "Custom" is selected for time frame." | General  
Case Wall Table  
| **Table Name:** "Results"  
****All of the columns from the response will be used as table columns. | General  
  
### List Repos

#### Description

List available repos in Logpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Max Repos To Return | Integer | 100 | No | Specify how many reports should be returned.  
  
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
        "success": true,
        "allowed_repos": [
            {
                "repo": "default",
                "address": "127.0.0.1:5504/default"
            },
            {
                "repo": "_logpoint",
                "address": "127.0.0.1:5504/_logpoint"
            },
            {
                "repo": "_LogpointAlerts",
                "address": "127.0.0.1:5504/_LogpointAlerts"
            },
            {
                "repo": "LogSource1",
                "address": "127.0.0.1:5504/LogSource1"
            }
        ],
        "logpoint": [
            {
                "name": "Logpoint",
                "ip": "127.0.0.1"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if success == true (is_success = true):** "Successfully retrieve available repos query from Logpoint".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Repos". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** "Available Repos"  
****Name - allowed_repos/repo Address - allowed_repos/address | General  
  
### Update Incident Status

#### Description

Update incident status in Logpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | Yes | Specify the id of the incident, which you want to update.  
Action | DLL | ClosePossible Values:ResolveClose | Yes | Specify the action for the incident.  
  
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
**if success== true (is_success = true):** "Successfully {0} incident with ID {1} in Logpoint.".format(resolved/closed, incident_id)******if success== false(is_success = true):** "Action wasn't able to {0} incident with ID {1} in Logpoint.".format(resolve/close, incident_id)******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Update Incident Status". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connector

### Logpoint - Incidents Connector

#### Description

Pull incidents from Logpoint.

### Configure Logpoint - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
IP Address | String | https://x.x.x.x | Yes | IP address of the Logpoint instance.  
Username | String | N/A | Yes | Username of the Logpoint account.  
Secret | Password | N/A | Yes | Secret of the Logpoint account.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch incidents.  
Lowest Risk To Fetch | String | N/A | No | Lowest risk of the incidents to fetch. Possible values: Critical, High, Medium, Low.  
Max Incidents To Fetch | Integer | 10 | No | How many incidents to process per one connector iteration..  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Logpoint server is valid.  
CA Certificate File | String | N/A | No | Base64 encoded CA certificate file.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
User Filter | CSV | N/A | No | A comma-separated list of usernames that are used to filter out incidents. Only incidents created by the valid users are ingested. If nothing is provided, this filter is not applied and the connector ingests incidents from all users.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
