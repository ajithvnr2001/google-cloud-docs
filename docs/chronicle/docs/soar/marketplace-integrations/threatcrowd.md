---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/threatcrowd/
title: ThreatCrowd \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:19.096217+00:00
---

# ThreatCrowd  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/threatcrowd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ThreatCrowd

This document provides guidance on how to integrate ThreatCrowd with Google SecOps.

## Configure ThreatCrowd integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Enrich Entities

#### Description

Quickly identify related infrastructures and malware.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to Apply  
---|---  
permalink | Returns if it exists in JSON result  
response_code | Returns if it exists in JSON result  
votes | Returns if it exists in JSON result  
references | Returns if it exists in JSON result  
hashes | Returns if it exists in JSON result  
resolutions | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
last_resolved | Returns if it exists in JSON result  
  
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
                "permalink": "https: //www.threatcrowd.org/ip.php?ip=1.1.1.1",
                "response_code": "1",
                "votes": -1,
                "references": [
                    "http: //www.talosintelligence.com/feeds/ip-filter.blf",
                    "https: //check.torproject.org/exit-addresses",
                    "https: //otx.alienvault.com/pulse/56714a2867db8c3f8a46fe95/"
                ],
                "hashes": [],
                "resolutions": [{
                    "domain": "afplink.net",
                    "last_resolved": "2016-06-24"
                },{
                    "domain": "jabber.zwiebeltoralf.de",
                    "last_resolved": "2016-12-28"
                }]},
            "Entity": "1.1.1.1"
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
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
