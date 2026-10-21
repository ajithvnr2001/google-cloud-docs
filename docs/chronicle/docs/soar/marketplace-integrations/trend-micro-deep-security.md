---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-deep-security/
title: Trend Micro Deep Security \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:04:29.646924+00:00
---

# Trend Micro Deep Security  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-deep-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trend Micro Deep Security

This document provides guidance on how to integrate Trend Micro Deep Security with Google SecOps.

## Configure Trend Micro Deep Security to work with Google Security Operations

To create a new API key:

  1. Navigate to **Administration** > **User Management** > **API Keys**.
  2. Click **New**.
  3. In the **Properties** window, enter a _Name_ and _Description_ for the API key.
  4. Click on the **Role** list and select a role.
  5. Next, select a **Language** and a **Time Zone**. You can also select **Expires on** , which is optional, for expiry date for the API key.
  6. Click **OK**.
  7. Copy the **Secret key value**. Make sure to copy the secret key value now, because this is the only time it will be shown.



## Configure Trend Micro Deep Security integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{host or IP}:{port} | Yes | API root of the Trend Micro Deep Security instance.  
API Secret Key | Password | N/A | Yes | API Secret Key of the Trend Micro Deep Security instance.  
API Version | String | v1 | Yes | API Version of the Trend Micro Deep Security instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trend Micro Deep Security server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Assign Security Profile to Host

#### Description

Assign the specified policy to computers.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Security Profile Name | String | N/A | Policy Name.  
  
#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_assigned | True/False | is_assigned:False  
  
##### JSON Result
    
    
    N/A
    

### Get Host Info

#### Description

Describe a computer.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

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
    

### Get Security Profiles

#### Description

Get all of the policies from Deep Security.

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
    

### Ping

#### Description

Verifies that the user has a connection to Trend Micro Deep Security via the user's device.

#### Parameters

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
is_ connected | True/False | is_connected:False  
  
##### JSON Result
    
    
    N/A
    

### Scan Host

#### Description

Request a malware scan.

#### Parameters

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_ success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
