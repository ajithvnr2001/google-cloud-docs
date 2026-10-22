---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/urlvoid/
title: URLVoid \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:57.119977+00:00
---

# URLVoid  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/urlvoid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# URLVoid

This document provides guidance on how to integrate URLVoid with Google SecOps.

## Configure URLVoid to work with Google Security Operations

### API

For configuring URLVoid to work with Google SecOps, the process is the same as for APIVoid.

  1. To obtain your personal API Key, please sign in to your [APIVoid account](https://app.apivoid.com/login/).

  2. Click on the one of the two **My API Keys** buttons to get to the page where is your API key stored.

  3. Once you get to the page with relevant key, click the **copy** button to copy your key to the clipboard, which will be later used in this integration configuration with Google SecOps.




### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure URLVoid integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get domain reputation

#### Description

Check if a domain is blacklisted by a popular and trusted domain blacklist services. The multiple domain blacklist services are used in order to better identify potentially malicious and fraudulent websites involved in malware distribution, phishing incidents, and fake online shops.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Threshold | String | 0 | Domain risk threshold.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * URL



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
alexa_top_100k | Returns if it exists in JSON result  
domain_length | Returns if it exists in JSON result  
alexa_top_10k | Returns if it exists in JSON result  
blacklists | Returns if it exists in JSON result  
scantime | Returns if it exists in JSON result  
detection_rate | Returns if it exists in JSON result  
detections | Returns if it exists in JSON result  
engines_count | Returns if it exists in JSON result  
engines | Returns if it exists in JSON result  
engine | Returns if it exists in JSON result  
detected | Returns if it exists in JSON result  
confidence | Returns if it exists in JSON result  
reference | Returns if it exists in JSON result  
region_name | Returns if it exists in JSON result  
reverse_dns | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
isp | Returns if it exists in JSON result  
continent_code | Returns if it exists in JSON result  
latitude | Returns if it exists in JSON result  
city_name | Returns if it exists in JSON result  
longitude | Returns if it exists in JSON result  
country_code | Returns if it exists in JSON result  
country_name | Returns if it exists in JSON result  
continent_name | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "alexa_top_100k": false,
                "domain_length": 17,
                "alexa_top_10k": false,
                "blacklists": {
                    "scantime": "0.07",
                    "detection_rate": "0%",
                    "detections": 0,
                    "engines_count": 29,
                    "engines":
                    [
                        {
                            "engine": "ThreatLog",
                            "detected": false,
                            "confidence": "high",
                            "reference": "http://www.threatlog.com/"
                        }, {
                            "engine": "Threat Sourcing",
                            "detected": false,
                            "confidence": "high",
                            "reference":"https://www.threatsourcing.com/"
                        }, {
                            "engine": "URLVir",
                            "detected": false,
                            "confidence": "high",
                            "reference": "http://www.urlvir.com/"
                        }
                    ]
                },
                "server":
                {
                    "region_name": null,
                    "reverse_dns": "",
                    "ip": "",
                    "isp": null,
                    "continent_code": null,
                    "latitude": null,
                    "city_name": null,
                    "longitude": null,
                    "country_code": null,
                    "country_name": null,
                    "continent_name": null
                },
                "host": "qotaerltozres.com",
                "most_abused_tld": false,
                "alexa_top_250k": false
            },
            "Entity": "qotaerltozres.com"
        },
        "Entity": "1.1.1.1"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
