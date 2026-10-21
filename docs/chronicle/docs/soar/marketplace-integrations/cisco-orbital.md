---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-orbital/
title: Cisco Orbital \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:23.784065+00:00
---

# Cisco Orbital  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-orbital/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco Orbital

This document describes how to integrate Cisco Orbital with Google Security Operations.

## Use Cases

Perform active actions - execute SQL queries to get more information about the endpoint.

## Configure Cisco Orbital Integration to work with Google Security Operations

### Product Permission

In order to authenticate, you need to generate a token and use this token in API requests.

### How to generate Client ID and Client Secret

To generate Client ID and Client Secret, you need to perform the following steps:

  1. Login into Cisco Orbital.
  2. Navigate to the account settings and click **Create API Credentials**.
  3. Fill out the fields.
  4. Copy Client ID and Client Secret.



## Configure Cisco Orbital integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Client ID | String | N/A | Yes | Client ID of the Cisco Orbital account.  
Client Secret | Password | N/A | Yes | Client Secret of the Cisco Orbital account.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the Cisco Orbital server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Cisco Orbital with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters..

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully connected to the Cisco Orbital server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ ****"Failed to connect to the Cisco Orbital server! Error is {0}".format(exception.stacktrace) | General  
  
### Execute Query

#### Description

Execute queries on endpoints based on IP and Hostname entities in Cisco Orbital.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query that needs to be executed.  
Name | String | N/A | No | Specify the name for the query job. If nothing is specified, the action uses a name in the following format: `PRODUCT_NAME-GUID`  
Custom Context Fields | String | N/A | No | Specify additional custom context fields that should be added to the job. Format: key_1:value_1,key_2:value_1.  
Max Results To Return | Integer | 100 | No | Specify how many results should be returned.  
Hide Case Wall Table | Checkbox | N/A | No | If enabled, action will not prepare a case wall table.  
Timeout | Integer | 1 | No | Specify how many minutes to wait for results before finishing action execution. Maximum: 5 minutes. **Default:** 1 minute.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "results": [
            {
                "node": "eXHZw6pLMxepKQtf9B8VTQ",
                "osQuery": [
                    {
                        "sql": "SELECT name,pid FROM processes;"
                    }
                ],
                "osQueryResult": [
                    {
                        "types": [
                            "",
                            ""
                        ],
                        "columns": [
                            "name",
                            "pid"
                        ],
                        "values": [
                            "[System Process]",
                            "0",
                            "System",
                            "4",
                            "Registry",
                            "88",
                            "smss.exe",
                            "516",
                            "csrss.exe",
                            "596",
                            "wininit.exe",
                            "672",
                            "csrss.exe",
                            "680",
                            "winlogon.exe",
                            "724",
                            "services.exe",
                            "796",
                            "lsass.exe",
                            "804",
                            "svchost.exe",
                            "916",
                            "fontdrvhost.exe",
                            "936",
                            "svchost.exe",
                            "944",
                            "svchost.exe",
                            "1020",
                            "svchost.exe",
                            "296",
                            "fontdrvhost.exe",
                            "560",
                            "dwm.exe",
                            "1048",
                            "svchost.exe",
                            "1136",
                            "svchost.exe",
                            "1144",
                            "svchost.exe",
                            "1192",
                            "svchost.exe",
                            "1256",
                            "svchost.exe",
                            "1280",
                            "svchost.exe",
                            "1372",
                            "svchost.exe",
                            "1392",
                            "svchost.exe",
                            "1488",
                            "svchost.exe",
                            "1504",
                            "svchost.exe",
                            "1552",
                            "svchost.exe",
                            "1604",
                            "svchost.exe",
                            "1716",
                            "svchost.exe",
                            "1724",
                            "svchost.exe",
                            "1804",
                            "svchost.exe",
                            "1812",
                            "svchost.exe",
                            "1964"
                        ],
                        "error": "",
                        "secs": 0.06800670176744461,
                        "label": "",
                        "name": ""
                    }
                ],
                "error": {
                    "en": ""
                },
                "hostinfo": {
                    "osinfo": {
                        "os": "windows",
                        "osname": "Windows 10 Enterprise Evaluation",
                        "release": "6.3",
                        "version": "10.0.18363",
                        "arch": "amd64"
                    },
                    "hostname": "TIP-HW-HOST-034",
                    "interfaces": {
                        "Ethernet0": {
                            "name": "Ethernet0",
                            "mac": "00:50:56:a2:05:8b",
                            "ipv4": "172.30.202.128/24",
                            "ipv6": "fe80::983:e8ed:c392:3e3e/64",
                            "active": true
                        }
                    },
                    "external": {
                        "name": "",
                        "mac": "",
                        "ipv4": "185.180.102.139",
                        "active": true
                    },
                    "updated": "2020-10-12T12:03:30.1329732Z",
                    "version": "v1.7.6"
                },
                "rowcount": 149,
                "context": {
                    "description": "front desk",
                    "lol": "kek",
                    "value": "anything\"}"
                }
            },
            {
                "node": "oHNPQUeWwK1ql3R2J13GSw",
                "osQuery": [
                    {
                        "sql": "SELECT name,pid FROM processes;"
                    }
                ],
                "osQueryResult": [
                    {
                        "types": [
                            "",
                            ""
                        ],
                        "columns": [
                            "name",
                            "pid"
                        ],
                        "values": [
                            "[System Process]",
                            "0",
                            "System",
                            "4",
                            "Registry",
                            "88",
                            "smss.exe",
                            "360",
                            "csrss.exe",
                            "440",
                            "wininit.exe",
                            "520",
                            "csrss.exe",
                            "536",
                            "winlogon.exe",
                            "616",
                            "services.exe",
                            "656",
                            "lsass.exe",
                            "664",
                            "svchost.exe",
                            "772",
                            "fontdrvhost.exe",
                            "784",
                            "fontdrvhost.exe",
                            "792",
                            "svchost.exe",
                            "864",
                            "svchost.exe",
                            "6852",
                            "SystemSettings.exe",
                            "7864",
                            "YourPhone.exe",
                            "5160",
                            "RuntimeBroker.exe",
                            "516",
                            "dllhost.exe",
                            "1496"
                        ],
                        "error": "",
                        "secs": 0.025061199441552162,
                        "label": "",
                        "name": ""
                    }
                ],
                "error": {
                    "en": ""
                },
                "hostinfo": {
                    "osinfo": {
                        "os": "windows",
                        "osname": "Windows 10 Enterprise Evaluation",
                        "release": "6.3",
                        "version": "10.0.18363",
                        "arch": "amd64"
                    },
                    "hostname": "TIP-HW-HOST-033",
                    "fqdn": {
                        "127.0.0.1": "www.virustotal.com"
                    },
                    "interfaces": {
                        "Ethernet0": {
                            "name": "Ethernet0",
                            "mac": "00:50:56:a2:66:8a",
                            "ipv4": "172.30.202.127/24",
                            "ipv6": "fe80::84:5a0f:7973:63/64",
                            "active": true
                        }
                    },
                    "external": {
                        "name": "",
                        "mac": "",
                        "ipv4": "185.180.102.139",
                        "active": true
                    },
                    "updated": "2020-10-07T00:11:31.0951018Z",
                    "version": "v1.7.6"
                },
                "rowcount": 132,
                "context": {
                    "description": "front desk",
                    "lol": "kek",
                    "value": "anything\"}"
                }
            }
        ],
        "error": {
            "en": ""
        },
        "next": ""
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:** _If SQL query is executed without errors on one of the entities (is_success=true):_ "Successfully executed query and retrieved results from Cisco Orbital on the following entities:\n".format(entity.identifier) _If SQL query is not executed on some entities (is_success=true):_ "Action wasn't able to successfully execute query and retrieve results from Cisco Orbital on the following entities:\n".format(entity.identifier) _If the 400 status code is reported in the first response (is_success=false):_ "Action wasn't able to execute queries in Cisco Orbital. Reason: {0}".format(comma-separated list of errors) _If all of the results have an error:_ "Action wasn't able to execute queries on all provided entities in Cisco Orbital. Reason: errors in the query." _Async Message:_ "Submitted Query. Waiting for results until timeout." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, otheris reported:_ "Error executing action "List Buckets". Reason: {0}''.format(error.Stacktrace) _If the "Timeout" parameter is not in the 1-5 range:_ "Timeout value should be in range from 1 to 5." | General  
Case Wall Table For each result that doesn't have an error | _If entity type is hostname:_ **Table Name:** "Results for {0}".format(entity.identifier) _If other entity types:_ **Table Name:** "Results for {0} ({1})".format(entity.identifier, hostinfo/hostname) All of the columns from the response will be used as table columns. | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
