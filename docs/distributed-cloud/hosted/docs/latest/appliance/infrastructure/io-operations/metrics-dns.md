---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-dns/
title: Domain Name System (DNS) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:55.565694+00:00
---

# Domain Name System (DNS)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Domain Name System (DNS) Stay organized with collections  Save and categorize content based on your preferences. 

## Metrics list

Name and description | Type | Scrape interval or emit duration | Labels  
---|---|---|---  
`coredns_dns_do_requests_total`  
DNS requests with the DO (DNSSEC OK) bit set (DO=1) for each zone. | Counter |  |   
`coredns_dns_requests_total`  
DNS requests made for each zone, protocol, and family. | Counter |  |   
`coredns_dns_responses_total`  
Total number of response status codes. | Counter |  |   
`coredns_dns_request_duration_seconds`  
Time in seconds that each request takes for each zone. | Histogram |  |   
`coredns_panics_total`  
Total number of panics. | Counter |  |   
`unbound_queries_total`  
Total number of queries received. | Counter |  |   
`unbound_query_types_total`  
Total number of queries with a given query type. | Counter |  |   
`unbound_recursive_replies_total`  
Total number of replies sent to queries that required a recursive processing. | Counter |  |   
`unbound_time_up_seconds_total`  
Time up elapsed in seconds since the server boot. | Counter |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
