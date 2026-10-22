---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberint/
title: Cyberint \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:49.867133+00:00
---

# Cyberint  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cyberint

This document describes how to integrate Cyberint with Google Security Operations.

## Configure Cyberint integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{instance}.cyberint.io | Yes | API root of the Cyberint instance.  
API Key | Password | N/A | Yes | API key of the Cyberint instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the Cyberint server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

Ingestion of alerts

## Actions

### Ping

#### Description

Test connectivity to the Cyberint with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't use entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Cyberint server with the provided connection parameters!"**The action should fail and stop a playbook execution:**___If not successful:_ "Failed to connect to the Cyberint server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Alert

#### Description

Update alert in Cyberint.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | Name | N/A | Yes | Specify the ID of the alert that would need to have the status updated.  
Status | DDL | Select OnePossible Values:

  * Open
  * Acknowledged
  * Closed

| No | Specify the status for the event. **Note:** If "Closed" is selected, the "Closure Reason" parameter needs to be provided as well.  
Closure Reason | DDL | Select One Possible Values:

  * Resolved
  * Irrelevant
  * False
  * Positive

| No | Specify the closure reason for closed status.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success = true):_ "Successfully updated the alert with ID "{alert_id}" in Cyberint.".**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Alert Status". Reason: {0}''.format(error.Stacktrace)_If "Select One" is provided:_ "Error executing action "Update Alert Status". Reason: "Status" needs to be provided.'' _If the "Status" parameter is set to "Closed", but the "Closure Reason" parameter isn't provided:_ "Error executing action "Update Alert Status". Reason: if "Status" is "Closed" then you need to provide "Closure Reason".'' | General  
  
## Connectors

## Cyberint - Alerts Connector

#### Description

Pull information about alerts from Cyberint.

**Note:** The whitelist filter works with the "type" parameter.

#### Configure Cyberint - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance}.cyberint.io | Yes | API root of the Cyberint instance.  
API Key | Password | N/A | Yes | API key of the Cyberint instance.  
Lowest Severity To Fetch | Integer | N/A | No | Lowest risk that needs to be used to fetch alerts. Possible values: Low, Medium, High, Very High. If nothing is specified, the connector will ingest alerts with all severities.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 100 | No | How many alerts to process per one connector iteration. Default: 100.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Cyberint server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Disable Overflow | Boolean | Unchecked | Yes | If enabled, the connector ignores the overflow mechanism.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
