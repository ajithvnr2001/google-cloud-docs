---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ipinfo/
title: IPinfo \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:46.978524+00:00
---

# IPinfo  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ipinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IPinfo

This document provides guidance on how to integrate IPinfo with Google SecOps.

## Configure IPinfo to work with Google Security Operations

To obtain your Access Token, first sign in to your [IPinfo Account](https://ipinfo.io/account/login).

You will be redirected to a **Dashboard page** , where you can find your Access Token.

## Configure IPinfo integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get Domain Information

#### Description

Fetch domain information for an address.

#### Parameters

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
count | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
range | Returns if it exists in JSON result  
domains | Returns if it exists in JSON result  
asn | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
           "count": 939,
           "domain": "comcast.net",
           "ip": "1.1.1.1",
           "range": "1.1.1.1/12",
           "domains":
             [[
                "comcast.net",
                "Comcast.com",
                "Watchable.com",
                "Comcastnow.com",
                "Comcastsportsnet.com",
                "Xfinityprepaid.net",
                "Comcastaddelivery.com",
                "Bigtoptestdrive.com",
                "Gotgearamazingoutdoors.com",
                "comcastspotlight-mediafactbook.com",
                "Entertainmentmoney.com",
                "footballmaniasweepstakes.com",
                "Jobsatcomcast.com",
                "anyscreem.org",
                "amyscreen.net",
                "amalunasweeps.com",
                "Comcastlabs.com",
                "anycreen.org",
                "coloradotruckauthority.com",
                "touchdownandtailgate.com",
                "Readytoridemonroepbr.com",
                "anysceren.net",
                "Bostonhealthads.com",
                "Comcastspotlight-3d-hlly.com",
                 "Fordfrugalista.com"
              ]],
         "asn": "AS7922"
       },
      "Entity": "comcast.net"
    }]
    

### Get IP Information

#### Description

This is one of the most common tools of any website, domain, or IP address to find out the user, internet provider, and location. IP address scanning is useful in finding the origin of unwanted emails or the source of spam, virus, and attacks. It will show you the domain owner's registered WHOIS and ARIN contact data, and the company that operates the associated server, wherever they are. You may find out their internet service provider for dynamic IP addresses of private users to allow them to contact them for a complaint.

#### Parameters

N/A

#### Run On

This actionr runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
city | Returns if it exists in JSON result  
loc | Returns if it exists in JSON result  
country | Returns if it exists in JSON result  
company | Returns if it exists in JSON result  
hostname | Returns if it exists in JSON result  
asn | Returns if it exists in JSON result  
carrier | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
postal | Returns if it exists in JSON result  
region | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
           "city": "Southbridge",
           "loc": "42.0707,-72.0440",
           "country": "US",
           "company":
             {
               "domain": "sprint.com",
               "type": "isp",
               "name": "Sprint Springfield POP"
              },
           "hostname": "66-87-125-72.pools.spcsdns.net",
           "asn":
             {
               "route": "1.1.1.1/24",
               "type": "isp",
               "domain": "spcsdns.net",
               "name": "Sprint Personal Communications Systems",
               "asn": "AS10507"
              },
          "carrier":
               {
                 "mnc": "120",
                 "mcc": "310",
                 "name": "Sprint"
               },
           "ip": "1.1.1.1",
           "postal": "01550",
           "region": "Massachusetts"
          },
     "Entity": "1.1.1.1"
    }]
    

### Ping

#### Description

Check API token validity.

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
ping_status | True/False | ping_status:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
