---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/armis/
title: Integrate Armis with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:45:56.542731+00:00
---

# Integrate Armis with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/armis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Armis with Google SecOps

This document describes how to integrate Armis with Google Security Operations.

## Use Cases

  1. Perform enrichment actions.
  2. Perform ingestion of the alerts.
  3. Perform triaging action (Update Alert Status).



## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | {{root}} | Yes | Armis API root  
API Secret | Password | N/A | Yes | Armis API secret  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Armis server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to Armis.

#### Parameters

N/A

#### Run on

The action doesn't use entities, nor has mandatory input parameters.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successful:** "Successfully connected to the Armis server with the provided connection parameters!" **The action should fail and stop a playbook execution:** **if not successful:** "Failed to connect to the Armis server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Enrich entities using information from Armis. Supported entities: IP, Mac Address.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Create Endpoint Insight | Checkbox | Checked | Yes | If enabled, the action creates an insight containing information about the endpoints.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Mac Address



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON result
    
    
    {
        "accessSwitch": null,
        "category": "Computers",
        "dataSources": [
            {
                "firstSeen": "2021-03-07T04:04:22.562873+00:00",
                "lastSeen": "2021-03-07T04:04:22.562873+00:00",
                "name": "Example",
                "types": [
                    "Asset & System Management",
                    "Virtualization"
                ]
            },
            {
                "firstSeen": "2021-03-07T04:04:22.562873+00:00",
                "lastSeen": "2021-03-07T04:04:22.562873+00:00",
                "name": "Armis Smart Scanner",
                "types": [
                    "Vulnerability Management"
                ]
            }
        ],
        "firstSeen": "2021-03-07T04:04:22.562873+00:00",
        "id": 1616,
        "ipAddress": "192.0.2.120",
        "ipv6": null,
        "lastSeen": "2021-03-21T08:05:40.244960+00:00",
        "macAddress": "01:23:45:ab:cd:ef",
        "manufacturer": "VMware",
        "model": "VMware Virtual Platform",
        "name": "Example",
        "operatingSystem": "CentOS",
        "operatingSystemVersion": "6.6",
        "purdueLevel": 4.0,
        "riskLevel": 5,
        "sensor": {
            "name": "North conference room",
            "type": "Physical Sensor"
        },
        "site": {
            "location": "Palo Alto",
            "name": "Palo Alto Offices"
        },
        "tags": [
            "Discover",
            "Example"
        ],
        "type": "Virtual Machines",
        "user": "",
        "visibility": "Full"
    }
    

#### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
category | When available in JSON  
id | When available in JSON  
ipAddress | When available in JSON  
macAddress | When available in JSON  
name | When available in JSON  
os | When available in JSON  
purdue_level | When available in JSON  
risk_level | When available in JSON  
tags | When available in JSON  
type | When available in JSON  
user | When available in JSON  
visibility | When available in JSON  
site | When available in JSON  
link | When available in JSON  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if enriched some(is_success = true):** "Successfully enriched the following entities using Armis:\n".format(entity.identifier) **If didn't enrich some (is_success = true):** "Action wasn't able to enriche the following entities using Armis:\n".format(entity.identifier) **If didn't enrich all (is_success = false):** "No entities were enriched". **The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Entity Table |  | Entity  
  
### List Alert Connections

List connections related to the alert in Armis.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Alert ID | Integer |  | Yes | Specify the id of the alert for which you want to pull connections data.  
Lowest Severity To Fetch | DDL | Medium Possible Values:

  * Low
  * Medium
  * High

| No | Specify the lowest severity of the connections that should be used when fetching them.  
Max Connections To Return | Integer | 50 | No | Specify how many connections to return.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON result
    
    
    {
        "band": null,
        "channel": null,
        "dhcpAuthenticationDuration": null,
        "duration": 12339,
        "endTimestamp": "2021-03-18T20:19:31.562873+00:00",
        "id": 33355,
        "inboundTraffic": 12412512,
        "outboundTraffic": 19626489,
        "protocol": "Bluetooth",
        "radiusAuthenticationDuration": null,
        "risk": "Medium",
        "rssi": null,
        "sensor": {
            "name": "EXAMPLE",
            "type": "Switch"
        },
        "site": {
            "location": "Location",
            "name": "Location HQ"
        },
        "snr": null,
        "sourceId": 2097,
        "startTimestamp": "2021-03-18T16:53:52.562873+00:00",
        "targetId": 217,
        "title": "Connection between Example and user's iPhone",
        "totalAssociationDuration": null,
        "traffic": 32039001,
        "wlanAssociationDuration": null
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if 200 and data is available (is_success = true):** "Successfully returned connections related to the alert {alertId} based on the provided criteria in Armis." **If 200 and no data is available (is_success=false):** "No connections were found related to the alert {alertId} based on the provided criteria in Armis." **The action should fail and stop a playbook execution:** **if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Alert Connections". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** Available Communications **Columns:**

  * Title
  * Protocol
  * Severity
  * Start Time
  * End Time

| General  
  
### Update Alert Status

Update status of the alert in Armis.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Alert ID | Integer |  | Yes | Specify the id of the alert for which you want to update status.  
Status | DDL | Unhandled Possible values:

  * Unhandled
  * Suppressed
  * Resolved

| No | Specify what status should be set for the alert.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
**Output message*** | **The action should not fail nor stop a playbook execution:** **if 200 (is_success = true):** "Successfully updated status of the alert "{alert id}" to "{status}" in Armis.". **If 400 (is_success=true):** "Alert "{alert id}" already has status "{status}" in Armis. " **The action should fail and stop a playbook execution:** **if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Update Alert Status". Reason: {0}''.format(error.Stacktrace) **If 404:** "Error executing action "Update Alert Status". Reason: alert "{alert id}" wasn't found in Armis.' | **General**  
  
## Connector

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Armis - Alerts Connector

Pull alerts with related activities from Armis.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | alert_type | Yes | The name of the field where the product name is stored.The default value is `alert_type`.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `alert_type` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.  
Event Field Name | String | type | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
API Root | String | https://{{api_root}} | Yes | API root of the Armis instance.  
API Secret | Password | N/A | Yes | API Secret of the Armis account.  
Lowest Severity To Fetch | Low | Low | No | Lowest severity that will be used to fetch alerts. Possible values: `Low`, `Medium`, `High`.  
Max Hours Backwards | Integer | 1 | No | The number of hours before the first connector iteration to retrieve the alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Alerts To Fetch | Integer | 10 | No | The number of alerts to process per one connector iteration. The maximum value is `1000`.  
`Use whitelist as a blacklist` | Checkbox | Checked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If selected, the integration validates the SSL certificate when connecting to the Armis server.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
