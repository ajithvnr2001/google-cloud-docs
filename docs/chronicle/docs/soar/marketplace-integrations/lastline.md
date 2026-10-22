---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/lastline/
title: Lastline \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:58.521574+00:00
---

# Lastline  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/lastline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Lastline

**Important:** Lastline was acquired by VMWare and became part of VMware NSX Network Detection and Response.

This document provides guidance on how to integrate Lastline with Google SecOps.

## Use Cases

Dynamic Analysis of URL or File objects.

## Configure Lastline integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://user.lastline.com | Yes | Lastline API root  
Username | String | N/A | Yes | Lastline account username to use in the integration.  
Password | Password | N/A | Yes | Lastline account password to use in the integration.  
Verify SSL | Checkbox | Checked | No | Specify whether the integration should check if API root is configured with the valid certificate.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Lastline service with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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

  * **if successful:** "Successfully connected to the Lastine service with the provided connection parameters!"

**The action should fail and stop a playbook execution:**

  * **if account credentials are incorrect:** "Failed to connect to the Lastline service with the provided account. Please check your configuration. Error is {0}".format(exception.stacktrace)



  * **if other critical error:** "Failed to connect to the Lastline service! Error is {0}".format(exception.stacktrace)

| General  
  
### Submit URL

#### Description

Submit analysis task for the provided URL.

**Note:** Action is not working with Google SecOps entities, URL to analyze should be provided as action input parameter.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
URL For Analysis | String | N/A | Yes | Specify URL to analyze.  
Wait for the report? | Checkbox | Checked | No | Specify whether the action should wait for the report creation. Report also can be obtained later with Get Analysis Results action once scan is completed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### JSON Result

If Wait for the report checkbox is not set:
    
    
    {
        "success": 1,
        "data": {
            "submission_timestamp": "2021-03-10 07:13:25",
            "task_uuid": "543b3a6ffd17001009d4e10cfa16c2c3",
            "expires": "2021-03-11 14:51:57"
        }
    }
    

If Wait for the report checkbox is set:
    
    
    {
        "success": 1,
        "data": {
            "submission": "2021-03-14 04:46:11",
            "expires": "2021-03-16 04:46:10",
            "task_uuid": "5801c22ce6b4001003e58377051920f2",
            "reports": [
                {
                    "relevance": 1.0,
                    "report_uuid": "36150b54987b7f8bIUnzQWg2UgKxu8qdz7caWKwqyWz1yyE1aFpa9g",
                    "report_versions": [
                        "ll-pcap"
                    ],
                    "description": "Pcap analysis"
                },
                {
                    "relevance": 1.0,
                    "report_uuid": "a03998ee0d483efaRlYorEk0lbJUBcMXkYP1YfeGpQTufOFDWraR5Q",
                    "report_versions": [
                        "ll-web"
                    ],
                    "description": "Dynamic analysis in instrumented Chrome browser"
                }
            ],
            "submission_timestamp": "2021-03-15 03:58:51",
            "child_tasks": [
                {
                    "task_uuid": "772d23d8d59500100f87aac889c70ece",
                    "score": 0,
                    "tag": "network traffic analysis",
                    "parent_report_uuid": "a03998ee0d483efaRlYorEk0lbJUBcMXkYP1YfeGpQTufOFDWraR5Q"
                }
            ],
            "score": 0,
            "malicious_activity": [
                "Info: A Domain / URL of high reputation was visited"
            ],
            "analysis_subject": {
                "url": "https://yahoo.com"
            },
            "last_submission_timestamp": "2021-03-15 03:58:51"
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** "Successfully created analysis task for the url {0}".format(url)  
****
  * **If successful and checkbox to wait for result was provided, after action is complete (fetches the result):** "Successfully fetched the analysis results for the url {0}".format(url)  
****
  * **If incorrect url was provided (is_success=false):** "Failed to create analysis task because the provided url {0} is incorrect.".format(url)  
****
  * **If other non critical error happened (is_success=false):** "Failed to create analysis task for the url {0}. Error is {1}".format(url,entity_identifier)  
****

**The action should fail and stop a playbook execution:**

  * **if api credentials are incorrect:** "Failed to connect to the Lastline service with the provided api key or token. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if account credentials are incorrect:** "Failed to connect to the Lastline service with the provided account. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if other critical error:** "Failed to connect to the Lastline service! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table Name:** "{0} Analysis Results".**Table Columns:** Submission_TimestampLatest_Submission_TimestampResults_Expiry_TimestampAnalysis_Task_UUIDScoreMalicious_Activity | **General**  
  
### Submit File

#### Description

Submit analysis task for the provided File.

**Note:** Action is not working with Google SecOps entities, full path to file to analyze should be provided as action input parameter.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Path | String | N/A | Yes | Specify full path to file to analyze.  
Wait for the report? | Checkbox | Checked | No | Specify whether the action should wait for the report creation. Report also can be obtained later with Get Analysis Results action once scan is completed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result

If Wait for the report checkbox is not set:
    
    
    {
        "success": 1,
        "data": {
            "submission_timestamp": "2021-03-10 07:13:25",
            "task_uuid": "543b3a6ffd17001009d4e10cfa16c2c3",
            "expires": "2021-03-11 14:51:57"
        }
    }
    

If Wait for the report checkbox is set:
    
    
    {
        "success": 1,
        "data": {
            "activity_to_mitre_techniques": {
                "Search: Enumerates running processes": [
                    {
                        "tactics": [
                            {
                                "id": "TA0007",
                                "name": "Discovery"
                            }
                        ],
                        "id": "T1057",
                        "name": "Process Discovery"
                    }
                ],
                "Settings: Requiring rights elevation in browser": [
                    {
                        "tactics": [
                            {
                                "id": "TA0005",
                                "name": "Defense Evasion"
                            }
                        ],
                        "id": "T1112",
                        "name": "Modify Registry"
                    }
                ],
                "Autostart: Registering a scheduled task": [
                    {
                        "tactics": [
                            {
                                "id": "TA0002",
                                "name": "Execution"
                            },
                            {
                                "id": "TA0003",
                                "name": "Persistence"
                            },
                            {
                                "id": "TA0004",
                                "name": "Privilege Escalation"
                            }
                        ],
                        "id": "T1053",
                        "name": "Scheduled Task"
                    }
                ],
                "Memory: Tracking process identifiers through mutexes": [
                    {
                        "tactics": [
                            {
                                "id": "TA0004",
                                "name": "Privilege Escalation"
                            },
                            {
                                "id": "TA0005",
                                "name": "Defense Evasion"
                            }
                        ],
                        "id": "T1055",
                        "name": "Process Injection"
                    }
                ],
                "Autostart: Registering a new service at startup": [
                    {
                        "tactics": [
                            {
                                "id": "TA0003",
                                "name": "Persistence"
                            },
                            {
                                "id": "TA0004",
                                "name": "Privilege Escalation"
                            }
                        ],
                        "id": "T1050",
                        "name": "New Service"
                    }
                ],
                "Settings: Granting rights to debug or read memory of another process(SeDebugPrivilege)": [
                    {
                        "tactics": [
                            {
                                "id": "TA0004",
                                "name": "Privilege Escalation"
                            },
                            {
                                "id": "TA0005",
                                "name": "Defense Evasion"
                            }
                        ],
                        "id": "T1134",
                        "name": "Access Token Manipulation"
                    }
                ],
                "Search: Enumerates loaded modules": [
                    {
                        "tactics": [
                            {
                                "id": "TA0007",
                                "name": "Discovery"
                            }
                        ],
                        "id": "T1057",
                        "name": "Process Discovery"
                    }
                ]
            },
            "submission": "2021-03-14 04:51:20",
            "expires": "2021-03-16 03:30:53",
            "child_tasks": [
                {
                    "task_uuid": "226d6278859c00102b480de14f0f1835",
                    "score": 0,
                    "tag": "File extracted from analysis subject",
                    "parent_report_uuid": "aad392a7339d5b51VH8vSLfPk5llbmidNtkUBTCCayKfK6j5wX22"
                },
                {
                    "task_uuid": "9894fee9908c001002eed0219fad3d28",
                    "score": 0,
                    "tag": "File extracted from analysis subject",
                    "parent_report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO"
                },
                {
                    "task_uuid": "f543a862fe90001023e3a67cc2769a30",
                    "score": 0,
                    "tag": "URL extracted from analysis subject",
                    "parent_report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO"
                },
                {
                    "task_uuid": "05efc0b74077001027ab691bdc7971ae",
                    "score": 0,
                    "tag": "network traffic analysis",
                    "parent_report_uuid": "aad392a7339d5b51VH8vSLfPk5llbmidNtkUBTCCayKfK6j5wX22"
                },
                {
                    "task_uuid": "390905dc316200102cd51e8880973a26",
                    "score": 0,
                    "tag": "URL extracted from analysis subject",
                    "parent_report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO"
                },
                {
                    "task_uuid": "a3710e5d6a1400102540b44b56011019",
                    "score": 0,
                    "tag": "network traffic analysis",
                    "parent_report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO"
                },
                {
                    "task_uuid": "c3a87f9a2f1b0010203b6049def1a1ac",
                    "score": 0,
                    "tag": "URL extracted from analysis subject",
                    "parent_report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO"
                },
                {
                    "task_uuid": "5fb932bf8dfc00100fbb9f2c75e8a061",
                    "score": 0,
                    "tag": "URL extracted from analysis subject",
                    "parent_report_uuid": "aad392a7339d5b51VH8vSLfPk5llbmidNtkUBTCCayKfK6j5wX22"
                }
            ],
            "reports": [
                {
                    "relevance": 1.0,
                    "report_uuid": "5749cedc8a1d6828hssTbnLGm6AOH3AUpefWyKY6nK8xCfvaZNEO",
                    "report_versions": [
                        "ll-int-win",
                        "ll-win-timeline-based",
                        "ioc:ll",
                        "ioc:stix",
                        "ioc:openioc",
                        "ioc:openioc:tanium",
                        "ll-win-timeline-thread-based"
                    ],
                    "description": "Dynamic analysis on Microsoft Windows 10"
                },
                {
                    "relevance": 0.0,
                    "report_uuid": "d4672aa84d9aa966WyYQH1SwRbltbJ3IzDXGUf7fL8F9uQwLOs4T",
                    "report_versions": [
                        "ll-static"
                    ],
                    "description": "Static analysis"
                },
                {
                    "relevance": 1.0,
                    "report_uuid": "aad392a7339d5b51VH8vSLfPk5llbmidNtkUBTCCayKfK6j5wX22",
                    "report_versions": [
                        "ll-int-win",
                        "ll-win-timeline-based",
                        "ioc:ll",
                        "ioc:stix",
                        "ioc:openioc",
                        "ioc:openioc:tanium",
                        "ll-win-timeline-thread-based"
                    ],
                    "description": "Dynamic analysis on Microsoft Windows 7"
                }
            ],
            "submission_timestamp": "2021-03-15 06:37:17",
            "task_uuid": "8af81dd5b542001024d946e57d28c99b",
            "score": 39,
            "malicious_activity": [
                "Autostart: Registering a new service at startup",
                "Autostart: Registering a scheduled task",
                "Memory: Tracking process identifiers through mutexes",
                "Search: Enumerates loaded modules",
                "Search: Enumerates running processes",
                "Settings: Granting rights to debug or read memory of another process(SeDebugPrivilege)",
                "Settings: Requiring rights elevation in browser",
                "Steal: Targeting Windows Saved Credential"
            ],
            "analysis_subject": {
                "sha256": "3ed0fead30f80313e7fdb275652295108f8044da592f27aa7e98232bf40b4738",
                "sha1": "933b0903a87d1ec2c1b54e4608223f42168422c7",
                "mime_type": "application/x-pe-app-32bit-i386",
                "md5": "a6d2b2f3ff369137748ff40403606862"
            },
            "last_submission_timestamp": "2021-03-15 06:37:17"
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** "Successfully created analysis task for the file {0}".format(file)  
****
  * **If successful and checkbox to wait for result was provided, after action is complete (fetches the result):** "Successfully fetched the analysis results for the file {0}".format(file)  
****
  * **If incorrect file path was provided (is_success=false):** "Failed to create analysis task because the provided file path {0} is incorrect.".format(file)  
****
  * **If other non critical error happened (is_success=false):** "Failed to create analysis task for the url {0}. Error is {1}".format(url,entity_identifier)  
****

**The action should fail and stop a playbook execution:**

  * **if api credentials are incorrect:** "Failed to connect to the Lastline service with the provided api key or token. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if account credentials are incorrect:** "Failed to connect to the Lastline service with the provided account. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if other critical error:** "Failed to connect to the Lastline service! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table Name:** "{0} Analysis Results".**Table Columns:** Submission_TimestampLatest_Submission_TimestampResults_Expiry_TimestampAnalysis_Task_UUIDScoreMalicious_Activitymd5_hashsha1_hashsha256_hashmime_type | General  
Attachments | **fileName:** lastline_file_analisys_full_report.json **fileContent:** json response from the request 5  | General  
  
### Search Analysis History

#### Description

Search Lastline completed analysis tasks history. For submission either URL or Filehash in a format of md5 or sha1 can be provided.

**Note:** Action is not working with Google SecOps entities, only action input parameters are used.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Submission Name | String | N/A | No | Submission name to search for. Can be either URL or Filehash in a format of MD5 and SHA1.  
Submission Type | DDL | Not Specified | No | Optionally specify a submission type to search for, either URL or FileHash.  
Max Hours Backwards | Integer | 24 | No | Time frame for which to search for completed analysis tasks  
Search in last x scans | Integer | 100 | Yes | Search for report in last x analysis's executed in Any.Run.  
Skip first x scans | Integer | 0 | No | Skip first x scans returned by Any.Run API.  
  
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
        "success": 1,
        "data": [
            {
                "username": "tip.labops@siemplify.co",
                "status": "finished",
                "task_subject_filename": null,
                "task_subject_sha1": "933b0903a87d1ec2c1b54e4608223f42168422c7",
                "task_uuid": "8af81dd5b542001024d946e57d28c99b",
                "task_subject_md5": "a6d2b2f3ff369137748ff40403606862",
                "task_subject_url": null,
                "task_start_time": "2021-03-15 06:37:18",
                "analysis_history_id": 711622656,
                "title": null,
                "score": 39
            },
            {
                "username": "tip.labops@siemplify.co",
                "status": "finished",
                "task_subject_filename": null,
                "task_subject_sha1": "933b0903a87d1ec2c1b54e4608223f42168422c7",
                "task_uuid": "8af81dd5b542001024d946e57d28c99b",
                "task_subject_md5": "a6d2b2f3ff369137748ff40403606862",
                "task_subject_url": null,
                "task_start_time": "2021-03-15 06:28:24",
                "analysis_history_id": 3856791660,
                "title": null,
                "score": 39
            },
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**

  * **if successful and found reports:** "Found Lastline completed analysis tasks for the provided search parameters".  
****
  * **If fail to find reports:** "No Any.Run reports were found."  
****

**Action should fail and stop playbook execution:**

  * **if account credentials are incorrect:** "Failed to connect to the Lastline service with the provided account. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if other critical error:** "Failed to connect to the Lastline service! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table Name:** Search Results**Table Columns:** Task UUIDmd5sha1Sha256UrlStatusSubmitted by (username)Submitted at | General  
  
### Get Analysis Results

#### Description

Enrich Google SecOps FileHash or URL entities with the previously completed analysis tasks results.

**Note:** Action supports filehash entity in md-5, sha-1 and sha-256 formats. Action always fetches the latest analysis available for the provided entity in Lastline.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threshold | Integer | 70 | Yes | Mark entity as suspicious if the score value for the entity is above the specified threshold.  
Search in last x scans | Integer | 25 | Yes | Search for report for provided entity in last x analysises executed in Lastline.  
Create Insight? | Checkbox | Unchecked | No | Specify whether to create insight based on the report data.  
  
#### Run On

This action runs on the following entities:

  * File Hash (md-5, sha-1, sha-256)
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "success": 1,
        "data": {
            "submission": "2021-03-14 04:46:11",
            "expires": "2021-03-16 04:46:10",
            "task_uuid": "5801c22ce6b4001003e58377051920f2",
            "reports": [
                {
                    "relevance": 1.0,
                    "report_uuid": "36150b54987b7f8bIUnzQWg2UgKxu8qdz7caWKwqyWz1yyE1aFpa9g",
                    "report_versions": [
                        "ll-pcap"
                    ],
                    "description": "Pcap analysis"
                },
                {
                    "relevance": 1.0,
                    "report_uuid": "a03998ee0d483efaRlYorEk0lbJUBcMXkYP1YfeGpQTufOFDWraR5Q",
                    "report_versions": [
                        "ll-web"
                    ],
                    "description": "Dynamic analysis in instrumented Chrome browser"
                }
            ],
            "submission_timestamp": "2021-03-15 03:58:51",
            "child_tasks": [
                {
                    "task_uuid": "772d23d8d59500100f87aac889c70ece",
                    "score": 0,
                    "tag": "network traffic analysis",
                    "parent_report_uuid": "a03998ee0d483efaRlYorEk0lbJUBcMXkYP1YfeGpQTufOFDWraR5Q"
                }
            ],
            "score": 0,
            "malicious_activity": [
                "Info: A Domain / URL of high reputation was visited"
            ],
            "analysis_subject": {
                "url": "https://yahoo.com"
            },
            "last_submission_timestamp": "2021-03-15 03:58:51"
        }
    }
    

##### Entity Enrichment

**Option 1. URL**

Enrichment Field Name | Logic - When to apply  
---|---  
IsSuspicous | Entity should be marked as suspicious if specific threshold is met.  
Lastline.Submission_Timestamp | Always  
Lastline.Latest_Submission_Timestamp | Always  
Lastline.Results_Expiry_Timestamp | Always  
Lastline.Analysis_Task_UUID | Always  
Lastline.Score | Always  
Lastline.Malicious_Activity | Always  
  
**Option 2. File**

Enrichment Field Name | Logic - When to apply  
---|---  
IsSuspicous | Entity should be marked as suspicious if specific threshold is met.  
Lastline.Submission_Timestamp | Always  
Lastline.Latest_Submission_Timestamp | Always  
Lastline.Results_Expiry_Timestamp | Always  
Lastline.Analysis_Task_UUID | Always  
Lastline.Score | Always  
Lastline.Malicious_Activity | Always  
Lastline.md5 | Always  
Lastline.sha1 | Always  
Lastline.sha256 | Always  
Lastline.mime\\_type | Always  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If successful and fetched the result:** "Successfully fetched the analysis results for the {0} {1}".format(url_or_filehash, value)  
****
  * **If incorrect url or file was provided (is_success=false):** "Failed to fetch the analysis results for the {0}".format(url_or_file)  
****
  * **If nothing was found (is_success=false):** "No previously completed analysis tasks were found based on the provided parameters for entity {0}".format(url_or_hash)  
****
  * **If unsupported entity was provided to the action (is_success=false):** "Entity type {0} is not supported by the action, only URL of Filehash are supported, skipping this entity type".format(entity.type)  
****
  * **If other non critical error happened (is_success=false):** "Failed to create analysis task for the url {0}. Error is {1}".format(url,entity_identifier)  
****

**The action should fail and stop a playbook execution:**

  * **if account credentials are incorrect:** "Failed to connect to the Lastline service with the provided account. Please check your configuration. Error is {0}".format(exception.stacktrace)  
****
  * **if other critical error:** "Failed to connect to the Lastline service! Error is {0}".format(exception.stacktrace)

| General  
Table (for URL) | **Table Name:** "{0} Analysis Results".**Table Columns:** Submission_TimestampLatest_Submission_TimestampResults_Expiry_TimestampAnalysis_Task_UUIDScoreMalicious_Activity | General  
Table (for FileHash) | **Table Name:** "{0} Analysis Results".**Table Columns:** Submission_TimestampLatest_Submission_TimestampResults_Expiry_TimestampAnalysis_Task_UUIDScoreMalicious_Activitymd5_hashsha1_hashsha256_hashmime_type | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
