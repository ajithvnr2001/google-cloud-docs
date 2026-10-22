---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/intezer/
title: Intezer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:27.310675+00:00
---

# Intezer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/intezer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Intezer

This document provides guidance on how to integrate Intezer with the SOAR module of Google Security Operations.

## Integrate Intezer with Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`API Root` | _Required_ API root of the Intezer service.  
`API Key` | _Required_ API key of the Intezer service.  
`Verify SSL` | _Optional_ If selected, Google SecOps verifies that the SSL certificate for the connection to the Intezer server is valid. Not selected by default.  
  
For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Detonate File

Use Intezer to analyze a file.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`File Path` | _Required_ The paths to the files that you want to analyze. You can provide multiple paths in a comma-separated string, such as `/tmp/example1.eml,/tmp/example2.eml`.  
`Related Alert ID` | _Optional_ The alert ID related to the file.  
  
#### Action outputs

The following table describes the output types associated with the Detonate File action:

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

The following example describes the JSON result output received when using the Detonate File action:
    
    
    [
       {
          "analysis_id":"6cd3347b-f5b2-4c98-a0bc-039a6386dc34",
          "analysis_status":"created",
          "analysis_type":"file",
          "identifier":"/tmp/example.eml"
       }
    ]
    

##### Output messages

The Detonate File action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the analysis ids for the following file paths: PATH in Intezer` | Action succeeded.  
`Action wasn't able to fetch the analysis ids for the following file paths: PATH in Intezer` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Detonate File action:

Script result name | Value  
---|---  
is_success | True or False  
  
### Detonate Hash

Analyze a file hash (SHA-1, SHA-256, or MD5) in Intezer Analyze.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`File Hash` | _Required_ The hash of the reports that you want to analyze. You can provide multiple hashes in a comma-separated string.  
  
#### Action outputs

The following table describes the output types associated with Detonate File action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Detonate Hash action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Detonate Hash action:
    
    
    [
       {
          "analysis_id":"7bbbec69-5764-479e-bb1c-c3686e992fbb",
          "analysis_status":"created",
          "analysis_type":"file",
          "identifier":"6be971118951786bc7be55ef5656149504008a3e"
       },
       {
          "analysis_id":"33ee6661-7435-4e0a-a606-0b7d1a644859",
          "analysis_status":"created",
          "analysis_type":"file",
          "identifier":"5b97c39d87ad627c53023bfebb0ea1b5227c3f4e86e3bf06b23f3e4b0d6726e2"
       }
    ]
    

##### Output messages

The Detonate Hash action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the analysis ids for the following hashes: HASH_LIST` | Action succeeded.  
`Action wasn't able to fetch the analysis ids for the following hashes: HASH_LIST` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Detonate URL

Analyze a suspicious URL with Intezer.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Url` | _Optional_ The URL that you want to analyze, such as `https://www.example.com/`.You can provide multiple URLs in a comma-separated string.  
  
#### Action outputs

The following table describes the output types associated with Detonate URL action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Detonate URL action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Detonate URL action:
    
    
    [
       {
          "analysis_id":"d99b7317-02a3-4282-81e9-d27528a575c0",
          "analysis_status":"created",
          "analysis_type":"url",
          "identifier":"www.example.com"
       },
       {
          "analysis_id":"ee8d2e7e-950b-43f2-b0b7-cbfc3c20dfc5",
          "analysis_status":"created",
          "analysis_type":"url",
          "identifier":"https://www.example.com/"
       }
    ]
    

##### Output messages

The Detonate URL action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the analysis ids for the following urls: URL_LIST in Intezer` | Action succeeded.  
`Action wasn't able to fetch the analysis ids for the following urls: URL_LIST in Intezer` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Get Alert

Get an ingested alert triage and response information using the alert ID.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Alert ID` | _Required_ The alert ID to query.  
`Wait For Completion` | _Optional_ If selected, the action waits for the analysis to complete.  
  
#### Action outputs

The following table describes the output types associated with the Get Alert action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Get Alert action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Get Alert action:
    
    
    {
       "result":{
          "alert_id":"ldt:91a1c5ef609ac479ba77f8ca5879c82fc:958686237274",
          "source":"cs",
          "sender":"cs",
          "raw_alert":{
             "cid":"123456789abcdef123456789abcdef12",
             "alert_type":"identify",
             "created_timestamp":"2023-11-09T00:03:10.116556016Z",
             "detection_id":"ldt:91a1c5ef609ac479ba77f8ca5879c82fc:958686237274",
             "evidences":[
                {
                   "evidence_type":"domain",
                   "evidence_value":"domain"
                }
             ],
             "device":{
                "device_id":"6a1c5ef609ac479ba77f8ca5879c82fc",
                "cid":"123456789abcdef123456789abcdef12",
                "agent_load_flags":"0",
                "agent_local_time":"2023-10-18T23:01:49.681Z",
                "agent_version":"7.03.15805.0",
                "bios_manufacturer":"Example Technologies LTD",
                "bios_version":"6.00",
                "config_id_base":"65994753",
                "config_id_build":"15805",
                "config_id_platform":"8",
                "external_ip":"35.246.203.0",
                "hostname":"example-hostname",
                "first_seen":"2023-06-14T10:50:40Z",
                "last_seen":"2023-11-09T00:01:56Z",
                "local_ip":"198.51.100.1",
                "mac_address":"02-42-48-a3-7f-29",
                "major_version":"3",
                "minor_version":"10",
                "os_version":"CentOS 7.9",
                "platform_id":"3",
                "platform_name":"Linux",
                "product_type_desc":"Server",
                "status":"normal",
                "system_manufacturer":"Example, Inc.",
                "system_product_name":"Example Virtual Platform",
                "groups":[
                   "9489d65c343244169627d4a728389039"
                ],
                "modified_timestamp":"2023-11-09T00:02:06Z"
             },
             "behaviors":[
                {
                   "device_id":"6a1c5ef609ac479ba77f8ca5879c82fc",
                   "timestamp":"2023-11-09T00:03:02Z",
                   "template_instance_id":"1359",
                   "behavior_id":"10304",
                   "filename":"bash",
                   "filepath":"/usr/bin/bash",
                   "alleged_filetype":"",
                   "cmdline":"bash crowdstrike_test_high",
                   "scenario":"suspicious_activity",
                   "objective":"Falcon Detection Method",
                   "tactic":"Falcon Overwatch",
                   "tactic_id":"CSTA0006",
                   "technique":"Malicious Activity",
                   "technique_id":"CST0002",
                   "display_name":"TestTriggerHigh",
                   "description":"A high level detection was triggered on this process for testing purposes.",
                   "severity":70,
                   "confidence":100,
                   "ioc_type":"",
                   "ioc_value":"",
                   "ioc_source":"",
                   "ioc_description":"",
                   "user_name":"root",
                   "user_id":"0",
                   "control_graph_id":"ctg:6a1c5ef609ac479ba77f8ca5879c82fc:958686237274",
                   "triggering_process_graph_id":"pid:6a1c5ef609ac479ba77f8ca5879c82fc:46565404531105",
                   "sha256":"00f8cbc5b3a6640af5ac18d01bc5a666f6f583b1379b9491e0bcc28ba78c92e9",
                   "md5":"cfd65bed18a1fae631091c3a4c4dd533",
                   "parent_details":{
                      "parent_sha256":"00f8cbc5b3a6640af5ac18d01bc5a666f6f583b1379b9491e0bcc28ba78c92e9",
                      "parent_md5":"cfd65bed18a1fae631091c3a4c4dd533",
                      "parent_cmdline":"/bin/sh -c ./alert.sh",
                      "parent_process_graph_id":"pid:6a1c5ef609ac479ba77f8ca5879c82fc:46565400489930"
                   },
                   "pattern_disposition":0,
                   "pattern_disposition_details":{
                      "indicator":false,
                      "detect":false,
                      "inddet_mask":false,
                      "sensor_only":false,
                      "rooting":false,
                      "kill_process":false,
                      "kill_subprocess":false,
                      "quarantine_machine":false,
                      "quarantine_file":false,
                      "policy_disabled":false,
                      "kill_parent":false,
                      "operation_blocked":false,
                      "process_blocked":false,
                      "registry_operation_blocked":false,
                      "critical_process_disabled":false,
                      "bootup_safeguard_enabled":false,
                      "fs_operation_blocked":false,
                      "handle_operation_downgraded":false,
                      "kill_action_failed":false,
                      "blocking_unsupported_or_disabled":false,
                      "suspend_process":false,
                      "suspend_parent":false
                   }
                }
             ],
             "email_sent":false,
             "first_behavior":"2023-11-09T00:03:02Z",
             "last_behavior":"2023-11-09T00:03:02Z",
             "max_confidence":100,
             "max_severity":70,
             "max_severity_displayname":"High",
             "show_in_ui":true,
             "status":"new",
             "hostinfo":{
                "domain":""
             },
             "seconds_to_triaged":0,
             "seconds_to_resolved":0,
             "behaviors_processed":[
                "pid:6a1c5ef609ac479ba77f8ca5879c82fc:46565404531105:10304"
             ],
             "date_updated":"2023-11-12T00:06:14Z"
          },
          "alert_sub_types":[
    
          ],
          "alert":{
             "alert_id":"ldt:91a1c5ef609ac479ba77f8ca5879c82fc:958686237274",
             "alert_url":null,
             "creation_time":"2023-11-12T00:06:14",
             "alert_title":"ldt:91a1c5ef609ac479ba77f8ca5879c82fc:958686237274",
             "device":{
    
             },
             "creation_time_display":"12 Nov 23 | 00:06 UTC"
          },
          "triage_result":{
             "alert_verdict":"audited",
             "risk_category":"audited",
             "risk_level":"informational",
             "risk_score":60,
             "risk_level_display":"Informational",
             "risk_category_display":"Audited",
             "alert_verdict_display":"Audited"
          },
          "response":{
             "status":"no_action_needed",
             "automated_response_actions":[
    
             ],
             "user_recommended_actions":[
    
             ],
             "user_recommended_actions_display":"",
             "status_display":"No Action Needed"
          },
          "note":"\ud83d\udfe6 Intezer Automated Triage\n===================================\nAudited - No Action Needed\n===================================\n\n- Title: ldt:alert-ID\n- Source: CrowdStrike\n- Creation time: 12 Nov 23 | 00:06 UTC\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/ldt:alert_ID",
          "source_display":"CrowdStrike",
          "source_type":"edr",
          "intezer_alert_url":"https://analyze.intezer.com/alerts/ldt:alert-ID"
       },
       "status":"succeeded"
    }
    

##### Output messages

The Get Alert action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the alert details for the following alert id: ALERT_ID in Intezer` | Action succeeded.  
`Action wasn't able to fetch the alert detail for the following alert: ERROR_REASON in Intezer ` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Get File Report

Get a file analysis report based on an analysis ID or a file hash.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Analysis ID` | _Optional_ A comma-separated list of the file analysis IDs to run the action on. This parameter is case sensitive. If both **Analysis ID** and **File Hash** parameters are provided, the **File Hash** value has priority.  
`File Hash` | _Optional_ A comma-separated list of file hashes to run the action on. This parameter is case sensitive. If both **Analysis ID** and **File Hash** parameters are provided, the **File Hash** value has priority.  
`Private Only` | _Optional_ If selected, the action show only private reports (relevant only for hashes).  
`Wait For Completion` | _Optional_ If selected, the action waits for the analysis to complete before returning the report.  
  
#### Action outputs

The following table describes the output types associated with the Get Report action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Get Report action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Get Report action:
    
    
    [
       {
          "analysis_id":"fdc18702-e308-43e5-9476-554501fb2009",
          "analysis_type":"file",
          "analysis_status":"succeeded",
          "analysis_content":{
             "analysis":{
                "analysis_id":"fdc18702-e308-43e5-9476-554501fb2009",
                "analysis_time":"Fri, 16 Feb 2024 08:16:20 GMT",
                "analysis_url":"https://analyze.intezer.com/analyses/analysis-id",
                "file_name":"file_name",
                "is_private":true,
                "sha256":"9baf8bb61b9ab2e28d9a2599bc8f524489845782097464edd20ad7d0353c3b6d",
                "sub_verdict":"inconclusive",
                "tags":[
                   "non_executable"
                ],
                "verdict":"unknown"
             },
             "iocs":{
                "files":[
                   {
                      "analysis_id":"fdc18702-e308-43e5-9476-554501fb2009",
                      "family":null,
                      "path":"file_name",
                      "sha256":"9baf8bb61b9ab2e28d9a2599bc8f524489845782097464edd20ad7d0353c3b6d",
                      "type":"main_file",
                      "verdict":"unknown"
                   }
                ],
                "network":[
                   {
                      "classification":"suspicious",
                      "ioc":"198.51.100.161",
                      "source":[
                         "Network communication"
                      ],
                      "type":"ip"
                   }
                ]
             },
             "ttps":[
                {
                   "data":[
                      {
                         "cid":2793,
                         "pid":1996,
                         "type":"call"
                      },
                      {
                         "cid":5365,
                         "pid":1340,
                         "type":"call"
                      },
                      {
                         "cid":5366,
                         "pid":1340,
                         "type":"call"
                      },
                      {
                         "cid":5373,
                         "pid":1340,
                         "type":"call"
                      },
                      {
                         "cid":5375,
                         "pid":1340,
                         "type":"call"
                      }
                   ],
                   "description":"Guard pages use detected - possible anti-debugging.",
                   "name":"antidebug_guardpages",
                   "severity":2,
                   "ttps":[
                      {
                         "name":"Native API",
                         "ttp":"Execution::Native API [T1106]"
                      }
                   ]
                }
             ],
             "metadata":{
                "file_type":"non executable",
                "indicators":[
                   {
                      "classification":"informative",
                      "name":"non_executable"
                   }
                ],
                "md5":"a01073d047bd9bb151b8509570ea44d6",
                "sha1":"610742629fe7d7188042c8c427fc68723d53cd42",
                "sha256":"9baf8bb61b9ab2e28d9a2599bc8f524489845782097464edd20ad7d0353c3b6d",
                "size_in_bytes":21,
                "ssdeep":"3:H0shRFCZ:HlS"
             },
             "root-code-reuse":null
          }
       }
    ]
    

##### Output messages

The Get File Report action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the file analysis for the following items: ANALYSIS_ID_OR_HASH_LIST in Intezer` | Action succeeded.  
`No file analysis were found for the provided items` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Get URL Report

Get a URL analysis report based on the URL analysis ID.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Analysis ID` | _Required_ A comma-separated list of the file analysis IDs to run the action on. This parameter is case sensitive.The analysis ID is returned when submitting a URL for analysis.   
`Wait For Completion` | _Optional_ If selected, the action waits for the analysis to complete.  
  
#### Action outputs

The following table describes the output types associated with the Get URL Report action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Get URL Report action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Get URL Report action:
    
    
    [
       {
          "analysis_id":"Aef96e22-e0b1-45de-b7fa-2b9596ecb922",
          "analysis_type":"url",
          "analysis_status":"succeeded",
          "analysis_content":{
             "analysis":{
                "analysis_id":"aef96e22-e0b1-45de-b7fa-2b9596ecb922",
                "analysis_time":"Wed, 07 Feb 2024 06:16:42 GMT",
                "analysis_url":"https://analyze.intezer.com/url/aef96e22-e0b1-45de-b7fa-2b9596ecb922",
                "api_void_risk_score":0,
                "certificate":{
                   "issuer":"Example Secure Certificate Authority",
                   "protocol":"TLS 1.3",
                   "subject_name":"analyze.intezer.com",
                   "valid_from":"2023-07-25 19:50:53.000000",
                   "valid_to":"2024-08-25 19:50:53.000000"
                },
                "domain_info":{
                   "creation_date":"2015-08-28 04:24:45.000000",
                   "domain_name":"intezer.com",
                   "registrar":"Example, LLC"
                },
                "indicators":[
                   {
                      "classification":"informative",
                      "indicator_info":"text/html",
                      "indicator_type":"content_type",
                      "text":"Content type: text/html"
                   },
                   {
                      "classification":"informative",
                      "indicator_type":"valid_https",
                      "text":"Valid https"
                   },
                   {
                      "classification":"informative",
                      "indicator_type":"url_accessible",
                      "text":"URL is accessible"
                   },
                   {
                      "classification":"suspicious",
                      "indicator_type":"empty_page_title",
                      "text":"Has empty page title"
                   },
                   {
                      "classification":"informative",
                      "indicator_type":"domain_ipv4_assigned",
                      "text":"Assigned IPv4 domain"
                   },
                   {
                      "classification":"informative",
                      "indicator_type":"domain_ipv4_valid",
                      "text":"Valid IPv4 domain"
                   },
                   {
                      "classification":"informative",
                      "indicator_type":"uses_cloudflare",
                      "text":"Uses Cloudflare"
                   }
                ],
                "ip":"203.0.113.201",
                "redirect_chain":[
                   {
                      "response_status":200,
                      "url":"https://example.com/"
                   }
                ],
                "scanned_url":"https://example.com/",
                "submitted_url":"https://example.com",
                "summary":{
                   "description":"No suspicious activity was detected for this URL",
                   "main_connection_gene_count":0,
                   "main_connection_gene_percentage":0.0,
                   "title":"No Threats",
                   "verdict_name":"no_threats",
                   "verdict_type":"no_threats"
                }
             }
          }
       }
    ]
    

##### Output messages

The Get URL Report action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the url analysis for the following analysis ids: ANALYSIS_ID in Intezer` | Action succeeded.  
`No url analysis were found for the provided analysis ids` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Index File

Index the file genes into the organizational database.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Index As` | _Required_ Index as trusted or malicious.  
`SHA256` | _Optional_ The SHA-256 hash to index.You can provide multiple hashes in a comma-separated string.  
`Family Name` | _Optional_ The family name to use in the index.This parameter is required if the **Index As** parameter value is `malicious`.  
  
#### Action outputs

The following table describes the output types associated with the Index File action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Index File action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Index File action:
    
    
    [
       {
          "index_id":"091ed5aa-a94f-48d9-9b90-89ff434947b2",
          "status":"succeeded"
       }
    ]
    

##### Output messages

The Index File action provides the following output messages:

Output message | Message description  
---|---  
`Waiting for results for the following hashes: HASH_LIST` | Action is still in progress.  
`Successfully indexed the following file hashes: HASH_LIST in Intezer` `Action wasn't able to index the following file hashes: HASH_LIST` | Action succeeded.  
`None of the file hash got indexed` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Ping

Test connectivity to Intezer.

This action runs on all entities.

#### Action inputs

None.

#### Action outputs

The following table describes the output types associated with the Ping action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script result name | Value  
---|---  
is_success | True or False  
  
### Submit Alert

Submit a new alert that includes the raw alert information to Intezer for processing.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Source` | _Required_ The source of the alert.  
`Raw Alert` | _Required_ Alert raw data in JSON format.  
`Alert Mapping` | _Required_ Mapping to use for the alert in JSON format.  
  
#### Action outputs

The following table describes the output types associated with the Submit Alert action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Submit Alert action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Submit Alert action:
    
    
    {
       "alert_id":"ccdt:2a1c5ef609ac479ba77f8ca5879c82fc:958686237274"
    }
    

##### Output messages

The Submit Alert action provides the following output messages:

Output message | Message description  
---|---  
`Successfully submitted details about the following alert: ALERT_ID` | Action succeeded.  
`Error executing action "Submit Alert". Reason: Invalid parameter "Alert Mapping". The JSON structure is invalid. Wrong value provided: ALERT_ID` | Action failed.Check the **Alert Mapping** parameter value.  
  
### Submit File

Submit a file for analysis.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`File Paths` | _Required_ The paths of the files to analyze.  
  
#### Action outputs

The following table describes the output types associated with the Submit File action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the Submit File action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result

The following example describes the JSON result output received when using the Submit File action:
    
    
    {
        "C:\\\\Users\\\\User1\\\\Downloads\\test_file.exe":
          {
            "4e553bce90f0b39cd71ba633da5990259e185979c2859ec2e04dd8efcdafe356":
                    {
                      "family_name": "Example",
                      "analysis_id": "548e6b8b-20b1-445c-9922-af6b52a8abc3",
                      "sub_verdict": "known_malicious",
                      "analysis_url": "https://analyze.intezer.com/#/analyses/analysis-ID",
                      "verdict": "malicious",
                      "sha256": "4e553bce90f0b39cd71ba633da5990259e185979c2859ec2e04dd8efcdafe356",
                      "is_private": true,
                      "analysis_time": "Thu, 14 Feb 2019 08:58:27 GMT"
                    }
           }
    }
    

### Submit Hash

Submit a hash for analysis to Intezer.

This action runs on a FileHash entity.

#### Action inputs

None.

#### Action outputs

The following table describes the output types associated with the Submit Hash action:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Not available  
Script result | Available  
  
##### Entity enrichment

The following table describes the entity enrichment logic associated with the Submit Hash action:

Enrichment field | Logic  
---|---  
`family_name` | Returns if it exists in the JSON result  
`analysis_id` | Returns if it exists in JSON result  
`sub_verdict` | Returns if it exists in JSON result  
`analysis_url` | Returns if it exists in JSON result  
`verdict` | Returns if it exists in JSON result  
`sha256` | Returns if it exists in JSON result  
`is_private` | Returns if it exists in JSON result  
`analysis_time` | Returns if it exists in JSON result  
  
##### JSON result

The following example describes the JSON result output received when using the Submit Hash action:
    
    
    [{
        "EntityResult":
          {
            "family_name": "Example",
            "analysis_id": "548e6b8b-20b1-445c-9922-af6b52a8abc3",
            "sub_verdict": "known_malicious",
            "analysis_url": "https://analyze.intezer.com/#/analyses/analysis-ID",
            "verdict": "malicious",
            "sha256": "4e553bce90f0b39cd71ba633da5990259e185979c2859ec2e04dd8efcdafe356",
            "is_private": true,
            "analysis_time": "Thu, 14 Feb 2019 08:58:27 GMT"
          },
       "Entity": "4e553bce90f0b39cd71ba633da5990259e185979c2859ec2e04dd8efcdafe356"
    }]
    

##### Script result

The following table describes the values for the script result output when using the Submit Hash action:

Script result name | Value  
---|---  
is_success | True or False  
  
### Submit Suspicious Email

Submit a suspicious phishing email in raw format (`.msg` or `.eml`) to Intezer for processing.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`Email File Path` | _Required_ The path to the email file.  
  
#### Action outputs

The following table describes the output types associated with the Submit Suspicious Email action:

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

The following example describes the JSON result output received when using the Submit Suspicious Email action:
    
    
    {
       "alert_id":"3385f4f9aec655dfac9d59d54e8ff1f12343501ebc62bf1a91ad1954bb6ae0b9"
    }
    

##### Output messages

The Submit Suspicious Email action provides the following output messages:

Output message | Message description  
---|---  
`Successfully submitted suspicious email EMAIL_FILE_PATH in Intezer` | Action succeeded.  
`Error executing action "Intezer". Reason: No such file or directory: EMAIL_FILE_PATH` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Submit Suspicious Email action:

Script result name | Value  
---|---  
is_success | True or False  
  
### Unset Index File

Remove files from the index.

This action runs on all entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters | Description  
---|---  
`SHA256` | _Optional_ The SHA-256 hash to remove from the index. You can provide multiple files in a comma-separated string.  
  
#### Action outputs

The following table describes the output types associated with the Unset Index File action:

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

The Unset Index File action provides the following output messages:

Output message | Message description  
---|---  
`Successfully unset file index for the following hashes: HASH_LIST in Intezer` `Action wasn't able to unset file index for the following hashes: HASH_LIST` | Action succeeded.  
`Action wasn't able to unset file index for the following hashes: HASH_LIST` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Unset Index File action:

Script result name | Value  
---|---  
is_success | True or False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
