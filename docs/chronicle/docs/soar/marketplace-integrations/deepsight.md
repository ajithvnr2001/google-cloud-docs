---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/deepsight/
title: DeepSight \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:49.613940+00:00
---

# DeepSight  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/deepsight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DeepSight

This document describes how to integrate DeepSight with Google Security Operations.

## Configure DeepSight integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Ping

#### Description

Test Connectivity.

#### Parameters

This action runs on all entities.

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
null | True/False | null:False  
  
##### JSON Result
    
    
    N/A
    

### Scan Domain

#### Description

Scan a domain.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname
  * URL



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
domain | Returns if it exists in JSON result  
whitelisted | Returns if it exists in JSON result  
schemaVersion | Returns if it exists in JSON result  
whois | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
          "domain": "example.com",
          "whitelisted": true,
          "schemaVersion": 2,
          "whois":
            {
              "city": "Reno",
              "updated": "2014-04-30T00: 00: 00Z",
              "created": "1994-11-01T00: 00: 00Z",
              "nameServers": ["NS1.P31.DYNECT.NET",
                              "NS2.P31.DYNECT.NET",
                              "NS3.P31.DYNECT.NET"],
              "country": "Us",
              "expires": "2022-10-31T00: 00: 00Z",
              "person": "Hostmaster,AmazonLegalDept.",
              "registrar": "MarkmonitorInc.",
              "postalCode": "89507",
            "organization": "AmazonTechnologies,Inc.",
              "email":"john_doe@example.com"
             }
          },
      "Entity": "example.com"
    }]
    

### Scan Email

#### Description

Scan an email.

#### Parameters

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
date | Returns if it exists in JSON result  
title | Returns if it exists in JSON result  
uri | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          {
           "date": "2015-04-27T01:10Z",
           "title": "Laziok Trojan Activity and Infrastructure\\u2014January to April 2015",
           "uri": "/v1/mati/reports/300156",
           "id": 300156
          },
       "Entity": "john_doe@example.com"
    }]
    

### Scan File Name

#### Description

Scan the name of the that was involved in an event.

#### Parameters

N/A

#### Run On

This action runs on the Filename entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
date | Returns if it exists in JSON result  
title | Returns if it exists in JSON result  
uri | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | True/False | null:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
           "date": "2015-04-27T01:10Z",
           "title": "Laziok Trojan Activity and Infrastructure\\u2014January to April 2015",
           "uri": "/v1/mati/reports/300156",
           "id": 300156
         },
       "Entity": "BadGuy1"
    }]
    

### Scan Hash

#### Description

Scan a hash.

#### Parameters

N/A

#### Run On

This action runs on the Filename entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
matiReports | Returns if it exists in JSON result  
intelligence | Returns if it exists in JSON result  
detection_name | Returns if it exists in JSON result  
Activity | Returns if it exists in JSON result  
schemaVersion | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
events | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
reputation | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          {
            "matiReports":
               [{
                  "date": "2015-04-27T01:10:47Z",
                  "title": "Laziok Trojan Activity and Infrastructure\\u2014January to April 2015",
                  "uri": "/v1/mati/reports/300156",
                  "id": 300156
                }],
            "intelligence":
          {
            "countries": ["kor", "Gtm","are"],
            "paths": ["CSIDL_PROFILE\\\\appdata\\\\local\\\\searchlike"],
            "fileNames": ["SEARCHLIKE.EXE"],
            "parentProcesses": ["f8403ce30c3a2a42b4604c2cf952533ed828a3d7bdb289b0cec82b8844a72a5a"],
            "filesCreated": [{"path": "CSIDL_PROFILE\\\\appdata\\\\local\\\\searchlike",
                              "sha256": "6d873e6198f7aca685b4c697dfbf82e3450ed5277c5f3c55b1b6fb0338521e0f",
                              "fileName": "B_SEARCHLIKEEX.EXE"
                             }]
            },
       "detection_name": "Trojan.Mdropper",
       "Activity":
           {
             "dns": [{"type": "A",
                      "target": "acroipm2.adobe.com"}],
             "urls": [{"url":
    "http://acroipm.adobe.com/assets/102.zip"}]
            },
       "schemaVersion": 3,
       "sha256": "e46d5472e49793017892cb18a0aa174ff9c5b79cec0a9451f1b70e21b19855c2",
       "events":
           [{
              "pid": 2528,
              "type": "PROCESS:CURRENT",
              "target": "C:\\\\Windows\\\\SysWOW64\\\\cmd.exe",
              "severity": 1,
              "details": "B41859D39D786D32B23A9D2E00F4011DEC7A02402AE"
            }],
        "md5": "a77e89bf60e931477f5858a004fb5e0a",
        "reputation": "Malicious"
         },
      "Entity": "a77e89bf60e931477f5858a004fb5e0a"
    }]
    

### Scan IP

#### Description

Scan an IP address.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
geolocation | Returns if it exists in JSON result  
Network | Returns if it exists in JSON result  
targetIndustries | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
whitelisted | Returns if it exists in JSON result  
behaviours | Returns if it exists in JSON result  
targetCountries | Returns if it exists in JSON result  
lastSeen | Returns if it exists in JSON result  
urls | Returns if it exists in JSON result  
domains | Returns if it exists in JSON result  
Organization | Returns if it exists in JSON result  
schemaVersion | Returns if it exists in JSON result  
firstSeen | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
        "EntityResult":
          {
            "geolocation":
                {
                  "latitude": 39.91176055,
                  "city": "Beijing",
                  "longitude": 116.3792325,
                  "country": "China"
                 },
            "Network":
                {
                  "carrier": "ChinaUnicomBeijingProvinceNetwork",
                  "asn": 4808,
                  "lineSpeed": "High",
                  "ipRouting": "Fixed"
                },
            "targetIndustries":
                [{
                  "name": "Utilities",
                  "naics": 221
                 },{
                  "name": "Telecommunications",
                  "naics": 517
                }],
            "ip": "1.1.1.1",
            "whitelisted": false,
            "behaviours":
                [{
                   "behaviour": "Attacks",
                   "type": "WWWAttacks",
                   "description": "FakeBrowserUpdate"
                }],
            "targetCountries": ["fra", "tur", "twn"],
            "lastSeen": "2019-01-20T00: 00: 00Z",
            "urls":
                [{
                  "url": "http: //iremedypro.com/assets/img/jQuery/014/LOGS/c1dabc02e7c9c23688fcdccb9c94379f",
                  "uri": "/v1/urls/http: //iremedypro.com/assets/img/jQuery/014/LOGS/c1dabc02e7c9c23688fcdccb9c94379f"
                }],
            "domains":
                [{
                  "domain": "iremedypro.com",
                  "uri": "/v1/domains/iremedypro.com"
                }],
            "Organization":
                 {
                  "isic": "J6110",
                  "type": "InternetServiceProvider",
                  "name": "ChinaUnicomBeijingProvinceNetwork",
                   "naics": 517110
                   },
           "schemaVersion": 2,
           "firstSeen": "2016-01-01T00: 00: 00Z"
          },
       "Entity": "1.1.1.1"
     }]
    

### Scan URL

#### Description

Scan a URL.

#### Parameters

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
url | Returns if it exists in JSON result  
host | Returns if it exists in JSON result  
whitelisted | Returns if it exists in JSON result  
schemaVersion | Returns if it exists in JSON result  
whois | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
        "EntityResult":
           {
             "url": "https: //www.facebook.com",
             "host":
                {
                  "domain": "facebook.com",
                  "uri": "/v1/domains/facebook.com"
                },
             "whitelisted": true,
             "schemaVersion": 2,
             "whois":
                 {
                   "city": "MenloPark",
                   "updated": "2015-08-25T00: 00: 00Z",
                   "created": "1997-03-29T00: 00: 00Z",
                   "nameServers": ["A.NS.FACEBOOK.COM", "B.NS.FACEBOOK.COM"],
                   "country": "Us",
                   "expires": "2020-03-30T00: 00: 00Z",
                   "person": "DomainAdministrator",
                   "registrar": "MarkmonitorInc.",
                   "postalCode": "94025",
                   "organization": "Facebook,Inc.",
                   "email": "john_doe@example.com"
                  }
            },
       "Entity": "https: //www.facebook.com"
     }]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
