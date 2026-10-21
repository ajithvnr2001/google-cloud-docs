---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify-threatfuse/
title: Integrate Siemplify ThreatFuse with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:20.787439+00:00
---

# Integrate Siemplify ThreatFuse with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify-threatfuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Siemplify ThreatFuse with Google SecOps

This document explains how to integrate Siemplify ThreatFuse with Google Security Operations.

## Use cases

The **Siemplify ThreatFuse** integration uses Google SecOps capabilities to support the following use cases:

  * **Enrich network and user entities** : Automatically retrieve threat scores, confidence levels, and metadata for IPs, URLs, hashes, and emails to identify malicious activity.

  * **Discover related threat data** : Uncover associated hashes, domains, and IP addresses to map out the infrastructure used by threat actors.

  * **Analyze campaign associations** : Retrieve details on linked campaigns, malware families, and TTPs to understand the broader context of an incident.

  * **Manage intelligence feeds** : Submit new observables to ThreatFuse or report false positives directly from the platform to refine your organization's threat data.




## Before you begin

Before you configure the integration in Google SecOps, verify the following requirements in your Siemplify ThreatFuse (powered by Anomali ThreatStream) environment:

  * **API credentials** : You must have a valid API key and the email address associated with your Anomali or ThreatFuse account.

  * **Credential retrieval** : To obtain your API key, sign in to the ThreatFuse portal, go to the **User Profile** section, and locate the **API Information** tab. For details, see [Anomali ThreatStream settings](https://siemplify.threatstream.com/settings?action=profile).

  * **Instance details** : Identify your specific web root and API root. Typically, for cloud instances, the API root is `https://api.threatstream.com`.




## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Web Root | String | https://siemplify.threatstream.com | Yes | Web Root of the Siemplify ThreatFuse instance. This parameter is used for creating report links across integration items.  
API Root | String | https://api.threatstream.com | Yes | API Root of the Siemplify ThreatFuse instance.  
Email Address | String | N/A | Yes | Email address of the Siemplify ThreatFuse account.  
API Key | Password | N/A | Yes | API key of the Siemplify ThreatFuse account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Siemplify ThreatFuse server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test connectivity to the Siemplify ThreatFuse with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

The action idoesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful:_ "Successfully connected to the Siemplify ThreatFuse server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:******  
****_If not successful:_ "Failed to connect to the Siemplify ThreatFuse server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Retrieve information about IPs, URLs, hashes, email addresses from Siemplify ThreatFuse. If multiple records are found for the same entity, the action will enrich using the latest record.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Severity Threshold | DDL | MediumPossible value:

  * Very High
  * High
  * Medium
  * Low

| Yes | Specify the severity threshold for the entity, in order to mark it as suspicious. If multiple records are found for the same entity, the action takes the highest severity out of all available records.  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold for the entity, in order to mark it as suspicious.Maximum is 100. If multiple records are found for the entity, the action takes the average.Active records have priority.  
Ignore False Positive Status | Checkbox | Unchecked | No | If enabled, the action ignores the false positive status and mark the entity as suspicious based on the "Severity Threshold" and "Confidence Threshold" parameters.If disabled, the action never labels false positive entities as suspicious, regardless, if they pass the "Severity Threshold" and "Confidence Threshold" conditions or not.   
Add Threat Type To Case | Checkbox | Unchecked | No | If enabled, the action adds threat types of the entity from all records as tags to the case. Example: apt  
Only Suspicious Entity Insight | Checkbox | Unchecked | Yes | If enabled, the action creates insight only for entities that exceeded the "Severity Threshold" and "Confidence Threshold" parameters.  
Create Insight | Checkbox | Unchecked | Yes | If enabled, the action adds an insight per processed entity.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "objects": [
            {
                "status": "inactive",
                "itype": "mal_md5",
                "expiration_ts": "2019-02-25T08:58:58.000Z",
                "ip": null,
                "is_editable": false,
                "feed_id": 2197,
                "update_id": 3328068779,
                "longitude": null,
                "org": "",
                "threat_type": "malware",
                "workgroups": [],
                "rdns": null,
                "confidence": 60,
                "uuid": "31d9ed97-9811-4b4b-9e2d-4b3f822eb37f",
                "subtype": "MD5",
                "trusted_circle_ids": [
                    146,
                    254
                ],
                "id": 51744433673,
                "source": "targetedthreats - OSINT",
                "owner_organization_id": 2,
                "import_session_id": null,
                "latitude": null,
                "type": "md5",
                "sort": [
                    1551097291170
                ],
                "description": null,
                "tags": [
                    {
                        "id": "fvj",
                        "name": "Family=Code4HK"
                    },
                    {
                        "id": "zwz",
                        "name": "Report=https://malware.lu/articles/2014/09/29/analysis-of-code4hk.html"
                    }
                ],
                "threatscore": 54,
                "source_reported_confidence": 60,
                "modified_ts": "2019-02-25T12:21:31.170Z",
                "is_public": false,
                "asn": "",
                "created_ts": "2018-11-27T09:00:33.468Z",
                "tlp": null,
                "is_anonymous": false,
                "country": null,
                "can_add_public_tags": false,
                "value": "15e5143e1c843b4836d7b6d5424fb4a5",
                "retina_confidence": -1,
                "meta": {
                    "detail2": "bifocals_deactivated_on_2019-02-25_09:30:00.127233",
                    "severity": "high"
                },
                "resource_uri": "/api/v2/intelligence/51744433673/"
          "report_link": "https://siemplify.threatstream.com/detail/url/http:%2F%2Fsweetpineapple.co.za%2Fwp-admin%2Fuser%2Finternetbanking.suncorpbank.htm"
            },
            {
                "status": "active",
                "itype": "apt_md5",
                "expiration_ts": "9999-12-31T00:00:00+00:00",
                "ip": null,
                "is_editable": false,
                "feed_id": 191,
                "update_id": 5406560,
                "value": "15e5143e1c843b4836d7b6d5424fb4a5",
                "is_public": true,
                "threat_type": "apt",
                "workgroups": [],
                "rdns": null,
                "confidence": 90,
                "uuid": null,
                "retina_confidence": -1,
                "trusted_circle_ids": null,
                "id": 5406560,
                "source": "SLC Alert Malware Domains",
                "owner_organization_id": 736,
                "import_session_id": null,
                "latitude": null,
                "type": "md5",
                "sort": [
                    1421928716491
                ],
                "description": null,
                "tags": [
                    {
                        "name": "HITRUST"
                    },
                    {
                        "name": "Public-Threats"
                    }
                ],
                "threatscore": 77,
                "source_reported_confidence": 60,
                "modified_ts": "2015-01-22T12:11:56.491Z",
                "org": "",
                "asn": "",
                "created_ts": "2015-01-22T12:11:56.491Z",
                "tlp": null,
                "is_anonymous": null,
                "country": null,
                "can_add_public_tags": true,
                "longitude": null,
                "subtype": "MD5",
                "meta": {
                    "severity": "high",
                    "detail": "Public Threats,HITRUST"
                },
                "resource_uri": "/api/v2/intelligence/5406560/"
            },
            {
                "status": "active",
                "itype": "apt_md5",
                "expiration_ts": "9999-12-31T00:00:00+00:00",
                "ip": null,
                "is_editable": false,
                "feed_id": 0,
                "update_id": 59177,
                "value": "15e5143e1c843b4836d7b6d5424fb4a5",
                "is_public": true,
                "threat_type": "apt",
                "workgroups": [],
                "rdns": null,
                "confidence": 100,
                "uuid": null,
                "retina_confidence": -1,
                "trusted_circle_ids": null,
                "id": 59177,
                "source": "Analyst",
                "owner_organization_id": 2,
                "import_session_id": 2325,
                "latitude": null,
                "type": "md5",
                "sort": [
                    1412172414589
                ],
                "description": null,
                "tags": [
                    {
                        "name": "apt_md5"
                    },
                    {
                        "name": "CN-APT"
                    },
                    {
                        "name": "IOS-Malware"
                    },
                    {
                        "name": "LadyBoyle"
                    }
                ],
                "threatscore": 85,
                "source_reported_confidence": 0,
                "modified_ts": "2014-10-01T14:06:54.589Z",
                "org": "",
                "asn": "",
                "created_ts": "2014-10-01T14:06:40.858Z",
                "tlp": null,
                "is_anonymous": null,
                "country": null,
                "can_add_public_tags": false,
                "longitude": null,
                "subtype": "MD5",
                "meta": {
                    "detail2": "imported by user 1",
                    "severity": "very-high",
                    "detail": "LadyBoyle, IOS Malware, CN APT"
                },
                "resource_uri": "/api/v2/intelligence/59177/"
            }
        ],
        "is_risky": "true"
        "meta": {
            "total_count": 3,
            "offset": 0,
            "limit": 1000,
            "took": 27,
            "next": null
        }
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
TFuse_id | When available in JSON  
TFuse_status | When available in JSON  
TFuse_itype | When available in JSON  
TFuse_expiration_time | When available in JSON  
TFuse_ip | When available in JSON  
TFuse_feed_id | When available in JSON  
TFuse_confidence | When available in JSON  
TFuse_uuid | When available in JSON  
TFuse_retina_confidence | When available in JSON  
TFuse_trusted_circle_ids | When available in JSON  
TFuse_source | When available in JSON  
TFuse_latitude | When available in JSON  
TFuse_type | When available in JSON  
TFuse_description | When available in JSON  
TFuse_tags | When available in JSON  
TFuse_threat_score | When available in JSON  
TFuse_source_confidence | When available in JSON  
TFuse_modification_time | When available in JSON  
TFuse_org_name | When available in JSON  
TFuse_asn | When available in JSON  
TFuse_creation_time | When available in JSON  
TFuse_tlp | When available in JSON  
TFuse_country | When available in JSON  
TFuse_longitude | When available in JSON  
TFuse_severity | When available in JSON  
TFuse_subtype | When available in JSON  
TFuse_report | When available in JSON  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one of the provided entities is enriched (is_success=true):_ "Successfully enriched the following entities using Siemplify ThreatFuse: \n {0}".format(entity.identifier list)  
****_If fail to enrich specific entities (is_success=true):_ "Action was not able to enrich the following entities using Siemplify ThreatFuse\n: {0}".format([entity.identifier])  
****_If fail to enrich for all entities (is_success=false):_ "No entities were enriched."  
**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)  
_If the "Confidence Threshold" parameter is not in the 0-100 range:_ ****"'Confidence Threshold' value should be in range from 0 to 100." | General  
CSV | **Table Name:** Related Analysis Links: {entity_identifier}**Table Columns:**

  * Name: mapped as key in the second response (example Virustotal)
  * Link: ****mapped as value to the key

| General  
CSV | Keys based on the enrichment table.The No Enrichment Prefix, parameter is capitalized. | General  
  
### Get Related Hashes

Retrieve entity related hashes based on the associations in Siemplify ThreatFuse.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold.Maximum: 100  
Search Threat Bulletins | Checkbox | Checked | No | If enabled, the action searches among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, the action searches among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, the action searches among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, the action searches campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, the action searches among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, the action searches among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, the action searches among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, the action searches among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, the action searches among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, the action searches among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, the action searches among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, the action searches among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, the action searches among TTPs.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, the action searches among vulnerabilities.  
Max Hashes To Return | Integer | 50 | No | Specify the number of hashes to return.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes
  * Threat Actor
  * CVE



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "{}_hashes".format(subtype): ["md5hash_1"],
    "all_hashes": ["md5hash_1"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (is_success=true):_ "Successfully retrieved related hashes from Siemplify ThreatFuse"  
****_If no hashes are found (is_success=false):_ "No related hashes were found."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ ****"Error executing action "Get Related Hashes". Reason: {0}''.format(error.Stacktrace)****_If the "Confidence Threshold" parameter is not in the 0-100 range:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Get Related URLs

Retrieve entity related URLs based on the associations in Siemplify ThreatFuse.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold. Maximum: 100  
Search Threat Bulletins | Checkbox | Checked | No | If enabled, the action searches among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, the action searches among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, the action searches among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, the action searches campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, the action searches among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, the action searches among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, the action searches among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, the action searches among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, the action searches among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, the action searches among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, the action searches among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, the action searches among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, the action searches among TTPs.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, the action searches among vulnerabilities.  
Max URLs To Return | Integer | 50 | No | Specify the number of URLs to return.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes
  * Threat Actor
  * CVE



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "urls": ["https://www.google.com/url?q=http:/wzFgw"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one URL across entities is found (is_success=true):_ "Successfully retrieved related urls from Siemplify ThreatFuse."  
****_If no hashes are found (is_success=false):_ "No related urls were found."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ ****"Error executing action "Get Related URLs". Reason: {0}''.format(error.Stacktrace)****_If the "Confidence Threshold" parameter is not in the 0-100 range:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Get Related Domains

Retrieve entity related domains based on the associations in Siemplify ThreatFuse.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold. Maximum: 100  
Search Threat Bulletins | Checkbox | Checked | No | If enabled, the action searches among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, the action searches among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, the action searches among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, the action searches campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, the action searches among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, the action searches among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, the action searches among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, the action searches among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, the action searches among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, the action searches among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, the action searches among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, the action searches among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, the action searches among TTPs.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, the action searches among vulnerabilities.  
Max Domains To Return | Integer | 50 | No | Specify the number of domains to return.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes
  * Threat Actor
  * CVE



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "domains": ["www.google.com"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (issuccess=true):_ "Successfully retrieved related domains from Siemplify ThreatFuse."  
****_If no hashes are found (issuccess=false):_ "No related domains were found."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Related Domains". Reason: {0}''.format(error.Stacktrace)****_If the "Confidence Threshold" parameter is not in the 0-100 range:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Get Related Email Addresses

Retrieve entity related email addresses based on the associations in Siemplify ThreatFuse.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold.Maximum: 100   
Search Threat Bulletins | Checkbox | Checked | No | If enabled, the action searches among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, the action searches among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, the action searches among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, the action searches campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, the action searches among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, the action searches among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, the action searches among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, the action searches among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, the action searches among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, the action searches among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, the action searches among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, the action searches among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, the action searches among TTPs.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, the action searches among vulnerabilities.  
Max Domains To Return | Integer | 50 | No | Specify the number of domains to return.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes
  * Threat Actor
  * CVE



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "urls": ["https://www.google.com/url?q=http:/wzFgw"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (issuccess=true):_ "Successfully retrieved related email addresses from Siemplify ThreatFuse."  
****_If no hashes are found (issuccess=false):_ "No related email addresses were found."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Related Email Addresses". Reason: {0}''.format(error.Stacktrace)****_If the "Confidence Threshold" parameter is not in range 0-100:_ "'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Get Related IPs

Retrieve entity related IP addresses based on the associations in Siemplify ThreatFuse.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Confidence Threshold | Integer | N/A | Yes | Specify the confidence threshold. Maximum: 100   
Search Threat Bulletins | Checkbox | Checked | No | If enabled, the action searches among threat bulletins.  
Search Actors | Checkbox | Checked | No | If enabled, the action searches among actors.  
Search Attack Patterns | Checkbox | Checked | No | If enabled, the action searches among attack patterns.  
Search Campaigns | Checkbox | Checked | No | If enabled, the action searches campaigns.  
Search Courses Of Action | Checkbox | Checked | No | If enabled, the action search among courses of action.  
Search Identities | Checkbox | Checked | No | If enabled, the action searches among identities.  
Search Incidents | Checkbox | Checked | No | If enabled, the action searches among incidents.  
Search Infrastructures | Checkbox | Checked | No | If enabled, the action searches among infrastructures.  
Search Intrusion Sets | Checkbox | Checked | No | If enabled, the action searches among intrusion sets.  
Search Malware | Checkbox | Checked | No | If enabled, the action searches among malware.  
Search Signatures | Checkbox | Checked | No | If enabled, the action searches among signatures.  
Search Tools | Checkbox | Checked | No | If enabled, the action searches among tools.  
Search TTPs | Checkbox | Checked | No | If enabled, the action searches among TTPs.  
Search Vulnerabilities | Checkbox | Checked | No | If enabled, the action searches among vulnerabilities.  
Max Domains To Return | Integer | 50 | No | Specify the number of domains to return.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes
  * Threat Actor
  * CVE



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
    "urls": ["https://www.google.com/url?q=http:/wzFgw"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (is_success=true):_ "Successfully retrieved related IPs from Siemplify ThreatFuse."  
****_If no hashes are found (is_success=false):_ "No related IPs were found."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ ****"Error executing action "Get Related IPs". Reason: {0}''.format(error.Stacktrace)****_If the "Confidence Threshold" parameter is not in the 0-100 range:_ ****"'Confidence Threshold' value should be in range from 0 to 100." | General  
  
### Get Related Associations

Retrieve entity related associations from Siemplify ThreatFuse.

**Note:** Make sure that the email address doesn't contain spaces.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Return Campaigns | Checkbox | Checked | No | If enabled, the action fetches related campaigns and details about them.  
Return Threat Bulletins | Checkbox | Unchecked | No | If enabled, the action fetches related threat bulletins and details about them.  
Return Actors | Checkbox | Unchecked | No | If enabled, the action fetches related actors and details about them.  
Return Attack Patterns | Checkbox | Unchecked | No | If enabled, the action fetches related attack patterns and details about them.  
Return Courses Of Action | Checkbox | Unchecked | No | If enabled, the action fetches related courses of action and details about them.  
Return Identities | Checkbox | Unchecked | No | If enabled, the action fetches related identities and details about them.  
Return Incidents | Checkbox | Unchecked | No | If enabled, the action fetches related incidents and details about them.  
Return Infrastructure | Checkbox | Unchecked | No | If enabled, the action fetches related infrastructure and details about them.  
Return Intrusion Sets | Checkbox | Unchecked | No | If enabled, the action fetches related intrusion sets and details about them.  
Return Malware | Checkbox | Unchecked | No | If enabled, the action fetches related malware and details about them.  
Return Signatures | Checkbox | Unchecked | No | If enabled, the action fetches related signatures and details about them.  
Return Tools | Checkbox | Unchecked | No | If enabled, the action fetches related tools and details about them.  
Return TTPs | Checkbox | Unchecked | No | If enabled, the action fetches related TTPs and details about them.  
Return Vulnerabilities | Checkbox | Checked | No | If enabled, the action fetches related vulnerabilities and details about them.  
Create Campaign Entity | Checkbox | Unchecked | No | If enabled, the action creates an entity out of available "Campaign" associations.  
Create Actors Entity | Checkbox | Unchecked | No | If enabled, the action creates an entity out of available "Actor" associations.  
Create Signature Entity | Checkbox | Unchecked | No | If enabled, the action creates an entity out of available "Signature" associations.  
Create Vulnerability Entity | Checkbox | Unchecked | No | If enabled, the action creates an entity out of available "Vulnerability" associations.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight based on the results.  
Create Case Tag | Checkbox | Checked | No | If enabled, the action creates case tags based on the results.  
Max Associations To Return | Integer | N/A | No | Specify the number of associations to return per type.  
Max Statistics To Return | Integer | 3 | No | Specify the number of top statistics results regarding IOCs to return. **Note:** The action processes the maximum of 1000 IOCs related to the association. If you provide "0", the action does not try to fetch statistics information.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes



#### Action Results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "campaign": [
            {
                "name": "Coronavirus",
                "id": 1
            },
            {
                "name": "Bad campaign",
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
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one association across entities is found (is_success=true):_ "Successfully retrieved related associations from Siemplify ThreatFuse"****_If no associations are found (is_success=false):_ ****"No related associations were found."  
****_Async Message:_ Waiting for all of the association details to be retrieved"  
**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Related Association". Reason: {0}''.format(error.Stacktrace) | General  
CSV | **Name:** "Related Associations"**Columns:**

  * ID
  * Name
  * Type (association name)
  * Status (mapped as status/display_name)

| General  
  
### Submit Observables

Submit an observable to Siemplify ThreatFuse based on the IP, URL, Hash, Email entities.

**Note:** This action requires "Org admin", "Create Anomali Community Intel" and "Approve Intel" permissions.

#### Where to find trusted circle IDs

To find the ID of a trusted circle, locate the trusted circle on Siemplify ThreatFuse, and click on its name. The URL displayed in the address bar shows the ID.

For example: https://siemplify.threatstream.com/search?trustedcircles=13.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Classification | DDL | PrivatePossible Values:

  * Public
  * Private

| Yes | Specify the classification of the observable.  
Threat Type | DDL | APTPossible Values

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
  * P2
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
Expiration Date | Integer | N/A | No | Specify the expiration date in days for the observable.If nothing is specified here, the action creates an observable that never expires.  
Trusted Circle IDs | CSV | N/A | No | Specify a comma-separated list of trusted circle IDs. Observables are shared with those trusted circles.   
TLP | DDL | Select OnePossible Values:

  * Select One
  * Red
  * Green
  * Amber
  * White

| No | Specify the TLP for your observables.  
Confidence | Integer | N/A | No | Specify what should be the confidence for the observable. **Note:** This parameter only works, if you create observables in your organization and the "Override System Confidence" parameter is enabled.  
Override System Confidence | Checkbox | Unchecked | No | If enabled, created observables has the confidence specified in the "Confidence" parameter. **Note:** You can't share observables in trusted circles and publicly, when this parameter is enabled.  
Anonymous Submission | Checkbox | Unchecked | No | If enabled, the action makes an anonymous submission.  
Tags | CSV | N/A | No | Specify a comma-separated list of tags that you want to add to observable.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    approved_jobs = [
        {
            "id": 123123,
            "entity": {entity.identifier}
        }
    ]
        jobs_with_excluded_entities = [
        {
            "id": 123123,
            "entity": {entity.identifier}
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (is_success=true):_ ****"Successfully submitted and approved the following entities in Siemplify ThreatFuse:\n{0}".format(entity.identifier list)  
****_If fail for some entities (rejected entities) (is_success=true):_ "Action was not able to successfully submit and approve the following entities in Siemplify ThreatFuse\n: {0}".format([entity.identifier])  
****_If fail to enrich for all entities (is_success=false):_ ****"No entities were successfully submitted to Siemplify ThreatFuse."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ ****"Error executing action "Submit Observable". Reason: {0}''.format(error.Stacktrace)  
****_If the 400 status code is reported:_ "Error executing action "Submit Observable". Reason: {0}''.format(message) | General  
  
### Report As False Positive

Report entities in Siemplify ThreatFuse as false positive.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Reason | String | N/A | Yes | Specify the reason why you want to mark entities as false positive.  
Comment | String | N/A | Yes | Specify additional information related to your decision regarding marking the entity as false positive.  
  
#### Run On

This action runs on the following entities:

  * Hash
  * IP Address
  * URL
  * User Name with Email regexes



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one hash across entities is found (is_success=true):_ "Successfully reported the following entities as false positive in Siemplify ThreatFuse:\n{0}".format(entity.identifier list)  
****_If fail to mark specific entities (is_success=true):_ "Action was not able to report the following entities as false positive in Siemplify ThreatFuse\n: {0}".format([entity.identifier])  
****_If fail to enrich for all entities (issuccess=false):_ "No entities were reported as false positive."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Report As False Positive". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Siemplify ThreatFuse - Observables Connector

Pull observables from Siemplify ThreatFuse.

**Note:** Source names are used in the whitelist.

#### Recommendations

When configuring connector, it is recommended to use a separate environment, so that the analysts won't be flooded with all of the speculative alerts.

#### Where to find trusted circle IDs

To find the ID of a trusted circle, locate the trusted circle on Siemplify ThreatFuse, and click its name. The URL displayed in the address bar shows the ID.

For example: `https://siemplify.threatstream.com/search?trustedcircles=13`.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://api.threat  
stream.com | Yes | API root of the Siemplify ThreatFuse instance.  
Email Address | String | N/A | Yes | Email address of the Siemplify ThreatFuse account.  
API Key | Password | N/A | Yes | API Key of the Siemplify ThreatFuse account.  
Lowest Severity To Fetch | String | High | Yes | Lowest severity that will be used to fetch observables. Possible values:  
Low Medium High Very-High  
Lowest Confidence To Fetch | Integer | 50 | Yes | Lowest confidence that will be used to fetch observables. Maximum is 100.  
  
Source Feed Filter | CSV | N/A | No | Comma-separated list of feed ids that should be used to ingest observables. Example: 515,4129  
Observable Type Filter | CSV | url, domain, email, hash, ip, ipv6 | No | Comma-separated list of observable types that should be ingested. Example: url, domain Possible values: url, domain, email, hash, ip, ipv6  
Observable Status Filter | CSV | active | No | Comma-separated list of observable status that should be used to ingest new data. Example: active,inactive Possible values: active,inactive,falsepos  
Threat Type Filter | CSV | N/A | No | Comma-separated list of threat types that should be used to ingest observables. Example: аdware,anomalous,anonymization,aptPossible values:   
аdware,anomalous,anonymization,  
apt,bot,brute,c2,compromised,  
crypto,data_leakage,ddos,dyn_dns,exfil,  
exploit,fraud,hack_tool,i2p,informational,  
malware,p2p,parked,phish,scan,sinkhole,spam,  
suppress,suspicious,tor,vps  
Trusted Circle Filter | CSV | N/A | No | Comma-separated list of trusted circle ids that should be used to ingest observables.Example: 146,147  
Tag Name Filter | CSV | N/A | No | Comma-separated list of tag names associated with observables that should be used with ingestion. Example: Microsoft Credentials, Phishing.  
Source Feed Grouping | Checkbox | Unchecked | No | If enabled, the connector will group observables from the same source under the same Siemplify Alert.  
Fetch Max Days Backwards | Integer | 1 | No | Amount of days from where to fetch observables.  
Max Observables Per Alert | Integer | 100 | No | How many observables should be a part of one Siemplify Alert. Maximum is 200.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, dynamic list will be used as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Siemplify Threatfuse server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
