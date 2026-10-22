---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/xforce/
title: X-Force \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:22.905140+00:00
---

# X-Force  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/xforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# X-Force

This document provides guidance on how to integrate X-Force with Google SecOps.

## Configure X-Force to work with Google Security Operations

  1. To obtain your personal API key, please log in to the [IBM X-Force Exchange](https://www.ibm.com/links?url=https%3A%2F%2Fexchange.xforce.ibmcloud.com%2F) website with an active IBM ID.

  2. View your user profile on the upper right corner of your screen, and then go to the **Settings** page down below to create a new API key/password pair.

  3. On the Settings page, click **API Access** , then the **Generate** button in the API Key Generation section.




## Configure X-Force integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Hash Info

#### Description

Query X-Force for hash information.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | string | N/A | The value of the threshold can be: low, medium or high.  
  
#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
malware | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
  
##### Insights

If the risk score of the entity exceeds the threshold, then the Insight will be added to warn that the hash is marked as malware.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risk | True/False | is_risk:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "malware":
                {
                    "hash": "0x474B9CCF5AB9D72CA8A333889BBB34F0",
                    "family": ["tsunami"],
                    "origins":
                    {
                        "downloadServers": {},
                        "subjects": {},
                        "CnCServers":
                        {
                            "count": 1,
                            "rows":
                            [{
                                "count": 483,
                                "origin": "CnC",
                                "domain": "pc-guard.net",
                                "filepath": "v.html",
                                "ip": "1.1.1.1",
                                "uri": "http://pc-guard.net/v.html",
                                "lastseen": "2014-10-20T23:19:00Z",
                                "md5": "474B9CCF5AB9D72CA8A333889BBB34F",
                                "type": "CnC",
                                "firstseen": "2014-10-20T23:19:00Z",
                                "schema": "http"
                            }]},
                        "emails": {},
                        "external":
                        {
                            "detectionCoverage": 46,
                            "family": ["heuristic", "trojan"]
                        }},
                    "created": "2014-10-20T23:19:00Z",
                    "familyMembers":
                    {
                        "tsunami":
                        {
                            "count": 61
                        }},
                    "md5": "0x474B9CCF5AB9D72CA8A333889BBB34F0",
                    "type": "md5",
                    "risk": "high"
                },
                "tags": []
            },
            "Entity": "474B9CCF5AB9D72CA8A333889BBB34F0"
        }
    ]
    

### Get IP by Category

#### Description

Get IP by category.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Category | string | N/A | Category for IP.  
  
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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "ip": "string",
            "score": "integer",
            "created": "string"
        }
    ]
    

### Get IP Info

#### Description

Query X-Force for IP information.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | string | N/A | Threshold must be an integer (example: 3).  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Entities are marked as suspicious if they exceed Threshold. Otherwise: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
subnets | Returns if it exists in JSON result  
reasonDescription | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
reason | Returns if it exists in JSON result  
score | Returns if it exists in JSON result  
categoryDescriptions | Returns if it exists in JSON result  
cats | Returns if it exists in JSON result  
geo | Returns if it exists in JSON result  
history | Returns if it exists in JSON result  
  
##### Insights

If the risk score exceeds the threshold, add Insight and mark it as suspicious.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "subnets":
                [{
                    "subnet": "1.1.1.1/14",
                    "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                    "created": "2017-10-18T06:23:00.000Z",
                    "ip": "1.1.1.1",
                    "asns":
                    {
                        "8359":
                        {
                            "Company": "MTS, RU",
                            "cidr": 14
                        }},
                    "reason": "Regional Internet Registry",
                    "score": 1,
                    "categoryDescriptions": {},
                    "cats": {},
                    "geo":
                    {
                        "country": "Russia",
                        "countrycode": "RU"
                    }}, {
                        "subnet": "1.1.1.1/20",
                        "reasonDescription": "Based on statistical DNS analysis.",
                        "created": "2014-01-22T19:56:00.000Z",
                        "ip": "1.1.1.1",
                        "reason": "DNS heuristics",
                        "score": 1,
                        "categoryDescriptions":
                        {
                            "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                        },
                        "cats":
                        {
                            "Dynamic IPs": 71
                        }}],
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "tags": [],
                "ip": "1.1.1.1",
                "reason": "Regional Internet Registry",
                "score": 1,
                "categoryDescriptions":
                {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "cats":
                {
                    "Dynamic IPs": 71
                },
                "geo":
                {
                    "country": "Russia",
                    "countrycode": "RU"
                },
                "history":
                [{
                    "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                    "created": "2012-03-22T07:26:00.000Z",
                    "ip": "1.1.1.1/14",
                    "reason": "Regional Internet Registry",
                    "score": 1,
                    "categoryDescriptions": {},
                    "cats": {},
                    "geo":
                    {
                        "country": "Russia",
                        "countrycode": "RU"
                    }}, {
                        "reasonDescription": "Based on statistical DNS analysis.",
                        "created": "2012-04-13T13:34:00.000Z",
                        "ip": "1.1.1.1/14",
                        "reason": "DNS heuristics",
                        "score": 1,
                        "categoryDescriptions":
                        {
                            "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                        },
                        "cats":
                        {
                            "Dynamic IPs": 100
                        },
                        "geo":
                        {
                            "country": "Russia",
                            "countrycode": "RU"
                        }}, {
                            "reasonDescription": "Based on statistical DNS analysis.",
                            "created": "2014-01-22T19:56:00.000Z",
                            "ip": "1.1.1.1/20",
                            "reason": "DNS heuristics",
                            "score": 1,
                            "categoryDescriptions":
                            {
                                "Dynamic IPs\": "This category contains IP addresses of dialup hosts and DSL lines."
                            },
                            "cats":
                            {
                                "Dynamic IPs": 71
                            },
                            "geo":
                            {
                                "country": "Russia",
                                "countrycode": "RU"
                            }}]},
            "Entity": "1.1.1.1"
        }
    ]
    

### Get IP Malware

#### Description

Query X-Force for the malware associated with an IP address.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | string | N/A | Threshold must be an integer (example: 3).  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Entities are marked as suspicious if malware_count is bigger than 0.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
malware | Returns if it exists in JSON result  
  
##### Insights

Add a warning Insight that the entity was associated with malware and mark it as suspicious if malware_count > 0.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_malware | True/False | is_malware:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "malware":
                [{
                    "count": 13,
                    "origin": "CnC",
                    "domain": "l33t-milf.info",
                    "last": "2016-10-29T06:31:00Z",
                    "family": ["kasidet"],
                    "filepath": "dom/tasks.php",
                    "ip": "0x00000000000000000000ffff08080808",
                    "uri": "http://example.com/dom/tasks.php",
                    "first": "2016-10-29T06:31:00Z",
                    "host": "dom",
                    "lastseen": "2016-10-29T06:31:00Z",
                    "md5": "4C10F74CE20328B7CC4207245BC9D725",
                    "type": "CnC",
                    "firstseen": "2016-10-29T06:31:00Z",
                    "schema": "http"
                }]},
            "Entity": "1.1.1.1"
        }
    ]
    

### Get URL Info

#### Description

Query X-Force for URL information.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | string | N/A | Threshold must be an integer(example: 3).  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

Entities are marked as suspicious if they exceed threshold. Otherwise: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
associated | Returns if it exists in JSON result  
result | Returns if it exists in JSON result  
tags | Returns if it exists in JSON result  
  
##### Insights

Add a warning Insight and mark it as suspicious if the risk score exceeds threshold.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risk | True/False | is_risk:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "associated":
                [{
                    "url": "markossolomon.com",
                    "cats": {},
                    "score": null,
                    "categoryDescriptions": {}
                }],
                "result":
                {
                    "url": "markossolomon.com/f1q7qx.php",
                    "cats":
                    {
                        "Botnet Command and Control Server": true
                    },
                    "score": 10,
                    "categoryDescriptions":
                    {
                        "Botnet Command and Control Server": "This category contains Web sites or domains that host a botnet command and control server."
                    }},
                "tags": []
            },
            "Entity": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP"
        }
    ]
    

### Ping

#### Description

Test Connectivity to X-Force.

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
is_connected | True/False | is_connected:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
