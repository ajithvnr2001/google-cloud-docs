---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cynet/
title: Cynet \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:57:46.090503+00:00
---

# Cynet  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cynet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cynet

This document describes how to integrate Cynet with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Cynet.zip).

## Configure Cynet integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Delete Hash in Host

#### Description

Delete the file remediation action.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
13590 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult": 13590,
       "Entity": "0DC213FE4551740E12CAC575A9880753A9DACD510533F31BD7F635E743A7605"
    }]
    

### Hash Query

#### Description

Retrieve all the information about a specific file.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
meta_copyright | Returns if it exists in JSON result  
common_filename | Returns if it exists in JSON result  
occurrences | Returns if it exists in JSON result  
meta_product_name_and_version | Returns if it exists in JSON result  
first_seen | Returns if it exists in JSON result  
is_whitelisted | Returns if it exists in JSON result  
imports_winsock | Returns if it exists in JSON result  
meta_description | Returns if it exists in JSON result  
meta_companyName | Returns if it exists in JSON result  
risk_level | Returns if it exists in JSON result  
has_autorun_occurrences | Returns if it exists in JSON result  
meta_original_filename | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
has_program_files_folder_occurrences | Returns if it exists in JSON result  
common_path | Returns if it exists in JSON result  
certificate_thumbprint | Returns if it exists in JSON result  
certificate_name | Returns if it exists in JSON result  
certificate_root_name | Returns if it exists in JSON result  
alert_severity_level | Returns if it exists in JSON result  
ssdeep | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
has_hidden_window_occurrences | Returns if it exists in JSON result  
alert_product_name | Returns if it exists in JSON result  
imports_wininet | Returns if it exists in JSON result  
domains | Returns if it exists in JSON result  
last_seen | Returns if it exists in JSON result  
imports_ntdll | Returns if it exists in JSON result  
av_detections | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "meta_copyright": "Copyright (C) 2000",
        "common_filename": "ipscan.exe",
        "has_sockets": "false",
        "occurrences": [{
            "file_type": "PROCESS",
            "creation_time": "2017-12-15T14:34:41Z",
            "owner_user": "builtin\\\\administrators",
            "last_run_time": "2017-12-15T14:34:41Z",
            "hostname": "host1",
            "commandline_parameters": "C:\\\\DocumenteD\\\\___soft\\\\IP_Tools\\\\IPscan\\\\ipscan.exe",
            "filename": "ipscan.exe",
            "parent_path": "c:\\\\windows\\\\explorer.exe",
            "sha256": "40DC213FE4551740E12CAC575A9880753A9DACD510533F31BD7F635E743A7605",
            "running_user": "cabuk\\\\r610739",
            "full_path":"c:\\\\documented\\\\___soft\\\\ip_tools\\\\ipscan\\\\ipscan.exe"
        }],
        "meta_product_name_and_version": " 0.0.0.0",
        "first_seen": "2016-12-27T15:07:53Z",
        "is_whitelisted": "false",
        "imports_winsock": "false",
        "meta_description": "Angry IP scanner",
        "meta_companyName": "Angryziber Software",
        "risk_level": 1000,
        "has_autorun_occurrences": "false",
        "meta_original_filename": "ipscan.exe",
        "sha256": "40DC213FE4551740E12CAC575A9880753A9DACD510533F31BD7F635E743A7605",
        "has_program_files_folder_occurrences": "false",
        "common_path": "c:\\\\documented\\\\___soft\\\\ip_tools\\\\ipscan\\\\ipscan.exe",
        "certificate_thumbprint": "0000000000000000000000000000000000000000",
        "certificate_name": "",
        "certificate_root_name": "",
        "alert_severity_level": "Critical",
        "ssdeep": "",
        "md5": "6C1BCF0B1297689C8C4C12CC70996A75",
        "sha1": "",
        "has_hidden_window_occurrences": "true",
        "alert_product_name": "Angry IP Scanner - Cynet.Scanner.Angry IP Scanner",
        "imports_wininet": "false",
        "domains": [],
        "last_seen": "2018-02-28T11:26:32Z",
        "imports_ntdll": "false",
        "av_detections": 22
    }
    

### Kill Hash in Host

#### Description

Kill the process file remediation action.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": 13590,
            "Entity": "0DC213FE4551740E12CAC575A9880753A9DACD510533F31BD7F635E743A7605"
        }
    ]
    

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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Quarantine Hash in Host

#### Description

Action to remediate the quarantined file.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": 13590,
            "Entity": "0DC213FE4551740E12CAC575A9880753A9DACD510533F31BD7F635E743A7605"
        }
    ]
    

### Remediation Status

#### Description

Get the remediation status based on the remediation ID.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remediation ID | String | N/A | e.g. 312.  
  
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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "status": 24,
      "statusInfo": "File does not exist",
      "id": 13592
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
