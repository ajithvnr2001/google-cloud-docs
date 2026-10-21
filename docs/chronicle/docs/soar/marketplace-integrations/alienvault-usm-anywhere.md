---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvault-usm-anywhere/
title: Integrate LevelBlue USM Anywhere with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:48:12.823605+00:00
---

# Integrate LevelBlue USM Anywhere with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvault-usm-anywhere/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate LevelBlue USM Anywhere with Google SecOps

This document describes how to integrate LevelBlue Unified Security Management (USM) Anywhere with Google Security Operations (Google SecOps).

**Important:** AlienVault USM Anywhere became LevelBlue USM Anywhere. In the Google SecOps platform, the integration for LevelBlue USM Anywhere is called _AlienVault USM Anywhere_.

## Network access to LevelBlue USM Anywhere

API access from Google SecOps to LevelBlue USM Anywhere: Allow traffic over port 443 (HTTPS).

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | N/A | Yes | Address of the LevelBlue USM Anywhere instance.  
ClientID | String | N/A | Yes | The ID of the user.  
Secret | Password | N/A | Yes | The password of the user account.  
Product Version | String | V2 | Yes | Version of the LevelBlue USM Anywhere product.  
Use SSL | Checkbox | Checked | No | If selected, the integration validates the SSL certificate when connecting to the LevelBlue USM Anywhere server.  
Run Remotely | Checkbox | Unchecked | No | Select the checkbox to run the configured integration remotely. Once selected, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Alarm Details

Retrieves details for an alarm by ID.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Alarm ID | String | N/A | Yes | The alarm ID. Can be obtained by running connector.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | _In case of error:_ "Failed to get details about AlienVault Anywhere alarm! Error is {}. action should fail." _Action pass successfully:_ "Successfully returned AlienVault Anywhere alarm {} details" _When Product version parameter is set to V1:_ "Action should fail with clear message that is supported in V2." | General  
CSV Table | **Columns:**

  * ID
  * Priority
  * Occurred Time
  * Received Time
  * Source
  * Source Organization
  * Source Country
  * Destination
  * Rule Attack ID
  * Rule Strategy
  * Rule ID
  * Rule Attack Tactic
  * Rule Attack Technique
  * Rule Intent

| General  
  
### List Events

Search for AlienVault events.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Alarms Limit | String | N/A | No | Maximum number of alarms to return.  
Account Name | String | N/A | No | The account name.  
Event Name | String | N/A | No | The name of the event.  
Start Time | String | N/A | No | Filtered results will include events that occurred after this timestamp. Format: "%d/%m/%Y"  
End Time | String | N/A | No | Filtered results will include events that occurred before this timestamp. Format: "%d/%m/%Y"  
Suppressed | Checkbox | N/A | No | Whether to filter events by the suppressed flag.  
Source Name | String | N/A | No | The source name.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    {
        "rep_device_fqdn": "192.0.2.30",
        "sorce_name": "192.0.2.30",
        "tag": "pdate-esp-kernelmodle.sh",
        "timestamp_occred": "1596541223000",
        "destination_address": "198.51.100.130",
        "rep_dev_canonical": "192.0.2.30",
        "destination_name": "198.51.100.130",
        "received_from": "Centos7-001",
        "timestamp_occred_iso8601": "2020-08-04T11:40:23.000Z",
        "id": "f52dd545-ff14-5576-3b70-47f10f528f53",
        "needs_enrichment": True,
        "rep_device_asset_id": "256fa9b1-a066-c9eb-561a-c2110035978a",
        "timestamp_received": "1596541223152",
        "sorce_canonical": "256fa9b1-a066-c9eb-561a-c2110035978a",
        "destination_fqdn": "198.51.100.130",
        "_links": {
            "self": {
                "href": "URL"
            }
        },
        "has_alarm": False,
        "rep_device_address": "192.0.2.30",
        "event_name": "pdate-esp-kernelmodle.sh event",
        "sed_hint": False,
        "transient": False,
        "packet_type": "log",
        "was_fzzied": True,
        "sppressed": False,
        "log": "<13>Ag  4 14:40:23 Centos7-001 pdate-esp-kernelmodle.sh: McAfeeESPFileAccess installed in this system is - 198.51.100.130",
        "sorce_asset_id": "256fa9b1-a066-c9eb-561a-c2110035978a",
        "timestamp_received_iso8601": "2020-08-04T11:40:23.152Z",
        "destination_canonical": "198.51.100.130",
        "time_offset": "Z"
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | _In case of general error:_ "Action didn't complete due to error: {error}", result value should be set to false and the action should fail. _If the action is completed successfully:_ "Successfully returned {len(events)} AlienVault Anywhere events" _If the action failed to run:_ "Failed to list Endgame AlienVault Anywhere events!" _When Product version parameter is set to V1:_ "Action should fail with clear message that is supported in V2." | General  
CSV Table | **Table Title:** Events **Table Columns:**

  * ID
  * Name
  * Occurred Time
  * Received Time
  * Suppressed
  * Severity
  * Category
  * Sub Category
  * Access Control Outcome
  * Destination
  * Destination Port
  * Source
  * Source Port

**Values:**

  1. id= uuid
  2. name = event_name
  3. Occurred Time=timestamp_occurred_iso8601
  4. Received Time=timestamp_received_iso8601
  5. Suppressed =suppressed
  6. Severity = event_severity
  7. Category = event_category
  8. Sub Category = event_subcategory
  9. Access Control Outcome = access_control_outcome
  10. Destination = destination_name
  11. Destination Port = destination_port
  12. Source = source_name
  13. Source Port= source_port

| General  
  
### Ping

Test connectivity.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### AlienVault USM Anywhere Connector

Google SecOps fetches alarms from LevelBlue USM Anywhere in near real-time and forwards them as alerts for cases.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Environment | DDL | N/A | Yes | Select the required environment. For example, "Customer One". If the alert's **Environment** field is empty, it will be injected into this environment.  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection.  
Product Field Name | String | device_product | Yes | The field name used to determine the device product.  
Event Field Name | String | event_name | Yes | The name of the field that determines the event name (subtype).  
Max Days Backwards | Integer | 1 | Yes | The number of days before the first connector iteration to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Alerts Per Cycle | Integer | 10 | Yes | The maximum number of alerts to fetch in each connector's cycle. Limits the number of alerts in every cycle.  
Verify SSL | Checkbox | Unchecked | No | If selected, the integration validates the SSL certificate when connecting to the LevelBlue USM Anywhere server.  
Product Version | String | V2 | Yes | AlienVault Anywhere version - V1, V2.  
Secret | Password | N/A | Yes | The password of the according user.  
ClientID | String | N/A | Yes | ID of the user.  
Api Root | String | N/A | Yes | Example: https://<instance>.alienvault.com  
Script Timeout (Seconds) | String | 60 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Rule Method | String | N/A | No | Filter alarms by rule method. The method would provide additional detail on the target of the attack and the particular vulnerability. Example: Firefox - CVE-2008-4064  
Rule Strategy | String | N/A | No | The strategy of the rule that triggered the alarm. For example, use Client-Side Attack - Known Vulnerability when trying to exploit a known vulnerability in a web browser the attacker.  
Rule Intent | String | N/A | No | Filter alarms by the purpose of the alarm. The intent describes the context of the behavior that is being observed. These are the threat categories: System Compromise, Exploitation & Installation, Delivery & Attack, Reconnaissance & Probing, Environmental Awareness.  
Priority | String | N/A | No | Filter by alarm priority, comma-separated. Valid value: high/medium/low  
Use Suppressed Filter | Checkbox | Unchecked | No | This parameter will be used to determine whether to filter the incoming alerts using the Show Suppressed filter or not.  
Show Suppressed | Checkbox | Checked | No | Whether to include suppressed alarms in the search.  
Padding Period | Integer | 0 | No | Padding period in hours for the connector execution.  
  
The **AlienVault USM Anywhere Connector** has two parameters, allowing smart filtering of the alerts being ingested into Google SecOps, regarding the `suppressed` attribute that those alerts have:

  * **Use Suppressed Filter** : This parameter determines whether to filter the incoming alerts using the `Show Suppressed` filter or not.
  * **Show Suppressed** : This parameter determines whether to include suppressed alarms in the search or not. There are three options in this connector:

    1. Bring all the AV alerts in, suppressed and not suppressed - clear both boxes.
    2. Bring only the non-suppressed alarms from AV - select the `Use Suppressed Filter` box and clear the `Show Suppressed` box.
    3. Bring only the suppressed alarms from AV but nothing else - select both the `Use Suppressed Filter` and `Show Suppressed` boxes. It's a default option.



For more information on alarm suppression in AlienVault, see [Creating Suppression Rules from the Alarms Page](https://cybersecurity.att.com/documentation/usm-anywhere/user-guide/alarms/suppression-rule.htm).

#### Connector rules

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
