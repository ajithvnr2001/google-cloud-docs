---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/micro-focus-itsma/
title: Micro Focus ITSMA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:07.230493+00:00
---

# Micro Focus ITSMA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/micro-focus-itsma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Micro Focus ITSMA

This document provides guidance on how to integrate Micro Focus ITSMA with Google SecOps.

## Configure Micro Focus ITSMA integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Create Incident

#### Description

Create a new incident.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Display Label | String | N/A | The display label of the incident.  
Description | String | N/A | The description of the incident.  
Impact Score | String | N/A | The impact scope of the incident.  
Urgency | String | N/A | The urgency of the incident.  
Service ID | String | N/A | The ID of the category of the incident.  
  
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
incident_id | N/A | N/A  
  
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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Update Incident

#### Description

Update an existing incident

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Incident ID | String | N/A | The ID of the incident.  
Display Label | String | N/A | The updated display label of the incident.  
Description | String | N/A | The updated description of the incident.  
Impact Score | String | N/A | The updated impact score of the incident.  
Urgency | String | N/A | The updated urgency of the incident.  
Service ID | String | N/A | The updated ID of the category of the incident.  
  
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
    

### Update Incident External Status

#### Description

Update the external status for an incident.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Incident ID | String | N/A | The ID of the incident.  
Status | String | N/A | The updated external status of the incident.  
  
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
