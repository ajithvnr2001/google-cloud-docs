---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal/
title: Integrate VirusTotal with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:26:07.759382+00:00
---

# Integrate VirusTotal with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate VirusTotal with Google SecOps

This document explains how to integrate VirusTotal with Google Security Operations (Google SecOps).

This integration uses VirusTotal API v2.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/VirusTotal.zip).

**Note:** We recommended using the **Google Threat Intelligence** integration as it provides more capabilities and features.

## Before you begin

To use the VirusTotal integration, configure an API key.

To configure the API key, complete the following steps:

  1. Sign in to the VirusTotal portal.
  2. Under your username, click **API key**.
  3. Copy the generated API key to use it in the integration parameters.
  4. Click **Save**.



## Integration parameters

The VirusTotal integration requires the following parameters:

Parameter | Description  
---|---  
`Api Key` | Required.The API key to access VirusTotal.  
`Verify SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to VirusTotal.Not selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Get Domain Report

Use the **Get Domain Report** action to retrieve domain reports from VirusTotal for provided entities and enrich those entities within the Google SecOps platform.

This action runs on the following Google SecOps entities:

  * `User`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Get Domain Report** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment table

The **Get Domain Report** action can enrich the following fields:

Enrichment field name | Applicable logic  
---|---  
`Forcepoint ThreatSeeker category` | Returns if it exists in the JSON result.  
`BitDefender domain info` | Returns if it exists in the JSON result.  
`Categories` | Returns if it exists in the JSON result.  
`BitDefender Category` | Returns if it exists in the JSON result.  
`Alexa Category` | Returns if it exists in the JSON result.  
`Alexa domain info` | Returns if it exists in the JSON result.  
`Websense ThreatSeeker category` | Returns if it exists in the JSON result.  
`TrendMicro category` | Returns if it exists in the JSON result.  
`Opera domain info` | Returns if it exists in the JSON result.  
`Webutation domain info` | Returns if it exists in the JSON result.  
`verbose_msg` | Returns if it exists in the JSON result.  
`whois` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Domain Report** action:
    
    
    [
        {
            "EntityResult": {
                "detected_downloaded_samples": [],
                "undetected_downloaded_samples": [{
                    "date": "2018-08-08 22:48:28",
                    "positives": 0,
                    "sha256": "ef1955ae757c8b966c83248350331bd3a30f658ced11f387f8ebf05ab3368629",
                    "total": 59
                }],
                "resolutions": [{
                    "last_resolved": "2019-01-13 03:31:09",
                    "ip_address": "192.0.2.1"
                }],
                "Opera domain info": "The URL domain/host was seen to host badware at some point in time",
                "domain_siblings": [],
                "BitDefender domain info": "This URL domain/host was seen to host badware at some point in time",
                "whois": "Domain Name: EXAMPLE.CO.IN, nUpdated Date: 2018-05-22T09:30:37Z, nCreation Date: 2003-06-23T14:02:33Z, nRegistry Expiry Date: 2019-06-23T14:02:33Z, nDomain Status: clientDeleteProhibited, nDomain Status: clientTransferProhibited, nDomain Status: clientUpdateProhibited, nRegistrant Country: US, nName Server: NS1.EXAMPLE.COM, nName Server: NS2.EXAMPLE.COM, nName Server: NS3.EXAMPLE.COM, nName Server: NS4.EXAMPLE.COM, nDNSSEC: unsigned",
                "Alexa domain info": "example.co.in is one of the top 100 sites in the world and is in the Search_Engines category",
                "verbose_msg": "Domain found in dataset",
                "BitDefender category": "searchengines",
                "undetected_referrer_samples": [{
                    "date": "2019-02-05 13:20:39",
                    "positives": 0,
                    "sha256": "3baf9f2a2d2b152193d2af602378b71e40d381e835b0aa3111851b2f29e64f38",
                    "total": 71
                }],
                "whois_timestamp": 1548379042,
                "WOT domain info": {
                    "Vendor reliability": "Excellent",
                    "Child safety": "Excellent",
                    "Trustworthiness": "Excellent",
                    "Privacy": "Excellent"
                },
                "detected_referrer_samples": [{
                    "date": "2019-02-05 01:11:35",
                    "positives": 1,
                    "sha256": "097ea19b440441248b157698e2b23555cdf6117491b5f49f7ec8e492550cb02c",
                    "total": 70
                }],
                "Forcepoint ThreatSeeker category": "search engines and portals",
                "Alexa category": "search_engines",
                "detected_communicating_samples": [{
                    "date": "2019-01-28 23:58:13",
                    "positives": 30,
                    "sha256": "e65faa1283f8941d98dc23ff6822be228a24cb4489a5e5b01aeee749bf851658",
                    "total": 70
                }],
                "TrendMicro category": "search engines portals",
                "categories": [
                    "searchengines", "search engines and portals"
                ],
                "undetected_urls": [[
                    "http://example.co.in/example", "daed97b2c77f0f72c9e4ee45506e3e1bc4e34d7b8846246877a02779bb85dd5b", 0, 70, "2019-02-04 14:58:23"
                ]],
                "response_code": 1,
                "Webutation domain info": {
                    "Safety score": 100,
                    "Adult content": "no",
                    "Verdict": "safe"
                },
                "subdomains": [
                    "www.example.co.in"
                ],
                "Websense ThreatSeeker category": "search engines and portals",
                "detected_urls": [{
                    "url": "http://example.co.in/urlURL",
                    "positives": 2,
                    "total": 66,
                    "scan_date": "2018-01-13 00:38:35"
                }],
                "Alexa rank": 100,
                "undetected_communicating_samples": [{
                    "date": "2018-11-17 03:19:28",
                    "positives": 0,
                    "sha256": "e2a6ab7d594490c62bd3bb508dc38d7191ad48977da4d8dcce08dcb8af0070e9",
                    "total": 68
                }],
                "pcaps": [
               "97e4a17068ce3ed01ed1c25c3d263fc0145e5ecc53b7db6f2ba84496b53d4a65"
                ]},
            "Entity": "example.co.in"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Get Domain Report** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan Hash

Use the **Scan Hash** action to scan file hashes with VirusTotal, mark entities as suspicious, and show insights, if the risk score matches a given threshold.

This action runs on the Google SecOps `Filehash` entity.

#### Action inputs

The **Scan Hash** action requires the following parameters:

Parameter | Description  
---|---  
`Threshold` | Required. The threshold to mark detections as suspicious.If the malicious engine detections reach or exceed the set threshold, the action marks the entity as suspicious.  
`Rescan after days` | Optional. The number of days after the latest scan date to rescan the entity.  
  
#### Action outputs

The **Scan Hash** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
Insight | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment table

The **Scan Hash** action can enrich the following fields:

Enrichment field name | Applicable logic  
---|---  
`permalink` | Returns if it exists in the JSON result.  
`sha1` | Returns if it exists in the JSON result.  
`resource` | Returns if it exists in the JSON result.  
`Scan date` | Returns if it exists in the JSON result.  
`Scan ID` | Returns if it exists in the JSON result.  
`verbose_msg` | Returns if it exists in the JSON result.  
`total` | Returns if it exists in the JSON result.  
`positives` | Returns if it exists in the JSON result.  
`sha256` | Returns if it exists in the JSON result.  
`md5` | Returns if it exists in the JSON result.  
`Detecting Engines` | Returns if it exists in the JSON result.  
  
##### Insight

The **Scan Hash** action can return the following insight:

Severity | Description  
---|---  
`Warn` | The action creates a warning insight to inform about the malicious status of the enriched hash.The action only creates the insight when the number of detected engines equals or exceeds the minimum suspicious threshold that you set before scan.  
  
##### JSON result

The following example shows the JSON result output received when using the **Scan Hash** action:
    
    
    [
        {
            "EntityResult": {
                "permalink": "https://www.virustotal.com/file/HASH/analysis/ANALYSIS_ID/",
                "sha1": "3395856ce81f2b7382dee72602f798b642f14140",
                "resource": "HASH",
                "response_code": 1,
                "scan_date": "2019-02-05 15:41:52",
                "scan_id": "HASH-ANALYSIS_ID",
                "verbose_msg": "Scan finished, information embedded",
                "total": 60,
                "positives": 54,
                "sha256": "HASH",
                "md5": "44d88612fea8a8f36de82e1278abb02f",
                "scans": {
                    "Bkav": {
                        "detected": true,
                        "version": "192.0.2.1",
                        "result": "Trojan",
                        "update": "20190201"
                    },
                    "MicroWorld-eScan": {
                        "detected": true,
                        "version": "14.0.297.0",
                        "result": "Test-File",
                        "update": "20190205"
                    }}},
            "Entity": "HASH"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Scan Hash** action:

Script result name | Value  
---|---  
`is_risky` | `True` or `False`  
  
### Scan IP

Use the **Scan IP** action to gather the information that VirusTotal has seen recently on a specific IP.

This action runs on the Google SecOps `IP Address` entity.

#### Action inputs

The **Scan IP** action requires the following parameters:

Parameter | Description  
---|---  
`Threshold` | Optional. The threshold to mark an IP address as suspicious.If the malicious engine detections reach or exceed the set threshold, the action marks the IP address as suspicious.The default value is `25`.  
  
#### Action outputs

The **Scan IP** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
Insights | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment table

The **Scan IP** action can enrich the following fields:

Enrichment field name | Applicable logic  
---|---  
`Country` | Returns if it exists in the JSON result.  
`Related Domains` | Returns if it exists in the JSON result.  
`Last Scan Date` | Returns if it exists in the JSON result.  
`verbose_msg` | Returns if it exists in the JSON result.  
`Resolutions` | Returns if it exists in the JSON result.  
  
##### Insights

The **Scan IP** action can return the following insights:

Severity | Description  
---|---  
`Warn` | The action creates a warning insight to inform about the malicious status of the enriched IP address.The action only creates the insight when the number of detected engines equals or exceeds the minimum suspicious threshold that you set before scan.  
Insight name | Body  
---|---  
`Entity Insight` | 

  * Country: `country`
  * Malicious Referrer Samples: `len(detected_referrer_samples)`
  * Malicious Downloaded Samples: `len(detected_downloaded_samples)`
  * Malicious Communicating Samples: `len(detected_communicating_samples)`
  * Malicious URLs: `len(detected_urls)`

  
  
##### JSON result

The following example shows the JSON result output received when using the **Scan IP** action:
    
    
    [
        {
            "EntityResult": {
                "asn": 4436,
                "undetected_urls": [[
                    "http://example.com", "2ed06796f95e7c1xxxxxbd68d81754acf535c999e901bfe2cf9c45612396f66", 0, 66, "2022-11-23 06:51:49"
                ]],
                "undetected_downloaded_samples": [{
                    "date": "2018-07-09 07:53:30",
                    "positives": 0,
                    "sha256": "6a0bf66ddc73d7e64eb2ff0dd3512c5378c0c63c2ad4e13c0e1429fe",
                    "total": 60
                }],
                "country": "country",
                "response_code": 1,
                "as_owner": "Example, Inc.",
                "verbose_msg": "IP address in dataset",
                "detected_downloaded_samples": [{
                    "date": "2023-05-20 08:38:00",
                    "positives": 6,
                    "sha256": "9cf5c07c99c3342d83b241c25850da0bf231ee150cb962cab1e8399cb",
                    "total": 57
                }],
                "resolutions": [{
                    "last_resolved": "2023-05-13 00:00:00",
                    "hostname": "40515350444dff68-2f7735d5ad283fa41a203a082d9a8f25.example.com"
                }],
                "detected_urls": [{
                    "url": "http://example.com",
                    "positives": 2,
                    "total": 67,
                    "scan_date": "2023-05-20 07:16:45"
                }]},
                "Entity": "192.0.2.1"
            }
        ]
    

##### Script result

The following table lists the value for the script result output when using the **Scan IP** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan URL

Use the **Scan URL** action to scan a URL with VirusTotal.

This action runs on the Google SecOps `URL` entity.

#### Action inputs

The **Scan URL** action requires the following parameters:

Parameter | Description  
---|---  
`Threshold` | Required. The threshold to mark detections as suspicious.If the malicious engine detections reach or exceed the set threshold, the action marks the entity as suspicious.  
`Rescan after days` | Optional. The number of days after the latest scan date to rescan the entity.  
  
#### Action outputs

The **Scan URL** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
Insight | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment table

The **Scan URL** action can enrich the following fields:

Enrichment field name | Applicable logic  
---|---  
`Scan date` | Returns if it exists in the JSON result.  
`Scan ID` | Returns if it exists in the JSON result.  
`risk_score` | Returns if it exists in the JSON result.  
`Total` | Returns if it exists in the JSON result.  
`Online Link` | Returns if it exists in the JSON result.  
`Scanned Url` | Returns if it exists in the JSON result.  
`resource` | Returns if it exists in the JSON result.  
`Detecting Engines` | Returns if it exists in the JSON result.  
`Risk Score` | Returns if it exists in the JSON result.  
`Last Scan Date` | Returns if it exists in the JSON result.  
`verbose_msg` | Returns if it exists in the JSON result.  
`File Scan ID` | Returns if it exists in the JSON result.  
  
##### Insight

The **Scan URL** action can return the following insight:

Severity | Description  
---|---  
`Warn` | The action creates a warning insight to inform about the malicious status of the enriched URL.The action only creates the insight when the number of detected engines equals or exceeds the minimum suspicious threshold that you set before scan.  
  
##### JSON result

The following example shows the JSON result output received when using the **Scan URL** action:
    
    
    [
        {
            "EntityResult": {
                "permalink": "https://www.virustotal.com/url/URL_HASH/analysis/ANALYSIS_ID/",
                "resource": "http://example.php",
                "url": "http://example.php",
                "response_code": 1,
                "scan_date": "2019-02-04 05:28:54",
                "scan_id": "URL_HASH-ANALYSIS_ID",
                "verbose_msg": "Scan finished, scan information embedded in this object",
                "filescan_id": null,
                "positives": 5,
                "total": 67,
                "scans": {
                    "CLEAN MX": {
                        "detected": false,
                        "result": "clean site"
                    },
                    "DNS8": {
                        "detected": false,
                        "result": "clean site"
                    }}},
            "Entity": "http://example.php"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Scan URL** action:

Script result name | Value  
---|---  
`is_risky` | `True` or `False`  
  
### Upload and Scan File

Use the **Upload and Scan File** action to upload and scan a file with VirusTotal.

This action runs on all Google SecOps entities.

#### Action inputs

The **Upload and Scan File** action requires the following parameters:

Parameter | Description  
---|---  
`Threshold` | Required. The minimum number of positive detections from VirusTotal scanners to consider a file risky and trigger an insight.The default value is `3`.  
`File Paths` | Required. A comma-separated list of paths to upload and scan.  
`Linux Server Address` | Optional. The address of a remote Linux server where the files are located, such as `192.0.2.1`.  
`Linux User` | Optional. The username to authenticate at the remote Linux server.  
`Linux Password` | Optional. The password to authenticate at the remote Linux server.  
  
#### Action outputs

The **Upload and Scan File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
Insight | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment table

The **Upload and Scan File** action can enrich the following fields:

Enrichment field name | Applicable logic  
---|---  
`resource` | Returns if it exists in the JSON result.  
`Scan date` | Returns if it exists in the JSON result.  
`Scan ID` | Returns if it exists in the JSON result.  
`permalink` | Returns if it exists in the JSON result.  
`Total` | Returns if it exists in the JSON result.  
`Md5` | Returns if it exists in the JSON result.  
`Sha1` | Returns if it exists in the JSON result.  
`Sha256` | Returns if it exists in the JSON result.  
`positives` | Returns if it exists in the JSON result.  
`total` | Returns if it exists in the JSON result.  
`Detecting Engines` | Returns if it exists in the JSON result.  
`verbose_msg` | Returns if it exists in the JSON result.  
  
##### Insight

The **Upload and Scan File** action can return the following insight:

Severity | Description  
---|---  
`Warn` | The action creates a warning insight to inform about the malicious status of the enriched file.The action only creates the insight when the number of detected engines equals or exceeds the minimum suspicious threshold that you set before scan.  
  
##### JSON result

The following example shows the JSON result output received when using the **Upload and Scan File** action:
    
    
    {
        "file_path": {
            "scan_id": "FILE_ID-ANALYSIS_ID",
            "sha1": "ec44b2af88e602e3981db0b218ecb5d59dc0dfec",
            "resource": "FILE_ID-ANALYSIS_ID",
            "response_code": 1,
            "scan_date": "2019-02-05 15:55:50",
            "permalink": "https://www.virustotal.com/file/FILE_ID/analysis/ANALYSIS_ID/",
            "verbose_msg": "Scan finished, information embedded",
            "total": 58,
            "positives": 0,
            "sha256": "FILE_ID",
            "md5": "848d57fbd8e29afa08bd3f58dd30f902",
            "scans": {
                "Bkav": {
                    "detected": false,
                    "version": "192.0.2.1",
                    "result": null,
                    "update": "20190201"
                },
                "MicroWorld-eScan": {
                    "detected": false,
                    "version": "14.0.297.0",
                    "result": null,
                    "update": "20190205"
                }
            }
        }
    }
    

##### Script result

The following table lists the value for the script result output when using the **Upload and Scan File** action:

Script result name | Value  
---|---  
`is_risky` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
