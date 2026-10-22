---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elastica-cloudsoc/
title: Elastica CloudSOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:46.876701+00:00
---

# Elastica CloudSOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elastica-cloudsoc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Elastica CloudSOC

**Important:** Elastica CloudSOC was acquired by Symantec and then by Broadcom and became Symantec CloudSOC.

This document describes how to integrate Elastica CloudSOC with Google Security Operations.

## Overview

## Configure Elastica CloudSOC integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get User Activities

#### Description

Fetch user activities from Symantec CloudSOC. Symantec CloudSOC provides insights into user activity and an overview of how cloud applications are used.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Minutes Back | String | N/A | Fetch logs since 'x' minutes backwards. Example: 5  
  
#### Use cases

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
browser | Returns if it exists in JSON result  
_domain | Returns if it exists in JSON result  
severity | Returns if it exists in JSON result  
latitude | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
object_type | Returns if it exists in JSON result  
location | Returns if it exists in JSON result  
longitiude | Returns if it exists in JSON result  
device | Returns if it exists in JSON result  
host | Returns if it exists in JSON result  
user_agent | Returns if it exists in JSON result  
created_timestamp | Returns if it exists in JSON result  
event_type | Returns if it exists in JSON result  
message | Returns if it exists in JSON result  
user_name | Returns if it exists in JSON result  
inserted_timestamp | Returns if it exists in JSON result  
activity_type | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
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
          "user_name": "Meny Har",
          "inserted_timestamp": "2019-01-20T07:49:14",
          "activity_type": "Failure"
        },
      "Entity": "john_doe@example.com"
    }]
    

### Ping

#### Description

Verifies connectivity to the Symantec CloudSOC server.

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
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
