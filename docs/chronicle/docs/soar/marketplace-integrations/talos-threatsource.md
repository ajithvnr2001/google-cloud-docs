---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/talos-threatsource/
title: Talos ThreatSource \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:48:23.765861+00:00
---

# Talos ThreatSource  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/talos-threatsource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Talos ThreatSource

This document provides guidance on how to integrate Talos ThreatSource with Google SecOps.

## Configure Talos ThreatSource integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Reputation

#### Description

Get the reputation and details of an IP Address or a domain.

#### Parameters

This action has no input parameters.

#### Use cases

This action has no use cases.

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname
  * URL



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "1.1.1.1": {
                    "reputation": {
                        "domain": "one.one.one",
                        "daychange": 43.0,
                        "web_score": "",
                        "ip": "1.1.1.1",
                        "dnsmatch": 1,
                        "display_ipv6_volume": "false",
                        "daily_spam_name": "None",
                        "daily_spam_level": 0,
                        "category": {
                            "description": "Infrastructure and Content Delivery Networks",
                            "long_description": "Content delivery infrastructure and dynamically generated content; websites that cannot be classified more specifically because they are secured or otherwise difficult to classify."
                        },
                        "daily_mag": 3.8307894844544057,
                        "monthly_spam_level": 0,
                        "hostname": "one.one.one.one",
                        "monthly_spam_name": "None",
                        "talos_url": "https://www.talosintelligence.com/reputation_center/lookup?search=1.1.1.1",
                        "blacklists": {
                            "cbl.abuseat.org": {
                                "rules": [],
                                "lookup_uri": "http://cbl.abuseat.org/lookup.cgi?ip=1.1.1.1"
                            },
                            "pbl.spamhaus.org": {
                                "rules": [],
                                "lookup_uri": "http://www.spamhaus.org/query/bl?ip=1.1.1.1"
                            },
                            "sbl.spamhaus.org": {
                                "rules": [],
                                "lookup_uri": "http://www.spamhaus.org/query/bl?ip=1.1.1.1"
                            },
                            "bl.spamcop.net": {
                                "rules": [],
                                "lookup_uri": "http://spamcop.net/w3m?action=checkblock&ip=1.1.1.1"
                            }},
                        "talos_blacklist": {
                            "entry": {
                                "first_seen": "2013-04-10T10:05:01",
                                "classifications": ["malware"],
                                "expiration": "2014-12-17T19:09:58"
                            }},
                        "cidr": "false",
                        "email_score": "",
                        "email_score_name": "Good",
                        "web_score_name": "Neutral",
                        "organization": "CloudFlare",
                        "monthly_mag": "3.692884173719037"
                    },
                    "location": {
                        "map": "null",
                        "country": "Australia",
                        "locations": [{
                            "latitude": -33.494,
                            "ips": {
                                "good": [{
                                    "ip": "1.1.1.1",
                                    "magnitude": 3.692884173719037
                                }]},
                            "longitude": 143.2104
                        }],
                        "country_code": "AU",
                        "country_flag": "/images/flags/AU.png",
                        "cities": [{
                            "country": "Australia",
                            "name": "NULL",
                            "country_code": "AU",
                            "country_flag": "/images/flags/AU.png"
                        }]}}},
            "Entity": "test"
        }
    ]
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Talos_reputation | Returns if it exists in JSON result  
Talos_domain | Returns if it exists in JSON result  
Talos_daychange | Returns if it exists in JSON result  
Talos_web_score | Returns if it exists in JSON result  
Talos_ip | Returns if it exists in JSON result  
Talos_dnsmatch | Returns if it exists in JSON result  
Talos_display_ipv6_volume | Returns if it exists in JSON result  
Talos_daily_spam_name | Returns if it exists in JSON result  
Talos_daily_spam_level | Returns if it exists in JSON result  
Talos_category | Returns if it exists in JSON result  
Talos_description | Returns if it exists in JSON result  
Talos_daily_mag | Returns if it exists in JSON result  
Talos_monthly_spam_level | Returns if it exists in JSON result  
Talos_hostname | Returns if it exists in JSON result  
Talos_monthly_spam_name | Returns if it exists in JSON result  
Talos_url | Returns if it exists in JSON result  
Talos_blacklists | Returns if it exists in JSON result  
Talos_rules | Returns if it exists in JSON result  
Talos_lookup_uri | Returns if it exists in JSON result  
Talos_idr | Returns if it exists in JSON result  
Talos_email_score | Returns if it exists in JSON result  
Talos_email_score_name | Returns if it exists in JSON result  
Talos_web_score_name | Returns if it exists in JSON result  
Talos_organization | Returns if it exists in JSON result  
Talos_monthly_mag | Returns if it exists in JSON result  
Talos_location | Returns if it exists in JSON result  
Talos_magnitude | Returns if it exists in JSON result  
Talos_longitude | Returns if it exists in JSON result  
Talos_country_code | Returns if it exists in JSON result  
Talos_country_flag | Returns if it exists in JSON result  
Talos_cities | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success = true):_ "Successfully enriched the following entities using information from Talos ThreatSource: {entity.identifier}".___If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Talos ThreatSource: {entity.identifier}". _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Reputation". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity.identifier} **Table** **Columns:**

  * Key
  * Value

| Entity  
  
### Ping

#### Description

Verifies that the user has a connection to Talos ThreatSource through the user's device.

#### Parameters

This action has no input parameters.

#### Use cases

This action has no use cases.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### WhoIs

#### Description

Retrieve Whois information about entities using Talos ThreatSource.

**Note:** This action takes the domain part from the URL entities.

#### Parameters

This action has no input parameters.

#### Use cases

This action has no use cases.

#### Run On

This action runs on the IP Address, Hostname, URL entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success = true):_ "Successfully returned Whois information about the following entities using information from Talos ThreatSource: {entity.identifier}"._If "error" is in the response for one entity (is_success=true):_ "Action wasn't able to return Whois information about the following entities using information from Talos ThreatSource: {entity.identifier}". ___If "error" is in the response (is_success=false):_ "No Whois information was found for the provided entities."**The action should fail and stop a playbook execution:******_If fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Whois". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
