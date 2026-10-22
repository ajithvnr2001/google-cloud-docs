---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-active-response/
title: McAfee Active Response \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:27.059811+00:00
---

# McAfee Active Response  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-active-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee Active Response

**Important:** McAfee Active Response became part of the Trellix product portfolio and is known as Active Response. Active Response will reach end of life on December 31, 2023.

This document provides guidance on how to integrate McAfee Active Response with Google SecOps.

## Configure McAfee Active Response integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

## Actions

### Ping

#### Description

Test the connectivity to Active Response.

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
    

### Search

#### Description

Active Response searches data on your managed endpoints in real time.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Collectors | String | N/A | The collectors to search in.  
Filter Collector | String | N/A | The collector filter.  
Filter By | String | N/A | The field to filter by.  
Filter Operator | String | N/A | The operator of the filter. Must be one of these: GreaterEqualThan, GreaterThan, LessEqualThan, LessThan, Equals, Contains, StartWith, EndsWith, Before, and After.  
Filter Value | String | N/A | The filter value.  
  
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
