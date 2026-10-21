---
url: https://docs.cloud.google.com/service-directory/docs/query-dns/
title: Query using DNS \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:06.447082+00:00
---

# Query using DNS  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/query-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Query using DNS Stay organized with collections  Save and categorize content based on your preferences. 

Service Directory supports DNS queries for the following record types:

  * `A`/`AAAA`/`SRV` records for a service or an endpoint
  * `SOA`/`NS` records for the private zone origin



For a detailed explanation of these record types, see [List of DNS record types](https://www.wikipedia.org/wiki/List_of_DNS_record_types).

`A`/`AAAA` queries must observe the following format:
    
    
    SERVICE_NAME.ZONE_DOMAIN_NAME
    

Optionally:
    
    
    ENDPOINT_NAME.SERVICE_NAME.ZONE_DOMAIN_NAME
    

`SRV` queries must observe the following format:
    
    
    _SERVICE_NAME._tcp.SERVICE_NAME.ZONE_DOMAIN_NAME
    

**Note:** `SERVICE_NAME` appears _twice_ in the query name and the first label is preceded by a literal underscore character.

Optionally:
    
    
    _SERVICE_NAME._tcp.ENDPOINT_NAME.SERVICE_NAME.ZONE_DOMAIN_NAME
    

All services and endpoints in Service Directory default to having their service name as the symbolic service and a protocol of **tcp**.

## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
