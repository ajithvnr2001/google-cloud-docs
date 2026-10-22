---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-threatgrid/
title: Cisco Threat Grid \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:43.082627+00:00
---

# Cisco Threat Grid  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-threatgrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco Threat Grid

**Important:** Cisco Threat Grid was renamed to Cisco Secure Malware Analytics.

This document describes how to integrate Cisco Secure Malware Analytics with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/CiscoThreatGrid.zip).

## Configure Cisco Threat Grid integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Hash Associated Domains

#### Description

Get domains associated with a given hash.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to Apply  
---|---  
cisco_threat_grid.get_associated_network | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": ["migsel.com"],
            "Entity": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"
        }
    ]
    

### Get Hash Associated IPs

#### Description

Get IPs associated with a given hash.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to Apply  
---|---  
cisco_threat_grid.get_associated_network | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": ["95.128.128.129",
                             "192.168.1.255",
                             "192.168.1.1"],
            "Entity": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"
        }
    ]
    

### Get Submissions

#### Description

Get submissions by entity.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Threshold | String | 50 | Mark as suspicious if max threat score pass the threshold.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Filehash
  * Hostname
  * Process
  * URL
  * Filename



#### Action Results

##### Entity Enrichment

Entity is marked as suspicious if the max score exceeds a threshold. Else: false.

Enrichment Field Name | Logic - When to Apply  
---|---  
Name | Returns if it exists in JSON result  
Submitted | Returns if it exists in JSON result  
Score | Returns if it exists in JSON result  
Indicators | Returns if it exists in JSON result  
SHA256 | Returns if it exists in JSON result  
MD5 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                "Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe",
                 "Submitted": "2018-06-13T09:16:12Z",
                 "Score": 95,
                 "Indicators": 20,
                 "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894",
                 "MD5": "5fa6b79842cec6d8d172fb16e56b7247"
                }, {
                    "Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe",
                    "Submitted": "2018-06-13T09:15:51Z",
                    "Score": 95,
                    "Indicators": 21,
                    "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894",
                    "MD5": "5fa6b79842cec6d8d172fb16e56b7247"
                }, {
                    "Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe",
                    "Submitted": "2018-06-13T09:14:38Z",
                    "Score": 95,
                    "Indicators": 20,
                    "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894",
                    "MD5": "5fa6b79842cec6d8d172fb16e56b7247"
                }, {
                    "Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe",
                    "Submitted": "2018-06-13T09:13:12Z",
                    "Score": 95,
                    "Indicators": 19,
                    "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894",
                    "MD5": "5fa6b79842cec6d8d172fb16e56b7247"
                }, {
                    "Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe",
                    "Submitted": "2018-06-13T09:12:27Z",
                    "Score": 95,
                    "Indicators": 19,
                    "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894",
                    "MD5": "5fa6b79842cec6d8d172fb16e56b7247"
                }
            ],
            "Entity\": \"dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"
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

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Upload Sample

#### Description

Upload and analyze a sample.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Parameter | Type | Default Value | Description  
File Path | String | N/A | The sample file path.  
Vm | String | N/A | The vm to run the analysis on. Example: win7-x64  
Playbook | String | N/A | Name of a playbook to apply to this sample run. Example: default  
Network Exit | String | N/A | Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location.  
Private | Checkbox | Checked | If checked, the sample will be marked private.  
Linux Server Address | String | N/A | Specify the IP address of the remote linux server, where the file is located.  
Linux Username | String | N/A | Specify the username of the remote linux server, where the file is located.  
Linux Password | Password | N/A | Specify the password of the remote linux server, where the file is located.  
  
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

Script Result Name | Value Options | Example  
---|---|---  
score | N/A | N/A  
  
##### JSON Result
    
    
    {
        "count": 0,
        "max-confidence": 0,
        "sample": "99ca73a47996cc3069e39a672728a49c",
        "score": 0,
        "bis": [],
        "max-severity": 0
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If one of the "Linux Server Address", "Linux Username", "Linux Password" parameters is not provided:_ **_Error executing action "{action_name}". Reason: for remote server connection you need to provide values for all parameters "Linux Server Address", "Linux Username", "Linux Password"._** | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
