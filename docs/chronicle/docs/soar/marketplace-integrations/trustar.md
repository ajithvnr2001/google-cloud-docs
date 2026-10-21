---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trustar/
title: TruSTAR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:12.760950+00:00
---

# TruSTAR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trustar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TruSTAR

**Important:** TruSTAR was acquired by Splunk and became part of Splunk Intelligence Management.

This document provides guidance on how to integrate TruSTAR with Google SecOps.

## Use Cases

Perform enrichment actions.

## Configure TruSTAR integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.trustar.co | Yes | TruSTAR API root  
API Key | String | N/A | Yes | TruSTAR API key  
API Secret | Password |  | Yes | TruSTAR API secret  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the TruSTAR server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Where To Find API Token and API Secret

  1. Navigate to https://station.trustar.co/settings/api
  2. Copy "Client ID" and "Client Secret" and put them in the integration configuration
  3. Execute test run.



## Actions

### Ping

#### Description

Test connectivity to TruSTAR with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
**if successful:** "Successfully connected to the TruSTAR server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the TruSTAR server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from TruSTAR. Supported entities: All.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Level Threshold | DDL | LowDefault values:BenignLowMediumHigh | Yes | Specify what should be the lowest security level for the entity to be marked as suspicious.  
Enclave Filter | CSV |  | No | Specify a comma-separated list of enclave names that should be used during the enrichment.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "indicatorType": "URL",
        "value": "http://esmne052.top/downfiles/lv.exe",
        "correlationCount": 0,
        "priorityLevel": "NOT_FOUND",
        "noteCount": 0,
        "sightings": 3,
        "firstSeen": 1617901588427,
        "lastSeen": 1617923344643,
        "enclaveIds": [
            "b850e851-27e3-4cc2-9269-69ac0aad63b1",
            "85313bc9-deb4-4022-ac03-923adcee9298",
            "cf777992-5dde-4d08-aef2-5e7c13951f54"
        ],
        "tags": [
            {
                "guid": "385a631d-fe0a-4657-ab4b-b201d48bf58c",
                "name": "api-tag",
                "enclaveId": "85313bc9-deb4-4022-ac03-923adcee9298"
            }
        ],
        "source": "",
        "notes": [],
        "guid": "URL|http://esmne052.top/downfiles/lv.exe",
        "summaries": [
            {
                "reportId": "970da023-e974-4223-80be-4b83c85583d9",
                "updated": 1617900133000,
                "enclaveId": "cf777992-5dde-4d08-aef2-5e7c13951f54",
                "source": {
                    "key": "virustotal",
                    "name": "VirusTotal"
                },
                "type": "URL",
                "value": "http://esmne052.top/downfiles/lv.exe",
                "score": {
                    "name": "Positives/Total Scans",
                    "value": "12/85"
                },
                "attributes": [
                    {
                        "name": "Scan Date",
                        "value": 1617900133000
                    },
                    {
                        "name": "Websites with Positive Detections",
                        "value": [
                            "AegisLab WebGuard",
                            "AlienVault",
                            "CRDF",
                            "ESET",
                            "Emsisoft",
                            "Fortinet",
                            "G-Data",
                            "Kaspersky",
                            "Spamhaus",
                            "URLhaus",
                            "VX Vault",
                            "benkow.cc"
                        ]
                    }
                ],
                "severityLevel": 1
            },
        ]
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
sightings | When available in JSON  
first_seen | When available in JSON  
last_seen | When available in JSON  
tags | When available in JSON  
source | When available in JSON  
security_level | When available in JSON  
report_link | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if enriched some(is_success = true):** "Successfully enriched the following entities using TruSTAR:\n".format(entity.identifier)  
******If didn't enrich some (is_success = true):** "Action wasn't able to enrich the following entities using TruSTAR:\n".format(entity.identifier)  
******If didn't enrich all (is_success = false):** "No entities were enriched".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)  
******If one of the enclaves were not found:** "Error executing action "Enrich Entities". Reason: the following enclaves were not found: {0}. Please check the spelling or use the action "List Enclaves" to find the valid enclaves.''.format(enclave names) | General  
Entity Table | Same Columns as in the Enrichment table, but without prefix. | Entity  
  
### Get Related IOCs

#### Description

Get information about IOCs that are related to the provided entities. Supported entities: All.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Max IOCs To Return | Integer | 50 | No | Specify how many IOCs to return. Default: 50. Maximum: 1000.  
Enclave Filter | CSV |  | No | Specify a comma-separated list of enclave names that should be used during the enrichment.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "{indicatorType_1}": ["{value_1}"],
        "{indicatorType_2}": ["{value_2}"]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if at least one IOC was found(is_success = true):** "Successfully returned related IOCs for the provided entities in TruSTAR".  
******If no IOCs were found(is_success=false)** "No related IOCs were found for the provided entities in TruSTAR".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Related IOCs". Reason: {0}''.format(error.Stacktrace)  
******If non 200 response:** "Error executing action "Get Related IOCs". Reason: {0}''.format(message)  
******If one of the enclaves were not found:** "Error executing action "Get Related IOCs". Reason: the following enclaves were not found: {0}. Please check the spelling or use the action "List Enclaves" to find the valid enclaves.''.format(enclave names) | General  
Case Wall Table  
| **Name:**_**Statistics**_**Columns:** TypeCount  | General  
  
### Get Related Reports

#### Description

Get information about reports related to the entities. Supported entities: All.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Yes | No | If enabled, action will create an insight containing information about reports related to the entities.  
Include Report Body In Insight | Checkbox | No | No | If enabled, insight will contain information about the report body. Note: report body can be very big in size.  
Enclave Filter | CSV |  | No | Specify a comma-separated list of enclave names that should be used during the enrichment.  
Max Reports To Return | Integer |  | No | Specify how many reports to return. Default: 10. Maximum: 25.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "id": "b8decde8-a68e-4961-aa0b-e07474e394b0",
        "created": 1615928416710,
        "updated": 1615928416710,
        "title": "35201",
        "distributionType": "ENCLAVE",
        "submissionStatus": "PROCESSED",
        "timeBegan": 1615928416187,
        "reportBody": "Event # 1\n   Source IP: 4.2.2.2\n   Destination IP: 10.250.250.25\n   Raw Event: <114>Mar 16 22:04:21 SyslogAlertForwarder: |6863274412612564368|Signature|2021-03-16 22:04:20 GMT+02:00|\"DNS: Microsoft SMTP Service DNS resolver overflow\"|0x40302f00|High|ms-smtp-dns-resolver-overflow|Medium|My Company|BDCFailover|3A-3B|4.2.2.2|53|10.250.250.25|1027|Inbound|buffer-overflow",
        "externalTrackingId": "qradar-offence-35201",
        "enclaveIds": [
            "28177710-9cb8-aa2f-29e8-135c14365e80"
        ],
        "tags": [
            {
                "guid": "sense offense",
                "name": "sense offense",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "host logout",
                "name": "host logout",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "service stopped",
                "name": "service stopped",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "object access success",
                "name": "object access success",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "process creation success",
                "name": "process creation success",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "information",
                "name": "information",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "user privilege",
                "name": "user privilege",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            },
            {
                "guid": "user login failure",
                "name": "user login failure",
                "enclaveId": "28177710-9cb8-aa2f-29e8-135c14365e80"
            }
        ]
    }
    

##### Entity Insight

![Get Related Reports insight
example](https://docs.cloud.google.com/static/chronicle/images/integrations/trustar-get-related-reports-insight.png)

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if one report is found (is_success = true):** "Successfully returned related reports for the provided entities in TruSTAR".  
******If no reports are found (is_success=false)** "No related reports were found in TruSTAR"  
****  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Related Reports". Reason: {0}''.format(error.Stacktrace)******If none 200 response:** "Error executing action "Get Related Reports". Reason: {0}''.format(message)  
******If one of the enclaves were not found:** "Error executing action "Get Related Reports". Reason: the following enclaves were not found: {0}. Please check the spelling or use the action "List Enclaves" to find the valid enclaves.''.format(enclave names) | General  
Case Wall | **Title:** Related Reports**Columns:** Title Tags  | General  
  
### List Enclaves

#### Description

List available enclaves in TruSTAR.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String |  | No | Specify what value should be used in the filter.  
Max Enclaves To Return | Integer | 50 | No | Specify how many enclaves to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "name": "COVID-19 OSINT Community Enclave",
            "templateName": "COVID-19",
            "workflowSupported": false,
            "read": true,
            "create": false,
            "update": false,
            "id": "b0a7be7b-a847-4597-9e1d-20ae18c344ea",
            "type": "OPEN"
        },
        {
            "name": "Hybrid Analysis Public Feed",
            "templateName": "Open Source",
            "workflowSupported": false,
            "read": true,
            "create": false,
            "update": false,
            "id": "2eeccced-c740-4ad9-aa5c-82744cd1f6aa",
            "type": "OPEN"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if one enclave is found (is_success = true):** "Successfully returned available enclaves in TruSTAR".  
******If no enclaves are found (is_success=false):** "No related enclaves were found in TruSTAR"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Enclaves". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Title:** Related Reports**Columns:** Name Read CreateUpdate IDType | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
