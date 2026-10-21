---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mx-toolbox/
title: MxToolbox \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:16:02.666283+00:00
---

# MxToolbox  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mx-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MxToolbox

This document provides guidance on how to integrate MxToolbox with Google SecOps.

## Configure MxToolbox integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### A Record Lookup

#### Description

A record lookup returns the IP address for a specific domain name.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * Hostname
  * URL
  * User



#### Action Results

##### Entity Enrichment

IP Address | Returns if it exists in JSON result  
---|---  
Type | Returns if it exists in JSON result  
Domain Name | Returns if it exists in JSON result  
TTL | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ip_addresses | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          [{
            "IP Address": "1.1.1.1",
            "Type": "A",
            "Domain Name": "example.com",
            "TTL": "10 min"
          }],
      "Entity": "example.com"
    }]​
    

### Blacklist Check

#### Description

The blacklist check will test a mail server IP address against over 100 DNS based email blacklists. (Commonly called Realtime blacklist, DNSBL or RBL). If your mail server has been blacklisted, some emails you send may not be delivered. Email blacklists are a common way of reducing spam.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Blacklist Threshold | String | N/A | The threshold of the blacklist to determine whether a domain or IP are blacklisted  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Info | Returns if it exists in JSON result  
Name | Returns if it exists in JSON result  
PublicDescription | Returns if it exists in JSON result  
IsExcludedByUser | Returns if it exists in JSON result  
BlacklistReasonDescription | Returns if it exists in JSON result  
BlacklistResponseTime | Returns if it exists in JSON result  
Url | Returns if it exists in JSON result  
BlacklistReasonCode | Returns if it exists in JSON result  
BlacklistTTL | Returns if it exists in JSON result  
ID | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_blacklisted | True/False | is_blacklisted:True  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          [{
             "Info": "Blacklisted by SURBL multi",
             "Name": "SURBL multi",
             "PublicDescription": null,
             "IsExcludedByUser": false,
             "BlacklistReasonDescription": "Listed",
             "BlacklistResponseTime": "63",
             "Url": "https://mxtoolbox.com/Problem/blacklist/SURBL-multi?page=prob_blacklist&showlogin=1&hidetoc=1&action=blacklist:chinatlz.com",
             "BlacklistReasonCode": "1.1.1.1",
             "BlacklistTTL": "180",
             "ID": 285
           }],
       "Entity": "chinatlz.com"
    }]​
    

### HTTPS Information Lookup

#### Description

The HTTPS Lookup and SSL Certificate Checker will query a website URL and tell you if it responds securely with SSL encryption.

#### Parameters

N/A

#### Run On

This action runs on the URL entity

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
https | True/False | https:False  
  
##### JSON Result
    
    
    N/A
    

### MX Record Lookup

#### Description

MX record lookup returns the mail server address for a specific Domain.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * Hostname
  * URL
  * User



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Hostname | Returns if it exists in JSON result  
Pref | Returns if it exists in JSON result  
IPAddress | Returns if it exists in JSON result  
TTL | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
mx_domains | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         [{
            "Hostname": "aspmx.l.google.com",
            "Pref": "1",
            "IPAddress": "1.1.1.1",
            "TTL": "60min"
           },{
            "Hostname": "aspmx3.googlemail.com",
            "Pref": "10",
            "IPAddress": "2a00: 1450: 400b: c03: : 1a",
            "TTL": "60min"
          }],
       "Entity": "example.com"
    }]
    

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
    

### Ping External IP

#### Description

Ping external IP or Domain using ICMP protocol.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * URL
  * User
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ping_results | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Reverse DNS Lookup

#### Description

The Reverse Lookup tool will do a reverse IP lookup. If you type in an IP address, MX ToolBox will attempt to locate a DNS PTR record for that IP address. You can then click on the results to find out more about that IP Address. Please note: in general, your ISP must setup and maintain these Reverse DNS records (i.e. PTR records) for you.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
IP Address | Returns if it exists in JSON result  
Type | Returns if it exists in JSON result  
Domain Name | Returns if it exists in JSON result  
TTL | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ptr_domains | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          [{
              "IP Address": "1.1.1.1",
              "Type": "PTR",
              "Domain Name": "google-public-dns-a.google.com",
              "TTL": "24 hrs"
           }],
       "Entity": "1.1.1.1"
    }]
    

### SPF Lookup

#### Description

Sender Policy Framework (SPF) records allow domain owners to publish a list of IP addresses or subnets that are authorized to send email on their behalf.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
IP Address | String | N/A | The IP address to look for.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * User
  * URL



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
1.1.1.1/24 | Returns if it exists in JSON result  
64.233.160.0/19 | Returns if it exists in JSON result  
103.237.104.0/22 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
auth_sender | N/A | N/A  
  
##### JSON Result
    
    
    [{
        "EntityResult":
                      [
                      "1.1.1.1/24",
                      "64.233.160.0/19",
                      "103.237.104.0/22"],
        "Entity": "example.com"
    }]​
    

### STCP Port Status

#### Description

Check if a specific TCP port is open.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Port Number | String | N/A | The port number to check.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * User
  * URL



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
port_statuses | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
