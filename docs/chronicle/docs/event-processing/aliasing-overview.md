---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/aliasing-overview/
title: Configure aliasing \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:49.582414+00:00
---

# Configure aliasing  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/aliasing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Configure aliasing 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Aliasing enables enrichment. For example, aliasing lets you find IP and MAC addresses for a hostname, or job titles and employment status for a user ID.

Like other features in Google Security Operations, aliasing requires data ingestion and indexing. It includes the following categories:

  * **Customer-specific data** : Data unique to a customer. For example, only `Cymbal` can provide data for `tim.smith@cymbal.com`. Customer-specific aliasing types include assets, users, and processes.
  * **Global data** : Data that applies to all customers. Google ingests and indexes this data on your behalf. For example, you can use Google Threat Intelligence data about a malicious file to check for its presence in your enterprise by using a matching file hash value. For more information, see [Enrich events with VirusTotal file metadata](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#enrich-events-with-VirusTotal-file-metadata). Google SecOps also provides GeoIP data to map IP addresses found in your customer-specific data to geographic locations. For more information, see [IP geolocation enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#ip_geolocation_enrichment).



## Asset aliasing

Asset aliasing links hostnames, IP addresses, MAC addresses, asset IDs, and other metadata. It involves the following steps:

  * **DHCP aliasing**: Uses DHCP events to link hostnames, MAC addresses, and IP addresses.
  * **EDR aliasing**: Maps product IDs (asset IDs) to hostnames. EDR mapping fields are derived exclusively from the `CS_EDR` log type.
  * **Asset context aliasing** : Associates an asset indicator with entity data, such as hostname, IP address, MAC address, software version, and deployment status.



### DHCP indexed fields

Google SecOps indexes DHCP records to generate aliases that link hostnames, IP addresses, and MAC addresses.

The following table lists the UDM fields and their corresponding indicator types used for asset aliasing:

UDM field | Indicator type  
---|---  
**principal.ip** and **principal.asset.ip** |  `ASSET_IP_ADDRESS`  
**principal.mac** and **principal.asset.mac** | `MAC`  
**principal.hostname** and **principal.asset.hostname** | `HOSTNAME`  
**principal.asset_id** and **principal.asset.asset_id** | `PRODUCT_SPECIFIC_ID`  
**network.dhcp.yiaddr** on ACK, OFFER, WIN_DELETED, and WIN_EXPIRED | `ASSET_IP_ADDRESS`  
**network.dhcp.ciaddr** on INFORM, RELEASE, and REQUEST | `ASSET_IP_ADDRESS`  
**network.dhcp.requested_address** on DECLINE | `ASSET_IP_ADDRESS`  
**network.dhcp.chaddr** | `MAC`  
**network.dhcp.client_hostname** | `HOSTNAME`  
  
### EDR mapping indexed fields

Google SecOps indexes EDR mapping fields to generate aliases that link hostnames and product specific IDs.

The following table lists the UDM fields and their corresponding indicator types: 

UDM field | Indicator type  
---|---  
**principal.hostname** and **principal.asset.hostname** | `HOSTNAME`  
**principal.asset_id** and **principal.asset.asset_id** | `PRODUCT_SPECIFIC_ID`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
