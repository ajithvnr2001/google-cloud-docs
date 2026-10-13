---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-icdx/
title: Symantec ICDx \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:37.824591+00:00
---

# Symantec ICDx  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-icdx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec ICDx

This document provides guidance on how to integrate Symantec ICDx with Google SecOps.

## Configure Symantec ICDx integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Event

#### Description

Get event data by its ID.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Event UUID | String | N/A | N/A  
  
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
    

### Get Events Minutes Back

#### Description

Get events for query, by minutes back.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | Request query.  
Limit | String | N/A | Received events amount limit.  
Minutes Back | String | N/A | Fetch events minutes back parameter.  
Fields | String | N/A | Specific event fields to bring(Comma separated.)  
  
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
4.0 | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Test Symantec ICDx connectivity.

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
    

## Connectors

### Symantec ICDx query Connector

#### Description

Fetching events from Symantec ICDx server using a query.

#### Configure Symantec ICDx Query Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | String | device_product | The field name used to determine the device product.  
EventClassId | String | name | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | String | 60 | The timeout limit (in seconds) for the python process running current script.  
API Root | String | null | N/A  
API Token | Password | null | N/A  
Verify SSL | Boolean | FALSE | Whether to use son connection or not.  
Search Query | String | null | N/A  
Events Limit | Integer | 10 | Max count of events to pull in one cycle. Example: 20  
Max Days Backwards | Integer | 1 | Max number of days to fetch alerts since. Example: 3  
Proxy Server Address | String | null | The address of the proxy server to use.  
Proxy Username | String | null | The proxy username to authenticate with.  
Proxy Password | Password | null | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy support

The connector supports proxy.

##### Whitelist/Blacklist

The connector supports Whitelist/Blacklist rules.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
