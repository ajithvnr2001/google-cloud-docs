---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-security-complete-cloud/
title: Symantec Endpoint Security Complete Cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:32.931081+00:00
---

# Symantec Endpoint Security Complete Cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-security-complete-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Endpoint Security Complete Cloud

**Important:** This integration refers to Symantec Endpoint Security Complete.

This document provides guidance on how to integrate Symantec Endpoint Security Complete Cloud with Google SecOps.

## Use Cases

Perform enrichment actions.

## Configure Symantec Endpoint Security Complete Cloud integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.sep.securitycloud.symantec.com | Yes | Symantec Endpoint Security Complete API root  
Client ID | String | N/A | Yes | Symantec Endpoint Security Complete Client ID  
Client Secret | Password |  | Yes | Symantec Endpoint Security Complete Client Secret  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Symantec Endpoint Security Complete server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Symantec Endpoint Security Complete with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
**if successful:** "Successfully connected to the Symantec Endpoint Security Complete server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Symantec Endpoint Security Complete server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Symantec Endpoint Security Complete. Supported entities: Hostname, Hash, URL and IP Address. Only SHA256 hashes are supported.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Device Group | String | Default | Yes | Specify the name of the device group that should be used to retrieve information about endpoints.  
Create Endpoint Insight | Checkbox | Checked | No | If enabled, action will create an insight containing information about the endpoints.  
Create IOC Insight | Checkbox | Checked | No | If enabled, action will create an insight containing information about enriched IOCs.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * Hash
  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result - for Endpoint
    
    
    {
        "id": "x10bQZJsRi6z87se02g3Vw",
        "os": {
            "ver": "10.0.18363",
            "name": "Windows 10 Enterprise Edition",
            "type": "WINDOWS_WORKSTATION",
            "64_bit": true,
            "lang": "en",
            "major_ver": 10,
            "minor_ver": 0,
            "sp": 0,
            "tz_offset": -480,
            "user": "Admin",
            "user_domain": "LocalComputer",
            "vol_avail_mb": 5443,
            "vol_cap_mb": 30138
        },
        "name": "DESKTOP-8P0TH6Q",
        "host": "DESKTOP-8P0TH6Q",
        "domain": "WORKGROUP",
        "created": "2020-11-19T12:24:23.422Z",
        "modified": "2021-03-05T10:39:03.884Z",
        "adapters": [
            {
                "addr": "2001:db8::",
                "category": "Public",
                "ipv4Address": "192.0.2.182",
                "ipv4_gw": "192.0.2.1",
                "ipv4_prefix": 24,
                "ipv6Address": "2001:db8:1:1:1:1:1:1",
                "ipv6_gw": "192.0.2.1",
                "ipv6_prefix": 64,
                "mask": "255.255.255.0"
            }
        ],
        "device_status": "SECURE",
        "parent_device_group_id": "rujWDk9WTcKsnLkCeZKl7A",
        "products": [
            {
                "name": "Symantec Endpoint Protection",
                "product_status": "SECURE",
                "version": "14.3.3384.1000",
                "agent_status": "ONLINE",
                "last_connected_time": "2021-03-05T10:39:23.271Z",
                "features": [
                    {
                        "name": "APP_ISOLATION",
                        "state": "ENABLED",
                        "feature_status": "SECURE",
                        "engine_version": "6.7.0.2033"
                    },
                    {
                        "name": "FIREWALL",
                        "state": "ENABLED",
                        "feature_status": "SECURE"
                    }
                ]
            }
        ]
    }
    

##### JSON Result - for IOC's
    
    
    {
        "reputation": "BAD",
        "prevalence": "LessThanFifty",
        "firstSeen": "2021-04-01",
        "lastSeen": "2021-04-03",
        "targetOrgs": {
            "topCountries": [
                "us",
                "cm",
                "sg"
            ],
            "topIndustries": [
                "financial services"
            ]
        },
        "state": "blocked",
        "process_chain": [
            {
                "parent": {
                    "parent": {
                        "file": "6a671b92a69755de6fd063fcbe4ba926d83b49f78c42dbaeed8cdb6bbc57576a",
                        "processName": "explorer.exe"
                    },
                    "file": "f686f2ff41923bb5c106c76d5f3df30146eb37683b81c4a57110dcc63032526a",
                    "processName": "chrome.exe"
                }
            }
        ]
    }
    

##### Entity Enrichment - for Endpoint

Enrichment Field Name | Logic - When to apply  
---|---  
id | When available in JSON  
os | When available in JSON  
hostname | When available in JSON  
domain | When available in JSON  
ips | When available in JSON  
mac |   
status | When available in JSON  
link | When available in JSON  
  
##### Entity Enrichment - for IOC's

Enrichment Field Name | Logic - When to apply  
---|---  
reputation | When available in JSON  
prevalence | When available in JSON  
countries | When available in JSON  
first_seen | When available in JSON  
last_seen | When available in JSON  
industries | When available in JSON  
state | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if enriched some(is_success = true):** "Successfully enriched the following entities using Symantec Endpoint Security Complete:\n".format(entity.identifier)  
**If didn't enrich some (is_success = true):** "Action wasn't able to enrich the following entities using Symantec Endpoint Security Complete:\n".format(entity.identifier)  
******If didn't enrich all (is_success = false):** "No entities were enriched".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)******If invalid device group:** "Error executing action "Enrich Entities". Reason: the provided device group wasn't found. Please check the spelling.' | General  
Entity Table | **** | Entity  
  
### List Device Groups

#### Description

List available device groups in Symantec Endpoint Security Complete.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains  
| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter.  
Max Groups To Return | Integer | 50 | No | Specify how many groups to return. Default: 50.  
  
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
        "total": 1,
        "device_groups": [
            {
                "id": "rujWDk9WTcKsnLkCeZKl7A",
                "name": "Default",
                "created": "2020-11-19T02:17:15.236Z",
                "modified": "2020-11-19T02:17:17.482Z",
                "parent_id": ""
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if 200 and data is available (is_success = true):** "Successfully returned available device groups in Symantec Endpoint Security Complete.".  
******If 200 and no data is available (is_success=false)** "No device groups were found based on the provided criteria in Symantec Endpoint Security Complete."  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Device Groups". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** Available Device Groups**Columns:** ID Name  | General  
  
### Get Related IOCs

#### Description

Get IOCs related to the entities from Symantec Endpoint Security Complete. Supported entities: Hash, URL and IP Address. Only SHA256 hashes are supported.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Source Filter | CSV | byThreatActor,  
byProcessChain,  
bySignature,  
bySampleTraits,  
byNetworkingTrait,  
bySimilarIncidents | No | Specify the source filter. If nothing is provided, action will return related entities, based on all sources.   
**Possible Values:** byThreatActor, byProcessChain, bySignature, bySampleTraits, byNetworkingTrait,bySimilarIncidents  
  
#### Run On

This action runs on the following entities:

  * Hash
  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "total": 1,
        "device_groups": [
            {
                "id": "rujWDk9WTcKsnLkCeZKl7A",
                "name": "Default",
                "created": "2020-11-19T02:17:15.236Z",
                "modified": "2020-11-19T02:17:17.482Z",
                "parent_id": ""
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if 200 (is_success = true):** "Successfully returned related IOCs for the provided entities from Symantec Endpoint Security Complete.".  
******if no IOCs were found (is_success = false):** "No related IOCs were found for the provided entities from Symantec Endpoint Security Complete.".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Related IOCs". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
