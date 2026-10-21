---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali-staxx/
title: Integrate Anomali STAXX with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:24.859907+00:00
---

# Integrate Anomali STAXX with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali-staxx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Anomali STAXX with Google SecOps 

This document explains how to integrate Anomali STAXX with Google Security Operations (Google SecOps).

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server Address | String | https://<ip>:<port> | Yes | Server address of the Anomali STAXX instance.  
Username | String | N/A | Yes | Username of the Anomali STAXX account.  
Password | Password | N/A | Yes | Password of the Anomali STAXX account.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the Anomali STAXX server is valid.  
Run Remotely | Checkbox | Checked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test connectivity to Anomali STAXX with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

None.

#### Run on

This action doesn't run on entities, nor has mandatory input parameters.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful:_ "Successfully connected to the Anomali STAXX server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Anomali STAXX server! Error is {0}".format(exception.stacktrace) | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Anomali STAXX - Indicators Connector

Pull indicators from Anomali STAXX.

#### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes |  The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
Event Field Name | String | itype | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Int | 180 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
Server Address | String | https://<ip>:<port> | Yes | Server address of the Anomali STAXX instance.  
Username | String | N/A | Yes | Username of the Anomali STAXX account.  
Password | Password | N/A | Yes | Password of the Anomali STAXX account.  
Server Timezone | String | N/A | No | Specify which timezone is set on the Anomali STAXX server in regards to UTC, such as `+1` or `-1`. If nothing is specified, the connector uses UTC as a default timezone.  
Lowest Severity To Fetch | String | Medium | Yes | Lowest severity that will be used to fetch Indicators. Possible values:

  * Low
  * Medium
  * High
  * Critical

  
Lowest Confidence To Fetch | Integer | 0 | No | Lowest confidence that will be used to fetch indicators.  
Fetch Max Hours Backwards | Integer | 1 | No | The number of hours prior to now to retrieve indicators. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Indicators To Fetch | Integer | 50 | No | How many indicators to process per one connector iteration.  
`Use whitelist as a blacklist` | Checkbox | Unchecked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If selected, the integration validates the SSL certificate when connecting to the Anomali STAXX server.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
