---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nessusscanner/
title: Nessus scanner \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:31:12.520950+00:00
---

# Nessus scanner  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nessusscanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Nessus scanner

This document provides guidance on how to integrate Nessus scanner with Google SecOps.

## Configure Nessus scanner to work with Google Security Operations

### Generate API Key

  1. In Nessus click **Settings** in the top navigation bar, and the **About Page** will appear.
  2. In the left navigation bar, click **My Account** , and then the **My Account** page appears.
  3. Click the **API Keys** tab.
  4. Click **Generate**. A dialog box appears, confirming your selection to generate a new API key.
  5. Click **Generate again,** and your new API key will appear.



An API Key consists of an Access Key and a Secret Key. API Keys authenticate with the **Nessus REST API** (version 6.4 or greater) and pass with requests using the `X-ApiKeys` HTTP header.

  * API Keys are only provided upon initial generation, therefore it is recommended to store your API keys in a safe location.
  * API Keys cannot be retrieved by Nessus. If you lose your API Key, you must generate a new API Key.
  * Regenerating an API Key will immediately rid of any applications currently using the key.
  * For configuring or launching scans, you can not directly access Nessus scanning APIs, except as permitted as part of enterprise solutions Tenable.sc and Tenable.io.
  * For detailed information on Nessus scanner API keys, see the [Nessus Documentation Portal](https://docs.tenable.com/nessus/Content/GenerateAnAPIKey.htm).



## Configure Nessus scanner integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Create Scan

#### Description

Create a new scan in Nessus with a template.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Scan Name | String | N/A | Scan display name.  
Scan Template Title | String | N/A | Scan template title value.  
Description | String | N/A | Description content.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
     "dashboard_file": null,
     "scanner_id": 1,
     "last_modification_date": 1548175315,
     "creation_date": 1548175315,
     "user_permissions": 128,
     "owner": "admin",
     "timezone": null,
     "id": 317,
     "description": "",
    "Uuid": "template-21bcfdad-2e39-818b-3d52-c52418a107fe29a0c3da8dfc1037",
     "sms": null,
     "shared": 0,
     "type": "public",
     "owner_id": 2,
     "rrules": null,
     "scan_time_window": null,
     "container_id": 0,
     "tag_id": 100,
     "notification_filters": null,
     "default_permisssions": 0,
     "emails": null,
     "name": "test",
     "custom_targets": "1.1.1.1",
     "enabled": true,
     "use_dashboard": false,
     "starttime": null,
     "policy_id": 316
     }
    

### Get Scan Report

#### Description

Get a full report on the scan results.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Scan Name | String | N/A | Scan display name.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_ succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
        "info": {
            "control": true,
            "edit_allowed": true,
            "hasaudittrail": true,
            "user_permissions": 128,
            "alt_targets_used": null,
            "targets": "1.1.1.1",
            "uuid": "22fcf2ad-a92f-7019-8f2c-8a07151abf01a66999472d31043b",
            "hostcount": 1,
            "object_id": 258,
            "acls": [{
                "display_name": "admin",
                "name": "admin",
                "owner": 1,
                "type": "user",
                "id": 2,
                "permissions": 128
            }],
            "policy": "AdvancedScan",
            "no_target": null,
            "scanner_name": "LocalScanner",
            "scan_end": 1521367948,
            "status": "completed",
            "scanner_end": 1521367945,
            "timestamp": 1521367948,
            "scan_type": "local",
            "scan_start": 1521367553,
            "folder_id": 100,
            "name": "Nessus",
            "haskb": true,
            "pci-can-upload": false,
            "scanner_start": 1521367553
        },
        "remediations": {
            "num_cves": 5,
            "remediations": null,
            "num_impacted_hosts": 0,
            "num_hosts": 1,
            "num_remediated_cves": 0},
        "vulnerabilities": [{
            "count": 1,
            "severity": 0,
            "plugin_family": "Windows",
            "vuln_index": 109,
            "severity_index": 0,
            "plugin_name": "WindowsTerminalServicesEnabled",
            "plugin_id": 10940
        }],
        "notes": null,
        "compliance": [],
        "hosts": [{
            "info": 80,
            "scanprogresscurrent": 1927,
            "medium": 10,
            "scanprogresstotal": 1927,
            "totalchecksconsidered": 1927,
            "host_index": 0,
            "hostname": "1.1.1.1",
            "numchecksconsidered": 1927,
            "high": 0, "score": 1120,
            "low": 4,
            "severitycount ": {
                "item": [{
                    "count": 80,
                    "severitylevel": 0
                }]},
            "host_id": 2,
            "progress": "1927-1927/95562-95562",
            "critical": 0,
            "severity": 94
        }],
        "filters": [{
            "control": {
                "regex": "^[0-9]+$",
                "readable_regex": "NUMBER",
                "type": "entry"
            },
            "operators": ["eq", "neq", "match"
                         ],
            "readable_name": "BugtraqID",
            "name": "bid"
        }],
        "comphosts": [],
        "history": [{
            "status": "completed",
            "uuid": "bc951f80-7c2b-745d-f386-b27c95151bf4d6d3fd07a9633969",
            "history_id": 260,
            "creation_date": 1519209387,
            "scheduler": 0,
            "last_modification_date": 1519209860,
            "alt_targets_used": false,
            "type": "local", "owner_id": 2
        }]
    }
    

### Get Scan Templates

#### Description

Get all scan templates from the server.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
        "Templates": [{
            "name": "wannacry",
            "title": "WannaCryRansomware",
            "is_agent": null,
            "unsupported": false,
            "manager_only": false,
            "desc": "RemoteandlocalchecksforMS17-010.",
            "subscription_only": false,
            "uuid": "861a8b95-f04c-40b0-ece6-263b1bec457c09cfc122c9666645"
        }]
    }
    

### Get Scans

#### Description

Fetch a list of existing scans.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    {
        "Scans":
        [{
            "status": "completed",
            "control": true,
            "uuid": "024f0bff-489f-6677-ea7f-84545c1b4223579810b0b97f6d01",
            "read": true,
            "last_modification_date": 1538656691,
            "enabled": true,
            "creation_date": 1521364372,
            "user_permissions": 128,
            "folder_id": 100,
            "starttime": null,
            "shared": false,
            "owner": "admin",
            "timezone": null,
            "rrules": null,
            "type": "local",
            "id": 279,
            "name": "Nessus-test"
        }]
    }
    

### Launch Scan

#### Description

Launch a scan on the Nessus server.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Scan Name | String | N/A | Scan display name.  
  
#### Use cases

N/A

#### Run On

N/A

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
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

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

## Jobs

### Launch Scan and get a Report

#### Description

A job for initiating a scan in Nessus and getting a scan report.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
API Root | 2 | N/A | N/A  
Access Key | 2 | N/A | N/A  
Secret Key | 2 | N/A | N/A  
Scan Name | 2 | N/A | N/A  
Scan Download Path | 2 | N/A | N/A  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
