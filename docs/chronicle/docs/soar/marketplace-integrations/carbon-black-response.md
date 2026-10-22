---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-response/
title: Carbon Black Response \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:24.632590+00:00
---

# Carbon Black Response  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Carbon Black Response

**Important:** Carbon Black Response was acquired by VMware and became VMware Carbon Black EDR (EDR).

This document describes how to integrate VMware Carbon Black EDR with Google Security Operations.

## Configure VMware Carbon Black EDR (EDR) to work with Google Security Operations

### API Key

To obtain an API key, please complete the following steps:

  1. Log into the console
  2. Click the **username** in the upper right
  3. Navigate to the Profile info.
  4. Click the **API Token** button on the left side to reveal the API token.

In case there is no API token displayed, click the **Reset** button to create a new one.


**Note:** Carbon Black Configuration is used for both CB Defense and CB Response. For detailed information, please refer to [CB Response Rest API Authentication page](https://developer.carbonblack.com/reference/enterprise-response/authentication/).

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Carbon Black Response integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://x.x.x.x | Yes | The address of the VMware Carbon Black EDR (EDR) instance.  
Api Key | String | N/A | Yes | API key generated in the VMware Carbon Black EDR (EDR) console.  
Version | String | 6.3 | Yes | The version of the product. Make sure you provide shorter form of the version. For example, instead of providing 7.4.0, provide 7.4.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Binary Free Query

#### Description

List binaries by free query.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Example: md5:* AND original_filename:{file-name}  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "host_count": x,
            "digsig_result":"Signed",
            "Observed_filename": ["c:\\\\windows\\\\system32\\\\xxxxxx.exe"],
            "product_version": "10.0.17134.1",
            "digsig_issuer": "Microsoft Windows Production PCA 2011",
            "legal_copyright": "\\\\u00a9 Microsoft Corporation. All rights reserved.",
            "digsig_sign_time": "2018-04-11T19:19:00Z",
            "orig_mod_len": 20888,
            "is_executable_image": true,
            "is_64bit": true,
            "digsig_subject": "Microsoft Windows",
            "digsig_publisher": "Microsoft Corporation",
            "group": ["Default Group"],
            "file_version": "10.0.17134.1 (WinBuild.160101.0800)",
            "company_name": "Microsoft Corporation",
            "internal_name": "xxxxxxx.exe",
            "product_name": "Microsoft\\\\u00ae Windows\\\\u00ae Operating System",
            "digsig_result_code": "0",
            "timestamp": "2018-12-30T03:55:55.376Z",
            "copied_mod_len": 20888,
            "server_added_timestamp": "2018-12-30T03:55:55.376Z",
            "digsig_prog_name": "Microsoft Windows",
            "md5": "2528137C6745C4EADD87817A1909677E",
            "endpoint": ["DESKTOP-CEIFS6E|15",
                         "DESKTOP-CEIFS6E|16",
                         "LP-AVITAL|17",
                         "LAPTOP-66I4I93K|18"],
            "watchlists": [
                {
                    "wid": "3",
                    "value": "2018-12-30T04:00:03.635Z"
                }],
            "signed": "Signed",
            "original_filename": "xxxxxxx.exe",
            "cb_version": 520,
            "os_type": "Windows",
            "file_desc": "COM Surrogate",
            "last_seen": "2019-02-21T15:27:33.231Z"
        }
    ]
    

### Block Hash

#### Description

Block a hash.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Create Watchlist

#### Description

Create a watchlist for processes (type = events) or for binaries (type = modules).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Watchlist Name | String | N/A | Yes | Name of this watchlist.  
Query | String | N/A | Yes | The raw Carbon Black query that this watchlist matches.  
Watchlist Type | String | N/A | Yes | The type of watchlist. e.g. modules.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Download Binary

#### Description

Download a binary.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAA4fug4AtAnNIb",
            "Entity": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
    ]
    

### Enrich Binary

#### Description

Enrich hash with binary information from CB Response.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "host_count": x,
                "digsig_result": "Unsigned",
                "observed_filename":["c:\\\\\\\\TEST_source\\\\\\\\main\\\\\\\\client\\\\\\\\wpf\\\\\\\\TEST.client\\\\\\\\bin\\\\\\\\release\\\\\\\\TEST.client.exe"],
                "product_version": "x.x.x.x",
                "legal_copyright": "TEST",
                "orig_mod_len": 4108800,
                "is_executable_image": "True",
                "is_64bit": "False",
                "group": ["Default Group"],
                "file_version": "x.x.x.x",
                "comments": "Flavor=Release",
                "company_name": "TEST",
                "internal_name": "TEST.xxxxxx.exe",
                "icon": "iVBORw0KGgoAAAANSUhEUg",
                "product_name": "(unknown)",
                "digsig_result_code": "xxxxxxx",
                "timestamp": "2016-12-11T18:54:03.352Z",
                "copied_mod_len": 4108800,
                "server_added_timestamp": "2016-12-11T18:54:03.352Z",
                "md5": "82A2C91219F140BB2A4FE34A7390B6C7",
                "endpoint": ["WS-ALON|4"],
                "Watchlists": [
                    {
                        "wid": "3", "value": "2016-12-11T19:00:03.232Z"
                    }],
                "signed": "Unsigned",
                "original_filename": "TEST.xxxxx.exe",
                "cb_version": 520,
                "os_type": "Windows",
                "file_desc": " ",
                "last_seen": "2016-12-11T19:00:04.178Z"
            },
            "Entity": "82A2C91219F140BB2A4FE34A7123B6C7"
        }
    ]
    

### Enrich Process

#### Description

Enrich process entity with data from CB Response.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * Process
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                    "modload_count": 28,
                    "sensor_id": 14,
                    "filtering_known_dlls": "False",
                    "process_md5": "d752c96401e2540a123c599154fc6fa9",
                    "parent_unique_id": "0000000e-0000-13d4-01d4-a04566d108ba-00000001",
                    "emet_count": 0,
                    "cmdline": "\\\\\\\\??\\\\\\\\C:\\\\\\\\Windows\\\\\\\\system32\\\\\\\\conhost.exe 0xffffffff -ForceV1",
                    "last_update": "2018-12-30T13:41:43.904Z",
                    "id": "x-x-x-x-x",
                    "parent_name": "python.exe",
                    "parent_md5": "000000000000000000000000000000",
                    "group": "Default Group",
                    "hostname": "TEST",
                    "filemod_count": 0,
                    "start": "2018-12-30T13:41:43.885Z",
                    "emet_config": "",
                    "netconn_count": 0,
                    "interface_ip": 167772456,
                    "process_pid": xxxx,
                    "username": "TEST\\\\\\\\xxxxxx",
                    "terminated": "True",
                    "process_name": "xxxxx.exe",
                    "comms_ip": xxxxxxx,
                    "path": "c:\\\\\\\\windows\\\\\\\\system32\\\\\\\\xxxxxx.exe",
                    "regmod_count": 0,
                    "parent_pid": 5076,
                    "crossproc_count": 1,
                    "current_segment": 0,
                    "segment_id": 1,
                    "host_type": "server",
                    "processblock_count": 0,
                    "os_type": "windows",
                    "childproc_count": 0,
                    "unique_id": "0000000e-0000-1310-01d4-a04566d29849-00000001"
                }],
            "Entity": "process.exe"
        }
    ]
    

### Get FileMod Data for Process

#### Description

Get filemod data for a process by its ID.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Process ID | String | N/A | Yes | Process unique ID.  
Segment ID | String | N/A | Yes | e.g. 1.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Process":
        {
            "process_md5": "517110bd83835338c037269e603db55d",
            "sensor_id": x,
            "group": "Default Group",
            "segment_id": x,
            "process_name": "xxxxxxx.exe",
            "start": "2013-09-19T22:07:07Z",
            "regmod_complete": [
                "2|2013-09-19 22:07:07.000000|\\\\\\\\registry\\\\\\\\user\\\\\\\\s-1-5-19\\\\\\\\software\\\\\\\\microsoft\\\\\\\\sqmclient\\\\\\\\reliability\\\\\\\\adaptivesqm\\\\\\\\manifestinfo\\\\\\\\version",
                "2|2013-09-19 22:09:07.000000|\\\\\\\\registry\\\\\\\\machine\\\\\\\\software\\\\\\\\microsoft\\\\\\\\reliability analysis\\\\\\\\rac\\\\\\\\wmilasttime"],
            "cmdline": "xxxxxxx.exe $(arg0)",
            "Filemod_complete": [
                "2|2013-09-19 22:07:07.000000|c:\\\\\\\\programdata\\\\\\\\microsoft\\\\\\\\rac\\\\\\\\statedata\\\\\\\\racmetadata.dat|",
                "2|2013-09-19 22:07:07.000000|c:\\\\\\\\programdata\\\\\\\\microsoft\\\\\\\\rac\\\\\\\\temp\\\\\\\\sql4475.tmp|"],
            "parent_id": "",
            "modload_complete": [
                "2013-09-19 22:07:07.000000||c:\\\\\\\\windows\\\\\\\\system32\\\\\\\\xxxxxx.exe",
                "2013-09-19 22:07:07.000000||c:\\\\\\\\windows\\\\\\\\system32\\\\\\\\ntdll.dll"],
            "id": "xxxxxxxxxxxxxxxx",
            "path": "c:\\\\\\\\xxxxxxx\\\\\\\\xxxxxx\\\\\\\\xxxxxxx.exe",
            "os_type": "windows",
            "last_update": "2013-09-19T22:09:07Z",
            "hostname": "xxxx-xxxxxxxxxxx"
        },
        "elapsed": 0.0126001834869
    }
    

### Get License

#### Description

Get the current license from CB Response.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Get Process Tree Data

#### Description

Get process tree data for process by the ID(JSON).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Process ID | String | N/A | Yes | Process unique ID.  
Segment ID | String | N/A | Yes | e.g. 1.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Process":
        {
            "process_md5": "517110bd83835338c037269e603db55d",
            "sensor_id": x,
            "group": "Default Group",
            "segment_id": x,
            "process_name": "xxxxxx.exe",
            "last_update": "2013-09-19T22:09:07Z",
            "cmdline": "taskhost.exe $(arg0)",
            "start": "2013-09-19T22:07:07Z",
            "parent_id": "xxxxxxxxx",
            "id": "xxxxxxxxx",
            "path": "c:\\\\\\\\xxxxxxx\\\\\\\\xxxxxxx\\\\\\\\xxxxxxx.exe",
            "os_type": "xxxxxxx",
            "hostname": "xxxxxxx-xxxxxx"
        },
        "Siblings": [
            {
                "process_md5": "c78655bc80301d76ed4fef1c1ea40a7d",
                "sensor_id": x,
                "group": "Default Group",
                "segment_id": x,
                "process_name": "xxxxxxxx.exe",
                "last_update": "2013-09-19T22:34:49Z",
                "start": "2013-09-10T04:10:07Z",
                "parent_id": "xxxxxxxxx",
                "id": "xxxxxxxxxxxx",
                "path": "c:\\\\\\\\xxxxxx\\\\\\\\xxxxxxx\\\\\\\\xxxxxx.exe",
                "os_type":"xxxxxx",
                "hostname": "xxx-xxxxxxx"
            }],
        "children": [],
        "parent": {
            "process_md5": "24acb7e5be595468e3b9aa488b9b4fcb",
            "sensor_id": x,
            "group": "Default Group",
            "segment_id": x,
            "process_name": "xxxxxx.exe",
            "last_update": "2013-09-19T22:09:07Z",
            "start": "2013-09-10T04:09:51Z",
            "parent_id": "xxxxxxxxxxxx",
            "id": "xxxxxxxxxxxxx",
            "path": "c:\\\\\\\\xxxxxxx\\\\\\\\xxxxxxx\\\\\\\\xxxxxx.exe",
            "os_type": "xxxxxx",
            "hostname": "xxx-xxxxxxxx"
        }
    }
    

### Get System Info

#### Description

Get system information for a sensor from CB Response and enrich the entity.

#### Parameters

N/A

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
                "systemvolume_total_size": "479127379968",
                "computer_name": "LP-WORKER",
                "os_environment_display_string": "Windows 10 Professional, 64-bit",
                "systemvolume_free_size": "319940304896",
                "physical_memory_size": "17058787328",
                "emet_version": "",
                "emet_dump_flags": "",
                "clock_delta": "10840",
                "supports_cblr": "True",
                "id": xx,
                "is_isolating": "False",
                "emet_process_count": 0,
                "build_id": 2,
                "uptime": "1640459",
                "computer_dns_name":"xx-xxxxxx.xxxxxx.xxxxx",
                "emet_report_setting": "(Locally configured)",
                "last_update": "2018-06-25 13:27:47.442521+03:00",
                "parity_host_id": "0",
                "power_state": 0,
                "network_isolation_enabled": "False",
                "uninstalled": "None",
                "next_checkin_time": "2018-06-25 13:28:13.089904+03:00",
                "status": "Offline",
                "num_eventlog_bytes": "13771",
                "sensor_health_message": "Elevated memory usage",
                "build_version_string": "1.1.1.1",
                "computer_sid": "S-1-5-21-x-x-x",
                "node_id": 0,
                "event_log_flush_time": "None",
                "emet_exploit_action": " (Locally configured)",
                "emet_telemetry_path":"",
                "license_expiration": "1990-01-01 00:00:00+02:00",
                "supports_isolation": "True",
                "emet_is_gpo": "False",
                "supports_2nd_gen_modloads": "False",
                "network_adapters": "x.x.x.x,xxxxxxxxx|",
                "sensor_health_status": 90,
                "registration_time": "2018-03-01 08:12:47.420579+02:00",
                "restart_queued": "False",
                "notes": "None",
                "num_storefiles_bytes": "0",
                "os_environment_id": 5,
                "cookie": 292474955,
                "shard_id": x,
                "boot_id": "xx",
                "last_checkin_time": "2018-06-25 13:27:43.091387+03:00",
                "os_type": 1,
                "group_id": x,
                "display": "True",
                "sensor_uptime": "x",
                "uninstall":"False"
            },
            "Entity": "xx-xxxxx"
        }
    ]
    

### Hosts by Process

#### Description

Get hosts that are related to a particular process.

#### Parameters

N/A

#### Run On

This action runs on the Process entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                    "systemvolume_total_size": "160534884352",
                    "computer_name": "COMPUTER",
                    "os_environment_display_string": "Windows 10 Server Server Standard (Evaluation), 64-bit",
                    "systemvolume_free_size": "120903110656",
                    "physical_memory_size": "8589463552",
                    "emet_version": "",
                    "emet_dump_flags": "",
                    "clock_delta": "7348",
                    "supports_cblr": "True",
                    "id": xx,
                    "is_isolating": "False",
                    "emet_process_count": 0,
                    "build_id": 2,
                    "uptime": "5888902",
                    "computer_dns_name": "COMPUTER",
                    "emet_report_setting": " (Locally configured)",
                    "last_update": "2019-01-07 11:07:17.187979+02:00",
                    "parity_host_id": "x",
                    "power_state": 0,
                    "network_isolation_enabled": "False",
                    "uninstalled": "None",
                    "next_checkin_time": "2019-01-07 11:07:44.348203+02:00",
                    "status": "Offline",
                    "num_eventlog_bytes": "34800",
                    "sensor_health_message": "Healthy",
                    "build_version_string": "1.1.1.1",
                    "computer_sid": "S-1-5-21-405201704-2854221227-856099807",
                    "node_id": 0,
                    "event_log_flush_time": "None",
                    "emet_exploit_action": " (Locally configured)",
                    "emet_telemetry_path": "",
                    "license_expiration": "1990-01-01 00:00:00+02:00",
                    "supports_isolation": "True",
                    "emet_is_gpo": "False",
                    "supports_2nd_gen_modloads": "False",
                    "network_adapters": "x.x.x.x,xxxxxxxx|",
                    "sensor_health_status": 100,
                    "registration_time": "2018-12-22 02:46:33.629175+02:00",
                    "restart_queued": "False",
                    "notes": "None",
                    "num_storefiles_bytes": "0",
                    "os_environment_id": 8,
                    "cookie": 1164577502,
                    "shard_id": 0,
                    "boot_id": "1",
                    "last_checkin_time": "2019-01-07 11:07:14.349477+02:00",
                    "os_type": 1,
                    "group_id": 1,
                    "display": "True",
                    "sensor_uptime": "1412441",
                    "uninstall": "False"
                }],
            "Entity": "xxxxxx.xxx"
        }
    ]
    

### Isolate Host

#### Description

Isolate an endpoint from the network.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Kill Process

#### Description

Kill a process on a particular host.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * Process
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### List Processes

#### Description

List processes that are related to given entities.

#### Parameters

N/A

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
            "EntityResult": [
                {
                    "modload_count": 63,
                    "sensor_id": xx,
                    "filtering_known_dlls": "False",
                    "process_md5": "00eb8baca58a0dd0106d67db566d6ea4",
                    "parent_unique_id": "x-x-x-x-x-x",
                    "emet_count": 0,
                    "cmdline": "python.exe C:\\\\\\\\HOST_Server\\\\\\\\z31fmfzn.vzo.py",
                    "last_update": "2018-12-30T13:39:55.642Z",
                    "id": "xxxxxx-xxxx-xxxxx-xxxxxx-xxxxxxx",
                    "parent_name": "xxxx.xxxxxx.xxxxxxx.xxxxxxx.exe",
                    "parent_md5": "000000000000000000000000000000",
                    "group": "Default Group",
                    "hostname": "xxxx",
                    "filemod_count": 7,
                    "start": "2018-12-30T13:39:34.728Z",
                    "emet_config": "",
                    "netconn_count": 2,
                    "interface_ip": 167772456,
                    "process_pid": 6024,
                    "username": "xxxx\\\\\\\\xxxx",
                    "terminated": "True",
                    "process_name": "xxxxx.exe",
                    "comms_ip": xxxxxx,
                    "path": "c:\\\\\\\\python27\\\\\\\\python.exe",
                    "regmod_count": 0,
                    "parent_pid": 4152,
                    "crossproc_count": 1,
                    "current_segment": 0,
                    "segment_id": x,
                    "host_type": "server",
                    "processblock_count": 0,
                    "os_type": "windows",
                    "childproc_count": 1,
                    "unique_id": "x-x-x-x-x-x"
                }],
            "Entity": "HOST"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Process Free Query

#### Description

List processes by free query.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | e.g. process_name:python.exe.  
  
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
            "process_md5": "00eb8baca58a0dd0106d67db566d6ea4",
            "sensor_id": xx,
            "filtering_known_dlls": "False",
            "modload_count": 63,
            "parent_unique_id": "x-x-x-x-x-x",
            "emet_count": 0,
            "group": "Default Group",
            "cmdline": "python.exe C:\\\\\\\\bin\\\\\\\\\\\\\\\\z31fmfzn.vzo.py",
            "last_update": "2018-12-30T13:39:55.642Z",
            "id": "x-x-x-x-x",
            "parent_name": "xxxx.xxxxxx.xxxxxx.xxxxxx.exe",
            "parent_md5": "000000000000000000000000000000",
            "parent_pid": 4152,
            "hostname": "xxxx",
            "filemod_count": 7,
            "start": "2018-12-30T13:39:34.728Z",
            "emet_config": "",
            "netconn_count": 2,
            "interface_ip": xxxxxxxx,
            "process_pid": 6024,
            "username": "xxxxx\\\\\\\\xxxxx",
            "terminated": "True",
            "process_name": "xxxxxx.xxx",
            "comms_ip": xxxxxxx,
            "path": "c:\\\\\\\\python27\\\\\\\\xxxxxx.exe",
            "regmod_count": 0,
            "crossproc_count": 1,
            "current_segment": 0,
            "segment_id": x,
            "host_type": "server",
            "processblock_count": 0,
            "os_type": "windows",
            "childproc_count": 1,
            "unique_id": "x-x-x-x-x-x"
        }
    ]
    

### Resolve Alert

#### Description

Resolve an alert.

**Note:** VMware Carbon Black EDR (EDR) REST-API returns a successful answer even if the alert that you tried to resolve doesn't exist.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | The ID of the alert to resolve.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Unblock Hash

#### Description

Unblock a hash.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Unisolate Host

#### Description

Rejoin an endpoint to the network.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
## Connectors

## Carbon Black Response Connector

### Configure Carbon Black Response Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Environment | DDL | N/A | Yes | Select the required environment. For example, "Customer One". In case that the alert's Environment field is empty, this alert will be injected to this environment.  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection.  
Product Field Name | String | device_product | Yes | The field name used to determine the device product.  
Event Field Name | String | name | Yes | The field name used to determine the event name (sub-type).  
Script Timeout (Seconds) | String | 60 | Yes | The timeout limit (in seconds) for the python process running current script.  
API Root | String | null | Yes | https://x.x.x.x  
API Key | Password | N/A | Yes | N/A  
Version | String | 6.3 | Yes | CB server version, default 6.3 will be used  
Alerts Count Limit | Integer | 20 | Yes | Limit the number of alerts in every cycle. Example: 20  
Max Days Backwards | Integer | 3 | Yes | This field is used in the connector first running cycle and determine the connector start time. Example: 3  
Environment Field Name | String | N/A | No | The name of the environment's field.  
List Type | String | N/A | No | Can be whitelist or blacklist.  
List Operator | String | N/A | No | Can be 'exact', 'start with', 'ends with' or 'contains'.  
List Fields | String | N/A | No | List of fields, comma-separated.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
