---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/reversinglabs-a1000/
title: ReversingLabs A1000 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:15.878794+00:00
---

# ReversingLabs A1000  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/reversinglabs-a1000/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ReversingLabs A1000

This document provides guidance on how to integrate ReversingLabs A1000 with Google SecOps.

## Configure ReversingLabs A1000 integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Delete Sample

#### Description

Delete a set of samples that exist on the A1000 appliance. All related data including, extracted samples, and metadata will be deleted.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Get Report

#### Description

Get a summary classification report and all details for a sample or a list of samples using hash value(s).

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Filed Name** | Logic-When to apply  
---|---  
threat_status | Returns if it exists in JSON result  
local_last_seen | Returns if it exists in JSON result  
classification_origin | Returns if it exists in JSON result  
imphash | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
sha512 | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
threat_name | Returns if it exists in JSON result  
local_first_seen | Returns if it exists in JSON result  
classification_reason | Returns if it exists in JSON result  
threat_level | Returns if it exists in JSON result  
trust_factor | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
aliases | Returns if it exists in JSON result  
  
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
                "threat_status": "malicious",
                "local_last_seen": "2019-01-22T14: 21: 35.513535Z",
                "classification_origin": {
                    "imphash": "",
                    "sha1": "9747d177bddfc9809079283829e6bbbe315dcfa0",
                    "sha512": "efabb440ab2b82dda2614308b8e2d5e1850ede3fb9c8e6f1e521f1b0728d621a6f5174c30b8e27d7964bcff0ae6b8a1a48ecc4a69d0dc3eae7eccf54a4791785",
                    "sha256": "d3133784ef82208faaa3b917096d7c3e0ad9eb89a5eb4d7770418c8261da4a41", "md5": "242b13c72845a90a869ed0add78f6110"
                },
                "threat_name": "Android.Trojan.Agent",
                "local_first_seen": "2018-01-21T15: 30: 36.698843Z",
                "classification_reason": "cloud",
                "threat_level": 5,
                "trust_factor": 5,
                "md5": "2f61c5a77a64b3d45d651dc2fa7baff7",
                "aliases":["76ea783ed0744703347a00403a73694c2a1e5a957f0f969b4284353fc7c919b4"
                ]},
            "Entity": "2f61c5a77a64b3d45d651dc2fa7baff7"
        }
    ]
    

### Get Scan Status

#### Description

Return the processing status in the A1000 system for the list of hash values.

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
            "EntityResult": "processed",
           "Entity": "2f61c5a77a64b3d45d651dc2fa7baff7"
        },{
            "EntityResult": "processed",
            "Entity": "526e57077b938b3c3dbce56f8aaaa7be"
        }
    ]
    

### Ping

#### Description

Test connectivity.

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
    

### Upload File

#### Description

Upload a file for analysis on the A1000 appliance.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
File Path | String | N/A | Target file path.  
  
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
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "threat_status": "unknown",
        "local_last_seen": "2019-01-28T11:40:23.195946Z",
        "classification_origin": null,
        "threat_name": null,
        "local_first_seen": "2019-01-28T11:09:06.752747Z",
        "classification_reason": "unknown",
        "threat_level": 0,
        "trust_factor": 5,
        "md5": "848d57fbd8e29afa08bd3f58dd30f902",
        "aliases": [
            "Notes.txt"
        ]
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
