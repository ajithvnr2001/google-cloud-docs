---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/dshield/
title: DShield \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:56:11.690938+00:00
---

# DShield  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/dshield/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DShield

This document describes how to integrate DShield with Google Security Operations.

## Configure DShield integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get IP Info

#### Description

Query DShield for information about external IP addresses.

#### Parameters

N/A

#### Run On

This action runs on the IP Address.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
comment | Returns if it exists in JSON result  
count | Returns if it exists in JSON result  
updated | Returns if it exists in JSON result  
Alexa | Returns if it exists in JSON result  
network | Returns if it exists in JSON result  
attacks | Returns if it exists in JSON result  
maxdate | Returns if it exists in JSON result  
asname | Returns if it exists in JSON result  
assize | Returns if it exists in JSON result  
number | Returns if it exists in JSON result  
maxrisk | Returns if it exists in JSON result  
as | Returns if it exists in JSON result  
asabusecontact | Returns if it exists in JSON result  
ascountry | Returns if it exists in JSON result  
threatfeeds | Returns if it exists in JSON result  
mindate | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_enriched | True/False | is_enriched:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
        {
          "comment": "Googlepublicrecursivenameserver",
          "count": 8218,
          "updated": "2019-01-2004: 51: 46",
          "Alexa":
            {
             "domains": 1,
             "lastrank": 6178,
             "hostname": "google-public-dns-a.google.com",
             "lastseen": "2016-01-02",
             "firstseen": "2016-01-02"
            },
          "network": "1.1.1.1/24",
          "attacks": 32,
          "maxdate": "2019-01-20",
          "asname": "GOOGLE-GoogleLLC",
          "assize": 609498,
          "number": "1.1.1.1",
          "maxrisk": 0,
          "as": 15169,
          "asabusecontact": "john_doe@example.com",
          "ascountry": "US",
          "threatfeeds":
            {
              "qakbot":
                 {
                   "lastseen": "2015-04-03",
                   "firstseen": "2015-04-02"
                 },
              "forumspam":
                 {
                  "lastseen": "2018-12-05",
                  "firstseen": "2011-05-10"
                  }
             },
           "mindate": "2019-01-14"
         },
      "Entity": "1.1.1.1"
    }]​
    

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
