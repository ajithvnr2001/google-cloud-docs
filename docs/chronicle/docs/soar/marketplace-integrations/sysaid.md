---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sysaid/
title: SysAid \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:05.294987+00:00
---

# SysAid  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sysaid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SysAid

This document provides guidance on how to integrate SysAid with Google SecOps.

## Configure SysAid integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Close Service Request

#### Description

Close a service request by its ID.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Solution | String | N/A | The solution of the request service.  
  
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
    

### Create Service Request

#### Description

Create a service request.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Title | String | N/A | The title of the service request.  
Description | String | N/A | The description of the service request.  
Service Request Type | String | N/A | The type of the service request. Valid values: incident, request, problem, change, all.  
Status | String | N/A | The status of the request service.  
Priority | String | N/A | The priority of the request service.  
Assignee | String | N/A | The assignee of the request service.  
Urgency | String | N/A | The urgency of the request service.  
Request User | String | N/A | The request user of the request service.  
Category | String | N/A | The category of the request service.  
Subcategory | String | N/A | The subcategory of the request service.  
Third Category | String | N/A | The third category of the request service.  
Assigned Group | String | N/A | The assigned group of the request service.  
  
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
    

### Delete Service Request

#### Description

Delete a service request.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Service Request ID | String | N/A | The ID of the service request to delete.  
  
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
    

### Get Service Request

#### Description

Get a service request.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Service Request ID | String | N/A | The ID of the service request to get info about.  
  
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
service_request | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### List Service Requests

#### Description

List service requests.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Service Request Type | String | N/A | The type of the service request to filter by. Valid values: incident, request, problem, change, all.  
Status | String | N/A | The status of the request service to filter by.  
Priority | String | N/A | The priority of the request service to filter by.  
Assignee | String | N/A | The assignee of the request service to filter by.  
Urgency | String | N/A | The urgency of the request service to filter by.  
Request User | String | N/A | The request user of the request service to filter by.  
Category | String | N/A | The category of the request service to filter by.  
Subcategory | String | N/A | The subcategory of the request service to filter by.  
Third Category | String | N/A | The third category of the request service to filter by.  
Assigned Group | String | N/A | The assigned group of the request service to filter by.  
Get Archived | Boolean | N/A | Whether to get archived request services or not.  
  
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
request_services | True/False | request_services:False  
  
##### JSON Result
    
    
    N/A
    

### List Users

#### Description

List SysAid users.

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
users | True/False | users:False  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Test the connectivity to SysAid.

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
    

### Update Service Request

#### Description

Update a service request.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Service Request ID | String | N/A | The ID of the service request to update.  
Status | String | N/A | The new status of the request service.  
Priority | String | N/A | The new priority of the request service.  
Assignee | String | N/A | The new assignee of the request service.  
Urgency | String | N/A | The new urgency of the request service.  
Request User | String | N/A | The new request user of the request service.  
Category | String | N/A | The new category of the request service.  
Subcategory | String | N/A | The new subcategory of the request service.  
Third Category | String | N/A | The new third category of the request service.  
Assigned Group | String | N/A | The new assigned group of the request service.  
  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
