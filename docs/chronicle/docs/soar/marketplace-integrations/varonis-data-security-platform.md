---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/varonis-data-security-platform/
title: Varonis Data Security Platform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:57.958716+00:00
---

# Varonis Data Security Platform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/varonis-data-security-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Varonis Data Security Platform

This document provides guidance on how to integrate Varonis Data Security Platform with Google SecOps.

## Product Use Cases

  1. Ingest Varonis alerts for analysis in Google Security Operations.
  2. Update the Varonis alerts from Google SecOps.



## Product PermissionConfiguration

To configure Varonis to work with Google SecOps the following steps need to be taken:

  1. A special API patch needs to be installed on DatAdvantage deployment, please contact Varonis team about it.
  2. User that will be used for the integration should have DatAdavantage "Web UI User" and "DatAlertConfiguration" roles.



## Configure Varonis Data Security Platform integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{ip address}:{port} | Yes | Specify API URL for the target Varonis Data Security instance.  
Username | String | N/A | Yes | Specify the username to connect with.  
Password | Password | N/A | Yes | Specify the password to connect with.  
Verify SSL | Checkbox | Checked | Yes | If enabled, the certificate configured for the API root is validated.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Varonis Data Security Platform with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page on the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run on

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Varonis Data Security Platform with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Varonis Data Security Platform! Error is {0}".format(exception.stacktrace)  | General  
  
### Update Alert

#### Description

Update Varonis Data Security Platform alert.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert GUID | CSV | N/A | Yes | Specify alert GUID for the update. This action can run on multiple alerts. Multiple alerts can be specified as a comma-separated string.  
Alert Status | DDL | Select One Possible values:

  * Select One
  * Open
  * Under Investigation
  * Closed

| Yes | Specify the alert status to update to.  
Closing Reason | DDL | Not Provided Possible values:

  * Not Provided
  * Resolved
  * Misconfiguration
  * Threat model disabled or deleted
  * Account misclassification
  * Legitimate activity
  * Other

| No | Specify the closing reason for the alert. When the alert status is changed to "closed", closing reason must be specified.  
  
#### Playbook Use Cases Examples

Update DatAdvantage alert from Google SecOps.

#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** If alert is updated successfully: "Alert(s) {0} were updated successfully".format(list of alerts) **The action should fail and stop a playbook execution:** If failed to update the alert: "Failed to update alert(s) {0} due to following error {1}".format(alert list, error code) If a fatal error, like wrong credentials, no connection to the server, other is reported: "Failed to execute "Update Alert" action! Error is {0}".format(exception.stacktrace)  | General  
  
## Connectors

### Varonis Data Security Platform Alerts Connector

#### Description

The connector can be used to fetch alerts from the Varonis Data Security Platform. The connector dynamic list can be used to filter specific alerts for ingestion based on the Varonis Data Security Platform alert name.

#### Configure Varonis Data Security Platform Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | device_product | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | Type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
PythonProcessTimeout | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{ip address}:{port} | Yes | Specify the API URL for the target Varonis Data Security Platform instance.  
Username | String | N/A | Yes | Specify the username to connect with.  
Password | Password | N/A | Yes | Specify the password to connect with.  
Max Days Backwards | Integer | 3 | Yes | Fetch alerts X days backwards.  
Max Alerts per Cycle | Integer | 10 | Yes | Fetch X alerts per connector cycle.  
Max Events per Varonis alert | Integer | 25 | Yes | Maximum number of events that the connector fetches for the Varonis Data Security Platform alert.  
Status | CSV | Open, Under Investigation, Closed | Yes | Data Security Platform alert statuses to fetch.  
Severity | CSV | Low, Medium, High | Yes | Data Security Platform alerts severities to fetch.  
Disable Overflow | Checkbox | Checked | No | If enabled, the connector ignores the Google SecOps overflow mechanism when creating alerts.  
Use Dynamic List as BlockList | Checkbox | Unchecked | Yes | If enabled, the connector uses alert names specified in the Dynamic list as a BlockList. It ingests only alerts that don't match Dynamic List.  
Verify SSL | Checkbox | Checked | Yes | If enabled, the certificate configured for the API root is validated.  
Alert Name Template | String | [Name] |  | If provided, the connector uses this value for Google SecOps Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Varonis alert - [name]. Note: The connector first uses CSOAR Event for placeholders. Only keys that have string value are handled. If nothing is provided or the user provides an invalid template, the connector uses the default alert name - [name].  
Rule Generator Template | String | [Name] |  | If provided, the connector uses this value for Google SecOps Rule Generator Value. You can provide placeholders in the following format: [name of the field]. Example: Varonis alert - [name]. Note: The connector first uses Google SecOps Event for placeholders. Only keys that have string value are handled. If nothing is provided or the user provides an invalid template, the connector uses the default rule generator - [name].  
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
