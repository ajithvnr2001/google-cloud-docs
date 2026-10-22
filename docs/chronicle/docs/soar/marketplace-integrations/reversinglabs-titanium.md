---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/reversinglabs-titanium/
title: ReversingLabs Titanium \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:00.680586+00:00
---

# ReversingLabs Titanium  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/reversinglabs-titanium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ReversingLabs Titanium

This document provides guidance on how to integrate ReversingLabs Titanium with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/ReversinglabsTitanium.zip).

## Configure ReversingLabs Titanium integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Malware Details

#### Description

Query ReversingLabs Titanium for hash information.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
rl | Returns if it exists in JSON result  
malware_presence | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
scanner_count | Returns if it exists in JSON result  
scanner_percent | Returns if it exists in JSON result  
scanner_match | Returns if it exists in JSON result  
query_hash | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
first_seen | Returns if it exists in JSON result  
threat_level | Returns if it exists in JSON result  
trust_factor | Returns if it exists in JSON result  
last_seen | Returns if it exists in JSON result  
Entity | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "rl": {
                    "malware_presence": {
                        "status": "KNOWN",
                        "scanner_count": 41,
                        "scanner_percent": 0.0,
                        "scanner_match": 0,
                        "query_hash": {
                            "sha1": "81fe8bfe87576c3ecb22426f8e57847382917acf"
                        },
                        "first_seen": "2013-03-17T15:10:55",
                        "threat_level": 0,
                        "trust_factor": 0,
                        "last_seen": "2019-05-18T19:48:34"
                    }
                }
            },
            "Entity": "81fe8bfe87576c3ecb22426f8e57847382917acf"
        }
    ]
    

### Ping

#### Description

Verify that the user has a connection to ReversingLabs Titanium Cloud via the user's device.

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
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
