---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-cortex-xdr/
title: Integrate Palo Alto Cortex XDR with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:28:36.688365+00:00
---

# Integrate Palo Alto Cortex XDR with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-cortex-xdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Palo Alto Cortex XDR with Google SecOps

**Important:** This integration refers to Palo Alto Networks Cortex XDR.

This document provides guidance on how to integrate Palo Alto Cortex XDR with Google Security Operations.

## Before you begin

To obtain your Cortex XDR API Key, you must obtain credentials from your Palo Alto Networks Cortex XDR account

Complete the following steps to obtain your Cortex XDR API Key:

  1. Go to **Settings**.
  2. Select + **New Key**.
  3. Choose the type of API Key to generate (**Advanced** **Only**).
  4. Provide a comment that describes the purpose for the API key (Optional).
  5. Select your level of access for this key.
  6. **Generate** the API Key.
  7. Copy the API key, and then click **Done**.



To obtain your Cortex XDR API Key ID:

  1. Go to **API Keys** table > **ID column**.
  2. Note your corresponding **ID** number. This value represents the **x-xdr-auth-id:{key_id}** token.

**Note:** See [Get Started with Cortex XDR APIs](https://cortex-panw.stoplight.io/docs/cortex-xdr/3u3j0e7hcx8t1-get-started-with-cortex-xdr-ap-is), for more information and detailed instructions about generating the API key for this integration.

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | https://api-{fqdn} | Yes | Palo Alto Networks Cortex XDR API Root. **Note:** The FQDN represents a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual FQDN.  
Api Key | Password | N/A | Yes | A unique identifier used as the "Authorization:{key}" header required for authenticating API calls. Depending on your security level, you can generate Advanced API key from your Cortex XDR app.  
Api Key ID | Integer | 3 | Yes | A unique token used to authenticate the API Key. The header used when running an API call is "x-xdr-auth-id:{key_id}".  
Verify SSL | Checkbox | Unchecked | Yes | Option to verify SSL/TLS connection.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Comment To Incident

Use the **Add Comment To Incident** action to add a comment to an incident in in Palo Alto Cortex XDR.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Comment To Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | Required. The ID of the incident to update.  
`Comment` | Required. The comment to add to the incident.  
  
#### Action outputs

The **Add Comment To Incident** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Comment To Incident** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added a comment to an incident with ID COMMENT_ID in Palo Alto XDR.` | The action succeeded.  
`Error executing action "Add Comment To Incident". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Incident** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Hashes to Block List

Use this action to add files, which are unlisted, to a specified block list.

**Note:** Only SH256 format for file hashes is supported.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Comment | String | N/A | No | Provide additional comment that represents additional information regarding the action  
Incident ID | String | N/A | No | Specify the incident ID for which those added hashes are related to  
  
#### Run On

This action runs on the Filehash entity

#### Action Results

This action can provide the results detailed in the following sections.

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    {
    
    "success": ["hashes that were added"],
    
    "already_existed": ["hashes that already existed"]
    
    "failed": ["hashes that failed"]
    
    "unsupported": ["unsupported hashes"]
    
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****For successfully added entities :** "Successfully added the following entities to the Block List: " +successful_entities_list __**For unsuccessful entities:**_****_"Could not add the following entities to the Block List: "+unsuccessful_entities_list.**If one hash of the unsupported type is provided (is_success=true):** The following hashes are unsupported: {unsupported hashes}**If all hashes of the unsupported type is provided (is_success=false):** None of the provided hashes are supported.******The action should fail and stop a playbook execution:**  
****"Failed to perform action "Add Hashes to Blacklist" {0}".format(exception.stacktrace) | General  
  
### Download File

Use the **Download File** action to download files from remote endpoints in Palo Alto XDR.

This action runs on the following Google SecOps entities:

  * `ADDRESS`
  * `HOSTNAME`

**Important:** This action executes asynchronously. You must increase the standard script timeout value within the Google SecOps IDE to ensure the file download complete signal returns successfully.

#### Action inputs

The **Download File** action requires the following parameters:

Parameters | Description  
---|---  
`File Paths` | _Required_ A comma-separated list of absolute file paths on the target endpoint to download.  
`Download Folder Path` | _Required_ The local folder path on the system where the downloaded files should be stored. The default value is `/tmp`.  
`Overwrite` | _Required_ If selected, the action overwrites any existing local file with the same name in the destination folder. Disabled by default.  
`Incident ID` | _Optional_ The ID of the Cortex XDR incident to associate this file download activity with, allowing the results to appear cleanly in the incident timeline.  
`Agent ID` | _Optional_ A comma-separated list of target agent IDs to download the files from. This parameter functions alongside and filters the provided entity context.  
`Unzip File` | _Required_ If selected, the action unzips the downloaded file and saves it in its original format. Otherwise, the file is saved as a zip archive.  
  
#### Action outputs

The **Download File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Download File** action:
    
    
    {
      "Entity": "10.10.10.10",
      "EntityResult": {
        "download_file_path": [
          "/tmp/sample.exe"
        ],
        "errored_file_paths": [
          "/tmp/missing.exe"
        ],
        "errors": {
          "/tmp/missing.exe": "File not found on endpoint"
        }
      }
    }
    

##### Output messages

The **Download File** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded target files from the specified endpoints via Palo Alto Cortex XDR.` | Action succeeded. [cite: 31]  
`Error executing action "Download File". Reason: ERROR_REASON` | Action failed.Check network connectivity, verify endpoint agent states, ensure the script timeout limit is adjusted, or check target file permissions.  
  
##### Script result

The following table describes the values for the script result output when using the **Download File** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich Entities

Enrich Google SecOps Host and IP entities based on the information from the Palo Alto Networks Cortex XDR.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
domain | Returns if it exists in JSON result  
endpoint_name | Returns if it exists in JSON result  
endpoint_type | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
endpoint_version | Returns if it exists in JSON result  
install_date | Returns if it exists in JSON result  
installation_package | Returns if it exists in JSON result  
is_isolated | Returns if it exists in JSON result  
group_name | Returns if it exists in JSON result  
alias | Returns if it exists in JSON result  
active_directory | Returns if it exists in JSON result  
endpoint_status | Returns if it exists in JSON result  
endpoint_id | Returns if it exists in JSON result  
content_version | Returns if it exists in JSON result  
os_type | Returns if it exists in JSON result  
last_seen | Returns if it exists in JSON result  
first_seen | Returns if it exists in JSON result  
users | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    [{
        "EntityResult":
           {
             "domain": "st2.local",
             "endpoint_name": "ST2-PC-1-14",
             "endpoint_type": "AGENT_TYPE_SERVER",
             "ip": null,
             "endpoint_version": "6.1.0.9915",
             "install_date": 1568103207592,
             "installation_package": "papi-test",
             "is_isolated": null,
             "group_name": null,
             "alias": "",
             "active_directory": null,
             "endpoint_status": "DISCONNECTED",
             "endpoint_id": "4ce98b4d8d2b45a9a1d82dc71f0d1304",
             "content_version": "",
             "os_type": "AGENT_OS_WINDOWS",
             "last_seen": 1568103207592,
             "first_seen": 1568103207591,
             "users": ["TEST USER"]
            },
        "Entity": "PC01"
     }]
    

### Execute XQL Search

Use the **Execute XQL Search** action fetch information using XQL in Palo Alto Cortex XDR.

**Note:** This action is asynchronous, the script timeout value for this action should therefore be adjusted in the Google SecOps IDE as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Execute XQL Search** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required. The query to execute in Palo Alto Cortex XDR. Don't provide `limit` as part of the query. The action retrieves this value from `Max Results To Return`.  
`Time Frame` | Optional. The query to execute in Palo Alto Cortex XDR. Don't provide `limit` as part of the query. The action retrieves this value from `Max Results To Return`. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | Optional. The start time for the results in format ISO 8601. If `Custom` is selected for `Time Frame`, this parameter is required.  
`End Time` | Optional. The end time for the results in format ISO 8601. If `Custom` is selected for `Time Frame` and no value is provided, the action uses the current time.  
`Max Results To Return` | Optional. The action appends `limit` to the provided query. The maximum value is`1000`. The default value is `50`.  
  
#### Action outputs

The **Execute XQL Search** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Execute XQL Search** action:
    
    
    {
        "events": [
            {
                "event_id": "AAABmRQvChTmouboArIcKg==",
                "_product": "XDR agent",
                "_time": 1756980296509,
                "_vendor": "PANW",
                "insert_timestamp": 1756980477113,
                "event_type": "NETWORK",
                "event_sub_type": "NETWORK_STREAM_CONNECT_FAILED"
            },
            {
                "event_id": "AAABmRQtb2XmouboArIb1g==",
                "_product": "XDR agent",
                "_time": 1756980191374,
                "_vendor": "PANW",
                "insert_timestamp": 1756980477113,
                "event_type": "NETWORK",
                "event_sub_type": "NETWORK_STREAM_CONNECT_FAILED"
            }
        ]
    }
    

##### Output messages

The **Execute XQL Search** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned results for the query QUERY in Palo Alto XDR.` `No results were found for the query QUERY in Palo Alto XDR.` `Waiting for the search job to finish…` | The action succeeded.  
`Error executing action "Execute XQL Search". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute XQL Search** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Endpoint Agent Report

Get the agent report for an endpoint.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

### Get Incident Details

Use the **Get Incident Details** action to retrieve information about an incident in Palo Alto Cortex XDR.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Incident Details** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | Required. The ID of the incident to return.  
`Lowest Alert Severity` | Optional. The lowest alert severity required for an alert to be included. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`

The default value is `High`.  
`Max Alerts To Return` | Optional. The maximum amount of alerts to return. The maximum value is`1000`. The default value is `50`.  
  
#### Action outputs

The **Get Incident Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Get Incident Details** action:
    
    
    {
        "incident_id": "146408",
        "is_blocked": false,
        "incident_name": null,
        "creation_time": 1756265930000,
        "modification_time": 1756265938000,
        "detection_time": null,
        "status": "new",
        "severity": "medium",
        "description": "'PHP XDebug Session Detection' generated by PAN NGFW",
        "assigned_user_mail": null,
        "assigned_user_pretty_name": null,
        "alert_count": 1,
        "low_severity_alert_count": 0,
        "med_severity_alert_count": 1,
        "high_severity_alert_count": 0,
        "critical_severity_alert_count": 0,
        "user_count": 0,
        "host_count": 0,
        "notes": null,
        "resolve_comment": null,
        "resolved_timestamp": null,
        "manual_severity": null,
        "manual_description": null,
        "xdr_url": "https://xyz.com/incident-view?caseId=146408",
        "starred": true,
        "starred_manually": false,
        "hosts": null,
        "users": [],
        "incident_sources": [
            "PAN NGFW"
        ],
        "rule_based_score": null,
        "predicted_score": 40,
        "manual_score": null,
        "aggregated_score": 40,
        "wildfire_hits": 0,
        "alerts_grouping_status": "Enabled",
        "mitre_tactics_ids_and_names": null,
        "mitre_techniques_ids_and_names": null,
        "alert_categories": [
            "Vulnerability"
        ],
        "original_tags": [
            "DS:PANW/NGFW"
        ],
        "tags": [
            "DS:PANW/NGFW"
        ],
        "network_artifacts": {
            "total_count": 1,
            "data": [
                {
                    "type": "IP",
                    "alert_count": 1,
                    "is_manual": false,
                    "network_domain": null,
                    "network_remote_ip": "0.0.0.0",
                    "network_remote_port": 500,
                    "network_country": "JP"
                }
            ]
        },
        "file_artifacts": {
            "total_count": 0,
            "data": []
        },
        "alerts": [
            {
                "external_id": "7540915192461269271",
                "severity": "medium",
                "matching_status": "UNMATCHABLE",
                "end_match_attempt_ts": null,
                "local_insert_ts": 1756265929231,
                "last_modified_ts": null,
                "bioc_indicator": null,
                "matching_service_rule_id": null,
                "attempt_counter": 0,
                "bioc_category_enum_key": null,
                "case_id": 146408,
                "is_whitelisted": false,
                "starred": true,
                "deduplicate_tokens": "00421ab2ab1a43d089b1f690f8b4e54a",
                "filter_rule_id": null,
            }
        ]
    }
    

##### Output messages

The **Get Incident Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about incident with ID INCIDENT_ID in Palo Alto XDR.` | The action succeeded.  
`Error executing action "Get Incident Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Incident Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Isolate Endpoint

Isolate an endpoint.

#### Action inputs

The **Isolate Endpoint** action requires the following parameters:

Parameter | Description  
---|---  
`Agent ID` | Optional. A comma-separated list of agent IDs to isolate. This parameter works in conjunction with the provided entities.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

### Ping

Test connectivity to Palo Alto Networks Cortex XDR.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

### Query

Retrieve the data of a specific incident including alerts, and key artifacts.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Incident ID | String | N/A | The ID of the incident for which you want to retrieve data.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    {
        "file_artifacts":
        {
            "total_count": 2,
            "data": [
                {
                    "file_signature_status": "SIGNATURE_SIGNED",
                    "is_process": "true",
                    "is_malicious": "false",
                    "is_manual": "false",
                    "file_name": "cmd.exe",
                    "file_signature_vendor_name": "Microsoft Corporation",
                    "file_sha256": "6f88fb88ffb0f1d5465c2826e5b4f523598b1b8378377c8378ffebc171bad18b",
                    "type": "HASH",
                    "file_wildfire_verdict": "BENIGN",
                    "alert_count": 1
                }, {
                    "file_signature_status": "SIGNATURE_SIGNED",
                    "is_process": "true",
                    "is_malicious": "false",
                    "is_manual": "false",
                    "file_name": "WmiPrvSE.exe",
                    "file_signature_vendor_name": "Microsoft Corporation",
                    "file_sha256": "25dfb8168246e5d04dd6f124c95e4c4c4e8273503569acd5452205558d099871",
                    "type": "HASH",
                    "file_wildfire_verdict": "BENIGN",
                    "alert_count": 1
                }]},
        "incident": {
            "status": "new",
            "incident_id": "1645",
            "user_count": 1,
            "assigned_user_mail": " ",
            "severity": "high",
            "resolve_comment": " ",
            "assigned_user_pretty_name": " ",
            "notes": " ",
            "creation_time": 1564877575921,
            "alert_count": 1,
            "med_severity_alert_count": 0,
            "detection_time": " ",
            "modification_time": 1564877575921,
            "manual_severity": " ",
            "xdr_url": "https://ac997a94-5e93-40ea-82d9-6a615038620b.xdr.us.paloaltonetworks.com/incident-view/1645",
            "manual_description": " ",
            "low_severity_alert_count": 0,
            "high_severity_alert_count": 1,
            "host_count": 1,
            "description": "WMI Lateral Movement generated by BIOC detected on host ILCSYS31 involving user ILLICIUM\\\\ibojer"
        },
        "alerts": {
            "total_count": 1,
            "data": [
                {
                    "action_pretty": "Detected",
                    "description": "Process action type = execution AND name = cmd.exe Process name = wmiprvse.exe, cgo name = wmiprvse.exe",
                    "host_ip": "10.0.50.31",
                    "alert_id": "21631",
                    "detection_timestamp": 1564877525123,
                    "name": "WMI Lateral Movement",
                    "category": "Lateral Movement",
                    "severity": "high",
                    "source": "BIOC",
                    "host_name": "ILCSYS31",
                    "action": "DETECTED",
                    "user_name": "ILLICIUM\\\\ibojer"
                }]},
        "network_artifacts": {
            "total_count": 0,
            "data": []
        }
    }
    

### Resolve an Incident

The ability to close XDR incidents with a close reason.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Incident ID | String | N/A | The ID of the incident to be updated.  
Status | List | UNDER_INVESTIGATION | Updated incident status.  
Resolve Comment | String | N/A | Descriptive comment explaining the incident change.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

### Scan Endpoint

Use the **Scan Endpoint** action to scan endpoints in Palo Alto Cortex XDR.

**Important:** This action executes asynchronously, requiring you to adjust the script timeout value in the Google SecOps IDE.

This action runs on the following Google SecOps entities:

  * `IP Address`

  * `Hostname`




#### Action inputs

The **Scan Endpoint** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | Optional. The ID of the Incident to associate the scan activity with, allowing the results to appear in the Incident timeline.  
`Agent ID` | Optional. A comma-separated list of agent IDs to include in the scan. This parameter works in conjunction with the provided entities.  
  
#### Action outputs

The **Scan Endpoint** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Scan Endpoint** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully scanned the following endpoints in Palo Alto XDR: ENTITY_ID` `The scan didn't complete for the following endpoints in Palo Alto XDR: ENTITY_ID` `The scan didn't complete for all of the provided endpoints in Palo Alto XDR.` | The action succeeded.  
`Error executing action "Scan Endpoint". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Scan Endpoint** action:
    
    
    [
       {
          "Entity": "192.168.1.10",
          "EntityResult": {
             "endpoint_id": "a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5",
             "endpoint_name": "PLACEHOLDER-SERVER-NAME",
             "endpoint_type": "AGENT_TYPE_SERVER",
             "endpoint_status": "CONNECTED",
             "os_type": "AGENT_OS_WINDOWS",
             "os_version": "10.0.yyyy",
             "ip": [
                "192.168.1.10"
             ],
             "ipv6": [],
             "public_ip": "203.0.113.45",
             "users": [],
             "domain": "WORKGROUP",
             "alias": "",
             "first_seen": 1680000000000,
             "last_seen": 1760000000000,
             "content_version": "YYYY-ZZZZZ",
             "installation_package": "PLACEHOLDER-PACKAGE",
             "active_directory": [],
             "install_date": 1680000000000,
             "endpoint_version": "X.Y.Z.W",
             "is_isolated": "AGENT_UNISOLATED",
             "isolated_date": null,
             "group_name": [
                "PLACEHOLDER-GROUP"
             ],
             "operational_status": "PROTECTED",
             "operational_status_description": "[]",
             "operational_status_details": [],
             "scan_status": "SCAN_STATUS_PENDING",
             "content_release_timestamp": 1760000000000,
             "last_content_update_time": 1760000000000,
             "operating_system": "Windows Server PLACEHOLDER",
             "mac_address": [
                "00:1A:2B:3C:4D:5E"
             ],
             "assigned_prevention_policy": "PLACEHOLDER-POLICY",
             "assigned_extensions_policy": "Windows Default",
             "token_hash": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
             "tags": {
                "server_tags": [
                   "PLACEHOLDER-TAG"
                ],
                "endpoint_tags": []
             },
             "content_status": "UP_TO_DATE"
          }
       }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Scan Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update an Incident

The ability to set a specific XDR incident as under investigation, assign to named users, etc.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Incident ID | String | N/A | The ID of the incident to be updated.  
Assigned User Name | String | N/A | The updated full name of the incident assignee.  
Severity | List | Low | Administrator-defined severity.  
Status | List | UNDER_INVESTIGATION | Updated incident status.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

### Unisolate Endpoint

Unisolate an endpoint.

#### Action inputs

The **Unisolate Endpoint** action requires the following parameters:

Parameter | Description  
---|---  
`Agent ID` | Optional. A comma-separated list of agent IDs to unisolate. This parameter works in conjunction with the provided entities.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

This action can provide the results detailed in the following sections.

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### JSON Result
    
    
    N/A
    

## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Palo Alto Cortex XDR Connector

Use this connector to pull incidents from Palo Alto Cortex XDR.

**Note:** Dynamic List functionality applies to the `source` parameter.

#### Connector inputs

The **Palo Alto Cortex XDR Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `event_type`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Optional. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Api Root` | Required. The API root of the Palo Alto XDR instance.  
`Api Key` | Required. The Palo Alto XDR API key used for authentication.  
`Api Key ID` | Required. The ID associated with the Palo Alto XDR API Key.  
`Status Filter` | Optional. A comma-separated list of alert statuses to ingest. The possible values are as follows:

  * `New`
  * `Under Investigation`
  * `Resolved`

The default value is `New,Under Investigation`.  
`Split Incident Alerts` | Optional. If selected, the connector separates individual alerts within a single incident into distinct SOAR Alerts. Disabled by default.  
`Lowest Alert Severity To Fetch` | Optional. The lowest severity level of alerts to retrieve. `Lowest Incident SmartScore To Fetch` acts as a primary filter. If a parent incident's score meets its threshold, all associated alerts are processed regardless of this setting. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`
  * `Critical`

If no value is provided, the connector ingests alerts with all severity levels.  
`Lowest Incident Severity To Fetch` | Optional. The lowest severity level of incidents to retrieve. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`
  * `Critical`

If no value is provided, the connector ingests incidents with all severity levels.  
`Lowest Incident SmartScore To Fetch` | Optional. The lowest SmartScore (`0` to `100`) required to fetch an incident. This filter operates independently of `Lowest Incident Severity To Fetch`. If an incident meets either the severity or the SmartScore threshold, it is ingested. If no value is provided, the SmartScore filter is ignored.  
`Max Days Backwards` | Required. The maximum number of days in the past to search for and retrieve incidents during the initial run. The default value is `24`.  
`Alerts Count Limit` | Required. The maximum number of incidents the connector processes for every iteration. The maximum value is `100`. The default value is `10`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list as a blocklist. Disabled by default.  
`Include Historical Artifacts` | Optional. If selected, the connector retrieves all historical artifacts associated with an alert during initial ingestion. **Note:** Enabling this option may increase the volume of data ingested during the first run.   
`Artifacts To Ignore` | Optional. A comma-separated list of artifacts to exclude from Google SecOps event creation.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Enabled by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Palo Alto Cortex XDR server. Enabled by default.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The proxy username to authenticate with.  
`Proxy Password` | Optional. The proxy password to authenticate with.  
  
#### Connector rules

The connector doesn't support Whitelist/Blacklist.

The connector supports proxy.

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Palo Alto Cortex XDR - Sync Incidents

Use the **Palo Alto Cortex XDR - Sync Incidents** job to synchronize alerts and incidents between Google SecOps and Palo Alto Networks Cortex XDR.

This job ensures that incident statuses, comments, and user assignees remain consistent across both platforms.

#### Job behavior

The **Palo Alto Cortex XDR - Sync Incidents** job facilitates bidirectional synchronization through the following mechanisms:

  * **Synchronization stages** : The job executes in two distinct phases:

    1. Pushes status updates from Google SecOps to Palo Alto Cortex XDR.
    2. Pulls modifications from Palo Alto Cortex XDR to update Google SecOps.
  * **Processing window** : On the first iteration, the job processes cases based on `Max Hours Backwards`. Subsequent runs process updates based on the timestamp of the last synchronized alert.

  * **Case identification** : The job identifies relevant cases by searching for the `Palo Alto XDR Incident` tag.

  * **Manual mapping** : For cases that did not originate from the Palo Alto Cortex XDR Connector, you must perform the following two steps:

    1. Add the `Palo Alto XDR Incident` tag to the case.
    2. Add an `Incident_ID` context value containing the XDR incident ID.
  * **Comment synchronization** : The job synchronizes comments between the platforms using the following rules:

    * Comments originating from XDR are prefixed with `Palo Alto XDR:`.
    * Comments originating from Google SecOps are prefixed with `Google SecOps:`.
    * Case closure comments are included in the synchronization to ensure consistent audit trails.
  * **Closure logic and fallbacks** : When a case is resolved, the job maps the closure reason to the appropriate **Reason** and **Root Cause** in XDR. If a specific combination is not found in the XDR environment, the job uses a generic fallback option to ensure the incident closes successfully.

  * **User assignment** : If the **User Mapping** JSON is configured, the job synchronizes assignees. If a user is not present in the mapping, the sync for that user is skipped and logged.

  * **Contextual alert data** : A list of alerts associated with the incident is maintained in the `XDR_ALERTS` context value for each case.




#### Job parameters

The **Palo Alto XDR - Sync Incidents** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment from which to synchronize incidents. The default value is `Default Environment`.  
`Api Root` | Required. The Palo Alto Cortex XDR API root URL.  
`Api Key` | Required. The API Key used for authentication with the Palo Alto Cortex XDR server.  
`Api Key ID` | Required. The ID associated with the Palo Alto XDR API Key.  
`Max Hours Backwards` | Required. The number of hours prior to the current time to synchronize incidents during the initial job iteration. The default value is `24`.  
`User Mapping JSON` | Optional. A JSON object used to map Google SecOps display names to XDR usernames for the purpose of synchronizing case assignees. Use the following format:
    
    
    {
      "Google SecOps Display Name": "XDR Username"
    }

If no value is provided, user synchronization is skipped.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Palo Alto Cortex XDR server. Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
