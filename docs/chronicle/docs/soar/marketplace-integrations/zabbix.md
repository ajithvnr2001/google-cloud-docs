---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zabbix/
title: Zabbix \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:50.618408+00:00
---

# Zabbix  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zabbix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zabbix

This document provides guidance on how to integrate Zabbix with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Zabbix.zip).

## Configure Zabbix integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://{IP}/Zabbix | Yes | The API root of the Zabbix instance.  
Username | String | N/A | Yes | The username of the Zabbix account.  
Password | Password | N/A | Yes | The password of the according user.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, the integration verifies that the SSL certificate for the connection to the Zabbix server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Execute Script

#### Description

Execute a script on hosts by the IP.

#### Parameters

Parameter Display Value | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Script Name | String | N/A | Yes | The name of the script to execute.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "response": "success",
                "value": "sudo: no tty present and no askpass program specified\\n"
            },
            "Entity": "1.1.1.1"
        }
    ]
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
response | Returns if it exists in JSON result  
value | Returns if it exists in JSON result  
  
##### Insights

N/A

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

## Connectors

### Zabbix Connector

#### Description

Zabbix connector fetches events from Zabbix.

**Note:** The connector only processes hosts that are not in maintenance mode. If the host is in maintenance mode, the connector ignores the event.

#### Configure Zabbix Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector: 

Parameter Display Value | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Field Name | Yes | The field name used to determine the device product.  
Event Field Name | String | Event Field Name | Yes | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | String | 300 | Yes | The timeout limit (in seconds) for the python process running current script.  
Api Root | String | N/A | Yes | N/A  
Username | String | N/A | Yes | N/A  
Password | Password | N/A | Yes | N/A  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | String | N/A | No | The proxy password to authenticate with.  
Verify SSL | Checkbox | Unchecked | No | If enabled, the integration verifies that the SSL certificate for the connection to the Zabbix server is valid.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

##### Whitelist/Blacklist

The connector supports Whitelist/Blacklist rules.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
