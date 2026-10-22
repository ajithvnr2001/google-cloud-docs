---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nozomi-networks/
title: Nozomi Networks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:31.015737+00:00
---

# Nozomi Networks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nozomi-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Nozomi Networks

This document provides guidance on how to integrate Nozomi Networks with Google SecOps.

## Use Cases

  * Enrich information about assets.
  * Perform queries against Nozomi installation.
  * Perform CLI commands on Nozomi installation.



## Configure Nozomi Networks integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API URL | String | https://x.x.x.x:port | Yes | Nozomi API URL to connect to  
Username | String | N/A | Yes | Nozomi account username to use for connection  
Password | Password | N/A | Yes | Nozomi account password to use for connection  
Verify SSL | Checkbox | Unchecked | No | Specify whether API URL certificate should be validated before connection.  
CA Certificate | String | N/A | No |   
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Nozomi Networks instance with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successfu** l: print "Successfully connected to the Nozomi Networks instance with the provided connection parameters!"

**The action should fail and stop a playbook execution:**

  * **if critical error, like wrong credentials or lost connectivity** : print "Failed to connect to the Nozomi Networks instance! Error is {0}".format(exception.stacktrace)

| General  
  
### Enrich Entities

#### Description

Enrich Google SecOps Host or IP entities based on the information from the Nozomi Networks device.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional fields to add to enrichment | String | N/A | No | Comma separated list of fields that should be additionally taken from Nodes query to add to fields that are used for enrichment by default.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "result": [
            {
                "appliance_host": "nozomi-n2os.local",
                "label": "DESKTOP-8P0TH6Q.local",
                "id": "172.30.202.127",
                "_asset_kb_id": null,
                "ip": "172.30.202.127",
                "mac_address": "00:50:56:a2:51:88",
                "mac_address:info": {
                    "source": "",
                    "likelihood": 0,
                    "likelihood_level": "unconfirmed"
                },
                "mac_vendor": "VMware, Inc.",
                "_private_status": "no",
                "subnet": "172.30.202.0/24",
                "vlan_id": null,
                "vlan_id:info": {
                    "source": "passive"
                },
                "zone": "Internal",
                "level": "5",
                "type": "computer",
                "type:info": {
                    "source": "passive"
                },
                "os": "Windows 10 / Server 2016",
                "vendor": null,
                "vendor:info": {
                    "source": "passive"
                },
                "product_name": null,
                "product_name:info": {
                    "source": "passive"
                },
                "firmware_version": null,
                "firmware_version:info": {
                    "source": "passive"
                },
                "serial_number": null,
                "serial_number:info": {
                    "source": "passive"
                },
                "is_broadcast": false,
                "is_public": false,
                "reputation": null,
                "is_confirmed": true,
                "is_learned": true,
                "is_fully_learned": true,
                "is_disabled": false,
                "_is_licensed": true,
                "roles": [
                    "other"
                ],
                "links": [
                    {
                        "id": "224.0.0.252",
                        "protos": [
                            {
                                "name": "llmnr",
                                "last_activity": "1602495882225"
                            }
                        ]
                    },
                    {
                        "id": "172.30.202.255",
                        "protos": [
                            {
                                "name": "browser",
                                "last_activity": "1605052230602"
                            },
                            {
                                "name": "netbios-ns",
                                "last_activity": "1604654773056"
                            }
                        ]
                    },
                    {
                        "id": "224.0.0.251",
                        "protos": [
                            {
                                "name": "mdns",
                                "last_activity": "1602636321803"
                            }
                        ]
                    },
                    {
                        "id": "239.255.255.250",
                        "protos": [
                            {
                                "name": "ssdp",
                                "last_activity": "1600331209918"
                            }
                        ]
                    }
                ],
                "links_count": "5",
                "protocols": [
                    "browser",
                    "llmnr",
                    "mdns",
                    "netbios-ns",
                    "ssdp"
                ],
                "created_at": "1595315728295",
                "first_activity_time": "1595315728295",
                "last_activity_time": "1605052230602",
                "received.packets": "0",
                "received.bytes": "0",
                "received.last_5m_bytes": "0",
                "received.last_15m_bytes": "0",
                "received.last_30m_bytes": "0",
                "sent.packets": "5088",
                "sent.bytes": "1031179",
                "sent.last_5m_bytes": "0",
                "sent.last_15m_bytes": "0",
                "sent.last_30m_bytes": "0",
                "tcp_retransmission.percent": 0,
                "tcp_retransmission.packets": "0",
                "tcp_retransmission.bytes": "0",
                "tcp_retransmission.last_5m_bytes": "0",
                "tcp_retransmission.last_15m_bytes": "0",
                "tcp_retransmission.last_30m_bytes": "0",
                "variables_count": null,
                "device_id": "TIP-HW-HOST-033",
                "properties": {},
                "custom_fields": {},
                "bpf_filter": "ip host 172.30.202.127",
                "device_modules": {},
                "capture_device": "em1"
            }
        ],
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Nozomi.level | When not null  
Nozomi.appliance_host | When not null  
Nozomi.ip | When not null  
Nozomi.mac_address | When not null  
Nozomi.vlan_id | When not null  
Nozomi.os | When not null  
Nozomi.roles | When not null  
Nozomi.vendor | When not null  
Nozomi.firmware_version | When not null  
Nozomi.serial_number | When not null  
Nozomi.product_name | When not null  
Nozomi.type | When not null  
Nozomi.protocols | When not null  
Nozomi.device_id | When not null  
Nozomi.capture_device | When not null  
Nozomi.is_broadcast | When not null  
Nozomi.is_public | When not null  
Nozomi.is_confirmed | When not null  
Nozomi.is_disabled | When not null  
Nozomi.is_licensed | When not null  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful and at least one of the provided entities were enriched:** print "Successfully enriched entities: {0}".format([entity.Identifier]).
  * **If fail to enrich all of the provided entities:** print "No entities were enriched."
  * **If fail to find data in Nozomi device to enrich specific entities:** print "Action was not able to find Nozomi Guardian information to enrich the following entities: {0}".format([entity.identifier])
  * **If action found multiple matches in Nozomi for some Google SecOps entities, first match was taken to enrich entities:** print "Multiple matches were found in Nozomi Guardian, taking first match for the following entities:/n {0}".format(entity.identifiers list)

**The action should fail and stop a playbook execution:**

  * **If fatal error, like wrong credentials, no connection to server, other:** print "Failed to execute Enrich Entities action! Error is {0}".format(exception.stacktrace)

| General  
  
### Run a Query

#### Description

Run a query on Nozomi Networks device.

**Note:** Action is not working with Google SecOps Entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify a query to execute on Nozomi Networks device, for example: alerts | head 10.  
Record Limit | Integer | 10 | No | Can be used to specify how many records can be returned by the action. If default value of 10 is set, parameter adds "| head 10" to the final query to limit the number of returned records. If nothing is provided for the parameter - all query results are returned. Negative values are ignored.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "result": [
            {
                "id": "0bee5f36-9b50-4037-8b02-f02f5cd637c3",
                "type_id": "VI:NEW-ARP",
                "name": "New ARP",
                "description": "New ARP packet from node with MAC address 00:50:56:a2:e8:0b and IP address 172.30.202.8",
                "severity": 10,
                "mac_src": "00:50:56:a2:e8:0b",
                "mac_dst": "ff:ff:ff:ff:ff:ff",
                "ip_src": "172.30.202.8",
                "ip_dst": null,
                "risk": "6.0",
                "protocol": "arp",
                "src_roles": "other",
                "dst_roles": "other",
                "time": 1604974955058,
                "ack": false,
                "id_src": "00:50:56:a2:e8:0b",
                "id_dst": "ff:ff:ff:ff:ff:ff",
                "synchronized": false,
                "appliance_id": "",
                "port_src": null,
                "port_dst": null,
                "label_src": null,
                "label_dst": null,
                "trigger_id": null,
                "trigger_type": null,
                "appliance_host": "nozomi-n2os.local",
                "appliance_ip": "172.30.202.226",
                "transport_protocol": "ethernet",
                "is_security": true,
                "note": null,
                "appliance_site": null,
                "parents": [
                    "9827b15f-bbdf-483a-b074-8991793f80f3",
                    "e76a4060-50f1-47cd-98c4-fb25bfb16433"
                ],
                "is_incident": false,
                "properties": {
                    "base_risk": 4,
                    "from_id": "00:50:56:a2:e8:0b",
                    "is_dst_node_learned": true,
                    "is_dst_reputation_bad": false,
                    "is_src_node_learned": false,
                    "is_src_reputation_bad": false,
                    "to_id": "ff:ff:ff:ff:ff:ff"
                },
                "created_time": 1604974955058,
                "incident_keys": [],
                "bpf_filter": "ether host 00:50:56:a2:e8:0b and ether host ff:ff:ff:ff:ff:ff and ether proto 0x0806",
                "closed_time": 0,
                "status": "open",
                "session_id": "154400:50:56:a2:e8:0bff:ff:ff:ff:ff:ff0000175aff64a32",
                "replicated": false,
                "capture_device": "em1",
                "threat_name": "",
                "type_name": "New ARP",
                "sec_profile_visible": true,
                "zone_src": "Layer2",
                "zone_dst": "Layer2"
            },
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**

  * **if successful:** print "Query executed successfully".
  * **if nothing found:** print "Query executed successfully, but did not return any results.".
  * **if error: print "Query didn't completed due to error:** {0}".format(exception.stacktrace).
  * **If timeout: print "Query didn't completed due to timeout** {0}".format(exception.stacktrace).

**Action should fail and stop playbook execution:**

  * **If fatal error, like wrong credentials, no connection to server, other:** print "Failed to execute Run a Query action! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table title:** Query Results**Columns:** dynamically generate columns based on the query result | General  
  
### Run a CLI Command

#### Description

Run a CLI command on Nozomi Networks device.

**Note:** Nozomi API doesn't provide a validation for executed CLI commands, its up to the User to make sure that the provided CLI command is correct. Action is not working with Google SecOps Entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
CLI Command | String | N/A | Yes | Specify a CLI Command to execute on Nozomi Networks device. Note: Nozomi API doesn't provide a validation for executed CLI commands, its up to the User to make sure that the provided CLI command is correct.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**

  * **if successful:** print "CLI Command executed".

**Action should fail and stop playbook execution:**

  * **If fatal error, like wrong credentials, no connection to server, other:** print "Failed to execute Run a Query action! Error is {0}".format(exception.stacktrace)

| General  
  
### List Vulnerabilities

#### Description

List vulnerabilities discovered by Nozomi device based on the provided action input parameters.

**Note:** Action is not working with Google SecOps entities, only with action input parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IP Address | String | N/A | No | List vulnerabilities for the provided ip address. Parameter accepts multiple values as a comma separated string.  
CVE Score | Integer | N/A | No | Minimum CVE score vulnerability should have to be listed, score can be a number from 0 to 10.  
Vulnerability Name Contains | String | N/A | No | Specify a string that vulnerability name should contain to be listed.  
CVE ID | String | N/A | No | If you know specific CVE to look for, provide the related id in this field, for example, CVE-2020-1207. Parameter accepts multiple values as a comma separated string.  
Record Limit | Integer | 25 | Yes | Can be used to specify how many records can be returned by the action.  
Include vulnerabilities that marked as resolved? | Checkbox | Unchecked | No | Specify whether action should also return vulnerabilities that are marked as resolved.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "result": [
            {
                "id": "cb9054a6-11a6-47ff-9c08-8033e42f9e63",
                "node_id": "172.30.202.71",
                "cve": "CVE-2017-8718",
                "cve_summary": "The Microsoft JET Database Engine in Windows Server 2008 SP2 and R2 SP1, Windows 7 SP1, Windows 8.1 and RT 8.1, Windows Server 2012 and R2, Windows 10 Gold, 1511, 1607, 1703, and Windows Server 2016 allows an attacker to take control of an affected system, due to how it handles objects in memory, aka \"Microsoft JET Database Engine Remote Code Execution Vulnerability\". This CVE ID is unique from CVE-2017-8717.",
                "cve_score": 9.3,
                "cve_creation_time": 1507886940000,
                "cve_update_time": 1508488860000,
                "time": 1598516419115,
                "cwe_id": "119",
                "cwe_name": "Improper Restriction of Operations within the Bounds of a Memory Buffer",
                "matching_cpes": [
                    "cpe:/o:microsoft:windows_server_2016:-:-:-"
                ],
                "cve_references": [
                    {
                        "name": "101162",
                        "reference_type": "VENDOR_ADVISORY",
                        "source": "BID",
                        "url": "http://www.securityfocus.com/bid/101162"
                    },
                    {
                        "name": "1039527",
                        "reference_type": "VENDOR_ADVISORY",
                        "source": "SECTRACK",
                        "url": "http://www.securitytracker.com/id/1039527"
                    },
                    {
                        "name": "https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8718",
                        "reference_type": "VENDOR_ADVISORY",
                        "source": "CONFIRM",
                        "url": "https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8718"
                    }
                ],
                "likelihood": 0.4,
                "resolved": false,
                "resolved_reason": "",
                "resolved_source": null,
                "installed_on": null,
                "appliance_id": "",
                "appliance_ip": "",
                "appliance_host": "",
                "zone": "Internal"
            }
        ],
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**

  * **if successful:** print "Search executed successfully".
  * **if nothing found:** print "Search executed successfully, but did not return any results.".

**Action should fail and stop playbook execution:**

  * **If fatal error, like wrong credentials, no connection to server, other:** print "Failed to execute Run a Query action! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table title:** Vulnerabilities Found**Columns:** Ip address CVE ID Vulnerability name Vulnerability Description CVE ScoreZone Is Resolved References CVE Creation Time CVE Update Time | General  
  
## Connector

### Nozomi Networks Alerts Connector

#### Description

Connector to fetch Nozomi Networks Alerts to Google SecOps.

#### Configure Nozomi Networks Alerts Connector on Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | Operation | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API URL | String | https://x.x.x.x:port | Yes | Nozomi API URL to connect to  
Username | String | N/A | Yes | Nozomi account username to use for connection  
Password | Password | N/A | Yes | Nozomi account password to use for connection  
Verify SSL | Checkbox | Unchecked | No | Specify whether API URL certificate should be validated before connection.  
CA Certificate | String | N/A | No |   
Minimum severity to fetch | integer | N/A | No | Minimum severity alert should have to be ingested, severity can be a number from 0 to 10.  
Ingest only alerts that have "is_security" attribute set to True? | Checkbox | Unchecked | No | Specify if only alerts that have "is_security" attribute set to True should be ingested.  
Ingest only alerts that have "is_incident" attribute set to True? | Checkbox | Unchecked | No | Specify if only alerts that have "is_incident" attribute set to True should be ingested.  
Fetch Max Hours Backwards | Integer | 8 | Yes | Fetch alerts from X hours backwards.  
Fetch Backwards Time Interval (minutes) | Integer | 60 | Yes | Time interval connector should use to fetch alerts from max hours backwards. If Nozomi Device is deployed in a large network, the number of generated alerts can be substantial. Because of this, this parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Time interval cant be bigger than max hours backwards value.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
