---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/digital-shadows/
title: Digital Shadows \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:48.926224+00:00
---

# Digital Shadows  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/digital-shadows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Digital Shadows

This document describes how to integrate Digital Shadows with Google Security Operations.

## Use cases

Digital Shadows integration is used as a source for alerts and to enrich entities.

## Prerequisites

To use the Digital Shadows API, the API key is required. 

**Important:** To obtain the API credentials, contact a Digital Shadows representative.

Requests to all operation endpoints require HTTP basic authentication and dedicated (high entropy) API credentials that normally consist of a 6-character _key_ and a 32-character _secret_.

**Note:** Your usual email and password login details are incompatible with the HTTP Basic authentication mechanism. Use credentials received from a Digital Shadows representative.

## Integrate Digital Shadows with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration inputs

To configure the integration, use the following parameters:

Parameters  
---  
`Instance Name` | _Optional_ Name of the Instance you intend to configure integration for.  
`Description` | _Optional_ Instance description.  
`API Key` | _Required_ Digital Shadow API Key.  
`API Secret` | _Optional_ Digital Shadow API Secret.  
`Run Remotely` | _Optional_ Check the field to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).Unchecked by default.  
**Note:** You can make changes at a later stage, if needed. Once configured, the instances can be used in playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Enrich CVE

Enrich a CVE using Digital Shadows information.

Analysts may use this action to get more information about the particular CVE, which is useful for the investigation.

#### Entities

This action runs on the CVE entity.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | Available  
Case wall table | N/A  
Enrichment table | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment

Enrichment field | Source (JSON key) | Logic  
---|---|---  
`DigitalShadows_Exploit_title` | `entity/title` | If available in JSON result.  
`DigitalShadows_Exploit_type` | `entity/type` | If available in JSON result.  
`DigitalShadows_Exploit_platform` | `entity/platform` | If available in JSON result.  
`DigitalShadows_Exploit_source` | `entity/sourceUri` | If available in JSON result.  
`DigitalShadows_Vulnerability_sourceURL` | `entity/sourceUri` | If available in JSON result.  
`DigitalShadows_Vulnerability_description` | `entity/description` | If available in JSON result.  
`DigitalShadows_Vulnerability_score` | `entity/cvss2Score/baseScore` | If available in JSON result.  
`DigitalShadows_Vulnerability_authentication` | `entity/cvss2Score/authentication` | If available in JSON result.  
`DigitalShadows_Vulnerability_accessVector` | `entity/cvss2Score/accessVector` | If available in JSON result.  
`DigitalShadows_Vulnerability_accessComplexity` | `entity/cvss2Score/accessComplexity` | If available in JSON result.  
`DigitalShadows_Vulnerability_confidentialityImpact` | `entity/cvss2Score/confidentialityImpact` | If available in JSON result.  
`DigitalShadows_Vulnerability_integrityImpact` | `entity/cvss2Score/integrityImpact` | If available in JSON result.  
`DigitalShadows_Vulnerability_availabilityImpact` | `entity/cvss2Score/availabilityImpact` | If available in JSON result.  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
        "content": [
            {
                "entity": {
                    "cveIdentifier": "CVE-2011-0489",
                    "created": "2011-01-18T18:03:00.000Z",
                    "updated": "2017-08-17T01:33:00.000Z",
                    "sourceUri": "https://nvd.nist.gov/vuln/detail/CVE-2011-0489",
                    "description": "The server components in Example_DB 10.0 do not require authentication for administrative commands, which allows remote attackers to modify data, obtain sensitive information, or cause a denial of service by sending requests over TCP to (1) the Lock Server or (2) the Advanced Multithreaded Server, as demonstrated by commands that are ordinarily sent by the (a) ookillls and (b) oostopams applications.  NOTE: some of these details are obtained from third party information.",
                    "relatedCPEs": [
                        "cpe:/a:example:example%2fdb:10.0"
                    ],
                    "cvss2Score": {
                        "baseScore": 7.5,
                        "authentication": "NONE",
                        "accessVector": "NETWORK",
                        "accessComplexity": "LOW",
                        "confidentialityImpact": "PARTIAL",
                        "integrityImpact": "PARTIAL",
                        "availabilityImpact": "PARTIAL"
                    }
                },
                "type": "VULNERABILITY",
                "snippet": "CVE ID: CVE-2011-0489</em><br><br>",
                "sortDate": "2017-08-17T01:33:00.000Z"
            },
            {
                "entity": {
                    "id": "f75754b5-65a3-46ee-bea7-e0f015a5283d",
                    "uri": "http://example.com",
                    "pasted": "2018-01-05T09:10:02.000Z",
                    "observableCounts": {
                        "ipV4": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "email": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "md5": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha1": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha256": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "host": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "cve": {
                            "count": 100,
                            "exceededMaximum": true
                        }
                    },
                    "screenshot": {
                        "id": "3ab6b3cb-349d-4ed7-b150-773454a11908",
                        "link": "https://example.com"
                    },
                    "screenshotThumbnail": {
                        "id": "7529cf75-5ddb-4e2d-8fc9-f3531e33704e",
                        "link": "https://example.com"
                    }
                },
                "type": "PASTE",
                "snippet": "&quot;\n  ], \n  &quot;CVE-2002-1656&quot;: [\n    &quot;3043&quot;\n  ], \n  &quot;CVE-2003-0347&quot;: [\n    &quot;23094&quot;\n  ], \n  &quot;<em>CVE</em>-<em>2011</em>-<em>0489</em>&quot;: [\n    &quot;15988",
                "sortDate": "2018-01-05T09:10:02.000Z"
            },
                "type": "PASTE",
                "snippet": ") sequences in a crafted request.\n| [<em>CVE</em>-<em>2011</em>-<em>0489</em>] The server components in Example_DB 10.0 do ...  in a crafted request.\n| [<em>CVE</em>-<em>2011</em>-<em>0489</em>] The server components in Example_DB 10.0 do not require ...  request.\n| [<em>CVE</em>-<em>2011</em>-<em>0489</em>] The server components in Example_DB 10.0 do not require ...  files via &quot;../\\&quot; (dot dot forward-slash backslash) sequences in a crafted request.\n| [<em>CVE</em>-<em>2011</em>-<em>0489</em>",
                "sortDate": "2019-07-23T21:35:39.000Z"
            }
        ],
        "currentPage": {
            "offset": 0,
            "size": 50
        },
        "total": 4,
        "facets": {}
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched CVE.` `No CVEs were enriched.` | Action succeeded.  
`Error executing action "Enrich CVE". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Case wall links

  * If `TYPE=Exploit` is available in the JSON response:

**Title** : Exploit Source URL

**Link** : `entity/sourceUri`

  * If `TYPE=Vulnerability` is available in the JSON response:

**Title** : Vulnerability Source URL:

**Link** : `entity/sourceUri`

  * For all entities that returned data:

**Title** : Full Digital Shadow Search Result

**Link** : `https://portal-digitalshadows.com/search?q=ENTITY`




### Enrich Hash - Deprecated

**Deprecated:** This action is deprecated.

Enrich a Hash using Digital Shadows information.

##### Use cases

Analysts may use this action to collect additional details, for example whether or not it is a safe hash that would be beneficial to the investigation. 

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Source (JSON Key)** | **Logic - When to apply**  
---|---|---  
DigitalShadows_CylanceFileHash_generalScore | entity/fileHashInfo/generalScore | If available in JSON Result.  
DigitalShadows_CylanceFileHash_classifier_ml | entity/fileHashInfo/classifiers/ml | If available in JSON Result.  
DigitalShadows_CylanceFileHash_classifier_industry | entity/fileHashInfo/classifiers/industry | If available in JSON Result.  
DigitalShadows_CylanceFileHash_classifier_human | entity/fileHashInfo/classifiers/human | If available in JSON Result.  
  
DigitalShadows_WebrootFileHash_category | entity/category | If available in JSON Result.  
DigitalShadows_WebrootFileHash_malwareCategory | entity/malwareCategory | If available in JSON Result.  
DigitalShadows_WebrootFileHash_fileSizeBytes | entity/fileSizeBytes | If available in JSON Result.  
DigitalShadows_WebrootFileHash_fileLastSeen | entity/fileLastSeen | If available in JSON Result.  
DigitalShadows_WebrootFileHash_sourceUrls | entity/sourceUrls | If data is available in JSON Result. Empty lists should be ignored.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "content": [
            {
                "entity": {
                    "requestedHash": "617f7301fd67e8b5d8ad42d4e94e02cb313fe5ad51770ef93323c6115e52fe98",
                    "status": 0,
                    "fileHashInfo": {
                        "status": "COMPLETE",
                        "statusCode": 1,
                        "generalScore": -1.0,
                        "classifiers": {
                            "ml": 1.0,
                            "industry": -1.0,
                            "human": -1.0
                        },
                        "hashes": {
                            "sha256": "617F7301FD67E8B5D8AD42D4E94E02CB313FE5AD51770EF93323C6115E52FE98",
                            "sha1": "CF0743ED381ADE69BBA3D1DD3D357A8300BCD4AE",
                            "md5": "8FE94843A3E655209C57AF587849AC3A"
                        }
                    }
                },
                "type": "CYLANCE_FILE_HASH"
            },
                  {
                "entity": {
                    "id": "7ab729ab-2176-4072-8fcc-483410e7949d",
                    "uri": "http://example.com",
                    "title": "Malware hashes",
                    "pasted": "2019-12-07T04:01:21.000Z",
                    "observableCounts": {
                        "ipV4": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "email": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "md5": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha1": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha256": {
                            "count": 45,
                            "exceededMaximum": false
                        },
                        "host": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "cve": {
                            "count": 0,
                            "exceededMaximum": false
                        }
                    },
                    "screenshot": {
                        "id": "a358a7fd-ce76-4ac0-a338-7a17c5affcca",
                        "link": "https://example.com"
                    },
                    "screenshotThumbnail": {
                        "id": "2a98b417-1846-47ca-835f-b4be580cfdc2",
                        "link": "https://example.com"
                    }
                },
                "type": "PASTE",
                "snippet": "617f7301fd67e8b5d8ad42d4e94e02cb313fe5ad51770ef93323c6115e52fe98\n137e17ed0c693f5ba23c3f3bf252f7edc29548d97f426625a4e0c5fea0558e45",
                "sortDate": "2019-12-07T04:01:21.000Z"
            },
            {
                "entity": {
                    "id": "e05f1f61-5996-4ff9-b656-5d7fe856e459",
                    "uri": "http://example.com",
                    "pasted": "2017-12-27T08:53:14.000Z",
                    "observableCounts": {
                        "ipV4": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "email": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "md5": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha1": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha256": {
                            "count": 100,
                            "exceededMaximum": true
                        },
                        "host": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "cve": {
                            "count": 0,
                            "exceededMaximum": false
                        }
                    },
                    "screenshot": {
                        "id": "d41fd1d9-aa0c-411d-87f5-824d036e9843",
                        "link": "https://example.com"
                    },
                    "screenshotThumbnail": {
                        "id": "ab91eba6-f8fd-4a7e-a3b4-6b100ee50789",
                        "link": "https://example.com"
                    }
                },
                "type": "PASTE",
                "snippet": "617F7301FD67E8B5D8AD42D4E94E02CB313FE5AD51770EF93323C6115E52FE98",
                "sortDate": "2017-12-27T08:53:14.000Z"
            }
        ],
        "currentPage": {
            "offset": 0,
            "size": 25
        },
        "total": 4,
        "facets": {}
     }
     

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:** _If no errors and returned data for entities:_   
Print "Successfully connected to the Digital Shadows with the provided connection parameters!  
_If no errors and returned no data for entities:_  
Print "No hashes were enriched". **The action should fail and stop a playbook execution:** _If error:_ Print "Error executing action "Enrich Hash". Reason: {0}''.format(error.Stacktrace) | General  
Links | **For all entities that returned data:** **Title:** Full Digital Shadows Search Result **Link:** https://portal-digitalshadows.com/search?q=`ENTITY` | Entity  
  
### Enrich IP - Deprecated

**Deprecated:** This action is deprecated.

Enrich an IP using Digital Shadows information.

#### Use cases

Analysts may use this action to get more information about the IP address, which is useful for the investigation.

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Source (JSON Key)** | **Logic - When to apply**  
---|---|---  
DigitalShadows_WebrootIP_reputationScore | entity/reputationScore | If available in JSON Result.  
DigitalShadows_WebrootIP_asn | entity/asn | If available in JSON Result.  
DigitalShadows_WebrootIP_currentlyClassifiedAsThreat | entity/currentlyClassifiedAsThreat | If available in JSON Result.  
DigitalShadows_WebrootIP_ipThreatHistory | entity/ipThreatHistory | If available in JSON Result.  
DigitalShadows_WebrootIP_country | entity/ipGeoInfo/country | If available in JSON Result.  
DigitalShadows_WebrootIP_region | entity/ipGeoInfo/region | If available in JSON Result.  
DigitalShadows_WebrootIP_state | entity/ipGeoInfo/state | If available in JSON Result.  
DigitalShadows_WebrootIP_city | entity/ipGeoInfo/city | If available in JSON Result.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "content": [
            {
                "entity": {
                    "ipAddress": "192.0.2.1",
                    "updatedDateTime": "2020-02-21T01:10:01.000Z",
                    "reputationScore": 18,
                    "asn": 13335,
                    "currentlyClassifiedAsThreat": false,
                    "threatCategories": [],
                    "ipThreatHistory": [],
                    "ipReputationHistory": [
                        {
                            "timestamp": "2020-02-21T01:10:01.000Z",
                            "reputation": 18
                        },
                        {
                            "timestamp": "2020-02-07T01:10:02.000Z",
                            "reputation": 29
                        }
                    ],
                    "ipIncidentHistory": [
                        {
                            "classifiedAsThreat": false,
                            "startDateTime": "2019-07-15T00:37:12.000Z",
                            "durationSeconds": 0,
                            "numberOfAttempts": 0,
                            "eventType": "Phishing IPs",
                            "threatType": "Phishing",
                            "eventDescription": "IP hosts phishing sites",
                            "applications": [],
                            "hostingPhishUrls": [
                                "example.net"
                            ],
                            "scanDetails": [],
                            "attackDetails": []
                        },
                        {
                            "classifiedAsThreat": false,
                            "startDateTime": "2018-07-21T00:23:27.000Z",
                            "durationSeconds": 0,
                            "numberOfAttempts": 0,
                            "eventType": "Phishing IPs",
                            "threatType": "Phishing",
                            "eventDescription": "IP hosts phishing sites",
                            "applications": [],
                            "hostingPhishUrls": [
                                "example.net"
                            ],
                            "scanDetails": [],
                            "attackDetails": []
                        }
                    ],
                    "ipGeoInfo": {
                        "country": "united states",
                        "region": "mid atlantic",
                        "state": "new jersey",
                        "city": "newark",
                        "latitude": "40.73873",
                        "longitude": "-74.19453",
                        "organization": "example  inc.",
                        "carrier": "example",
                        "tld": "",
                        "sld": "",
                        "asn": "example_isn"
                    }
                },
                "type": "WEBROOT_IP"
            },
            {
                "entity": {
                    "id": "0007b64b-ef21-4b5f-a0c2-1e469ceb6896",
                    "uri": "http://example.com",
                    "pasted": "2019-10-23T13:32:46.000Z",
                    "observableCounts": {
                        "ipV4": {
                            "count": 100,
                            "exceededMaximum": true
                        },
                        "email": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "md5": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha1": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "sha256": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "host": {
                            "count": 0,
                            "exceededMaximum": false
                        },
                        "cve": {
                            "count": 0,
                            "exceededMaximum": false
                        }
                    },
                    "screenshot": {
                        "id": "b019cfcf-2d36-4bcd-9bf3-69fa67b5ec6d",
                        "link": "https://example.com"
                    },
                    "screenshotThumbnail": {
                        "id": "57af6550-6690-478f-8ba5-640a5560311a",
                        "link": "https://example.com"
                    }
                },
                "type": "PASTE",
                "snippet": "192.0.2.1\n192.0.2.2\n192.0.2.3\n192.0.2.4\n192.0.2.5\n192.0.2.6\n192.0.2.7",
                "sortDate": "2019-10-23T13:32:46.000Z"
            }
        ],
        "currentPage": {
            "offset": 0,
            "size": 50
        },
        "total": 10,
        "facets": {}
     }
     

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:**_If no errors and returned data for entities:_  
Print "Successfully enriched IP addresses {0}".format(entity)  
_If no errors and returned no data for entities:_   
Print "No IP addresses were enriched". **The action should fail and stop a playbook execution:** _If error:_ Print "Error executing action "Enrich IP". Reason: {0}''. format(error.Stacktrace) | General  
Links | **For all entities that returned data:** **Title:** Full Digital Shadows Search Result **Link:** https://portal-digitalshadows.com/search?q= `ENTUTY` | Entity  
  
### Enrich URL

Enrich a URL using Digital Shadows information.

Analysts may use this action to get more information about the specific URL address, which is useful for the investigation.

#### Entities

This action runs on the URL entity.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | Available  
Case wall table | N/A  
Enrichment table | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment

Enrichment field | Source (JSON key) | Logic  
---|---|---  
`DigitalShadows_WebrootDomain_timesLabeledAsThreat` | `entity/threatHistory` | If available in JSON result.  
`DigitalShadows_WebrootDomain_age` | `entity/age` | If available in JSON result.  
`DigitalShadows_WebrootIP_popularity` | `entity/popularity` | If available in JSON result.  
`DigitalShadows_WebrootIP_reputation` | `entity/reputation` | If available in JSON result.  
`DigitalShadows_WebrootIP_threatCategories` | `entity/threatCategories` | If available in JSON result.  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
        "content": [
            {
                "entity": {
                    "domainOrUrl": "www.example.com",
                    "lastUpdated": "2020-02-25T12:08:20.944Z",
                    "threatCategories": [
                        {
                            "confidence": 93,
                            "group": "Security",
                            "name": "Malware Sites"
                        }
                    ],
                    "reputation": 10,
                    "popularity": "UNRANKED",
                    "age": 82,
                    "threatHistory": 1,
                    "webrootCrawlHistory": [],
                    "domainHostedHashes": []
                },
                "type": "WEBROOT_DOMAIN"
            }
        ],
        "currentPage": {
            "offset": 0,
            "size": 50
        },
        "total": 66,
        "facets": {}
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched URLs: URLS` `No URLs were enriched.` | Action succeeded.  
`Error executing action "Enrich URL". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Case wall link

For all entities that returned data:

**Title** : Full Digital Shadow Search Result  
**Link** : `https://portal-digitalshadows.com/search?q=ENTITY`

### Ping

Test connectivity to Digital Shadows with parameters provided at the integration configuration page in the Google Security Operations Marketplace tab.

This action can be executed manually and isn't used playbooks.

#### Entities

This action doesn't run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | Available  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Digital Shadows with the provided connection parameters!` | Action succeeded.  
`Error executing action "Ping". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Case wall link

For all entities that returned data:

**Title** : Full Digital Shadow Search Result  
**Link** : `https://portal-digitalshadows.com/search?q=ENTITY`

## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Digital Shadows - Incident Connector

Ingest incidents from Digital Shadows into Google SecOps.

##### Connector inputs

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ Input the source field name to retrieve the `Product Field` name. Default value is `Product Name`.  
`Event Field Name` | _Required_ Enter the source field name to retrieve the `Event Field` name. Default value is `type`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the default environment is used.  
`Script Timeout (Seconds)` | _Required_ Timeout limit for the python process running the current script. Default value is 180 seconds.  
`API Key` | _Required_ Digital Shadow API Key.  
`API secret` | _Required_ Digital Shadow API Secret.  
`Client Secret` | _Required_ Client Secret of the CrowdStrike account.  
`Fetch Max Hours Backwards` | _Optional_ Number of hours before now to retrieve incidents from. Default value is 1 hour.  
`Lowest Severity To Fetch` | _Required_ Lowest severity score of the incidents to fetch. Possible values are:

  * `VERY_HIGH`
  * `HIGH`
  * `MEDIUM`
  * `LOW`
  * `VERY_LOW`
  * `NONE`

Default value is `NONE`.  
`Incident Type Filter` | _Optional_ Comma-separated list of incident types that should be ingested into Google SecOps. By default, the connector retrieves all of the incident types. Possible values are:

  * `DATA_LEAKAGE`
  * `CYBER_THREAT`
  * `PHYSICAL_SECURITY`
  * `SOCIAL_MEDIA_COMPLIANCE`
  * `BRAND_PROTECTION`
  * `INFRASTRUCTURE`

  
`Max Incidents To Fetch` | _Optional_ Number of incidents to process per one connector iteration. Default value is 50.  
`Use whitelist as a blacklist` | _Required_ If checked, the dynamic list is used as a blocklist. Unchecked by default.  
`Verify SSL` | _Required_ If checked, verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Unchecked by default.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Password` | _Optional_ Proxy password to authenticate with.  
  
#### Connector rules

Connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
