---
url: https://docs.cloud.google.com/data-transfer/product-name-change-announce/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:29:24.014046+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer/product-name-change-announce/




Stay organized with collections  Save and categorize content based on your preferences. 

# Renaming Egress to Data Transfer - Effected SKU Descriptions

Starting December 15, 2023, Google Cloud product names and SKU descriptions will change from "egress" or "ingress" to "data transfer", with modifying terms such as "outbound" or "out and inbound" or "in". The purpose is to align this terminology more closely with industry standards. For more information, refer to the FAQ below.

## FAQ: Renaming Egress to Data Transfer

**What is changing?**  
We are renaming Egress to Data Transfer to more accurately describe the service offered to customers. This name change will apply across Technical Documentation, Pricing web pages and SKU descriptions.

**Why are we making this change?**  
This change helps us clearly identify to the market that the fees tied to Internet, Inter-zone and Inter-region data transfer are for the purpose of serving workloads to customers which involves data transfer within GCP.

**Which instances of Egress are we changing?**  
Any instance of the word Egress used with regards to billed data transfer from one entity to another. This includes Intra-zone, Inter-zone (between VMs in a region), Inter-region (across regions), Internet (GCP to Internet) to name a few. The list is below:

**Current Usage** | **New Usage** | **Definition**  
---|---|---  
Inter-zone Egress | Inter-zone Data Transfer | Data transferred between two Google Cloud resources in the same region  
Inter-region Egress | Inter-region Data Transfer | Data transferred between two Google Cloud resources in different regions  
Internet Egress | Data Transfer out to Internet | Data transferred between a Google Cloud resource and an internet end-point  
Internet Egress* - Premium | Premium Tier Data Transfer out to Internet | Data transferred between a Google Cloud resource and an internet end-point, carried over Google backbone  
Internet Egress* - Standard | Standard Tier Data Transfer out to Internet | Data transferred between a Google Cloud resource and an internet end-point, carried over public internet  
Interconnect Egress | Interconnect Data Transfer out | Data transferred between a Google Cloud resource and another CSP / on-prem data center over private link  
VPN Egress | VPN Data Transfer | Data transferred between two resources over VPN tunnel  
CDN Cache Egress | CDN Data Transfer out to Internet | Data transferred from CDN Edge Cache out to Internet  
  
*Ingress will be renamed to Data Transfer in

**When will the changes be rolled out?**  
All changes will be effective on 12/15/23

**Are there any pricing changes?**  
There will be no impact to existing customer contracts, pricing and discounts.

**What are the implications of changing SKU descriptions?**  
For the most part, this will not affect any billing operations. If, however, customers export billing data to reporting tools like BigQuery, they should ensure that they are referring to the updated SKU descriptions in their scripts. A sample change in SQL query could look like:

Old Query: _select distinct SKUs from table where SKU_description like "%Egress%"_  
New Query: _select distinct SKUs from table where SKU_description like "%Data Transfer%"_

**How are we communicating these changes to customers?**  
We plan to send an MSA to customers on November 15 2023.

**Where can I find the list of new SKU descriptions?**  
You can find a list of old and new SKU descriptions [here](https://services.google.com/fh/files/emails/b_302695304_m1_sku.pdf). We will also include this link within the customer MSA.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-23 UTC."],[],[]] 
