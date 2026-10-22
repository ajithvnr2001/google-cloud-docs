---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/joesandbox/
title: Joe Sandbox \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:05.416469+00:00
---

# Joe Sandbox  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/joesandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Joe Sandbox

This document provides guidance on how to integrate Joe Sandbox with Google SecOps.

## Configure Joe Sandbox to work with Google Security Operations

To obtain API Key, navigate to **User Settings** in Joe Sandbox - **API Key.**

## Configure Joe Sandbox integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Detonate File

#### Description

Run a file in Joe Sandbox and retrieve an analysis of results.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
File Paths | String | N/A | The paths of the files to scan comma separated.  
Comment | String | N/A | The comment to add to the entry.  
Report Format | String | N/A | The format of the report.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold.

##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight will be created to inform on the malicious status of the enriched file. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ScriptResult | True/False | ScriptResult:False  
  
##### JSON Result
    
    
    {
       "path\\\\mocks.txt":
          {
             "status": "finished",
             "runs":
               [{
                   "detection": "clean",
                   "yara": false,
                   "system": "w7_1",
                   "error": null
                 },{
                   "detection": "clean",
                   "yara": false,
                   "system": "w7x64",
                   "error": null
                }],
             "sha1": "e96a0e74ed5cfbcaa65c764939b29945e988be9b",
             "tags": [],
             "webid": "773601",
             "comments": "testing",
             "filename": "mocks.txt",
             "scriptname": "default.jbs",
             "time": "2019-01-21T11:21:20+01:00",
             "duration": 530,
             "sha256": "6087f230c0d6ea362f23ca2abb4baf82a9058cb0143af3e82584005f56626f5b",
             "md5": "502cddb08849eb191386017dfca05670",
             "analysisid": "765760"
          }
    }
    

### Ping

#### Description

Verifies that the user has a connection to Joe Sandbox through the user's device.

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
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
    N/A
    

### Search Hash

#### Description

Search for a hash in sandbox records.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold.

Enrichment Field Name | Logic - When to apply  
---|---  
status | Returns if it exists in JSON result  
runs | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
webid | Returns if it exists in JSON result  
comments | Returns if it exists in JSON result  
filename | Returns if it exists in JSON result  
scriptname | Returns if it exists in JSON result  
time | Returns if it exists in JSON result  
duration | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
analysisid | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight will be created to inform on the malicious status of the enriched hash. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious threshold set before scan.  
  
### Search URL

#### Description

Search for a URL in sandbox records.

#### Parameters

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold.

Enrichment Field Name | Logic - When to apply  
---|---  
status | Returns if it exists in JSON result  
runs | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
webid | Returns if it exists in JSON result  
comments | Returns if it exists in JSON result  
filename | Returns if it exists in JSON result  
scriptname | Returns if it exists in JSON result  
time | Returns if it exists in JSON result  
duration | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
analysisid | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight will be created to inform on the malicious status of the enriched URL. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
            "status": "finished",
            "runs":
               [{
                  "detection": "clean",
                  "yara": false,
                  "system": "w7_1",
                  "error": null
                },{
                  "detection": "clean",
                  "yara": false,
                  "system": "w7x64",
                  "error": null
               }],
           "sha1": "e96a0e74ed5cfbcaa65c764939b29945e988be9b",
           "tags": [],
           "webid": "773601",
           "comments": "testing",
           "filename": "mocks.txt",
           "scriptname": "default.jbs",
           "time": "2019-01-21T11:21:20+01:00",
           "duration": 530,
           "sha256": "6087f230c0d6ea362f23ca2abb4baf82a9058cb0143af3e82584005f56626f5b",
           "md5": "502cddb08849eb191386017dfca05670",
           "analysisid": "765760"
          },
       "Entity": "https://sampleweb.com"
    }]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
