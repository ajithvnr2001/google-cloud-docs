---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafeensm/
title: McAfee NSM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:39.584650+00:00
---

# McAfee NSM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafeensm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee NSM

**Important:** This integration refers to Mcafee Network Security Manager.

This document provides guidance on how to integrate McAfee NSM with Google SecOps.

## Overview

## Configure McAfee NSM integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
API Root | String | https://x.x.x.x/sdkapi/ | True |   
Username | String | N/A | True |   
Password | Password | N/A | True |   
Domain ID | String | N/A | True |   
Siemplify Policy Name | String | N/A | True |   
Sensors Names List Comma Separated | String | sensor_name1,sensor_name2,sensor_name3 | True |   
  
## Actions

### Block IP

#### Description

Block IP address.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

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
    

### Get Alert Info Data

#### Description

Get alert data by ID.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Alert ID | String | https://x.x.x.x/sdkapi/ | True | N/A  
Sensor Name | String | N/A | True | N/A  
  
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
alert_json | N/A | N/A  
  
##### JSON Result
    
    
    {
        "name": "MALWARE: Blacklisted File Detected",
        "assignTo": "---",
        "description": {
            "definition": "A McAfee-maintained blacklist that is dynamically updated with Callback Detectors updates.",
            "signatures": [{
                "conditions": "null"
            }],
            "componentAttacks": "null",
            "target": "ServerOrClient",
            "reference": {
                "cveId": "[]",
                "certId": "null",
                "bugtraqId": "[]",
                "nspId": "0x4840c300",
                "microsoftId": "[]",
                "additionInfo": "null",
                "arachNidsId": "[]"
            },
            "protocals": "[smtp, ftp, http]",
            "comments": {
                "availableToChildDomains": "true",
                "parentDomainComments": "null",
                "comments": " "
            },
            "rfSB": "No",
            "attackCategory": "Malware",
            "attackSubCategory": "---",
            "protectionCategory": "[Malware/Bot]",
            "httpResponseAttack": "No",
            "btf": "Medium"
        },
        "summary": {
            "destination": "null",
            "zoombie": "null",
            "target": {
                "ipAddrs": "1.1.1.1",
                "risk": "N/A",
                "country": "India",
                "networkObject": "---",
                "hostName": "null",
                "vmName": "null",
                "proxyIP": "1.1.1.1",
                "user": "Unknown",
                "os": "---",
                "port": 41128
            },
            "attacker": {
                "ipAddrs": "1.1.1.1",
                "risk": "N/A",
                "country": "India",
                "networkObject": "---",
                "hostName": "null",
                "vmName": "null",
                "proxyIP": "1.1.1.1",
                "user": "Unknown",
                "os": "---",
                "port": 80
            },
            "cAndcServer": "null",
            "source": "null",
            "compromisedEndpoint": "null",
            "attackedHIPEndpoint": {
                "ipAddrs": "1.1.1.1",
                "risk": "N/A",
                "country": "India",
                "networkObject": "---",
                "hostName": "null",
                "vmName": "null",
                "proxyIP": "1.1.1.1",
                "user": "Unknown",
                "os": "---",
                "port": 41128
            },
            "fastFluxAgent": "null",
            "event": {
                "domain": "My Company",
                "protocol": "http",
                "zone": "null",
                "alertId": "2246015847757997493",
                "attackCount": 1,
                "vlan": "-11",
                "direction": "Inbound",
                "detection": "Signature",
                "application": "HTTP",
                "device": "NS9100-50",
                "result": "Inconclusive",
                "time": "Jan 04, 2016 09:50:39",
                "relevance": "Unknown",
                "matchedPolicy": "CustomFP_Engine_With_AlertOnly",
                "interface": "G3/1-G3/2"
            }},
        "details": {
            "malwareFile": {
                "engine": "Manager Blacklist",
                "fileHash": "3f3f7c3b9722912ddeddf006cff9d9d0",
                "malwareConfidence": "Very High",
                "malwareName": "null",
                "fileName": "/Firewall.cpl",
                "size": "6144 bytes"
            },
            "exceededThreshold": "null",
            "callbackDetectors": "null",
            "layer7": {
                "httpReturnCode": 200,
                "httpURI": "/Firewall.cpl",
                "httpRequestMethod": "GET",
                "httpServerType": "Apache/2.2.13 (Fedora) Last - Modified: Wed, 10 Oct 2012 05: 19: 15 GMT",
                "httpHostHeader": "null",
                "httpUserAgent": "Wget/1.11.4 (Red Hat modified)"
            },
            "portScan": "null",
            "sqlInjection": "null",
            "triggeredComponentAttacks": "null",
            "hostSweep": "null",
            "matchedSignature": "null",
            "communicationRuleMatch": "null",
            "fastFlux": "null"
        },
        "alertState": "UnAcknowledged",
        "uniqueAlertId": "6245941293374080682"
    }
    

### Is IP Blocked

#### Description

Check if an IP address is blocked.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

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
    

### Ping

#### Description

Test Connectivity.

#### Parameters

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
    

### Quarantine IP

#### Description

Quarantine a particular IP address.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

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
    

### Unblock IP

#### Description

Unblock a particular IP address.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

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
    
    
    [{
       "EntityResult":
         [{
            "EPOEvents.ThreatCategory": "av.detect",
            "EPOEvents.TargetUserName": "VM-EPOAGENTTEST\\\\\\\\Admin",
            "EPOEvents.TargetPort": "None",
            "EPOEvents.TargetFileName": "C:\\\\\\\\Users\\\\\\\\Admin\\\\\\\\Desktop\\\\\\\\eicar.txt",
            "EPOEvents.TargetIPV4": -1979711347,
            "EPOEvents.ThreatName": "EICAR test file",
            "EPOEvents.SourceUserName": "None",
            "EPOEvents.TargetProcessName": "None",
            "EPOEvents.SourceProcessName": "None",
            "EPOEvents.ThreatType": "test",
            "EPOEvents.SourceIPV4": -1979711347,
            "EPOEvents.TargetProtocol": "None",
            "VSECustomEvent.MD5": "44d88612fea8a8f36de82e1278abb02f",
            "EPOEvents.SourceURL": "None",
            "EPOEvents.ThreatActionTaken": "deleted",
            "EPOEvents.TargetHostName": "VM-EPOAGENTTEST",
            "EPOEvents.ThreatHandled": "True",
            "EPOEvents.SourceHostName": "_"
          }, {
            "EPOEvents.ThreatCategory": "av.detect",
            "EPOEvents.TargetUserName": "VM-EPOAGENTTEST\\\\\\\\Admin",
            "EPOEvents.TargetPort": "None",
            "EPOEvents.TargetFileName": "C:\\\\\\\\Users\\\\\\\\Admin\\\\\\\\Desktop\\\\\\\\eicar.txt",
            "EPOEvents.TargetIPV4": -1979711347,
            "EPOEvents.ThreatName": "EICAR test file",
            "EPOEvents.SourceUserName": "None",
            "EPOEvents.TargetProcessName": "None",
            "EPOEvents.SourceProcessName": "None",
            "EPOEvents.ThreatType": "test",
            "EPOEvents.SourceIPV4": -1979711347,
            "EPOEvents.TargetProtocol": "None",
            "VSECustomEvent.MD5": "44d88612fea8a8f36de82e1278abb02f",
            "EPOEvents.SourceURL": "None",
            "EPOEvents.ThreatActionTaken": "deleted",
            "EPOEvents.TargetHostName": "VM-EPOAGENTTEST",
            "EPOEvents.ThreatHandled": "True",
            "EPOEvents.SourceHostName": "_"
          }],
      "Entity": "44d88612fea8a8f36de82e1278abb02f"
    }]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
