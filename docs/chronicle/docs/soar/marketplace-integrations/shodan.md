---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/shodan/
title: Shodan \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:35.024658+00:00
---

# Shodan  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/shodan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Shodan

This document provides guidance on how to integrate Shodan with Google SecOps.

## ‌Configure Shodan Integration to work with Google Security Operations

To obtain the API Key, please complete the following steps:

  1. Log into your [Shodan account](https://account.shodan.io/login).

  2. You will find your API Key in the **Account Overview** section of the Shodan Interface.




## Configure Shodan integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### DNS Resolve

#### Description

Look up the IP address for the provided list of hostnames.

#### Parameters

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
google.com | Returns if it exists in JSON result  
bing.com | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "google.com": "1.1.1.1",
        "bing.com": "1.1.1.1"
    }
    

### DNS Reverse

#### Description

Look up the hostnames that have been defined for the given list of IP addresses.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
146.125.10.5 | Returns if it exists in JSON result  
8.8.8.8 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "146.125.10.5": null,
        "8.8.8.8": [
            "google-public-dns-a.google.com"
        ]
    }
    

### Get API Info

#### Description

Returns information about the API plan belonging to the given API key.

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
    
    
    {
        "https": false,
        "unlocked": false,
        "unlocked_left": 0,
        "telnet": false,
        "scan_credits": 0,
        "plan": "oss",
        "query_credits": 0
    }
    

### Get IP Info

#### Description

Get all available information on an IP.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Return Historical Banners | Boolean | false | True if all historical banners should be returned.  
Set Minify | Boolean | false | True to only return the list of ports and the general host information, no banners.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
data | Returns if it exists in JSON result  
_shodan | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
crawler | Returns if it exists in JSON result  
options | Returns if it exists in JSON result  
module | Returns if it exists in JSON result  
ptr | Returns if it exists in JSON result  
hash | Returns if it exists in JSON result  
opts | Returns if it exists in JSON result  
raw | Returns if it exists in JSON result  
isp | Returns if it exists in JSON result  
port | Returns if it exists in JSON result  
hostnames | Returns if it exists in JSON result  
location | Returns if it exists in JSON result  
city | Returns if it exists in JSON result  
country_name | Returns if it exists in JSON result  
region_code | Returns if it exists in JSON result  
area_code | Returns if it exists in JSON result  
dma_code | Returns if it exists in JSON result  
country_code3 | Returns if it exists in JSON result  
postal_code | Returns if it exists in JSON result  
longitude | Returns if it exists in JSON result  
country_code | Returns if it exists in JSON result  
latitude | Returns if it exists in JSON result  
resolver_hostname | Returns if it exists in JSON result  
recursive | Returns if it exists in JSON result  
resolver_id | Returns if it exists in JSON result  
software | Returns if it exists in JSON result  
timestamp | Returns if it exists in JSON result  
domains | Returns if it exists in JSON result  
org | Returns if it exists in JSON result  
os | Returns if it exists in JSON result  
asn | Returns if it exists in JSON result  
transport | Returns if it exists in JSON result  
ip_str | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "data": [
                    {
                        "_shodan": {
                            "id": "d670bfbb-4821-4320-969d-0590789ab502",
                            "crawler": "545144fc95e7a7ef13ece5dbceb98ee386b37950",
                            "options": {},
                            "module": "dns-udp",
                            "ptr": true
                        },
                        "hash": -553166942,
                        "opts": {
                            "raw": "34ef818200010000000000000756455253494f4e0442494e440000100003"
                        },
                        "ip": 134744072,
                        "isp": "Google",
                        "data": "nRecursion: enabled",
                        "port": 53,
                        "hostnames": ["google-public-dns-a.google.com"],
                        "location": {
                            "city": null,
                            "region_code": null,
                            "area_code": null,
                            "dma_code": null,
                            "country_code3": "USA",
                            "country_name": "United States",
                            "postal_code": null,
                            "longitude": -97.822,
                            "country_code": "US",
                            "latitude": 37.751000000000005
                        },
                        "dns": {
                            "resolver_hostname": null,
                            "recursive": true,
                            "resolver_id": null,
                            "software": null
                        },
                        "timestamp": "2019-01-29T12:36:09.300695",
                        "domains": ["google.com"],
                        "org": "Google",
                        "os": null,
                        "asn": "AS15169",
                        "transport": "udp",
                        "ip_str": "1.1.1.1"
                    }
                ],
                "city": null,
                "region_code": null,
                "tags": [],
                "ip": 134744072,
                "isp": "Google",
                "area_code": null,
                "dma_code": null,
                "last_update": "2019-01-29T12:36:09.300695",
                "country_code3": "USA",
                "country_name": "United States",
                "hostnames": ["google-public-dns-a.google.com"],
                "postal_code": null,
                "longitude": -97.822,
                "country_code": "US",
                "ip_str": "1.1.1.1",
                "latitude": 37.751000000000005,
                "org": "Google",
                "os": null,
                "asn": "AS15169",
                "ports": [53]
            },
            "Entity": "1.1.1.1"
        }
    ]
    

### Ping

#### Description

Verify that the user has a connection to Shodan via the user's device.

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
is_connected | True/False | is_connected:False  
  
##### JSON Result
    
    
    N/A
    

### Scan a Network

#### Description

Scan a network using Shodan. Shodan crawls the entire Internet at least once a month, but if you want to request Shodan to scan a network immediately, you can do so using the on-demand scanning capabilities of the API.

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
    

### Enable User

#### Description

Update user attribute - enable user.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
User Name | Int | N/A | Full user name as exist in the CyberArkVault.  
  
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
success_scan | True/False | success_scan:False  
  
##### JSON Result
    
    
    N/A
    

### Search

#### Description

Search the Shodan database.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Search Query | 0 | N/A | Search query; identical syntax to the website. e.g. find Apache webservers located in Germany(apache country:'DE', city:'Berlin').  
Facets | 0 | N/A | A comma-separated list of properties to get summary information on. Property names can also be in the format of 'property:count'. (i.e. country:100, city:5). More information can be found at <https://developer.shodan.io/api>.  
Set Minify | 1 | false | Whether to minify the banner and only return the important data.  
  
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
    
    
    {
        "matches": [
            {
                "timestamp": "2014-01-15T05: 49: 56.283713",
                "isp": "Vivacom",
                "data": "@PJL INFO STATUS CODE=35078 DISPLAY=Power Saver ONLINE=TRUE",
                "port": 9100,
                "hostnames": [],
                "location": {
                    "city": null,
                    "region_code": null,
                    "area_code": null,
                    "longitude": 25,
                    "country_code3": "BGR",
                    "country_name": "Bulgaria",
                    "postal_code": null,
                    "dma_code": null,
                    "country_code": "BG",
                    "latitude": 43
                },
                "ip": 3579573318,
                "domains": [],
                "org": "Vivacom",
                "os": null,
                "asn": "AS8866",
                "ip_str": "1.1.1.1"
            }
        ],
        "facets": {
            "org": [
                {
                    "count": 107,
                    "value": "UniversityofMinnesota"
                }
            ]
        },
        "total": 12039
    }
    

### Search for Exploits

#### Description

Search across a variety of data sources for exploits and use facets to get summary information.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Search Query | String | N/A | Search query used to search the database of known exploits.  
Facets | String | N/A | A comma-separated list of properties to get summary information on. (i.e. port, source, author). More information can be found at <https://developer.shodan.io/api>.  
Page | String | N/A | The page number to page through results 100 at a time.  
  
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
    
    
    {
        "matches": [
            {
                "cve": "CVE-2011-2064",
                "description": "Cisco IOS 12.4MDA before 12.4(24)MDA5 on the Cisco Content Services Gateway - Second Generation (CSG2) allows remote attackers to cause a denial of service (device reload) via crafted ICMP packets, aka Bug ID CSCtl79577.",
                "osvdb": [73657],
                "bid": [48581],
                "source": "CVE",
                "_id": "2011-2064",
                "msb": []}],
        "facets": {
            "type": [
                {
                    "count": 1,
                    "value": "remote"
                }
            ]
        },
        "total": 4
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
