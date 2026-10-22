---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-atd/
title: McAfee ATD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:16.430499+00:00
---

# McAfee ATD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-atd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee ATD

**Important:** McAfee ATD became part of the Trellix product portfolio and was renamed to Trellix ATD.

This document provides guidance on how to integrate McAfee ATD with Google SecOps.

## Configure McAfee ATD integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Check Hash

#### Description

Check if a hash is blacklisted.

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
is_blacklisted | True/False | is_blacklisted:False  
  
##### JSON Result
    
    
    [{
       "EntityResult": true,
       "Entity": "ebdd035084968f675ee1510519dd8319"
    }]
    

### Get Analyzer Profiles

#### Description

Get Trellix ATD analyzer profiles data.

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
    
    
    [{
       "overrideOS": 0,
       "logZip": 0,
       "family": 0,
       "default64OSName": "",
       "artimas": 0,
       "yararules": 0,
       "xMode": 0,
       "consoleLog": 0,
       "sophosAV": 0,
       "defaultVM": 0,
       "userLog": 0,
       "filePassword1": "",
       "dnnEnable": 0,
       "recusiveAnalysis": 0,
       "imageid": 0,
       "vmDesc": "Only Down Selectors",
       "heuristic": 0,
       "netdriveZip": 0,
       "ssKeyid": 1,
       "gtiTS": 1,
       "ssAPIid": 1,
       "pe32": 0,
       "createTime": "2012-12-01 02:16:01",
       "locBlackList": 1,
       "openarchive": 1,
       "yaraScan": 0,
       "runtimeArgument": "",
       "dumpZip": 0,
       "userid": 1,
       "filePassword": "",
       "internet": 0,
       "default32OSName": "",
       "lastChange": "2018-08-20 01:04:37",
       "summary": 1,
       "maxExecTime": 180,
       "asm": 0,
       "ntvLog": 0,
       "name": "Analyzer Profile 1",
       "reAnalysis": 1,
       "noPDF": 0,
       "flp": 0,
       "mfeAV": 1,
       "aviraAV": 0,
       "vmProfileid": 1,
       "gam": 1,
       "gml": 0,
       "netLog": 0,
       "sandbox": 0,
       "dropZip": 0,
       "selectedOSName": "",
       "minExecTime": 5,
       "ssLevelid": 1,
       "gtiURLRep": 0,
       "customrules": 0,
       "locWhiteList": 0
    }]
    

### Get Report

#### Description

Get a report for task IDs.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Task IDs | String | N/A | The IDs of the tasks to fetch reports for, comma separated.  
Create Insight | Boolean | Checked | If enabled, action will create an insight containing all of the retrieved information about the report.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
report | True/False | report:False  
  
##### JSON Result
    
    
    {
      "95":
       {
         "Summary":
           {
             "JSONversion": "1.002",
             "SubmitterName": "User",
             "Subject":
                {
                  "Name": "events.txt",
                  "Timestamp": "2018-08-21 08:29:48",
                  "FileType": "2",
                  "sha-256": "74834D752D73B4C81EAD10184A091C12AA30BD809D575FD9CFA07B0EBBD7A0D7", "sha-1": "6BDA9FCFB56CE2B34168D499EE04970F640ADD9A",
                  "parent_archive": "Not Available",
                  "md5": "11FBEF3A9916BF50EC5002B5795B23C3",
                  "Type": "ASCII text",
                  "size": "481231"
                },
            "Process":
              [{
                 "Reason": "processed by down selectors",
                 "Name": "events.txt",
                 "Severity": "0"
               }],
            "Data":
               {
                 "compiled_with": "Not Available",
                 "analysis_seconds": "181",
                 "sandbox_analysis": "0"
               },
            "SUMversion": "1.1.1.1",
            "JobId": "95",
            "SubmitterType": "STAND_ALONE",
            "Behavior": ["Identified as --- by GTI File Reputation", "Identified as --- by Anti-Malware"],
            "hasDynamicAnalysis": "false",
            "TaskId": "95",
            "Verdict":
              {
                 "Severity": "0",
                 "Description": "No malicious activity was detected, but this does NOT mean that execution of the sample is safe"
               },
            "OSversion": "StaticAnalysis",
            "Selectors":
              [{
                 "Engine": "GTI File Reputation",
                 "Severity": "0",
                 "MalwareName": "---"
                },
               {
                 "Engine": "Anti-Malware",
                 "Severity": "0",
                 "MalwareName": "---"
                },
               {
                 "Engine": "Sandbox",
                 "Severity": "0",
                 "MalwareName": "---"
               }],
            "MISversion": "1.1.1.1",
            "DETversion": "1.1.1.1"
         }
       }
    }
    

### Ping

#### Description

Verify that the user has a connection to Trellix ATD via the user's device.

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
    

### Submit File

#### Description

Submit a file for analysis.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
File Paths | String | N/A | The paths of the file to submit, comma separated.  
Analyzer Profile ID | String | N/A | The ID of the analyzer profile to analyze with.  
  
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
task_id | True/False | task_id:False  
  
##### JSON Result
    
    
    {
        "C:\\temp\\test.txt\": 95
    }
    

### Submit URL

#### Description

Submit a URL for analysis.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Analyzer Profile ID | String | N/A | The ID of the analyzer profile to analyze the URLs with. It can be found in ATD under the Policy Analyzer Profile section.  
Create Insight | Boolean | Checked | If enabled, action will create an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
Summary | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
report | True/False | report:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
           "Summary":
              {
                "JSONversion": "1.002",
                "SubmitterName": "User",
                "Subject":
                   {
                     "sha-1": "6BDA9FCFB56CE2B34168D499EE04970F640ADD9A",
                     "Timestamp": "2018-08-21 08:29:48",
                     "FileType": "2",
                     "sha-256": "74834D752D73B4C81EAD10184A091C12AA30BD809D575FD9CFA07B0EBBD7A0D7",
                     "parent_archive": "Not Available",
                     "Name": "events.txt",
                     "md5": "11FBEF3A9916BF50EC5002B5795B23C3",
                     "Type": "ASCII text",
                     "size": "481231"
                   },
               "Process":
                  [{
                    "Reason": "processed by down selectors",
                    "Name": "events.txt",
                    "Severity": "0"
                  }],
                "Data":
                   {
                     "compiled_with": "Not Available",
                     "analysis_seconds": "181",
                     "sandbox_analysis": "0"
                   },
                "SUMversion": "1.1.1.1",
                "JobId": "95",
                "SubmitterType": "STAND_ALONE",
                "Behavior":
                  ["Identified as --- by GTI File Reputation",
                   "Identified as --- by Anti-Malware"],
               "hasDynamicAnalysis": "false",
               "TaskId": "95",
               "Verdict":
                  {
                     "Description": "No malicious activity was detected, but this does NOT mean that execution of the sample is safe",
                     "Severity": "0"
                   },
               "OSversion": "StaticAnalysis",
               "Selectors":
                 [{
                    "Engine": "GTI File Reputation",
                    "Severity": "0",
                    "MalwareName": "---"
                   },
                  {
                    "Engine": "Anti-Malware",
                    "Severity": "0",
                    "MalwareName": "---"
                   },
                  {
                    "Engine": "Sandbox",
                    "Severity": "0",
                    "MalwareName": "---"
                  }],
              "MISversion": "1.1.1.1",
              "DETversion": "1.1.1.1"
             }
         },
      "Entity": "http://google.com"
    }]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
