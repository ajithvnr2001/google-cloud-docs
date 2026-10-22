---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/domaintools/
title: DomainTools \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:10.828066+00:00
---

# DomainTools  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/domaintools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DomainTools

This document describes how to integrate DomainTools with Google Security Operations.

## Configure DomainTools integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Domain Profile

#### Description

Enrich an external domain entity with DomainTools that threatens data from Intelligence and returns a CSV output.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * Domain



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
    
    
    [
        {
            "Entity": "example-domain.com",
            "EntityResult": {
                "registrant": {
                    "name": "Privacy Protect LLC",
                    "domains": 66370905,
                    "product_url": "https:\\/\\/reversewhois.domaintools.com\\/?all[]=Privacy+Protect+LLC&none[]="
                },
                "server": {
                    "ip_address": "192.0.2.1",
                    "other_domains": 1898,
                    "product_url": "https:\\/\\/reverseip.domaintools.com\\/search\\/?q=example-domain.com"
                },
                "registration": {
                    "created": "2024-01-15",
                    "expires": "2025-01-15",
                    "updated": "2024-10-22",
                    "registrar": "Example Registrar Co.",
                    "statuses": [
                        "clientDeleteProhibited",
                        "clientRenewProhibited",
                        "clientTransferProhibited",
                        "clientUpdateProhibited"
                    ]
                }
            }
        }
    ]
    

### Get Domain Risk

#### Description

Enrich the external domain entity with the domain risk score that was given by DomainTools data.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | String | N/A | Mark entity as suspicious if the domain risk score passes the given threshold. e.g. 3.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * Domain



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "Entity": "risky-example-one.com",
            "EntityResult": {
                "domain": "risky-example-one.com",
                "risk_score": 99,
                "components": [
                    {
                        "name": "proximity",
                        "risk_score": 70
                    },
                    {
                        "name": "threat_profile",
                        "risk_score": 99
                    },
                    {
                        "name": "threat_profile_phishing",
                        "risk_score": 99
                    },
                    {
                        "name": "threat_profile_malware",
                        "risk_score": 95
                    },
                    {
                        "name": "threat_profile_spam",
                        "risk_score": 0
                    }
                ]
            }
        },
        {
            "Entity": "high-risk-test.net",
            "EntityResult": {
                "domain": "high-risk-test.net",
                "risk_score": 99,
                "components": [
                    {
                        "name": "proximity",
                        "risk_score": 70
                    },
                    {
                        "name": "thre at_profile",
                        "risk_score": 99
                    },
                    {
                        "name": "threat_profile_phishing",
                        "risk_score": 99
                    },
                    {
                        "name": "threat_profile_malware",
                        "risk_score": 95
                    },
                    {
                        "name": "threat_profile_spam",
                        "risk_score": 0
                    }
                ]
            }
        }
    ]
    

### Get Hosting History

#### Description

Receive, enrich, and add a CSV table to the Domain Hosting History Information.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname



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
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname



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
    
    
    N/A
    

### Recent Domains

#### Description

Look for new domains with a specific word in them.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
String Query | String | N/A | Search for new domains containing a particular word.  
  
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
null | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Reverse Domain

#### Description

Find IPs pointing to a certain domain.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * Domain



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "Entity": "http://www.example-domain.com/",
            "EntityResult": {
                "ip_addresses": [
                    {
                        "ip_address": "192.0.2.10",
                        "domain_count": 2,
                        "domain_names": [
                            "malware-host.net",
                            "test-site-two.org"
                        ]
                    },
                    {
                        "ip_address": "192.0.2.11",
                        "domain_count": 1,
                        "domain_names": [
                            "another-test-domain.com"
                        ]
                    }
                ]
            }
        }
    ]
    

### Reverse Email

#### Description

Find domains with an email address in their WhoIs record.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Reverse IP

#### Description

Find domain names that share a particular IP address.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
