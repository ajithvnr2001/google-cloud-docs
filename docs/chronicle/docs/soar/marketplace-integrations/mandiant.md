---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant/
title: Integrate Mandiant with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:48.502949+00:00
---

# Integrate Mandiant with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Mandiant with Google SecOps

This document explains how to integrate Mandiant with Google Security Operations.

**Important:** This integration is no longer maintained. Use [Mandiant Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-threat-intelligence), as it has superseded this version and receives all current updates.

## Use cases

The **Mandiant** integration uses Google SecOps capabilities to support the following use cases:

  * **Enrich hostnames, IP addresses, and URLs** : Automatically retrieve threat intelligence for network-based indicators to identify malicious activity.

  * **Analyze file hashes** : Evaluate MD5, SHA-1, and SHA-256 hashes against Mandiant's repository to determine if files are known threats.

  * **Identify related indicators** : Discover additional IOCs associated with specific threat actors or vulnerabilities to map out a broader attack surface.

  * **Retrieve malware details** : Get targeted information on malware families, including their roles and common targets, to aid in incident response.




## Before you begin

To authenticate the connection between Google SecOps and Mandiant, you must provide a valid Client ID and Client Secret. 

You can generate and manage these credentials within your Mandiant Advantage console.

For detailed instructions on generating these credentials, see the [Mandiant API guide](https://advantage.mandiant.com/docs/api-guide).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
UI Root | String | https://advantage.mandiant.com | Yes | UI root of the Mandiant instance.  
API Root | String | https://api.intelligence.mandiant.com | Yes | API root of the Mandiant instance.  
Client ID | Password | N/A | No | Client ID of the Mandiant account.  
CA Certificate File | String | N/A | No | Client Secret of the Mandiant account.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Mandiant server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate Client ID and Client Secret

Go to **Settings - > API Access and Keys** and click **Get Key ID and Secret**.

## Use Cases

Enrich entities.

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test connectivity to Mandiant with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Mandiant server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Mandiant server! Error is {0}".format(exception.stacktrace)" | General  
  
### Enrich Entities

Enrich entities using information from Mandiant. Supported entities: Hostname, IP Address, URL, File Hash, Threat Actor, Vulnerability.

**Note:** Only the MD5, SHA-1 and SHA-256 are supported.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Severity Score Threshold | Integer | 50 | Yes | Specify the lowest severity score that is used to mark the entity as suspicious. **Note:** Only indicators (hostname, IP address, file hash, url) can be marked as suspicious.Maximum: 100  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
Only Suspicious Entity Insight | Checkbox | Unchecked | No | If enabled, the action only creates an insight for suspicious entities.**Note:** The "Create Insight" parameter should be enabled. Insights for the "Threat Actor" and "Vulnerability" entities are also created even though they are not marked as suspicious.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * URL
  * File Hash
  * Threat Actor
  * Vulnerability



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result

##### JSON Result for Indicators
    
    
    {
        "Entity": "173.254.xx.xx",
        "EntityResult": {
          "first_seen": "2022-03-22T21:46:43.000Z",
          "last_seen": "2022-05-22T00:58:48.000Z",
          "sources": [
            {
              "first_seen": "2022-03-22T21:46:46.000+0000",
              "last_seen": "2022-03-24T19:12:57.000+0000",
              "osint": false,
              "category": [],
              "source_name": "Mandiant"
            }
          ],
          "mscore": 100,
          "attributed_associations": [
            {
              "id": "malware--f1151a22-9d9c-589d-90ad-xxxxx",
              "name": "EMOTET",
              "type": "malware"
            }
          ],
          "misp": {
            "smtp-receiving-ips": false,
            "covid": false,
            "eicar.com": false,
            "majestic_million": false,
            "sinkholes": false,
            "alexa": false,
            "cisco_top1000": false,
            "microsoft": false,
            "microsoft-office365": false,
            "crl-hostname": false,
            "googlebot": false,
            "microsoft-azure-germany": false,
            "microsoft-attack-simulator": false,
            "microsoft-azure": false,
            "rfc5735": false,
            "tranco10k": false,
            "dax30": false,
            "public-dns-v4": false,
            "dynamic-dns": false,
            "public-dns-v6": false,
            "covid-19-cyber-threat-coalition-whitelist": false,
            "common-ioc-false-positive": false,
            "cisco_1M": false,
            "google-gmail-sending-ips": false,
            "microsoft-azure-china": false,
            "stackpath": false,
            "google": false,
            "cloudflare": false,
            "moz-top500": false,
            "tranco": false,
            "tlds": false,
            "university_domains": false,
            "smtp-sending-ips": false,
            "cisco_top20k": false,
            "empty-hashes": false,
            "nioc-filehash": false,
            "amazon-aws": false,
            "url-shortener": false,
            "microsoft-office365-ip": false,
            "microsoft-win10-connection-endpoints": false,
            "microsoft-azure-us-gov": false,
            "majestic_million_1M": false,
            "mozilla-CA": false,
            "whats-my-ip": false,
            "microsoft-office365-cn": false,
            "vpn-ipv6": false,
            "rfc3849": false,
            "rfc6761": false,
            "security-provider-blogpost": false,
            "cisco_top5k": false,
            "apple": false,
            "public-dns-hostname": false,
            "mozilla-IntermediateCA": false,
            "rfc1918": false,
            "ti-falsepositives": false,
            "akamai": false,
            "bank-website": false,
            "alexa_1M": false,
            "automated-malware-analysis": false,
            "rfc6598": false,
            "google-gcp": false,
            "ovh-cluster": false,
            "multicast": false,
            "phone_numbers": false,
            "fastly": false,
            "cisco_top10k": false,
            "second-level-tlds": false,
            "wikimedia": false,
            "disposable-email": false,
            "common-contact-emails": false,
            "vpn-ipv4": true,
            "ipv6-linklocal": false,
            "covid-19-krassi-whitelist": false,
            "crl-ip": false
          },
          "id": "ipv4--da5b1f26-cf25-5a61-9c93-xxxxx",
          "type": "ipv4",
          "value": "173.254.xx.xx",
          "is_publishable": true,
          "last_updated": "2022-05-22T01:04:46.098Z",
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ipv4--da5b1f26-xxxx-5a61-9c93-6dxxxxxxxxxx"
        }
      }
    

##### JSON Result for Threat Actor
    
    
    {
        "Entity": "APxxxxx",
        "EntityResult": {
          "motivations": [
            {
              "id": "motivation--1b8ca82a-7cff-5622-bedd-xxxx",
              "name": "Espionage",
              "attribution_scope": "confirmed"
            }
          ],
          "aliases": [
            {
              "name": "Comment Crew (Internet)",
              "attribution_scope": "confirmed"
            }
          ],
          "industries": [
            {
              "id": "identity--cc593632-0c42-500c-8d0b-xxxxx",
              "name": "Aerospace & Defense",
              "attribution_scope": "confirmed"
            },
            {
              "id": "identity--8768c9d0-830d-5c94-88d1-xxxxxxx",
              "name": "Transportation",
              "attribution_scope": "confirmed"
            }
          ],
          "observed": [
            {
              "earliest": "2003-06-20T12:00:00.000Z",
              "recent": "2015-10-20T00:00:00.000Z",
              "attribution_scope": "confirmed"
            }
          ],
          "malware": [
            {
              "id": "malware--09673ebc-9fbf-5ab0-9130-xxxxx",
              "name": "AGEDMOAT",
              "attribution_scope": "confirmed"
            },
            {
              "id": "malware--a2de25d8-beae-5e86-b10e-xxxxxx",
              "name": "ZERODUE",
              "attribution_scope": "confirmed"
            }
          ],
          "tools": [
            {
              "id": "malware--57e5ea29-1c08-5f80-b28e-xxxxx",
              "name": "ANGRYIP",
              "attribution_scope": "confirmed"
            }
          ],
          "suspected_attribution": [],
          "locations": {
            "source": [
              {
                "region": {
                  "id": "location--02178345-7a8a-546a-b82f-xxxxx",
                  "name": "Asia",
                  "attribution_scope": "confirmed"
                },
                "sub_region": {
                  "id": "location--c80cc2c3-c5b6-5769-b228-xxxxx",
                  "name": "East Asia",
                  "attribution_scope": "confirmed"
                },
                "country": {
                  "id": "location--26e2c717-7772-5ad5-8f0c-xxxxx",
                  "name": "China",
                  "iso2": "CN",
                  "attribution_scope": "confirmed"
                }
              }
            ],
            "target": [
              {
                "id": "location--a509dfc8-789b-595b-a201-xxxxx",
                "name": "Belgium",
                "iso2": "be",
                "region": "Europe",
                "sub-region": "West Europe",
                "attribution_scope": "confirmed"
              }
            ],
            "target_sub_region": [
              {
                "id": "location--7b33370b-da4b-5c48-9741-xxxxx",
                "name": "East Asia",
                "key": "eastasia",
                "region": "Asia",
                "attribution_scope": "confirmed"
              }
            ],
            "target_region": [
              {
                "id": "location--9488166d-6469-5e54-ba5f-xxxxx",
                "name": "Africa",
                "key": "africa",
                "attribution_scope": "confirmed"
              }
            ]
          },
          "cve": [
            {
              "id": "vulnerability--8cb90843-f69a-5aa6-95dc-xxxxx",
              "cve_id": "CVE-2009-xxxx",
              "attribution_scope": "confirmed"
            }
          ],
          "associated_uncs": [],
          "id": "threat-actor--0ac5c1db-8ad6-54b8-b4b9-xxxxx",
          "name": "APxxxx",
          "description": "A description of the threat actor",
          "type": "threat-actor",
          "last_updated": "2022-05-29T05:30:48.000Z",
          "last_activity_time": "2015-10-20T00:00:00.000Z",
          "audience": [
            {
              "name": "intel_fusion",
              "license": "INTEL_RBI_FUS"
            }
          ],
          "is_publishable": true,
          "counts": {
            "reports": 171,
            "malware": 92,
            "cve": 1,
            "associated_uncs": 0,
            "aliases": 4,
            "industries": 16,
            "attack_patterns": 111
          },
          "intel_free": true,
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ipv4--da5b1f26-xxxx-5a61-9c93-6dxxxxxxxxxx"
        }
      }
    

##### JSON Result for Vulnerability
    
    
      {
        "Entity": "CVE-2022-xxxx",
        "EntityResult": {
          "exploits": [],
          "vulnerable_products": "<p>The following vendors/products have been reported as vulnerable:</p>\\n<ul>\\n<li>Company A:&nbsp;NetWeaver Application Server for ABAP&nbsp;7.01, 7.02, 7.11, 7.30, 7.31, 7.40, 7.50, 7.51, 7.52, 7.53, 7.54, 7.55, 7.56, and 7.86</li>\\n</ul>",
          "sources": [
            {
              "source_description": "Company A Security Patch Day – January 2022",
              "source_name": "Company A",
              "url": "https://wiki.scn.company.com/wiki/pages/viewpage.action?pageId=596902035",
              "date": "2022-01-11T17:00:00.000Z",
              "unique_id": "59690xxxx"
            }
          ],
          "exploitation_state": "No Known",
          "date_of_disclosure": "2022-01-11T07:00:00.000Z",
          "id": "vulnerability--27efc4f2-4d7b-5d39-a96f-xxxxx",
          "vendor_fix_references": [
            {
              "url": "https://launchpad.support.company.com/#/notes/311xxxxx",
              "name": "Company A (311xxxx) Security Update Information",
              "unique_id": "311xxxxx"
            }
          ],
          "title": "Company A NetWeaver Application Server 7.86 Unspecified Vulnerability",
          "exploitation_vectors": [
            "General Network Connectivity"
          ],
          "was_zero_day": false,
          "vulnerable_cpes": [
            {
              "technology_name": "netweaver_as_abap 7.31",
              "vendor_name": "Company A",
              "cpe_title": "company a netweaver_as_abap 7.31",
              "cpe": "cpe:2.3:a:aompany a:netweaver_as_abap:7.31:*:*:*:*:*:*:*"
            }
          ],
          "executive_summary": "<p>An unspecified vulnerability exists within Company A&nbsp;NetWeaver Application Server 7.86 and earlier that, when exploited, allows an authenticated attacker to remotely access potentially sensitive information. Exploit code is not publicly available. Mitigation options include a vendor fix.</p>",
          "cwe": "Unknown",
          "description": null,
          "cve_id": "CVE-2022-xxxx",
          "risk_rating": "LOW",
          "observed_in_the_wild": false,
          "common_vulnerability_scores": {
            "v2.0": {
              "access_complexity": "LOW",
              "temporal_score": 3,
              "confidentiality_impact": "PARTIAL",
              "report_confidence": "CONFIRMED",
              "base_score": 4,
              "access_vector": "NETWORK",
              "vector_string": "AV:N/AC:L/Au:S/C:P/I:N/A:N/E:U/RL:OF/RC:C",
              "integrity_impact": "NONE",
              "availability_impact": "NONE",
              "remediation_level": "OFFICIAL_FIX",
              "authentication": "SINGLE",
              "exploitability": "UNPROVEN"
            }
          },
          "available_mitigation": [
            "Patch"
          ],
          "exploitation_consequence": "Information Disclosure",
          "analysis": "<p>Mandiant Threat Intelligence considers this a Low-risk vulnerability because of the privileges required and the limited impact upon exploitation.</p>",
          "audience": [
            "intel_vuln"
          ],
          "publish_date": "2022-01-11T18:24:00.000Z",
          "workarounds": null,
          "type": "vulnerability",
          "is_publishable": true,
          "associated_actors": [],
          "associated_malware": [],
          "intel_free": false,
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ipv4--da5b1f26-xxxx-5a61-9c93-6dxxxxxxxxxx"
        }
      }
    

##### Entity Enrichment

**Enrichment Table for Indicators - Prefix** Mandiant_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
first_seen | first_seen | When available in JSON  
last_seen | last_seen | When available in JSON  
sources | CSV of unique "sources/source_name" | When available in JSON  
mscore | mscore | When available in JSON  
attributed_associations_{associated_associations/type} | CSV of attributed_associations/name per attributed_associations/type, so one key per type.For example, all of the malware is in one place. | When available in JSON  
report_link | It's crafted. | When available in JSON  
  
**Enrichment Table for Threat Actor - Prefix** Mandiant_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
motivations | CSV of motivations/name | When available in JSON  
aliases | CSV of aliases/name | When available in JSON  
industries | CSV of industries/name | When available in JSON  
malware | CSV of malware/name | When available in JSON  
locations\\_source | CSV of locations/source/country/name | When available in JSON  
locations\\_target | CSV of locations/target/name | When available in JSON  
cve | CSV of cve/cve\\_id | When available in JSON  
description | description | When available in JSON  
last\\_activity\\_time | last\\_activity\\_time | When available in JSON  
report\\_link | It's crafted. | When available in JSON  
  
**Enrichment Table for Vulnerability - Prefix** Mandiant_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
sources | CSV of source_name | When available in JSON  
exploitation_state | exploitation_state | When available in JSON  
date_of_disclosure | date_of_disclosure | When available in JSON  
vendor_fix_references | vendor_fix_references/url | When available in JSON  
title | title | When available in JSON  
exploitation_vectors | CSV of exploitation_vectors | When available in JSON  
description | description | When available in JSON  
risk_rating | risk_rating | When available in JSON  
available_mitigation | CSV of available_mitigation | When available in JSON  
exploitation_consequence | exploitation_consequence | When available in JSON  
report_link | It's crafted. | When available in JSON  
  
##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******If data is available for one entity (is_success=true): "Successfully enriched the following entities using information from Mandiant: {entity.identifier}." If data is not available for one entity (is_success=true): "Action wasn't able to enrich the following entities using information from Mandiant: {entity.identifier}."_If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)" | General  
Case Wall Table | **Table Title:** {entity.identifier} **Table Columns:**

  * Key
  * Value

| Entity  
  
### Get Related Entities

Get information about IOC related to entities using information from Mandiant. Supported entities: Hostname, IP Address, URL, File Hash, Threat Actor.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Lowest Severity Score | Integer | 50 | Yes | Specify the lowest severity score that is used to return related indicators.Maximum: 100  
Max IOCs To Return | Integer | 100 | No | Specify the number of indicators that the action needs to process per entity.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * URL
  * File Hash
  * Threat Actor



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "hash": [{value}],
        "url": [{value}],
        "fqdn": [{value}],
        "ip": [{value}],
        "email": [{value}]
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully returned related indicators for the following entities using information from Mandiant: {entity.identifier}."_If no data is not available for one entity (is_success=true):_ "No related indicators were found for the following entities using information from Mandiant: {entity.identifier}."_If data is not available for all entities (is_success=false):_ "No related indicators were found."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Related Entities". Reason: {0}''.format(error.Stacktrace)" | General  
  
### Enrich IOCs

Get information about IOC from Mandiant.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
IOC Identifiers | CSV | N/A | Yes | Specify a comma-separated list of IOCs that need to be enriched.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "first_seen": "2011-09-12T12:23:13.000Z",
        "last_seen": "2011-09-12T12:23:13.000Z",
        "sources": [
            {
                "first_seen": "2011-09-12T12:23:13.000+0000",
                "last_seen": "2011-09-12T12:23:13.000+0000",
                "osint": false,
                "category": [],
                "source_name": "Mandiant"
            }
        ],
        "mscore": 47,
        "attributed_associations": [
            {
                "id": "threat-actor--0ac5c1db-8ad6-54b8-b4b9-c32fc738c54a",
                "name": "APT1",
                "type": "threat-actor"
            }
        ],
        "misp": {
            "smtp-receiving-ips": false,
            "covid": false,
            "eicar.com": false,
            "majestic_million": false,
            "sinkholes": false,
            "alexa": false,
            "cisco_top1000": false,
            "crl-hostname": false,
            "microsoft-office365": false,
            "microsoft": false,
            "googlebot": false,
            "microsoft-azure-germany": false,
            "microsoft-attack-simulator": false,
            "microsoft-azure": false,
            "rfc5735": false,
            "tranco10k": false,
            "public-dns-v4": false,
            "dax30": false,
            "dynamic-dns": false,
            "public-dns-v6": false,
            "covid-19-cyber-threat-coalition-whitelist": false,
            "common-ioc-false-positive": false,
            "cisco_1M": false,
            "google-gmail-sending-ips": false,
            "microsoft-azure-china": false,
            "stackpath": false,
            "google": false,
            "cloudflare": false,
            "moz-top500": false,
            "tranco": false,
            "tlds": true,
            "university_domains": false,
            "smtp-sending-ips": false,
            "cisco_top20k": false,
            "empty-hashes": false,
            "nioc-filehash": false,
            "amazon-aws": false,
            "url-shortener": false,
            "microsoft-office365-ip": false,
            "microsoft-win10-connection-endpoints": false,
            "microsoft-azure-us-gov": false,
            "majestic_million_1M": false,
            "mozilla-CA": false,
            "whats-my-ip": false,
            "microsoft-office365-cn": false,
            "vpn-ipv6": false,
            "rfc3849": false,
            "rfc6761": false,
            "security-provider-blogpost": false,
            "cisco_top5k": false,
            "apple": false,
            "public-dns-hostname": false,
            "mozilla-IntermediateCA": false,
            "rfc1918": false,
            "ti-falsepositives": false,
            "akamai": false,
            "bank-website": false,
            "automated-malware-analysis": false,
            "rfc6598": false,
            "alexa_1M": false,
            "google-gcp": false,
            "ovh-cluster": false,
            "multicast": false,
            "phone_numbers": false,
            "fastly": false,
            "cisco_top10k": false,
            "second-level-tlds": true,
            "wikimedia": false,
            "disposable-email": false,
            "common-contact-emails": false,
            "vpn-ipv4": false,
            "ipv6-linklocal": false,
            "covid-19-krassi-whitelist": false,
            "crl-ip": false
        },
        "id": "fqdn--25667188-bcf5-5abc-b1cc-caabfa18e2b3",
        "type": "fqdn",
        "value": "agru.qpoe.com",
        "is_publishable": true,
        "is_exclusive": true,
        "last_updated": "2022-02-21T13:20:27.176Z"
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******If data is available for one IOC (is_success=true): "Successfully enriched the following IOCs using information from Mandiant: {ioc .identifier}." If no data is not available for one IOC (is_success=true): "Action wasn't able to enrich the following IOCs using information from Mandiant: {ioc .identifier}." If data is not available for all IOCs (is_success=false): "No IOCs were enriched."**The action should fail and stop a playbook execution:******If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Get Related Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Malware Details

Get information about malware from Mandiant.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Malware Names | CSV | N/A | Yes | Specify a comma-separated list of malware names that need to be enriched.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
Fetch Related IOCs | Checkbox | Checked | No | If enabled, the action fetches indicators that are related to the provided malware.  
Max Related IOCs To Return | Integer | 100 | No | Specify the number of indicators that the action needs to process per malware.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "inherently_malicious": 1,
        "operating_systems": [
            "Windows"
        ],
        "aliases": [],
        "capabilities": [
            {
                "name": "Allocates memory",
                "description": "Capable of allocating memory. "
            }
        ],
        "detections": [],
        "yara": [],
        "roles": [
            "Cryptocurrency Miner"
        ],
        "malware": [],
        "actors": [],
        "cve": [],
        "id": "malware--96f82012-c77e-5887-bee9-69aec0b88578",
        "name": "PHOTOMINER",
        "description": "PHOTOMINER is a Windows-based modular cryptocurrency mining malware that communicates over HTTP.",
        "type": "malware",
        "last_updated": "2022-04-13T02:59:30.000Z",
        "last_activity_time": "2022-04-13T02:59:30.000Z",
        "audience": [
            {
                "name": "intel_fusion",
                "license": "INTEL_RBI_FUS"
            }
        ],
        "is_publishable": true,
        "counts": {
            "reports": 0,
            "capabilities": 26,
            "malware": 0,
            "actors": 0,
            "detections": 0,
            "cve": 0,
            "aliases": 0,
            "industries": 5,
            "attack_patterns": 19
        },
        "intel_free": false
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one malware (is_success=true):_ "Successfully enriched the following malware using information from Mandiant: {malware name}."_If no data is not available for one malware (is_success=true):_ "Action wasn't able to enrich the following malware using information from Mandiant: {malware name}."_If data is not available for all malware (is_success=false)_ : "No malware information was found."**The action should fail and stop a playbook execution:******If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Get Malware Details". Reason: {0}''.format(error.Stacktrace)" | General  
Case Wall Table | **Table Name:** Malware Results **Table Columns:**

  * Name - name
  * Description - description
  * Aliases - csv of {aliases/name}
  * Last Activity Time - {last_activity_time}

| General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
