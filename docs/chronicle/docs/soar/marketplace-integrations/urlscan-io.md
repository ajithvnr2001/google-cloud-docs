---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/urlscan-io/
title: Integrate UrlScan.io with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:26.992553+00:00
---

# Integrate UrlScan.io with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/urlscan-io/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate UrlScan.io with Google SecOps 

This document provides guidance on how to integrate urlscan.io with Google SecOps.

This document explains how to integrate UrlScan.io with Google Security Operations.

## Use cases

The **UrlScan.io** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated URL analysis** : Automatically submit suspicious URLs to UrlScan.io to determine risk levels and retrieve screenshots for visual verification during incident triage.

  * **Threat intelligence enrichment** : Enrich alerts by querying UrlScan.io for detailed metadata on IP addresses, domains, and URLs, providing analysts with immediate context on ASN, server types, and malicious scores.

  * **Proactive historical scan search** : Search existing public and private scans associated with indicators of compromise to identify historical malicious activity and patterns.

  * **Deep-dive forensics and reporting** : Retrieve comprehensive scan details using specific scan IDs to perform in-depth analysis of cookies, request counts, and related links for complex security investigations.




## Before you begin

To authenticate the connection between Google SecOps and UrlScan.io, you must provide a valid API key. 

You can obtain and manage your API keys within the **Profile** section of your [urlscan.io account](https://urlscan.io/user/login/).

## Integration parameters

The **urlscan.io** integration requires the following parameters:

Parameter | Description  
---|---  
`Api Key` | Required. The unique API key used to authenticate with the urlscan.io service.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the UrlScan.io server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### URL Check

Submit a URL to be scanned and get the scan details.

#### Parameters

**Parameter Name** | **Type** | **Is Mandatory** | **Default Value** | **Description**  
---|---|---|---|---  
Visibility | DDL  
possible:  
public, unlisted, private.  | No | public | Scans on [urlscan.io](http://urlscan.io/) have one of three visibility levels, make sure to use the appropriate level for your submission.  
Threshold | integer | No | -1 | Mark entity as suspicious if the score of verdicts is equal or above the given threshold. Default is -1, in this case, we consider every scanned url as suspicious.  
Create Insight | Boolean | No | Yes | If enabled, action will create an insight containing information about entities.  
Only Suspicious Insight | Boolean | No | No | If enabled, action will only create insight for suspicious entities. Note: "Create Insight" parameter needs to be enabled.  
Add Screenshot To Insight | Boolean | No | No | If enabled, action will add a screenshot of the website to the insight, if it's available.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Domain
  * URL



#### Action Results

##### Entity Enrichment

**Name** | **Key**  
---|---  
real_url | tasks/url  
visibility | visibility  
requests_count | len(data/requests)  
cookies | CSV of data/cookies/name  
related_links | CSV of data/links/href  
main_country | page/country  
main_domain | page/domain  
main_ip | page/ip  
main_asn | page/asnname  
main_server | page/server  
related_ips_count | len(lists/ips)  
related_domains_count | len(lists/domains)  
related_countries | CSV lists/countries  
overall_score | verdicts/overall/score  
categories | verdicts/overall/categories  
tags | verdicts/overall/tags  
malicious | verdicts/overall/malicious  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "Entity": "https://example.com",
            "EntityResult": {
                "lists": {
                    "ips": [
                        "0.0.0.0"
                    ],
                    "countries": [
                        "ZZ"
                    ],
                    "asns": [
                        "00000"
                    ],
                    "domains": [
                        "subdomain.example.com"
                    ],
                    "servers": [
                        "GenericServer/1.0.0"
                    ],
                    "urls": [
                        "https://example.com/",
                        "https://example.com/assets/image.png",
                        "https://example.com/assets/script.js",
                        "https://example.com/assets/style.svg",
                        "https://example.com/favicon.ico"
                    ],
                    "linkDomains": [
                        "node1.example.com",
                        "node2.example.com",
                        "node3.example.com"
                    ],
                    "certificates": [
                        {
                            "subjectName": "*.example.com",
                            "issuer": "CA-0",
                            "validFrom": 1000000000,
                            "validTo": 2000000000
                        }
                    ],
                    "hashes": [
                        "hash_string_alpha_001",
                        "hash_string_alpha_002",
                        "hash_string_alpha_003"
                    ]
                },
                "page": {
                    "asn": "AS00000",
                    "asnname": "PROVIDER - Service Provider Inc., ZZ",
                    "city": "",
                    "country": "ZZ",
                    "domain": "subdomain.example.com",
                    "ip": "0.0.0.0",
                    "ptr": "host.provider.net",
                    "server": "GenericServer/1.0.0",
                    "url": "https://example.com/",
                    "apexDomainAgeDays": 1,
                    "mimeType": "application/octet-stream",
                    "title": "Title Placeholder",
                    "tlsValidDays": 0,
                    "tlsAgeDays": 0,
                    "domainAgeDays": 1,
                    "tlsValidFrom": "2000-01-01T00:00:00.000Z",
                    "umbrellaRank": 0,
                    "apexDomain": "example.com",
                    "tlsIssuer": "CA-0",
                    "status": "000"
                },
                "scanner": {
                    "country": "zz"
                },
                "stats": {
                    "IPv6Percentage": 0,
                    "adBlocked": 0,
                    "malicious": 0,
                    "securePercentage": 0,
                    "secureRequests": 0,
                    "totalLinks": 0,
                    "uniqCountries": 0
                },
                "submitter": {
                    "country": "ZZ"
                },
                "task": {
                    "method": "system",
                    "source": "source_id",
                    "time": "2000-01-01T00:00:00.000Z",
                    "url": "https://example.com/",
                    "uuid": "00000000-0000-0000-0000-000000000000",
                    "visibility": "private",
                    "reportURL": "https://service.io/result/id/",
                    "screenshotURL": "https://service.io/screen/id.png",
                    "domURL": "https://service.io/dom/id/",
                    "domain": "subdomain.example.com",
                    "apexDomain": "example.com"
                },
                "verdicts": {
                    "overall": {
                        "score": 0,
                        "categories": [],
                        "brands": [],
                        "tags": [],
                        "malicious": false,
                        "hasVerdicts": false
                    },
                    "service_provider": {
                        "score": 0,
                        "categories": [],
                        "brands": [],
                        "tags": [],
                        "malicious": false,
                        "hasVerdicts": false
                    },
                    "engines": {
                        "score": 0,
                        "malicious": false,
                        "categories": [],
                        "enginesTotal": 0,
                        "maliciousTotal": 0,
                        "benignTotal": 0,
                        "maliciousVerdicts": [],
                        "benignVerdicts": [],
                        "hasVerdicts": false,
                        "tags": [
                            "tag-alpha",
                            "tag-beta"
                        ]
                    },
                    "community": {
                        "score": 0,
                        "categories": [],
                        "brands": [],
                        "votesTotal": 0,
                        "votesMalicious": 0,
                        "votesBenign": 0,
                        "malicious": false,
                        "hasVerdicts": false
                    }
                },
                "is_risky": false
            }
        }
    ]
    

### Search For Scans

Search for [urlscan.io](http://urlscan.io/) existing scans by attributes such as domains, IPs, Autonomous System (AS) numbers, hashes, etc. The action will find **public** scans performed by anyone as well as **unlisted** and **private** scans performed by you or your teams.

#### Parameters

**Parameter Name** | **Type** | **Is Mandatory** | **Default Value** | **Description**  
---|---|---|---|---  
Max Scans | Integer | No | 100 | Number of scans to return per entity. Default: 100, Max: 10000 (depending on subscription).  
  
#### Run On

This action runs on the following entities:

  * IP address
  * Hostnames
  * URLs
  * Filename
  * Hashes
  * Domain



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {"entity_identifier": "www.unitedneighborsfcu.com",
    "entity_results":[
      {
            "indexedAt": "2020-12-09T12:16:43.329Z",
            "task": {
                "visibility": "public",
                "method": "automatic",
                "domain": "www.unitedneighborsfcu.com",
                "time": "2020-12-09T12:16:23.168Z",
                "source": "certstream-suspicious",
                "uuid": "96310829-fed4-4d61-9fb0-39eb2952719f",
                "url": "https://www.unitedneighborsfcu.com"
            },
            "stats": {
                "uniqIPs": 6,
                "consoleMsgs": 0,
                "uniqCountries": 3,
                "dataLength": 1938842,
                "encodedDataLength": 1568193,
                "requests": 28
            },
            "page": {
                "country": "US",
                "server": "Microsoft-IIS/10.0",
                "domain": "www.unitedneighborsfcu.com",
                "ip": "8.21.114.55",
                "mimeType": "text/html",
                "asnname": "LEVEL3, US",
                "asn": "AS3356",
                "url": "https://www.unitedneighborsfcu.com/",
                "status": "200"
            },
            "_id": "96310829-fed4-4d61-9fb0-39eb2952719f",
            "sort": [1607516183168, "96310829-fed4-4d61-9fb0-39eb2952719f"],
            "result": "https://urlscan.io/api/v1/result/96310829-fed4-4d61-9fb0-39eb2952719f/",
            "screenshot": "https://urlscan.io/screenshots/96310829-fed4-4d61-9fb0-39eb2952719f.png"
      }
      ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if find scans for some of the entities (is_success = true):** print "Successfully listed scans for the following entities:\n".format(entity.identifier)
  * **If didn't find scans for some of the entities (is_success = true):** print "Action wasn't able to list scans for the following entities:\n".format(entity.identifier)
  * **If didn't find scans for all of the entities(is_success = false):** print "Action wasn't able to list scans for the available entities".
  * **If no entities:** print "No suitable entities were found in the current scope.  
  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** __print "Error executing action "Search for Scans". Reason: {0}''.format(error.Stacktrace).

| General  
Case Wall Table | **Title** : "{entity identifier} - Search Results"**Columns:** Scan IDURLScan DateSizeIPSUnique CountriesCountryScan Type | General  
Case Wall Link | **Title:** "[urlscan.io](http://urlscan.io/) Web Report + (entity ID). | General  
Case Wall attachment | Will contain the screenshot. | General  
  
### Get Scan Full Details

Get Scan Full Details by scan ID

#### Parameters

**Parameter Name** | **Type** | **Is Mandatory** | **Default Value** | **Description**  
---|---|---|---|---  
Scan ID | String | Yes | N/A | Get scan report using the scan ID. Comma-separated values.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    ['Effective URL'] = response['page']['url']
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if find some scan ids (is_success = true):** print "Successfully fetched results for the following scans: {scan ids}
  * **If didn't find some (is_success = true):** print "Action wasn't able to fetch results for the following scans: {scan ids}
  * **If didn't find all (is_success = false):** print "Action wasn't able to fetch results. The provided scan ids are not available using [urlscan.io](http://urlscan.io/)"

**The action should fail and stop a playbook execution:**

  * **if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Scan Full Details". Reason: {0}''.format(error.Stacktrace)

| General  
Case Wall link | **Title:** "[urlscan.io](http://urlscan.io/) Web Report + (Scan ID). | General  
Case Wall attachment | Will contain the screenshot. | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
