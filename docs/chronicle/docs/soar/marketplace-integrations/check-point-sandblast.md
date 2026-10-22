---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-sandblast/
title: Check Point SandBlast \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:37.183878+00:00
---

# Check Point SandBlast  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-sandblast/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Check Point SandBlast

**Important:** Check Point SandBlast was renamed to Harmony Endpoint.

This document describes how to integrate Check Point SandBlast with Google Security Operations.

## Configure Check Point SandBlast integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://<service_address>/tecloud/ api/<version>/file | Yes | Specify the Check Point SandBlast Api root URl.  
API Key | Password | N/A | Yes | Specify the Check Point SandBlast API key.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the Check Point SandBlast server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Check Point SandBlast with parameters provided at the integration configuration page in the Google Security Operations Marketplace tab.

#### Parameters

N/A

#### Use Cases

Test connectivity to the target system with parameters configured for Integration from the Google SecOps server.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully connected to the Check Point SandBlast server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the SandBlast server! Error is {}".format(e) | General  
  
### Query

#### Description

Get threat reputation information about FILEHASH entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threshold | String | 0 | Yes | Mark entity as suspicious if severity is equal or above the given threshold.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entities are marked as suspicious if:

  1. Threat Emulation combined verdict equals malicious.
  2. AV severity is greater than or equal to threshold (in the JSON: av.malware_info.severity).

Enrichment Field Name | Logic  
---|---  
SandBlast_av_block | Returns if it exists in JSON  
SandBlast_av_signature_name | Returns if it exists in JSON  
SandBlast_av_severity | Returns if it exists in JSON  
SandBlast_av_confidence | Returns if it exists in JSON  
SandBlast_te_combined_verdict | Returns if it exists in JSON  
SandBlast_te_severity | Returns if it exists in JSON  
SandBlast_te_confidence | Returns if it exists in JSON  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "Entity": "8a2f57269b2f47b4e8f2e122e424754b",
            "EntityResult": {
            "status": {
                "code": 1006,
                "label": "PARTIALLY_FOUND",
                "message": "The request cannot be fully answered at this time."
            },
            "md5": "8a2f57269b2f47b4e8f2e122e424754b",
            "file_type": "",
            "file_name": "untitled.doc",
            "features": ["te", "av"],
            "te": {
                "trust": 0,
                "images": [{
                    "report": {
                        "verdict": "unknown"
                    },
                    "status": "not_found",
                    "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
                    "revision": 1
                }, {
                    "report": {
                        "verdict": "unknown"
                    },
                    "status": "not_found",
                    "id": "5e5de275-a103-4f67-b55b-47532918fa59",
                    "revision": 1
                }],
                "score": -2147483648,
                "status": {
                    "code": 1004, "label": "NOT_FOUND",
                    "message": "Could not find the requested file. Please upload it."
                }},
            "av": {
                "malware_info": {
                    "signature_name": "",
                    "malware_family": 0,
                    "malware_type": 0,
                    "severity": 0,
                    "confidence": 0
                },
                "status": {
                    "code": 1001,
                    "label": "FOUND",
                    "message": "The request has been fully answered."
                }
            }
        }
    }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully found info the following entities:..."_If partially successful:_ "Partial information was found for the following entities:..."_If not found entities:_ "No information was found for the following entities:..."_If failed to find entities:_ "Failed to fetch information for the following entities:..."_If not successful:_ "No entities were enriched."__**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ "An error occurred while running action. Error: {}".format(e) | General  
  
### Upload File

#### Description

Upload files for analysis.

**Note:** The "Upload File" action takes a suspicious file, and uses its path and name to upload it to the sandblast engine. The upload action is not waiting for the results and just makes sure that the file is uploaded. Regardless of the results - the upload action can happen at any time and if needed - the "query" action should take place after this one so that the data for the uploaded file is then pulled into Google SecOps.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
file path | String | N/A | Yes | path to the file to be uploaded  
file name | String | N/A | Yes | Display Name of the uploaded file  
Enable Threat Emulation feature | Checkbox | Checked | No | If enabled, threat emulation feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.  
Enable AntiVirus feature | Checkbox | Unchecked | No | If enabled, antivirus feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.  
Enable Threat Extraction feature | Checkbox | Unchecked | No | If enabled, threat extraction feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "Entity": "/tmp/test.txt",
            "EntityResult": {
                "status": {
                    "code": 1002,
                    "label": "UPLOAD_SUCCESS",
                    "message": "The file was uploaded successfully."
                },
                "sha1": "6caf005c3183d9b5b8dfa5b60f24eb1ebbfab876",
                "md5": "c12c504bbe0f7be6ca87d4933c43fac1",
                "sha256": "e757f729d149e047705ad6adfbcdd28b0ad28899385712ee0a58261bcb03ac36",
                "file_type": "",
                "file_name": "2020092414.log",
                "features": ["te"],
                "te": {
                    "trust": 0,
                    "images": [{
                        "report": {
                            "verdict": "unknown"
                        },
                        "status": "not_found",
                        "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
                        "revision": 1
                    }, {
                        "report": {
                            "verdict": "unknown"
                        },
                        "status": "not_found",
                        "id": "5e5de275-a103-4f67-b55b-47532918fa59",
                        "revision": 1
                    }],
                    "score": -2147483648,
                    "status": {
                        "code": 1002,
                        "label": "UPLOAD_SUCCESS",
                        "message": "The file was uploaded successfully."
                    }
                }
            }
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful_**:** "Successfully uploaded the following files: {}".format(".join([file_path for file_path in successful_paths])Else: "No files were uploaded."_If failed:_ "An error occurred on the following files: {}Please check logs for more information.".format(".join([file_path for file_path in failed_paths])" **The action should fail and stop a playbook execution:******_If_ a ****_critical error, like wrong credentials or lost connectivity is reported:_ "An error occurred while running action. Error: {}".format(e) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
