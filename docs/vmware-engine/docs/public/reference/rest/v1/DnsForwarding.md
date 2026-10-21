---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/DnsForwarding/
title: DnsForwarding \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:22.472760+00:00
---

# DnsForwarding  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/DnsForwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  DnsForwarding Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ForwardingRule
    * JSON representation



DNS forwarding config. This config defines a list of domain to name server mappings, and is attached to the private cloud for custom domain resolution.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "forwardingRules": [
        {
          object ([ForwardingRule](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/DnsForwarding#ForwardingRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this DNS profile. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`forwardingRules[]` |  `object (`[ForwardingRule](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/DnsForwarding#ForwardingRule)`)` Required. List of domain mappings to configure  
  
## ForwardingRule

A forwarding rule is a mapping of a `domain` to `nameServers`. This mapping allows VMware Engine to resolve domains for attached private clouds by forwarding DNS requests for a given domain to the specified nameservers.

JSON representation  
---  
      
    
    {
      "domain": string,
      "nameServers": [
        string
      ]
    }  
  
Fields  
---  
`domain` |  `string` Required. Domain used to resolve a `nameServers` list.  
`nameServers[]` |  `string` Required. List of DNS servers to use for domain resolution  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
