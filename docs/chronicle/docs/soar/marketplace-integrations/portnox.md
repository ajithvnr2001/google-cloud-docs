---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/portnox/
title: Portnox \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:24:38.119007+00:00
---

# Portnox  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/portnox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Portnox

This document provides guidance on how to integrate Portnox with Google SecOps.

## Configure Portnox Integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Enrich Device

#### Description

Enrich each of the query result devices (based on MAC address) with additional data from Portnox.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get Device History

#### Description

Get device history.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Days Backwards | String | N/A | Fetch history 'x' days backwards. Example: 1  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get Device Locations

#### Description

Get the locations of a device.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get Installed Applications

#### Description

Get a list of all of the installed applications on a device.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get Open Ports

#### Description

Get a list of all open ports on a device.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get Services

#### Description

Get a list of all of the services on a device.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
    

### Get User History

#### Description

Get the user authentication history of a device.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
is_success | True/False | is_success:True/False  
  
##### JSON Result
    
    
    N/A
    

### Revalidate Device

#### Description

Revalidate the device policy over Portnox NAC.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
DeviceId | String | N/A | The device to revalidate ID.  
  
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
is_valid | True/False | is_valid:False  
  
##### JSON Result
    
    
    N/A
    

### Revalidate Device by Address

#### Description

Revalidate a device by the IP address or by MAC address.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * MAC Address



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
