---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/orca-security/
title: Orca Security \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:36.621416+00:00
---

# Orca Security  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/orca-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Orca Security

This document provides guidance on how to integrate Orca Security with Google SecOps.

## Configure Orca Security integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
UI Root | String | https://{ui instance} | Yes | UI root of the Orca Security instance.  
API Root | String | https://{api instance} | Yes | API root of the Orca Security instance.  
API Key | String | N/A | Yes | API Key of the Orca Security instance account. If both the "API Key" and "API Token" parameters are provided, the "API Token" parameter is used.  
API Token | String | N/A | Yes | API Token of the Orca Security instance account. If both the "API Key" and "API Token" parameters are provided, the "API Token" parameter is used.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Orca Security SIEM server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate API key

  1. Go to **Settings- > Integrations-> Orca API**.
  2. Click **Manage Keys** , and then click **Generate a new key**.
  3. Copy and paste the generated key into Google SecOps.



## Use Cases

  1. Ingest alerts.
  2. Fetch information about assets or vulnerabilities.
  3. Triage alerts.
  4. Track compliance.



## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test connectivity to Orca Security with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Orca Security server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Orca Security server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Alert

Update an alert in Orca Security.

**Note:** This action only initiates the verification process of the alert.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert needs to be updated.  
Verify Alert | Checkbox | Unchecked | No | If enabled, the action initiates the verification process for the alert.  
Snooze State | DDL | Select OnePossible Values:

  * Select One
  * Snooze
  * Unsnooze

| No | Specify the snooze state for the alert.  
Snooze Days | String | 1 | No | Specify the number of days alert needs to be snoozed.This parameter is mandatory, if the "Snooze State" parameter is set to "Snooze".If nothing is provided, the action snoozes the alert for 1 day.  
Status | DDL | Select OnePossible Values:

  * Select One
  * Open
  * In Progress
  * Close
  * Dismiss

| No | Specify the status to set for the alert.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": "ss",
        "type": "Alert",
        "data": {
            "AlertId": {
                "value": "263534"
            },
            "AlertSource": {
                "value": "Orca Scan"
            },
            "AlertType": {
                "value": "cc"
            },
            "AssetData": {
                "value": {
                    "asset_name": "Armor-test/CE",
                    "asset_type": "cisource",
                    "asset_vpcs": [],
                    "asset_state": "enabled",
                    "account_name": "Armn",
                    "asset_category": "CI Source",
                    "cloud_provider": "shiftleft",
                    "cloud_vendor_id": "fbn",
                    "asset_tags_info_list": [
                        "retest_tag|maybe"
                    ],
                    "custom_tags_info_list": [],
                    "cluster_type": null,
                    "vm_id": null,
                    "asset_labels": null,
                    "resource_group_name": null,
                    "cluster_name": "An"
                }
            },
            "Category": {
                "value": "Vulnerabilities"
            },
            "ClosedReason": {
                "value": "user moved to done"
            },
            "ClosedTime": {
                "value": "2025-09-23T10:10:59+00:00"
            },
            "CommentsCount": {
                "value": 0
            },
            "CreatedAt": {
                "value": "2025-09-23T00:22:07+00:00"
            },
            "CveFixAvailable": {
                "value": true
            },
            "CveIds": {
                "value": [
                    "CVE"
                ]
            },
            "CveOpen": {
                "value": {
                    "CVE-2025-41249": {
                        "detected": "23.09.2025"
                    }
                }
            },
            "Description": {
                "value": "cc"
            },
            "Details": {
                "value": "cc"
            },
            "IsLive": {
                "value": true
            },
            "Labels": {
                "value": [
                    "fix_available"
                ]
            },
            "LastSeen": {
                "value": "2025-09-23T10:23:59+00:00"
            },
            "LastUpdated": {
                "value": "2025-09-23T11:36:35+00:00"
            },
            "MaxCvssScore": {
                "value": 7.5
            },
            "Name": {
                "value": "orca-1263534"
            },
            "OrcaScore": {
                "value": 3.1
            },
            "PrevUserDefinedStatus": {
                "value": "snoozed"
            },
            "Recommendation": {
                "value": "Pc"
            },
            "RelatedCompliances": {
                "value": []
            },
            "RemediationCli": {
                "value": []
            },
            "RemediationConsole": {
                "value": []
            },
            "RiskFindings": {
                "value": {
                    "cves": {
                        "fixable": 1,
                        "top_cves": [
                            {
                                "cve_id": "cc",
                                "fixable": true,
                                "cvss_score": 7.5,
                                "first_seen": "2025-09-23T00:22:12+00:00",
                                "cvss_source": "CNA v3",
                                "cvss_vector": "c",
                                "exploitable": false,
                                "cvss_severity": "HIGH",
                                "patched_version": "6.2.11",
                                "cvss_source_link": "cc"
                            }
                        ],
                        "total_cves": 1,
                        "exploitable": 0,
                        "count_by_cvss_severity": {
                            "HIGH": 1
                        }
                    },
                    "package": {
                        "target": "./jobs/job-scheduler/pom.xml",
                        "origin_url": "https://example.com",
                        "package_id": "org.sp",
                        "package_name": "cc",
                        "installed_version": "5.3.22"
                    }
                }
            },
            "RiskLevel": {
                "value": "low"
            },
            "RiskLevelTime": {
                "value": "2025-09-23T00:22:07+00:00"
            },
            "RuleId": {
                "value": "r81a3c225f3"
            },
            "RuleSource": {
                "value": "Orca"
            },
            "RuleType": {
                "value": "vulnerability"
            },
            "Score": {
                "value": 3
            },
            "ScoreVector": {
                "value": {
                    "AlertBaseScore": {
                        "score": 3.15,
                        "Features": [
                            {
                                "score": 0.0,
                                "value": "None",
                                "weight": 0.5,
                                "category": "Attack Impact",
                                "display_name": "Mitre Category",
                                "effect_level": 0,
                                "impact_level": 0.0
                            }
                        ],
                        "display_name": "Alert Base Score"
                    }
                }
            },
            "Severity": {
                "value": "hazardous"
            },
            "Source": {
                "value": "./jobs/job-scheduler/pom.xml"
            },
            "Status": {
                "value": "open"
            },
            "StatusTime": {
                "value": "2025-09-23T11:36:35+00:00"
            },
            "Title": {
                "value": "ccs"
            },
            "UserDefinedStatus": {
                "value": "open"
            },
            "VerificationStatus": {
                "value": "scan_failed"
            },
            "cluster_unique_id": {
                "value": "cc"
            },
            "GroupUniqueId": {
                "value": "cc"
            },
            "last_sync": {
                "value": "2025-09-23T10:44:43+00:00"
            }
        },
        "name": "orca-1263534",
        "group_unique_id": "cc",
        "cluster_unique_id": "cc",
        "last_seen": "2025-09-23T10:27:42+00:00"
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully updated alert with ID "{id}" in Orca Security."_If the "requested to set same configuration" error is reported (is_success=true):_ "Alert with ID "{id}" already has status "{status}" in Orca Security."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Alert". Reason: {0}''.format(error.Stacktrace)"_If other error is reported:_ "Error executing action "Update Alert". Reason: {error}."_If "Select One" is selected for the "Snooze State" parameter:_ "Error executing action "Update Alert". Reason: "Snooze Day" needs to be provided."_If "Select One" is selected for the "Snooze State" or "Status" parameter, and the "Verify Alert" parameter is not enabled:_ "Error executing action "Update Alert". Reason: at least one of the following parameters needs to be provided: "Status", "Verify Alert", "Snooze Alert". | General  
  
### Add Comment To Alert

Add a comment to alert in Orca Security.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert to which action needs to add a comment.  
Comment | String | N/A | Yes | Specify the comment that needs to be added to alert.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
      "unique_id": 315478535,
      "user_email": "tip.labops@siemplify.co",
      "user_name": "John Doe",
      "alert_id": "orca-264",
      "asset_unique_id": "AwsIamRole_570398916848_e739eb76-1d18-7e74-d3d4-42dc68c8ece4",
      "create_time": "2022-03-28T14:06:10+00:00",
      "type": "comment",
      "details": {
          "description": "Added comment",
          "comment": "asd"
      }
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******If the 200 status code is reported (is_success=true): "Successfully added a comment to alert with ID "{id}" in Orca Security."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Comment To Alert". Reason: {0}''.format(error.Stacktrace)"___If an error is reported:_ "Error executing action "Add Comment To Alert". Reason: {error}." | General  
  
### Get Asset Details

#### Description

Retrieve information about assets from Orca Security.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Asset IDs | CSV | N/A | Yes | Specify a comma-separated list of asset ids for which you want to return details.  
Return Vulnerabilities Information | Checkbox | Checked | No | If enabled, the action returns vulnerabilities that are related to the asset.  
Lowest Severity For Vulnerabilities | DDL | HazardousPossible Values:

  * Compromised
  * Imminent Compromise
  * Hazardous
  * Informational

| No | The lowest severity that needs to be used to fetch vulnerabilities.  
Max Vulnerabilities To Fetch | Integer | 50 | No | Specify the number of vulnerabilities to return per asset. Maximum: 100  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight for every enriched asset.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
        {
            "status": "success",
            "data": [
                {
                    "id": "cc",
                    "type": "cc",
                    "data": {
                        "Category": {
                            "value": "Storage"
                        },
                        "ConsoleUrlLink": {
                            "value": "helo"
                        },
                        "CreationTime": {
                            "value": "2025-09-23T16:24:59+00:00"
                        },
                        "Exposure": {
                            "value": "N/A"
                        },
                        "FirstSeen": {
                            "value": "2025-09-24T05:46:47+00:00"
                        },
                        "LastSeen": {
                            "value": "2025-09-24T15:13:16+00:00"
                        },
                        "Name": {
                            "value": "App Server"
                        },
                        "NewCategory": {
                            "value": "Data Storage"
                        },
                        "NewSubCategory": {
                            "value": "File System"
                        },
                        "Observations": {
                            "value": []
                        },
                        "OrcaScore": {
                            "value": 6.4
                        },
                        "Region": {
                            "value": "us-east-1"
                        },
                        "RelatedCompliances": {
                            "value": [
                                "abc",
                                "cc"
                            ]
                        },
                        "RiskLevel": {
                            "value": "medium"
                        },
                        "Score": {
                            "value": 4
                        },
                        "State": {
                            "value": "in-use"
                        },
                        "SubCategory": {
                            "value": "Volume"
                        },
                        "Tags": {
                            "value": {
                                "Client": "aw",
                                "Name": "App Server",
                                "SnapLabsManaged": "true"
                            }
                        },
                        "Type": {
                            "value": "cc"
                        },
                        "UiUniqueField": {
                            "value": "vol-cc"
                        },
                        "Zones": {
                            "value": [
                                "us-east-1b"
                            ]
                        },
                        "AssetUniqueId": {
                            "value": "cc"
                        },
                        "cluster_unique_id": {
                            "value": "cc"
                        },
                        "full_scan_time": {
                            "value": "2025-09-24T15:13:01+00:00"
                        },
                        "GroupUniqueId": {
                            "value": "cc"
                        }
                    },
                    "name": "App Server",
                    "group_unique_id": "cc",
                    "cluster_unique_id": "cc",
                    "asset_unique_id": "cc",
                    "last_seen": "2025-09-24T15:16:16+00:00"
                }
            ],
            "vulnerabilities": []
        }
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one asset (is_success=true):_ "Successfully enriched the following assets using information from Orca Security: {asset id}"_If data is not available for one asset (is_success=true):_ "Action wasn't able to enrich the following assets using information from Orca Security: {asset id}" _If data is not available for all assets (is_success=false):_ "None of the provided assets were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Asset Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Asset Details **Table Columns:**

  * Name: {asset_name}
  * Type: {asset_type}
  * Account: {account_name}
  * Category: {asset_category}
  * Subcategory: {asset_subcategory}
  * State: {asset_state}
  * Severity: {state/severity}
  * First Seen: {state/created_at}
  * Last Seen: {state/last_seen}

| General  
  
### Get Compliance Info

Get information about compliance based on selected frameworks in Orca Security.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Framework Names | CSV | N/A | No | Specify a comma-separated list of names of the frameworks for which you want to retrieve compliance details.If nothing is provided, the action returns information about all selected frameworks.  
Max Frameworks To Return | Integer | 50 | No | Specify the number of frameworks to return.  
Create Insight | Checkbox | Checked | Yes | If enabled, the action creates an insight containing information about compliance.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    "frameworks": [
      {
        "display_name": "Orca Best Practices",
        "id": "orca_best_practices",
        "custom": false,
        "description": "Orca Best Practices",
        "active": true,
        "avg_score_percent": 70,
        "test_results": {
          "FAIL": 121,
          "PASS": 284
        },
        "categories": {
          "total_count": 12,
          "data": {
            "Storage": {
              "FAIL": 28,
              "PASS": 35
            },
            "Database": {
              "FAIL": 8,
              "PASS": 94
            },
            "Monitoring": {
              "FAIL": 20,
              "PASS": 4
            },
            "Users and Access": {
              "FAIL": 23,
              "PASS": 11
            },
            "Network": {
              "FAIL": 29,
              "PASS": 96
            },
            "Messaging Service": {
              "FAIL": 1,
              "PASS": 11
            },
            "Serverless": {
              "FAIL": 3,
              "PASS": 13
            },
            "Vm": {
              "FAIL": 6,
              "PASS": 4
            },
            "Authentication": {
              "FAIL": 4,
              "PASS": 10
            },
            "Account": {
              "PASS": 1
            },
            "ComputeServices": {
              "FAIL": 1,
              "PASS": 2
            },
            "Container": {
              "PASS": 1
            }
          }
        },
        "top_accounts": [
          {
            "570398916848": {
              "account_name": "alon-vendors",
              "FAIL": 121,
              "PASS": 284
            }
          }
        ]
      }
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully returned information about compliance in Orca Security."_If one framework is not found (is_success=true):_ "Information from the following frameworks wasn't found in Orca Security. Please check the spelling."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Compliance Info". Reason: {0}''.format(error.Stacktrace)"_If all frameworks are not found (is_success=false):_ "Error executing action "Get Compliance Info". Reason: none of the provided frameworks were found in Orca Security. Please check the spelling. | General  
Case Wall Table | **Table Name:** Compliance Details **Table Columns:**

  * Name: {display_name}
  * Description: {description}
  * Score: {avg_score_percent}
  * Failed: {test_results/FAIL}
  * Passed: {test_results/PASS}
  * Active: {active}

| General  
  
### Scan Assets

Scan assets in Orca Security.

**Note:** This action runs as async. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Asset IDs | String | N/A | Yes | Specify a comma-separated list of asset ids for which you want to return details.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
      "version": "0.1.0",
      "scan_unique_id": "4f606aae-9e9b-4d01-aa29-797a06b6300e",
      "asset_unique_ids": [
          "i-080f6dfdeac0c7ffc"
      ],
      "status": "done"
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one asset (is_success=true):_ "Successfully scanned the following assets in Orca Security: {asset name}"._If data is not available for one asset or the asset is not found (is_success=true):_ "Action wasn't able to scan the following assets using in Orca Security: {asset name}"_If data is not available for all assets (is_success=false):_ "None of the provided assets were scanned."_Async message:_ "Pending assets: {asset names}"**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Scan Assets". Reason: {0}''.format(error.Stacktrace)"_If ran into a timeout:_ "Error executing action "Scan Assets". Reason: action ran into a timeout during execution. Pending assets: {assets that are still in progress}. Please increase the timeout in IDE." | General  
  
### Get Vulnerability Details

#### Description

Retrieve information about vulnerabilities from Orca Security.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
CVE IDs | CSV | N/A | No | Specify a comma-separated list of CVEs that need to be enriched.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight for every enriched vulnerability.Insight creation is not affected by the filtering that can be made with the "Fields To Return" parameter.  
Max Assets To Return | Integer | 50 | No | Specify how many assets related to the CVE to return.Maximum: 10000  
Fields To Return | CSV | N/A | No | Specify a comma-separated list of fields that need to be returned.If vulnerabilities don't have specific fields to return, such fields values are set to nulls.**Note:** This parameter checks the JSON object, as it was flattened.Example: "object": {"id": 123} -> object_id is the key.  
Output | DDL | JSONPossible Values:

  * JSON
  * CSV

| No | Specify the type of the output for the action.If "JSON" is selected, the action returns a regular JSON Result. If "CSV" is selected, the action creates a file in the action execution folder and JSON result contains a path to that file.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "cve_id": "{cve_id}",
        "results": [
            {
                "asset_auto_updates": "off",
                "vm_asset_unique_id": "vm_570398916848_i-07cb1901406d7f7a2",
                "group_type_string": "VM",
                "asset_regions_names": [
                    "N. Virginia"
                ],
                "group_type": "asg",
                "cluster_type": "asg",
                "type": "cve",
                "score": 4,
                "vm_id": "i-07cb1901406d7f7a2",
                "asset_name": "alon-test",
                "context": "data",
                "nvd": {
                    "cvss2_severity": "MEDIUM",
                    "cvss2_score": 5.0,
                    "cvss3_severity": "HIGH",
                    "cvss3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N",
                    "cvss3_score": 7.5,
                    "cvss2_vector": "AV:N/AC:L/Au:N/C:N/I:P/A:N"
                },
                "asset_distribution_version": "2 (2022.01.05)",
                "asset_first_public_ips": [
                    "54.234.117.173"
                ],
                "asset_first_private_ips": [
                    "10.0.85.56"
                ],
                "group_name": "alon-test",
                "level": 1,
                "fix_available_state": "Yes",
                "organization_name": "Partners",
                "published": "2019-09-30T19:15:00+00:00",
                "packages": [
                    {
                        "installed_version": "1.12.13",
                        "package_name": "/opt/cni/bin/vlan",
                        "non_os_package_paths": [
                            "/opt/cni/bin/vlan"
                        ],
                        "patched_version": "1.13.1"
                    },
                    {
                        "installed_version": "1.12.13",
                        "package_name": "/opt/cni/bin/ipvlan",
                        "non_os_package_paths": [
                            "/opt/cni/bin/ipvlan"
                        ],
                        "patched_version": "1.13.1"
                    },
                    {
                        "installed_version": "1.12.13",
                        "package_name": "/opt/cni/bin/firewall",
                        "non_os_package_paths": [
                            "/opt/cni/bin/firewall"
                        ],
                        "patched_version": "1.13.1"
                    },
                    {
                        "installed_version": "1.12.13",
                        "package_name": "/opt/cni/bin/tuning",
                        "non_os_package_paths": [
                            "/opt/cni/bin/tuning"
                        ],
                        "patched_version": "1.13.1"
                    },
                    {
                        "installed_version": "1.12.13",
                        "package_name": "/opt/cni/bin/loopback",
                        "non_os_package_paths": [
                            "/opt/cni/bin/loopback"
                        ],
                        "patched_version": "1.13.1"
                    }
                ],
                "cloud_vendor_id": "570398916848",
                "labels": [
                    "fix_available"
                ],
                "asset_image_id": "ami-0d6c8b2a8562eba37",
                "asset_num_public_dnss": 1,
                "cve_id": "CVE-2019-16276",
                "asset_state": "running",
                "organization_id": "e739eb76-3d1a-4022-b5d0-360b10d44685",
                "asset_availability_zones": [
                    "us-east-1b"
                ],
                "asset_unique_id": "vm_570398916848_i-07cb1901406d7f7a2",
                "asset_num_private_dnss": 1,
                "asset_vendor_id": "i-07cb1901406d7f7a2",
                "cvss3_score": 6.5,
                "group_val": "nongroup",
                "asset_type_string": "VM",
                "asset_regions": [
                    "us-east-1"
                ],
                "group_unique_id": "asg_570398916848_alon-test",
                "cloud_account_id": "1b6a52d3-58ed-4879-af03-b99f252f532d",
                "asset_num_private_ips": 1,
                "account_name": "alon-vendors",
                "asset_type": "vm",
                "fix_available": true,
                "cvss3_vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N",
                "cluster_unique_id": "asg_570398916848_alon-test",
                "summary": "Go before 1.12.10 and 1.13.x before 1.13.1 allow HTTP Request Smuggling.",
                "severity": "informational",
                "cluster_name": "alon-test",
                "asset_first_public_dnss": [
                    "ec2-54-234-117-173.compute-1.amazonaws.com"
                ],
                "tags_info_list": [
                    "aws:ec2launchtemplate:version|1",
                    "aws:autoscaling:groupName|alon-test",
                    "aws:ec2launchtemplate:id|lt-09b558a2361e6b988"
                ],
                "asset_first_private_dnss": [
                    "ip-10-0-85-56.ec2.internal"
                ],
                "cloud_provider": "aws",
                "asset_vpcs": [
                    "vpc-07ef7f777429cfd82"
                ],
                "source_link": "https://nvd.nist.gov/vuln/detail/CVE-2019-16276",
                "asset_category": "VM",
                "asset_distribution_major_version": "2",
                "asset_tags_info_list": [
                    "aws:ec2launchtemplate:version|1",
                    "aws:autoscaling:groupName|alon-test",
                    "aws:ec2launchtemplate:id|lt-09b558a2361e6b988"
                ],
                "cloud_provider_id": "570398916848",
                "asset_num_public_ips": 1,
                "asset_labels": [
                    "brute-force_attempts"
                ],
                "asset_distribution_name": "Amazon",
                "affected_packages": [
                    "/opt/cni/bin/vlan",
                    "/opt/cni/bin/ipvlan",
                    "/opt/cni/bin/firewall",
                    "/opt/cni/bin/tuning",
                    "/opt/cni/bin/loopback"
                ],
                "asset_role_names": [
                    "ssh"
                ]
            }
        ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one vulnerability (is_success=true):_ "Successfully enriched the following vulnerabilities using information from Orca Security: {cve id}"_If data is not available for one vulnerability (is_success=true):_ "Action wasn't able to enrich the following vulnerabilities using information from Orca Security: {cve id}"_If data is not available for all vulnerabilities (is_success=false):_ "None of the provided vulnerabilities were enriched."**The action should fail and stop a playbook execution:******If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Get Vulnerability Details". Reason: {0}''.format(error.Stacktrace)" | General  
Case Wall Table | **Table Name:** Vulnerability Details**Table Columns:**

  * ID: {cve_id}
  * Description: {summary}
  * Fix Available: {fix_available}
  * Affected Assets Count: {group_size}
  * Labels: {csv of labels}
  * Publish Date: {published}

| General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

## Orca Security - Alerts Connector

#### Description

Pull information about alerts from Orca Security.

**Note:** The dynamic list filter works with the "data.title" parameter.

#### Configure Orca Security - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | asset_type_string | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | **""** | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field using regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https:/{{IP}}:8501 | Yes | API root of the Orca Security instance.  
API Key | String | N/A | Yes | API Key of the Orca Security instance account. If both the "API Key" and "API Token" parameters are provided, the "API Token" parameter is used.  
API Token | String | N/A | Yes | API Token of the Orca Security instance account. If both the "API Key" and "API Token" parameters are provided, the "API Token" parameter is used.  
Category Filter | CSV | N/A | No | A comma-separated list of category names that should be used during ingestion of the alerts. **Note:** This parameter is case sensitive. | Lowest Priority To Fetch | String | N/A | No | The lowest severity that needs to be used to fetch alerts. Possible values: Compromised, Imminent compromise, Hazardous, Informational If nothing is specified, the connector ingests alerts with all severities.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 100 | No | Number of alerts to process per one connector iteration.  
Use dynamic list as a blacklist | Checkbox | Unchecked | Yes | If enabled, dynamic lists is used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the Orca Security server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Alert Type Filter | CSV | N/A | No | Type of the alerts that need to be ingested. This filter works with the `AlertType_value` parameter in response. Example: `aws_s3_bucket_accessible_to_unmonitored_account`  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
