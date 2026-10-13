---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vectra/
title: Vectra \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:00.277765+00:00
---

# Vectra  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vectra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Vectra

This document provides guidance on how to integrate Vectra with Google SecOps.

## Use Cases

  1. Ingest Vectra detections to use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform enrichment actions - get data from Vectra to enrich data in Google SecOps Alerts.



## Product Permission

In order to get an API token, you have to go to the Profile page and copy it.

![API token location](https://docs.cloud.google.com/static/chronicle/images/integrations/vectra-api-token.png)

## Configure Vectra integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://{address}:{port} | Yes | API root of the Vectra server.  
API Token | Password | N/A | Yes | API token of the Vectra account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Vectra server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Vectra with parameters provided at the integration configuration page in the Google Security Operations Marketplace tab.

#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully connected to the Vectra server with the provided connection parameters!"  
**The action should fail and stop a playbook execution:**  
_If not successful:_ Print "Failed to connect to the Vectra server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address.

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
Vectra_id | results/id | When available in JSON  
Vectra_name | results/name | When available in JSON  
Vectra_state | results/state | When available in JSON  
Vectra_threat | results/threat | When available in JSON  
Vectra_certainty | results/certainty | When available in JSON  
Vectra_ip | results/last_source | When available in JSON  
Vectra_tags | Space-separated {results/tags} | When available in JSON  
Vectra_note | results/note | When available in JSON  
Vectra_url | results/url | When available in JSON  
Vectra_last_modified | results/last_modified | When available in JSON  
Vectra_groups | Space-separated {results/groups} | When available in JSON  
Vectra_is_key_asset | results/is_key_asset | When available in JSON  
Vectra_has_active_traffic | results/has_active_traffic | When available in JSON  
Vectra_is_targeting_key_asset | results/is_targeting_key_asset | When available in JSON  
Vectra_privilege_level | results/privilege_level | When available in JSON  
Vectra_previous_ip | Space-separated {results/previous_ips} | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
                "id": 131,
                "name": "DESKTOP-DAIOS7J",
                "active_traffic": false,
                "has_active_traffic": false,
                "t_score": 0,
                "threat": 0,
                "c_score": 0,
                "certainty": 0,
                "severity": null,
                "last_source": "10.0.2.68",
                "ip": "10.0.2.68",
                "previous_ips": [],
                "last_detection_timestamp": "2019-10-08T17:13:57Z",
                "key_asset": false,
                "is_key_asset": false,
                "state": "inactive",
                "targets_key_asset": false,
                "is_targeting_key_asset": false,
                "detection_set": [],
                "host_artifact_set": [
                    {
                        "type": "netbios",
                        "value": "DESKTOP-DAIOS7J",
                        "source": null,
                        "siem": false
                    }
                ],
                "sensor": "YLq09aHU",
                "sensor_name": "Vectra X",
                "tags": [],
                "note": null,
                "note_modified_by": null,
                "note_modified_timestamp": null,
                "url": "https://70.54.200.216:64443/api/v2.1/hosts/131",
                "host_url": "https://70.54.200.216:64443/api/v2.1/hosts/131",
                "last_modified": "2020-02-12T13:41:51Z",
                "assigned_to": null,
                "assigned_date": null,
                "groups": [],
                "has_custom_model": false,
                "privilege_level": null,
                "privilege_category": null,
                "probable_owner": null,
                "detection_profile": null,
                "host_session_luids": [],
                "host_luid": "e0M-jygN"
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful_ ****_and at least one of the provided entities were enriched (is_success = true):_ Print "Successfully enriched the following endpoints from Vectra: \n {0}".format(entity.identifier list)  
_If action found multiple matches in Vectra for some Google SecOps entities, first match was taken to enrich endpoint:_ Print "Multiple matches were found in Vectra, taking first match for the following entities:/n {0}".format(entity.identifiers list)_If Ifail to enrich specific entities(is_success = true):_ Print "No entities were enriched."**The action should fail and stop a playbook execution:**  
_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich Endpoint". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Tags

#### Description

Add tags to the endpoint or detection in Vectra.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Item Type | Dropdown | Endpoint  
Possible values:  
EndpointDetection | Yes | Select to which item type you want to add tags.  
Item ID | String | N/A | Yes | Specify ID of the detection/endpoint.  
Tags | CSV | N/A | Yes | Specify what tags you want to add to detection/endpoint. Tags should be separated by comma, for example: tag1, tag2.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If detection/endpoint is found and tags were successfully updated (is_success = true):_ Print "Successfully added tags {0} to {1} with ID {2}.format(tags, Item Type, Item ID)  
_If detection/endpoint was found, but tags were not added (is_success=False):_ Print "Action wasn't able to add tags {0} to {1} with ID {2}. Reason: {3}. format(tags, Item Type, Item ID, tags parameter from response)"._If detection/endpoint was not found (is_success=False):_ Print "{0} with ID {1} was not found.format(Item Type, Item ID)."_II is_success=false without a specific situation and it's not a critical error:_ Print "Action wasn't able to add tags to {0} with ID {1}.format(Item Type, Item ID)":**The action should fail and stop a playbook execution:**  
_If fatal error (wrong credentials, connection error, action crashes):_ Print "Error executing action "Add Tags". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove Tags

#### Description

Remove tags from the endpoint or detection in Vectra.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Item Type | Dropdown | Endpoint  
Possible values:  
EndpointDetection | Yes | Select from which item type you want to remove tags.  
Item ID | String | N/A | Yes | Specify ID of the detection/endpoint.  
Tags | CSV | N/A | Yes | Specify what tags you want to remove from detection/endpoint. Tags should be separated by comma, for example: tag1, tag2.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If detection/endpoint is found and tags were successfully updated (is_success = true):_ Print "Successfully removed tags {0} from {1} with ID {2}.format(tags, Item Type, Item ID)  
_If detection/endpoint was not found (is_success=False):_ Print "{0} with ID {1} was not found.".format(Item Type, Item ID)."_If detection/endpoint was found, but tag is not found (is_success=False):_ Print "Tags {0} don't exist in {1} with ID {2}.".format(list of tags that were not found separated by comma, Item Type, Item ID)."_If is_success=false without a specific situation and it's not a critical error:_ Print "Action wasn't able to remove tags from {0} with ID {1}.format(Item Type, Item ID)":**The action should fail and stop a playbook execution:**  
_If fatal error (wrong credentials, connection error, action crashes):_ Print "Error executing action "Remove Tags". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Note

#### Description

Update note for the endpoint or detection.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Item Type | Dropdown | Endpoint  
Possible values:  
EndpointDetection | Yes | Select on which item type you want to update a note.  
Item ID | String | N/A | Yes | Specify ID of the detection/endpoint.  
Note | String | N/A | Yes | Specify what note you want to have on the detection/endpoint.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If detection/endpoint is found and note was successfully updated (is_success = true):_ Print "Successfully updated note on {1} with ID {2}.format(Item Type, Item ID)  
_If detection/endpoint was not found (is_success=False):_ Print "{0} with ID {1} was not found.".format(Item Type, Item ID)."_If is_success=false without a specific situation and it's not a critical error:_ Print "Action wasn't able to update note on {0} with ID {1}.format(Item Type, Item ID)":**The action should fail and stop a playbook execution:**  
_If fatal error (wrong credentials, connection error, action crashes):_ Print "Error executing action "Update Note". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Detection Status

#### Description

Update status of the detection.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Detection ID | Integer | N/A | Yes | Specify the detection ID on which you want to update the status.  
Status | DDL | Fixed  
Possible Values:FixedActive  
| Yes | Specify what status to set on the detection.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:**_If detection is found and status was successfully updated (is_success = true):_ Print "Successfully updated status to '{0}' on detection with ID {1}.format(Status, Detection ID)   
_If detection was not found (is_success=False):_ Print "Detection with ID {1} was not found.".format(Detection ID)."_If is_success=false without a specific situation and it's not a critical error:_ Print "Action wasn't able to update status on detection with ID {1}.format(detection ID)":**The action should fail and stop a playbook execution:**  
_If fatal error (wrong credentials, connection error, action crashes):_ Print "Error executing action "Update Detection Status". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Triage Rule Details

#### Description

Get detailed information about triage rules.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Triage Rule IDs | Integer | N/A | Yes | Specify a comma-separated list of triage rule IDs. Example: 28,29  
Create Insights | Checkbox | True | Yes | If enabled, action will create a separate insight for every processed triage rule.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Insight

Insight Title | Insight Description  
---|---  
"Triage Rule {0}".format(triage_rule) | "Detection Category: {0}\n Triage Category: {1}\n Detection: {2} \n Description: {3}".format(detection_category, triage_category, detection, description)  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": 28,
        "url": "https://api.demo.vectranetworks.com/api/v2.1/rules/28",
        "description": "whatever",
        "enabled": true,
        "created_timestamp": "2020-10-01T17:21:19Z",
        "last_timestamp": "2020-10-01T17:21:19Z",
        "is_whitelist": false,
        "priority": 1,
        "active_detections": 1,
        "total_detections": 1,
        "template": false,
        "additional_conditions": {
            "OR": [
                {
                    "AND": [
                        {
                            "ANY_OF": {
                                "field": "remote1_ip",
                                "values": [
                                    {
                                        "url": null,
                                        "value": "35.166.75.118",
                                        "label": "35.166.75.118"
                                    }
                                ],
                                "groups": [],
                                "label": "C&C Server IP"
                            }
                        }
                    ]
                }
            ]
        },
        "source_conditions": {
            "OR": [
                {
                    "AND": [
                        {
                            "ANY_OF": {
                                "field": "host",
                                "values": [
                                    {
                                        "url": "https://api.demo.vectranetworks.com/api/v2.1/hosts/142",
                                        "value": 142,
                                        "label": "IP-10.10.100.10"
                                    }
                                ],
                                "groups": [],
                                "label": "Host"
                            }
                        }
                    ]
                }
            ]
        },
        "detection_category": "COMMAND & CONTROL",
        "triage_category": "triage rule 1",
        "detection": "Hidden HTTPS Tunnel"
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful and at least one of the provided rule ids were enriched (is_success = true):_ Print "Successfully retrieved information about the following triage rules from Vectra: \n {0}".format(processed rule ids)_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to retrieve information about the following triage rules\n: {0}".format(not processed rule ids)_If fail to enrich for all entities (is_success = false):_ Print "No information was retrieved about the triage rules."**The action should fail and stop a playbook execution:**  
_If fatal error (wrong credentials, connection error, action crashes):_ Print "Error executing action "Get Triage Rule Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Triage Rules Details**Table Columns:** ID (mapped as id)Enabled (mapped as enabled)Detection Category (mapped as detection_category)Triage Category (mapped as triage_category)Detection (mapped as detection)Whitelist (mapped as is_whitelist)Priority (mapped as priority)Created At (mapped as created_timestamp) | General  
  
## Connectors

### Vectra - Detections Connector

#### Configure Vectra - Detections Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:x:x | Yes | API root of the Vectra server.  
API Token | Password | N/A | Yes | API token of the Vectra account.  
Lowest Threat Score To Fetch | Integer | 50 | Yes | Lowest threat score that will be used to fetch detections. Min: 0 Max: 100  
Lowest Certainty Score To Fetch | Integer | 0 | No | Lowest certainty score that will be used to fetch detections. Min: 0 Max: 100  
Category Filter | Comma-separated values | Command and Control,Botnet ,Reconnaissance,Lateral Movement,Exfiltration,Info |  | Specify which categories of detections to ingest into Google SecOps. Possible values: Command and Control Botnet Reconnaissance Lateral Movement Exfiltration Info  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch threats.  
Max Detections To Fetch | Integer | 25 | No | How many detections to process per one connector iteration. Limit is 5000. This is a Vectra limitation.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Vectra server is valid.  
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
