---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/harmony-mobile/
title: Harmony Mobile \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:27.865646+00:00
---

# Harmony Mobile  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/harmony-mobile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Harmony Mobile

This document provides guidance on how to integrate Harmony Mobile with Google SecOps.

## Use Cases

  1. Perform enrichment of entities
  2. Ingestion of alerts



## How to generate Client ID and Client Secret

  1. Navigate to "Harmony Endpoint" section
  2. Go to "Global Settings"
  3. Go to "API Keys" section
  4. Press on the "New" button.
  5. Select "Harmony Mobile" Service and "Read-Only" role
  6. Copy "Client ID" and "Client Secret". Put those parameters into integration configuration.



## Configure Harmony Mobile integration on Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://cloudinfra-gw.portal.checkpoint.com | Yes | API root of the Harmony Mobile instance.  
Client ID | String | N/A | Yes | Client ID of the Harmony Mobile account.  
Client Secret | Password | N/A | Yes | Client Secret of the Harmony Mobile account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Harmony Mobile server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Harmony Mobile with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the Harmony Mobile server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Harmony Mobile server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Harmony Mobile. Supported entities: Hostname.

**Note:** Hostname entity should contain the "name" of the device.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "client_version": "3.8.6.4637",
        "device_type": "Android",
        "email": "dana@example.com",
        "internal_id": 1,
        "last_connection": "Wed, 14 Jul 2021 05:26:09 +0000",
        "mail_sent": true,
        "mdm": null,
        "model": "HUAWEI / HUAWEI GRA-L09",
        "name": "Dana Doe",
        "number": "+11",
        "os_type": "Android_4_x",
        "os_version": "6.0",
        "risk": "No Risk",
        "status": "Active"
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
client_version | When available in JSON  
device_type | When available in JSON  
email | When available in JSON  
last_connection | When available in JSON  
model | When available in JSON  
name | When available in JSON  
number | When available in JSON  
os_type | When available in JSON  
os_version | When available in JSON  
risk | When available in JSON  
status | When available in JSON  
  
##### Insights

![Example of entity
insight](https://docs.cloud.google.com/static/chronicle/images/integrations/harmony-mobile-enrich-entities-entity-insight.png)

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message | **The action should not fail nor stop a playbook execution:**  
**if data is available for one(is_success = true):** "Successfully enriched the following entities using information from Harmony Mobile: {entity.identifier}".  
******If data is not available for one (is_success=true):** "Action wasn't able to enrich the following entities using information from Harmony Mobile: {entity.identifier}". ******If data is not available for all (is_success=false):** None of the provided entities were enriched.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Title:** {entity.identifier} | Entity  
  
## Connector

### Harmony Mobile - Alerts Connector

#### Description

Pull information about alerts from Harmony Mobile. Note: whitelist filter works with "alertEvent" parameter.

#### Configure Harmony Mobile - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | alertType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://cloudinfra-gw.portal.checkpoint.com | Yes | API root of the Harmony Mobile instance.  
Client ID | String | N/A | Yes | Client ID of the Harmony Mobile account.  
Client Secret | Password | N/A | Yes | Client Secret of the Harmony Mobile account.  
Lowest Risk To Fetch | Integer |  | False | Lowest risk that needs to be used to fetch alerts. Possible values: Informational, Low, Medium, High. If nothing is specified, the connector will ingest alerts with all risk levels.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 100 | No | How many alerts to process per one connector iteration. Default: 100.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Harmony Mobile server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
