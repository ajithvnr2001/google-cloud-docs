---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-ddan/
title: Trend Micro DDAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:37.911672+00:00
---

# Trend Micro DDAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-ddan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trend Micro DDAN

This document provides guidance on how to integrate Trend Micro DDAN with Google SecOps.

## Configure Trend Micro DDAN integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | `https://``IP_ADDRESS` | Yes | API root of the Trend Micro DDAN instance.  
API Key | Password | N/A | Yes | API key of the Trend Micro DDAN instance.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the Trend Micro DDAN is valid.  
  
## Actions

### Ping

Test connectivity to Trend Micro DDAN with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should neither fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Trend Micro DDAN server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Trend Micro DDAN server! Error is {0}".format(exception.stacktrace)" | General  
  
### Submit File

Submit files in Trend Micro DDAN.

**Note:** This action is running as async. Adjust the script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File URLs | CSV | N/A | Yes | Specify a comma-separated list of the URLs that point to the file that needs to be analyzed.  
Fetch Event Log | Checkbox | Checked | No | If enabled, the action fetches event logs related to the files.  
Fetch Suspicious Objects | Checkbox | Checked | No | If enabled, the action fetches suspicious objects.  
Fetch Sandbox Screenshot | Checkbox | Unchecked | No | If enabled, the action tries to fetch a sandbox screenshot related to the files.  
Resubmit File | Checkbox | Checked | No | If enabled, the action doesn't check if there was a submission for this file previously.  
Max Event Logs To Return | Integer | 50 | No | Specify the number of event logs to return. Maximum: 200  
Max Suspicious Objects To Return | Integer | 50 | No | Specify the number of suspicious objects to return. Maximum: 200  
Fetch Suspicious Objects | Checkbox | Checked | No | If enabled, the action fetches suspicious object.  
Max Suspicious Objects To Return | Integer | 50 | No | Specify the number of suspicious objects to return. Maximum: 200  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "REPORTS": {
            "IMAGE_TYPE": {
                "TYPE": "Windows 10"
            },
            "OVERALL_RISK_LEVEL": -19,
            "FILE_ANALYZE_REPORT": {
                "FileSHA1": "2C2218022BC734EFF94290199C2CDC46E9531F9B",
                "FileMD5": "6061C079AFC5B3198F2752F875513E58",
                "FileSHA256": "6CE4952C2EE4D70CBC3B4276007D0815C03FA0E87E209DF7B901D143C06859AA",
                "FileTLSH": "",
                "FileID": "3315_0001",
                "OrigFileName": "https://example.com/",
                "DownloadedFileName": "",
                "MalwareSourceIP": "",
                "MalwareSourceHost": "",
                "ROZRating": -19,
                "CensusPrevalence": -1,
                "GRIDIsKnownGood": -1,
                "AuthenticodeIsGood": 0,
                "IsAllowed": 0,
                "IsDenylisted": 0,
                "OverallROZRating": -19,
                "AnalyzeTime": "2022-11-07 15:39:24",
                "VirusDetected": 0,
                "EngineVersion": "",
                "PatternVersion": "",
                "VirusName": "",
                "TrueFileType": "URL",
                "FileSize": 0,
                "PcapReady": 0,
                "SandcastleClientVersion": "6.0.5511",
                "AnalyzeStartTime": "2022-11-07 15:39:23",
                "ParentChildRelationship": "",
                "DuplicateSHA1": 0,
                "ConnectionMode": "nat",
                "ExternalServiceMode": "Global",
                "DiagInfo": "",
                "RedirectChain": {
                    "Connection": {
                        "ID": 1,
                        "URL": "https://example.com",
                        "WRSScore": 71,
                        "WRSCategoryID": 93,
                        "WRSCategoryName": "Newly Observed Domain",
                        "ThreatName": "",
                        "RedirectFrom": ""
                    }
                },
                "DroppedFiles": "",
                "USandboxVersion": "5.8.1044"
            },
            "EXTRA_INFO": {
                "VAAnalysisTime": 96,
                "TotalProcessingTime": 97
            }
        },
        "Screenshot": "",
        "EventLog": [
            {
                "EventLog": {
                    "Date": "2022-11-07 15:37:49+00",
                    "Source": 1,
                    "SubmitDate": "2022-11-07 15:37:49.618895+00",
                    "ProtocolGroup": "",
                    "Protocol": "",
                    "VLANId": "",
                    "Direction": "",
                    "DstIP": "",
                    "DstIPStr": "",
                    "DstPort": "",
                    "DstMAC": "",
                    "SrcIP": "",
                    "SrcIPStr": "",
                    "SrcPort": "",
                    "SrcMAC": "",
                    "DomainName": "",
                    "HostName": "",
                    "DetectionName": "",
                    "RiskTypeGroup": "",
                    "RiskType": "",
                    "FileName": "",
                    "FileExt": "",
                    "TrueFileType": "",
                    "FileSize": "",
                    "RuleID": "",
                    "Description": "Dummy log content",
                    "ConfidenceLevel": "",
                    "Recipient": "",
                    "Sender": "",
                    "Subject": "",
                    "BOTCmd": "",
                    "BOTUrl": "",
                    "ChannelName": "",
                    "NickName": "",
                    "URL": "https://example.com",
                    "UserName": "",
                    "Authentication": "",
                    "UserAgent": "",
                    "TargetShare": "",
                    "DetectedBy": "",
                    "PotentialRisk": "",
                    "HasQFile": "",
                    "ServerName": "",
                    "MessageID": "",
                    "EngineVer": "",
                    "PatternNum": "",
                    "VirusType": "",
                    "EngineVirusMajorType": ""
                }
            }
        ],
        "SuspiciousObjects": ""
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should neither fail nor stop a playbook execution:** _If returned report (is_success=true):_ "Successfully analyzed the following URLs in Trend Micro DDAN: `SUCCESSFUL_URLS`" _If didn't return report for one (is_success=true):_ "Action wasn't able to return results the following URLs in Trend Micro DDAN: `SUCCESSFUL_URLS`" _If didn't return report for all URLs (is_success=true):_ "No results for the provided URLs." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Submit File URL". Reason: {0}''.format(error.Stacktrace)" | General  
  
### Submit File URL

Submit a file using URLs in Trend Micro DDAN.

**Note:** This action is running as async. Adjust the script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File URLs | CSV | N/A | Yes | Specify a comma-separated list of the URLs that point to the file that needs to be analyzed.  
Fetch Event Log | Checkbox | Checked | No | If enabled, the action fetches event logs related to the files.  
Fetch Suspicious Objects | Checkbox | Checked | No | If enabled, the action fetches suspicious objects.  
Fetch Sandbox Screenshot | Checkbox | Unchecked | No | If enabled, the action tries to fetch a sandbox screenshot related to the files.  
Resubmit File | Checkbox | Checked | No | If enabled, the action doesn't check if there was a submission for this file previously.  
Max Event Logs To Return | Integer | 50 | No | Specify the number of event logs to return. Maximum: 200  
Max Suspicious Objects To Return | Integer | 50 | No | Specify the number of suspicious objects to return. Maximum: 200  
Fetch Suspicious Objects | Checkbox | Checked | No | If enabled, the action fetches suspicious object.  
Max Suspicious Objects To Return | Integer | 50 | No | Specify the number of suspicious objects to return. Maximum: 200  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "REPORTS": {
            "IMAGE_TYPE": {
                "TYPE": "Windows 10"
            },
            "OVERALL_RISK_LEVEL": -19,
            "FILE_ANALYZE_REPORT": {
                "FileSHA1": "2C2218022BC734EFF94290199C2CDC46E9531F9B",
                "FileMD5": "6061C079AFC5B3198F2752F875513E58",
                "FileSHA256": "6CE4952C2EE4D70CBC3B4276007D0815C03FA0E87E209DF7B901D143C06859AA",
                "FileTLSH": "",
                "FileID": "3315_0001",
                "OrigFileName": "https://example.com",
                "DownloadedFileName": "",
                "MalwareSourceIP": "",
                "MalwareSourceHost": "",
                "ROZRating": -19,
                "CensusPrevalence": -1,
                "GRIDIsKnownGood": -1,
                "AuthenticodeIsGood": 0,
                "IsAllowed": 0,
                "IsDenylisted": 0,
                "OverallROZRating": -19,
                "AnalyzeTime": "2022-11-07 15:39:24",
                "VirusDetected": 0,
                "EngineVersion": "",
                "PatternVersion": "",
                "VirusName": "",
                "TrueFileType": "URL",
                "FileSize": 0,
                "PcapReady": 0,
                "SandcastleClientVersion": "6.0.5511",
                "AnalyzeStartTime": "2022-11-07 15:39:23",
                "ParentChildRelationship": "",
                "DuplicateSHA1": 0,
                "ConnectionMode": "nat",
                "ExternalServiceMode": "Global",
                "DiagInfo": "",
                "RedirectChain": {
                    "Connection": {
                        "ID": 1,
                        "URL": "https://example.com",
                        "WRSScore": 71,
                        "WRSCategoryID": 93,
                        "WRSCategoryName": "Newly Observed Domain",
                        "ThreatName": "",
                        "RedirectFrom": ""
                    }
                },
                "DroppedFiles": "",
                "USandboxVersion": "5.8.1044"
            },
            "EXTRA_INFO": {
                "VAAnalysisTime": 96,
                "TotalProcessingTime": 97
            }
        },
        "Screenshot": "{base64 of }",
        "EventLog": [
            {
                "EventLog": {
                    "Date": "2022-11-07 15:37:49+00",
                    "Source": 1,
                    "SubmitDate": "2022-11-07 15:37:49.618895+00",
                    "ProtocolGroup": "",
                    "Protocol": "",
                    "VLANId": "",
                    "Direction": "",
                    "DstIP": "",
                    "DstIPStr": "",
                    "DstPort": "",
                    "DstMAC": "",
                    "SrcIP": "",
                    "SrcIPStr": "",
                    "SrcPort": "",
                    "SrcMAC": "",
                    "DomainName": "",
                    "HostName": "",
                    "DetectionName": "",
                    "RiskTypeGroup": "",
                    "RiskType": "",
                    "FileName": "",
                    "FileExt": "",
                    "TrueFileType": "",
                    "FileSize": "",
                    "RuleID": "",
                    "Description": "Dummy log content",
                    "ConfidenceLevel": "",
                    "Recipient": "",
                    "Sender": "",
                    "Subject": "",
                    "BOTCmd": "",
                    "BOTUrl": "",
                    "ChannelName": "",
                    "NickName": "",
                    "URL": "https://example.com",
                    "UserName": "",
                    "Authentication": "",
                    "UserAgent": "",
                    "TargetShare": "",
                    "DetectedBy": "",
                    "PotentialRisk": "",
                    "HasQFile": "",
                    "ServerName": "",
                    "MessageID": "",
                    "EngineVer": "",
                    "PatternNum": "",
                    "VirusType": "",
                    "EngineVirusMajorType": ""
                }
            }
        ],
        "SuspiciousObjects": ""
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should neither fail nor stop a playbook execution:** _If returned report (is_success=true):_ "Successfully analyzed the following URLs in Trend Micro DDAN: `SUCCESSFUL_URLS`" _If didn't return report for one (is_success=true):_ "Action wasn't able to return results the following URLs in Trend Micro DDAN: `SUCCESSFUL_URLS`" _If didn't return report for all URLs (is_success=true):_ "No results for the provided URLs." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Submit File URL". Reason: {0}''.format(error.Stacktrace)" | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
