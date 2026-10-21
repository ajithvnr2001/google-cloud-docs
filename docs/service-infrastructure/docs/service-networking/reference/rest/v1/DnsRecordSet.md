---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/DnsRecordSet/
title: DnsRecordSet \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:40.119514+00:00
---

# DnsRecordSet  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/DnsRecordSet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  DnsRecordSet Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a DNS record set resource.

JSON representation  
---  
      
    
    {
      "domain": string,
      "type": string,
      "ttl": string,
      "data": [
        string
      ]
    }  
  
Fields  
---  
`domain` |  `string` Required. The DNS or domain name of the record set, e.g. `test.example.com`. Cloud DNS requires that a DNS suffix ends with a trailing dot.  
`type` |  `string` Required. The identifier of a supported record type.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The period of time for which this RecordSet can be cached by resolvers.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`data[]` |  `string` Required. As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) for examples see <https://cloud.google.com/dns/records/json-record>.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
