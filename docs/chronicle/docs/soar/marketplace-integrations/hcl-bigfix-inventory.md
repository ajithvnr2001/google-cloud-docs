---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/hcl-bigfix-inventory/
title: HCL BigFix Inventory \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:19.483858+00:00
---

# HCL BigFix Inventory  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/hcl-bigfix-inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HCL BigFix Inventory

This document provides guidance on how to integrate HCL BigFix Inventory with Google SecOps.

## Configure HCL BigFix Inventory integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{{ip address}}:9081 | Yes | API root of the HCL BigFix Inventory instance.  
API Token | Password | N/A | Yes | API Token of the HCL BigFix Inventory account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the HCL BigFix Inventory server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Where to find API Token

To view the token, log in to BigFix Inventory, hover the cursor over ![User
icon](https://docs.cloud.google.com/static/chronicle/images/integrations/hcl-big-fix-icon.png), and click **Profile**. Then, click **Show token**.

## Uses Cases

Enrich entities.

## Actions

### Ping

#### Description

Test connectivity to HCL BigFix Inventory with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the HCL BigFix Inventory server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the HCL BigFix Inventory server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from HCL BigFix Inventory. Supported entities: Hostname, IP Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Custom Fields | CSV | N/A | No | Specify a comma-separated list of fields that needs to be returned in addition to the ones that are returned by default.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
      "id": 1,
      "bigfix_id": 1055452,
      "computer_group_id": 0,
      "name": "BIGFIX-SRV",
      "dns_name": "BIGFIX-SRV.bigfix.local",
      "ip_address": [
          "172.30.202.178"
      ],
      "os": "Win2016 10.0.14393.5066 (1607)",
      "os_type": "WINDOWS",
      "first_seen": "2022-05-11T07:22:30Z",
      "last_seen": "2022-05-23T06:58:08Z",
      "is_deleted": 0,
      "deletion_date": null,
      "is_managed_by_vm_manager": 0,
      "computer_health": {
          "agent_version": "10.0.6.84",
          "catalog_version": 2638693,
          "is_catalog_scan_successful": true,
          "is_filesys_scan_successful": true,
          "is_idtag_scan_successful": true,
          "is_low_on_disk_space": false,
          "is_missing_prereqs": false,
          "is_out_of_date": false,
          "is_out_of_sync": false,
          "is_package_scan_successful": true,
          "last_scan_attempt": "2022-05-18T07:59:39Z"
      },
      "computer_hardware": {
          "shared_pool_id": null,
          "system_model": "VMware7,1",
          "cluster_name": null,
          "cluster_cores_count": null,
          "partition_cores": "8.0",
          "status": "4",
          "server_id": 1,
          "server_name": "TLM_VM_4222eeb3-28a8-d59e-b8a2-d1a70361fed4",
          "server_serial_number": "TLM_VM_4222eeb3-28a8-d59e-b8a2-d1a70361fed4",
          "server_type": "-",
          "server_vendor": "-",
          "server_model": "-",
          "node_total_processors": 1,
          "server_cores": 8,
          "pvu_per_core": 120,
          "default_pvu_value": "0",
          "parent_hostname": null
      }
    }
    

##### Entity Enrichment - Prefix HCLBigFixInv_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
name | name | When available in JSON  
dns_name | dns_name | When available in JSON  
ip_address | CSV of ip_address | When available in JSON  
os | os | When available in JSON  
first_seen | first_seen | When available in JSON  
last_seen | last_seen | When available in JSON  
is_deleted | is_deleted | When available in JSON  
deletion_date | deletion_date | When available in JSON  
last_scan_attempt | computer_health/last_scan_attempt | When available in JSON  
is_out_of_date | computer_health/is_out_of_date | When available in JSON  
is_out_of_sync | computer_health/is_out_of_sync | When available in JSON  
is_missing_prereqs | computer_health/is_missing_prereqs | When available in JSON  
is_low_on_disk_space | computer_health/is_low_on_disk_space | When available in JSON  
  
##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from HCL BigFix Inventory: {entity.identifier}." _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from HCL BigFix Inventory: {entity.identifier}." _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier} **Table Columns:**

  * Key
  * Value

| Entity  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
