---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/redis/
title: Redis \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:39:12.392333+00:00
---

# Redis  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Redis

This document provides guidance on how to integrate Redis with Google SecOps.

## Configure Redis integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add to List

#### Description

Add a value to the head of a Redis list. If the list does not exist then create a new list.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
List Name | String | N/A | Target list name.  
Value | String | N/A | Can be any of the following types: str, int, dict, list, etc.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_added | True/False | is_added:False  
  
##### JSON Result
    
    
    [
        "value1",
        "value2",
        "value3"
    ]
    

### Get Key

#### Description

Return the value at the selected key, or return none if the key doesn't exist

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Key Name | String | N/A | Target key name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
key_value | True/False | key_value:False  
  
##### JSON Result
    
    
    N/A
    

### Get List

#### Description

Return the value of an element from a Redis list.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
List Name | String | N/A | Target list name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Verifies that the user has a connection to Redis through the user's device.

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

Script Result Name | Value Options | Example  
---|---|---  
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
    N/A
    

### Set Key

#### Description

Set a string value in a Redis key. If the key already holds a value, then overwrite the value regardless of its type.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Key Name | String | N/A | Target key name.  
Value | String | N/A | Can be any of the following types: str, int, dict, list, etc.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insight

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_set | True/False | is_set:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
