---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stellar-cyber-starlight/
title: Stellar Cyber Starlight \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:30.671199+00:00
---

# Stellar Cyber Starlight  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stellar-cyber-starlight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stellar Cyber Starlight

This document provides guidance on how to integrate Stellar Cyber Starlight with Google SecOps.

## Product Use Cases

  1. Ingest Stellar Cyber Starlight security events to use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform searches in Stellar Cyber Starlight.



## Product Permission

Basic auth (username:api_key)

## Configure Stellar Cyber Starlight integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://{ip address}/connect/api/ | Yes | API Root of the Stellar Cyber Starlight instance.  
Username | String | N/A | Yes | Username of the Stellar Cyber Starlight account.  
API Key | Password | N/A | No | API Key of the Stellar Cyber Starlight account. This parameter was used for Basic Authentication. If both `API Key` and `API Token` are provided, the `API Token` is prioritized.  
API Token | Password | N/A | No | API Token of the Stellar Cyber Starlight account. This parameter is used for JWT Authentication. If both `API Key` and `API Token` are provided, the `API Token` is prioritized.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verify the SSL certificate for the connection to the Stellar Cyber Starlight server is valid  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Stellar Cyber Starlight with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully connected to the Stellar Cyber Starlight server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
****_If not successful:_ Print "Failed to connect to the Stellar Cyber Starlight server! Error is {0}".format(exception.stacktrace) _If 401 for API token:_ Print "Failed to connect to the Stellar Cyber Starlight server. Invalid API token provided or username. Please validate credentials." _If 401 for API key:_ Print "Failed to connect to the Stellar Cyber Starlight server. Invalid API key or username provided. Please validate credentials." | General  
  
### Simple Search

#### Description

Perform simple search in Stellar Cyber Starlight.

#### Known Indexes

Name | Index  
---|---  
Assets | aella-assets-*  
AWS Events | aella-cloudtrail-*  
Linux Events | aella-audit-*  
ML-IDS/Malware Detection Events | aella-maltrace-*  
Monitoring | aella-ade-*  
Scans | aella-scan-*  
Security Events | aella-ser-*  
SNMP | aella-perf-*  
Syslog | aella-syslog-*  
Traffic | aella-adr-*  
Users | aella-users-*  
Windows Events | aella-wineventlog-*  
  
#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Index | String | N/A | Yes | Specify in which index do you want to search. You can find a list of known indexes in the documentation.  
Query | String | N/A | Yes | Specify query filter for the search.  
Max Results To Return | Integer | 50 | No | Specify how many results to return in response.  
Sort Field | String | N/A | No | Specify the field, which should be used for sorting.  
Sort Order | DDL | DescendingPossible Values:  
AscendingDescending  
| No | Specify the sort order for the result.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
                    "_index": "aella-ser-1594316167944-",
                    "_type": "amsg",
                    "_id": "LzfKNHMByqrLS2zLF9bf",
                    "_score": null,
                    "_source": {
                        "actual": 1,
                        "advanced": 2,
                        "aella_tuples": "172.30.202.208.52.8.234.27.80.67",
                        "anomaly_id": "job024_anomalous_user_agent-2020.07.09",
                        "appid": 67,
                        "appid_family": "Web",
                        "appid_name": "http",
                        "appid_stdport": "yes",
                        "days_silent": 14,
                        "detected_field": "metadata.request.user_agent",
                        "detected_value": "curl/7.47.0",
                        "detector_index": 0,
                        "doc_ids": [],
                        "dscp_name": "Best Effort",
                        "dstip": "52.8.234.27",
                        "dstip_geo": {
                            "city": "San Jose",
                            "countryCode": "US",
                            "countryName": "United States",
                            "latitude": 37.3388,
                            "longitude": -121.8914,
                            "region": "California"
                        },
                        "dstip_geo_point": "37.3388,-121.8914",
                        "dstip_host": "dl.stellarcyber.ai",
                        "dstip_reputation": "Good",
                        "dstip_type": "public",
                        "dstmac": "e8:1c:ba:4c:37:be",
                        "dstport": 80,
                        "duration": 605,
                        "end_reason": 4,
                        "end_time": 1594318194011,
                        "engid": "ad42005056a204db",
                        "engid_gateway": "",
                        "engid_name": "siemplify-sensor",
                        "event_category": "network",
                        "event_name": "user_agent_anomaly",
                        "event_score": 54,
                        "event_source": "rare_ml",
                        "event_status": "New",
                        "event_type": "conn",
                        "fidelity": 99,
                        "flow_score": 100,
                        "inbytes_delta": 2323,
                        "inbytes_total": 2323,
                        "inpkts_delta": 5,
                        "locid": "unassigned location",
                        "metadata": {
                            "request": {
                                "host": "dl.stellarcyber.ai",
                                "index": 1,
                                "method": "GET",
                                "server": "dl.stellarcyber.ai",
                                "uri": "/ubuntu/apt.gpg.key",
                                "user_agent": "curl/7.47.0"
                            },
                            "response": {
                                "code": 200,
                                "file_type": "data",
                                "index": 1,
                                "mime_type": "application/octet-stream",
                                "processing_time": 0,
                                "response_time": 199
                            }
                        },
                        "metadata.request.user_agent": "\"curl/7.47.0\"",
                        "msg_class": "interflow_traffic",
                        "msg_origin": {
                            "source": "network_sensor"
                        },
                        "msgtype": 4,
                        "msgtype_name": "startend",
                        "netid": 0,
                        "netid_name": "vlan0",
                        "obsid": 2887699152,
                        "orig_id": "4TfENHMByqrLS2zLZtWQ",
                        "orig_index": "aella-adr-1594315890054-",
                        "outbytes_delta": 570,
                        "outbytes_total": 570,
                        "outpkts_delta": 7,
                        "port_name": "ethernet0",
                        "processing_time": 0,
                        "proto": 6,
                        "proto_name": "tcp",
                        "response_time": 199,
                        "severity": 30,
                        "src_tuples": "00:50:56:a2:04:db.0.172.30.202.208",
                        "srcip": "172.30.202.208",
                        "srcip_geo": {
                            "city": "Unknown",
                            "countryCode": "UN",
                            "countryName": "Unknown"
                        },
                        "srcip_geo_point": "0.0,0.0",
                        "srcip_host": "172.30.202.208",
                        "srcip_reputation": "Good",
                        "srcip_type": "private",
                        "srcmac": "00:50:56:a2:04:db",
                        "srcport": 42344,
                        "start_time": 1594317594889,
                        "state": "Closed",
                        "tcp_rtt": 203,
                        "tenant_id": "",
                        "tenantid": "",
                        "threat_score": 0,
                        "timestamp": 1594318142374,
                        "tos": 0,
                        "totalbytes": 2893,
                        "totalpackets": 12,
                        "typical": 0,
                        "url": "dl.stellarcyber.ai/ubuntu/apt.gpg.key",
                        "url_reputation": "Good",
                        "vlan": 0,
                        "write_time": 1594318526414
                    },
                    "sort": [
                        1594318142374
                    ]
                }
    

##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If status code == 200 (is_success = true)_ Print "Successfully executed search in Stellar Cyber Starlight."****_If other status code (is_success=false):_ Print "Action wasn't able to execute search in Stellar Cyber Starlight. Reasons: {0}.(new line separated list of error/root_cause/reason.)  
******The action should fail and stop a playbook execution:**  
****_Ii fatal error, like wrong credentials, no connection to the_ ****_server, other:_ Print "Error executing action "Simple Search". Reason: {0}''.format(error.Stacktrace) | General  
  
### Advanced Search

#### Description

Perform advanced search in Stellar Cyber Starlight.

#### Known Indexes

Name | Index  
---|---  
Assets | aella-assets-*  
AWS Events | aella-cloudtrail-*  
Linux Events | aella-audit-*  
ML-IDS/Malware Detection Events | aella-maltrace-*  
Monitoring | aella-ade-*  
Scans | aella-scan-*  
Security Events | aella-ser-*  
SNMP | aella-perf-*  
Syslog | aella-syslog-*  
Traffic | aella-adr-*  
Users | aella-users-*  
Windows Events | aella-wineventlog-*  
  
#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Index | String | N/A | Yes | Specify in which index do you want to search. You can find a list of known indexes in the documentation.  
DSL Query | String | { "size": 1, "from": 0, "query": { "match_all": {} }, "sort": [ { "timestamp": { "order": "asc" } } ]}  
| Yes | Specify the JSON object of the DSL query that you want to execute.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
                    "_index": "aella-ser-1594316167944-",
                    "_type": "amsg",
                    "_id": "LzfKNHMByqrLS2zLF9bf",
                    "_score": null,
                    "_source": {
                        "actual": 1,
                        "advanced": 2,
                        "aella_tuples": "172.30.202.208.52.8.234.27.80.67",
                        "anomaly_id": "job024_anomalous_user_agent-2020.07.09",
                        "appid": 67,
                        "appid_family": "Web",
                        "appid_name": "http",
                        "appid_stdport": "yes",
                        "days_silent": 14,
                        "detected_field": "metadata.request.user_agent",
                        "detected_value": "curl/7.47.0",
                        "detector_index": 0,
                        "doc_ids": [],
                        "dscp_name": "Best Effort",
                        "dstip": "52.8.234.27",
                        "dstip_geo": {
                            "city": "San Jose",
                            "countryCode": "US",
                            "countryName": "United States",
                            "latitude": 37.3388,
                            "longitude": -121.8914,
                            "region": "California"
                        },
                        "dstip_geo_point": "37.3388,-121.8914",
                        "dstip_host": "dl.stellarcyber.ai",
                        "dstip_reputation": "Good",
                        "dstip_type": "public",
                        "dstmac": "e8:1c:ba:4c:37:be",
                        "dstport": 80,
                        "duration": 605,
                        "end_reason": 4,
                        "end_time": 1594318194011,
                        "engid": "ad42005056a204db",
                        "engid_gateway": "",
                        "engid_name": "siemplify-sensor",
                        "event_category": "network",
                        "event_name": "user_agent_anomaly",
                        "event_score": 54,
                        "event_source": "rare_ml",
                        "event_status": "New",
                        "event_type": "conn",
                        "fidelity": 99,
                        "flow_score": 100,
                        "inbytes_delta": 2323,
                        "inbytes_total": 2323,
                        "inpkts_delta": 5,
                        "locid": "unassigned location",
                        "metadata": {
                            "request": {
                                "host": "dl.stellarcyber.ai",
                                "index": 1,
                                "method": "GET",
                                "server": "dl.stellarcyber.ai",
                                "uri": "/ubuntu/apt.gpg.key",
                                "user_agent": "curl/7.47.0"
                            },
                            "response": {
                                "code": 200,
                                "file_type": "data",
                                "index": 1,
                                "mime_type": "application/octet-stream",
                                "processing_time": 0,
                                "response_time": 199
                            }
                        },
                        "metadata.request.user_agent": "\"curl/7.47.0\"",
                        "msg_class": "interflow_traffic",
                        "msg_origin": {
                            "source": "network_sensor"
                        },
                        "msgtype": 4,
                        "msgtype_name": "startend",
                        "netid": 0,
                        "netid_name": "vlan0",
                        "obsid": 2887699152,
                        "orig_id": "4TfENHMByqrLS2zLZtWQ",
                        "orig_index": "aella-adr-1594315890054-",
                        "outbytes_delta": 570,
                        "outbytes_total": 570,
                        "outpkts_delta": 7,
                        "port_name": "ethernet0",
                        "processing_time": 0,
                        "proto": 6,
                        "proto_name": "tcp",
                        "response_time": 199,
                        "severity": 30,
                        "src_tuples": "00:50:56:a2:04:db.0.172.30.202.208",
                        "srcip": "172.30.202.208",
                        "srcip_geo": {
                            "city": "Unknown",
                            "countryCode": "UN",
                            "countryName": "Unknown"
                        },
                        "srcip_geo_point": "0.0,0.0",
                        "srcip_host": "172.30.202.208",
                        "srcip_reputation": "Good",
                        "srcip_type": "private",
                        "srcmac": "00:50:56:a2:04:db",
                        "srcport": 42344,
                        "start_time": 1594317594889,
                        "state": "Closed",
                        "tcp_rtt": 203,
                        "tenant_id": "",
                        "tenantid": "",
                        "threat_score": 0,
                        "timestamp": 1594318142374,
                        "tos": 0,
                        "totalbytes": 2893,
                        "totalpackets": 12,
                        "typical": 0,
                        "url": "dl.stellarcyber.ai/ubuntu/apt.gpg.key",
                        "url_reputation": "Good",
                        "vlan": 0,
                        "write_time": 1594318526414
                    },
                    "sort": [
                        1594318142374
                    ]
                }
    

##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If status code == 200 (is_success = true)_ Print "Successfully executed search in Stellar Cyber Starlight."****_If other status code (is_success=false):_ Print "Action wasn't able to execute search in Stellar Cyber Starlight. Reasons: {0}.(new line separated list of error/root_cause/reason.)  
******The action should fail and stop a playbook execution:**  
****_Ii fatal error, like wrong credentials, no connection to the_ ****_server, other:_ Print "Error executing action "Advanced Search". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Security Event

#### Description

Update security event in Stellar Cyber Starlight.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Index | String | N/A | Yes | Specify the index of the security event.  
ID | String | N/A | Yes | Specify the ID of the security event.  
Status | DDL | Select OnePossible Values:Select OneNew  
In Progress  
Ignored  
Closed | No | Specify the new status for the security event.  
Comment | String | N/A | No | Specify a comment for the security event.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If status code == 200 (is_success = true):** "Successfully updated event {event_id} in Stellar Cyber Starlight.".  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Update Security Event". Reason: {0}''.format(error.Stacktrace)  
******If other status code (is_success=false):** Error executing action "Update Security Event". Reason: {text from response}  
******If none of the parameters are provided:** Error executing action "Update Security Event". Reason: at least one of the "Status", "Comment" should have a value. | General  
  
## Connectors

### Stellar Cyber Starlight - Security Events Connector

#### Description

Pull security events from Stellar Cyber Starlight.

**Note:** The dynamic list works with the Google SecOps alert name, which can be either `event_category: event_name` or `_source_xdr_event_xdr_killchain_stage:_source_xdr_event_name`.

#### Configure Stellar Cyber Starlight - Security Events Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_data.event_name | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{ip}/connect/api/ | Yes | API Root of the Stellar Cyber Starlight instance.  
Username | String | N/A | Yes | Username of the Stellar Cyber Starlight account.  
API Key | Password | N/A | No | API Key of the Stellar Cyber Starlight account. This parameter was used for Basic Authentication. If both `API Key` and `API Token` are provided, the `API Token` is prioritized.  
API Token | Password | N/A | No | API Token of the Stellar Cyber Starlight account. This parameter is used for JWT Authentication. If both `API Key` and `API Token` are provided, the `API Token` is prioritized.  
Lowest Severity To Fetch | Integer | 50 | Yes | Lowest severity that will be used to fetch events.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max Events To Fetch | Integer | 50 | No | How many events to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Stellar Cyber Starlight server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Padding Period | Integer | 0 | No | Padding period in hours for the connector execution.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
