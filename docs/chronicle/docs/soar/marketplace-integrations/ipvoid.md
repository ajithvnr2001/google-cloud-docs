---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ipvoid/
title: IPVoid \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:27:23.543829+00:00
---

# IPVoid  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ipvoid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IPVoid

This document provides guidance on how to integrate IPVoid with Google SecOps.

## Configure IPVoid to work with Google Security Operations

### API

For configuring IPVoid to work with Google SecOps, the process is the same as for APIVoid.

  1. To obtain your personal API Key, please sign in to your [APIVoid account](https://app.apivoid.com/login/).

  2. Click on the one of the two **My API Keys** buttons to get to the page where is your API Key stored.

  3. Once you get to the page with relevant key, click the **copy** button to copy your key to the clipboard, which will be later used in this integration configuration with Google SecOps.




### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure IPVoid integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get IP Reputation

#### Description

Search for an IP address through different DNS-based blacklists (DNSBL) and the reputation services to promote the IP address identification for malware incidents and spamming.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Threshold | String | N/A | IP risk threshold.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
information | Returns if it exists in JSON result  
blacklists | Returns if it exists in JSON result  
anonymity | Returns if it exists in JSON result  
IP | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
successThreshold | True/False | successThreshold:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
        {
          "information":
             {
               "is_proxy": false,
               "is_vpn": false,
               "region_name": "Zhejiang",
               "is_webproxy": false,
               "latitude": 28.680280685424805,
               "isp": "ChinaNet Zhejiang Province Network",
               "continent_code": "AS",
               "is_tor": false,
               "reverse_dns": "",
               "detections": 18,
               "engines_count": 76,
               "longitude": 121.44277954101562,
               "city_name": "Jiaojiang",
               "country_name": "China",
               "continent_name": "Asia",
               "detection_rate": "24%",
               "country_code": "CN",
               "is_hosting": false
            },
          "blacklists":
            {
               "scantime": "0.57",
              "detection_rate": "24%",
              "detections": 18,
              "engines_count": 76,
              "engines":
                 [{
                    "engine": "PlonkatronixBL",
                    "detected": false,
                    "reference": "http://bl.plonkatronix.com/"
                  },
                  {
                    "engine": "Peter-s NUUG IP BL",
                    "detected": true,
                    "reference": "https://home.nuug.no/~peter/"
                   },
                  {
                    "engine": "Malc0de",
                    "detected": false,
                    "reference": "http://malc0de.com/database/index.php"
                   }]
             },
           "anonymity":
             {
               "is_tor": false,
               "is_proxy": false,
               "is_vpn": false,
               "is_webproxy": false,
               "is_hosting": false
              },
           "ip": "1.1.1.1"
         },
     "Entity": "1.1.1.1"
    }]
    

### Ping

#### Description

Test Connectivity.

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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### WhoIs

#### Description

Query the Whois database to find information on a given domain name or an IP address.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
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
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
