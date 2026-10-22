---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-blue-coat-proxysg/
title: Symantec Blue Coat ProxySG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:57.744481+00:00
---

# Symantec Blue Coat ProxySG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-blue-coat-proxysg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Blue Coat ProxySG

**Important:** Symantec Blue Coat ProxySG was acquired by Broadcom and become Broadcom Symantec ProxySG.

This document provides guidance on how to integrate Symantec Blue Coat ProxySG with Google SecOps.

## Configure Symantec Blue Coat ProxySG integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
SSH Root | String | {ip address}:22 | Yes | SSH root of the Blue Coat ProxySG instance.  
Username | String | N/A | Yes | Username of the Blue Coat ProxySG SSH account.  
Password | Password | N/A | Yes | Base64 encoded CA certificate file.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

  1. Enrich entities.
  2. Block entities.



## Actions

### Ping

#### Description

Test connectivity to Broadcom Symantec ProxySG with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Broadcom Symantec ProxySG server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Broadcom Symantec ProxySG server! Error is {0}".format(exception.stacktrace)" | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Broadcom Symantec ProxySG. Supported entities: Hostname, IP Address, and URL.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "raw_output": "{raw output from the console}",
    
        "categories": {
            "Policy": "none",
            "Blue Coat": "none",
            "IWF": "none",
            "Local": "unavailable",
            "Proventia": "unavailable"
        },
        "category_group": {
            "Blue_Coat": "none"
        },
        "risk level": 1,
        "Country": "Unavailable",
        "Official Host Name": "twitter.com",
        "Resolved Addresses": [
            "104.244.42.1",
            "104.244.42.65"
        ],
        "Cache TTL": "1231, cache HIT",
        "DNS Resolver Response": "Success"
    }
    

##### Entity Enrichment

  * **Enrichment Table for URL - Prefix** BCProxySG_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
risk_level | {risk_level} | When available in JSON  
category_{categories.keys} | {categories/values} one key **Note:** One value as entry. | When available in JSON  
category_group_{category_group.keys} | {category_group/values} | When available in JSON  
  * **Enrichment Table for IP Address - Prefix** BCProxySG_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
country | {country} | When available in JSON  
  * **Enrichment Table for Hostname - Prefix** BCProxySG_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
official_hostname | {Official Host Name} | When available in JSON  
resolved_addresses | CSV of "Resolved Addresses" | When available in JSON  
cache_ttl | Cache TTL | When available in JSON  



##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Blue Coat ProxySG: {entity.identifier}."_If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Blue Coat ProxySG: {entity.identifier}" _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * Key
  * Value

| Entity  
  
### Block Entities

#### Description

Block entities using Broadcom Symantec ProxySG. Supported entities: IP Address.

#### Parameters

N/A

#### Run On

The action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "raw_output": "raw"
            "status": {success/failure}
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully blocked the following entities in Broadcom Symantec ProxySG: {entity.identifier}."_If data is not available for one entity (is_success=true):_ "Action wasn't able to block the following entities in Blue Coat ProxySG: {entity.identifier}."_If data is not available for all entities (is_success=false):_ "None of the provided entities were blocked."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
