---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortianalyzer/
title: FortiAnalyzer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:31.053900+00:00
---

# FortiAnalyzer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortianalyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FortiAnalyzer

This document describes how to integrate FortiAnalyzer with Google Security Operations.

## Before you begin

To ensure successful communication between Google SecOps and FortiAnalyzer, you must configure a dedicated administrator account with specific API and resource permissions.

Category | Permission Level  
---|---  
**System Settings** | None  
**Administrative Domain** | None  
**Device Manager** | Read-Only  
Add/Delete/Edit Devices/Groups | Read-Only  
**Log View/FortiView** | Read-Only  
**Incidents & Events** | Read-Write  
Create & Update Incidents | Read-Write  
**Triage Event** | None  
**Execute Playbook** | None  
**Reports** | None  
Run Report | None  
**Fabric View** | None  
  
To enable the integration to communicate with the FortiAnalyzer API, you must grant the administrator account the necessary API permissions:

  1. In FortiAnalyzer, navigate to the administrator list and select the user account created for this integration.

  2. In the **Edit Administrator** sidebar, locate the **JSON API Access** field and set it to `Read-Write`.

  3. Click **OK** to save the changes.




### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{ip address} | Yes | API root of the FortiAnalyzer instance.  
Username | String | N/A | Yes | Username of the FortiAnalyzer account. Ensure that the credentials provided belong to a user account assigned to the profile defined in Before you begin.  
Password | Password | N/A | Yes | Password of the FortiAnalyzer account. Ensure that the credentials provided belong to a user account assigned to the profile defined in Before you begin.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the FortiAnalyzer is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add Comment To Alert

#### Description

Add a comment to the alert in FortiAnalyzer.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert that needs to be updated.  
Comment | String | N/A | Yes | Specify the comment for the alert.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "jsonrpc": "2.0",
        "id": "string",
        "result": {
            "status": "done"
        }
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If returned information (is_success=true):_ "Successfully added a comment to the alert with ID {id} in FortiAnalyzer." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Add Comment To Alert". Reason: {0}''.format(error.Stacktrace)" _If alert is not found:_ "Error executing action "Add Comment To Alert". Reason: alert with ID {alert id} wasn't found in FortiAnalyzer. Please check the spelling." | General  
  
### Enrich entities

#### Description

Enrich entities using information from FortiAnalyzer. Supported entities: Hostname, IP Address.

#### Parameters

N/A

#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "adm_pass": [
            "ENC",
            "FLP+Dq8f3t2/S+GQ6DfPL2iRhtmk1CEZzEeH8+nVkRkFd72IUbBZM6uDyw0fQ1j1i28H1wtfqf6HlGEK2ubxs0rXE4L+Uqj433si+AmEF9gEB5gLw/4P5YYRkw/aOYF74k8/8bincoa31jBe0u0HWRNdWYQSyG7IWgvZGsPK4at0gwZI"
        ],
        "adm_usr": "admin",
        "app_ver": "",
        "av_ver": "",
        "beta": -1,
        "branch_pt": 1255,
        "build": 1255,
        "checksum": "",
        "conf_status": 0,
        "conn_mode": 0,
        "conn_status": 0,
        "db_status": 0,
        "desc": "",
        "dev_status": 0,
        "eip": "",
        "fap_cnt": 0,
        "faz.full_act": 0,
        "faz.perm": 15,
        "faz.quota": 0,
        "faz.used": 0,
        "fex_cnt": 0,
        "first_tunnel_up": 0,
        "flags": 2097152,
        "foslic_cpu": 0,
        "foslic_dr_site": 0,
        "foslic_inst_time": 0,
        "foslic_last_sync": 0,
        "foslic_ram": 0,
        "foslic_type": 0,
        "foslic_utm": 0,
        "fsw_cnt": 0,
        "ha_group_id": 0,
        "ha_group_name": "",
        "ha_mode": 0,
        "ha_slave": null,
        "hdisk_size": 0,
        "hostname": "",
        "hw_rev_major": 0,
        "hw_rev_minor": 0,
        "hyperscale": 0,
        "ip": "172.30.203.248",
        "ips_ext": 0,
        "ips_ver": "",
        "last_checked": 1665664693,
        "last_resync": 0,
        "latitude": "0.0",
        "lic_flags": 0,
        "lic_region": "",
        "location_from": "",
        "logdisk_size": 0,
        "longitude": "0.0",
        "maxvdom": 10,
        "mgmt.__data[0]": 0,
        "mgmt.__data[1]": 0,
        "mgmt.__data[2]": 0,
        "mgmt.__data[3]": 0,
        "mgmt.__data[4]": 0,
        "mgmt.__data[5]": 0,
        "mgmt.__data[6]": 0,
        "mgmt.__data[7]": 0,
        "mgmt_if": "",
        "mgmt_mode": 2,
        "mgmt_uuid": "1841991674",
        "mgt_vdom": "",
        "module_sn": "",
        "mr": 2,
        "name": "FGVMEV2YKQ61YQD5",
        "node_flags": 0,
        "nsxt_service_name": "",
        "oid": 181,
        "onboard_rule": null,
        "opts": 0,
        "os_type": 0,
        "os_ver": 7,
        "patch": 2,
        "platform_str": "FortiGate-VM64",
        "prefer_img_ver": "",
        "prio": 0,
        "private_key": "",
        "private_key_status": 0,
        "psk": "",
        "role": 0,
        "sn": "FGVMEV2YKQ61YQD5",
        "source": 2,
        "tab_status": "",
        "tunnel_cookie": "",
        "tunnel_ip": "",
        "vdom": [
            {
                "comments": null,
                "devid": "FGVMEV2YKQ61YQD5",
                "ext_flags": 0,
                "flags": 0,
                "name": "root",
                "node_flags": 0,
                "oid": 3,
                "opmode": 1,
                "rtm_prof_id": 0,
                "status": null,
                "tab_status": null,
                "vdom_type": 1,
                "vpn_id": 0
            }
        ],
        "version": 700,
        "vm_cpu": 0,
        "vm_cpu_limit": 0,
        "vm_lic_expire": 0,
        "vm_mem": 0,
        "vm_mem_limit": 0,
        "vm_status": 0
    }
    

##### Entity Enrichment - Prefix FortiAn_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
adm_usr | adm_usr | When available in JSON  
build | build | When available in JSON  
ip | ip | When available in JSON  
last_checked | last_checked | When available in JSON  
last_resync | last_resync | When available in JSON  
name | name | When available in JSON  
sn | sn | When available in JSON  
os_type | os_type | When available in JSON  
os_ver | os_ver | When available in JSON  
patch | patch | When available in JSON  
platform\\_str | platform\\_str | When available in JSON  
version | version | When available in JSON  
desc | desc | When available in JSON  
  
##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from FortiAnalyzer: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from FortiAnalyzer: {entity.identifier}" _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Title:** {entity.identifier}**Columns:** Key Value | Entity  
  
### Ping

#### Description

Test connectivity to FortiAnalyzer with parameters provided at the integration configuration page in the Google Security Operations Marketplace tab.

#### Parameters

N/A

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

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the BitSight server with the provided connection parameters!" **The action should fail and stop a playbook execution:** If not successful: "Failed to connect to the BitSight server! Error is {0}".format(exception.stacktrace) | General  
  
### Search Logs

#### Description

Search logs in FortiAnalyzer.

**Note:** Action is running as async, adjust the script timeout value in the IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Log Type | DDL | Traffic Possible values:

  * Traffic
  * App Control
  * Attack
  * Content, DLP
  * Email Filter
  * Event, History
  * Virus
  * VOIP
  * Web Filter
  * Netscan
  * FCT Event
  * FCT Traffic
  * WAF
  * GTP

| No | Specify the log type that needs to be searched.  
Case Sensitive Filter | Checkbox | Unchecked | No | If enabled, the filter is case sensitive.  
Query Filter | String | N/A | No | Specify the query filter for the search.  
Device ID | String | All\\_Fortigate | No | Specify the ID of the device that needs to be searched. If nothing is provided, the action searches in All_Fortigate. Examples of values: All_FortiGate, All_FortiMail, All_FortiWeb, All_FortiManager, All_Syslog, All_FortiClient, All_FortiCache, All_FortiProxy, All_FortiAnalyzer, All_FortiSandbox, All_FortiAuthenticator, All_FortiDDoS  
Time Frame | DDL | Last Month Possible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results. If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.  
Time Order | DDL | DESC Possible values:

  * DESC
  * ASC

| No | Specify the time ordering in the search.  
Max Logs To Return | Integer | 20 | No | Specify the number of logs you want to return. Default: 20. Maximum: 1000.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "sessionid": "29658",
        "srcip": "172.30.201.188",
        "dstip": "173.243.138.210",
        "srcport": "17453",
        "dstport": "443",
        "trandisp": "noop",
        "duration": "1",
        "proto": "6",
        "sentbyte": "216",
        "rcvdbyte": "112",
        "sentpkt": "4",
        "rcvdpkt": "2",
        "logid": "0001000014",
        "service": "HTTPS",
        "app": "HTTPS",
        "appcat": "unscanned",
        "srcintfrole": "undefined",
        "dstintfrole": "undefined",
        "eventtime": "1665752066921638736",
        "srccountry": "Reserved",
        "dstcountry": "Canada",
        "srcintf": "root",
        "dstintf": "port1",
        "dstowner": "540",
        "tz": "-0700",
        "devid": "FGVMEV2YKQ61YQD5",
        "vd": "root",
        "csf": "FortiNetFabric",
        "dtime": "2022-10-14 05:54:27",
        "itime_t": "1665752069",
        "devname": "FGVMEV2YKQ61YQD5"
    }{
        "date": "2022-10-14",
        "time": "05:54:27",
        "id": "7154350659607724033",
        "itime": "2022-10-14 05:54:29",
        "euid": "102",
        "epid": "102",
        "dsteuid": "102",
        "dstepid": "102",
        "logver": "702021255",
        "type": "traffic",
        "subtype": "local",
        "level": "notice",
        "action": "close",
        "policyid": "0"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If returned information (is_success=true):_ "Successfully retrieved logs for the provided criteria in FortiAnalyzer." _If returned no information (is_success=true):_ "No logs were found for the provided criteria in FortiAnalyzer." **The action should fail and stop a playbook execution:** If a fatal error, like wrong credentials, no connection to the server, or other is reported: "Error executing action "Search Logs". Reason: {0}''.format(error.Stacktrace)" If an error is reported in the response: "Error executing action "Search Logs". Reason: {0}''.format(error/message)" | General  
  
### Update alert

#### Description

Update an alert in FortiAnalyzer.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert that needs to be updated.  
Acknowledge Status | DDL | Select One Possible values:

  * Select One
  * Acknowledge
  * Unacknowledge

| No | Specify the acknowledgment status for alert.  
Mark As Read | Checkbox | Unchecked | No | If enabled, the action marks the alert as read.  
Assign To | String | N/A | No | Specify to whom the alert needs to be assigned.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "alerttime": "1665653864",
        "logcount": "17",
        "alertid": "202210131000040003",
        "adom": "root",
        "epid": "1",
        "epname": "not implemented dev type",
        "subject": "desc:Trim local db",
        "euid": "1",
        "euname": "N/A",
        "devname": "fortianalyzer",
        "logtype": "event",
        "devtype": "FortiAnalyzer",
        "devid": "FAZ-VMTM22013516",
        "vdom": "_self_locallog_",
        "groupby1": "desc:Trim local db",
        "triggername": "Local Device Event",
        "tag": "Default,System,Local",
        "eventtype": "event",
        "severity": "medium",
        "extrainfo": "{ \"msg\": \"Requested to trim database tables older than 60 days to enforce the retention policy of Adom FortiAuthenticator.\" }",
        "ackflag": "no",
        "readflag": "yes",
        "filterkey": "3377053565526629289",
        "firstlogtime": "1665653864",
        "multiflag": "",
        "lastlogtime": "1665653887",
        "updatetime": "1665747977",
        "filtercksum": "2072153473",
        "filterid": "1",
        "assignto": "api_user",
        "ackby": "admin",
        "acktime": "1665747892"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If returned information (is_success=true):_ "Successfully updated alert with ID {alert id} in FortiAnalyzer." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Update Alert". Reason: {0}''.format(error.Stacktrace) _If alert is not found:_ "Error executing action "Update Alert". Reason: alert with ID {alert id} wasn't found in FortiAnalyzer. Please check the spelling." If the "Acknowledge Status" parameter is set to "Select One", the "Mark as Read" parameter is set to False and nothing is provided in the "Assign To" parameter: "Error executing action "Update Alert". Reason: at least one of the "Acknowledge Status", "Mark As Read" or "Assign To" parameters should have a value ." | General  
  
## Connectors

### FortiAnalyzer - Alerts Connector

#### Description

Pull information about alerts from FortiAnalyzer.

**Note:** The dynamic list filter works with the "subject" parameter.

#### Configure FortiAnalyzer - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | siemplify_type | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{ip address} | Yes | API root of the FortiAnalyzer instance.  
Username | String | N/A | Yes | Username of the FortiAnalyzer account.  
Password | Password | N/A | Yes | Password of the FortiAnalyzer account.  
Lowest Severity To Fetch | String | Medium | No | The lowest severity that needs to be used to fetch alerts. Possible values: low, medium, high, critical. If nothing is specified, the connector ingests alerts with all severities.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 20 | No | Number of alerts per type to process per one connector iteration.  
Use dynamic list as a blacklist | Checkbox | Unchecked | Yes | If enabled, the dynamic list is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, the connector verifies that the SSL certificate for the connection to the FortiAnalyzer server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
