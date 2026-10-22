---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali/
title: Integrate Anomali with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:45.108278+00:00
---

# Integrate Anomali with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Anomali with Google SecOps 

This document describes how to integrate Anomali with Google Security Operations (Google SecOps).

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Anomali.zip).

## Before you begin

To obtain your personal API Key, complete the following steps:

  1. Sign in to your [Anomali ThreatStream account](https://ui.threatstream.com/login).

  2. Click **My API Keys**.

  3. Copy the API key value and paste it into the Api Key parameter field in the **Configure Instance** dialog in Google SecOps.




### Network

Function | Default port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://api.threatstream.com/api | Yes | Address of the Anomali instance.  
Username | String | `user@domain.com` | Yes | The email address of the user which should be used to connect to Anomali.  
Password | Password | N/A | Yes | The password of the according user.  
Api Key | String | N/A | Yes | API key generated in AlienVault console.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Threat Info

Enrich entities using information from Anomali ThreatStream. Supported entities: IP, URL, Hash, Email Addresses (User entities that match email regex).

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Limit | String | 10 | Yes | Specify how many records to return per entity.  
Severity Threshold | DDL | Medium Possible values:

  * Very High
  * High
  * Medium
  * Low

| No | Specify what should be the severity threshold for the entity, in order to mark it as suspicious. If multiple records are found for the same entity, action will take the highest severity out of all available records.  
Confidence Threshold | Integer | 50 | No | Specify what should be the confidence threshold for the entity, in order to mark it as suspicious. Note: Maximum is 100. If multiple records are found for the entity, action will take the average. Active records have priority. Default: 50.  
Ignore False Positive Status | Checkbox | Unchecked | No | If enabled, action will ignore the false positive status and mark the entity as suspicious based on the Severity Threshold and Confidence Threshold. If disabled, action will never label false positive entities as suspicious, regardless, if they pass the Severity Threshold and Confidence Threshold conditions or not.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * URL
  * Hash
  * Email Addresses (User entities that match email regex)



#### Action results

##### Entity enrichment

Name | Logic - When To Apply  
---|---  
id | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
itype | Returns if it exists in JSON result  
expiration_time | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
feed_id | Returns if it exists in JSON result  
confidence | Returns if it exists in JSON result  
uuid | Returns if it exists in JSON result  
retina_confidence | Returns if it exists in JSON result  
trusted_circle_ids | Returns if it exists in JSON result  
source | Returns if it exists in JSON result  
latitude | Returns if it exists in JSON result  
type | Returns if it exists in JSON result  
description | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
threat_score | Returns if it exists in JSON result  
source_confidence | Returns if it exists in JSON result  
modification_time | Returns if it exists in JSON result  
org_name | Returns if it exists in JSON result  
asn | Returns if it exists in JSON result  
creation_time | Returns if it exists in JSON result  
tlp | Returns if it exists in JSON result  
country | Returns if it exists in JSON result  
longitude | Returns if it exists in JSON result  
severity | Returns if it exists in JSON result  
subtype | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
        {
            "Entity": "ENTITY_ID",
            "EntityResult": {
                "Info": [{
                    "source_created": null,
                    "status": "inactive",
                    "itype": "mal_domain",
                    "expiration_ts": "2020-11-28T13:29:57.000Z",
                    "ip": "192.0.2.1",
                    "is_editable": false,
                    "feed_id": 1111111,
                    "update_id": 1111111111,
                    "longitude": -0.1223454,
                    "is_public": true,
                    "threat_type": "malware",
                    "workgroups": [],
                    "rdns": null,
                    "confidence": 11111,
                    "uuid": "UUID",
                    "retina_confidence": 1111111,
                    "trusted_circle_ids": null,
                    "id": 111111111111111110000,
                    "source": "COVID19 Cyber Threat Coalition Blocklist - Domains",
                    "owner_organization_id": 111,
                    "import_session_id": null,
                    "source_modified": null,
                    "type": "domain",
                    "sort": [1607193157800, "56224953198"],
                    "description": null,
                    "tags": [{
                        "id": "wu6",
                        "name": "Blocklist"
                    }, {
                        "id": "pvj",
                        "name": "Coronavirus"
                    }, {
                        "id": "01i",
                        "name": "COVID-19"
                    }, {
                        "id": "o70",
                        "name": "Malicious"
                    }, {
                        "id": "fk0",
                        "name": "Source:COVID19-Cyber-Threat-Coalition"
                    }],
                    "threatscore": 11111,
                    "source_reported_confidence": 11111,
                    "modified_ts": "2020-12-05T18:32:37.800Z",
                    "org": "Namecheap",
                    "asn": "11111111",
                    "created_ts": "2020-10-29T13:33:24.904Z",
                    "tlp": null,
                    "is_anonymous": false,
                    "latitude": 51.4964,
                    "country": "GB",
                    "can_add_public_tags": false,
                    "value": "VALUE",
                    "subtype": null,
                    "meta": {
                        "registration_updated": "2020-10-24T22:16:59+00:00",
                        "detail2": "bifocals_deactivated_on_2020-12-05_18:30:00.085789",
                        "severity": "high",
                        "registration_created": "2020-10-24T22:16:42+00:00"
                    },
                    "resource_uri": "/api/v2/intelligence/"
                }],
                "Campaigns": [{
                    "association_info": [{
                        "comment": null,
                        "created": "2020-10-29T13:33:29.200283",
                        "from_id": "ID"
                    }],
                    "can_add_public_tags": true,
                    "circles": [],
                    "created_ts": "2020-03-15T04:24:55.428496",
                    "end_date": "2020-03-23T16:05:00.761000",
                    "feed_id": 0,
                    "id": "ID",
                    "is_anonymous": true,
                    "is_cloneable": "yes",
                    "is_public": true,
                    "modified_ts": "2021-02-02T02:38:19.892072",
                    "name": "Coronavirus (COVID-19)",
                    "objective": null,
                    "organization": {
                        "id": 0,
                        "name": "Analyst",
                        "title": "Analyst"
                    },
                    "publication_status": "published",
                    "published_ts": "2020-04-06T21:40:24.452312",
                    "resource_uri": "/api/v1/campaign/",
                    "source_created": null,
                    "source_modified": null,
                    "start_date": "2020-01-30T13:10:00.070000",
                    "status": {
                        "display_name": "Ongoing",
                        "id": 1,
                        "resource_uri": "/api/v1/campaignstatus/1/"
                    },
                    "tags": ["Malware", "Fraud", "Phishing", "COVID-19", "Coronavirus", "Scams"],
                    "tags_v2": [{
                        "id": "wqe",
                        "name": "Coronavirus"
                    }, {
                        "id": "hlg",
                        "name": "COVID-19"
                    }, {
                        "id": "74i",
                        "name": "Phishing"
                    }, {
                        "id": "0y2",
                        "name": "Malware"
                    }, {
                        "id": "u63",
                        "name": "Scams"
                    }, {
                        "id": "1er",
                        "name": "Fraud"
                    }],
                    "tlp": "white",
                    "uuid": "UUID",
                    "workgroups": []
                }],
                "Tip": [{
                    "all_circles_visible": true,
                    "association_info": [{
                        "comment": null,
                        "created": "2020-10-29T13:33:29.212118",
                        "from_id": "ID"
                    }],
                    "body_content_type": "richtext",
                    "campaign": null,
                    "can_add_public_tags": true,
                    "circles": [],
                    "created_ts": "2020-03-19T04:23:35.714929",
                    "feed_id": 0,
                    "id": "ID",
                    "is_anonymous": true,
                    "is_cloneable": "yes",
                    "is_editable": true,
                    "is_email": false,
                    "is_public": true,
                    "modified_ts": "2021-02-02T02:38:20.061912",
                    "name": "Coronavirus (COVID-19) Cyber Threats",
                    "original_source": null,
                    "original_source_id": null,
                    "owner_org": {
                        "id": 0,
                        "name": "Analyst",
                        "title": "Analyst"
                    },
                    "parent": null,
                    "published_ts": "2020-05-25T18:39:36.890647",
                    "resource_uri": "/api/v1/ID/",
                    "source_created": null,
                    "source_modified": null,
                    "starred_by_me": false,
                    "starred_total_count": 5,
                    "status": "published",
                    "tags": ["Scams", "HCL-", "Malware"],
                    "tags_v2": [{
                        "id": "ID",
                        "name": "Coronavirus"
                    }, {
                        "id": "ID",
                        "name": "COVID-19"
                    }, {
                        "id": "ID",
                        "name": "Phishing"
                    }],
                    "threat_actor": null,
                    "tlp": "white",
                    "ttp": null,
                    "uuid": "UUID",
                    "votes": {
                        "me": null,
                        "total": 0
                    },
                    "watched_by_me": false,
                    "watched_total_count": 11111,
                    "workgroups": []
                }],
                "Actors": [],
                "Incidents": [],
                "TTP": []
            }
        }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | _If data is available for one entity (is_success=true):_ "Successfully returned information about the following entities from Anomali ThreatStream: {entity.identifier}" _If no data is available for one entity (is_success=true):_ "Action wasn't able to return information about the following entities from Anomali ThreatStream: {entity.identifier}" _If not available for all entities (is_success=false):_ "No entities were enriched. _Critical error (fail):_ Error executing action "Get Threat Info". Reason: {error traceback}" | General  
  
### Ping

Test connectivity to Anomali ThreatStream.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
### Get Related Associations

Retrieve entity related associations from Anomali ThreatStream.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Return Campaigns | Checkbox | Checked | No | If enabled, action will fetch related campaigns and details about them.  
Return Threat Bulletins | Checkbox | Checked | No | If enabled, action will fetch related threat bulletins and details about them.  
Return Actors | Checkbox | Checked | No | If enabled, action will fetch related actors and details about them.  
Return Attack Patterns | Checkbox | Checked | No | If enabled, action will fetch related attack patterns and details about them.  
Return Courses Of Action | Checkbox | Checked | No | If enabled, action will fetch related courses of action and details about them.  
Return Identities | Checkbox | Checked | No | If enabled, action will fetch related identities and details about them.  
Return Incidents | Checkbox | Checked | No | If enabled, action will fetch related incidents and details about them.  
Return Infrastructure | Checkbox | Checked | No | If enabled, action will fetch related infrastructure and details about them.  
Return Intrusion Sets | Checkbox | Checked | No | If enabled, action will fetch related intrusion sets and details about them.  
Return Malware | Checkbox | Checked | No | If enabled, action will fetch related malware and details about them.  
Return Signatures | Checkbox | Checked | No | If enabled, action will fetch related signatures and details about them.  
Return Tools | Checkbox | Checked | No | If enabled, action will fetch related tools and details about them.  
Return TTPs | Checkbox | Checked | No | If enabled, action will fetch related TTPs and details about them.  
Return Vulnerabilities | Checkbox | Checked | No | If enabled, action will fetch related vulnerabilities and details about them.  
Create Campaign Entity | Checkbox | Unchecked | No | If enabled, action will create an entity out of available Campaign associations.  
Create Actors Entity | Checkbox | Unchecked | No | If enabled, action will create an entity out of available Actor associations.  
Create Signature Entity | Checkbox | Unchecked | No | If enabled, action will create an entity out of available Signature associations.  
Create Vulnerability Entity | Checkbox | Unchecked | No | If enabled, action will create an entity out of available Vulnerability associations.  
Max Associations To Return | Integer | 5 | No | Specify how many associations to return per type.  
  
#### Run on

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * Email



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
    {
        "campaign": [
            {
                "name": "Example 1",
                "id": 1
            },
            {
                "name": "Example 2",
                "id": 2
            }
        ],
        "actor": [
            {
                "name": "Actor 1",
                "id": 1
            },
            {
                "name": "Actor 2",
                "id": 2
            }
        ],
        "attackpattern": [
            {
                "name": "Pattern 1",
                "id": 1
            },
            {
                "name": "Pattern 2",
                "id": 2
            }
        ],
        "courseofaction": [
            {
                "name": "Course of Action 1",
                "id": 1
            },
            {
                "name": "Course Of Action 2",
                "id": 2
            }
        ],
        "identity": [
            {
                "name": "Identity 1",
                "id": 1
            },
            {
                "name": "Identity 2",
                "id": 2
            }
        ],
        "incident": [
            {
                "name": "Incident 1",
                "id": 1
            },
            {
                "name": "Incident 2",
                "id": 2
            }
        ],
        "infrastructure": [
            {
                "name": "Infrustructure 1",
                "id": 1
            },
            {
                "name": "Infrustructure 2",
                "id": 2
            }
        ],
        "intrusionset": [
            {
                "name": "Intrusion set 1",
                "id": 1
            },
            {
                "name": "Intrusion set 2",
                "id": 2
            }
        ],
        "malware": [
            {
                "name": "Malware 1",
                "id": 1
            },
            {
                "name": "Malware 2",
                "id": 2
            }
        ],
        "signature": [
            {
                "name": "Signature 1",
                "id": 1
            },
            {
                "name": "Signature 2",
                "id": 2
            }
        ],
        "tool": [
            {
                "name": "Tool 1",
                "id": 1
            },
            {
                "name": "Tool 2",
                "id": 2
            }
        ],
        "ttp": [
            {
                "name": "TTP 1",
                "id": 1
            },
            {
                "name": "TTP 2",
                "id": 2
            }
        ],
        "vulnerability": [
            {
                "name": "Vulnerability 1",
                "id": 1
            },
            {
                "name": "Vulnerability 2",
                "id": 2
            }
        ],
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one association across entities is found (is_success=true):_ "Successfully retrieved related associations from Anomali" _If no associations are found (is_success=false):_ "No related associations were found." _Async Message:_ "Waiting for all of the association details to be retrieved" **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Related Association". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** "Related Associations" **Table Columns:**

  * ID
  * Name
  * Type
  * Status 

|   
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
