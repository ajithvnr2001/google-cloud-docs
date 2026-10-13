---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/DnsKeySpec/
title: DnsKeySpec \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:30.329518+00:00
---

# DnsKeySpec  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/DnsKeySpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  DnsKeySpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Parameters for DnsKey key generation. Used for generating initial keys for a new ManagedZone and as default when adding a new DnsKey.

JSON representation  
---  
      
    
    {
      "keyType": enum ([KeyType](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/KeyType)),
      "algorithm": enum ([Algorithm](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/Algorithm)),
      "keyLength": integer,
      "kind": string
    }  
  
Fields  
---  
`keyType` |  `enum (`[KeyType](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/KeyType)`)` Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, are only used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and are used to sign all other types of resource record sets.  
`algorithm` |  `enum (`[Algorithm](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/Algorithm)`)` String mnemonic specifying the DNSSEC algorithm of this key.  
`keyLength` |  `integer` Length of the keys in bits.  
`kind` |  `string`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
