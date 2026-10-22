---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-umbrella/
title: Cisco Umbrella \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:45.399185+00:00
---

# Cisco Umbrella  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-umbrella/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco Umbrella

This document describes how to integrate Cisco Umbrella with Google Security Operations.

## Configure Cisco Umbrella to work with Google Security Operations

### Get the Enforcement token

To retrieve your key:

  1. Navigate to **Policies > Policy Components > Integrations**.
  2. Expand the appropriate integration or click **Add** to generate a custom integration.



**Reference:** <https://docs.umbrella.com/investigate-api/reference#reference-getting-started>

**Note:** For more information, see [Cisco Umbrella: The Umbrella Enforcement API for Custom Integrations](https://support.umbrella.com/hc/en-us/articles/231248748)

### Get the Investigate token

**Warning:** Open access to the following URL: [https://investigate.umbrella.com](https://investigate.umbrella.com/). This page will be empty when you first visit it.

To create your first API Access token:

  1. Click **Create new token**.
  2. Give the token a name and click **Create**. The generated token includes the email address of the person who created it and the creation date. To revoke the token, click **Delete**.



**Reference:** <https://docs.umbrella.com/investigate-api/reference#about-the-api-and-authentication>

## Configure Cisco Umbrella integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add Domain

#### Description

Add a domain to the OpenDNS block list.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Delete Domain

#### Description

Delete a domain from the OpenDNS block list.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Get Associated Domains

#### Description

Get associated domains for a particular host name.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
cisco_umbrella_Domains | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult": ["google.com", "twilio.com", "gmail.com"],
        "Entity": "example.com"
    }]
    

### Get Domain Security Info

#### Description

Provide security information about a domain (as an attachment).

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
found | Returns if it exists in JSON result  
popularity | Returns if it exists in JSON result  
geodiversity_normalized | Returns if it exists in JSON result  
dga_score | Returns if it exists in JSON result  
rip_score | Returns if it exists in JSON result  
asn_score | Returns if it exists in JSON result  
securerank2 | Returns if it exists in JSON result  
geoscore | Returns if it exists in JSON result  
attack | Returns if it exists in JSON result  
ks_test | Returns if it exists in JSON result  
pagerank | Returns if it exists in JSON result  
geodiversity | Returns if it exists in JSON result  
prefix_score | Returns if it exists in JSON result  
perplexity | Returns if it exists in JSON result  
entropy | Returns if it exists in JSON result  
fastflux | Returns if it exists in JSON result  
threat_type | Returns if it exists in JSON result  
tld_geodiversity | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
           {
             "found": false,
             "popularity": 0.0,
             "geodiversity_normalized": [],
             "dga_score": -16.878373381058395,
             "rip_score": 0.0,
             "asn_score": 0.0,
             "securerank2": 0.0,
             "geoscore": 0.0,
             "attack": "",
             "ks_test": 0.0,
             "pagerank": 0.0,
             "geodiversity": [],
             "prefix_score": 0.0,
             "perplexity": 0.9961472993373601,
             "entropy": 2.2516291673878226,
             "fastflux": false,
             "threat_type": "",
             "tld_geodiversity": []
           },
       "Entity": "zahav1.ru"
    }]
    

### Get Domain Status

#### Description

Provide the status of a domain, its categories of content, and security.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
content_categories | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
security_categories | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
       {   "content_categories": "Ecommerce/Shopping",
           "status": "1",
           "security_categories": ""
       },
      "Entity": "example.com"
    }]
    

### Get Malicious Domains

#### Description

Get malicious domains for an IP address.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
192.168.0.2 | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "192.168.0.2":
         [  "d.applovin.com.doesntexist.com",
            "atdmt.com.doesntexist.com",
            "Adservice.google.com.doesntexist.com"
          ]
    }
    

### Get Whois

#### Description

Retrieve the WHOIS information for the stated email address(es), nameserver(s), and domains.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
billingContactState | Returns if it exists in JSON result  
administrativeContactPostalCode | Returns if it exists in JSON result  
zoneContactCity | Returns if it exists in JSON result  
address | Returns if it exists in JSON result  
registrantFaxExt | Returns if it exists in JSON result  
auditUpdatedDate | Returns if it exists in JSON result  
administrativeContactCity | Returns if it exists in JSON result  
administrativeContactEmail | Returns if it exists in JSON result  
technicalContactFax | Returns if it exists in JSON result  
billingContactOrganization | Returns if it exists in JSON result  
billingContactEmail | Returns if it exists in JSON result  
technicalContactPostalCode | Returns if it exists in JSON result  
registrantOrganization | Returns if it exists in JSON result  
zoneContactPostalCode | Returns if it exists in JSON result  
registrantState | Returns if it exists in JSON result  
administrativeContactName | Returns if it exists in JSON result  
billingContactFaxExt | Returns if it exists in JSON result  
billingContactCity | Returns if it exists in JSON result  
technicalContactEmail | Returns if it exists in JSON result  
registrantCountry | Returns if it exists in JSON result  
technicalContactFaxExt | Returns if it exists in JSON result  
administrativeContactStreet | Returns if it exists in JSON result  
administrativeContactOrganization | Returns if it exists in JSON result  
billingContactCountry | Returns if it exists in JSON result  
billingContactName | Returns if it exists in JSON result  
registrarName | Returns if it exists in JSON result  
technicalContactTelephoneExt | Returns if it exists in JSON result  
administrativeContactFax | Returns if it exists in JSON result  
zoneContactFax | Returns if it exists in JSON result  
timestamp | Returns if it exists in JSON result  
registrantCity | Returns if it exists in JSON result  
administrativeContactTelephoneExt | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
updated | Returns if it exists in JSON result  
expires | Returns if it exists in JSON result  
whoisServers | Returns if it exists in JSON result  
technicalContactName | Returns if it exists in JSON result  
technicalContactState | Returns if it exists in JSON result  
nameServers | Returns if it exists in JSON result  
zoneContactFaxExt | Returns if it exists in JSON result  
recordExpired | Returns if it exists in JSON result  
registrantFax | Returns if it exists in JSON result  
registrantTelephoneExt | Returns if it exists in JSON result  
billingContactFax | Returns if it exists in JSON result  
technicalContactOrganization | Returns if it exists in JSON result  
administrativeContactState | Returns if it exists in JSON result  
zoneContactOrganization | Returns if it exists in JSON result  
billingContactPostalCode | Returns if it exists in JSON result  
zoneContactStreet | Returns if it exists in JSON result  
zoneContactName | Returns if it exists in JSON result  
registrantPostalCode | Returns if it exists in JSON result  
billingContactTelephone | Returns if it exists in JSON result  
emails | Returns if it exists in JSON result  
registrantTelephone | Returns if it exists in JSON result  
administrativeContactCountry | Returns if it exists in JSON result  
technicalContactCity | Returns if it exists in JSON result  
administrativeContactTelephone | Returns if it exists in JSON result  
created | Returns if it exists in JSON result  
registrarIANAID | Returns if it exists in JSON result  
registrantStreet | Returns if it exists in JSON result  
domainName | Returns if it exists in JSON result  
technicalContactCountry | Returns if it exists in JSON result  
billingContactStreet | Returns if it exists in JSON result  
timeOfLatestRealtimeCheck | Returns if it exists in JSON result  
zoneContactState | Returns if it exists in JSON result  
registrantEmail | Returns if it exists in JSON result  
administrativeContactFaxExt | Returns if it exists in JSON result  
billingContactTelephoneExt | Returns if it exists in JSON result  
zoneContactCountry | Returns if it exists in JSON result  
zoneContactEmail | Returns if it exists in JSON result  
zoneContactTelephoneExt | Returns if it exists in JSON result  
technicalContactTelephone | Returns if it exists in JSON result  
technicalContactStreet | Returns if it exists in JSON result  
zoneContactTelephone | Returns if it exists in JSON result  
hasRawText | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          {
            "billingContactState": null,
            "administrativeContactPostalCode": "89507",
            "zoneContactCity": null,
            "addresses": ["p.o. box 8102"],
            "registrantFaxExt": null,
            "registrantName": "Hostmaster, Amazon Legal Dept.",
            "auditUpdatedDate": "2019-01-08 12:03:30.000 UTC",
            "administrativeContactCity": "Reno",
            "administrativeContactEmail": "john_doe@example.com",
            "technicalContactFax": "12062667010",
            "billingContactOrganization": null,
            "billingContactEmail": null,
            "technicalContactPostalCode": "89507",
            "registrantOrganization": "Amazon Technologies, Inc.",
            "zoneContactPostalCode": null,
            "registrantState": "NV",
            "administrativeContactName": "Hostmaster, Amazon Legal Dept.",
            "billingContactFaxExt": null,
            "billingContactCity": null,
            "technicalContactEmail": "john_doe@example.com",
            "registrantCountry": "UNITED STATES",
            "technicalContactFaxExt": null,
            "administrativeContactStreet": ["p.o. box 8102"],
            "administrativeContactOrganization": "Amazon Technologies, Inc.",
            "billingContactCountry": null,
            "billingContactName": null,
            "registrarName": "MarkMonitor, Inc.",
            "technicalContactTelephoneExt": null,
            "administrativeContactFax": null,
            "zoneContactFax": null,
            "timestamp": null,
            "registrantCity": "Reno",
            "administrativeContactTelephoneExt": null,
            "status": [
                       "clientDeleteProhibited clientTransferProhibited clientUpdateProhibited serverDeleteProhibited serverTransferProhibited serverUpdateProhibited"],
            "updated": "2014-04-30",
            "expires": "2022-10-31",
            "whoisServers": "whois.markmonitor.com",
            "technicalContactName": "Hostmaster, Amazon Legal Dept.",
            "technicalContactState": "NV",
            "nameServers": [
                            "ns1.p31.dynect.net",
                            "Ns2.p31.dynect.net",
                            "Ns3.p31.dynect.net"
                           ],
            "zoneContactFaxExt": null,
            "recordExpired": false,
            "registrantFax": "12062667010",
            "registrantTelephoneExt": null,
            "billingContactFax": null,
            "technicalContactOrganization": "Amazon Technologies, Inc.",
            "administrativeContactState": "NV",
            "zoneContactOrganization": null,
            "billingContactPostalCode": null,
            "zoneContactStreet": [],
            "zoneContactName": null,
            "registrantPostalCode": "89507",
            "billingContactTelephone": null,
            "emails": ["hostmaster@example.com"],
            "registrantTelephone": "12062664064",
            "administrativeContactCountry": "UNITED STATES",
            "technicalContactCity": "Reno",
            "administrativeContactTelephone": "12062664064",
            "created": "1994-11-01",
            "registrarIANAID": "292",
            "registrantStreet": ["p.o. box 8102"],
            "domainName": "example.com",
            "technicalContactCountry": "UNITED STATES",
            "billingContactStreet": [],
            "timeOfLatestRealtimeCheck": 1547718689211,
            "zoneContactState": null,
            "registrantEmail": "john_doe@example.com",
            "administrativeContactFaxExt": null,
            "billingContactTelephoneExt": null,
            "zoneContactCountry": null,
            "zoneContactEmail": null,
            "zoneContactTelephoneExt": null,
            "technicalContactTelephone": "12062664064",
            "technicalContactStreet": ["p.o. box 8102"],
            "zoneContactTelephone": null,
            "hasRawText": true
         },
      "Entity": "example.com"
    }]
    

### Is Domain In Cisco Popularity List

Use the **Is Domain In Cisco Popularity List** action to verify if a domain is present in the Cisco Popularity List.

This action runs on the following Google SecOps entities:

  * `Domain`

  * `Hostname`

  * `URL`




#### Action inputs

None.

#### Action outputs

The **Is Domain In Cisco Popularity List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The following table lists the fields enriched using the **Is Domain In Cisco Popularity List** action:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`is_found_in_cisco_popular_list` | `true/false` | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Is Domain In Cisco Popularity List** action:
    
    
    [{
       "Entity": "",
       "EntityResult": {
           "found": "true",
           "entries": [
               {
                   "order": 123,
                   "domain": ""
               }
           ]
       }
    }]
    

##### Output messages

The **Is Domain In Cisco Popularity List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the following entities in Cisco Umbrella: ENTITY.` | The action succeeded.  
`Error executing action "Is Domain In Cisco Popularity List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Is Domain In Cisco Popularity List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Top Domains

Use the **List Top Domains** action to retrieve data on the most frequent domains based on the Cisco Popularity List.

#### Action inputs

The **List Top Domains** action requires the following parameters:

Parameter | Description  
---|---  
`Max Domains To Return` | Required. The maximum number of domains to retrieve from the list. The maximum value is `100,000`. The default value is `100`.  
  
#### Action outputs

The **List Top Domains** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
#### JSON result

The following example shows the JSON result output received when using the **List Top Domains** action:
    
    
    [{
    "order": 123,
    "domain": ""
    }]
    

##### Output messages

The **List Top Domains** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned top domains from Cisco Umbrella.` | The action succeeded.  
`Error executing action "List Top Domains". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Top Domains** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
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

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
