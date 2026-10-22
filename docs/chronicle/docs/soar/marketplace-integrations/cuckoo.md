---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cuckoo/
title: Cuckoo \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:06.445569+00:00
---

# Cuckoo  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cuckoo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cuckoo

This document describes how to integrate Cuckoo with Google Security Operations.

## Configure Cuckoo integration in Google Security Operations

### Configure Cuckoo integration with a CA certificate

You can verify your connection with a CA certificate file if needed.

Before you start, ensure you have the following:

  * The CA certificate file
  * The latest Cuckoo integration version



To configure the integration with a CA certificate, complete the following steps:

  1. Parse your CA certificate file into a Base64 String.
  2. Open the integration configuration parameters page.
  3. Insert the string in the **CA Certificate File** field.
  4. To test that the integration is successfully configured, select the **Verify SSL** checkbox and click **Test**.



### Configure Cuckoo integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

#### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | http://x.x.x.x:8090 | Yes | Address of the Cuckoo instance.  
Web Interface Address | String | http://x.x.x.x:8000 | Yes | Address of the Cuckoo Web UI instance.  
Warning Threshold | Integer | 5.0 | Yes | N/A  
CA Certificate File | String | N/A | No | N/A  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Cuckoo connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
API Token | Password | N/A | No | API Token of the integration.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Detonate File

#### Description

Submit a file for analysis and get a report, also known as async.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Paths | String | N/A | Yes | The path of the file to submit.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
max_score | N/A | N/A  
  
##### JSON Result
    
    
    {
        "powershell8693919272434274241.ps1": {
            "info": {
                "category": "file",
                "added": 1547640117.991152,
                "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09",
                "package": "ps1",
                "started": 1547640190.471362,
                "route": "internet",
                "custom": null,
                "machine": {
                    "status": "stopped",
                    "shutdown_on": "2019-01-16 12:28:55",
                    "started_on": "2019-01-16 12:03:16",
                    "manager": "VirtualBox",
                    "label": "win7x6427",
                    "name": "win7x6427"
                },
                "ended": 1547641736.394026,
                "score": 6.6,
                "platform": "windows",
                "version": "2.0.6",
                "owner": null,
                "git": {
                    "head": "03731c4c136532389e93239ac6c3ad38441f81a7",
                    "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"
                },
                "options": "procmemdump=yes,route=internet",
                "id": 889621,
                "duration": 1545
            },
            "signatures":
            [{
                "families": [],
                "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic",
                "name": "network_cnc_http",
                "markcount": 1,
                "references": [],
                "marks":
                [{
                    "suspicious_features": "Connection to IP address",
                    "type": "generic",
                    "suspicious_request": "GET http://1.1.1.1:8080/"
                }],
                "severity": 2
            }, {
                "families": [],
                "description": "Connects to smtp.live.com, possibly for spamming or data exfiltration",
                "name": "smtp_live",
                "markcount": 1,
                "references": [],
                "marks":
                [{
                    "category": "domain",
                    "type": "ioc",
                    "ioc": "smtp.live.com",
                    "description": null
                }],
                "severity": 2
            }, {
                "families": [],
                "description": "Connects to smtp.mail.yahoo.com, possibly for spamming or data exfiltration",
                "name": "smtp_yahoo",
                "markcount": 1,
                "references": [],
                "marks":
                [{
                    "category": "domain",
                    "type": "ioc",
                    "ioc": "smtp.mail.yahoo.com",
                    "description": null
                }],
                "severity": 2
            }]
        }
    }
    

### Detonate URL

#### Description

Send an URL for analysis and get a report, also known as async.

#### Parameters

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "info": {
                    "category": "url",
                    "git": {
                        "head": "03731c4c136532389e93239ac6c3ad38441f81a7",
                        "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"
                    },
                    "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09",
                    "package": "ie",
                    "started": null,
                    "route": "internet",
                    "custom": null,
                    "machine": {
                        "status": "stopped",
                        "shutdown_on": "2019-01-16 13:14:26",
                        "label": "win7x6412",
                        "manager": "VirtualBox",
                        "started_on": "2019-01-16 12:48:54",
                        "name": "win7x6412"
                    },
                    "ended": 1547644467.207864,
                    "added": null,
                    "id": 889669,
                    "platform": null,
                    "version": "2.0.6",
                    "owner": null,
                    "score": 4.4,
                    "options": "procmemdump=yes,route=internet",
                    "duration": null
                },
                "signatures": [{
                    "families": [],
                    "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic",
                    "name": "network_cnc_http",
                    "markcount": 1,
                    "references": [],
                    "marks": [{
                        "suspicious_features": "Connection to IP address",
                        "type": "generic",
                        "suspicious_request": "GET http://1.1.1.1:8080/"
                    }],
                    "severity": 2
                }, {
                    "families": [],
                    "description": "Performs some HTTP requests",
                    "name": "network_http",
                    "markcount": 9,
                    "references": [],
                    "marks": [{
                        "category": "request",
                        "ioc": "GET http://crl.microsoft.com/pki/crl/products/WinPCA.crl",
                        "type": "ioc",
                        "description": null
                    }, {
                        "category": "request",
                        "ioc": "GET http://www.microsoft.com/pki/crl/products/WinPCA.crl",
                        "type": "ioc",
                        "description": null
                    }, {
                        "category": "request",
                        "ioc": "GET http://crl.microsoft.com/pki/crl/products/MicrosoftTimeStampPCA.crl",
                        "type": "ioc",
                        "description": null
                    }],
                    "severity": 2
                }, {
                    "families": [],
                    "description": "Communicates with host for which no DNS query was performed",
                    "name": "nolookup_communication",
                    "markcount": 11,
                    "references": [],
                    "marks": [{
                        "host": "1.1.1.1",
                        "type": "generic"
                    }, {
                        "host": "1.1.1.1",
                        "type": "generic"
                    }, {
                        "host": "1.1.1.1",
                        "type": "generic"
                    }],
                    "severity": 3
                }]},
            "Entity": "http://digi.ba/eng/#pgc-56-0-0"
        }
    ]
    

##### Entity Enrichment

Entity is marked as suspicious (True) if the score exceeds the threshold. Otherwise: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Cuckoo_Score | N/A  
task_id | N/A  
  
### Get Report

#### Description

Get a report of a particular task by the ID, also known as async.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Task ID | String | N/A | Yes | The task's ID. Example: 10  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
score | N/A | N/A  
  
##### JSON Result
    
    
    {
        "info": {
            "category": "file",
            "added": 1547640117.991152,
            "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09",
            "package": "ps1",
            "started": 1547640190.471362,
            "route": "internet",
            "custom": null,
            "machine": {
                "status": "stopped",
                "shutdown_on": "2019-01-16 12:28:55",
                "started_on": "2019-01-16 12:03:16",
                "manager": "VirtualBox",
                "label": "win7x6427",
                "name": "win7x6427"
            },
            "ended": 1547641736.394026,
            "score": 6.6,
            "platform": "windows",
            "version": "2.0.6",
            "owner": null,
            "git": {
                "head": "03731c4c136532389e93239ac6c3ad38441f81a7",
                "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"
            },
            "options": "procmemdump=yes,route=internet",
            "id": 889621,
            "duration": 1545
        },
        "signatures": [{
            "families": [],
            "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic",
            "name": "network_cnc_http",
            "markcount": 1,
            "references": [],
            "marks": [{
                "suspicious_features": "Connection to IP address",
                "type": "generic",
                "suspicious_request": "GET http://1.1.1.1:8080/"
            }],
            "severity": 2
        }, {
            "families": [],
            "description": "Connects to smtp.live.com, possibly for spamming or data exfiltration",
            "name": "smtp_live",
            "markcount": 1,
            "references": [],
            "marks": [{
                "category": "domain",
                "type": "ioc",
                "ioc": "smtp.live.com",
                "description": null
            }],
            "severity": 2
        }, {
            "families": [],
            "description": "Connects to smtp.mail.yahoo.com, possibly for spamming or data exfiltration",
            "name": "smtp_yahoo",
            "markcount": 1,
            "references": [],
            "marks": [{
                "category": "domain",
                "type": "ioc",
                "ioc": "smtp.mail.yahoo.com",
                "description": null
            }],
            "severity": 2
        }]
    }
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
