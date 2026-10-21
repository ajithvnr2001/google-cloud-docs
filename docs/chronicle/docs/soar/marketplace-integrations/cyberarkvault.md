---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberarkvault/
title: CyberArk Vault \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:01:05.319724+00:00
---

# CyberArk Vault  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberarkvault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CyberArk Vault

This document describes how to integrate CyberArk Vault with Google Security Operations.

## Configure CyberArk Vault integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Disable User

#### Description

Update the attributes of a user by disabling the user.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
User Name | String | N/A | Full user name as it exists in the CyberArk Vault.  
  
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
    

### Enable User

#### Description

Update the users attributes by enabling the user.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
User Name | String | N/A | Full user name as it exists in the CyberArk Vault  
  
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
    

### Get Group Details

#### Description

Get details about a group.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
Group Name | String | N/A | Full group name as it exists in the CyberArk Vault.  
  
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
    

### Update Alert

#### Description

Get details on a user.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
User Name | String | N/A | Full user name as it exists in the CyberArk Vault.  
  
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
    

### Ping

#### Description

Test Connectivity.

#### Parameters

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
