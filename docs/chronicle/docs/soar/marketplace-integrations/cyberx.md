---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberx/
title: CyberX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:06.847562+00:00
---

# CyberX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CyberX

**Important:** CyberX was acquired by Microsoft and integrated with Azure Security Center for IoT.

This document describes how to integrate CyberX with Google Security Operations.

## Configure CyberX integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Enrich Endpoints

#### Description

Fetch details about the endpoints.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on the IP Address entity.

#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

### Get Alerts

#### Description

Fetch a list of all alerts XSense detects.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
alerts | N/A | N/A  
  
##### JSON result
    
    
    N/A
    

### Get Connection for Endpoint

#### Description

Get a list of each device's connections.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on the IP Address entity.

#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

### Get Device Vulnerability Report

#### Description

Fetch a report on vulnerabilities for each endpoint.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

### Get Events

#### Description

Fetch a list of reported events in the event log.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on the Events entity.

#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
events | True/False | events:False  
  
##### JSON result
    
    
    N/A
    

### Ping

#### Description

Test CyberX connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Entity enrichment

N/A

##### Insights

N/A

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
