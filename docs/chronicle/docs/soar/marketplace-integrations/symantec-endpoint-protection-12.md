---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-protection-12/
title: Symantec Endpoint Protection 12 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:22:58.746167+00:00
---

# Symantec Endpoint Protection 12  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-protection-12/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Endpoint Protection 12

This document provides guidance on how to integrate Symantec Endpoint Protection 12 with Google SecOps.

## Configure Symantec Endpoint Protection integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Report

#### Description

Get a command status report.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Command IDS | String | 7E975C32C71349E9BE495EC2220B902F | N/A  
  
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
reports | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "computerName": "HOST_1",
            "subStateId": 0,
            "hardwareKey": "36817A7B13C3A6317932AD9819097123",
            "computerId": "9C9850840A0000BD3566F8ECC8417123",
            "domainName": "Default",
            "stateId": 0,
            "computerIp": "1.1.1.1",
            "currentLoginUserName": "admin"
        }, {
            "computerName": "HOST_2",
            "subStateId": 0,
            "hardwareKey": "36817A7B13C3A6317932AD9819097123",
            "computerId": "9C9850840A0000BD3566F8ECC8417123",
            "domainName": "Default",
            "stateId": 0,
            "computerIp": "1.1.1.1",
            "currentLoginUserName": "admin"
        }
    ]
    

### Scan Endpoint

#### Description

Scan an endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Scan Type | List` | ScanNow_Full | The type of the scan to perform. ScanNow_Full = Full scan, ScanNow_Quick = quick scan, ScanNow_Custom = custom scan.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



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
    

### Update and Scan Endpoint

#### Description

Update and scan an endpoint.

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

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Update Endpoint

#### Description

Update an endpoint.

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

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
