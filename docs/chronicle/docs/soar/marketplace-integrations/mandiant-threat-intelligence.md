---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-threat-intelligence/
title: Integrate Mandiant Threat Intelligence with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:06:01.174899+00:00
---

# Integrate Mandiant Threat Intelligence with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-threat-intelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Mandiant Threat Intelligence with Google SecOps

This document explains how to integrate Mandiant Threat Intelligence with Google Security Operations.

**Note:** We recommend using the [**Google Threat Intelligence**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-threat-intelligence) integration instead, as it provides more capabilities and features than this integration.

## Use cases

The **Mandiant Threat Intelligence** integration uses the Google SecOps capabilities to support the following use cases:

  * **Automated triage and scoring** : Enrich entities (IPs, Hashes, Hostnames, URLs) in an active case with the Mandiant Severity Score (M-Score) to automatically determine suspicion status and prioritize high-risk indicators based on the configured threshold.

  * **Threat correlation and investigation** : Pivot from an indicator (IP, Hash, or URL) to retrieve and correlate associated Mandiant objects, including Threat Actors, Malware families, and Vulnerabilities (CVEs) linked to the observed activity.

  * **Proactive hunting and remediation** : Use known malware or threat actor names (from external reports) to retrieve all related indicators of compromise (IOCs) such as newly identified File Hashes or IPs for defensive blocking or proactive hunting across the environment.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

The Mandiant Threat Intelligence integration requires the following parameters:

Parameter | Description  
---|---  
`UI Root` | Required. The UI root of the Mandiant instance.  
`API Root` | Required. The API root of the Mandiant instance. To authenticate with Google Threat Intelligence credentials, enter the following value: `https://www.virustotal.com`.  
`Client ID` | Optional. The client ID of the Mandiant Threat Intelligence account. To generate the client ID in Mandiant Threat Intelligence, go to **Account settings > API access and keys > Get key ID and secret**.  
`Client Secret` | Optional. The client secret of the Mandiant Threat Intelligence account. To generate the client secret in Mandiant Threat Intelligence, go to **Account settings > API access and keys > Get key ID and secret**.  
`GTI API Key` | Optional. The API key of Google Threat Intelligence. To authenticate using Google Threat Intelligence, set the `API Root` value to `https://www.virustotal.com`. When you authenticate using the Google Threat Intelligence API key, it takes priority over other authentication methods.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Mandiant Threat Intelligence server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Entities

**Important:** This action can experience significant delays or fail due to timeouts if you supply invalid or generic entities in a case, for example, `NONE`, `N/A`, or `localhost`. 

Processing these entities can result in a high volume of API responses, leading to severe playbook latency. To prevent this, we recommend refining the action scope to include only relevant entities by using **Entity Selection** within your playbook.

Use the **Enrich Entities** action to enrich entities using the information from Mandiant Threat Intelligence.

This action runs on the following Google SecOps entities:

  * `CVE`
  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `Threat Actor`
  * `URL`

**Note:** This action only supports the `MD5`, `SHA-1`, and `SHA-256` hashes.

#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Severity Score Threshold` | Required. The minimum severity score an entity must meet or exceed to be marked as suspicious. The action can only mark the following indicators as suspicious:

  * `Hostname`
  * `IP Address`
  * `File Hash`
  * `URL`

The maximum value is `100`. The default value is `50`.  
`Create Insight` | Optional. If selected, the action creates an insight containing all retrieved information about the entity. Enabled by default.  
`Only Suspicious Entity Insight` | Optional. If selected, the action generates insights only for entities determined to be suspicious based on the configured severity threshold. Insights are always created for `Threat Actor` and `Vulnerability` entities, regardless of their suspicious status. **Note:** `Create Insight` must be enabled for this parameter.   
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The following table lists the values for indicators enrichment when using the **Enrich Entities** action:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`first_seen` | `first_seen` | When available in the JSON result.  
`last_seen` | `last_seen` | When available in the JSON result.  
`sources` | A CSV file of unique `sources/source_name` values. | When available in the JSON result.  
`mscore` | `mscore` | When available in the JSON result.  
`attributed_associations_{associated_associations/type}` | A CSV file of `attributed_associations/name` keys for every `attributed_associations/type` type (one key for every type). | When available in the JSON result.  
`report_link` | Crafted. | When available in the JSON result.  
  
The following table lists the values for enrichment of the `Threat Actors` entity when using the **Enrich Entities** action:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`motivations` | A CSV of `motivations/name` values. | When available in the JSON result.  
`aliases` | A CSV of `aliases/name` values. | When available in the JSON result.  
`industries` | A CSV of `industries/name` values. | When available in the JSON result.  
`malware` | A CSV of `malware/name` values. | When available in the JSON result.  
`locations\_source` | A CSV of `locations/source/country/name` values. | When available in the JSON result.  
`locations\_target` | A CSV of `locations/target/name` values. | When available in the JSON result.  
`cve` | A CSV of `cve/cve\_id` values. | When available in the JSON result.  
`description` | `description` | When available in the JSON result.  
`last\_activity\_time` | `last\_activity\_time` | When available in the JSON result.  
`report\_link` | Crafted. | When available in the JSON result.  
  
The following table lists the values for enrichment of the `Vulnerability` entity when using the **Enrich Entities** action:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`sources` | A CSV of `source_name` values. | When available in the JSON result.  
`exploitation_state` | `exploitation_state` | When available in the JSON result.  
`date_of_disclosure` | `date_of_disclosure` | When available in the JSON result.  
`vendor_fix_references` | `vendor_fix_references/url` | When available in the JSON result.  
`title` | `title` | When available in the JSON result.  
`exploitation_vectors` | A CSV of `exploitation_vectors` values. | When available in the JSON result.  
`description` | `description` | When available in the JSON result.  
`risk_rating` | `risk_rating` | When available in the JSON result.  
`available_mitigation` | A CSV of `available_mitigation` values. | When available in the JSON result.  
`exploitation_consequence` | `exploitation_consequence` | When available in the JSON result.  
`report_link` | Crafted | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output for indicators received when using the **Enrich Entities** action:
    
    
    {
        "Entity": "192.0.2.1",
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
          "id": "ID",
          "type": "ipv4",
          "value": "192.0.2.1",
          "is_publishable": true,
          "last_updated": "2022-05-22T01:04:46.098Z",
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ID"
        }
      }
    

The following example shows the JSON result output for the `Threat Actor` entity received when using the **Enrich Entities** action:
    
    
    {
        "Entity": "ENTITY_ID",
        "EntityResult": {
          "motivations": [
            {
              "id": "ID",
              "name": "Example",
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
              "id": "ID",
              "name": "Aerospace & Defense",
              "attribution_scope": "confirmed"
            },
            {
              "id": "ID",
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
              "id": "malware--ID",
              "name": "EXAMPLE1",
              "attribution_scope": "confirmed"
            },
            {
              "id": "malware--ID",
              "name": "EXAMPLE2",
              "attribution_scope": "confirmed"
            }
          ],
          "tools": [
            {
              "id": "malware--ID",
              "name": "EXAMPLE3",
              "attribution_scope": "confirmed"
            }
          ],
          "suspected_attribution": [],
          "locations": {
            "source": [
              {
                "region": {
                  "id": "location--ID",
                  "name": "Asia",
                  "attribution_scope": "confirmed"
                },
                "sub_region": {
                  "id": "location--ID",
                  "name": "East Asia",
                  "attribution_scope": "confirmed"
                },
                "country": {
                  "id": "location--ID",
                  "name": "China",
                  "iso2": "CN",
                  "attribution_scope": "confirmed"
                }
              }
            ],
            "target": [
              {
                "id": "location--ID",
                "name": "Belgium",
                "iso2": "be",
                "region": "Europe",
                "sub-region": "West Europe",
                "attribution_scope": "confirmed"
              }
            ],
            "target_sub_region": [
              {
                "id": "location--ID",
                "name": "East Asia",
                "key": "eastasia",
                "region": "Asia",
                "attribution_scope": "confirmed"
              }
            ],
            "target_region": [
              {
                "id": "location--ID",
                "name": "Africa",
                "key": "africa",
                "attribution_scope": "confirmed"
              }
            ]
          },
          "cve": [
            {
              "id": "vulnerability--ID",
              "cve_id": "CVE-ID",
              "attribution_scope": "confirmed"
            }
          ],
          "associated_uncs": [],
          "id": "threat-actor--ID",
          "name": "Example",
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
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ID"
        }
      }
    

The following example shows the JSON result output for the `Vulnerability` entity received when using the **Enrich Entities** action:
    
    
      {
        "Entity": "CVE-ID",
        "EntityResult": {
          "exploits": [],
          "vulnerable_products": "<p>The following vendors/products have been reported as vulnerable:</p>\\n<ul>\\n<li>Company A:&nbsp;Example Application Server&nbsp;7.01, 7.02, 7.11, 7.30, 7.31, 7.40, 7.50, 7.51, 7.52, 7.53, 7.54, 7.55, 7.56, and 7.86</li>\\n</ul>",
          "sources": [
            {
              "source_description": "Company A Security Patch Day – January 2022",
              "source_name": "Company A",
              "url": "URL",
              "date": "2022-01-11T17:00:00.000Z",
              "unique_id": "ID"
            }
          ],
          "exploitation_state": "No Known",
          "date_of_disclosure": "2022-01-11T07:00:00.000Z",
          "id": "vulnerability--ID",
          "vendor_fix_references": [
            {
              "url": "https://launchpad.support.company.com/#/notes/ID",
              "name": "Company A ID Security Update Information",
              "unique_id": "ID"
            }
          ],
          "title": "Company A Example Application Server 7.86 Unspecified Vulnerability",
          "exploitation_vectors": [
            "General Network Connectivity"
          ],
          "was_zero_day": false,
          "vulnerable_cpes": [
            {
              "technology_name": "example_as_abap 7.31",
              "vendor_name": "Company A",
              "cpe_title": "company a example_as_abap 7.31",
              "cpe": "cpe:2.3:a:company a:example_as_abap:7.31:*:*:*:*:*:*:*"
            }
          ],
          "executive_summary": "<p>An unspecified vulnerability exists within Company A&nbsp;Example Application Server 7.86 and earlier that, when exploited, allows an authenticated attacker to remotely access potentially sensitive information. Exploit code is not publicly available. Mitigation options include a vendor fix.</p>",
          "cwe": "Unknown",
          "description": null,
          "cve_id": "CVE-ID",
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
          "report_link": "https://advantage.mandiant.com/indicator/ipv4/ID"
        }
      }
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities using information from Mandiant: ENTITY_ID` `Action wasn't able to enrich the following entities using information from Mandiant: ENTITY_ID` `None of the provided entities were enriched.` | The action succeeded.  
`Error executing action MandiantThreatIntelligence - Enrich Entities. Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich IOCs

Use the **Enrich IOCs** action to retrieve threat intelligence data about specific IOCs from Mandiant.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Enrich IOCs** action requires the following parameters:

Parameter | Description  
---|---  
`IOC Identifiers` | Required. A comma-separated list of IOCs to retrieve threat intelligence data for.  
  
#### Action outputs

The **Enrich IOCs** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Enrich IOCs** action:
    
    
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
                "id": "threat-actor--ID",
                "name": "Example",
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
        "id": "fqdn--ID",
        "type": "fqdn",
        "value": "example.com",
        "is_publishable": true,
        "is_exclusive": true,
        "last_updated": "2022-02-21T13:20:27.176Z"
    }
    

##### Output messages

The **Enrich IOCs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following IOCs using information from Mandiant: IOC_ID` `Action wasn't able to enrich the following IOCs using information from Mandiant: IOC_ID.` `No IOCs were enriched.` | The action succeeded.  
`Error executing action "Enrich IOCs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich IOCs** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Malware Details

Use the **Get Malware Details** action to obtain information about malware from Mandiant Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Malware Details** action requires the following parameters:

Parameter | Description  
---|---  
`Malware Names` | Required. A comma-separated list of malware names to enrich.  
`Create Insight` | Optional. If selected, the action creates an insight that contains all retrieved information about the entity. Enabled by default.  
`Fetch Related IOCs` | Optional. If selected, the action fetches indicators that are related to the provided malware. Enabled by default.  
`Max Related IOCs To Return` | Optional. The maximum number of related indicators the action processes for each malware entry. The default value is `100`.  
  
#### Action outputs

The **Get Malware Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Malware Details** action:
    
    
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
        "id": "malware--ID",
        "name": "EXAMPLE",
        "description": "Example description",
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
    

##### Output messages

The **Get Malware Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following malware using information from Mandiant: MALWARE_NAME.` `Action wasn't able to enrich the following malware using information from Mandiant: MALWARE_NAME.` `No malware information was found.` | The action succeeded.  
`Error executing action "Get Malware Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Malware Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Related Entities

Use the **Get Related Entities** action to obtain details about indicators of compromise (IOCs) that are related to entities using information from Mandiant Threat Intelligence.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `Threat Actor`
  * `URL`



#### Action inputs

The **Get Related Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Lowest Severity Score` | Required. The minimum severity score an indicator must meet to be included in the results. The maximum value is `100`. The default value is `50`.  
`Max IOCs To Return` | Optional. The maximum number of IOCs the action retrieves for each processed entity. The default value is `100`.  
  
#### Action outputs

The **Get Related Entities** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Related Entities** action:
    
    
    {
        "hash": "VALUE",
        "url": "VALUE",
        "fqdn": "VALUE",
        "ip": "VALUE",
        "email": "VALUE"
    }
    

##### Output messages

The **Get Related Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related indicators for the following entities using information from Mandiant: ENTITY_ID` `No related indicators were found for the following entities using information from Mandiant: ENTITY_ID` `No related indicators were found.` | The action succeeded.  
`Error executing action "Get Related Entities". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related Entities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Mandiant Threat Intelligence.

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
`Successfully connected to the Mandiant server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Mandiant server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
