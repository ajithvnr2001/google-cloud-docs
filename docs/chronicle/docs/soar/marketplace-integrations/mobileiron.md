---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mobileiron/
title: MobileIron \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:00:22.279798+00:00
---

# MobileIron  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mobileiron/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MobileIron

**Important:** MobileIron was acquired by Ivanti. For more information about the MobileIron platform features, see [MobileIron Products](https://www.ivanti.com/company/history/mobileiron).

This document provides guidance on how to integrate MobileIron with Google SecOps.

## Configure MobileIron integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Fetch System Information

#### Description

Fetch system information for a device by its IP address.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Fields to Fetch | String | N/A | The values of the inserted fields will be fetched for a device (has to be comma separated string), ex: ios.DeviceName, user.display_name, user.email_address, user.user_id  
  
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
    

### Fetch System Information by UUID

#### Description

Get device system information by its UID.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device UUID | String | N/A | The UUID of the target device.  
  
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
    

### List Devices

#### Description

Get the list of all the devices at the system.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Fields to Fetch | String | N/A | The values of the inserted fields will be fetched for a device (has to be comma separated string), ex: ios.DeviceName, user.display_name, user.email_address, user.user_id  
  
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
    

### Ping

#### Description

Test integration connectivity.

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
    

### Unlock Device

#### Description

Unlock a device by its IP address.

#### Parameters

N/A

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
    

### Unlock Device by UUID

#### Description

Unlock a device by its UUID.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device UUID | String | N/A | The UUID of the target device.  
  
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
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
