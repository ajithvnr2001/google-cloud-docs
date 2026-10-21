---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-nx/
title: FireEye NX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:24.334746+00:00
---

# FireEye NX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-nx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye NX

**Important:** FireEye and McAfee Enterprise merged and became Trellix. FireEye NX was renamed to Trellix Network Security (NX).

This document describes how to integrate FireEye NX with Google Security Operations.

## Use Cases

  1. Ingest Trellix Network Security alerts to use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform enrichment actions - download alert artifacts using Trellix Network Security agent from Google SecOps.



## Configure FireEye NX integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://x.x.x.x:<port> | Yes | API root of Trellix Network Security server.  
Username | String | N/A | Yes | Username of the Trellix Network Security account.  
Password | Password | N/A | Yes | Password of the Trellix Network Security account.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the Trellix Network Security server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trellix Network Security with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully connected to the Trellix Network Security server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
****_If not successful:_ Print "Failed to connect to the Trellix Network Security server! Error is {0}".format(exception.stacktrace) | General  
  
### Download Alert Artifacts

#### Description

Download alert artifacts.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert UUID | String | N/A | Yes | Specify the alert uuid from where we need to download artifacts.  
Download Path | String | N/A | Yes | Specify where the action should save the files.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_if status code 200 (is_success = true):_ Print "Successfully downloaded Trellix Network Security alert artifacts with alert id {0}!".format(alert uuid)****  
****_if status code 200 (is_success = true):_ Print "Action wasn't able to download Trellix Network Security alert artifacts with alert id {0}. Reason: File with that path already exists."_if status code 404 (is_success = false) :_ Print "Artifacts for alert with uuid {0} were not found. ".format(alert_uuid)**The action should fail and stop a playbook execution:**  
****_if fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Download Alert Artifacts". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add IPS Policy Exception

#### Description

Add IPS Policy Exception in Trellix Network Security.

**Note:** IP entities are treated as "Attacker IP Address".

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Victim IP Subnet | String | x.x.x.x/24 | Yes | Specify the IP subnet of the victim that should be used to create a new policy exception. Format: x.x.x.x/xx. Example: 10.0.0.1/24  
Interface | DDL | ALLPossible ValuesABCDALL | Yes | Specify what interface should be used in policy exceptions.  
Mode | DLL | BlockPossible ValuesBlockUnblockSuppressSuppress-unblock | Yes | Specify the mode that should be used in the policy exception.  
Name | String | N/A | No | Specify the name for the policy exception. If nothing is specified, the action adds policy exceptions with the following name: `PRODUCT_NAME_INTERFACE_MODE` .  
  
#### Run On

The action runs on the IP entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 for at least one entity (is success=true):** "Successfully added IPS policy exceptions in Trellix Network Security based on the following entities: {0}!".  
******If one or more entities didn't work (status code 400) (is success=true):** "Action wasn't able to add IPS policy exceptions based on the following entities:\n{0}".  
******if none of the entities worked:** "No IPS policy exception were created".  
****  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Add IPS Policy Exception". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connectors

### FireEye NX - Alerts Connector

#### Description

Connector ingest Trellix Network Security alert into Google SecOps.

#### Configure FireEye NX - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:x | Yes | API root of Trellix Network Security server.  
Username | String | N/A | Yes | Username of the Trellix Network Security account.  
Password | Password |  | Yes | Password of the Trellix Network Security account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix Network Security server is valid.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, dynamic list will be used as a blocklist.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
