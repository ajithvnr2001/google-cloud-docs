---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmray/
title: VMRay \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:54.517758+00:00
---

# VMRay  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmray/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMRay

This document provides guidance to help you configure and integrate VMRay with Google SecOps.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/VMRay.zip).

## Integrate VMRay with Google SecOps SOAR

The integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | _Required_ The API root of the VMRay instance.  
`Api Key` | _Required_ The VMRay API key.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the VMRay server is valid. Selected by default.  
  
For instructions about configuring an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

The VMRay integration includes the following actions:

  * Add Tag to Submission
  * Ping
  * Scan Hash
  * Scan URL
  * Upload File and Get Report



### Add Tag to Submission

Use the **Add Tag to Submission** action to add a tag to the VMRay submission process.

This action runs on all Google SecOps entities.

#### Action inputs

The **Add Tag to Submission** action requires the following parameters:

Parameter | Description  
---|---  
`Submission ID` | _Required_ The ID of the submission process.  
`Tag Name` | _Required_ The tag name to add to the submission process.  
  
#### Action outputs

The **Add Tag to Submission** action provides the following outputs:

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

The **Add Tag to Submission** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added tag TAG_NAME to submission SUBMISSION_ID.` | The action succeeded.  
`Failed to add tag TAG_NAME to submission SUBMISSION_ID. Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Tag to Submission** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to VMRay.

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully tested connectivity.` | The action succeeded.  
`Failed to test connectivity.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan Hash

Use the **Scan Hash** action to get details about a specific hash.

This action runs on the Google SecOps Hash entity.

#### Action inputs

The **Scan Hash** action requires the following parameters:

Parameter | Description  
---|---  
`Threat Indicator Score Threshold` | _Required_ The lowest score to use for returning the threat indicators. The maximum value is 5.The default value is 3.  
`IOC Type Filter` | _Required_ A comma-separated list of IOC types to return. The possible values are as follows:

  * `domains`
  * `emails`
  * `files`
  * `ips`
  * `mutexes`
  * `processes`
  * `registry`
  * `urls`

The default value is `ips, files, emails, urls, domains`.  
`IOC Verdict Filter` | _Required_ A comma-separated list of IOC verdicts that is used during the IOCs ingestion.The possible values are as follows:

  * `Malicious`
  * `Suspicious`
  * `Clean`
  * `None`

The default value is `Malicious, Suspicious`.  
`Max IOCs To Return` | _Optional_ A number of IOCs to return for every entity in the IOC type.The default value is 10.  
`Max Threat Indicators To Return` | _Optional_ A number of threat indicators to return for every entity.The default value is 10.  
`Create Insight` | _Optional_ If selected, the action creates an insight that contains an information about entities.Selected by default.  
`Only Suspicious Insight` | _Optional_ If selected, the action only creates insights for suspicious entities.If you select this parameter, select the `Create Insight` parameter.Not selected by default.  
  
#### Action outputs

The **Scan Hash** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Scan Hash** action provides the following case wall table:

Table title: ENTITY_ID

Table columns:

  * **Key**
  * **Value**



##### Enrichment table

The **Scan Hash** action supports the following enrichment options:

Enrichment field name | Source (JSON key) | Applicability  
---|---|---  
`VMRay_sample_vti_score` | `sample_vti_score` | Always  
`VMRay_sample_child_sample_ids` | `sample_child_sample_ids` | Always  
`VMRay_sample_id` | `sample_id` | Always  
`VMRay_sample_sha1hash` | `sample_sha1hash` | Always  
`VMRay_sample_classifications` | `sample_classifications` | Always  
`VMRay_sample_last_md_score` | `sample_last_md_score` | Always  
`VMRay_sample_last_vt_score` | `sample_last_vt_score` | Always  
`VMRay_sample_severity` | `sample_severity` | Always  
`VMRay_sample_url` | `sample_url` | Always  
`VMRay_sample_imphash` | `sample_imphash` | Always  
`VMRay_sample_highest_vti_score` | `sample_highest_vti_score` | Always  
`VMRay_sample_container_type` | `sample_container_type` | Always  
`VMRay_sample_webif_url` | `sample_webif_url` | Always  
`VMRay_sample_type` | `sample_type` | Always  
`VMRay_sample_created` | `sample_created` | Always  
`VMRay_sample_last_reputation_severity` | `sample_last_reputation_severity` | Always  
`VMRay_sample_filesize` | `sample_filesize` | Always  
`VMRay_sample_parent_sample_ids` | `sample_parent_sample_ids` | Always  
`VMRay_sample_ssdeephash` | `sample_ssdeephash` | Always  
`VMRay_sample_md5hash` | `sample_md5hash` | Always  
`VMRay_sample_sha256hash` | `sample_sha256hash` | Always  
`VMRay_sample_highest_vti_severity` | `sample_highest_vti_severity` | Always  
`VMRay_sample_priority` | `sample_priority` | Always  
`VMRay_sample_is_multipart` | `sample_is_multipart` | Always  
`VMRay_sample_score` | `sample_score` | Always  
`VMRay_sample_filename` | `sample_filename` | Always  
`VMRay_ioc_domains` | A CSV file of IOCs or domains | Always  
`VMRay_ioc_ips` | A CSV file of IOCs or IP addresses | Always  
`VMRay_ioc_urls` | A CSV file of IOCs or URLs | Always  
`VMRay_ioc_files` | A CSV file of IOCs or files | Always  
`VMRay_ioc_emails` | A CSV file of IOCs or email addresses | Always  
`VMRay_ioc_mutexes` | A CSV file of IOCs or mutex names | Always  
`VMRay_ioc_processes` | A CSV file of IOCs or process names | Always  
`VMRay_ioc_registry` | A CSV file of IOCs or registries | Always  
`VMRay_threat_indicator_operations` | A CSV file of threat indicators or operations | Always  
`VMRay_threat_indicator_category` | A CSV file of threat indicators or categories | Always  
  
##### JSON result

The following example describes the JSON result output received when using the **Scan Hash** action:
    
    
    {
        "sample_child_relations": [],
        "sample_child_relations_truncated": false,
        "sample_child_sample_ids": [],
        "sample_classifications": [],
        "sample_container_type": null,
        "sample_created": "2019-06-05T07:29:05",
        "sample_display_url": "URL",
        "sample_filename": "sample.url",
        "sample_filesize": 35,
        "sample_highest_vti_score": 80,
        "sample_highest_vti_severity": "malicious",
        "sample_id": 3945509,
        "sample_imphash": null,
        "sample_is_multipart": false,
        "sample_last_md_score": null,
        "sample_last_reputation_severity": "malicious",
        "sample_last_vt_score": null,
        "sample_md5hash": "de765a6a9931c754b709d44c33540149",
        "sample_parent_relations": [],
        "sample_parent_relations_truncated": false,
        "sample_parent_sample_ids": [],
        "sample_password_protected": false,
        "sample_pe_signature": null,
        "sample_priority": 3,
        "sample_score": 80,
        "sample_severity": "malicious",
        "sample_sha1hash": "a4b19054d162aab802270aec8ef27f009ab4db51",
        "sample_sha256hash": "8fb5c7a88058fad398dfe290f3821a3983a608abe6b39d014d9800afa3d5af70",
        "sample_ssdeephash": "3:N1KTxKWiUgdhHn:C1N3an",
        "sample_threat_names": [
            "C2/Generic-A"
        ],
        "sample_type": "URL",
        "sample_url": "URL",
        "sample_verdict": "malicious",
        "sample_verdict_reason_code": null,
        "sample_verdict_reason_description": null,
        "sample_vti_score": "malicious",
        "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=ID",
        "iocs": {
            "domains": [
                {
                    "domain": "example.net",
                    "severity": "unknown",
                    "verdict": "clean"
                }
            ],
            "emails": [
                {
                    "email": "example.net",
                    "severity": "unknown",
                    "verdict": "clean"
                }
            ],
            "files": [
                {
                    "filename": "C:\\Program Files (x86)\\example.exe",
                    "categories": [
                        "Dropped File"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean",
                    "classifications": [
                        "Virus"
                    ],
                    "operations": [
                        "Access",
                        "Create",
                        "Write"
                    ],
                    "hashes": [
                        {
                            "imp_hash": null,
                            "md5_hash": "58a2430b19d0594b46caf69dea5c1023",
                            "sha1_hash": "e8f5809342eedc2b035f726811dcaa1a9b589cb7",
                            "sha256_hash": "b9072661a90377835205f5c66ee06ba82ec42d843c8ec5dc07c16da86c90b835",
                            "ssdeep_hash": "12:TMHdgo+tJVEdQiCXFMp3OOy9P72/FeFYX+NEVjB:2dfyiw2uTyOOT"
                        }
                    ]
                }
            ],
            "ips": [
                {
                    "ip_address": "192.0.2.1",
                    "severity": "not_suspicious",
                    "verdict": "malicious"
                }
            ],
            "mutexes": [
                {
                    "mutex_name": "NAME",
                    "operations": [
                        "access"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "processes": [
                {
                    "classifications": [],
                    "cmd_line": "/c del \"C:\\Users\\example.exe\"",
                    "process_ids": [
                        137
                    ],
                    "parent_processes": [
                        "\"C:\\Windows\\SysWOW64\\control.exe\""
                    ],
                    "process_names": [
                        "cmd.exe"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "registry": [
                {
                    "operations": [
                        "access",
                        "write"
                    ],
                    "reg_key_name": "HKEY_USERS\\ID\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\YLRPWV4P6TI",
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "urls": [
                {
                    "severity": "malicious",
                    "url": "URL",
                    "verdict": "malicious"
                }
            ]
        },
        "threat_indicators": [
            {
                "category": "Heuristics",
                "operation": "Contains suspicious meta data",
                "score": 4,
                "classifications": [
                    "Spyware"
                ]
            }
        ]
    }
    

##### Output messages

The **Scan Hash** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities using information from VMRay: ENTITY_ID` `Action wasn't able to enrich the following entities using information from VMRay: ENTITY_ID` `None of the provided entities were enriched.` | The action succeeded.  
`Error executing action "Scan Hash". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Scan Hash** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan URL

Use the **Scan URL** action to submit URLs and receive related information about them.

This action runs on the Google SecOps URL entity.

#### Action inputs

The **Scan URL** action requires the following parameters:

Parameter | Description  
---|---  
`Tag Names` | _Optional_ The tags to add to the submitted URL.  
`Comment` | _Optional_ The comment to add to the submitted URL.  
`Threat Indicator Score Threshold` | _Required_ The lowest score to use for returning threat indicators. The maximum value is 5.The default value is 3.  
`IOC Type Filter` | _Required_ A comma-separated list of IOC types to return. The possible values are as follows:

  * `domains`
  * `emails`
  * `files`
  * `ips`
  * `mutexes`
  * `processes`
  * `registry`
  * `urls`

The default values are `ips, urls, domains`.  
`IOC Verdict Filter` | _Required_ A comma-separated list of IOC verdicts that is used during the IOCs ingestion.The possible values are as follows:

  * `Malicious`
  * `Suspicious`
  * `Clean`
  * `None`

The default values are `Malicious, Suspicious`.  
`Max IOCs To Return` | _Optional_ A number of IOCs to return for every entity in the IOC type.The default value is 10.  
`Max Threat Indicators To Return` | _Optional_ A number of threat indicators to return for every entity.The default value is 10.  
`Create Insight` | _Optional_ If selected, the action creates an insight that contains information about entities.Selected by default.  
`Only Suspicious Insight` | _Optional_ If selected, the action only creates insights for suspicious entities.If selected, also select the `Create Insight` parameter.Not selected by default.  
  
#### Action outputs

The **Scan URL** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Scan URL** action provides the following case wall table:

Table title: ENTITY_ID

Table columns:

  * **Key**
  * **Value**



##### Enrichment table

The **Scan Hash** action supports the following enrichment options:

Enrichment field name | Source (JSON key) | Applicability  
---|---|---  
`VMRay_sample_vti_score` | `sample_vti_score` | Always  
`VMRay_sample_child_sample_ids` | `sample_child_sample_ids` | Always  
`VMRay_sample_id` | `sample_id` | Always  
`VMRay_sample_sha1hash` | `sample_sha1hash` | Always  
`VMRay_sample_classifications` | `sample_classifications` | Always  
`VMRay_sample_last_md_score` | `sample_last_md_score` | Always  
`VMRay_sample_last_vt_score` | `sample_last_vt_score` | Always  
`VMRay_sample_severity` | `sample_severity` | Always  
`VMRay_sample_url` | `sample_url` | Always  
`VMRay_sample_imphash` | `sample_imphash` | Always  
`VMRay_sample_highest_vti_score` | `sample_highest_vti_score` | Always  
`VMRay_sample_container_type` | `sample_container_type` | Always  
`VMRay_sample_webif_url` | `sample_webif_url` | Always  
`VMRay_sample_type` | `sample_type` | Always  
`VMRay_sample_created` | `sample_created` | Always  
`VMRay_sample_last_reputation_severity` | `sample_last_reputation_severity` | Always  
`VMRay_sample_filesize` | `sample_filesize` | Always  
`VMRay_sample_parent_sample_ids` | `sample_parent_sample_ids` | Always  
`VMRay_sample_ssdeephash` | `sample_ssdeephash` | Always  
`VMRay_sample_md5hash` | `sample_md5hash` | Always  
`VMRay_sample_sha256hash` | `sample_sha256hash` | Always  
`VMRay_sample_highest_vti_severity` | `sample_highest_vti_severity` | Always  
`VMRay_sample_priority` | `sample_priority` | Always  
`VMRay_sample_is_multipart` | `sample_is_multipart` | Always  
`VMRay_sample_score` | `sample_score` | Always  
`VMRay_sample_filename` | `sample_filename` | Always  
`VMRay_ioc_domains` | A CSV file of IOCs or domains | Always  
`VMRay_ioc_ips` | A CSV file of IOCs or IP addresses | Always  
`VMRay_ioc_urls` | A CSV file of IOCs or URLs | Always  
`VMRay_ioc_files` | A CSV file of IOCs or files | Always  
`VMRay_ioc_emails` | A CSV file of IOCs or email addresses | Always  
`VMRay_ioc_mutexes` | A CSV file of IOCs or mutex names | Always  
`VMRay_ioc_processes` | A CSV file of IOCs or process names | Always  
`VMRay_ioc_registry` | A CSV file of IOCs or registries | Always  
`VMRay_threat_indicator_operations` | A CSV file of threat indicators or operations | Always  
`VMRay_threat_indicator_category` | A CSV file of threat indicators or categories | Always  
  
##### JSON result

The following example describes the JSON result output received when using the **Scan URL** action:
    
    
    {
        "sample_child_relations": [],
        "sample_child_relations_truncated": false,
        "sample_child_sample_ids": [],
        "sample_classifications": [],
        "sample_container_type": null,
        "sample_severity": "malicious",
        "sample_sha1hash": "a4b19054d162aab802270aec8ef27f009ab4db51",
        "sample_sha256hash": "8fb5c7a88058fad398dfe290f3821a3983a608abe6b39d014d9800afa3d5af70",
        "sample_ssdeephash": "3:N1KTxKWiUgdhHn:C1N3an",
        "sample_threat_names": [
            "C2/Generic-A"
        ],
        "sample_type": "URL",
        "sample_url": "URL",
        "sample_verdict": "malicious",
        "sample_verdict_reason_code": null,
        "sample_verdict_reason_description": null,
        "sample_vti_score": "malicious",
        "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=ID",
        "iocs": {
            "domains": [
                {
                    "domain": "example.net",
                    "severity": "unknown",
                    "verdict": "clean"
                }
            ],
            "emails": [
                {
                    "email": "example.net",
                    "severity": "unknown",
                    "verdict": "clean"
                }
            ],
                    "files": [
                {
                    "filename": "C:\\Program Files (x86)\\example.exe",
                    "categories": [
                        "Dropped File"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean",
                    "classifications": [
                        "Virus"
                    ],
                    "operations": [
                        "Access",
                        "Create",
                        "Write"
                    ],
                    "hashes": [
                        {
                            "imp_hash": null,
                            "md5_hash": "58a2430b19d0594b46caf69dea5c1023",
                            "sha1_hash": "e8f5809342eedc2b035f726811dcaa1a9b589cb7",
                            "sha256_hash": "b9072661a90377835205f5c66ee06ba82ec42d843c8ec5dc07c16da86c90b835",
                            "ssdeep_hash": "12:TMHdgo+tJVEdQiCXFMp3OOy9P72/FeFYX+NEVjB:2dfyiw2uTyOOT"
                        }
                    ]
                }
            ],
            "ips": [
                {
                    "ip_address": "192.0.2.30",
                    "severity": "not_suspicious",
                    "verdict": "malicious"
                }
            ],
            "mutexes": [
                {
                    "mutex_name": "NAME",
                    "operations": [
                        "access"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "processes": [
                {
                    "classifications": [],
                    "cmd_line": "/c del \"C:\\Users\\example.exe\"",
                    "process_ids": [
                        137
                    ],
                    "parent_processes": [
                        "\"C:\\Windows\\SysWOW64\\control.exe\""
                    ],
                    "process_names": [
                        "cmd.exe"
                    ],
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "registry": [
                {
                    "operations": [
                        "access",
                        "write"
                    ],
                    "reg_key_name": "HKEY_USERS\\ID\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\YLRPWV4P6TI",
                    "severity": "not_suspicious",
                    "verdict": "clean"
                }
            ],
            "urls": [
                {
                    "severity": "malicious",
                    "url": "URL",
                    "verdict": "malicious"
                }
            ]
        },
        "threat_indicators": [
            {
                "category": "Heuristics",
                "operation": "Contains suspicious meta data",
                "score": 4,
                "classifications": [
                    "Spyware"
                ]
            }
        ]
    }
    

##### Output messages

The **Scan URL** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities using information from VMRay: ENTITY_ID` `Action wasn't able to enrich the following entities using information from VMRay: ENTITY_ID` `None of the provided entities were enriched.` | The action succeeded.  
`Error executing action "Scan URL". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Scan URL** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Upload File and Get Report

Use the **Upload File and Get Report** action to submit files for analysis in VMRay.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

#### Action inputs

The **Upload File and Get Report** action requires the following parameters:

Parameter | Description  
---|---  
`Sample File Path` | _Required_ A comma-separate list of absolute paths for submitted files.  
`Tag Names` | _Optional_ The tags to add to the submitted files.  
`Comment` | _Optional_ The comment to add to the submitted files.  
  
#### Action outputs

The **Upload File and Get Report** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Upload File and Get Report** action:
    
    
    {
        "data": {
          "sample_child_sample_ids": [],
          "sample_classifications": [
            "Dropper",
            "Pua",
            "Spyware"
          ],
          "sample_container_type": null,
          "sample_created": "2020-01-30T14:12:07",
          "sample_filename": "example.exe",
          "sample_filesize": 86448896,
          "sample_highest_vti_score": 74,
          "sample_highest_vti_severity": "suspicious",
          "sample_id": 4846052,
          "sample_imphash": "b34f154ec913d2d2c435cbd644e91687",
          "sample_is_multipart": false,
          "sample_last_md_score": null,
          "sample_last_reputation_severity": "whitelisted",
          "sample_last_vt_score": null,
          "sample_md5hash": "403799c0fdfb3728cd8f5992a7c8b949",
          "sample_parent_sample_ids": [],
          "sample_priority": 1,
          "sample_score": 74,
          "sample_severity": "suspicious",
          "sample_sha1hash": "17df3548dd9b8d0283d4acba8195955916eff5f3",
          "sample_sha256hash": "2acb1432850b2d2cdb7e6418c57d635950a13f5670eae83324f7ae9130198bbc",
          "sample_ssdeephash": "1572864:B9nbNI1LT6t5jOvefSRROaqMhUVkjSFuI5ym9Q5klp/yOmdAyNgc:vbNIZOOvUSRRObaCkjSFug4kYd7Nn",
          "sample_type": "Windows Exe (x86-32)",
          "sample_url": null,
          "sample_vti_score": 74,
          "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=ID"
        },
        "result": "ok"
    }
    

##### Output messages

The **Upload File and Get Report** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully submitted the following files to VMRay: SUBMITTED_FILES` `Error executing action "Upload File And Get Report". Reason: the following files were not accessible: PATHS` `Waiting for the results for: PENDING_FILE_NAME` | The action succeeded.  
`Error executing action "Upload File and Get Report". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Upload File and Get Report** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
