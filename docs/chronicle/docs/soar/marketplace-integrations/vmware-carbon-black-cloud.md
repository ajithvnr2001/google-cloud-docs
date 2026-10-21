---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-cloud/
title: VMware Carbon Black Cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:41.552158+00:00
---

# VMware Carbon Black Cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Carbon Black Cloud

This document provides guidance for administrators on how to configure and integrate VMware Carbon Black Cloud with the SOAR module of Google Security Operations.

## Overview

The VMware Carbon Black Cloud integration helps you with the following tasks:

  * Ingest VMware Carbon Black Cloud events and alerts to create alerts.

Google SecOps uses alerts to perform orchestrations with playbooks or manual analysis.

  * Perform enrichment actions.

Get data from VMware Carbon Black Cloud to enrich data in Google SecOps alerts.

  * Perform active actions.

Schedule a scan and quarantine a host in Google SecOps SOAR using the VMware Carbon Black Cloud agent.




This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/CBCloud.zip).

## Prerequisites

This section applies to the initial integration configuration. To ensure that the data flows as expected from VMware Carbon Black Cloud to Google SecOps, complete the steps that are listed in this section in VMware Carbon Black Cloud.

To configure API access for the VMware Carbon Black Cloud integration, complete the following steps:

  1. Configure the access level.
  2. Create an API key.



This integration has limitations. For more information about limitations, see [Configure Reputation Override](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/reputation-override-api/#configure-reputation-override) in the VMware Carbon Black Cloud documentation.

### Configure the access level

To configure the access level for the VMware Carbon Black Cloud integration, complete the following steps:

  1. In the VMware Carbon Black Cloud console, go to **Settings > API Access**.

  2. Select **Access Levels**.

  3. Click **Add Access Level**.

  4. Provide a name and description for the new access level and select the following permissions:

Category | Permission name | .Notation name | Permission type  
---|---|---|---  
Alerts | General information | org.alerts | Read  
Alerts | Dismiss | org.alerts.dismiss | Execute  
Device | Quarantine | device.quarantine | Execute  
Device | Bypass | device.bypass | Execute  
Device | General information | device | Read  
Device | Police assignment | device.policy | Update  
Device | Background scan | device.bg-scan | Execute  
Search | Events | org.search.events | CreateRead  
  5. Click **Save**.




### Create an API key

To create an API key for the VMware Carbon Black Cloud integration, complete the following steps:

  1. In the VMware Carbon Black Cloud console, go to **Settings > API Access > API Keys**.

  2. Click **Add API Key**.

  3. Enter the name for the key and select the access level that you created in a previous section.

  4. Click **Save** to obtain your API secret key and API ID pair.

Save the value of your API secret key as you cannot retrieve it later.




## Integrate VMware Carbon Black Cloud with Google SecOps

To configure or edit the integration parameters, you must be included in the Administrators permission group in Google SecOps. For more details about permissions groups for users, see [Working with permissions groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | Not applicable | No | Name of the instance that you intend to configure the integration for.  
Description | String | Not applicable | No | Description of the instance.  
API Root | String | `https://defense.conferdeploy.net/` | Yes | VMware Carbon Black Cloud API root URL.  
Organization Key | String | Not applicable | Yes | VMware Carbon Black Cloud organization key.  
API ID | String | Not applicable | Yes | VMware Carbon Black Cloud API ID (custom API key ID).  
API Secret Key | String | Not applicable | Yes | VMware Carbon Black Cloud API secret key (custom API secret key).  
Verify SSL | Checkbox | Selected | No | If selected, Google SecOps verifies that the SSL certificate for the connection to the VMware Carbon Black Cloud server is valid.  
Run Remotely | Checkbox | Not selected | No | Select the checkbox to run the configured integration remotely. After you select the checkbox, the option appears to select the remote user (agent).  
  
For instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can change the configuration at a later stage, if needed. After you configure the instances, you can use them in playbooks. For detailed information on configuring and supporting multiple instances, see [Support multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

Test connectivity to VMware Carbon Black Cloud.

#### Parameters

None.

#### Use cases

The action tests connectivity when executed from the integration configuration page in the Google SecOps Content Hub page. You can execute this action manually, but you can't use it in your playbooks.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the VMware Carbon Black Cloud server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the VMware Carbon Black Cloud server! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Enrich Entities

Enrich Google SecOps SOAR Host or IP Address entities based on the device information from the VMware Carbon Black Cloud.

This action runs on the following entities:

  * IP Address
  * Host



#### Use cases

Enrich Google SecOps SOAR host or IP entities with information from VMware Carbon Black Cloud, if the Carbon Black agent is installed on a respective IP address or host entity.

To help an incident responder investigate a possible malware alert from a host with a sensor installed, VMware Carbon Black Cloud can provide enrichment data such as the host information, sensor status, and its Carbon Black policy.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Entity enrichment

Enrichment field | Applicability  
---|---  
CB_Cloud.device_id | Always  
CB_Cloud.antivirus_status | Always  
CB_Cloud.antivirus_last_scan_time | If the information is displayed in the JSON result  
CB_Cloud.owner_email | If the information is displayed in the JSON result  
CB_Cloud.owner_first_name | If the information is displayed in the JSON result  
CB_Cloud.owner_last_name | If the information is displayed in the JSON result  
CB_Cloud.last_contact_time | Always  
CB_Cloud._last_device_policy_changed_time | If the information is displayed in the JSON result  
CB_Cloud.last_external_ip_address | Always  
CB_Cloud.last_internal_ip_address | Always  
CB_Cloud.last_location | Always  
CB_Cloud.full_device_name | Always  
CB_Cloud.organization_id | Always  
CB_Cloud.organization_name | Always  
CB_Cloud.device_os | If the information is displayed in the JSON result  
CB_Cloud.device_os_version | If the information is displayed in the JSON result  
CB_Cloud.passive_mode | Always  
CB_Cloud.device_policy_id | Always  
CB_Cloud.device_policy_name | Always  
CB_Cloud.device_policy_override | If true  
CB_Cloud.quarantined | Always  
CB_Cloud.scan_status | If the information is displayed in the JSON result  
CB_Cloud.sensor_out_of_date | Always  
CB_Cloud.sensor_states | Always  
CB_Cloud.sensor_version | Always  
CB_Cloud.device_status | Always  
  
##### Script result

The following table describes the values for the script result output when using the Enrich Entities action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Enrich Entities action:
    
    
    {
        "results": [
          {
            "activation_code": null,
            "activation_code_expiry_time": "2020-04-28T05:05:37.391Z",
            "ad_group_id": 649,
            "av_ave_version": null,
            "av_engine": "",
            "av_last_scan_time": null,
            "av_master": false,
            "av_pack_version": null,
            "av_product_version": null,
            "av_status": [
              "AV_DEREGISTERED"
            ],
            "av_update_servers": null,
            "av_vdf_version": null,
            "current_sensor_policy_name": "vmware-example",
            "deregistered_time": "2020-04-21T07:31:22.285Z",
            "device_meta_data_item_list": [
              {
                "key_name": "OS_MAJOR_VERSION",
                "key_value": "Windows 10",
                "position": 0
              },
              {
                "key_name": "SUBNET",
                "key_value": "10.0.2",
                "position": 0
              }
            ],
            "device_owner_id": 439953,
            "email": "User",
            "first_name": null,
            "id": 3401539,
            "last_contact_time": "2020-04-21T07:30:21.614Z",
            "last_device_policy_changed_time": "2020-04-21T05:05:57.518Z",
            "last_device_policy_requested_time": "2020-04-21T07:12:34.803Z",
            "last_external_ip_address": "198.51.100.209",
            "last_internal_ip_address": "203.0.113.15",
            "last_location": "OFFSITE",
            "last_name": null,
            "last_policy_updated_time": "2020-04-09T11:19:01.371Z",
            "last_reported_time": "2020-04-21T07:14:33.810Z",
            "last_reset_time": null,
            "last_shutdown_time": "2020-04-21T06:41:11.083Z",
            "linux_kernel_version": null,
            "login_user_name": null,
            "mac_address": "000000000000",
            "middle_name": null,
            "name": "<span class='hlt1'>WinDev2003Eval</span>",
            "organization_id": 1105,
            "organization_name": "cb-internal-alliances.com",
            "os": "WINDOWS",
            "os_version": "Windows 10 x64",
            "passive_mode": false,
            "policy_id": 36194,
            "policy_name": "vmware-example",
            "policy_override": false,
            "quarantined": false,
            "registered_time": "2020-04-21T05:05:37.407Z",
            "scan_last_action_time": null,
            "scan_last_complete_time": null,
            "scan_status": null,
            "sensor_kit_type": "WINDOWS",
            "sensor_out_of_date": false,
            "sensor_pending_update": false,
            "sensor_states": [
              "ACTIVE",
              "LIVE_RESPONSE_NOT_RUNNING",
              "LIVE_RESPONSE_NOT_KILLED",
              "LIVE_RESPONSE_ENABLED",
              "SECURITY_CENTER_OPTLN_DISABLED"
            ],
            "sensor_version": "3.4.0.1097",
            "status": "DEREGISTERED",
            "target_priority": "MEDIUM",
            "uninstall_code": "9EFCKADP",
            "vdi_base_device": null,
            "virtual_machine": false,
            "virtualization_provider": "UNKNOWN",
            "windows_platform": null
          }
        ],
        "num_found": 6
    }
    

##### Output messages

On a Case Wall, the Enrich Entities action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched entities:  ENTITY_ID_LIST` `No entities were enriched.` `Action was not able to find VMware Carbon Black Cloud info to enrich the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute Enrich Entities action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Dismiss VMware Carbon Black Cloud Alert

**Caution:** Starting on July 31, 2024, you will be unable to use Alerts v6 API in VMware Carbon Black Cloud. For details of the deprecation that VMware Carbon Black introduces to the Alerts v6 API, see [Alerts v6 API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/alerts-api/). We recommend that you update the integration version to upgrade to the Alerts v7 API.

Dismiss VMware Carbon Black Cloud alert.

In events that are created by VMware Carbon Black Cloud Alerts Connector, the **Event.id** field can be passed as a placeholder for alert ID to dismiss an alert in the Dismiss VMware Carbon Black Cloud Alert action.

This action accepts alert IDs in the alphanumeric format like `27162661199ea9a043c11ea9a29a93652bc09fd`, not in the format appearing in UI as `DONAELUN`.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | Not applicable | Yes | Alert ID to dismiss on VMware Carbon Black Cloud server. Specify the alert ID in the alphanumeric format like `27162661199ea9a043c11ea9a29a93652bc09fd`, not in the format appearing in UI as `DONAELUN`.  
Reason for dismissal | DDL | No dismissal reason | No | VMware Carbon Black Cloud reason for alert dismissal. Possible values are as follows:

  * No dismissal reason
  * Resolved
  * Resolved - Benign/Known good
  * Duplicate/Cleanup
  * Other

  
Determination | DDL | None | No | The determination value to set for an alert. Possible values are as follows:

  * None
  * True positive
  * False positive

  
Message for alert dismissal | String | Not applicable | No | Message to add to alert dismissal.  
  
#### Use cases

Dismiss or close a VMware Carbon Black Cloud alert based on the analysis done in Google SecOps SOAR.

After the alert was processed in Google SecOps SOAR, to keep the alert status synchronized between VMware Carbon Black Cloud and Google SecOps SOAR, the user needs an action that will dismiss (close) VMware Carbon Black Cloud alert from Google SecOps SOAR.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Dismiss VMware carbon Black Cloud Alert action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Dismiss VMware Carbon Black Cloud Alert action provides the following output messages:

Output message | Message description  
---|---  
`Successfully dismissed VMware Carbon Black Cloud alert with alert id ALERT_ID` `Failed to dismiss VMware Carbon Black Cloud alert! Error is ERROR_REASON` | Action succeeded.  
`Failed to execute Dismiss alert action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Update a Policy for Device by Policy ID

Change a policy on the VMware Carbon Black Cloud sensor on a host. The action scope is the IP Address or Host entity.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy ID | Integer | Not applicable | Yes | Specify a policy to associate with the VMware Carbon Black Cloud sensor.  
  
#### Use cases

Create a policy update task on VMware Carbon Black Cloud server from Google SecOps SOAR.

When analyzing alerts, an incident responder noticed that the same host generated multiple false-positive alerts in a short period of time. They can use this action to create a policy update task that changes the sensor policy to be less restrictive.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Update a Policy for Device by Policy ID action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Update a Policy for Device by Policy ID action provides the following output messages:

Output message | Message description  
---|---  
`Successfully changed device policy to DEVICE_POLICY for the following entities: ENTITY_ID_LIST` `No tasks were created.` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Action was not able assign policy DEVICE_POLICY for VMware Carbon Black Cloud devices for the following entities: ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities: ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Device Background Scan

Create a device background scan task on VMware Carbon Black Cloud server that is based on the IP Address or Host entities.

#### Use cases

Create a background scan task for the host using VMware Carbon Black Cloud sensor from Google SecOps SOAR.

When analyzing alerts, an incident responder notices that a host might be compromised. The incident responder can use this action to request an on-demand background scan of the host. This scan checks whether there are other suspicious executables on the host and the sensor on the host creates alerts for these suspicious executables.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Device Background Scan action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Device Background Scan action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created a background scan task for the following entities: ENTITY_ID_LIST` `No tasks were created` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Enable Bypass Mode for Device

Enable the bypass mode task for a device on the VMware Carbon Black Cloud server. The task is based on the Google SecOps SOAR IP Address or Host entities.

#### Use cases

Create an Enable Bypass Mode task on the VMware Carbon Black Cloud server from Google SecOps SOAR.

When analysing alerts related to a specific platform sensor or a host, an incident responder noticed that the sensor creates multiple false-positive alerts. They can use this action to enable the bypass mode for tracking what events the remote agent processes as alerts and updating the policies.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Enable Bypass Mode for Device action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Enable Bypass Mode for Device action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created enable bypass mode task for the following entities: ENTITY_ID_LIST` `No taskswere created` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Disable Bypass Mode for Device

Create a disable bypass mode task for devices on the VMware Carbon Black Cloud server. The task is based on the Google SecOps SOAR IP Address or Host entities.

#### Use cases

After enabling the bypass mode on a specific sensor and troubleshooting the VMware Carbon Black Cloud configuration and policies, an incident responder decided that the Carbon Black sensor works as expected and doesn't require to function in a bypass mode. They execute the Create Disable Bypass Mode Task for Device action to create a task for disabling the bypass mode on a specific host.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Disable Bypass Mode for Device action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Disable Bypass Mode for Device action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created disable bypass mode task for the following entities:  ENTITY_ID_LIST` `No tasks were created.` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Quarantine Device

Create a quarantine device task on the VMware Carbon Black Cloud server based on the Google SecOps SOAR IP Address or Host entities.

#### Use cases

An incident responder noticed that a host was showing signs of being compromised and can use this task to quarantine it.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Quarantine Device action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Quarantine Device action:
    
    
    [
      {
        "Entity": "siemplify-ID",
        "EntityResult": {
          "status": "done"
        }
      }
    ]
    

##### Output messages

On a Case Wall, the Quarantine Device action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created quarantine device task for the following entities:  ENTITY_ID_LIST` `No tasks were created.` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Unquarantine Device

Create an unquarantine device task on the VMware Carbon Black Cloud server based on the Google SecOps SOAR IP Address or Host entities.

#### Use cases

After analysing and remediating an alert related to a specific host that is managed by the VMware Carbon Black Cloud, an incident responder discovered that the host is not compromised. They execute the Unquarantine Device action to create an unquarantine host task on VMware Carbon Black Cloud server and connect to the host.

#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Unquarantine Device action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Unquarantine Device action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created quarantine device task for the following entities:  ENTITY_ID_LIST` `No tasks were created.` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Failed to execute action! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Execute Entity Processes Search

Use this action to search for information about processes that are stored in VMware Carbon Black Cloud.

This action runs on the following entities:

  * IP Address
  * Host
  * User
  * Hash
  * Process

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Start from Row | Integer | 0 | No | Specify the row to fetch data from.  
Max Rows to Return | Integer | 50 | No | Specify how many rows action should return.  
Create Insight | Checkbox | Not selected | No | If selected, the action creates a Google SecOps SOAR insight that is based on the process information from Carbon Black Cloud.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Entity enrichment

Enrichment field | Logic  
---|---  
IsSuspicous | Set to True when the returned data includes an alert category (`alert_category`) set to `THREAT` and a list of alert IDs (`alert_ids`) that is associated with the process.  
  
##### Script result

The following table describes the values for the script result output when using the Execute Entity Process Search action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Execute Entity Processes Search action:
    
    
    {
       "results": [
           {
               "alert_category": [
                   "THREAT"
               ],
               "alert_id": [
                   "19183229-384f-49a7-8ad7-87d0db243fcc",
                   "4dfc6aed-656d-41d1-9568-0de349d7a8b3",
                   "8eb04992-ed94-4471-8a71-fd78bad887de",
                   "ac3b3b3a-f4ce-41dc-9de8-123d5a1e2572",
                   "edc046a0-98f0-43eb-b3c0-a67469c11d19",
                   "f365a912-1d79-421e-bccb-f57b52100be8"
               ],
               "backend_timestamp": "2021-02-02T18:38:46.520Z",
               "childproc_count": 0,
               "crossproc_count": 0,
               "device_external_ip": "161.47.37.87",
               "device_group_id": 0,
               "device_id": 3602123,
               "device_installed_by": "sadiya@acalvio.com",
               "device_internal_ip": "172.26.115.53",
               "device_location": "UNKNOWN",
               "device_name": "desktop1-win10",
               "device_os": "WINDOWS",
               "device_os_version": "Windows 10 x64",
               "device_policy": "test",
               "device_policy_id": 32064,
               "device_target_priority": "HIGH",
               "device_timestamp": "2020-08-19T16:31:20.887Z",
               "document_guid": "sF1Ug1--SEyLWljQrWe8NA",
               "event_threat_score": [
                   6
               ],
               "filemod_count": 0,
               "ingress_time": 1612291119946,
               "modload_count": 0,
               "netconn_count": 0,
               "org_id": "7DESJ9GN",
               "parent_effective_reputation": "KNOWN_MALWARE",
               "parent_guid": "7DESJ9GN-0036f6cb-000026d4-00000000-1d676428bd025e2",
               "parent_hash": [
                   "86deb998e6b628755a1049a54b8863d32752d6176fb1ef3b7c4ee08c1f25edbc"
               ],
               "parent_name": "c:\\windows\\system32\\windowspowershell\\v1.o\\powershell.exe",
               "parent_pid": 9940,
               "parent_reputation": "KNOWN_MALWARE",
               "process_cmdline": [
                   "powershell.exe -ep bypass"
               ],
               "process_cmdline_length": [
                   25
               ],
               "process_effective_reputation": "COMPANY_BLACK_LIST",
               "process_guid": "7DESJ9GN-0036f6cb-000005b8-00000000-1d676428bdf1285",
               "process_hash": [
                   "908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6e22b5f6d53",
                   "cda48fc75952ad12d99e526d0b6bf70a"
               ],
               "process_name": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe",
               "process_pid": [
                   1464
               ],
               "process_reputation": "COMPANY_BLACK_LIST",
               "process_sha256": "908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6e22b5f6d53",
               "process_start_time": "2020-08-19T16:05:24.057Z",
               "process_username": [
                   "DESKTOP1-WIN10\\acalvio"
               ],
               "regmod_count": 0,
               "scriptload_count": 0,
               "watchlist_hit": [
                   "BeCXz92RjiQxN1PnYlM6w:SdJksR9SsWuLCJNeBsNPw:10",
                   "BeCXz92RjiQxN1PnYlM6w:s24xyq8SFapmQEMXv9yw:7",
                   "BeCXz92RjiQxN1PnYlM6w:s24xyq8SFapmQEMXv9yw:8"
               ]
           }
       ],
       "num_found": 1,
       "num_available": 1,
       "approximate_unaggregated": 6,
       "num_aggregated": 6,
       "contacted": 47,
       "completed": 47
    }
    

##### Output messages

On a Case Wall, the Execute Entity Processes Search action provides the following output messages:

Output message | Message description  
---|---  
`Process information was found for the following entities ENTITY_ID_LIST` `Process information was not found for all of the provided entities.` `Action was not able to find matching VMware Carbon Black Cloud devices for the following entities:  ENTITY_ID_LIST` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Error executing action "Execute Entity Processes Search". Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### List Reputation Overrides

Use this action to list reputation overrides that are configured in VMware Carbon Black Cloud.

This action doesn't run on entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Reputation Override List | DDL | Not SpecifiedPossible values:

  * Not Specified
  * White_List
  * Black_List

| No | Specify override list action should return.  
Reputation Override Type | DDL | Not Specified  
Possible values:

  * Not specified
  * SHA256 CERT
  * IT_TOOL

| No | Specify override type action should return.  
Start from Row | Integer | 0 | No | Specify from which row action should fetch data.  
Max Rows to Return | Integer | 50 | No | Specify how many rows action should return.  
Rows Sort Order | DDL | ASC  
Possible values:

  * ASC
  * DESC

|  | Specify sort order for the returned rows. Rows are sorted based on the `create_time` value.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Case wall table

On the Case Wall, the List Reputation Overrides provides the following tables:

  * SHA-256 table

**Table name** : Found SHA-256 Reputation Overrides

**Table columns:**

    * SHA-256 Hash
    * Filename
    * ID
    * Override List
    * Description
    * Source
    * Source Reference
    * Create Time
    * Created By
  * CERT table

**Table name:** Found CERT Reputation Overrides

**Table columns:**

    * Certificate Authority
    * Signed By
    * ID
    * Override List
    * Description
    * Source
    * Source Reference
    * Create Time
    * Created By
  * IT TOOL table

**Table name:** Found IT_TOOL Reputation Overrides

**Table columns:**

    * IT Tool Path
    * Include Child Processes
    * ID
    * Override List
    * Description
    * Source
    * Source Reference
    * Create Time
    * Created By



##### Script result

The following table describes the values for the script result output when using the List Reputation Overrides action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the List Reputation Overrides action for a certificate:
    
    
    {
       "num_found": 2,
       "results": [
           {
               "id": "6b040826d43a11eb85899b2a3fb7559d",
               "created_by": "user@example.com",
               "create_time": "2021-06-23T15:48:13.355Z",
               "override_list": "WHITE_LIST",
               "override_type": "CERT",
               "description": "",
               "source": "APP",
               "source_ref": null,
               "signed_by": "Example Software Corp.",
               "certificate_authority": "Symantec Class 3 SHA256 Code Signing CA"
           }
       ]
    }
    

The following example describes the JSON result output that is received when using the List Reputation Overrides action for a SHA-256 hash:
    
    
    {
       "num_found": 25,
       "results": [
           {
               "id": "0a0d2bf89d4d11ebbef6695028ab76fe",
               "created_by": "I2TK7ET355",
               "create_time": "2021-04-14T18:12:57.161Z",
               "override_list": "WHITE_LIST",
               "override_type": "SHA256",
               "description": "Test Data",
               "source": "APP",
               "source_ref": null,
               "sha256_hash": "f6a55db64b3369e7e0ce9abe8046c89ff3714c15c3174f04c10390c17af16f0e",
               "filename": null
           }
       ]
    }
    

The following example describes the JSON result output that is received when using the List Reputation Overrides action for an IT tool:
    
    
    {
       "id": "067ebeeaf03311eb8bb20bf76c87cd52",
       "created_by": "HZ9PEI2E3L",
       "create_time": "2021-07-29T06:05:50.790Z",
       "override_list": "BLACK_LIST",
       "override_type": "IT_TOOL",
       "description": "An override for an IT_TOOL",
       "source": "APP",
       "source_ref": null,
       "path": "C:\\TMP\\TMP\\TMP\\foo.exe",
       "include_child_processes": false
    }
    

##### Output messages

On a Case Wall, the List Reputation Overrides action provides the following output messages:

Output message | Message description  
---|---  
`Reputation overrides found.` `No reputation overrides found.` | Action succeeded.  
`Error executing action "List Reputation Overrides". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Create a Reputation Override for Certificate

Create a reputation override for the certificate. For more information about the reputation override, see [Reputation Override](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/reputation-override-api).

This action doesn't run on entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Certificate Authority | String | Not applicable | No | Specify the certificate authority that authorizes the validity of the certificate to add to reputation override.  
Signed By | String |  | Yes | Specify the name of the signer to add to reputation override.  
Description | String | Not applicable | No | Specify a description for the created reputation override.  
Reputation Override List | DDL | Not Specified | Yes | Specify an override list to create.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Create a Reputation Override for Certificate action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Create a Reputation Override for Certificate action:
    
    
    {
       "id": "fb19756cf03311eb81e9bf7658b8ce59",
       "created_by": "HZ9PEI2E3L",
       "create_time": "2021-07-29T06:12:41.168Z",
       "override_list": "WHITE_LIST",
       "override_type": "CERT",
       "description": "An override for a CERT",
       "source": "APP",
       "source_ref": null,
       "signed_by": "Test signer for override",
       "certificate_authority": "test cert ca"
    }
    

##### Output messages

On a Case Wall, the Create a Reputation Override for Certificate action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created new reputation override: OVERRIDE_ID` `Action failed to create a new certificate reputation override. Reason:ERROR_REASON` | Action succeeded.  
`Error executing action because Reputation Override List is not specified.` `Error executing action "Create a Reputation Override for Certificate". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Create a Reputation Override for SHA-256 Hash

Create a reputation override for the provided hash in the SHA-256 format. For more information about the reputation override, see [Reputation Override](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/reputation-override-api).

This action runs on the FileHash entity if it's provided.

You can provide the SHA-256 hash either as a Google SecOps SOAR FileHash entity (artifact) or as an action input parameter. If the hash is passed to action both as an entity and input parameter, then the action is executed on the input parameter.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
SHA-256 Hash | String | Not applicable | No | Specify a SHA-256 hash value to create an override for.  
Filename | String | Not applicable | Yes | Specify a corresponding filename to add to a reputation override.  
Description | String | Not applicable | No | Specify a description for the created reputation override.  
Reputation Override List | DDL | Not Specified | Yes | Specify an override list to create.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Create a Reputation Override for SHA-256 Hash action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Create a Reputation Override for SHA-256 Hash action:
    
    
    {
       "id": "1ea6c923f03211eb83cf87b4dce84539",
       "created_by": "HZ9PEI2E3L",
       "create_time": "2021-07-29T05:59:21.821Z",
       "override_list": "BLACK_LIST",
       "override_type": "SHA256",
       "description": "An override for a sha256 hash",
       "source": "APP",
       "source_ref": null,
       "sha256_hash": "af62e6b3d475879c4234fe7bd8ba67ff6544ce6510131a069aaac75aa92aee7a",
       "filename": "foo.exe"
    }
    

##### Output messages

On a Case Wall, the Create a Reputation Override for SHA-256 Hash action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created reputation override for the following entities:  ENTITY_ID_LIST` `Action failed to to create reputation override for the following entities: ENTITY_ID_LIST + API_ERROR` `No reputation overrides were created.` | Action succeeded.  
`Error executing action because wrong hash format was provided. Action is working only with Sha-256 hashes.` `Error executing action because Reputation Override List is not specified.` `Error executing action "Create a Reputation Override for SHA-256 Hash". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Create a Reputation Override for IT Tool

Use this action to create a reputation override for the specific IT tool such as Jira or ServiceNow. The reputation override is based on a filename and path. For more information about the reputation override, see [Reputation Override](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/reputation-override-api).

This action runs on the File entity if it's provided.

You can provide the filename either as a Google SecOps SOAR File entity (artifact) or as an action input parameter. If the filename is passed to the action both as an entity and input parameter, then the action uses the input parameter. The action appends the filename to the **File Path** parameter to get the resulting path and add the path to the override.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Name | String | Not applicable | No | Specify the corresponding filename to add to the reputation override.  
File Path | String | Not applicable | Yes | Specify the path where the corresponding IT tool is stored on disk to add the path to the reputation override. Example is as follows: `C\\TMP\\`.  
Include Child Processes | Checkbox | Not selected | No | If selected, include the IT tool child processes on the approved list.  
Description | String | Not applicable | No | Specify a description for the created reputation override.  
Reputation Override List | DDL | Not Specified | Yes | Specify the override list to create.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Create Reputation Override for IT Tool action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the Create Reputation Override for IT Tool action:
    
    
    {
       "id": "067ebeeaf03311eb8bb20bf76c87cd52",
       "created_by": "HZ9PEI2E3L",
       "create_time": "2021-07-29T06:05:50.790Z",
       "override_list": "BLACK_LIST",
       "override_type": "IT_TOOL",
       "description": "An override for an IT_TOOL",
       "source": "APP",
       "source_ref": null,
       "path": "C:\\TMP\\TMP\\TMP\\foo.exe",
       "include_child_processes": false
    }
    

##### Output messages

On a Case Wall, the Create a Reputation Override for IT Tool action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created reputation override for the following entities:  ENTITY_ID_LIST` `No reputation overrides were created.` `Action failed to create reputation override for the following entities:  ENTITY_ID_LIST + API_ERROR ` | Action succeeded.  
`Error executing action because Reputation Override List is not specified.` `Error executing action "Create a Reputation Override for IT Tool". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Delete a Reputation Override

Delete a reputation override using the provided reputation override ID. For more information about the reputation override, see [Reputation Override](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/reputation-override-api).

This action doesn't run on entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Reputation Override ID | String | Not applicable | Yes | Specify the reputation override ID to delete.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Not available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Delete Reputation Override action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Output messages

On a Case Wall, the Delete a Reputation Override action provides the following output messages:

Output message | Message description  
---|---  
`Successfully deleted reputation override OVERRIDE_ID_` `No tasks were created.` `Action failed to delete reputation override OVERRIDE_ID. Reason: ERROR_REASON` `Multiple matches were found in VMware Carbon Black Cloud, taking first match for the following entities:  ENTITY_ID_LIST` | Action succeeded.  
`Error executing action "Delete a Reputation Override". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### List Host Vulnerabilities

Use this action to list vulnerabilities that Carbon Black Cloud has found on the host.

This action runs on the following entities:

  * IP Address
  * Hostname



#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Severity Filter | CSV | Not applicable | No | Specify the comma-separated list of severities for vulnerabilities.If nothing is provided, the action ingests all related vulnerabilities.Possible values: Critical, Important, Moderate, Low.  
Max Vulnerabilities To Return | Integer | 100 | No | Specify the number of vulnerabilities to return for each host. If nothing is provided, the action processes all of the related vulnerabilities.  
  
#### Action outputs

The action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Not available  
Script result | Available  
JSON result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the List Host Vulnerabilities action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result

The following example describes the JSON result output that is received when using the List Host Vulnerabilities action:
    
    
    {
        "statistics": {
            "total": 123,
            "severity": {
                "critical": 1,
                "high": 1,
                "moderate": 1,
                "low": 1
            }
        },
        "details": [
            {
                "os_product_id": "161_0",
                "category": "OS",
                "os_info": {
                    "os_type": "WINDOWS",
                    "os_name": "Microsoft Windows 10 Enterprise",
                    "os_version": "10.0.10240",
                    "os_arch": "64-bit"
                },
                "product_info": {
                    "vendor": null,
                    "product": null,
                    "version": null,
                    "release": null,
                    "arch": null
                },
                "vuln_info": {
                    "cve_id": "CVE-2015-2534",
                    "cve_description": "Hyper-V in Microsoft Windows 8.1, Windows Server 2012 R2, and Windows 10 improperly processes ACL settings, which allows local users to bypass intended network-traffic restrictions via a crafted application, aka \"Hyper-V Security Feature Bypass Vulnerability.\"",
                    "risk_meter_score": 0.9,
                    "severity": "LOW",
                    "fixed_by": "KB3091287",
                    "solution": null,
                    "created_at": "2015-09-09T00:59:00Z",
                    "nvd_link": "http://example",
                    "cvss_access_complexity": null,
                    "cvss_access_vector": null,
                    "cvss_authentication": null,
                    "cvss_availability_impact": null,
                    "cvss_confidentiality_impact": null,
                    "cvss_integrity_impact": null,
                    "easily_exploitable": null,
                    "malware_exploitable": null,
                    "active_internet_breach": null,
                    "cvss_exploit_subscore": null,
                    "cvss_impact_subscore": null,
                    "cvss_vector": null,
                    "cvss_v3_exploit_subscore": null,
                    "cvss_v3_impact_subscore": null,
                    "cvss_v3_vector": null,
                    "cvss_score": null,
                    "cvss_v3_score": null
                },
                "device_count": 1,
                "affected_assets": null
            },
            {
                "os_product_id": "161_0",
                "category": "OS",
                "os_info": {
                    "os_type": "WINDOWS",
                    "os_name": "Microsoft Windows 10 Enterprise",
                    "os_version": "10.0.10240",
                    "os_arch": "64-bit"
                },
                "product_info": {
                    "vendor": null,
                    "product": null,
                    "version": null,
                    "release": null,
                    "arch": null
                },
                "vuln_info": {
                    "cve_id": "CVE-2017-8554",
                    "cve_description": "The kernel in Microsoft Windows 7 SP1, Windows Server 2008 SP2 and R2 SP1, Windows 8.1 and Windows RT 8.1, Windows Server 2012 and R2, Windows 10 Gold, 1511, 1607, and 1703, and Windows Server 2016 allows an authenticated attacker to obtain memory contents via a specially crafted application.",
                    "risk_meter_score": 0.9,
                    "severity": "LOW",
                    "fixed_by": "KB5016639",
                    "solution": null,
                    "created_at": "2017-06-29T13:29:00Z",
                    "nvd_link": "http://example",
                    "cvss_access_complexity": null,
                    "cvss_access_vector": null,
                    "cvss_authentication": null,
                    "cvss_availability_impact": null,
                    "cvss_confidentiality_impact": null,
                    "cvss_integrity_impact": null,
                    "easily_exploitable": null,
                    "malware_exploitable": null,
                    "active_internet_breach": null,
                    "cvss_exploit_subscore": null,
                    "cvss_impact_subscore": null,
                    "cvss_vector": null,
                    "cvss_v3_exploit_subscore": null,
                    "cvss_v3_impact_subscore": null,
                    "cvss_v3_vector": null,
                    "cvss_score": null,
                    "cvss_v3_score": null
                },
                "device_count": 1,
                "affected_assets": null
            }
        ]
    }
    

##### Output messages

On a Case Wall, the List Host Vulnerabilities action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved vulnerabilities for the following hosts: ENTITIES` `No vulnerabilities were found.` `No vulnerabilities were found for the following hosts: ENTITIES` | Action succeeded.  
`Error executing action "List Host Vulnerabilities". Reason: ERROR_REASON` `Error executing action "List Host Vulnerabilities". Reason: Invalid value provided in the "Severity Filter parameter. Possible values: Critical, High, Medium, Low, Unknown.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
## Connectors

The following connectors are available to use in the VMware Carbon Black Cloud integration:

  1. [Alert Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-cloud#vmware-carbon-black-cloud-alerts-connector), deprecated. It uses the same Carbon Black alert data for Google SecOps SOAR alerts and events, thus completely missing the Carbon Black event data. Use the Baseline connector or Tracking connector instead.

  2. [Baseline Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-cloud#vmware-carbon-black-cloud-alerts-and-events-baseline-connector) retrieves both alerts and events from Carbon Black. This connector doesn't monitor if new events are added to Carbon Black alerts.

  3. [Tracking Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-cloud#vmware-carbon-black-cloud-alerts-and-events-tracking-connector) retrieves both alerts and events from Carbon Black and monitors if new events are added to already ingested alerts. If a new event appears in a CB alert, the connector creates a new Google SecOps SOAR alert with events that were added to a Carbon BLack alert.




For instructions on how to configure a connector in Google SecOps SOAR, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### VMware Carbon Black Cloud Alerts Connector — Deprecated

**Deprecated:** This connector is deprecated.**Caution:** Starting on July 31, 2024, you will be unable to use Alerts v6 API in VMware Carbon Black Cloud. For details of the deprecation that VMware Carbon Black introduces to the Alerts v6 API, see [Alerts v6 API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/alerts-api/) in VMware Carbon Black Cloud. We recommend that you update the integration version to the Alerts v7 API.

Get alerts from VMware Carbon Black Cloud as Google SecOps SOAR alerts for analysis in Google SecOps SOAR platform.

#### Connector overview

The connector periodically connects to the VMware Carbon Black Cloud API endpoint and pulls a list of alerts that were generated over a specific time period. If there are new alerts present, then the connector creates Google SecOps SOAR alerts based on the Carbon Black Cloud alerts and saves the connector timestamp as the last successfully ingested alert time. During the next connector execution, the connector queries the Carbon Black API only for alerts that were created after the timestamp.

The connector checks for duplicate alerts (known as alerts that are marked as overflow) and doesn't create Google SecOps SOAR alerts from the duplicate alerts.

**Test Mode:** The connector has a test mode for debugging and troubleshooting purposes. In test mode, the connector does the following:

  * Not update the last run timestamp.
  * Retrieve alerts based on the specified amount of hours to pull alerts for.
  * Return a single alert for ingestion.



**Encrypted Communications:** The connector supports encrypted communications (SSL or TLS).

**Proxy support:** The connector supports connection to the API endpoints using proxy for HTTPS traffic.

**Unicode support:** The connector supports Unicode encoding for the alerts processed.

#### API permissions

The Carbon Black Cloud connector uses the same API credentials as the Carbon Black Cloud integration. For more details about the API configuration for Carbon Black Cloud, see the Prerequistes section.

#### Connector parameters

To configure or edit the connector parameters, you must be included in the Administrators permission group in Google SecOps. For more details about permissions groups for users, see [Working with permissions groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

Use the following parameters to configure the connector:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Environment | DDL | Not applicable | Yes | Select the required environment. For example, "Customer One". If the alert Environment field is empty, the alert is injected to this environment.  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection.  
Product Field Name | String | ProductName | Yes | The name of the field where the product name is stored.  
Event Field Name | String | AlertName | Yes | The name of the field where the event name is stored.  
Event Class ID | String | AlertName | No | The field name used to determine the event name (sub-type).  
Python Process Timeout | String | 180 | Yes | The timeout limit (in seconds) for the Python process that is running the current script.   
Environment Field Name | String | "" | No | The name of the field where the environment name is stored. If the environment field isn't found, the environment is `""`.   
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
API Root | String | Not applicable | Yes | VMware Carbon Black Cloud API Root URL.  
Organization Key | String | N/A | Yes | VMware Carbon Black Cloud organization key.  
API ID | String | N/A | Yes | VMware Carbon Black Cloud API ID (custom API key ID).  
API Secret Key | String | N/A | Yes | VMware Carbon Black Cloud API secret key (custom API secret key).  
Offset time in hours | Integer | 24 | Yes | Number of hours to fetch alerts from.  
Max Alerts Per Cycle | Integer | 10 | Yes | Number of alerts to process in a single connector run.  
Minimum Severity to Fetch | Integer | N/A | No | The minimum severity of Carbon Black Cloud alert to be ingested to Google SecOps SOAR.  
What Alert Field to use for Name field | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Name field. Possible values are type and policy_name.  
What Alert Field to use for Rule Generator | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Rule Generator field. Possible values are type, category, and policy_name.  
Proxy Server Address | IP_OR_HOST | Not applicable | No | Proxy server to use for connection.  
Proxy Server Username | String | Not applicable | No | Proxy server username.  
Proxy Server Password | Password | Not applicable | No | Proxy server password.  
  
#### Connector rules

  * The connector supports using proxies.



### VMware Carbon Black Cloud Alerts and Events Baseline Connector

**Caution:** Starting on July 31, 2024, you will be unable to use Alerts v6 API in VMware Carbon Black Cloud. For details of the deprecation that VMware Carbon Black introduces to the Alerts v6 API, see [Alerts v6 API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/alerts-api/) in VMware Carbon Black Cloud. We recommend that you update the integration version to the Alerts v7 API. In the Alerts v7 API, the connector default mapping returns the `backend_timestamp` value instead of `StartTime` and `backend_update_timestamp` instead of `EndTime`. To keep all your custom mapping changes, don't overwrite the mapping when updating the integration and manually change the `StartTime` and `EndTime` field values.

#### Overview

Use the VMware Carbon Black Cloud Baseline Connector to ingest the Carbon Black Cloud alerts and related events for alerts. After ingesting alerts, Google SecOps tags them as processed and doesn't fetch any updates for them. To fetch alert updates, use the Tracking connector.

#### Customize the Alert Name and Rule Generator fields in Google SecOps

The connector provides an option to customize Google SecOps SOAR **Alert Name** and **Rule Generator** field values using templates. For templates, the connector gets data from the Carbon Black Cloud alert data returned from the API.

The following is an example of the Carbon Black Cloud alert data that is returned from the API. The alert data references the fields available in the alert and can be used for templates:
    
    
    {
                "id": "aa751d91-6623-1a6b-8b4a-************",
                "legacy_alert_id": "aa751d91-6623-1a6b-8b4a-************",
                "org_key": "7DE****",
                "create_time": "2022-03-22T18:12:48.593Z",
                "last_update_time": "2022-03-22T18:13:12.504Z",
                "first_event_time": "2022-03-22T15:16:01.015Z",
                "last_event_time": "2022-03-22T15:45:25.316Z",
                "threat_id": "31c53f050ca571be0af1b29f2d06****",
                "severity": 5,
                "category": "THREAT",
                "device_id": 131****,
                "device_os": "WINDOWS",
                "device_os_version": "Windows 10 x64",
                "device_name": "**********",
                "device_username": "Administrator",
                "policy_name": "default",
                "target_value": "MEDIUM",
                "workflow": {
                    "state": "OPEN",
                    "remediation": null,
                    "last_update_time": "2022-03-22T18:12:48.593Z",
                    "comment": null,
                    "changed_by": "Carbon Black"
                },
                "notes_present": false,
                "tags": null,
                "policy_id": 6525,
                "reason": "The application windowsazureguestagent.exe invoked another application (arp.exe).",
                "reason_code": "T_RUN_ANY",
                "process_name": "waappagent.exe",
                "device_location": "OFFSITE",
                "created_by_event_id": "a44e00b5aa0b11ec9973f78f4c******",
                "threat_indicators": [
                    {
                        "process_name": "waappagent.exe",
                        "sha256": "a5664303e573266e0f9e5fb443609a7eb272f64680c38d78bce110384b37faca",
                        "ttps": [
                            "ATTEMPTED_CLIENT",
                            "COMPANY_BLACKLIST",
                            "MITRE_T1082_SYS_INF_DISCOVERY",
                            "MITRE_T1106_NATIVE_API",
                            "MITRE_T1571_NON_STD_PORT",
                            "NON_STANDARD_PORT",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    },
                    {
                        "process_name": "services.exe",
                        "sha256": "dfbea9e8c316d9bc118b454b0c722cd674c30d0a256340200e2c3a7480cba674",
                        "ttps": [
                            "RUN_BLACKLIST_APP"
                        ]
                    },
                    {
                        "process_name": "svchost.exe",
                        "sha256": "f3feb95e7bcfb0766a694d93fca29eda7e2ca977c2395b4be75242814eb6d881",
                        "ttps": [
                            "COMPANY_BLACKLIST",
                            "MODIFY_MEMORY_PROTECTION",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    },
                    {
                        "process_name": "windowsazureguestagent.exe",
                        "sha256": "9a9f62a1c153bdb7bbe8301c6d4f1abfad6035cfe7b6c1366e3e0925de6387c3",
                        "ttps": [
                            "ATTEMPTED_CLIENT",
                            "COMPANY_BLACKLIST",
                            "MITRE_T1082_SYS_INF_DISCOVERY",
                            "MITRE_T1106_NATIVE_API",
                            "MITRE_T1571_NON_STD_PORT",
                            "NON_STANDARD_PORT",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    }
                ],
                "threat_activity_dlp": "NOT_ATTEMPTED",
                "threat_activity_phish": "NOT_ATTEMPTED",
                "threat_activity_c2": "NOT_ATTEMPTED",
                "threat_cause_actor_sha256": "9a9f62a1c153bdb7bbe8301c6d4f1abfad6035cfe7b6c1366e3e0925de6387c3",
                "threat_cause_actor_name": "windowsazureguestagent.exe",
                "threat_cause_actor_process_pid": "3504-132914439190103761-0",
                "threat_cause_process_guid": "7DESJ9GN-004fd50b-00000db0-00000000-1d834fa6d7246d1",
                "threat_cause_parent_guid": null,
                "threat_cause_reputation": "TRUSTED_WHITE_LIST",
                "threat_cause_threat_category": null,
                "threat_cause_vector": "UNKNOWN",
                "threat_cause_cause_event_id": "a74fa7a3aa0b11ec9b401dea771569d9",
                "blocked_threat_category": "UNKNOWN",
                "not_blocked_threat_category": "NON_MALWARE",
                "kill_chain_status": [
                    "INSTALL_RUN"
                ],
                "sensor_action": null,
                "run_state": "RAN",
                "policy_applied": "NOT_APPLIED",
                "type": "CB_ANALYTICS",
                "alert_classification": null
            }
    

#### Connector parameters

To configure or edit the connector parameters, you must be included in the Administrators permission group in Google SecOps. For more details about permissions groups for users, see [Working with permissions groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | ProductName | Yes | The name of the field where the product name is stored.  
Event Field Name | String | AlertName | Yes | The name of the field where the event name is stored.  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored. If the environment field isn't found, the environment is `""`.  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
API Root | String | `https://defense.conferdeploy.net` | Yes | VMware Carbon Black Cloud API root URL.  
Organization Key | String | Not applicable | Yes | VMware Carbon Black Cloud organization key. For example, 7DDDD9DD.  
API ID | String | Not applicable | Yes | VMware Carbon Black Cloud API ID (custom API key ID).  
API Secret Key | String | Not applicable | Yes | VMware Carbon Black Cloud API secret key (custom API secret key).  
Offset time in hours | Integer | 24 | Yes | Number of hours to fetch alerts from.  
Max Alerts Per Cycle | Integer | 10 | Yes | Number of alerts to process in a single connector run.  
Minimum Severity to Fetch | Integer | N/A | No | The minimum severity of Carbon Black Cloud alert to ingest to Google SecOps SOAR. For example, 4 or 7.  
What Alert Field to use for Name field | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Name field. Possible values are type and policy_name.  
What Alert Field to use for Rule Generator | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Rule Generator field. Possible values are type, category, and policy_name.  
Alert Reputation to Ingest | String | Not applicable | No | The Carbon Black Cloud reputation of the alert to ingest. This parameter accepts multiple values as a comma-separated string.  
Event Limit to Ingest per Alert | Integer | 25 | Yes | The number of events to ingest into each Carbon Black Cloud alert.   
Proxy Server Address | IP_OR_HOST | Not applicable | No | Proxy server to use for connection.  
Proxy Server Username | String | Not applicable | No | Proxy server username.  
Proxy Server Password | Password | Not applicable | No | Proxy server password.  
Alert Name Template | String | Not applicable | No | If specified, the connector uses this value from the Carbon Black Cloud API response alert data to populate the Alert Name field. You can provide placeholders in the following format: [name of the field]. Example: Alert - [reason]. The maximum length for the field is 256 characters. If nothing is provided or you provide an invalid template, the connector uses the default alert name.  
Rule Generator Template | String | N/A | No | If specified, the connector uses this value from the Carbon Black Cloud API response alert data to populate the Rule Generator field. You can provide placeholders in the following format: [name of the field]. Example: Alert - [reason]. The maximum length for the field is 256 characters. If nothing is provided or the you provide an invalid template, the connector uses the default rule generator value.  
  
#### Connector rules

  * The connector supports using proxies.



### VMware Carbon Black Cloud Alerts and Events Tracking Connector

**Caution:** Starting on July 31, 2024, you will be unable to use Alerts v6 API in VMware Carbon Black Cloud. For details of the deprecation that VMware Carbon Black introduces to the Alerts v6 API, see [Alerts v6 API](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/alerts-api/) in VMware Carbon Black Cloud. We recommend that you update the integration version to upgrade to the Alerts v7 API. In the Alerts v7 API, the connector default mapping returns the `backend_timestamp` value instead of `StartTime` and `backend_update_timestamp` instead of `EndTime`. To keep all your custom mapping changes, don't overwrite the mapping when updating the integration and manually change the `StartTime` and `EndTime` field values.

#### Overview

Use the VMware Carbon Black Cloud Tracking connector to fetch Carbon Black Cloud alerts and related events. If the connector detects new events for already processed Carbon Black Cloud alerts, it creates an additional Google SecOps SOAR alert for each new detected event.

#### Customize the Alert Name and Rule Generator fields in Google SecOps

The connector provides an option to customize Google SecOps SOAR **Alert Name** and **Rule Generator** field values through templates. For templates, the connector gets data from the Carbon Black Cloud alert data returned by the API.

The following is an example of the Carbon Black Cloud alert data that is returned from the API. The alert data references the fields available in the alert and can be used for templates:
    
    
    {
                "id": "aa751d91-6623-1a6b-8b4a-************",
                "legacy_alert_id": "aa751d91-6623-1a6b-8b4a-************",
                "org_key": "7DE****",
                "create_time": "2022-03-22T18:12:48.593Z",
                "last_update_time": "2022-03-22T18:13:12.504Z",
                "first_event_time": "2022-03-22T15:16:01.015Z",
                "last_event_time": "2022-03-22T15:45:25.316Z",
                "threat_id": "31c53f050ca571be0af1b29f2d06****",
                "severity": 5,
                "category": "THREAT",
                "device_id": 131****,
                "device_os": "WINDOWS",
                "device_os_version": "Windows 10 x64",
                "device_name": "**********",
                "device_username": "Administrator",
                "policy_name": "default",
                "target_value": "MEDIUM",
                "workflow": {
                    "state": "OPEN",
                    "remediation": null,
                    "last_update_time": "2022-03-22T18:12:48.593Z",
                    "comment": null,
                    "changed_by": "Carbon Black"
                },
                "notes_present": false,
                "tags": null,
                "policy_id": 6525,
                "reason": "The application windowsazureguestagent.exe invoked another application (arp.exe).",
                "reason_code": "T_RUN_ANY",
                "process_name": "waappagent.exe",
                "device_location": "OFFSITE",
                "created_by_event_id": "a44e00b5aa0b11ec9973f78f4c******",
                "threat_indicators": [
                    {
                        "process_name": "waappagent.exe",
                        "sha256": "a5664303e573266e0f9e5fb443609a7eb272f64680c38d78bce110384b37faca",
                        "ttps": [
                            "ATTEMPTED_CLIENT",
                            "COMPANY_BLACKLIST",
                            "MITRE_T1082_SYS_INF_DISCOVERY",
                            "MITRE_T1106_NATIVE_API",
                            "MITRE_T1571_NON_STD_PORT",
                            "NON_STANDARD_PORT",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    },
                    {
                        "process_name": "services.exe",
                        "sha256": "dfbea9e8c316d9bc118b454b0c722cd674c30d0a256340200e2c3a7480cba674",
                        "ttps": [
                            "RUN_BLACKLIST_APP"
                        ]
                    },
                    {
                        "process_name": "svchost.exe",
                        "sha256": "f3feb95e7bcfb0766a694d93fca29eda7e2ca977c2395b4be75242814eb6d881",
                        "ttps": [
                            "COMPANY_BLACKLIST",
                            "MODIFY_MEMORY_PROTECTION",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    },
                    {
                        "process_name": "windowsazureguestagent.exe",
                        "sha256": "9a9f62a1c153bdb7bbe8301c6d4f1abfad6035cfe7b6c1366e3e0925de6387c3",
                        "ttps": [
                            "ATTEMPTED_CLIENT",
                            "COMPANY_BLACKLIST",
                            "MITRE_T1082_SYS_INF_DISCOVERY",
                            "MITRE_T1106_NATIVE_API",
                            "MITRE_T1571_NON_STD_PORT",
                            "NON_STANDARD_PORT",
                            "RUN_ANOTHER_APP",
                            "RUN_SYSTEM_APP"
                        ]
                    }
                ],
                "threat_activity_dlp": "NOT_ATTEMPTED",
                "threat_activity_phish": "NOT_ATTEMPTED",
                "threat_activity_c2": "NOT_ATTEMPTED",
                "threat_cause_actor_sha256": "9a9f62a1c153bdb7bbe8301c6d4f1abfad6035cfe7b6c1366e3e0925de6387c3",
                "threat_cause_actor_name": "windowsazureguestagent.exe",
                "threat_cause_actor_process_pid": "3504-132914439190103761-0",
                "threat_cause_process_guid": "7DESJ9GN-004fd50b-00000db0-00000000-1d834fa6d7246d1",
                "threat_cause_parent_guid": null,
                "threat_cause_reputation": "TRUSTED_WHITE_LIST",
                "threat_cause_threat_category": null,
                "threat_cause_vector": "UNKNOWN",
                "threat_cause_cause_event_id": "a74fa7a3aa0b11ec9b401dea771569d9",
                "blocked_threat_category": "UNKNOWN",
                "not_blocked_threat_category": "NON_MALWARE",
                "kill_chain_status": [
                    "INSTALL_RUN"
                ],
                "sensor_action": null,
                "run_state": "RAN",
                "policy_applied": "NOT_APPLIED",
                "type": "CB_ANALYTICS",
                "alert_classification": null
            }
    

#### Connector parameters

To configure or edit the connector parameters, you must be included in the Administrators permission group in Google SecOps. For more details about permissions groups for users, see [Working with permissions groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

Use the following parameters to configure the connector:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | ProductName | Yes | The name of the field where the product name is stored.  
Event Field Name | String | AlertName | Yes | The name of the field where the event name is stored.  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored. If the environment field isn't found, the environment is `""`.  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
API Root | String | `https://defense.conferdeploy.net` | Yes | VMware Carbon Black Cloud API root URL.  
Organization Key | String | Not applicable | Yes | VMware Carbon Black Cloud organization key. For example, 7DDDD9DD.  
API ID | String | Not applicable | Yes | VMware Carbon Black Cloud API ID (custom API key ID).  
API Secret Key | String | N/A | Yes | VMware Carbon Black Cloud API secret key (custom API secret key).  
Offset time in hours | Integer | 24 | Yes | The number of hours to fetch alerts from.  
Max Alerts Per Cycle | Integer | 10 | Yes | The number of alerts to process in a single connector run.  
Minimum Severity to Fetch | Integer | Not applicable | No | The minimum severity of the Carbon Black Cloud alert to ingest to Google SecOps SOAR. For example, 4 or 7.  
What Alert Field to use for Name field | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Name field. Possible values are: type and policy_name.  
What Alert Field to use for Rule Generator | String | type | Yes | The Carbon Black Cloud alert field to use for the Google SecOps SOAR Alert Rule Generator field. Possible values are type, category, and policy_name.  
Alert Reputation to Ingest | String | Not applicable | No | The Carbon Black Cloud alert reputation alert to ingest. This parameter accepts multiple values as a comma-separated string.  
Events Padding Period (hours) | Integer | 24 | Yes | The number of hours to fetch alert events from.  
Event Limit to Ingest per Alert | Integer | 25 | Yes | The number of events to ingested in a single Carbon Black Cloud alert for each connector iteration.  
Proxy Server Address | IP_OR_HOST | Not applicable | No | Proxy server to use for connection.  
Proxy Server Username | String | Not applicable | No | Proxy server username.  
Proxy Server Password | Password | Not applicable | No | Proxy server password.  
Alert Name Template | String | Not applicable | No | If specified, the connector uses this value from the Carbon Black Cloud API response alert data to populate the Alert Name field. You can provide placeholders in the following format: [name of the field]. Example: Alert - [reason]. The maximum length for the field is 256 characters. If nothing is provided or you provide an invalid template, the connector uses the default alert name value.  
Rule Generator Template | String | Not applicable | No | If specified, the connector uses this value from the Carbon Black Cloud API response alert data to populate the Rule Generator field. You can provide placeholders in the following format: [name of the field]. Example: Rule - [reason]. The maximum length for the field is 256 characters. If nothing is provided or you provide an invalid template, the connector uses the default rule generator value.  
Total Limit of Events per Alert | Integer | 100 | No | The total number of events that the connector retrieves for each Carbon Black Cloud alert. If this limit is reached, the connector retrieves no new events for an alert. To not limit the total number of events for each alert, leave this parameter value empty.  
  
#### Connector rules

  * The connector supports using proxies.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
