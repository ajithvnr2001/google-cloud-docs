---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-dns/
title: Cloud DNS (DNS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:07.084137+00:00
---

# Cloud DNS (DNS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Cloud DNS (DNS) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description | Type | Emit duration | Labels  
---|---|---|---  
`cloud_dns_requests_total` |  |  |   
The number of requests received by the Cloud DNS authoritative server. | Counter | 1 m | `server`, `zone`, `visibility`, `proto`, `family`, `type`, `zone_id`  
`cloud_dns_request_duration_seconds_count` |  |  |   
The histogram bucket representing the count of responses duration received by the client from the authoritative server. | Histogram | 1 m | `server`, `zone`, `visibility`, `zone_id`  
`cloud_dns_request_duration_seconds` |  |  |   
The histogram bucket representing the sum of response durations received by the client from the authoritative server. | Histogram | 1 m | `server`, `zone`, `visibility`, `zone_id`  
`cloud_dns_request_duration_seconds_bucket` |  |  |   
The histogram bucket representing response durations received by the client from the authoritative server. | Histogram | 1 m | `server`, `zone`, `visibility`, `zone_id`  
`cloud_dns_responses_total` |  |  |   
The number of responses received by the client from the authoritative server. | Counter | 1 m | `server`, `zone`, `visibility`, `rcode`, `zone_id`  
  
### Metric Labels Reference

The following table explains the labels available on the DNS metrics:

Label | Explanation  
---|---  
`family` | The IP address family of the client making the request (e.g., `1` for IPv4).  
`ha_cluster` | Internal identifier for the high-availability cluster/shard handling the request.  
`le` | The bucket boundary for histogram metrics (less than or equal to).  
`proto` | The transport protocol used for the DNS request (e.g., `udp`, `tcp`).  
`rcode` | The DNS response code (e.g., `NOERROR`, `NXDOMAIN`, `SERVFAIL`).  
`server` | The address of the DNS server handling the request (e.g., `dns://:53`).  
`type` | The DNS query type (e.g., `A`, `MX`, `PTR`).  
`visibility` | The visibility of the DNS zone (`PUBLIC` or `PRIVATE`).  
`zone` | The name of the DNS zone (e.g., `google.com.`).  
`zone_id` | The GDCag Zone in which the request was handled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
