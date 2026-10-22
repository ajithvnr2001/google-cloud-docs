---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/automox/
title: Integrate Automox with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:34.108212+00:00
---

# Integrate Automox with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/automox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Automox with Google SecOps

This document describes how to integrate Automox with Google Security Operations (Google SecOps).

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://#123;#123;api_root#125;#125; | Yes | API root of the Automox instance.  
API Key | Password | N/A | No | API key of the Automox instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Automox is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate API key

For more information on how to generate an API key, see the [Find your API key in the console](https://developer.automox.com/developer-portal/newbie-api-guide/#step-2-find-your-api-key-in-the-console) step available within the Newbie's Guide to Getting Started with Automox API document.

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Entities

Enrich entities using information from Automox.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Return Patches | Checkbox | Checked | No | If enabled, the action returns a list of patches that need to be updated on the machine. **Note:** The action does not return patches that were installed or those that were ignored.  
Max Patches To Return | Integer | 50 | No | Specify the number of patches to return. If nothing is provided, the action returns 50 patches.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": 2263017,
        "agent_version": "1.41.125",
        "commands": [],
        "compatibility_checks": {
            "missing_wmi_integrity_check": false,
            "missing_powershell": false,
            "low_diskspace": false
        },
        "compliant": true,
        "connected": false,
        "create_time": "2022-10-24T09:14:12+0000",
        "custom_name": "",
        "deleted": false,
        "detail": {
            "IPS": [
                "192.0.2.176",
                "2001:db8:1:1:1:1:1:1"
            ],
            "UPDATE_SOURCE_CHECK": {
                "CONNECTED": "True",
                "ERROR": "Succeeded"
            },
            "MDM_SERVER": null,
            "FQDNS": [
                "DESKTOP-65M05SE.WORKGROUP"
            ],
            "RAM": "8589934592",
            "SECURE_TOKEN_ACCOUNT": null,
            "LAST_USER_LOGON": {
                "SRC": "DESKTOP-65M05SE",
                "USER": "DESKTOP-65M05SE\\Admin",
                "TIME": "10/24/2022 2:59:45 AM"
            },
            "VOLUME": [
                {
                    "IS_SYSTEM_DISK": "True",
                    "VOLUME": "C:",
                    "FSTYPE": "NTFS",
                    "LABEL": "Local Disk",
                    "AVAIL": "63766056960",
                    "FREE": "39201988608"
                }
            ],
            "DISTINGUISHED_NAME": "",
            "MODEL": "VMware7,1",
            "CPU": "Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz",
            "MDM_PROFILE_INSTALLED": null,
            "VENDOR": "VMware, Inc.",
            "AUTO_UPDATE_OPTIONS": {
                "OPTIONS": "off",
                "ENABLED": "1"
            },
            "SERVICETAG": "No Asset Tag",
            "PS_VERSION": "5",
            "WSUS_CONFIG": {
                "WSUS_REACHABLE": "1",
                "WSUS_MANAGED": "0",
                "WSUS_SERVER": ""
            },
            "SERIAL": "VMware",
            "NICS": [
                {
                    "VENDOR": "Intel(R) 82574L Gigabit Network Connection",
                    "DEVICE": "Ethernet0",
                    "TYPE": "enet",
                    "MAC": "01:23:45:AB:CD:EF",
                    "IPS": [
                        "172.30.201.176",
                        "2001:db8:1:1:1:1:1:1"
                    ],
                    "CONNECTED": true
                },
                {
                    "IPS": [],
                    "CONNECTED": false,
                    "VENDOR": "WAN Miniport (IP)",
                    "DEVICE": "",
                    "TYPE": "enet",
                    "MAC": "01:23:45:AB:CD:EF"
                },
                {
                    "VENDOR": "WAN Miniport (IPv6)",
                    "DEVICE": "",
                    "TYPE": "enet",
                    "MAC": "01:23:45:AB:CD:EF",
                    "IPS": [],
                    "CONNECTED": false
                },
                {
                    "CONNECTED": false,
                    "VENDOR": "WAN Miniport (Network Monitor)",
                    "DEVICE": "",
                    "TYPE": "enet",
                    "MAC": "01:23:45:AB:CD:EF",
                    "IPS": []
                }
            ],
            "WMI_INTEGRITY_CHECK": "True",
            "VERSION": "440BX Desktop Reference Platform",
            "DISKS": [
                {
                    "TYPE": "VMware Virtual disk SCSI Disk Device",
                    "SIZE": "64420392960"
                }
            ]
        },
        "display_name": "DESKTOP-65M05SE",
        "exception": false,
        "instance_id": "",
        "ip_addrs": [
            "192.0.2.139"
        ],
        "ip_addrs_private": [
            "192.0.2.176",
            "2001:db8:1:1:1:1:1:1"
        ],
        "is_compatible": true,
        "is_delayed_by_notification": false,
        "is_delayed_by_user": false,
        "last_disconnect_time": "2022-10-25T09:19:29+0000",
        "last_logged_in_user": "DESKTOP-65M05SE\\Admin",
        "last_process_time": "2022-10-25T08:19:24+0000",
        "last_refresh_time": "2022-10-25T08:23:48+0000",
        "last_scan_failed": false,
        "last_update_time": "2022-10-25T08:22:14+0000",
        "mdm": null,
        "name": "DESKTOP-65M05SE",
        "needs_attention": false,
        "needs_reboot": false,
        "next_patch_time": null,
        "notification_count": 0,
        "organization_id": 104513,
        "organizational_unit": "",
        "os_family": "Windows",
        "os_name": "10 Enterprise Evaluation",
        "os_version": "10.0.19043",
        "os_version_id": 4876,
        "patch_deferral_count": 0,
        "patches": 1,
        "pending": false,
        "pending_patches": 0,
        "policy_status": [
            {
                "id": 316123693,
                "organization_id": 104513,
                "policy_id": 245687,
                "server_id": 2263017,
                "policy_name": "Apply All Patches",
                "policy_type_name": "patch",
                "status": 1,
                "result": "{}",
                "create_time": "2022-10-25T08:23:48+0000",
                "will_reboot": false,
                "pending_count": 0,
                "next_remediation": null
            }
        ],
        "reboot_deferral_count": 0,
        "reboot_is_delayed_by_notification": false,
        "reboot_is_delayed_by_user": false,
        "reboot_notification_count": 0,
        "refresh_interval": 1440,
        "serial_number": "VMware",
        "server_group_id": 145150,
        "server_policies": [],
        "status": {
            "device_status": "not-ready",
            "agent_status": "disconnected",
            "policy_status": "compliant",
            "policy_statuses": [
                {
                    "id": 245687,
                    "compliant": true
                },
                {
                    "id": 245688,
                    "compliant": true
                }
            ]
        },
        "tags": [
            "Recently Added"
        ],
        "timezone": "UTC-0700",
        "total_count": 1,
        "uptime": "1872",
        "uuid": "UUID",
        "list_of_patches": [
            {
                "id": 2077952013,
                "server_id": 2263017,
                "package_id": 227229243,
                "software_id": 167943,
                "installed": true,
                "ignored": false,
                "group_ignored": false,
                "deferred_until": null,
                "group_deferred_until": null,
                "name": "example",
                "display_name": "MSXML 6.0 RTM Security Update  (925673)",
                "version": "103",
                "repo": "WindowsUpdate",
                "cves": [],
                "cve_score": "9.0",
                "agent_severity": "9.0",
                "severity": "critical",
                "package_version_id": 233355423,
                "os_name": "10 Enterprise Evaluation",
                "os_version": "10.0.19043",
                "os_version_id": 4876,
                "create_time": "2021-06-28T15:45:57+0000",
                "requires_reboot": true,
                "patch_classification_category_id": 8,
                "patch_scope": "important",
                "is_uninstallable": false,
                "secondary_id": null,
                "is_managed": true,
                "impact": 0,
                "organization_id": 104513
            }
        ]
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
id | When available in JSON  
agent_version | When available in JSON  
compliant | When available in JSON  
connected | When available in JSON  
create_time | When available in JSON  
custom_name | When available in JSON  
ip_addrs_private | When available in JSON  
last_disconnect_time | When available in JSON  
last_logged_in_user | When available in JSON  
last_update_time | When available in JSON  
os | When available in JSON  
pending_patches | When available in JSON  
tags | When available in JSON  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Automox: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Automox: {entity.identifier}" _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Title:** {entity.identifier} **Columns:**

  * Key
  * Value

| Entity  
  
### Execute Device Command

Execute a command on the endpoint in Automox.

**Note:** This action is running asynchronously. If necessary, adjust the script timeout value in the IDE for the action.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Command | DDL | Scan Device Possible Values:

  * Scan Device
  * Install Specific Patches
  * Install All Available Patches
  * Restart Device

| No | Specify a command that needs to be executed on the device. **Note:** If "Install Specific Patches" is selected, the "Patch Names" parameter is mandatory.  
Patch Names | CSV | N/A | No | Specify a comma-separated list of patches that need to be installed.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": 8527028217,
        "server_id": 2263017,
        "command_id": 164850699,
        "organization_id": 104513,
        "args": "ASD",
        "reboot": 0,
        "exec_time": "2022-10-25T08:02:43+0000",
        "response": [
            "0",
            "Installing MS updates: ASD\\r\\nCouldn't find update for ASD, skipping.\\r\\nNothing left to do",
            null
        ],
        "response_time": "2022-10-25T08:22:14+0000",
        "policy_id": null,
        "agent_command_type": 0,
        "command_type_name": "InstallUpdate"
    }
    {
        "reason": "Device is offline. Please check the connectivity."
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** _If the device is found and it's connected (is_success=true):_ "Successfully executed command "{Command}" on the following entities in Automox: {entity.identifier}. Please check the JSON result to be sure that the command executed correctly." _If the device is not found or it's connected for one entity (is_success=true):_ "Action wasn't able to execute command "{Command}" on the following entities in Automox: {entity.identifier}. Please check the spelling and connectivity." _If the device is not found or it's connected for all entities (is_success=false):_ "No commands were executed on the provided entities. Please check the spelling and connectivity." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Execute Device Command". Reason: {0}''.format(error.Stacktrace) | General  
  
### Execute Policy

Execute a policy in Automox.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Remediation Scope | DDL | All DevicesPossible values:

  * Only Entities
  * All Devices

| No | Specify the remediation scope for the action.If "Only Entities" is selected, the action executes policies only on the valid entities in the scope.If "All Devices" is selected, the action executes the policy on all devices in the organization.  
Policy Name | String | N/A | No | Specify the name of the policy that needs to be executed.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "status": "done/failure if entity not found"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** _If remediated the server and successful for one entity (is_success=true):_ "Successfully executed policy {Policy} on the following entities in Automox: {entity.identifier}."_If remediated the server and one server is not found (is_success=true):_ "Action wasn't able to execute policy {Policy} on the following entities in Automox: {entity.identifier}."_If remediated the server and all servers are not found (is_success=false):_ "No entities were found. Policy {Policy} wasn't executed."_If remediate all servers (is_success=true):_ "Successfully executed policy {Policy} in Automox."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Execute Policy". Reason: {0}''.format(error.Stacktrace)_If the policy is not found:_ "Error executing action "Execute Policy". Reason: policy "{policy name}" wasn't found in Automox. Please check the spelling.'' | General  
  
### List Policies

List available policies in Automox.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select One Possible values:

  * Name
  * ID
  * Policy Type Name
  * Status

| No | Specify the key that needs to be used to filter policy.  
Filter Logic | DDL | Not Specified Possible values:

  * Not Specified
  * Equal
  * Contains

| No | Specify the filter logic that should be applied.Filtering logic works based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify the value that should be used in the filter. If "Equal" is selected, the action tries to find the exact match among results and if "Contains" is selected, the action tries to find results that contain that substring. If nothing is provided in this parameter, the filter is not applied. Filtering logic works based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return. If nothing is provided, the action returns 50 records.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
        {
            "id": 245687,
            "name": "Apply All Patches",
            "policy_type_name": "patch",
            "organization_id": 104513,
            "configuration": {
                "auto_patch": false,
                "patch_rule": "all",
                "auto_reboot": false,
                "notify_user": false,
                "include_optional": true,
                "notify_reboot_user": true,
                "missed_patch_window": true,
                "custom_notification_max_delays": 3,
                "custom_notification_deferment_periods": [
                    1,
                    2,
                    4
                ]
            },
            "schedule_days": 254,
            "schedule_weeks_of_month": 62,
            "schedule_months": 8190,
            "schedule_time": "17:00",
            "notes": "",
            "create_time": "2022-10-24T08:44:37+0000",
            "server_groups": [
                145150
            ],
            "server_count": 1,
            "status": "inactive"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success=true):_ "Successfully found policies for the provided criteria in Automox". _If data is not available (is_success=false):_ "No policies were found for the provided criteria in Automox." _If the "Filter Value" parameter is empty (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value." _If the "Filter Logic" parameter is set to "Not Specified" (is_success=true):_ "The filter was not applied, because parameter "Filter Logic" is not specified." **The action should fail and stop a playbook execution:** _If the "Filter Key" parameter is set "Select One" and the "Filter Logic" is set to "Equal" or "Contains":_ "Error executing action "{action name}". Reason: you need to select a field from the "Filter Key" parameter." _If an invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "{action name}". Reason: "Invalid value was provided for "Max Records to Return": . Positive number should be provided"." _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "List Policies". Reason: {0}''.format(error.Stacktrace) | General  
| Case Wall Table | **Table name:** Available Policies **Table columns:**

  * Name - name
  * Type - policy_type_name
  * ID - id
  * Status - status
  * Notes - notes

| General  
  
### Ping

Test the connectivity to Automox.

#### Parameters

N/A

#### Run on

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
| Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Automox server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Automox server! Error is {0}".format(exception.stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
