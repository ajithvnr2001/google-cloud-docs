---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/junipervsrx/
title: Juniper vSRX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:20.070312+00:00
---

# Juniper vSRX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/junipervsrx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Juniper vSRX

This document provides guidance on how to integrate Juniper vSRX with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/JuniperVSRX.zip).

## Configure Juniper vSRX integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add IP to Address set

#### Description

Add an IP to the address set.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Address Set Name | String | N/A | N/A  
Zone Name | String | N/A | N/A  
  
#### Use cases

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

Test integration connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action doesn't run on entities.

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
    

### Remove IP From Address set

#### Description

Remove an IP address from the address set.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Address Set Name | String | N/A | N/A  
Zone Name | String | N/A | N/A  
  
#### Use cases

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
        {
          "browser": "Chrome",
          "_domain":"siemplify.co",
          "severity": "error",
          "service": "Elastica",
          "latitude": 32.0678,
          "user": "john_doe@example.com",
          "object_type": "Session",
          "location": "Tel Aviv (Israel)",
          "longitude": 34.7647,
          "device": "Windows",
          "host": "1.1.1.1",
          "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
          "created_timestamp": "2019-01-20T07:49:14",
          "event_type": "PORTAL_LOGIN_FAILURE",
          "message": "Failed login attempt by user 'john_doe@example.com'", "_id": "--Fi3z-1QHewAgPiTQlvXQ",
          "user_name": "John Doe",
          "inserted_timestamp": "2019-01-20T07:49:14",
          "activity_type": "Failure"
        },
      "Entity": "john_doe@example.com"
    }]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
