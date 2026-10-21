---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tenableio/
title: Tenable.io \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:30.039863+00:00
---

# Tenable.io  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tenableio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tenable.io

**Important:** Tenable.io was renamed to Tenable Vulnerability Management.

This document provides guidance on how to integrate Tenable.io with Google SecOps.

## Use Cases

Perform enrichment of entities.

## Configure Tenable.io integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://cloud.tenable.com/ | Yes | API root of the Tenable Vulnerability Management instance.  
Secret Key | Password | N/A | Yes | Secret Key of the Tenable Vulnerability Management instance  
Access Key | Password | N/A | Yes | Access Key of the Tenable Vulnerability Management instance  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Tenable Vulnerability Management server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate Secret Key and Access Key

For more information, see [Generate API Keys](https://docs.tenable.com/tenableio/Content/Settings/GenerateAPIKey.htm).

## Actions

### Ping

#### Description

Test connectivity to the Tenable Vulnerability Management with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
**if successful:** "Successfully connected to the Tenable Vulnerability Management server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Tenable Vulnerability Management server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Tenable Vulnerability Management. Supported entities: IP Address, Hostname.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### JSON Result
    
    
    {
        "id": "6fd54284-7f0a-4cd2-afd5-49b847416e94",
        "has_agent": false,
        "created_at": "2020-07-29T09:36:39.253Z",
        "updated_at": "2021-07-06T10:21:33.889Z",
        "first_seen": "2020-07-29T09:36:25.336Z",
        "last_seen": "2021-07-06T10:21:31.194Z",
        "last_scan_target": "172.30.202.208",
        "last_authenticated_scan_date": null,
        "last_licensed_scan_date": "2021-07-06T10:21:31.194Z",
        "last_scan_id": "0dec9fa1-dccf-41d7-acd8-b5c0f2c17618",
        "last_schedule_id": "template-6e1a45e4-aee8-3c16-b1d0-d2c911747440267fa5001a36e72d",
        "sources": [
            {
                "name": "NESSUS_SCAN",
                "first_seen": "2020-07-29T09:36:25.336Z",
                "last_seen": "2021-07-06T10:21:31.194Z"
            }
        ],
        "tags": [],
        "interfaces": [
            {
                "name": "UNKNOWN",
                "fqdn": [],
                "mac_address": [
                    "00:50:56:a2:04:db"
                ],
                "ipv4": [
                    "172.30.202.208"
                ],
                "ipv6": []
            }
        ],
        "network_id": [
            "00000000-0000-0000-0000-000000000000"
        ],
        "ipv4": [
            "172.30.202.208"
        ],
        "ipv6": [],
        "fqdn": [],
        "mac_address": [
            "00:50:56:a2:04:db"
        ],
        "netbios_name": [],
        "operating_system": [
            "Linux Kernel 4.4 on Ubuntu 16.04 (xenial)"
        ],
        "system_type": [
            "general-purpose"
        ],
        "tenable_uuid": [],
        "hostname": [],
        "agent_name": [],
        "bios_uuid": [],
        "aws_ec2_instance_id": [],
        "aws_ec2_instance_ami_id": [],
        "aws_owner_id": [],
        "aws_availability_zone": [],
        "aws_region": [],
        "aws_vpc_id": [],
        "aws_ec2_instance_group_name": [],
        "aws_ec2_instance_state_name": [],
        "aws_ec2_instance_type": [],
        "aws_subnet_id": [],
        "aws_ec2_product_code": [],
        "aws_ec2_name": [],
        "azure_vm_id": [],
        "azure_resource_id": [],
        "gcp_project_id": [],
        "gcp_zone": [],
        "gcp_instance_id": [],
        "ssh_fingerprint": [],
        "mcafee_epo_guid": [],
        "mcafee_epo_agent_guid": [],
        "qualys_asset_id": [],
        "qualys_host_id": [],
        "servicenow_sysid": [],
        "installed_software": [
            "cpe:/a:openbsd:openssh:7.2"
        ],
        "bigfix_asset_id": [],
        "security_protection_level": null,
        "security_protections": [],
        "exposure_confidence_value": null
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
has_agent | When available in JSON  
last_seen | When available in JSON  
tags | When available in JSON  
ipv4 | When available in JSON  
ipv6 | When available in JSON  
netbios_name | When available in JSON  
hostname | When available in JSON  
OS | When available in JSON  
mac_address | When available in JSON  
system_type | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available for one(is_success = true):** "Successfully enriched the following entities using information from Tenable Vulnerability Management: {entity.identifier}".  
******If data is not available for one (is_success=true):** "Action wasn't able to enrich the following entities using information from Tenable Vulnerability Management: {entity.identifier}"**.****If data is not available for all (is_success=false):** None of the provided entities were enriched.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Title:** {entity.identifier} | Entity  
  
### List Plugin Families

#### Description

List available plugin families from Tenable Vulnerability Management.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among record types and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Plugin Families To Return | Integer | 50 | No | Specify how many plugin families to return. Default: 50.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
#### JSON Result
    
    
    [
            {
                "count": 11396,
                "name": "AIX Local Security Checks",
                "id": 27
            },
            {
                "count": 1986,
                "name": "Amazon Linux Local Security Checks",
                "id": 28
            },
            {
                "count": 121,
                "name": "Backdoors",
                "id": 9
            }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found at least one (is_success = true):** "Successfully listed available plugin families based on the provided criteria in Tenable Vulnerability Management.  
******If nothing was found(is_succees=true):** "No plugin families were found based on the provided criteria in Tenable Vulnerability Management"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Plugin Families". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Available Plugin Families**Columns:** Name Count  | General  
  
### Get Vulnerability Details

#### Description

Retrieve vulnerability details from Tenable Vulnerability Management.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Plugin IDs | CSV | N/A | No | Specify a comma-separated list of plugin IDs for which you want to return details.  
Create Insight | Checkbox | Un-checked | No | If enabled, action will create an insight containing information about all of the processed plugin ids.  
  
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
    "plugin_id": {plugin_id},
        "count": 1,
        "vuln_count": 27,
        "recasted_count": 0,
        "accepted_count": 0,
        "description": "The remote service accepts connections encrypted using TLS 1.0. TLS 1.0 has a number of cryptographic design flaws. Modern implementations of TLS 1.0 mitigate these problems, but newer versions of TLS like 1.2 and 1.3 are designed against these flaws and should be used whenever possible.\n\nAs of March 31, 2020, Endpoints that aren't enabled for TLS 1.2 and higher will no longer function properly with major web browsers and major vendors.\n\nPCI DSS v3.2 requires that TLS 1.0 be disabled entirely by June 30, 2018, except for POS POI terminals (and the SSL/TLS termination points to which they connect) that can be verified as not being susceptible to any known exploits.",
        "synopsis": "The remote service encrypts traffic using an older version of TLS.",
        "solution": "Enable support for TLS 1.2 and 1.3, and disable support for TLS 1.0.",
        "discovery": {
            "seen_first": "2020-07-29T10:29:04.991Z",
            "seen_last": "2021-07-06T10:11:11.706Z"
        },
        "severity": "Medium",
        "plugin_details": {
            "family": "Service detection",
            "modification_date": "2020-03-31T00:00:00Z",
            "name": "TLS Version 1.0 Protocol Detection",
            "publication_date": "2017-11-22T00:00:00Z",
            "type": "remote",
            "version": "1.9",
            "severity": "Medium"
        },
        "reference_information": [],
        "risk_information": {
            "risk_factor": "Medium",
            "cvss_vector": "AV:N/AC:H/Au:N/C:C/I:P/A:N",
            "cvss_base_score": "6.1",
            "cvss_temporal_vector": null,
            "cvss_temporal_score": null,
            "cvss3_vector": "AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N",
            "cvss3_base_score": "6.5",
            "cvss3_temporal_vector": null,
            "cvss3_temporal_score": null,
            "stig_severity": null
        },
        "see_also": [
            "https://tools.ietf.org/html/draft-ietf-tls-oldversions-deprecate-00"
        ],
        "vulnerability_information": {
            "vulnerability_publication_date": null,
            "exploited_by_malware": null,
            "patch_publication_date": null,
            "exploit_available": null,
            "exploitability_ease": null,
            "asset_inventory": "True",
            "default_account": null,
            "exploited_by_nessus": null,
            "in_the_news": null,
            "malware": null,
            "unsupported_by_vendor": null,
            "cpe": null,
            "exploit_frameworks": []
        }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data for at least one (is_success = true):** "Successfully retrieved information about the following vulnerabilities in Tenable Vulnerability Management: {plugin id}  
******if no data for at least one (is_success = true):** "Action wasn't able to retrieve information about the following vulnerabilities in Tenable Vulnerability Management: {plugin id}  
******if no data for all (is_success = false)** : "No information about provided vulnerabilities was found"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Vulnerability Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Vulnerability Details**Columns:** ID Severity Synopsis SolutionFamily | General  
  
### List Policies

#### Description

List available policies in Tenable Vulnerability Management.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Policies To Return | Integer | 50 | No | Specify how many policies to return. Default: 50. Max: 100.  
  
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
        "policies": [
            {
                "no_target": "false",
                "template_uuid": "731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65",
                "description": null,
                "name": "Koko",
                "owner": "dana@siemplify.co",
                "visibility": "private",
                "shared": 0,
                "user_permissions": 128,
                "last_modification_date": 1625744218,
                "creation_date": 1625744218,
                "owner_id": 2,
                "id": 73
            },
            {
                "no_target": "false",
                "template_uuid": "731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65",
                "description": null,
                "name": "Koko_01",
                "owner": "dana@siemplify.co",
                "visibility": "private",
                "shared": 0,
                "user_permissions": 128,
                "last_modification_date": 1625744230,
                "creation_date": 1625744230,
                "owner_id": 2,
                "id": 74
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully found policies for the provided criteria in Tenable Vulnerability Management.  
******if not found results (is_success = true):** "No policies were found for the provided criteria in Tenable Vulnerability Management.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Policies". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Available Policies**Columns:** Name Visibility Description | General  
  
### List Endpoint Vulnerabilities

#### Description

List endpoint vulnerabilities in Tenable Vulnerability Management. Supported entities: IP Address, Hostname.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Lowest Severity To Fetch | DDL | InfoPossible values:Info,  
Low,  
Medium,  
High,  
Critical | No | Specify the lowest severity that will be used to fetch vulnerabilities.  
Max Vulnerabilities To Return | Integer | 50 | No | Specify how many vulnerabilities to return per entity. Default: 50. Maximum: 200.  
  
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
        "count": 1,
        "plugin_family": "Windows",
        "plugin_id": 22313,
        "plugin_name": "Microsoft Exchange Server Unsupported Version Detection",
        "vulnerability_state": "New",
        "accepted_count": 0,
        "recasted_count": 0,
        "counts_by_severity": [
            {
                "count": 1,
                "value": 4
            }
        ],
        "severity": Critical
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data for at least one (is_success = true):** "Successfully listed vulnerabilities related to the following endpoints in Tenable Vulnerability Management: {entity.identifier}  
******if one endpoint not found (is_success = true):** "Action wasn't able to find the following endpoints in Tenable Vulnerability Management: {entity.identifier}  
******If no data for at least one endpoint (is_success = true):** "No vulnerabilities were found for the following endpoints: {entity.identifier}"  
******if no data for all (is_success = true):** "No vulnerabilities were found for the provided endpoints.  
******if no endpoints were found (is_success = false):** "Provided endpoints were not found in Tenable Vulnerability Management"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Endpoint Vulnerabilities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Columns:** ID Name Severity Family  | Entity  
  
### Scan Endpoints

#### Description

Initiate a scan on endpoints in Tenable Vulnerability Management. Supported entities: IP Address, Hostname.

**Note:** Action is running as async, please adjust script timeout value in Google SecOps IDE for action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scan Name | String | N/A | Yes | Specify the name of the scan.  
Policy Name | String | N/A | Yes | Specify the name of the policy that needs to be used for scanning. Note: in the UI those policies are shown in the "Scan Templates"  
Scanner Name | String | N/A | No | Specify the name of the scanner that should be used. If nothing is provided, action will use the default scanner from configuration.  
Send Report To | CSV | N/A | No | Specify a comma-separated list of email addresses that need to receive the scan report.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
      {
         "info": {
            "owner": "dana@siemplify.co",
            "name": "ScanWindows5",
            "no_target": false,
            "folder_id": 4,
            "control": true,
            "user_permissions": 128,
            "schedule_uuid": "template-c3f64881-a8b7-fea6-47c7-97e9b1bd50cb34fff961031c193c",
            "edit_allowed": false,
            "scanner_name": "scanner-name",
            "policy": "Advanced Network Scan",
            "shared": null,
            "object_id": 58,
            "tag_targets": null,
            "acls": [
                {
                    "permissions": 0,
                    "owner": null,
                    "display_name": null,
                    "name": null,
                    "uuid": null,
                    "id": null,
                    "type": "default"
                },
                {
                    "permissions": 128,
                    "owner": 1,
                    "display_name": "dana@siemplify.co",
                    "name": "dana@siemplify.co",
                    "uuid": "3385d69a-8829-4ee7-bfc3-0362c74fbc90",
                    "id": 2,
                    "type": "user"
                }
            ],
            "hostcount": 1,
            "uuid": "e87030dd-41e8-4598-8dc0-06e4be3aeda5",
            "status": "completed",
            "scan_type": "remote",
            "targets": "172.30.202.196",
            "alt_targets_used": false,
            "pci-can-upload": false,
            "scan_start": 1625565548,
            "timestamp": 1625566340,
            "is_archived": false,
            "reindexing": false,
            "scan_end": 1625566340,
            "haskb": true,
            "hasaudittrail": false,
            "scanner_start": null,
            "scanner_end": null
        },
        "hosts": [
            {
                "asset_id": 2,
                "host_id": 2,
                "uuid": "d84f2b72-19b6-4b8d-b6fc-ea4d1de25ea0",
                "hostname": "172.30.202.196",
                "progress": "100-100/200-200",
                "scanprogresscurrent": 100,
                "scanprogresstotal": 100,
                "numchecksconsidered": 100,
                "totalchecksconsidered": 100,
                "severitycount": {
                    "item": [
                        {
                            "count": 236,
                            "severitylevel": 0
                        },
                        {
                            "count": 1,
                            "severitylevel": 1
                        },
                        {
                            "count": 27,
                            "severitylevel": 2
                        },
                        {
                            "count": 0,
                            "severitylevel": 3
                        },
                        {
                            "count": 0,
                            "severitylevel": 4
                        }
                    ]
                },
                "severity": 264,
                "score": 2946,
                "info": 236,
                "low": 1,
                "medium": 27,
                "high": 0,
                "critical": 0,
                "host_index": 0
            }
        ],
        "vulnerabilities": [
            {
                "count": 63,
                "plugin_id": 10736,
                "plugin_name": "DCE Services Enumeration",
                "severity": "High",
                "plugin_family": "Windows",
                "vuln_index": 1
            }
        ],
        "comphosts": [],
        "compliance": [],
        "history": [
            {
                "history_id": 14167191,
                "owner_id": 2,
                "creation_date": 1625565548,
                "last_modification_date": 1625566340,
                "uuid": "e87030dd-41e8-4598-8dc0-06e4be3aeda5",
                "type": "remote",
                "status": "completed",
                "scheduler": 0,
                "alt_targets_used": false,
                "is_archived": false
            }
        ],
        "notes": [],
        "remediations": {
            "num_cves": 8,
            "num_hosts": 1,
            "num_remediated_cves": 0,
            "num_impacted_hosts": 0,
            "remediations": []
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if scan is finished and at least one endpoint was found (is_success = true):** "Successfully executed scan on the following endpoints: {entity.identifier}  
******if scan is finished and one endpoint not found (is_success = true):** "Action wasn't able to find the following endpoints in Tenable Vulnerability Management: {entity.identifier}  
******if no endpoints were found (is_success = false):** "Provided endpoints were not found in Tenable Vulnerability Management"  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Scan Endpoints". Reason: {0}''.format(error.Stacktrace)******If Policy is not found:** "Error executing action "Scan Endpoints". Reason: Policy {policy name} wasn't found in Tenable Vulnerability Management. Please check the spelling''.******If Scanner is not found:** "Error executing action "Scan Endpoints". Reason: Scanner {scan name} wasn't found in Tenable Vulnerability Management. Please check the spelling''.******If timeout:** "Error executing action "Scan Endpoints". Reason: Timeout was reached. Latest status: {status}".******If status is "aborted", "canceled", "paused", "stopped":** "Error executing action "Scan Endpoints". Reason: The scan was "{status}"". | General  
Case Wall | **Name:** __Scan Results**Columns:** ID Name Severity Family Count  | General  
  
### List Scanners

#### Description

List available scanners in Tenable Vulnerability Management.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among items and if "Contains" is selected, action will try to find items that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Scanners To Return | Integer | 50 | No | Specify how many scanners to return. Default: 50. Max: 100.  
  
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
           "scanners": [
            {
                "creation_date": 1627296891,
                "distro": "es7-x86-64",
                "engine_version": "18.15.0",
                "group": false,
                "hostname": "scaner",
                "id": 200394,
                "ip_addresses": [
                    "172.30.202.207"
                ],
                "key": "6201c49ba806af3cdc8611973b7831145c73ab3d31eb680c5709f3d16eca03e5",
                "last_connect": 1627299143,
                "last_modification_date": 1627298226,
                "linked": 1,
                "loaded_plugin_set": "202107260512",
                "name": "scanner-name",
                "network_name": "Default",
                "num_hosts": 0,
                "num_scans": 0,
                "num_sessions": 0,
                "num_tcp_sessions": 0,
                "owner": "system",
                "owner_id": 1,
                "owner_name": "system",
                "owner_uuid": "3a15b6cd-9412-4274-9801-2c4848dff142",
                "platform": "LINUX",
                "pool": false,
                "scan_count": 0,
                "shared": 1,
                "source": "service",
                "status": "on",
                "timestamp": 1627298226,
                "type": "managed",
                "ui_build": "271",
                "ui_version": "8.15.0",
                "user_permissions": 128,
                "uuid": "3b984f25-6e4b-4d1f-8ad7-8ac403ab8552",
                "remote_uuid": "c5a26121-c728-5986-1077-2eb50f187e31fb69854e12682a88",
                "supports_remote_logs": true,
                "supports_webapp": false
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if found results (is_success = true):** "Successfully found scanners for the provided criteria in Tenable Vulnerability Management.  
******if not found results (is_success = true):** "No scanners were found for the provided criteria in Tenable Vulnerability Management.  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Scanners". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** Available Scanners**Columns:** Name TypeStatus  | General  
  
## Connector

### Tenable IO - Vulnerabilities Connector

#### Description

Pull vulnerabilities from Tenable Vulnerability Management.

**Note:** The connector works with plugin families in whitelist.

#### Configure Tenable IO - Vulnerabilities Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API root | String | https://cloud.tenable.com |  | API Root of the Tenable Vulnerability Management instance.  
Access Key | Password |  | Yes | Access Key of the Tenable Vulnerability Management instance.  
Secret Key | Password |  | Yes | Secret Key of the Tenable Vulnerability Management instance.  
Lowest Severity To Fetch | String | Medium | No | Lowest severity that will be used to fetch vulnerabilities. If nothing is provided, the connector will fetch all vulnerabilities. Possible values: Info, Low, Medium, High, Critical  
Status Filter | CSV | open, reopened. | No | Status filter for the connector. It works with comma-separated values. If nothing is provided, the connector will ingest vulnerabilities with "open", "reopened" statuses. Possible values: open, reopened, fixed.  
Max Days Backwards | Integer | 30 | No | Amount of days from where to fetch vulnerabilities. Default: 30 days. Note: this parameter will return vulnerabilities that were opened/reopened/fixed in the timeframe that is specified in "Max Days Backwards".  
Grouping Mechanism | String | Host | Yes | Grouping mechanism that will be used to create Google SecOps alerts. Possible values: Host, Vulnerability, None.If Host is provided, the connector will create 1 Google SecOps alert containing all of the vulnerabilities per chunk related to the host. If Vulnerability is provided, the connector will create 1 Google SecOps alert containing information about all of the hosts that have that vulnerability in the scope of 1 chunk. If None or invalid value is provided, the connector will create a new Google SecOps alert for each separate vulnerability per host.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Tenable Vulnerability Management server is valid.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
