---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-etp/
title: FireEye ETP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:48.913669+00:00
---

# FireEye ETP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-etp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye ETP

**Important:** FireEye and McAfee Enterprise merged and became Trellix. FireEye ETP was renamed to Trellix Email Security - Cloud Edition.

This document describes how to integrate FireEye ETP with Google Security Operations.

**Note:** This integration has been updated to utilize FireEye ETP public API endpoints v2. Legacy V1 API support has been completely removed. Ensure your target instance configurations are updated to prevent ingestion disruptions.

## Use Cases

Ingest Trellix Email Security - Cloud Edition alerts and use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.

## Configure FireEye ETP Integration to work with Google SecOps

### Where to find API Key

  1. Navigate to account settings.
  2. Select "API Keys" section
  3. Press on the "Create API Key" button
  4. Fill out the mandatory fields. As a product choose "Email Threat Prevention".
  5. Press on the "Next" button
  6. Press on the "Grant All" button
  7. Press on the "Create API Key" button
  8. Copy API Key and paste it in "API Key" integration configuration parameter.



## Configure FireEye ETP integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://us.etp.trellix.com | Yes | API root of the FireEye ETP instance.  
API Key | String | N/A | No | API Key of the FireEye ETP account.  
Client ID | String | N/A | No | Client ID for Trellix IAM OAuth authentication.  
Client Secret | Password | N/A | No | Client Secret for Trellix IAM OAuth authentication.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the FireEye ETP server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Trellix Email Security - Cloud Edition with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
N/A |  |  |  |   
  
#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** "Successfully connected to the Trellix Email Security - Cloud Edition server with the provided connection parameters!" **The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to connect to the Trellix Email Security - Cloud Edition server! Error is {0}".format(exception.stacktrace) | General  
  
## Connector

### FireEye ETP - Email Alerts Connector

#### Description

Pull alerts from Trellix Email Security - Cloud Edition. Alerts from Trellix Email Security - Cloud Edition are grouped based on the email ID into one Google SecOps Alert.

#### Configure FireEye ETP - Email Alerts Connector in Google SecOps

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
API Root | String | https://us.etp.trellix.com | Yes | API root of the FireEye ETP instance.  
API Key | String | N/A | No | API Key of the FireEye ETP account.  
Client ID | String | N/A | No | Client ID for Trellix IAM OAuth authentication.  
Client Secret | Password | N/A | No | Client Secret for Trellix IAM OAuth authentication.  
Fetch Max Hours Backwards | Integer | 1 | No | Number of hours before the first connector iteration to retrieve alerts from.  
Timezone | String |  | No | Timezone of the instance. Default: UTC.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the FireEye ETP server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
