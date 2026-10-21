---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tanium/
title: Tanium \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:35.549706+00:00
---

# Tanium  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tanium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tanium

This document provides guidance on how to integrate Tanium with Google SecOps.

## Prerequisites

Tanium uses API tokens to authenticate calls into the REST APIs. For more information on how to generate API tokens, see [Managing API tokens](https://help.tanium.com/bundle/ug_console_cloud/page/platform_user/console_api_tokens.html) in the Tanium documentation.

## Integrate Tanium with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | URL | N/A | Yes | Specify the Tanium API Root that integration should use.  
API Token | Password | N/A | Yes | Specify the Tanium API Token that integration should use.  
Verify SSL | Checkbox | Checked | No | If enabled, the Google SecOps server checks that the certificate is configured for the API root.  
  
## Actions

### Ping

Test connectivity to the Tanium installation with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run on

This action doesn't run on entities, nor has mandatory input parameters.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ "Successfully connected to the Tanium installation with the provided connection parameters!"**The action should fail and stop a playbook execution:**___If critical error, like wrong credentials or lost connectivity is reported_ : "Failed to connect to the Tanium installation! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Enrich entities using information from Tanium. Action is a Google SecOps async action. Supported entities: Hostname, IP Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional Fields | CSV | N/A | No | Specify additional fields to fetch from Tanium for entity enrichment. Parameter accepts multiple values as a comma-separated string.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "data": {
            "now": "2022/01/28 10:18:54 GMT-0000",
            "max_available_age": "",
            "result_sets": [
                {
                    "age": 0,
                    "id": X,
                    "report_count": 2,
                    "saved_question_id": 0,
                    "question_id": X,
                    "archived_question_id": 0,
                    "seconds_since_issued": 0,
                    "issue_seconds": 0,
                    "expire_seconds": 0,
                    "tested": 4,
                    "passed": 1,
                    "mr_tested": 4,
                    "mr_passed": 4,
                    "estimated_total": 4,
                    "select_count": 10,
                    "error_count": 0,
                    "no_results_count": 0,
                    "columns": [
                        {
                            "hash": X,
                            "name": "Computer ID",
                            "type": 1
                        },
                        {
                            "hash": 0,
                            "name": "Count",
                            "type": 3
                        }
                    ],
                    "cache_id": "X",
                    "expiration": 0,
                    "filtered_row_count": 1,
                    "filtered_row_count_machines": 1,
                    "row_count": 1,
                    "row_count_machines": 1,
                    "item_count": 1,
                    "rows": [
                        {
                            "id": x,
                            "cid": x,
                            "data": [
                                [
                                    {
                                        "text": "X"
                                    }
                                ],
                                [
                                    {
                                        "text": "No User"
                                    }
                                ],
                                [
                                    {
                                        "text": "1"
                                    }
                                ]
                            ]
                        }
                    ]
                }
            ]
        }
    }
    

##### Enrichment table

**Prefix:** Tanium_

Enrichment Field Name | Logic - When to apply  
---|---  
Computer_ID | When available in JSON  
Operating_System | When available in JSON  
OS_Platform | When available in JSON  
Service_Pack | When available in JSON  
Domain_Name | When available in JSON  
Uptime | When available in JSON  
System_UUID | When available in JSON  
IP_Address | When available in JSON  
  
##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success = true):_ "Successfully enriched the following entities using information from Tanium: {entity.identifier}"._If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Tanium: {entity.identifier}"_If there are multiple matches in Tanium for the provided entity (is_success=true):_ "Multiple results found in Tanium for the entities, taking first match: {entity.identifier}"_If data is not available for all entities (is_success=false): "_ None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If the 400 status code (bad syntax of question) is reported:_ "Error executing action "Enrich Entities" because provided question text is invalid. "_If fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities"." Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity.identifier}**Table Columns:**

  * Key
  * Value

| Entity  
  
### Create Question

Create a new Tanium question based on the specified parameters, and the question is immediately asked. Action returns question ID that can be passed to the "Get Question Results" action to get question results. Note that the action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Question Text | String | N/A | Yes | Specify the contents of Tanium question. Example: Get Operating System from all machines  
  
#### Run on

The action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "data": {
            "id": X
        }
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success = true):_ "Successfully created Tanium question with id {question_id_from_response}".**The action should fail and stop a playbook execution:******_If the 400 status code (bad syntax of question) is reported:_ "Error executing action "Create Question" because provided question text is invalid. "_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Create Question". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Question Results

Fetch results for the Tanium question. Action is a Google SecOps async action. Note that the action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Question ID | Integer | N/A | Yes | Specify the Tanium question ID to get results for.  
Create Case Wall Table | Checkbox | Checked | No | If enabled, the action creates a case wall table as part of action results.  
Max Rows to Return | Integer | 50 | Yes | Specify the maximum number of rows that the action should return for the question.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "id": 1,
      "report_count": 3,
      "saved_question_id": 0,
      "question_id": 1,
      "seconds_since_issued": 600,
      "issue_seconds": 0,
      "expire_seconds": 600,
      "tested": 3,
      "passed": 3,
      "mr_tested": 3,
      "mr_passed": 3,
      "estimated_total": 3,
      "select_count": 3,
      "error_count": 0,
      "no_results_count": 0,
      "row_count": 3,
      "row_count_machines": 3,
      "item_count": 3,
      "filtered_row_count": 3,
      "filtered_row_count_machines": 3,
      "columns": [
        {
          "hash": 1,
          "name": "IP Address",
          "type": 5
        },
        {
          "hash": 2,
          "name": "Computer Name",
          "type": 1
        },
        {
          "hash": 3,
          "name": "Operating System",
          "type": 1
        }
      ],
      "rows": [
        {
          "IP Address": [
            "2001:db8:a::100",
            "192.0.2.10"
          ],
          "Computer Name": [
            "CLIENT-A01"
          ],
          "Operating System": [
            "Windows Server 2022 Datacenter"
          ]
        },
        {
          "IP Address": [
            "2001:db8:a::101"
          ],
          "Computer Name": [
            "CLIENT-B02"
          ],
          "Operating System": [
            "Windows Server 2019 Standard Evaluation"
          ]
        },
        {
          "IP Address": [
            "198.51.100.5"
          ],
          "Computer Name": [
            "server-web-prod.example.com"
          ],
          "Operating System": [
            "Debian 12.12"
          ]
        }
      ]
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success=true):_ "Successfully fetched results for the following Tanium question id: {question id}"._If data is not available (is_success=false):_ "No results were found for the Tanium question id: {question id}"**The action should fail and stop a playbook execution:******_If the 404 status code (question doesn't exist) is reported:_ "Failed to find Tanium question with question id {question_id}. "_If fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Qet Question Results". Reason: {0}''.format(error.Stacktrace) | General  
Table | **Table Name:** Tanium Question {question_id} Results**Table Columns:** Columns are generated based on the data returned from a question. | General  
  
### List Endpoint Events

List events related to the endpoints from Tanium. Action works with Tanium Threat Response API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event Type | DDL | Combined Possible values: 

  * File
  * Network
  * Process
  * Registry
  * Driver
  * Combined
  * DNS
  * Image

| No | Specify the type of the event that needs to be returned.  
Time Frame | DDL | Last Hour Possible Values: 

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Alert Time Till Now
  * 5 Minutes Around Alert Time
  * 30 Minutes Around Alert Time
  * 1 Hour Around Alert Time
  * Custom

| No | Specify a time frame for the results. If "Alert Time Till Now" is selected, the action uses start time of the alert as start time for the search and end time is current time. If "30 Minutes Around Alert Time" is selected, the action searches the alerts 30 minutes before the alert happened till 30 minutes after the alert has happened. Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time". If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.Format: ISO 8601  
Sort Field | String | timestamp | No | Specify the parameter that should be used for sorting.  
Sort Order | DDL | ASC Possible Values: 

  * ASC
  * DESC

| No | Specify the order of sorting.  
Max Events To Return | Integer | 50 | No | Specify the number of events to return per entity.Maximum: 500  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "events": [
        {
          "create_time": "2022-01-18 11:59:52.000",
          "end_time": null,
          "exit_code": null,
          "pid": 2,
          "process_path": "kthreadd",
          "id": "72057594037927939",
          "process_table_id": "72057594037927939",
          "parent_process_table_id": "72057594037927937",
          "parent_pid": -1,
          "user_name": "root",
          "group_name": "root",
          "hash_type_name": null,
          "hash": null,
          "process_command_line": null,
          "parent_path": "<Unknown Process>",
          "parent_command_line": "<Unknown Process>",
          "parent_hash": null,
          "create_time_raw": 1642507192000,
          "end_time_raw": null
        }
      ]
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If at least one event is found for an endpoint (is_success=true):_ "Successfully returned events for the following endpoints in Tanium:\n".format(entity)."_If no events are found for an endpoint (is_success=true):_ "No events were found for the following endpoints in Tanium:\n".format(entity)."_If no events are found for all endpoints (is_success=true):_ "No events were found for the provided endpoints in Tanium."_If couldn't create connection or no connection found for some endpoints (is_success=true):_ "Action wasn't able to retrieve information about events from the following endpoints in Tanium due to agent connectivity issues: {entity}. Please make sure that those hostnames are connected to the Tanium Threat Response module."If didn't enrich all (is_success=false): "No information about IOCs were found."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich IOC". Reason: {0}''.format(error.Stacktrace)_If couldn't create connection or no connection is found for all endpoints (is_success=false):_ "Error executing action "List Endpoint Events". Reason: action wasn't able to retrieve information about events from the provided endpoints in Tanium due to agent connectivity issues. Please make sure that those hostnames are connected to the Tanium Threat Response module." | General  
  
### Quarantine Endpoint

Quarantine the endpoints in Tanium. Action works with Tanium Threat Response API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Only Initiate | Checkbox | Unchecked | Yes | If enabled, the action only initiates the task execution without waiting for results.  
Package Names | String | 

  * `Apply Linux IPTables Quarantine` for Linux
  * `Apply Mac PF Quarantine` for macOS
  * `Apply Windows IPsec Quarantine` for Windows

| Yes | A JSON object containing all package names for every operating system.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "id": 82,
      "type": "responseAction",
      "status": "COMPLETED",
      "metadata": {
          "id": 2,
          "type": "gatherSnapshot",
          "status": "RUNNING",
          "computerName": "EX01.exlab.local",
          "userId": 1,
          "userName": "tanium",
          "options": {},
          "results": {
              "taskIds": [
                  73
              ],
              "actionIds": []
          },
          "expirationTime": "2022-03-08T14:31:50.211Z",
          "createdAt": "2022-03-01T14:31:50.212Z",
          "updatedAt": "2022-03-01T14:36:19.533Z"
      },
      "results": {
          "didActionComplete": false,
          "stopped": true,
          "finished": true
      },
      "error": null,
      "startTime": "2022-03-01T14:42:10.390Z",
      "endTime": "2022-03-01T15:29:50.495Z",
      "createdAt": "2022-03-01T14:42:10.379Z",
      "updatedAt": "2022-03-01T14:42:10.379Z"
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If at least one endpoint is quarantined (is_success=true):_ "Successfully initiated quarantine on the following endpoints in Tanium:\n".format(entity)_If_ _at least one endpoint is not quarantined, but not due to timeout (is_success=false):_ "Action wasn't able to quarantine the following endpoints in Tanium: {entity}. Please make sure that the Tanium Threat Response agent is connected properly and the hostname/IP address is correct."_If all endpoints are not quarantined, but not due to timeout (is_success=false):_ "Action wasn't able to quarantine the provided endpoints in Tanium. Please make sure that the Tanium Threat Response agent is connected properly and the hostname/IP address is correct."_Async Pending entities:_ {entities}**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Enrich IOC". Reason: {0}''.format(error.Stacktrace)_If couldn't create connection or no connection found for all endpoints (is_success=false):_ "Error executing action "Quarantine Endpoint". Reason: action wasn't able to quarantine the provided endpoints in Tanium due to agent connectivity issues. Please make sure that the endpoints are connected to the Tanium Threat Response module and the hostname/IP address is correct."_If run into a timeout:_ "Error executing action "Quarantine Endpoint". Reason: action ran into a timeout during execution. Pending entities: {entities that are still in progress}. Please increase the timeout in IDE or enable "Only Initiate"." | General  
  
### Download File

Download a file from endpoints in Tanium. Action works with Tanium Threat Response API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Paths | CSV | N/A | Yes | Specify the absolute path of the files on the endpoint that needs to be downloaded.  
Download Folder Path | String | N/A | Yes | Specify the path to the folder, where you want to store the files.  
Overwrite | Checkbox | Unchecked | Yes | If enabled, the action overwrites the file with the same name.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "absolute_file_path": [
            "file_path_1",
            "file_path_2"
        ],
        "entity": [
            {
                "identifier": "",
                "task_details": {
                    "id": 81,
                    "type": "fileDownload",
                    "status": "COMPLETED",
                    "metadata": {
                        "connection": "remote:centos-003:3864230059:1",
                        "paths": [
                            "/tmp/saaj-impl.jar"
                        ],
                        "compress": "true"
                    },
                    "results": {
                        "completed": [
                            "/tmp/saaj-impl.jar"
                        ],
                        "failed": [],
                        "fileResults": [
                            {
                                "response": {
                                    "source": "/tmp/saaj-impl.jar",
                                    "target": "/opt/Tanium/TaniumModuleServer/services/threat-response-service/tmp/4965e791-db87-4f31-ba60-2e52c9bac3de",
                                    "totalBytes": 503502,
                                    "transferHash": "5402c16c3873a722b94d8a3101cb98f5e4f862acc69cdee3a94cf40c1b04b265",
                                    "totalTimeMs": 260,
                                    "avgBytesPerSecond": 504123.0769230769
                                },
                                "uuid": "eb5077b3-9b02-42e2-bba4-58d9668a14e4",
                                "finalPath": "/opt/Tanium/TaniumModuleServer/services/threat-response-files/evidence/files/eb5077b3-9b02-42e2-bba4-58d9668a14e4.zip"
                            }
                        ]
                    },
                    "error": null,
                    "startTime": "2022-03-01T14:38:23.952Z",
                    "endTime": "2022-03-01T14:38:24.559Z",
                    "createdAt": "2022-03-01T14:38:23.943Z",
                    "updatedAt": "2022-03-01T14:38:23.943Z"
                }
            }
        ]
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If at least one file is downloaded per entity (is_success=true):_ "Successfully downloaded the following files from the endpoint {entity} in Tanium:\n".format(downloaded files)."_If at least one file is not downloaded per entity, but not due to timeout (is_success=false):_ "Action wasn't able to download the following files from the endpoint {entity} in Tanium: {pending files}. Please make sure that the Tanium Threat Response agent is connected properly and the hostname/IP address is correct. The JSON result has more details about the tasks."_Async Pending entities:_ {entities}**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Download File". Reason: {0}''.format(error.Stacktrace)"_If a file with the same name already exists, but "Overwrite" == false:_ "Error executing action "Download File". Reason: files with path {0} already exist. Please delete the files or set "Overwrite" to true."_If run into a timeout:_ "Error executing action "Download File". Reason: action ran into a timeout during execution. Pending entities: {entities that are still in progress}. Please increase the timeout in IDE." | General  
  
### Delete File

Download a file from endpoints in Tanium. Action works with Tanium Threat Response API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Paths | CSV | N/A | Yes | Specify the absolute path of the files on the endpoint that needs to be deleted.  
  
#### Run on

This action works with the following entities:

  * IP Address
  * Hostname



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "success": [],
      "not_exist_already_or_errors": []
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If at least one file is deleted (status code: 204, is_success=true):_ "Successfully deleted files from the following endpoints in Tanium:\n".format(entity)."_If at least one file doesn't exist on one endpoint (status code: 500, is_success=true):_ "Status about some of the files is not clear, please check the JSON result. Tanium returns status code 500 in the case, when file is not found, but also, if there are some other challenges."_If at least one file doesn't exist on all endpoints (status code: 500, is_success=false):_ "Status about all of the files is not clear, please check the JSON result. Tanium returns status code 500 in the case, when file is not found, but also, if there are some other challenges."_If at least one endpoint is not found (is_success=true):_ "Action wasn't able to delete files from the following endpoints in Tanium: {entity}. Please make sure that the Tanium Threat Response agent is connected properly and the hostname/IP address is correct."_If all endpoints are not found (is_success=false):_ "Action wasn't able to delete files from the provided endpoints in Tanium. Please make sure that the Tanium Threat Response agent is connected properly and the hostname/IP address is correct."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Delete File". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Task Details

Retrieve details about a task in Tanium. Action works with Tanium Threat Response API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Task IDs | CSV | N/A | Yes | Specify a comma-separated list of task IDs for which you want to fetch details.  
Wait For Completion | Checkbox | Checked | No | If enabled, the action waits for the task to have one of the following statuses:

  * Completed
  * Incomplete
  * Error

  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "id": 81,
        "type": "fileDownload",
        "status": "COMPLETED",
        "metadata": {
            "connection": "remote:centos-003:3864230059:1",
            "paths": [
                "/tmp/saaj-impl.jar"
            ],
            "compress": "true"
        },
        "results": {
            "completed": [
                "/tmp/saaj-impl.jar"
            ],
            "failed": [],
            "fileResults": [
                {
                    "response": {
                        "source": "/tmp/saaj-impl.jar",
                        "target": "/opt/Tanium/TaniumModuleServer/services/threat-response-service/tmp/4965e791-db87-4f31-ba60-2e52c9bac3de",
                        "totalBytes": 503502,
                        "transferHash": "5402c16c3873a722b94d8a3101cb98f5e4f862acc69cdee3a94cf40c1b04b265",
                        "totalTimeMs": 260,
                        "avgBytesPerSecond": 504123.0769230769
                    },
                    "uuid": "eb5077b3-9b02-42e2-bba4-58d9668a14e4",
                    "finalPath": "/opt/Tanium/TaniumModuleServer/services/threat-response-files/evidence/files/eb5077b3-9b02-42e2-bba4-58d9668a14e4.zip"
                }
            ]
        },
        "error": null,
        "startTime": "2022-03-01T14:38:23.952Z",
        "endTime": "2022-03-01T14:38:24.559Z",
        "createdAt": "2022-03-01T14:38:23.943Z",
        "updatedAt": "2022-03-01T14:38:23.943Z"
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If at least one task is fetched (is_success=true):_ "Successfully fetched details about the following tasks in Tanium:\n".format(id)."_If at least one task is not found (is_success=true):_ "Action wasn't able to find the following tasks in Tanium:\n".format(id)."If at least one task is not found (is_success=true): "No tasks were found in Tanium."_Async fetching details about tasks:_ {task ids}**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Task Details". Reason: {0}''.format(error.Stacktrace)"_If run into a timeout and the "Wait for completion" parameter is enabled:_ "Error executing action "Get Task Details". Reason: action ran into a timeout during execution. Pending tasks: {tasks that are still in progress}. Please increase the timeout in IDE." | General  
  
### Create Connection

Create connection to the endpoint in Tanium. 

#### Entities

This action runs on the Hostname and IP Address entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created a connection for the following entities: LIST_OF_SUCCESSFUL_ENTITIES` `No suitable entities were found in the scope.` | Action succeeded.  
`Action wasn't able to create a connection for the following entities: LIST_OF_FAILED_ENTITIES ` `Error executing action "Create Connection". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### List Connections

List endpoint connections in Tanium.

#### Entities

This action doesn't run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found connections in  INTEGRATION` `No connections were found in  INTEGRATION` | Action succeeded.  
`Error executing action "List Connections". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
