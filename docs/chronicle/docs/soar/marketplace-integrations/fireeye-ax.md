---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-ax/
title: FireEye AX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:07.525783+00:00
---

# FireEye AX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-ax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye AX

**Important:** FireEye and McAfee Enterprise merged and became Trelix. FireEye AX was renamed to Trellix Malware Analysis.

This document describes how to integrate FireEye AX with Google Security Operations.

## Use Cases

Perform enrichment of entities.

## Configure FireEye AX integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/<<ip address>> | Yes | API root of the Trellix Malware Analysis instance.  
Username | String | N/A | Yes | Username of Trellix Malware Analysis account.  
Password | Password | N/A | Yes | Password of Trellix Malware Analysis account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix Malware Analysis server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trellix Malware Analysis with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
**if successful:** "Successfully connected to the Trellix Malware Analysis server with the provided connection parameters!" **The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to connect to the Trellix Malware Analysis server! Error is {0}".format(exception.stacktrace) | General  
  
### Submit URL

#### Description

Submit file for analysis using URL in Trellix Malware Analysis. Supported entities: URL.

**Note:** Action is running as async, please adjust script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
VM Profile | String | N/A | Yes | Specify the virtual machine profile that should be used during analysis. Available VM profiles are available in the action "Get Appliance Details"  
Application ID | String | N/A | No | Specify the ID of the application that needs to be used during the analysis of the file. By default, Trellix Malware Analysis will select the needed application automatically. In order to get a list of available applications on the profile, please execute action "Get Appliance Details"  
Priority | DDL | NormalPossible Values:NormalUrgent | No | Specify the priority for the submission. "Normal" puts submission at the bottom of the queue, while "Urgent" puts submission at the top of the queue.  
Force Rescan | Checkbox |  | No | If enabled, action will force Trellix Malware Analysis to rescan the submitted file.  
Analysis Type | DDL | LivePossible Values:LiveSandbox | No | Specify the type of the analysis. If "Live" is selected, Trellix Malware Analysis will analyze suspected files live within the Malware Analysis Multi-Vector Virtual Execution (MVX) analysis engine. If "Sandbox" is selected Trellix Malware Analysis will analyze suspected files in a closed, protected environment.  
Create Insight | Checkbox |  | Yes | If enabled, action will create an insight containing information about the submitted file.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
     {
        "details":
            {
                "explanation": {
                    "malwareDetected": {
                        "malware": [
                            {
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147"
                            },
                            {
                                "note": "",
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147",
                                "application": "application:0",
                                "user": "xxxxx",
                                "original": "vlc-3.0.16-win64.exe",
                                "type": "exe",
                                "origid": 176
                            }
                        ]
                    },
                    "osChanges": [],
                    "staticAnalysis": {
                        "static": [
                            {}
                        ]
                    },
                    "stolenData": {
                        "info": {
                            "field": []
                        }
                    }
                },
                "src": {},
                "alertUrl": "https://172.18.5.2/malware_analysis/analyses?maid=177",
                "action": "notified",
                "attackTime": "2021-09-13 11:15:56 +0000",
                "dst": {},
                "applianceId": "AC1F6B7A7C8C",
                "id": 177,
                "name": "xxxxx_xxxxx",
                "severity": "MINR",
                "uuid": "61330da9-20ad-4196-a901-02b2166ad36d",
                "ack": "no",
                "product": "MAS",
                "vlan": 0,
                "malicious": "no"
            }
        ],
        "appliance": "MAS",
        "version": "MAS (MAS) 9.1.0.950877",
        "msg": "extended",
        "alertsCount": 1
    }
    

##### Enrichment Table

Enrichment Field Name | Logic - When to apply  
---|---  
malicious | When available in JSON  
severity | When available in JSON  
  
##### Entity Insight

Entity insight example:

**Malicious:** True

**Severity:** MINR **C &C Services Count:** 0 **Executed Processes Count:** 0 **Registry Changes Count:** 0 **Extracted Files Count:** 0

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data is available for one(is_success = true):** "Successfully enriched the following entities using information from Trellix Malware Analysis: {entity.identifier}". **If data is not available for one (is_success=true):** "Action wasn't able to enrich the following entities using information from Trellix Malware Analysis: {entity.identifier}" **If data is not available for all (is_success=false):** None of the provided entities were enriched. **Async Message:** Waiting for the following files to be processed: {pending files} **The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) **If timeout:** "Error executing action "Enrich Entities". Reason: action ran into a timeout. The following files are still processing: {pending urls}. Please increase the timeout in IDE. Note: adding the same files will create a separate analysis job in Trellix Malware Analysis. | General  
Case Wall Table | **Title:** {entity.identifier} | Entity  
  
### Submit File

#### Description

Submit file for analysis in Trellix Malware Analysis.

**Note:** Action is running as async, please adjust script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Paths | CSV | N/A | Yes | Specify a comma-separate list of absolute file paths for submission.  
VM Profile | String | N/A | Yes | Specify the virtual machine profile that should be used during analysis. Available VM profiles are available in the action "Get Appliance Details"  
Application ID | String | N/A | No | Specify the ID of the application that needs to be used during the analysis of the file. By default, Trellix Malware Analysis will select the needed application automatically. In order to get a list of available applications on the profile, please execute action "Get Appliance Details"  
Priority | DDL | NormalPossible Values:NormalUrgent | No | Specify the priority for the submission. "Normal" puts submission at the bottom of the queue, while "Urgent" puts submission at the top of the queue.  
Force Rescan | Checkbox |  | No | If enabled, action will force Trellix Malware Analysis to rescan the submitted file.  
Analysis Type | DDL | LivePossible Values:LiveSandbox | No | Specify the type of the analysis. If "Live" is selected, Trellix Malware Analysis will analyze suspected files live within the Malware Analysis Multi-Vector Virtual Execution (MVX) analysis engine. If "Sandbox" is selected Trellix Malware Analysis will analyze suspected files in a closed, protected environment.  
Create Insight | Checkbox |  | Yes | If enabled, action will create an insight containing information about the submitted file.  
  
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
        "absolute_path": "/opt/wow/koko.exe",
        "details":
            {
                "explanation": {
                    "malwareDetected": {
                        "malware": [
                            {
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147"
                            },
                            {
                                "note": "",
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147",
                                "application": "application:0",
                                "user": "xxxxx",
                                "original": "vlc-3.0.16-win64.exe",
                                "type": "exe",
                                "origid": 176
                            }
                        ]
                    },
                    "osChanges": [],
                    "staticAnalysis": {
                        "static": [
                            {}
                        ]
                    },
                    "stolenData": {
                        "info": {
                            "field": []
                        }
                    }
                },
                "src": {},
                "alertUrl": "https://172.18.5.2/malware_analysis/analyses?maid=177",
                "action": "notified",
                "attackTime": "2021-09-13 11:15:56 +0000",
                "dst": {},
                "applianceId": "AC1F6B7A7C8C",
                "id": 177,
                "name": "xxxxx_xxxxx",
                "severity": "MINR",
                "uuid": "61330da9-20ad-4196-a901-02b2166ad36d",
                "ack": "no",
                "product": "MAS",
                "vlan": 0,
                "malicious": "no"
            }
        ],
        "appliance": "MAS",
        "version": "MAS (MAS) 9.1.0.950877",
        "msg": "extended",
        "alertsCount": 1
    }
    

##### Entity Insight

Entity insight example:

**Malicious:** True

**Severity:** MAJR **C &C Services Count:** 15 **Executed Processes Count:** 0 **Registry Changes Count:** 13 **Extracted Files Count:** 10

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**If completed for one filepath (is_success = true):** "Successfully retrieved details for the following files in Trellix Malware Analysis: {submitted files}.". **Async Message:** Waiting for the following files to be processed: {pending files} **The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Submit File". Reason: {0}''.format(error.Stacktrace) **If timeout:** "Error executing action "Submit File". Reason: action ran into a timeout. The following files are still processing: {pending files}. Please increase the timeout in IDE. Note: adding the same files will create a separate analysis job in Trellix Malware Analysis. **If at least one file not found:** "Error executing action "Attach File To Case". Reason: the following files were not found or action doesn't have enough permissions to access them: {not available files}' | General  
  
### Get Appliance Details

#### Description

Retrieve information about Trellix Malware Analysis appliance.

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
        "absolute_path": "/opt/wow/koko.exe",
        "details":
            {
                "explanation": {
                    "malwareDetected": {
                        "malware": [
                            {
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147"
                            },
                            {
                                "note": "",
                                "md5Sum": "29ef299c80d00ee4340b3694d870fe82",
                                "sha256": "0cff2d41a69d72de30607b8fc09da90e352393e154a342efcddb91e06b3a2147",
                                "application": "application:0",
                                "user": "xxxxx",
                                "original": "vlc-3.0.16-win64.exe",
                                "type": "exe",
                                "origid": 176
                            }
                        ]
                    },
                    "osChanges": [],
                    "staticAnalysis": {
                        "static": [
                            {}
                        ]
                    },
                    "stolenData": {
                        "info": {
                            "field": []
                        }
                    }
                },
                "src": {},
                "alertUrl": "https://172.18.5.2/malware_analysis/analyses?maid=177",
                "action": "notified",
                "attackTime": "2021-09-13 11:15:56 +0000",
                "dst": {},
                "applianceId": "AC1F6B7A7C8C",
                "id": 177,
                "name": "xxxxx_xxxxx",
                "severity": "MINR",
                "uuid": "61330da9-20ad-4196-a901-02b2166ad36d",
                "ack": "no",
                "product": "MAS",
                "vlan": 0,
                "malicious": "no"
            }
        ],
        "appliance": "MAS",
        "version": "MAS (MAS) 9.1.0.950877",
        "msg": "extended",
        "alertsCount": 1
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**If completed for one filepath (is_success = true):** "Successfully retrieved details about Trellix Malware Analysis.". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Appliance Details". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
