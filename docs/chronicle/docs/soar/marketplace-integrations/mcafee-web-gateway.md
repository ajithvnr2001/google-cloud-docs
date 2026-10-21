---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-web-gateway/
title: McAfee Web Gateway \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:10:48.502852+00:00
---

# McAfee Web Gateway  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-web-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee Web Gateway

This document provides guidance on how to integrate McAfee Web Gateway with Google SecOps.

## Configure McAfee Web Gateway

To configure the McAfee Web Gateway to work with the Google Security Operations integration, follow these steps:

  1. Enable REST API interface:

     1. On Web Gateway page, select Configuration → Appliances.
     2. On the appliances tree, select the appliance you want to administer using the REST interface and click User Interface.
     3. Under UI Access, select Enable REST interface over HTTPS (HTTP REST interface is optional).
     4. Click Save Changes.
  2. Give permission to access REST interface:

     1. On Web Gateway page, select Accounts → Administrator Accounts.
     2. In the Roles area, select an administrator role and click Edit. The Edit Role window opens.
     3. Select REST interface accessible.
     4. Click OK to close the window.
     5. Click Save Changes.



## Configure McAfee Web Gateway integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Block IP

#### Description

Insert IP addresses to an "IP range"-type group.

**Note:** This group should be a part of rule used to block IP addresses.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Group Name | String | N/A | The group name.  
Description | String | N/A | The entry description.  
  
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
is_blocked | True/False | is_blocked:False  
  
##### JSON Result
    
    
    N/A
    

### Insert Item to Group

#### Description

Insert a network object to a group (IP, URL, etc.). Note that each group is type stricted.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Group Name | String | N/A | The group name.  
Item to Insert | String | N/A | The item to insert to the group. Default: x.x.x.x/24.  
Description | String | N/A | The entry description.  
  
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
is_blocked | True/False | is_blocked:False  
  
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
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
    N/A
    

### Remove Item From Group

#### Description

Remove a network object to a group (IP, URL, etc.). Note that each group is type stricted.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Group Name | String | N/A | The group name.  
Item to Delete | String | N/A | The item to delete from the group. Default: x.x.x.x/32.  
  
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
is_unblocked | True/False | is_unblocked:False  
  
##### JSON Result
    
    
    N/A
    

### Unblock IP

#### Description

Delete IP addresses from an "IP range"-type group.

**Note:** This group should be a part of a rule used to block IP addresses.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Group Name | String | N/A | The group name to unblock the IP in.  
  
#### Use cases

N/A

#### Run On

his action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_unblocked | True/False | is_unblocked:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
