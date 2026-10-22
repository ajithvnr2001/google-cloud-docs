---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cofense/
title: Cofense Triage \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:08.825946+00:00
---

# Cofense Triage  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cofense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cofense Triage

This document describes how to integrate Cofense Triage with Google Security Operations.

## Use Cases

  1. Ingest Cofense Triage reports and use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Enrichment of the related entities and details about the report.
  3. Triage of the report.



## Configure Cofense Triage integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://tap.phishmecloud.com | N/A | API Root of the Cofense Triage instance.  
Client ID | String | N/A | Yes | Client ID of the Cofense Triage account.  
Client Secret | Password | N/A | Yes | Client Secret of the Cofense Triage account.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Cofense Triage server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add Tags To Report

#### Description

Add tags to a report in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the id of the report to which you want to add tags.  
Tags | CSV | N/A | Yes | Specify a comma-separated list of tags that need to be applied to the report.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "id": "13507",
            "type": "reports",
            "links": {
                "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507"
            },
            "attributes": {
                "location": "Inbox",
                "risk_score": 96,
                "from_address": null,
                "subject": "Test Phishing domain",
                "received_at": "2020-10-12T21:30:54.000Z",
                "reported_at": "2020-10-12T21:30:53.000Z",
                "raw_headers": "X-Triage-Noise-Reduction: state=0\r\nX-Triage-Noise-Reduction: score=79\r\nX-Triage-Noise-Reduction: vacb1561f9d032089\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit",
                "text_body": "Testing<http://dsrihsddk.net/>\r\n\r\nThis is a poor reputation domain\r\n\r\n",
                "html_body": "<html xmlns:v=\"urn:schemas-microsoft-com:vml\" xml>\r\n</div>\r\n</body>\r\n</html>\r\n",
                "md5": "81fe86fc9c244be978ab8b8392d3c986",
                "sha256": "146b857b2a147eeb9091571327452006438294aeb21069e38c6f25a811aa6c03",
                "match_priority": 1,
                "tags": [
                    "dsa",
                    "asd"
                ],
                "categorization_tags": [],
                "processed_at": null,
                "created_at": "2020-10-12T21:31:36.495Z",
                "updated_at": "2020-11-17T15:33:27.567Z"
            },
            "relationships": {
                "assignee": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/assignee",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/assignee"
                    },
                    "data": null
                },
                "category": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/category",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/category"
                    },
                    "data": null
                },
                "cluster": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/cluster",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/cluster"
                    },
                    "data": {
                        "type": "clusters",
                        "id": "3915"
                    }
                },
                "reporter": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/reporter",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/reporter"
                    },
                    "data": {
                        "type": "reporters",
                        "id": "5331"
                    }
                },
                "attachment_payloads": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/attachment_payloads",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/attachment_payloads"
                    }
                },
                "attachments": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/attachments",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/attachments"
                    }
                },
                "headers": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/headers",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/headers"
                    }
                },
                "hostnames": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/hostnames",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/hostnames"
                    }
                },
                "urls": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/urls",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/urls"
                    }
                },
                "rules": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/rules",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/rules"
                    }
                },
                "threat_indicators": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/threat_indicators",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/threat_indicators"
                    }
                }
            },
            "meta": {
                "risk_score_summary": {
                    "integrations": 75,
                    "vip": 5,
                    "reporter": 15,
                    "rules": 1
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully added tags to the the report with ID {0} in Cofense Triage.".format(report_id)  
******if unsuccessful aka status code 404(is_success = false):**  
****print "Action wasn't able to add tags to the report with ID {0} in Cofense Triage. Reason: \n {1}".format(report_id, errors/detail)  
**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Add Tags To Report". Reason: {0}''.format(error.Stacktrace) | General  
  
### Categorize Report

#### Description

Categorize a report in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the id of the report to which you want to add tags.  
Category Name | String | N/A | Yes | Specify the name of the category that should be applied to the report. Available categories can be found in the "List Categories" action.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "id": "13507",
            "type": "reports",
            "links": {
                "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507"
            },
            "attributes": {
                "location": "Inbox",
                "risk_score": 96,
                "from_address": null,
                "subject": "Test Phishing domain",
                "received_at": "2020-10-12T21:30:54.000Z",
                "reported_at": "2020-10-12T21:30:53.000Z",
                "raw_headers": "X-Triage-Noise-Reduction: state=0\r\nX-Triage-Noise-Reduction: score=79\r\nX-Triage-Noise-Reduction: vacb1561f9d032089\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit",
                "text_body": "Testing<http://dsrihsddk.net/>\r\n\r\nThis is a poor reputation domain\r\n\r\n",
                "html_body": "<html xmlns:v=\"urn:schemas-microsoft-com:vml\" xml>\r\n</div>\r\n</body>\r\n</html>\r\n",
                "md5": "81fe86fc9c244be978ab8b8392d3c986",
                "sha256": "146b857b2a147eeb9091571327452006438294aeb21069e38c6f25a811aa6c03",
                "match_priority": 1,
                "tags": [
                    "dsa",
                    "asd"
                ],
                "categorization_tags": [],
                "processed_at": null,
                "created_at": "2020-10-12T21:31:36.495Z",
                "updated_at": "2020-11-17T15:33:27.567Z"
            },
            "relationships": {
                "assignee": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/assignee",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/assignee"
                    },
                    "data": null
                },
                "category": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/category",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/category"
                    },
                    "data": null
                },
                "cluster": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/cluster",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/cluster"
                    },
                    "data": {
                        "type": "clusters",
                        "id": "3915"
                    }
                },
                "reporter": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/reporter",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/reporter"
                    },
                    "data": {
                        "type": "reporters",
                        "id": "5331"
                    }
                },
                "attachment_payloads": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/attachment_payloads",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/attachment_payloads"
                    }
                },
                "attachments": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/attachments",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/attachments"
                    }
                },
                "headers": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/headers",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/headers"
                    }
                },
                "hostnames": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/hostnames",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/hostnames"
                    }
                },
                "urls": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/urls",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/urls"
                    }
                },
                "rules": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/rules",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/rules"
                    }
                },
                "threat_indicators": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reports/13507/relationships/threat_indicators",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reports/13507/threat_indicators"
                    }
                }
            },
            "meta": {
                "risk_score_summary": {
                    "integrations": 75,
                    "vip": 5,
                    "reporter": 15,
                    "rules": 1
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully updated category on the the report with ID {0} to {1} in Cofense Triage.".format(report_id, category_name)  
******if unsuccessful aka status code 404(is_success = false):** print "Action wasn't able to update the category on the report with ID {0} to {1} in Cofense Triage. Reason: \n {2}".format(report_id, category_name, errors/detail)  
  
**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Categorize Report". Reason: {0}''.format(error.Stacktrace) | General  
  
### Download Report Email

#### Description

Download raw email related to the report from Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the ID of the report, which contains the raw email that needs to be downloaded.  
Download Folder | String | N/A | Yes | Specify the absolute path to the download folder. Note: Name will be constructed in the following way {report id}.eml.  
Overwrite | Checkbox | Checked | No | If enabled, action will overwrite the file with the same name and filepath.  
Create Insight | Checkbox | Unchecked | No | If enabled, action will create an insight that contains raw email of the report.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "absolute_file_path": "{filepath}"
    }
    

##### Insight

Name | Body  
---|---  
Report {ID}. Raw Email | {content of the response. \n should be replaced with \  
}  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully downloaded raw email related to the report with ID {0} in Cofense Triage.".format(report_id)  
******if unsuccessful aka status code 400(is_success = false):** print "Action wasn't able to download raw email related to the report with ID {0} in Cofense Triage. Reason: \n {1}".format(report_id, errors/detail)  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Download Report Email". Reason: {0}''.format(error.Stacktrace)  
******If file with filename exists and overwrite false:** "Error executing action "Download Report Email". Reason: File with that file path already exists. Please remove it or set 'Overwrite' to true." | General  
  
### Download Report Preview

#### Description

Download image preview from the email related to the report from Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the ID of the report, which contains the raw email that needs to be downloaded.  
Download Folder | String | N/A | Yes | Specify the absolute path to the download folder. Note: Name will be constructed in the following way {report id}.eml.  
Overwrite | Checkbox | Checked | No | If enabled, action will overwrite the file with the same name and filepath.  
Image Format | DDL | PNG Possible values:

  * PNG
  * JPG

| Yes | Specify the format of the image.  
Create Insight | Checkbox | Unchecked | No | If enabled, action will create an insight that contains raw email of the report.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "absolute_file_path": "{filepath}"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful (is_success=true):** "Successfully downloaded preview related to the report with ID {0} in Cofense Triage.".format(report_id) **If unsuccessful that is when the 400 status code (is_success=false):** "Action wasn't able to download a preview related to the report with ID {0} in Cofense Triage. Reason: \n {1}".format(report_id, errors/detail) **The action should fail and stop a playbook execution:** **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Download Report Preview". Reason: {0}''.format(error.Stacktrace) **If file with filename exists and overwrite false:** "Error executing action "Download Report Email". Reason: File with that file path already exists. Please remove it or set 'Overwrite' to true." | General  
  
### Enrich URL

#### Description

Return information about the URL from Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Risk Score Threshold | Integer | 50 | Yes | Specify, what should be the risk score threshold for Google SecOps to label that URL as suspicious. Maximum is 100.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
COFENSE_TRG_id | If available in JSON Result.  
COFENSE_TRG_risk_score | If available in JSON Result.  
COFENSE_TRG_created_at | If available in JSON Result.  
COFENSE_TRG_updated_at | If available in JSON Result.  
  
##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "1",
                "type": "urls",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/urls/1"
                },
                "attributes": {
                    "url": "https://www.paypal.com/us",
                    "risk_score": null,
                    "created_at": "2019-04-12T02:58:20.008Z",
                    "updated_at": "2019-04-12T02:58:20.008Z"
                },
                "relationships": {
                    "hostname": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/1/relationships/hostname",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/1/hostname"
                        },
                        "data": {
                            "type": "hostnames",
                            "id": "2"
                        }
                    },
                    "clusters": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/1/relationships/clusters",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/1/clusters"
                        }
                    },
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/1/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/1/reports"
                        }
                    }
                }
            },
            {
                "id": "2",
                "type": "urls",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/urls/2"
                },
                "attributes": {
                    "url": "http://cie.org.mx/leather.php?amount=1qw2f60krdrf8c",
                    "risk_score": null,
                    "created_at": "2019-04-12T02:58:20.011Z",
                    "updated_at": "2019-04-12T02:58:20.011Z"
                },
                "relationships": {
                    "hostname": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/2/relationships/hostname",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/2/hostname"
                        },
                        "data": {
                            "type": "hostnames",
                            "id": "1"
                        }
                    },
                    "clusters": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/2/relationships/clusters",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/2/clusters"
                        }
                    },
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/urls/2/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/urls/2/reports"
                        }
                    }
                }
            }
        ],
        "links": {
            "first": "https://tap.phishmecloud.com/api/public/v2/urls?filter%5Burl%5D=https%3A%2F%2Fwww.paypal.com%2Fus%2Chttp%3A%2F%2Fcie.org.mx%2Fleather.php%3Famount%3D1qw2f60krdrf8c&page%5Bnumber%5D=1&page%5Bsize%5D=20",
            "last": "https://tap.phishmecloud.com/api/public/v2/urls?filter%5Burl%5D=https%3A%2F%2Fwww.paypal.com%2Fus%2Chttp%3A%2F%2Fcie.org.mx%2Fleather.php%3Famount%3D1qw2f60krdrf8c&page%5Bnumber%5D=1&page%5Bsize%5D=20"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful for at least one URL(is_success = true):** print "Successfully enriched the following URLs using Cofense Triage: \n {0}".format(entity.identifier list)  
******if successful for at least one URL(is_success = true):** print "Action wasn't able to enrich the following URLs using Cofense Triage: \n {0}".format(entity.identifier list)  
******If fail to enrich for all entities (is_success = false):** Print: "No URLs were enriched."******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Enrich URL". Reason: {0}''.format(error.Stacktrace) | General  
CSV | Fields that are in the Enrichment table section, but without the prefix "COFENSE_TRG_" | Entity  
  
### Execute Playbook

#### Description

Initiate a playbook execution in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the ID of the report on which you want to execute the playbook.  
Playbook Name | String | N/A | Yes | Specify the name of the playbook that needs to be executed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If the 204 status code is reported (is_success=true):** "Successfully executed playbook {playbook name} on report {report id} in Cofense Triage." **The action should fail and stop a playbook execution:** **If an invalid value is provided for the "Max Records to Return" parameter:** "Error executing action "Execute Playbook". Reason: {0}''.format(error.Stacktrace)" **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Playbooks". Reason: {0}''.format(error.Stacktrace) **If errors are reported in the response:** "Error executing action "Execute Playbook". Reason: {0}''.format(detail)" **If the playbook is not found:** "Error executing action "Execute Playbook". Reason: playbook with name {name} is not found." | General  
  
### Get Domain Details

#### Description

Return information about the domain from Cofense Triage.

#### Parameters

**Parameter Display Name**  
---  
**N/A**  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "1",
                "type": "hostnames",
                "attributes": {
                    "hostname": "cie.org.mx",
                    "risk_score": null,
                    "created_at": "2019-04-12T02:58:19.893Z",
                    "updated_at": "2019-04-12T02:58:19.974Z"
                },
                "relationships": {
                    "clusters": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/relationships/clusters",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/clusters"
                        }
                    },
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/reports"
                        }
                    },
                    "urls": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/relationships/urls",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/1/urls"
                        }
                    }
                }
            },
            {
                "id": "2",
                "type": "hostnames",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/2"
                },
                "attributes": {
                    "hostname": "www.paypal.com",
                    "risk_score": null,
                    "created_at": "2019-04-12T02:58:19.898Z",
                    "updated_at": "2019-04-12T02:58:19.965Z"
                },
                "relationships": {
                    "clusters": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/relationships/clusters",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/clusters"
                        }
                    },
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/reports"
                        }
                    },
                    "urls": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/relationships/urls",
                            "related": "https://tap.phishmecloud.com/api/public/v2/hostnames/2/urls"
                        }
                    }
                }
            }
        ],
        "links": {
            "first": "https://tap.phishmecloud.com/api/public/v2/hostnames?filter%5Bhostname%5D=www.paypal.com%2Ccie.org.mx&page%5Bnumber%5D=1&page%5Bsize%5D=20",
            "last": "https://tap.phishmecloud.com/api/public/v2/hostnames?filter%5Bhostname%5D=www.paypal.com%2Ccie.org.mx&page%5Bnumber%5D=1&page%5Bsize%5D=20"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful for at least one URL(is_success = true):** print "Successfully returned details about the following domains using Cofense Triage: \n {0}".format(entity.identifier list)  
******if successful for at least one URL(is_success = true):** print "Action wasn't able to get details about the following domains using Cofense Triage: \n {0}".format(entity.identifier list)  
******If fail to enrich for all entities (is_success = false):** Print: "No information about the domains was found."******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Domain Details". Reason: {0}''.format(error.Stacktrace) | General  
CSV | **Table Name:** Domain DetailsTable Columns:Name - hostnameRisk Score - risk_score | General  
  
### Get Report Headers

#### Description

Return information about the header related to the report from Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the id of the report for which you want to retrieve headers.  
Max Headers To Return | Integer | 50 | No | Specify how many headers to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "4",
                "type": "headers",
                "attributes": {
                    "key": "Mime-Version",
                    "value": "1.0",
                    "created_at": "2020-11-03T16:43:33.767Z",
                    "updated_at": "2020-11-03T16:43:33.767Z"
                },
                "relationships": {
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/headers/4/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/headers/4/reports"
                        }
                    }
                }
            }
        ],
        "links": {
            "first": "https://tap.phishmecloud.com/api/public/v2/reports/13507/headers?page%5Bnumber%5D=1&page%5Bsize%5D=20",
            "last": "https://tap.phishmecloud.com/api/public/v2/reports/13507/headers?page%5Bnumber%5D=1&page%5Bsize%5D=20"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully returned related headers to the report with ID {0} in Cofense Triage.".format(report_id)  
******if unsuccessful aka status code 404(is_success = false):** print "Action wasn't able to return related headers to the report with ID {0} in Cofense Triage. Reason: \n {1}".format(report_id, errors/detail)  
******If no rules found (is_success = false):** Print: "No related headers were found to the report with ID {0} in Cofense Triage.".format(report_id)  
**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Report Headers". Reason: {0}''.format(error.Stacktrace) | General  
CSV | **Table Name:** Report {0} Headers**Table Columns:****Name -** key**Value -** value | General  
  
### Get Report Reporters

#### Description

Return information about the reporter related to the report from Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Report ID | String | N/A | Yes | Specify the id of the report for which you want to retrieve reporters.  
Max Reporters To Return | Integer | 50 | No | Specify how many reporters to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     "data": {
            "id": "5331",
            "type": "reporters",
            "attributes": {
                "email": "user@example.com",
                "reports_count": 277,
                "last_reported_at": "2020-11-06T18:32:47.000Z",
                "reputation_score": 561,
                "vip": true,
                "created_at": "2019-10-24T01:05:28.649Z",
                "updated_at": "2020-11-06T18:33:59.004Z"
            },
            "relationships": {
                "clusters": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reporters/5331/relationships/clusters",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reporters/5331/clusters"
                    }
                },
                "reports": {
                    "links": {
                        "self": "https://tap.phishmecloud.com/api/public/v2/reporters/5331/relationships/reports",
                        "related": "https://tap.phishmecloud.com/api/public/v2/reporters/5331/reports"
                    }
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully returned related reporters to the report with ID {0} in Cofense Triage.".format(report_id)  
******if unsuccessful aka status code 404(is_success = false):** print "Action wasn't able to return related reporters to the report with ID {0} in Cofense Triage. Reason: \n {1}".format(report_id, errors/detail)  
******If no rules found (is_success = false):** Print: "No related reporters were found to the report with ID {0} in Cofense Triage.".format(report_id)  
**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Report Reporters". Reason: {0}''.format(error.Stacktrace) | General  
CSV | **Table Name:** Report {0} Reporters**Table Columns:****Email -** email**Reports Count -** reports_count**Reputation Score -** reputation_score**VIP -** vip | General  
  
### Get Threat Indicator Details

#### Description

Return information about the entities based on the threat indicator details from Cofense Triage.

**Note:** Only MD5 and SHA256 hashes are supported.

#### Parameters

**Parameter Display Name**  
---  
**N/A**  
  
#### Run On

This action runs on all entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
COFENSE_TRG_ti_id | If available in JSON Result.  
COFENSE_TRG_ti_type | If available in JSON Result.  
COFENSE_TRG_ti_threat_level | If available in JSON Result.  
COFENSE_TRG_ti_threat_source | If available in JSON Result.  
COFENSE_TRG_ti_created_at | If available in JSON Result.  
COFENSE_TRG_id_updated_at | If available in JSON Result.  
  
##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "1",
                "type": "threat_indicators",
                "attributes": {
                    "threat_level": "Malicious",
                    "threat_type": "MD5",
                    "threat_value": "f1364ab115332cb44b5d7bb734d2cbf6",
                    "threat_source": "Triage-UI",
                    "created_at": "2019-06-06T18:55:38.107Z",
                    "updated_at": "2020-11-03T16:41:19.972Z"
                },
                "relationships": {
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/threat_indicators/1/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/threat_indicators/1/reports"
                        }
                    }
                }
            }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful for at least one entity(is_success = true):** print "Successfully returned threat indicator details about the following entities using Cofense Triage: \n {0}".format(entity.identifier list)  
******if successful for at least one entity(is_success = true):** print "Action wasn't able to return threat indicator details about the following entities using Cofense Triage: \n {0}".format(entity.identifier list)  
**If fail to enrich for all entities (is_success = false):** Print: "No threat indicator information about the entities was found."******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Threat Indicator Details". Reason: {0}''.format(error.Stacktrace) | General  
CSV | Fields that are in the Enrichment table section, but without the prefix "COFENSE_TRG_" | Entity  
  
### List Categories

#### Description

List available categories in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Names | CSV | N/A | No | Specify a comma-separated list of category names. This parameter is useful to check, whether a category with the specified name exists.  
Lowest Score To Fetch | Integer | N/A | No | Specify the lowest accepted score for the category. This parameter can work with negative values.  
Only Malicious | Checkbox | Unchecked | No | If enabled, the action only returns malicious categories.  
Only Archived | Checkbox | Unchecked | No | If enabled, the action only returns archived categories.  
Only Non Archived | Checkbox | Unchecked | No | If enabled, the action only returns non-archived categories.  
Only Non Malicious | Checkbox | Unchecked | No | If enabled, the action only returns non-malicious categories.  
Max Categories To Return | Integer | N/A | No | Specify the number of categories to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "1",
                "type": "categories",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/categories/1"
                },
                "attributes": {
                    "name": "Non-Malicious",
                    "score": -5,
                    "malicious": false,
                    "color": "#739d75",
                    "archived": false,
                    "created_at": "2019-04-11T08:24:49.787Z",
                    "updated_at": "2019-11-12T19:15:37.849Z"
                },
                "relationships": {
                    "one_clicks": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/categories/1/relationships/one_clicks",
                            "related": "https://tap.phishmecloud.com/api/public/v2/categories/1/one_clicks"
                        }
                    },
                    "reports": {
                        "links": {
                            "self": "https://tap.phishmecloud.com/api/public/v2/categories/1/relationships/reports",
                            "related": "https://tap.phishmecloud.com/api/public/v2/categories/1/reports"
                        }
                    }
                }
            }
        ],
        "links": {
            "first": "https://tap.phishmecloud.com/api/public/v2/categories?filter%5Barchived%5D=false&filter%5Bmalicious%5D=false&filter%5Bname%5D=Non-Malicious&filter%5Bscore_gteq%5D=-5&page%5Bnumber%5D=1&page%5Bsize%5D=20",
            "last": "https://tap.phishmecloud.com/api/public/v2/categories?filter%5Barchived%5D=false&filter%5Bmalicious%5D=false&filter%5Bname%5D=Non-Malicious&filter%5Bscore_gteq%5D=-5&page%5Bnumber%5D=1&page%5Bsize%5D=20"
        }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful (is_success=true):** "Successfully returned available categories from Cofense Triage." **If no categories are found (is_success=false)** "No categories were found for the criteria." **The action should fail and stop a playbook execution:** **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Categories". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available Categories **Table Column:**

  * Name - name
  * Score - score
  * ID - id
  * Malicious - malicious
  * Archived - archived

| General  
  
### List Playbooks

#### Description

List available playbooks in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Filter Key | DDL | Select One Possible Values:

  * Name
  * Description

| No | Specify the key that needs to be used to filter playbooks.  
Filter Logic | DDL | Not Specified Possible values:

  * Not Specified
  * Equal
  * Contains

| No | Specify the type of filter logic that should be applied. Filtering logic works based on the value provided in the "Filter Key" parameter. **Note:** The "Equals" logic is case sensitive, while "Contains" is case insensitive.  
Filter Value | String | N/A | No | Specify the value that should be used in the filter. If "Equal" is selected, the action tries to find the exact match among results. If "Contains" is selected, the action tries to find results that contain that substring. If nothing is provided in this parameter, the filter is not applied. Filtering logic works based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return. If nothing is provided, the action returns 50 records. Maximum: 200  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
            {
                "id": "1",
                "type": "playbooks",
                "links": {
                    "self": "https://reltest6.phishmecloud.com/api/public/v2/playbooks/1"
                },
                "attributes": {
                    "name": "SN_Test",
                    "description": "",
                    "active": true,
                    "button_color": "#204d74",
                    "add_rule_tags_to_report_tags": true,
                    "remove_existing_report_tags": false,
                    "remove_existing_cluster_tags": false,
                    "report_tags": [
                        "SN_Test"
                    ],
                    "cluster_tags": [
                        "SN_Cluster_Test",
                        "test1"
                    ],
                    "delete_report": false,
                    "guid": "b443a844-ffc2-49d2-8903-1a5f7fde7526",
                    "created_at": "2021-05-28T01:29:22.080Z",
                    "updated_at": "2022-04-08T06:04:17.016Z"
                }
            }
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If data is available (is_success=true):** "Successfully found playbooks for the provided criteria in Cofense Triage." **If data is not available (is_success=false):** "No playbooks were found for the provided criteria in Cofense Triage." **If the "Filter Value" parameter is empty (is_success=true):** "The filter was not applied, because parameter "Filter Value" has an empty value." **If the "Filter Logic" parameter is set to "Not Specified" (is_success=true):** "The filter was not applied, because parameter "Filter Logic" is not specified." **The action should fail and stop a playbook execution:** **If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":** "Error executing action "{action name}". Reason: you need to select a field from the "Filter Key" parameter." **If an invalid value is provided for the "Max Records to Return" parameter:** "Error executing action "{action name}". Reason: "Invalid value was provided for "Max Records to Return": PROVIDED_VALUE. Positive number should be provided"." **If a fatal error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Playbooks". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available Playbooks **Table Column:**

  * Name - name
  * Active - active
  * ID - id
  * Description - description
  * Tags - csv of report_tags + cluster_tags
  * Created At - created_at

| General  
  
### List Reports Related To Threat Indicators

#### Description

List reports related to threat indicators in Cofense Triage.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Create Case Wall Table | Checkbox | Unchecked | No | If enabled, action will create a case wall table with information about reports.  
Max Reports To Return | Integer | 100 | No | Specify how many reports to return.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "reports": [
            {
                "id": "13219",
                "type": "reports",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/reports/13219"
                },
                "attributes": {
                    "location": "Inbox",
                    "risk_score": null,
                    "from_address": null,
                    "subject": "Delivery reports about your e-mail",
                    "received_at": "2019-05-17T01:25:07.642Z",
                    "reported_at": "2019-05-16T23:01:50.000Z",
                    "raw_headers": "Date: Fri, 17 May 2019 01:25:07 +0000\r\nMessage-ID: <5cde0d73994b2_10902aea1885332418512@ip-10-132-9-226.ec2.internal.mail>\r\nSubject: Delivery reports about your e-mail\r\nMime-Version: 1.0\r\nContent-Type: multipart/mixed;\r\n boundary=\"--==_mimepart_5cde0d7399130_10902aea18853324184a7\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit",
                    "md5": "3e4c2e6e85695569ae7a11aac8a774c6",
                    "sha256": "1434d565d7735a841f39cb953cfdbbba1d0793324900d42c25b212b454a77993",
                    "match_priority": 4,
                    "tags": [],
                    "categorization_tags": [],
                    "processed_at": null,
                    "created_at": "2019-05-17T01:25:07.652Z",
                    "updated_at": "2019-05-17T01:25:10.032Z"
                },
                "meta": {
                    "risk_score_summary": null
                }
            },
            {
                "id": "13227",
                "type": "reports",
                "links": {
                    "self": "https://tap.phishmecloud.com/api/public/v2/reports/13227"
                },
                "attributes": {
                    "location": "Inbox",
                    "risk_score": null,
                    "from_address": null,
                    "subject": "Delivery reports about your e-mail",
                    "received_at": "2019-05-17T14:53:54.318Z",
                    "reported_at": "2019-05-16T23:01:50.000Z",
                    "raw_headers": "Date: Fri, 17 May 2019 14:53:54 +0000\r\nMessage-ID: <5cdecb024a663_107f2b040f2cd3306399@ip-10-132-9-226.ec2.internal.mail>\r\nSubject: Delivery reports about your e-mail\r\nMime-Version: 1.0\r\nContent-Type: multipart/mixed;\r\n boundary=\"--==_mimepart_5cdecb024a2fd_107f2b040f2cd3306387b\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit",
                    "md5": "92bb365c3fe712216610e884621c771a",
                    "sha256": "da37a508cd47987e9989fc8a2af12352c6652fa5c421f4556ef6a198bf73821e",
                    "match_priority": 4,
                    "tags": [],
                    "categorization_tags": [],
                    "processed_at": null,
                    "created_at": "2019-05-17T14:53:54.327Z",
                    "updated_at": "2019-05-17T14:53:56.453Z"
                },
                "meta": {
                    "risk_score_summary": null
                }
            }
        ],
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful:** "Successfully returned reports related to provided entities from Cofense Triage."  
**If no reports found:** "No related reports were found for the provided entities".******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Reports Related To Threat Indicators". Reason: (error.Stacktrace) | General  
Case Wall Table | **Table Name:** Related Reports**Table Column:** IDSubject Created At Location  | General  
  
### Ping

#### Description

Test connectivity to Cofense Triage with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful:_ ****"Successfully connected to the Cofense Triage server with the provided connection parameters!"  
****  
**The action should fail and stop a playbook execution:******  
****_If not successful:_ "Failed to connect to the Cofense Triage server! Error is {0}".format(exception.stacktrace) | General  
  
## Connector

## Cofense Triage - Reports Connector

Pull reports from Cofense Triage.

### Configure Cofense Triage - Reports Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | location | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://tap.phishmecloud.com | Yes | API Root of the Cofense Triage instance.  
Client ID | String | N/A | Yes | Client ID of the Cofense Triage account.  
Report Location | CSV | Inbox,Reconnaissance | No | Comma-separated list of report locations from which the connector should ingest data. Only reports from the provided locations will be ingested. The possible values are as follows:

  * Inbox
  * Reconnaissance
  * Processed

If no value is provided, the connector ingests reports from all locations.  
Client Secret | Password | N/A | Yes | Client Secret of the Cofense Triage account.  
Lowest Risk Score To Fetch | Integer | 0 | Yes | Lowest risk score that will be used to fetch emails. Maximum is 100.  
Category | CSV | N/A | No | Comma-separated list of categories used to filter the incoming reports. The connector ingests a report only if it matches at least one category in the list.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch emails.  
Max Reports To Fetch | Integer | 10 | No | How many reports to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Cofense Triage server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
