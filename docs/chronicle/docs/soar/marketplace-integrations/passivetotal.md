---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/passivetotal/
title: PassiveTotal \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:46:38.750739+00:00
---

# PassiveTotal  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/passivetotal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PassiveTotal

**Important:** PassiveTotal Community product was replaced by Microsoft Defender Threat Intelligence.

This document provides guidance on how to integrate PassiveTotal with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/PassiveTotal.zip).

## Configure PassiveTotal to work with Google Security Operations

### Credentials

For more information about how to obtain API keys, see [Getting Started with RiskIQ Community API](https://api.riskiq.net/api/pt_started.html).

### Network

**Function** | **Default Port** | **Direction** | **Protocol**  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure PassiveTotal integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Ping

#### Description

Test connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### WhoIs Address Reputation

#### Description

Request an address reputation from RiskIQ.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
results | Returns if it exists in JSON result  
totalRecords | Returns if it exists in JSON result  
queryValue | Returns if it exists in JSON result  
pager | Returns if it exists in JSON result  
queryType | Returns if it exists in JSON result  
firstSeen | Returns if it exists in JSON result  
lastSeen | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Entity:Result | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
        "EntityResult": {
            "results": [{
                "recordHash": "1cb21131ee1c1be14c862d446d149d43296fa8bfa9678374f25ea9ab3c38b777",
                "resolve": "com-abhut.cricket",
                "recordType": "A",
                "resolveType": "domain",
                "value": "1.1.1.1",
                "source": ["virustotal"],
                "lastSeen": "2015-11-09 00:00:00",
                "collected": "2015-11-09 00:00:00",
                "firstSeen": "2015-11-09 00:00:00"
            }],
            "totalRecords": 6912,
            "queryValue": "1.1.1.1",
            "pager": "None",
            "queryType": "ip",
            "firstSeen": "1970-01-01 00:00:00",
            "lastSeen": "2019-01-24 09:43:20"
        },
            "Entity": "1.1.1.1"
        }
    ]
    

### WhoIs Scan Address

#### Description

RiskIQ address WHOIS query.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
contactEmail | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
billing | Returns if it exists in JSON result  
admin | Returns if it exists in JSON result  
text | Returns if it exists in JSON result  
registered | Returns if it exists in JSON result  
lastLoadedAt | Returns if it exists in JSON result  
whoisServer | Returns if it exists in JSON result  
telephone | Returns if it exists in JSON result  
registryUpdatedAt | Returns if it exists in JSON result  
nameServers | Returns if it exists in JSON result  
tech | Returns if it exists in JSON result  
organization | Returns if it exists in JSON result  
registrar | Returns if it exists in JSON result  
zone | Returns if it exists in JSON result  
registrant | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Entity:Result | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "contactEmail": "john_doe@example.com",
                "domain": "1.1.1.1",
                "name": "N/A",
                "billing": {},
                "admin": {
                    "organization": "Abuse",
                    "email": "john_doe@example.com",
                    "telephone": "1-650-253-0000"
                },
                "text": "IANA WHOIS server for more information on IANA.",
                "registered": "2014-03-14T00:00:00.000-0700",
                "lastLoadedAt": "2018-06-22T10:35:52.694-0700",
                "whoisServer": "whois.arin.net",
                "telephone": "N/A",
                "registryUpdatedAt": "1991-11-02T00:00:00.000-0800",
                "nameServers": [],
                "tech": {
                    "organization": "test LLC",
                    "email": "john_doe@example.com",
                    "telephone": "1-650-253-0000"
                },
                "organization": "test LLC",
                "registrar": "Administered by ARIN",
                "zone": {},
                "registrant": {
                    "city": "Mountain View",
                    "country": "US",
                    "state": "CA",
                    "street": "1600 Amphitheatre Parkway",
                    "postalCode": "94043",
                    "organization": "test LLC"
                }},
            "Entity": "1.1.1.1"
        }
    ]
    

### WhoIs Scan Domain

#### Description

RiskIQ domain WHOIS query.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
domain | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
billing | Returns if it exists in JSON result  
admin | Returns if it exists in JSON result  
text | Returns if it exists in JSON result  
registered | Returns if it exists in JSON result  
lastLoadedAt | Returns if it exists in JSON result  
whoisServer | Returns if it exists in JSON result  
telephone | Returns if it exists in JSON result  
registryUpdatedAt | Returns if it exists in JSON result  
nameServers | Returns if it exists in JSON result  
expiresAt | Returns if it exists in JSON result  
tech | Returns if it exists in JSON result  
organization | Returns if it exists in JSON result  
registrar | Returns if it exists in JSON result  
zone | Returns if it exists in JSON result  
registrant | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Entity:Result | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "domain": "example.com",
                "name": "N/A",
                "billing": {},
                "admin": {},
                "text": "Domain Name: test.COM   Registry Domain ID: 2138514_DOMAIN_COM-VRSN.",
                "registered": "1997-09-14T21:00:00.000-0700",
                "lastLoadedAt": "2018-10-01T15:38:19.795-0700",
                "whoisServer": "whois.markmonitor.com",
                "telephone": "N/A",
                "registryUpdatedAt": "2018-02-21T10:36:40.000-0800",
                "nameServers": ["ns1.example.com", "ns2.example.com", "ns3.example.com"],
                "expiresAt": "2020-09-13T21:00:00.000-0700",
                "tech": {},
                "organization": "N/A",
                "registrar": "MarkMonitor Inc.",
                "zone": {},
                "registrant": {
                }},
            "Entity": "example.com"
        }
    ]
    

### WhoIs Host Reputation

#### Description

Request host reputation from RiskIQ.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
results | Returns if it exists in JSON result  
totalRecords | Returns if it exists in JSON result  
queryValue | Returns if it exists in JSON result  
pager | Returns if it exists in JSON result  
queryType | Returns if it exists in JSON result  
firstSeen | Returns if it exists in JSON result  
lastSeen | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Entity:Result | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "results": [
                    {
                        "recordHash": "0aad10e23953813834d28098db21c0902f01190c3eba7e38869f798ca56abda7",
                        "resolve": "1.1.1.1",
                        "recordType": "A",
                        "resolveType": "ip",
                        "value": "example.com",
                        "source": ["riskiq"],
                        "lastSeen": "2013-09-12 13:08:07",
                        "collected": "2019-01-24 12:36:12",
                        "firstSeen": "2013-09-12 13:08:07"
                    }],
                "totalRecords": 5099,
                "queryValue": "example.com",
                "pager": "None",
                "queryType": "domain",
                "firstSeen": "2009-09-01 19:59:32",
                "lastSeen": "2019-01-24 12:36:11"
            },
            "Entity": "example.com"
        }
    ]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
