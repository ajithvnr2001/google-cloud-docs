---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali-threatstream/
title: Integrate Anomali ThreatStream with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:52.116419+00:00
---

# Integrate Anomali ThreatStream with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/anomali-threatstream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Anomali ThreatStream with Google SecOps

This document describes how to integrate Anomali ThreatStream with Google Security Operations (Google SecOps).

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Web Root | String | https://siemplify.threatstream.com | Yes | Web Root of the Anomali ThreatStream instance. This parameter is used for creating report links across integration items.  
API Root | String | https://api.threatstream.com | Yes | API Root of the Anomali ThreatStream instance.  
Email Address | String | N/A | Yes | Email address of the Anomali ThreatStream account.  
API Key | Password | N/A | Yes | API key of the Anomali ThreatStream account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Anomali ThreatStream server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Tags To Entities

Add tags to entities in Anomali ThreatStream.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Tags | CSV | N/A | Yes | Specify a comma-separated list of tags that need to be added to entities in Anomali ThreatStream.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * Email



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one hash across entities is found (is_success=true):_ "Successfully added tags to the following entities in Anomali ThreatStream:\n{0}".format(entity.identifier list) _If not found specific entities (is_success=true):_ "The following entities were not found in Anomali ThreatStream\n: {0}".format([entity.identifier]) _If not found all entities (is_success=false):_ "None of the provided entities were found." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Add Tags To Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Enrich Entities

Retrieve information about IPs, URLs, hashes, email addresses from Anomali ThreatStream.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Severity Threshold | DDL | Low Possible values:

  * Very High
  * High
  * Medium
  * Low

| Yes | Specify what should be the severity threshold for the entity, in order to mark it as suspicious. If multiple records are found for the same entity, action will take the highest severity out of all available records.  
Confidence Threshold | Integer | N/A | Yes | Specify what should be the confidence threshold for the entity, in order to mark it as suspicious. Note: Maximum is 100. If multiple records are found for the entity, action will take the average. Active records have priority.  
Ignore False Positive Status | Checkbox | Unchecked | No | If enabled, action will ignore the false positive status and mark the entity as suspicious based on the Severity Threshold and Confidence Threshold. If disabled, action will never label false positive entities as suspicious, regardless, if they pass the Severity Threshold and "Confidence Threshold" conditions or not.  
Add Threat Type To Case | Checkbox | Unchecked | No | If enabled, action will add threat types of the entity from all records as tags to the case. Example: apt  
Only Suspicious Entity Insight | Checkbox | Unchecked | Yes | If enabled, action will create insight only for entities that exceeded the Severity Threshold and Confidence Threshold.  
Create Insight | Checkbox | Unchecked | Yes | If enabled, action will add an insight per processed entity.  
  
#### Run on

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * Email



#### Action results

##### JSON result

The following example shows the JSON result output received when using the **Enrich Entities** action:
    
    
    {
      "results": [
        {
          "Entity": "8f42a5a1f2e1a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6g7h8",
          "EntityResult": [
            {
              "target_industry": [],
              "source": "Threat Intelligence Provider",
              "threatscore": 68,
              "threat_type": "malware",
              "trusted_circle_ids": [
                0
              ],
              "description": "Malware indicator description",
              "workgroups": [],
              "sort": [
                1713616121740,
                10000000001
              ],
              "resource_uri": "/api/v2/intelligence/10000000001/",
              "modified_ts": "2024-04-20T12:28:41.740Z",
              "update_id": 11111111111,
              "source_reported_confidence": 75,
              "type": "hash",
              "uuid": "00000000-0000-0000-0000-000000000000",
              "feed_id": 0,
              "retina_confidence": -1,
              "created_ts": "2024-04-20T12:14:12.356Z",
              "subtype": "SHA256",
              "id": 10000000001,
              "value": "8f42a5a1f2e1a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6g7h8",
              "itype": "mal_hash",
              "org": "ORG_NAME",
              "confidence": 75,
              "expiration_ts": "9999-12-31T00:00:00.000Z",
              "owner_organization_id": 0,
              "meta": {
                "severity": "medium",
                "detail2": "imported by system process"
              },
              "is_anonymous": true,
              "is_public": false,
              "asn": "",
              "status": "active",
              "can_add_public_tags": false,
              "tlp": "amber",
              "created_by": null,
              "rdns": null,
              "is_editable": false,
              "locations": [],
              "source_locations": [],
              "report_link": "https://threatstream.example.com/detail/hash/8f42a5a1f2e1a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6g7h8",
              "is_risky": true
            }
          ]
        },
        {
          "Entity": "e99a18c428cb38d5f260853678922e03",
          "EntityResult": [
            {
              "target_industry": [],
              "source": "Threat Intelligence Provider",
              "threatscore": 68,
              "threat_type": "malware",
              "trusted_circle_ids": [
                0
              ],
              "description": null,
              "workgroups": [],
              "sort": [
                1713615301656,
                10000000002
              ],
              "resource_uri": "/api/v2/intelligence/10000000002/",
              "modified_ts": "2024-04-20T12:15:01.656Z",
              "update_id": 11111111112,
              "source_reported_confidence": 75,
              "type": "md5",
              "uuid": "00000000-0000-0000-0000-000000000001",
              "feed_id": 0,
              "retina_confidence": -1,
              "created_ts": "2024-04-20T12:14:12.351Z",
              "subtype": "MD5",
              "id": 10000000002,
              "value": "e99a18c428cb38d5f260853678922e03",
              "itype": "mal_md5",
              "org": "ORG_NAME",
              "confidence": 75,
              "expiration_ts": "9999-12-31T00:00:00.000Z",
              "owner_organization_id": 0,
              "meta": {
                "severity": "medium",
                "detail2": "imported by system process"
              },
              "is_anonymous": true,
              "is_public": false,
              "asn": "",
              "status": "active",
              "can_add_public_tags": false,
              "tlp": "amber",
              "created_by": null,
              "rdns": null,
              "is_editable": false,
              "locations": [],
              "source_locations": [],
              "report_link": "https://threatstream.example.com/detail/hash/e99a18c428cb38d5f260853678922e03",
              "is_risky": true
            }
          ]
        }
      ],
      "is_risky": true
    }
    

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
id | When available in JSON  
status | When available in JSON  
itype | When available in JSON  
expiration_time | When available in JSON  
ip | When available in JSON  
feed_id | When available in JSON  
confidence | When available in JSON  
uuid | When available in JSON  
retina_confidence | When available in JSON  
trusted_circle_ids | When available in JSON  
source | When available in JSON  
latitude | When available in JSON  
type | When available in JSON  
description | When available in JSON  
tags | When available in JSON  
threat_score | When available in JSON  
source_confidence | When available in JSON  
modification_time | When available in JSON  
org_name | When available in JSON  
asn | When available in JSON  
creation_time | When available in JSON  
tlp | When available in JSON  
country | When available in JSON  
longitude | When available in JSON  
severity | When available in JSON  
subtype | When available in JSON  
report | When available in JSON  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one of the provided entities is enriched (is_success=true):_ "Successfully enriched the following entities using Anomali ThreatStream: \n {0}".format(entity.identifier list) _If failed to enrich specific entities (is_success=true):_ "Action was not able to enrich the following entities using Anomali ThreatStream\n: {0}".format([entity.identifier]) _If failed to enrich all entities (is_success=false):_ "No entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) _If the "Confidence Threshold" parameter is not in the 0-100 range:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
Case Wall Table | **Table Name:** Related Analysis Links: {entity_identifier} **Table Columns:**

  * Name
  * Link

| General  
Case Wall Table | **Keys based on the enrichment table** | Entity  
  
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
Create Insight | Checkbox | Checked | No | If enabled, action will create an insight based on the results.  
Create Case Tag | Checkbox | Unchecked | No | If enabled, action will create case tags based on the results.  
Max Associations To Return | Integer | 5 | No | Specify how many associations to return per type. Default: 5  
Max Statistics To Return | Integer | 3 | No | Specify how many top statistics results regarding IOCs to return. Note: The action will at max process 1000 IOCs related to the association. If you provide `0`, action doesn't try to fetch statistics information.  
  
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
is_success | True or False | is_success:False  
  
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
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one association across entities is found (is_success=true):_ "Successfully retrieved related associations from Anomali ThreatStream" _If no associations are found (is_success=false)_ : "No related associations were found." _Async Message:_ "Waiting for all of the association details to be retrieved" **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Related Association". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** "Related Associations" **Table Columns:**

  * ID
  * Name
  * Type
  * Status

|   
  
### Get Related Entities

Retrieve related entities based on the associations in Anomali ThreatStream.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify what should be the confidence threshold. Maximum is 100.  
Search Threat Bulletins | Checkbox | Checked | No | If enabled, action will search among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, action will search among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, action will search among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, action will search campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, action will search among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, action will search among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, action will search among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, action will search among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, action will search among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, action will search among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, action will search among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, action will search among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, action will search among ttps.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, action will search among vulnerabilities.  
Max Entities To Return | Integer | 50 | No | Specify how many entities to return per entity type.  
  
#### Run on

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * Email (user entity that matches email regex)
  * Threat Actor
  * CVE



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    {
    "{}_hashes.format(subtype)": [""],
    "all_hashes": ["md5hash_1"],
    "domains": [""]
    "urls": []
    "emails": []
    "ips": []
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one hash across entities is found (is_success=true):_ "Successfully retrieved related hashes from Anomali ThreatStream" _If no hashes are found (is_success=false):_ "No related hashes were found." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Related Hashes". Reason: {0}''.format(error.Stacktrace) _If the "Confidence Threshold" parameter is not in 0-100 range:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Ping

Test the connectivity to Anomali ThreatStream.

#### Parameters

N/A

#### Run on

This action doesn't run on entities, nor has mandatory input parameters.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Anomali ThreatStream server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Anomali ThreatStream server! Error is {0}".format(exception.stacktrace) | General  
  
### Remove Tags From Entities

Remove tags from entities in Anomali ThreatStream. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex).

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Tags | CSV | N/A | Yes | Specify a comma-separated list of tags that need to be removed from entities in Anomali ThreatStream.  
  
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
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one tag is removed from one entity (is_success=true):_ "Successfully removed the following tags from the "{entity.identifier}" entity in Anomali ThreatStream:\n{0}".format(tags) _If one tag is not found for one entity (is_success=true):_ "The following tags were already not a part of "{entity.identifier}" entity in Anomali ThreatStream:\n{0}".format(tags) _If all tags are not found for one entity (is_success=true):_ "None of the provided tags were part of "{entity.identifier}" entity in Anomali ThreatStream." _If one entity is not found (is_success=true):_ "The following entities were not found in Anomali ThreatStream\n: {0}".format([entity.identifier]) _If all entities are not found (is_success=false):_ "None of the provided entities were found." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Remove Tags From Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Report As False Positive

Report entities in Anomali ThreatStream as false positive. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex).

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Reason | String | N/A | Yes | Specify the reason why you want to mark entities as false positives.  
Comment | String | N/A | Yes | Specify additional information related to your decision regarding marking the entity as false positive.  
  
#### Run on

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * Email Address (user entity that matches email regex)



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one hash across entities is found (is_success=true):_ "Successfully reported the following entities as false positive in Anomali ThreatStream:\n{0}".format(entity.identifier list) _If fail to mark specific entities (is_success=true):_ "Action was not able to report the following entities as false positive in Anomali ThreatStream\n: {0}".format([entity.identifier]) _If fail to enrich all entities (is_success=false):_ "No entities were reported as false positive." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Report As False Positive". Reason: {0}''.format(error.Stacktrace) | General  
  
### Submit Observables

Submit an observable to Anomali ThreatStream based on IP, URL, Hash, Email entities. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex).

**Note:** This action requires the Org administrator, Create Anomali Community Intel, and Approve Intel permissions.

#### Where to find trusted circle IDs

To find the ID of a trusted circle, locate the trusted circle on Anomali ThreatStream, and click its name. The URL displayed in the address bar shows the ID, such as `https://siemplify.threatstream.com/search?trustedcircles=13.`

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Classification | DDL | Private Possible values:

  * Public
  * Private

| Yes | Specify the classification of the observable.  
Threat Type | DDL | APT Possible Values

  * APT
  * Adware
  * Anomalous
  * Anomyzation
  * Bot
  * Brute
  * C2
  * Compromised
  * Crypto
  * Data Leakage
  * DDOS
  * Dynamic DNS
  * Exfil
  * Exploit
  * Fraud
  * Hacking Tool
  * I2P
  * Informational
  * Malware
  * P2P
  * Parked
  * Phish
  * Scan
  * Sinkhole
  * Social
  * Spam
  * Suppress
  * Suspicious
  * TOR
  * VPS

| Yes | Specify the threat type for the observables.  
Source | String | Siemplify | No | Specify the intelligence source for the observable.  
Expiration Date | Integer | N/A | No | Specify the expiration date in days for the observable. If nothing is specified here, action will create an observable that will never expire.  
Trusted Circle IDs | CSV | N/A | No | Specify the comma-separated list of trusted circle ids. Observables will be shared with those trusted circles.  
TLP | DDL | Select One Possible Values:

  * Select One
  * Red
  * Green
  * Amber
  * White

| No | Specify the TLP for your observables.  
Confidence | Integer | N/A | No | Specify what should be the confidence for the observable. Note: This parameter will only work, if you create observables in your organization and requires Override System Confidence to be enabled.  
Override System Confidence | Checkbox | Unchecked | No | If enabled, created observables will have the confidence specified in the Confidence parameter. Note: You can't share observables in trusted circles and publicly, when this parameter is enabled.  
Anonymous Submission | Checkbox | Unchecked | No | If enabled, action will make an anonymous submission.  
Tags | CSV | N/A | No | Specify a comma-separated list of tags that you want to add to observable.  
  
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
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    approved_jobs = [
        {
            "id":,
            "entity": {entity.identifier}
        }
    ]
        jobs_with_excluded_entities = [
        {
            "id":,
            "entity": {entity.identifier}
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one hash across entities is found(is_success=true):_ "Successfully submitted and approved the following entities in Anomali ThreatStream:\n{0}".format(entity.identifier list) _If fails to enrich some entities (rejected entities) (is_success=true):_ "Action was not able to successfully submit and approve the following entities in Anomali ThreatStream\n: {0}".format([entity.identifier]) _If fails to enrich for all entities (is_success=false):_ "No entities were successfully submitted to Anomali ThreatStream." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Submit Observables". Reason: {0}''.format(error.Stacktrace) _If the 400 status code is reported:_ "Error executing action "Submit Observables". Reason: {0}''.format(message) | General  
| **Link:** `https://siemplify.threatstream.com/import/review/{jobid}` | Entity  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Anomali ThreatStream - Observables Connector

Pull observables from Anomali ThreatStream.

Source names are used in the dynamic list.

To find the ID of a trusted circle, locate the trusted circle on Anomali ThreatStream, and click its name. The URL displayed in the address bar shows the ID, such as `https://siemplify.threatstream.com/search?trustedcircles=13`.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes |  The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
Event Field Name | String | type | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | **""** | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://api.threatstream.com | Yes | API root of the Anomali ThreatStream instance.  
Email Address | String | N/A | Yes | Email address of the Anomali ThreatStream account.  
API Key | Password | N/A | Yes | API Key of the Anomali ThreatStream account.  
Lowest Severity To Fetch | String | High | Yes | Lowest severity that will be used to fetch observables. Possible values:

  * Low
  * Medium
  * High
  * Very-High

  
Lowest Confidence To Fetch | Integer | 50 | Yes | Lowest confidence that will be used to fetch observables. The maximum is `100`.  
Source Feed Filter | CSV | N/A | No | Comma-separated list of feed IDs that should be used to ingest observables, such as `515,4129`.  
Observable Type Filter | CSV | URL, domain, email, hash, ip, ipv6 | No | Comma-separated list of observable types that should be ingested, such as `URL, domain`. Possible values: `URL`, `domain`, `email`, `hash`, `ip`, `ipv6`  
Observable Status Filter | CSV | active | No | Comma-separated list of observable status that should be used to ingest new data, such as `active,inactive` Possible values: `active`, `inactive`, `falsepos`.  
Threat Type Filter | CSV | N/A | No | Comma-separated list of threat types that should be used to ingest observables, such as `adware,anomalous,anonymization,apt`. Possible values: `adware`, `anomalous`, `anonymization`, `apt`, `bot`, `brute`, `c2`, `compromised`, `crypto`, `data_leakage`, `ddos`, `dyn_dns`, `exfil`, `exploit`, `fraud`, `hack_tool`, `i2p`, `informational`, `malware`, `p2p`, `parked`, `phish`, `scan`, `sinkhole`, `spam`, `suppress`, `suspicious`, `tor`, `vps`  
Trusted Circle Filter | CSV | N/A | No | Comma-separated list of trusted circle ids that should be used to ingest observables, such as `146,147`.  
Tag Name Filter | CSV | N/A | No | Comma-separated list of tag names associated with observables that should be sed with ingestion, such as `Microsoft Credentials, Phishing`.  
Source Feed Grouping | Checkbox | Unchecked | No | If enabled, the connector groups observables from the same source under the same Google SecOps alert.  
Fetch Max Days Backwards | Integer | 1 | No | The number of days prior to today to retrieve the observables. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Observables Per Alert | Integer | 100 | No | The number of observables to include in a Google SecOps alert. The maximum allowed is 200.  
`Use whitelist as a blacklist` | Checkbox | Unchecked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If selected, the integration validates the SSL certificate when connecting to the Anomali ThreatStream server.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
