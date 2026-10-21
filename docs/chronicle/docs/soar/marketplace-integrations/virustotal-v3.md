---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal-v3/
title: Integrate VirusTotal v3 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:18:08.110284+00:00
---

# Integrate VirusTotal v3 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal-v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate VirusTotal v3 with Google SecOps 

This document explains how to integrate VirusTotal v3 with Google Security Operations (Google SecOps).

**Note:** We recommended using the **Google Threat Intelligence** integration as it provides more capabilities and features. 

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/VirusTotalV3.zip).

**Important:** In the Google SecOps platform, the integration for VirusTotal v3 is called _VirusTotalV3_.

## Use cases

The **VirusTotal v3** integration uses the Google SecOps capabilities to support the following use cases:

  * **File analysis** : Submit a file hash or a file to VirusTotal for analysis and retrieve scan results from multiple antivirus engines to determine if the submitted item is malicious.

  * **URL analysis** : Run a URL against the VirusTotal database to identify potentially malicious websites or phishing pages.

  * **IP address analysis** : Investigate an IP address and identify its reputation and any associated malicious activity.

  * **Domain analysis** : Analyze a domain name and identify its reputation and any associated malicious activity, such as phishing or malware distribution.

  * **Retrohunting** : Scan through the VirusTotal historical data to search for files, URLs, IPs, or domains that were previously flagged as malicious.

  * **Automated enrichment** : Automatically enrich incident data with threat intelligence.

  * **Phishing investigation** : Analyze suspicious emails and attachments by submitting them to VirusTotal for analysis.

  * **Malware analysis** : Upload malware samples to VirusTotal for dynamic and static analysis and obtain insights into the behavior and potential impact of the samples.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **VirusTotal Premium API:** To function properly, this integration requires a VirusTotal Premium API subscription. 

For more information about API tier differences, see [Public vs Premium API](https://docs.virustotal.com/reference/public-vs-premium-api).

  * **API key:** You must configure a VirusTotal API Key before you set up the integration instance in Google SecOps.


**Note:** This integration specifically uses the **VirusTotal API v3**. For more details, see [VirusTotal API v3 Overview](https://docs.virustotal.com/reference/overview).

### Configure the VirusTotal API key

Before you configure the VirusTotal v3 integration in Google SecOps, you must get, and copy, your API key:

  1. Sign in to the [VirusTotal portal](https://www.virustotal.com/gui/sign-in).

  2. Go to your **Account Settings** and under your username or profile, click **API key**.

  3. Copy the generated API key. Use this key to populate the `API Key` integration parameter.




## Integration parameters

The **VirusTotal v3** integration requires the following parameters:

Parameter | Description  
---|---  
`API Key` | Required. The VirusTotal API key.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the VirusTotal v3 server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Comment To Entity

Use the **Add Comment To Entity** action to add a comment to entities in VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

**Note:** This action only supports the `MD5`, `SHA-1`, and `SHA-256` hashes.

#### Action inputs

The **Add Comment To Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Comment` | Required. The comment to add to the entities.  
  
#### Action outputs

The **Add Comment To Entity** action provides the following outputs:

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

The following examples show the JSON result outputs received when using the **Add Comment To Entity** action:
    
    
    {
       "Status": "Done"
    }
    
    
    
    {
       "Status": "Not done"
    }
    

##### Output messages

The **Add Comment To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added comments to the following entities in VirusTotal: ENTITY_ID.` `Action wasn't able to add comments to the following entities in VirusTotal: ENTITY_ID.` `No comments were added to the provided entities in VirusTotal. ` | The action succeeded.  
`Error executing action "Add Comment To Entity". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Entity** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Vote To Entity

Use the **Add Vote To Entity** action to add a vote to entities in VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

**Note:** This action only supports the `MD5`, `SHA-1`, and `SHA-256` hashes.

#### Action inputs

The **Add Vote To Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Vote` | Required. The vote to assign to the entity's reputation. The possible values are as follows:

  * `Harmless`
  * `Malicious`

  
  
#### Action outputs

The **Add Vote To Entity** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Vote To Entity** action:
    
    
    {
       "Status": "Done"
    }
    
    
    
    {
       "Status": "Not done"
    }
    

##### Output messages

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added votes to the following entities in VirusTotal: ENTITY_ID.` `Action wasn't able to add votess to the following entities in VirusTotal: ENTITY_ID.` `No votes were added to the provided entities in VirusTotal. ` | The action succeeded.  
`Error executing action "Add Vote To Entity". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Vote To Entity** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Download File

Use the **Download File** action to download a file from VirusTotal.

This action runs on the Google SecOps `File Hash` entity.

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.**Important:** To run this action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Download File** action requires the following parameters:

Parameter | Description  
---|---  
`Download Folder Path` | Required. The path to the folder where the action saves downloaded files.  
`Overwrite` | Optional. If selected, the action replaces any existing file that has the same name as the new, downloaded file. Enabled by default.  
  
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

The following example shows the JSON result output received when using the **Download File** action:
    
    
    {
        "absolute_file_paths": ["file_path_1","file_path_2"]
    }
    

##### Output messages

The **Download File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related files for the following entities in VirusTotal: ENTITY_ID. ` `No related files were found for the following entities in VirusTotal: ENTITY_ID.` `No related files were found for the provided entities in VirusTotal.` | The action succeeded.  
`Error executing action "Download File". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
### Enrich Hash

Use the **Enrich Hash** action to enrich hashes with information from VirusTotal.

This action runs on the Google SecOps `File Hash` entity.

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.

#### Action inputs

The **Enrich Hash** action requires the following parameters:

Parameter | Description  
---|---  
`Engine Threshold` | Optional. The minimum number of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines.  
`Engine Percentage Threshold` | Optional. The minimum percentage (from `0` to `100`, inclusive) of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines. If you configure both `Engine Threshold` and `Engine Percentage Threshold`, the action uses the `Engine Threshold` value.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Resubmit Hash` | Optional. If selected, the action resubmits the hash for analysis rather than using existing results. Disabled by default.  
`Resubmit After (Days)` | Optional. The minimum number of days that must elapse since the last analysis before the hash is resubmitted. This parameter only applies if you select the `Resubmit Hash` parameter. The default value is `30`.  
`Retrieve Comments` | Optional. If selected, the action retrieves comments associated with the hash from VirusTotal. Enabled by default.  
`Retrieve Sigma Analysis` | Optional. If selected, the action retrieves the Sigma analysis results for the hash.Selected by default.  
`Sandbox` | Optional. A comma-separated list of sandbox environments to use for behavior analysis.If you don't set a value, the action uses the default value. The default value is `VirusTotal Jujubox`.  
`Retrieve Sandbox Analysis` | Optional. If selected, the action retrieves sandbox analysis results for the hash and creates a separate section in the JSON output for every specified sandbox.Selected by default.  
`Create Insight` | Optional. If selected, the action generates a security insight containing the analysis information for the hash. Enabled by default.  
`Only Suspicious Entity Insight` | Optional. If selected, the action generates insights only for hashes identified as suspicious based on the configured threshold parameters. This parameter only applies if `Create Insight` is enabled. Disabled by default.  
`Max Comments To Return` | Optional. The maximum number of comments the action retrieves during each run. The default value is `10`.  
`Widget Theme` | Optional. The theme to use for the VirusTotal widget. The possible values are as follows:

  * `Light`
  * `Dark`
  * `Chronicle`

The default value is `Dark`.  
`Fetch Widget` | Optional. If selected, the action retrieves and includes the visual summary widget related to the hash in the Case Wall output. Enabled by default.  
`Fetch MITRE Details` | Optional. If selected, the action retrieves MITRE ATT&CK techniques and tactics that are related to the hash.Disabled by default.  
`Lowest MITRE Technique Severity` | Optional. The minimum severity level for a MITRE ATT&CK technique to include in the results. The action treats the `Unknown` severity as `Info`. The possible values are as follows:

  * `High`
  * `Medium`
  * `Low`
  * `Info`

The default value is `Low`.  
  
#### Action outputs

The **Enrich Hash** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Enrich Hash** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Enrich Hash** action can provide the following table for every enriched entity:

Table name: **ENTITY_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



The **Enrich Hash** action can provide the following table for every entity that has comments:

Table name: **Comments: ENTITY_ID**

Table columns:

  * **Date**
  * **Comment**
  * **Abuse Votes**
  * **Negative Votes**
  * **Positive Votes**
  * **ID**



The **Enrich Hash** action can provide the following table for every entity that has the Sigma analysis results:

Table name: **Sigma Analysis: ENTITY_ID**

Table columns:

  * **ID**
  * **Severity**
  * **Source**
  * **Title**
  * **Description**
  * **Match Context**



##### Entity enrichment table

The following table lists the fields enriched using the **Enrich Hash** action:

Enrichment field name | Applicability  
---|---  
`VT3_id` | Applies when available in the JSON result.  
`VT3_magic` | Applies when available in the JSON result.  
`VT3_md5` | Applies when available in the JSON result.  
`VT3_sha1` | Applies when available in the JSON result.  
`VT3_sha256` | Applies when available in the JSON result.  
`VT3_ssdeep` | Applies when available in the JSON result.  
`VT3_tlsh` | Applies when available in the JSON result.  
`VT3_vhash` | Applies when available in the JSON result.  
`VT3_meaningful_name` | Applies when available in the JSON result.  
`VT3_magic` | Applies when available in the JSON result.  
`VT3_harmless_count` | Applies when available in the JSON result.  
`VT3_malicious_count` | Applies when available in the JSON result.  
`VT3_suspicious_count` | Applies when available in the JSON result.  
`VT3_undetected_count` | Applies when available in the JSON result.  
`VT3_reputation` | Applies when available in the JSON result.  
`VT3_tags` | Applies when available in the JSON result.  
`VT3_malicious_vote_count` | Applies when available in the JSON result.  
`VT3_harmless_vote_count` | Applies when available in the JSON result.  
`VT3_report_link` | Applies when available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Hash** action:
    
    
    {
        "data": {
            "attributes": {
                "categories": {
                    "Dr.Web": "known infection source/not recommended site",
                    "Forcepoint ThreatSeeker": "compromised websites",
                    "sophos": "malware repository, spyware and malware"
                },
                "first_submission_date": 1582300443,
                "html_meta": {},
                "last_analysis_date": 1599853405,
                "last_analysis_results": {
                    "EXAMPLELabs": {
                        "category": "harmless",
                        "engine_name": "EXAMPLELabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Example": {
                        "category": "harmless",
                        "engine_name": "Example",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "last_analysis_stats": {
                    "harmless": 64,
                    "malicious": 6,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                "last_http_response_code": 404,
                "last_http_response_content_length": 204,
                "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                "last_http_response_headers": {
                    "connection": "keep-alive",
                    "content-length": "204",
                    "content-type": "text/html; charset=iso-8859-1",
                    "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                    "keep-alive": "timeout=60",
                    "server": "nginx"
                },
                "last_modification_date": 1599853921,
                "last_submission_date": 1599853405,
                "reputation": 0,
                "tags": [
                    "ip"
                ],
                "targeted_brand": {},
                "threat_names": [
                    "Mal/HTMLGen-A"
                ],
                "times_submitted": 3,
                "title": "404 Not Found",
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/ID"
            },
            "type": "url",
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true
    
    "related_mitre_techniques": [{"id": "T1071", "name": "", "severity": ""}],
    "related_mitre_tactics": [{"id":"TA0011", "name": ""}]
    }
    

##### Output messages

The **Enrich Hash** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following hashes using VirusTotal: ENTITY_IDS.` `Action wasn't able to enrich the following hashes using VirusTotal: ENTITY_IDS.` `No hashes were enriched.` `The following whitelisted engines were not found in VirusTotal: ENGINE_NAMES.` | The action succeeded.  
`Error executing action "Enrich Hash". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Hash** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich IOC

Use the **Enrich IOC** action to enrich the indicators of compromise (IoCs) using information from VirusTotal.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Enrich IOC** action requires the following parameters:

Parameter | Description  
---|---  
`IOC Type` | Optional. The type of the IoC to enrich.The default value is `Filehash`. The possible values are as follows:

  * `Filehash`
  * `URL`
  * `Domain`
  * `IP Address`

  
`IOCs` | Required. A comma-separated list of IoCs to enrich.  
`Widget Theme` | Optional. The theme to use for the VirusTotal widget. The possible values are as follows:

  * `Light`
  * `Dark`
  * `Chronicle`

The default value is `Dark`.  
`Fetch Widget` | Optional. If selected, the action retrieves and includes the visual summary widget related to the IoC in the Case Wall output. Enabled by default.  
  
#### Action outputs

The **Enrich IOC** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Enrich IOC** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Enrich IOC** action can provide the following table for every enriched entity:

Table name: **IOC_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



##### JSON result

The following example shows the JSON result output received when using the **Enrich IOC** action:
    
    
    {
        "ioc": {
            "identifier": "203.0.113.1",
            "details": {
                "attributes": {
                    "categories": {
                        "Dr.Web": "known infection source/not recommended site",
                        "Forcepoint ThreatSeeker": "compromised websites",
                        "sophos": "malware repository, spyware and malware"
                    },
                    "first_submission_date": 1582300443,
                    "html_meta": {},
                    "last_analysis_date": 1599853405,
                    "last_analysis_results": {
                        "EXAMPLELabs": {
                            "category": "harmless",
                            "engine_name": "EXAMPLELabs",
                            "method": "blacklist",
                            "result": "clean"
                        },
                        "Example": {
                            "category": "harmless",
                            "engine_name": "Example",
                            "method": "blacklist",
                            "result": "clean"
                        }
                    },
                    "last_analysis_stats": {
                        "harmless": 64,
                        "malicious": 6,
                        "suspicious": 1,
                        "timeout": 0,
                        "undetected": 8
                    },
                    "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                    "last_http_response_code": 404,
                    "last_http_response_content_length": 204,
                    "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                    "last_http_response_headers": {
                        "connection": "keep-alive",
                        "content-length": "204",
                        "content-type": "text/html; charset=iso-8859-1",
                        "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                        "keep-alive": "timeout=60",
                        "server": "nginx"
                    },
                    "last_modification_date": 1599853921,
                    "last_submission_date": 1599853405,
                    "reputation": 0,
                    "tags": [
                        "ip"
                    ],
                    "targeted_brand": {},
                    "threat_names": [
                        "Mal/HTMLGen-A"
                    ],
                    "times_submitted": 3,
                    "title": "404 Not Found",
                    "total_votes": {
                        "harmless": 0,
                        "malicious": 0
                    },
                    "trackers": {},
                    "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
                },
                "id": "ID",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/urls/ID"
                },
                "type": "url",
            "report_link": "{generated report link}",
                "widget_url": "https: //www.virustotal.com/ui/widget/html/WIDGET_ID"
    "widget_html"
            }
        }
    }
    

##### Output messages

The **Enrich IOC** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following IOCs using VirusTotal: IOC_LIST` `No information found for the following IOCs using VirusTotal: IOC_LIST` `No information about IOCs were found` | The action succeeded.  
`Error executing action "Enrich IOC". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich IOC** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich IP

Use the **Enrich IP** action to enrich IP addresses using information from VirusTotal.

This action runs on the Google SecOps `IP Address` entity.

#### Action inputs

The **Enrich IP** action requires the following parameters:

Parameter | Description  
---|---  
`Engine Threshold` | Optional. The minimum number of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines.  
`Engine Percentage Threshold` | Optional. The minimum percentage (from `0` to `100`, inclusive) of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines. If you configure both `Engine Threshold` and `Engine Percentage Threshold`, the action uses the `Engine Threshold` value.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Retrieve Comments` | Optional. If selected, the action retrieves comments associated with the IP address from VirusTotal. Enabled by default.  
`Create Insight` | Optional. If selected, the action generates a security insight containing the analysis information for the IP address. Enabled by default.  
`Only Suspicious Entity Insight` | Optional. If selected, the action generates insights only for IP addresses identified as suspicious based on the configured threshold parameters. This parameter only applies if `Create Insight` is enabled. Disabled by default.  
`Max Comments To Return` | Optional. The maximum number of comments the action retrieves during each run. The default value is `10`.  
`Widget Theme` | Optional. The theme to use for the VirusTotal widget. The possible values are as follows:

  * `Light`
  * `Dark`
  * `Chronicle`

The default value is `Dark`.  
`Fetch Widget` | Optional. If selected, the action retrieves and includes the visual summary widget related to the IP address in the Case Wall output. Enabled by default.  
  
#### Action outputs

The **Enrich IP** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Enrich IP** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Enrich IP** action can provide the following table for every enriched entity:

Table name: **ENTITY_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



The **Enrich IP** action can provide the following table for every entity that has comments:

Table name: **Comments: ENTITY_ID**

Table columns:

  * **Date**
  * **Comment**
  * **Abuse Votes**
  * **Negative Votes**
  * **Positive Votes**
  * **ID**



##### Entity enrichment table

The following table lists the fields enriched using the **Enrich IP** action:

Enrichment field name | Applicability  
---|---  
`VT3_id` | Applies when available in the JSON result.  
`VT3_owner` | Applies when available in the JSON result.  
`VT3_asn` | Applies when available in the JSON result.  
`VT3_continent` | Applies when available in the JSON result.  
`VT3_country` | Applies when available in the JSON result.  
`VT3_harmless_count` | Applies when available in the JSON result.  
`VT3_malicious_count` | Applies when available in the JSON result.  
`VT3_suspicious_count` | Applies when available in the JSON result.  
`VT3_undetected_count` | Applies when available in the JSON result.  
`VT3_certificate_valid_not_after` | Applies when available in the JSON result.  
`VT3_certificate_valid_not_before` | Applies when available in the JSON result.  
`VT3_reputation` | Applies when available in the JSON result.  
`VT3_tags` | Applies when available in the JSON result.  
`VT3_malicious_vote_count` | Applies when available in the JSON result.  
`VT3_harmless_vote_count` | Applies when available in the JSON result.  
`VT3_report_link` | Applies when available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich IP** action:
    
    
    {
        "data": {
            "attributes": {
                "as_owner": "Example",
                "asn": 50673,
                "continent": "EU",
                "country": "NL",
                "last_analysis_results": {
                    "EXAMPLELabs": {
                        "category": "harmless",
                        "engine_name": "ExampleLabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "example.com URL checker": {
                        "category": "harmless",
                        "engine_name": "example.com URL checker",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "example": {
                        "category": "harmless",
                        "engine_name": "example",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "example": {
                        "category": "harmless",
                        "engine_name": "example",
                        "method": "blacklist",
                        "result": "clean"
                    }
                },
                "last_analysis_stats": {
                    "harmless": 81,
                    "malicious": 5,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_https_certificate": {
                    "cert_signature": {
                        "signature": "48ae0d5d0eb411e56bd328b93c7212c72fd21785070648e11d9ae2b80386711699978e650eafa233d234671b87c8134c1c38c59f702518ddebdc7849dc512e0158941507970ab3ab93788d27df728d727d7f9d28ed358abb145fb24803d0eeab04687ae07c7f1d3176374367efc000bd26d3cfc0659e54826ea2dfa2366d7bd9e8ed3bd2ff8a26898b37fadea198f93de8cf3ae3d703513bc0638f7b411d8eda9a3ac9a7510d7bfe553592792d10f8b2c255bc4a05c8c6bfbdb8def045dc754b39c9b89d2a5140818622760eb116abf6fd0a5798c1e274fe56a056ed21f419a6873d314c15238a398d8049b5ecc1ca003d0a07a989a710d137e4fc74b5671caa",
                        "signature_algorithm": "sha256RSA"
                    },
                    "extensions": {
                        "1.3.6.1.4.1.11129.2.4.2": "0481f200f00075007d3ef2f88fff88556824c2c0ca9e5289792bc50e78097f2e",
                        "CA": true,
                        "authority_key_identifier": {
                            "keyid": "KEY_ID"
                        },
                        "ca_information_access": {
                            "CA Issuers": "http://example.RSADomainValidationSecureServerCA.crt",
                            "OCSP": "http://example.com"
                        },
                        "certificate_policies": [
                            "1.3.6.1.4.1.6449.1.2.2.7",
                            "2.23.140.1.2.1"
                        ],
                        "extended_key_usage": [
                            "serverAuth",
                            "clientAuth"
                        ],
                        "key_usage": [
                            "ff"
                        ],
                        "subject_alternative_name": [
                            "example-panel.xyz",
                            "www.example-panel.xyz"
                        ],
                        "subject_key_identifier": "4f6429eaccd761eca91d9120b004f9d962453fef",
                        "tags": []
                    },
                    "issuer": {
                        "C": "US",
                        "CN": "Example RSA Domain Validation Secure Server CA",
                        "L": "Mountain View",
                        "O": "Example Ltd.",
                    },
                    "public_key": {
                        "algorithm": "RSA",
                        "rsa": {
                            "exponent": "010001",
                            "key_size": 2048,
                            "modulus": "00aa8b74f0cc92a85ed4d515abef751a22fd65f2b6b0d33239040a99c65f322f3e833c77540a15ee31dabbd2889dd710ff9d8ccd3b9ea454ca87761cd9ff8a383806986461f8ff764a1202a5ebfb09995cbf40cc11eb2514529704744e6c97a872cde728e278fb140eba3c3aaf60644c8d75fd0048bb506f9b7314e33690f3514598ee45dd366c30a94d6178af91c2784872c162233c66659cea675f22f47752e0877ba5b12a3d800d2e2510d3cc1222c226cee2b85852a7e02da1de2718c746560f3ae05bc6f2d7f1cd6fcdbe37318fc7ddd19ae3486c5f3293946c068735e843fa8467199456d4725ac0b23fc4e0b7b9d3f51c0e16b27542d250d29d7b28fb95"
                        }
                    },
                    "serial_number": "248562d360bcc919bb97883f0dfc609d",
                    "signature_algorithm": "sha256RSA",
                    "size": 1472,
                    "subject": {
                        "CN": "example-panel.xyz"
                    },
                    "tags": [],
                    "thumbprint": "f9aae62cc9262302e45d94fcc512d65529ea1b31",
                    "thumbprint_sha256": "406ac0efb0ef67de743b1ab0f4e0352564a7d5ebbd71e3a883c067acc3563016",
                    "validity": {
                        "not_after": "2021-08-06 23:59:59",
                        "not_before": "2020-08-06 00:00:00"
                    },
                    "version": "V3"
                },
                "last_https_certificate_date": 1605415789,
                "last_modification_date": 1605430702,
                "network": "203.0.113.0/24",
                "regional_internet_registry": "EXAMPLE",
                "reputation": -95,
                "tags": [],
                "total_votes": {
                    "harmless": 0,
                    "malicious": 10
                },
                "whois": "NetRange: 203.0.113.0 - 203.0.113.255\nCIDR: 203.0.113.0/24\nNetName: EXAMPLE-5\nNetHandle: NET-203-0-113-0-1\nParent: ()\nNetType: Allocated to EXAMPLE\nOrig",
                "whois_date": 1603912270
            },
            "id": "203.0.113.1",
            "links": {
                "self": "https://www.virustotal.com/api/v3/ip_addresses/203.0.113.1"
            },
            "type": "ip_address"
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true
    }
    

##### Output messages

The **Enrich IP** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following IPs using VirusTotal: ENTITY_ID` `Action wasn't able to enrich the following IPs using VirusTotal: ENTITY_ID` `No IPs were enriched.` `The following whitelisted engines were not found in VirusTotal: ENGINE_NAMES` | The action succeeded.  
`Error executing action "Enrich IP". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich IP** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich URL

Use the **Enrich URL** action to enrich a URL using information from VirusTotal.

This action runs on the Google SecOps `URL` entity.

#### Action inputs

The **Enrich URL** action requires the following parameters:

Parameter | Description  
---|---  
`Engine Threshold` | Optional. The minimum number of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines.  
`Engine Percentage Threshold` | Optional. The minimum percentage (from `0` to `100`, inclusive) of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines. If you configure both `Engine Threshold` and `Engine Percentage Threshold`, the action uses the `Engine Threshold` value.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Resubmit URL` | Optional. If selected, the action resubmits the URL for analysis rather than using existing results. Disabled by default.  
`Resubmit After (Days)` | Optional. The minimum number of days that must elapse since the last analysis before the hash is resubmitted. This parameter only applies if you select the `Resubmit Hash` parameter. The default value is `30`.  
`Retrieve Comments` | Optional. If selected, the action retrieves comments associated with the URL from VirusTotal. Enabled by default.  
`Create Insight` | Optional. If selected, the action generates a security insight containing the analysis information for the URL. Enabled by default.  
`Only Suspicious Entity Insight` | Optional. If selected, the action generates insights only for URLs identified as suspicious based on the configured threshold parameters. This parameter only applies if `Create Insight` is enabled. Disabled by default.  
`Max Comments To Return` | Optional. The maximum number of comments the action retrieves during each run. The default value is `10`.  
`Widget Theme` | Optional. The theme to use for the VirusTotal widget. The possible values are as follows:

  * `Light`
  * `Dark`
  * `Chronicle`

The default value is `Dark`.  
`Fetch Widget` | Optional. If selected, the action retrieves and includes the visual summary widget related to the URL in the Case Wall output. Enabled by default.  
  
#### Action outputs

The **Enrich URL** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Enrich URL** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Enrich URL** action can provide the following table for every enriched entity:

Table name: **ENTITY_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



The **Enrich URL** action can provide the following table for every entity that has comments:

Table name: **Comments: ENTITY_ID**

Table columns:

  * **Date**
  * **Comment**
  * **Abuse Votes**
  * **Negative Votes**
  * **Positive Votes**
  * **ID**



##### Entity enrichment table

The following table lists the fields enriched using the **Enrich URL** action:

Enrichment field name | Applicability  
---|---  
`VT3_id` | Applies when available in the JSON result.  
`VT3_title` | Applies when available in the JSON result.  
`VT3_last_http_response_code` | Applies when available in the JSON result.  
`VT3_last_http_response_content_length` | Applies when available in the JSON result.  
`VT3_threat_names` | Applies when available in the JSON result.  
`VT3_harmless_count` | Applies when available in the JSON result.  
`VT3_malicious_count` | Applies when available in the JSON result.  
`VT3_suspicious_count` | Applies when available in the JSON result.  
`VT3_undetected_count` | Applies when available in the JSON result.  
`VT3_reputation` | Applies when available in the JSON result.  
`VT3_tags` | Applies when available in the JSON result.  
`VT3_malicious_vote_count` | Applies when available in the JSON result.  
`VT3_harmless_vote_count` | Applies when available in the JSON result.  
`VT3_report_link` | Applies when available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich URL** action:
    
    
    {
        "data": {
            "attributes": {
                "categories": {
                    "Dr.Web": "known infection source/not recommended site",
                    "Forcepoint ThreatSeeker": "compromised websites",
                    "sophos": "malware repository, spyware and malware"
                },
                "first_submission_date": 1582300443,
                "html_meta": {},
                "last_analysis_date": 1599853405,
                "last_analysis_results": {
                    "AEXAMPLELabs": {
                        "category": "harmless",
                        "engine_name": "EXAMPLELabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Example": {
                        "category": "harmless",
                        "engine_name": "Example",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "last_analysis_stats": {
                    "harmless": 64,
                    "malicious": 6,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                "last_http_response_code": 404,
                "last_http_response_content_length": 204,
                "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                "last_http_response_headers": {
                    "connection": "keep-alive",
                    "content-length": "204",
                    "content-type": "text/html; charset=iso-8859-1",
                    "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                    "keep-alive": "timeout=60",
                    "server": "nginx"
                },
                "last_modification_date": 1599853921,
                "last_submission_date": 1599853405,
                "reputation": 0,
                "tags": [
                    "ip"
                ],
                "targeted_brand": {},
                "threat_names": [
                    "Mal/HTMLGen-A"
                ],
                "times_submitted": 3,
                "title": "404 Not Found",
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/ID"
            },
            "type": "url",
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true
    }
    

##### Output messages

The **Enrich URL** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following URLs using VirusTotal: ENTITY_ID` `Action wasn't able to enrich the following URLs using VirusTotal: ENTITY_ID` `No URLs were enriched.` `The following whitelisted engines were not found in VirusTotal: ENGINE_NAMES` `Waiting for action to retrieve results for the following URLs: URLS` | The action succeeded.  
`Error executing action "Enrich URL". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich URL** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Domain Details

Use the **Get Domain Details** action to retrieve detailed information about the domain using information from VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `Hostname`
  * `URL`



#### Action inputs

The **Get Domain Details** action requires the following parameters:

Parameter | Description  
---|---  
`Engine Threshold` | Optional. The minimum number of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines.  
`Engine Percentage Threshold` | Optional. The minimum percentage (from `0` to `100`, inclusive) of engines that must flag an entity as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines. If you configure both `Engine Threshold` and `Engine Percentage Threshold`, the action uses the `Engine Threshold` value.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Retrieve Comments` | Optional. If selected, the action retrieves comments associated with the domain from VirusTotal. Enabled by default.  
`Create Insight` | Optional. If selected, the action generates a security insight containing the analysis information for the domain. Enabled by default.  
`Only Suspicious Entity Insight` | Optional. If selected, the action generates insights only for entities identified as suspicious based on the configured threshold parameters. This parameter only applies if `Create Insight` is enabled. Disabled by default.  
`Max Comments To Return` | Optional. The maximum number of comments the action retrieves for the domain during each run. The default value is `10`.  
`Widget Theme` | Optional. The theme to use for the VirusTotal widget. The possible values are as follows:

  * `Light`
  * `Dark`
  * `Chronicle`

The default value is `Dark`.  
`Fetch Widget` | Optional. If selected, the action retrieves and includes the visual summary widget related to the domain in the Case Wall output. Enabled by default.  
  
#### Action outputs

The **Get Domain Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Get Domain Details** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Get Domain Details** action can provide the following table for every enriched entity:

Table name: **ENTITY_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



The **Get Domain Details** action can provide the following table for every entity that has comments:

Table name: **Comments: ENTITY_ID**

Table columns:

  * **Date**
  * **Comment**
  * **Abuse Votes**
  * **Negative Votes**
  * **Positive Votes**
  * **ID**



##### JSON result

The following example shows the JSON result output received when using the **Get Domain Details** action:
    
    
    {
        "data": {
            "attributes": {
                "categories": {
                    "Dr.Web": "known infection source/not recommended site",
                    "Forcepoint ThreatSeeker": "compromised websites",
                    "sophos": "malware repository, spyware and malware"
                },
                "first_submission_date": 1582300443,
                "html_meta": {},
                "last_analysis_date": 1599853405,
                "last_analysis_results": {
                    "EXAMPLELabs": {
                        "category": "harmless",
                        "engine_name": "EXAMPLELabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Example": {
                        "category": "harmless",
                        "engine_name": "Example",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "last_analysis_stats": {
                    "harmless": 64,
                    "malicious": 6,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                "last_http_response_code": 404,
                "last_http_response_content_length": 204,
                "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                "last_http_response_headers": {
                    "connection": "keep-alive",
                    "content-length": "204",
                    "content-type": "text/html; charset=iso-8859-1",
                    "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                    "keep-alive": "timeout=60",
                    "server": "nginx"
                },
                "last_modification_date": 1599853921,
                "last_submission_date": 1599853405,
                "reputation": 0,
                "tags": [
                    "ip"
                ],
                "targeted_brand": {},
                "threat_names": [
                    "Mal/HTMLGen-A"
                ],
                "times_submitted": 3,
                "title": "404 Not Found",
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/ID"
            },
            "type": "url",
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true
    }
    

##### Output messages

The **Get Domain Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following domains using VirusTotal: DOMAINS` `Action wasn't able to return details about the following domains using VirusTotal: DOMAINS` `The following whitelisted engines were not found in VirusTotal: ENGINE_NAMES` | The action succeeded.  
`Error executing action "Get Domain Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Domain Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Graph Details

Use the **Get Graph Details** action to obtain detailed information about graphs in VirusTotal.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Graph Details** action requires the following parameters:

Parameter | Description  
---|---  
`Graph ID` | Required. A comma-separated list of graph IDs for which to retrieve details.  
`Max Links To Return` | Optional. The maximum number of links to return for each graph. The default value is `50`.  
  
#### Action outputs

The **Get Graph Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Graph Details** action can provide the following table for every enriched entity:

Table name: **Graph ENTITY_ID Links**

Table columns:

  * **Source**
  * **Target**
  * **Connection Type**



##### JSON result

The following example shows the JSON result output received when using the **Get Graph Details** action:
    
    
    {
        "data": {
            "attributes": {
                "comments_count": 0,
                "creation_date": 1603219837,
                "graph_data": {
                    "description": "Example LLC",
                    "version": "api-5.0.0"
                },
                "last_modified_date": 1603219837,
                "links": [
                    {
                        "connection_type": "last_serving_ip_address",
                        "source": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671"
                    },
                    {
                        "connection_type": "last_serving_ip_address",
                        "source": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "203.0.113.3"
                    },
                    {
                        "connection_type": "network_location",
                        "source": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671"
                    },
                    {
                        "connection_type": "network_location",
                        "source": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "203.0.113.3"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "203.0.113.3",
                        "target": "relationships_communicating_files_20301133"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "4935cc8a4ff76d595e1bfab9fd2e6aa0f7c2fea941693f1ab4586eaba1528f47"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "c975794ff65c02b63fae1a94006a75294aac13277ca464e3ea7e40de5eda2b14"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "c7752154a2e894a4dec84833bee656357f4b84a9c7f601f586f79de667d8fe5c"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "692bb2ed1da43b0408c104b4ca4b4e97e15f3224e37dbea60214bcd991a2cfd3"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "74273ef55d8b7d23f7b058c7e47f3cbaf60c823a3e41ffb10e494917bad77381"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "f4f2f17c4df1b558cb80c8eab3edf5198970e9d87bd03943d4c2effafb696187"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "5edc8496869697aa229540bd6106b6679f6cfcbc6ee4837887183f470b49acb5"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "1582da57cb082d3f6835158133aafb5f3b8dcc880a813be135a0ff8099cf0ee8"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "be4ccb1ca71a987f481c22a1a43de491353945d815c89cbcc06233d993ac73cf"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "60bb6467ee465f23a15f17cd73f7ecb9db9894c5a3186081a1c70fdc6e7607d6"
                    }
                ],
                "nodes": [
                    {
                        "entity_attributes": {
                            "has_detections": false
                        },
                        "entity_id": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 0,
                        "text": "",
                        "type": "url",
                        "x": 51.22276722115952,
                        "y": 65.7811310194184
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 1,
                        "text": "",
                        "type": "relationship",
                        "x": 25.415664700492094,
                        "y": 37.66636498768037
                    },
                    {
                        "entity_attributes": {
                            "country": "US"
                        },
                        "entity_id": "203.0.113.3",
                        "fx": -19.03611541222395,
                        "fy": 24.958500220062717,
                        "index": 2,
                        "text": "",
                        "type": "ip_address",
                        "x": -19.03611541222395,
                        "y": 24.958500220062717
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 3,
                        "text": "",
                        "type": "relationship",
                        "x": 14.37403861978968,
                        "y": 56.85562691824892
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_communicating_files_20301133",
                        "index": 4,
                        "text": "",
                        "type": "relationship",
                        "x": -51.78097726144755,
                        "y": 10.087893225996158
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "4935cc8a4ff76d595e1bfab9fd2e6aa0f7c2fea941693f1ab4586eaba1528f47",
                        "index": 5,
                        "text": "",
                        "type": "file",
                        "x": -79.11606194776019,
                        "y": -18.475026322309112
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "c975794ff65c02b63fae1a94006a75294aac13277ca464e3ea7e40de5eda2b14",
                        "index": 6,
                        "text": "",
                        "type": "file",
                        "x": -64.80938048199627,
                        "y": 46.75892061191275
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "c7752154a2e894a4dec84833bee656357f4b84a9c7f601f586f79de667d8fe5c",
                        "index": 7,
                        "text": "",
                        "type": "file",
                        "x": -43.54064004476819,
                        "y": -28.547923020662786
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "692bb2ed1da43b0408c104b4ca4b4e97e15f3224e37dbea60214bcd991a2cfd3",
                        "index": 8,
                        "text": "",
                        "type": "file",
                        "x": -15.529860440278318,
                        "y": -2.068209789825876
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "74273ef55d8b7d23f7b058c7e47f3cbaf60c823a3e41ffb10e494917bad77381",
                        "index": 9,
                        "text": "",
                        "type": "file",
                        "x": -42.55971948293377,
                        "y": 46.937155845680415
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "html"
                        },
                        "entity_id": "f4f2f17c4df1b558cb80c8eab3edf5198970e9d87bd03943d4c2effafb696187",
                        "index": 10,
                        "text": "",
                        "type": "file",
                        "x": -62.447976875107706,
                        "y": -28.172418384729067
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "5edc8496869697aa229540bd6106b6679f6cfcbc6ee4837887183f470b49acb5",
                        "index": 11,
                        "text": "",
                        "type": "file",
                        "x": -89.0326649183805,
                        "y": -2.2638551448322484
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "1582da57cb082d3f6835158133aafb5f3b8dcc880a813be135a0ff8099cf0ee8",
                        "index": 12,
                        "text": "",
                        "type": "file",
                        "x": -26.35260716195174,
                        "y": -20.25669077264115
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "be4ccb1ca71a987f481c22a1a43de491353945d815c89cbcc06233d993ac73cf",
                        "index": 13,
                        "text": "",
                        "type": "file",
                        "x": -82.1415994911387,
                        "y": 34.89636762607467
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "ENTITY_ID",
                        "index": 14,
                        "text": "",
                        "type": "file",
                        "x": -90.87738694680043,
                        "y": 16.374462198116138
                    }
                ],
                "private": false,
                "views_count": 30
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/graphs/ID"
            },
            "type": "graph"
        }
    }
    

##### Output messages

The **Get Graph Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following graphs in VirusTotal: GRAPH_IDS` `Action wasn't able to return details about the following graphs in VirusTotal: GRAPH_IDS` `No information about the provided graphs was found.` | The action succeeded.  
`Error executing action "Get Graph Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Graph Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Related Domains

Use the **Get Related Domains** action to obtain the domains related to the provided entities from VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.**Important:** To run the **Get Related Domains** action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Get Related Domains** action requires the following parameters:

Parameter | Description  
---|---  
`Results` | Optional. The structure used to aggregate and group the returned JSON results. The possible values are as follows:

  * `Combined`: The action returns all unique results for the provided entities.
  * `Per Entity`: The action returns all unique items for every entity.

The default value is `Combined`.  
`Max Domains To Return` | Optional. The maximum number of domains to return. If you select `Combined` in the `Results` parameter, the action returns the configured number of domains for all entities. If you select `Per Entity` in the `Results` parameter, the action returns the configured number of domains for every entity. The default value is `40`.  
  
#### Action outputs

The **Get Related Domains** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Related Domains** action:
    
    
    {
        "domain": ["example.com"]
    }
    

##### Output messages

The **Get Related Domains** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related domains for the provided entities from VirusTotal.` `No related domains were found for the provided entities from VirusTotal.` | The action succeeded.  
`Error executing action "Get Related Domains". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related Domains** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Related Hashes

Use the **Get Related Hashes** action to obtain the hashes related to the provided entities from VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.**Important:** To run the **Get Related Hashes** action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Get Related Hashes** action requires the following parameters:

Parameter | Description  
---|---  
`Results` | Optional. The structure used to aggregate and group the returned JSON results. The possible values are as follows:

  * `Combined`: The action returns all unique results for the provided entities.
  * `Per Entity`: The action returns all unique items for every entity.

The default value is `Combined`.  
`Max Hashes To Return` | Optional. The maximum number of file hashes to return. If you select `Combined` in the `Results` parameter, the action returns the configured number of hashes for all entities. If you select `Per Entity` in the `Results` parameter, the action returns the configured number of hashes for every entity. The default value is `40`.  
  
#### Action outputs

The **Get Related Hashes** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Related Hashes** action:
    
    
    {
        "sha256_hashes": ["http://example.com"]
    }
    

##### Output messages

The **Get Related Hashes** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related hashes for the provided entities from VirusTotal.` `No related hashes were found for the provided entities from VirusTotal.` | The action succeeded.  
`Error executing action "Get Related Hashes". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related Hashes** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Related IPs

Use the **Get Related IPs** action to obtain the IP addresses related to the provided entities from VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `URL`

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.**Important:** To run the **Get Related IPs** action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Get Related IPs** action requires the following parameters:

Parameter | Description  
---|---  
`Results` | Optional. The structure used to aggregate and group the returned JSON results. The possible values are as follows:

  * `Combined`: The action returns all unique results for the provided entities.
  * `Per Entity`: The action returns all unique items for every entity.

The default value is `Combined`.  
`Max IPs To Return` | Optional. The maximum number of IP addresses to return. If you select `Combined` in the `Results` parameter, the action returns the configured number of IP addresses for all entities. If you select `Per Entity` in the `Results` parameter, the action returns the configured number of IP addresses for every entity. The default value is `40`.  
  
#### Action outputs

The **Get Related IPs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Related IPs** action:
    
    
    {
        "ips": ["203.0.113.1"]
    }
    

##### Output messages

The **Get Related IPs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related IPs to the provided entities from VirusTotal.` `No related IPs were found to the provided entities from VirusTotal.` | The action succeeded.  
`Error executing action "Get Related IPs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related IPs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Related URLs

Use the **Get Related URLs** action to obtain the URLs related to the provided entities from VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.**Important:** To run the **Get Related URLs** action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Get Related URLs** action requires the following parameters:

Parameter | Description  
---|---  
`Results` | Optional. The structure used to aggregate and group the returned JSON results. The possible values are as follows:

  * `Combined`: The action returns all unique results for the provided entities.
  * `Per Entity`: The action returns all unique items for every entity.

The default value is `Combined`.  
`Max URLs To Return` | Optional. The maximum number of URLs to return. If you select `Combined` in the `Results` parameter, the action returns the configured number of URLs for all entities. If you select `Per Entity` in the `Results` parameter, the action returns the configured number of URLs for every entity. The default value is `40`.  
  
#### Action outputs

The **Get Related URLs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Related URLs** action:
    
    
    {
        "urls": ["http://example.com"]
    }
    

##### Output messages

The **Get Related URLs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related URLs to the provided entities from VirusTotal.` `No related URLs were found to the provided entities from VirusTotal.` | The action succeeded.  
`Error executing action "Get Related URLs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related URLs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to VirusTotal.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

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

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the VirusTotal server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the VirusTotal server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search Entity Graphs

Use the **Search Entity Graphs** action to search graphs that are based on the entities in VirusTotal.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `Threat Actor`
  * `URL`
  * `User`

**Note:** This action only supports the MD5, SHA-1, and SHA-256 hashes.

#### Action inputs

The **Search Entity Graphs** action requires the following parameters:

Parameter | Description  
---|---  
`Sort Field` | Optional. The field used to order and sequence the returned VirusTotal graphs. The possible values are as follows:

  * `Owner`
  * `Creation Date`
  * `Last Modified Date`
  * `Views Count`
  * `Comments Count`

The default value is `Owner`.  
`Max Graphs To Return` | Optional. The maximum number of graphs to return. The default value is `10`.  
  
#### Action outputs

The **Search Entity Graphs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search Entity Graphs** action:
    
    
    {
        "data": [
            {
                "attributes": {
                    "graph_data": {
                        "description": "EXAMPLE",
                        "version": "5.0.0"
                    }
                },
                "id": "ID",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/graphs/ID"
                },
                "type": "graph"
            },
            {
                "attributes": {
                    "graph_data": {
                        "description": "Example Feb2020",
                        "version": "5.0.0"
                    }
                },
                "id": "ID_2",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/graphs/ID_2"
                },
                "type": "graph"
            }
        ],
        "links": {
            "next": "https://www.virustotal",
            "self": "https://www.virustotal.com/api/v3/graphs?filter=ip_address:203.0.113.3%20OR%20file:FILE_ID&order=last_modified_date&limit=2&attributes=graph_data"
        },
        "meta": {
            "cursor": "True:CsEGCo0CCusBAP8_vihw3_S_"
        }
    }
    

##### Output messages

The **Search Entity Graphs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned graphs based on the provided entities in VirusTotal.` `Action wasn't able to successfully return graph based on the provided entities on VirusTotal. Reason: ERROR_REASON.` `No graphs were found for the provided entities.` | The action succeeded.  
`Error executing action "Search Entity Graphs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
### Search Graphs

Use the **Search Graphs** action to search graphs based on custom filters in VirusTotal.

This action doesn't run on Google SecOps entities. 

Parameter | Description  
---|---  
`Query` | Required. The query filter for the graph. For more information about queries, see How to create queries and Graph-related modifiers.  
`Sort Field` | Optional. The field used to order and sequence the returned VirusTotal graphs. The possible values are as follows:

  * `Owner`
  * `Creation Date`
  * `Last Modified Date`
  * `Views Count`
  * `Comments Count`

The default value is `Owner`.  
`Max Graphs To Return` | Optional. The maximum number of graphs to return. The default value is `10`.  
  
#### How to create queries

To refine search results from graphs, create queries that contain graph-related modifiers. To improve the search, you can combine modifiers with `AND`, `OR`, and `NOT` operators.

Date and numeric fields support plus (`+`) or minus (`-`) suffixes. A plus suffix matches values greater than the provided value. A minus suffix matches values less than the provided value. Without a suffix, the query returns exact matches.

To define ranges, you can use the same modifier multiple times in a query. For example, to search graphs that are created between 2018-11-15 and 2018-11-20, use the following query:
    
    
    creation_date:2018-11-15+ creation_date:2018-11-20-
    

For dates or months that begin with `0`, remove the `0` character in the query. For example, format the date of 2018-11-01 as `2018-11-1`.

##### Graph-related modifiers

The following table lists modifiers which you can use to construct the search query:

Modifier | Description | Example  
---|---|---  
`Id` | Filters by graph identifier. | `id:g675a2fd4c8834e288af`  
`Name` | Filters by graph name. | `name:Example-name`  
`Owner` | Filters by graphs owned by the user. | `owner:example_user`  
`Group` | Filters by graphs owned by a group. | `group:example`  
`Visible_to_user` | Filters by graphs visible to the user. | `visible_to_user:example_user`  
`Visible_to_group` | Filters by graphs visible to the group. | `visible_to_group:example`  
`Private` | Filters by private graphs. | `private:true`, `private:false`  
`Creation_date` | Filters by the graph creation date. | `creation_date:2018-11-15`  
`last_modified_date` | Filters by the latest graph modification date. | `last_modified_date:2018-11-20`  
`Total_nodes` | Filters by graphs that contain a specific number of nodes. | `total_nodes:100`  
`Comments_count` | Filters by the number of comments in the graph. | `comments_count:10+`  
`Views_count` | Filters by the number of graph views. | `views_count:1000+`  
`Label` | Filters by graphs that contain nodes with a specific label. | `label:Kill switch`  
`File` | Filters by graphs that contain the specific file. | `file:131f95c51cc819465fa17`  
`Domain` | Filters by graphs that contain the specific domain. | `domain:example.com`  
`Ip_address` | Filters by graphs that contain the specific IP address. | `ip_address:203.0.113.1`  
`Url` | Filters by graphs that contain the specific URL. | `url:https://example.com/example/`  
`Actor` | Filters by graphs that contain the specific actor. | `actor:example actor`  
`Victim` | Filters by graphs that contain the specific victim. | `victim:example_user`  
`Email` | Filters by graphs that contain the specific email address. | `email:user@example.com`  
`Department` | Filters by graphs that contain the specific department. | `department:engineers`  
  
#### Action outputs

The **Search Graphs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search Graphs** action:
    
    
    {
        "data": [
            {
                "attributes": {
                    "graph_data": {
                        "description": "EXAMPLE",
                        "version": "5.0.0"
                    }
                },
                "id": "ID",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/graphs/ID"
                },
                "type": "graph"
            },
            {
                "attributes": {
                    "graph_data": {
                        "description": "Example Feb2020",
                        "version": "5.0.0"
                    }
                },
                "id": "ID_2",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/graphs/ID_2"
                },
                "type": "graph"
            }
        ],
        "links": {
            "next": "https://www.virustotal",
            "self": "https://www.virustotal.com/api/v3/graphs?filter=ip_address:203.0.113.3%20OR%20file:FILE_ID&order=last_modified_date&limit=2&attributes=graph_data"
        },
        "meta": {
            "cursor": "True:CsEGCo0CCusBAP8_vihw3_S_"
        }
    }
    

##### Output messages

The **Search Graphs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned graphs for the provided query in VirusTotal.` `Action wasn't able to successfully return graph for the provided query in VirusTotal. Reason: ERROR_REASON.` `No graphs were found for the provided query.` | The action succeeded.  
`Error executing action "Search Graphs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Graphs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search IOCs

Use the **Search IOCs** action to search for IOCs in the VirusTotal dataset.

This action doesn't run on Google SecOps entities. 

**Important:** To run this action, the VirusTotal Enterprise (VTE) is required.

#### Action inputs

The **Search IOCs** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required. The query string used to filter and search for IOCs in the dataset. To configure the query, follow the query syntax applicable to the VirusTotal Intelligence user interface. The default value is `""`.  
`Create Entities` | Optional. If selected, the action creates entities for the returned IOCs. This action does not enrich entities. Disabled by default.  
`Order By` | Required. The field used to determine the primary sorting criteria for the returned results. Entity types can have different order fields. For more information about how to search for files in VirusTotal, see [Advanced corpus search](https://docs.virustotal.com/reference/intelligence-search). The possible values are as follows:

  * `Use Default Order`
  * `Last Submission Date`
  * `First Submission Date`
  * `Positives`
  * `Times Submitted`
  * `Creation Date`
  * `Last Modification Date Last Update Date`

The default value is `Use Default Order`.  
`Sort Order` | Optional. The sort order of the results. The possible values are as follows:

  * `Ascending`
  * `Descending`

If you select `Use Default Order` in the `Order By` parameter, the action ignores this parameter. The default value is `Descending`.  
`Max IOCs To Return` | Optional. The maximum number of IoCs to return. The maximum value is `300`. The default value is `10`.  
  
#### Action outputs

The **Search IOCs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search IOCs** action:
    
    
    {
      "data": [
        {
          "attributes": {
            "type_description": "Email",
            "tlsh": "T1B4D31F04BE452B3093E7238E064E6FDBAFCC135F6611F1C60881AAD6C5C77A2E57D689",
            "exiftool": {
              "MIMEType": "text/plain",
              "FileType": "TXT",
              "WordCount": "2668",
              "LineCount": "1820",
              "MIMEEncoding": "us-ascii",
              "FileTypeExtension": "txt",
              "Newlines": "Windows CRLF"
            },
            "type_tags": [
              "internet",
              "email"
            ],
            "threat_severity": {
              "threat_severity_level": "SEVERITY_HIGH",
              "threat_severity_data": {
                "num_gav_detections": 3,
                "has_vulnerabilities": true,
                "popular_threat_category": "trojan",
                "type_tag": "email",
                "has_embedded_ips_with_detections": true
              },
              "last_analysis_date": "1698050597",
              "version": 2,
              "level_description": "Severity HIGH because it was considered trojan. Other contributing factors were that it has known exploits, it contains embedded IPs with detections and it could not be run in sandboxes."
            },
            "names": [
              "Re Example.eml"
            ],
            "last_modification_date": 1698057197,
            "type_tag": "email",
            "times_submitted": 1,
            "total_votes": {
              "harmless": 0,
              "malicious": 0
            },
            "size": 132299,
            "popular_threat_classification": {
              "suggested_threat_label": "obfsobjdat/malformed",
              "popular_threat_name": [
                {
                  "count": 8,
                  "value": "obfsobjdat"
                },
                {
                  "count": 2,
                  "value": "malformed"
                }
              ]
            },
            "last_submission_date": 1698049979,
            "last_analysis_results": {
              "Bkav": {
                "category": "undetected",
                "engine_name": "Example1",
                "engine_version": "2.0.0.1",
                "result": null,
                "method": "blacklist",
                "engine_update": "20231023"
              },
              "Lionic": {
                "category": "undetected",
                "engine_name": "Example2",
                "engine_version": "7.5",
                "result": null,
                "method": "blacklist",
                "engine_update": "20231023"
              },
            },
            "downloadable": true,
            "trid": [
              {
                "file_type": "file seems to be plain text/ASCII",
                "probability": 0
              }
            ],
            "sha256": "2d9df36964fe2e477e6e0f7a73391e4d4b2eeb0995dd488b431c4abfb4c27dbf",
            "type_extension": "eml",
            "tags": [
              "exploit",
              "cve-2018-0802",
              "cve-2018-0798",
              "email",
              "cve-2017-11882"
            ],
            "last_analysis_date": 1698049979,
            "unique_sources": 1,
            "first_submission_date": 1698049979,
            "ssdeep": "768:MedEkBNnx8ueVV+fitChi9KbpK0fixbRwHbcElIK944tCVQOgzdsSuom+cWmsCGY:Meo+fitC0mKuixYxlI1OO1cSPo0gptA",
            "md5": "bdfe36052e0c083869505ef4fd77e865",
            "sha1": "3a350de97009efe517ceffcea406534bb1ab800c",
            "magic": "SMTP mail, ASCII text, with CRLF line terminators",
            "last_analysis_stats": {
              "harmless": 0,
              "type-unsupported": 16,
              "suspicious": 0,
              "confirmed-timeout": 0,
              "timeout": 0,
              "failure": 0,
              "malicious": 28,
              "undetected": 32
            },
            "meaningful_name": "Re Example.eml",
            "reputation": 0
          },
          "type": "file",
          "id": "ID",
          "links": {
            "self": "URL"
          }
        },
      ]
    }
    

#### Output messages

The **Search IOCs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned IOCs based on the provided query from VirusTotal.` `The following IOCs were not created as new entities, as they already exist in the system: IOC_LIST` `No IOCs were found for the provided query.` | The action succeeded.  
`Error executing action "Search IOCs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search IOCs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Submit File

Use the **Submit File** action to submit a file and return results from VirusTotal.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Submit File** action requires the following parameters:

Parameter | Description  
---|---  
`File Paths` | Required. A comma-separated list of the absolute file paths on the local or remote server to submit. If you configure `Linux Server Address`, the action attempts to retrieve the file from the remote server.  
`Engine Threshold` | Optional. The minimum number of engines that must flag a file as malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines.  
`Engine Percentage Threshold` | Optional. The minimum percentage (from `0` to `100`, inclusive) of engines that must flag a file malicious or suspicious for it to be considered suspicious. If you configure `Engine Whitelist`, the action only includes results from the specified engines. If you configure both `Engine Threshold` and `Engine Percentage Threshold`, the action uses the `Engine Threshold` value.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Retrieve Comments` | Optional. If selected, the action retrieves comments associated with the file from VirusTotal. Comments are not fetched when `Private Submission` is enabled. Enabled by default.  
`Retrieve Sigma Analysis` | Optional. If selected, the action retrieves the Sigma analysis results for the file. Enabled by default.  
`Max Comments To Return` | Optional. The maximum number of comments the action retrieves during each run. The default value is `50`.  
`Linux Server Address` | Optional. The network location (IP address or hostname) of the source files on the remote Linux server.  
`Linux Username` | Optional. The authentication username for the remote Linux server.  
`Linux Password` | Optional. The authentication password for the remote Linux server.  
`Private Submission` | Optional. If selected, the action submits the file privately. To submit the file privately, the VirusTotal Premium access is required. Disabled by default.  
`Fetch MITRE Details` | Optional. If selected, the action retrieves MITRE ATT&CK techniques and tactics related to the hash. Disabled by default.  
`Lowest MITRE Technique Severity` | Optional. The minimum severity level for a MITRE ATT&CK technique to include in the results. The action treats `Unknown` as `Info`. The possible values are as follows:

  * `High`
  * `Medium`
  * `Low`
  * `Info`

The default value is `Low`.  
`Retrieve AI Summary` | Optional. If selected, the action retrieves an AI-generated summary for the file. This option is only available for private submissions. This parameter is experimental. Disabled by default.  
  
#### Action outputs

The **Submit File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Submit File** action can return the following links:

Name: **Report Link: PATH**

Value: URL

##### Case wall table

The **Submit File** action can provide the following table for every submitted file:

Table name: **Results: PATH**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



The **Submit File** action can provide the following table for every submitted file that has comments:

Table name: **Comments: PATH**

Table columns:

  * **Date**
  * **Comment**
  * **Abuse Votes**
  * **Negative Votes**
  * **Positive Votes**
  * **ID**



The **Submit File** action can provide the following table for every entity that has the Sigma analysis results:

Table name: **Sigma Analysis: ENTITY_ID**

Table columns:

  * **ID**
  * **Severity**
  * **Source**
  * **Title**
  * **Description**
  * **Match Context**



##### JSON result

The following example shows the JSON result output received when using the **Submit File** action:
    
    
    {
        "data": {
            "attributes": {
                "categories": {
                    "Dr.Web": "known infection source/not recommended site",
                    "Forcepoint ThreatSeeker": "compromised websites",
                    "sophos": "malware repository, spyware and malware"
                },
                "first_submission_date": 1582300443,
                "html_meta": {},
                "last_analysis_date": 1599853405,
                "last_analysis_results": {
                    "EXAMPLELabs": {
                        "category": "harmless",
                        "engine_name": "EXAMPLELabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Example": {
                        "category": "harmless",
                        "engine_name": "Example",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "last_analysis_stats": {
                    "harmless": 64,
                    "malicious": 6,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                "last_http_response_code": 404,
                "last_http_response_content_length": 204,
                "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                "last_http_response_headers": {
                    "connection": "keep-alive",
                    "content-length": "204",
                    "content-type": "text/html; charset=iso-8859-1",
                    "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                    "keep-alive": "timeout=60",
                    "server": "nginx"
                },
                "last_modification_date": 1599853921,
                "last_submission_date": 1599853405,
                "reputation": 0,
                "tags": [
                    "ip"
                ],
                "targeted_brand": {},
                "threat_names": [
                    "Mal/HTMLGen-A"
                ],
                "times_submitted": 3,
                "title": "404 Not Found",
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/ID"
            },
            "type": "url",
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true
    }
    

##### Output messages

The **Submit File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following files using VirusTotal: PATHS` `Action wasn't able to return details about the following files using VirusTotal: PATHS` `No details about the files were retrieved.` `The following whitelisted engines were not found in VirusTotal: ENGINE_NAMES` `Waiting for results for the following files: PATHS` | The action succeeded.  
`Error executing action "Submit File". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Submit File** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### VirusTotal - Livehunt Connector

Use the **VirusTotal - Livehunt Connector** to pull information about the VirusTotal Livehunt notifications and related files.

**Note:** The dynamic list works with the `rule_name` parameter.**Important:** This connector requires a VirusTotal Premium API token.

#### Connector rules

The **VirusTotal - Livehunt Connector** supports proxies.

#### Connector inputs

The **VirusTotal - Livehunt Connector** requires the following parameters:

Parameter | Description  
---|---  
`API Key` | Required. The VirusTotal API key.  
`Engine Percentage Threshold To Fetch` | Required. The minimum percentage threshold of security engines (`0` to `100`) that must flag a file as malicious or suspicious for the connector to ingest the file. The default value is `0`.  
`Engine Whitelist` | Optional. A comma-separated list of engine names for the action to consider when determining if a hash is malicious. The calculation excludes engines that provide no entity information. If no value is provided, the action uses all available engines.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `type`.  
`Max Hours Backwards` | Optional. The number of lookback hours to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Notifications To Fetch` | Optional. The maximum number of notifications to process in every connector run. The default value is `40`.  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Proxy Password` | Optional. The password for proxy server authentication.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The username for proxy server authentication.  
`PythonProcessTimeout` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Use dynamic list as a blacklist` | Optional. If selected, the connector uses the dynamic list as a blocklist. Disabled by default.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the VirusTotal server. Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
