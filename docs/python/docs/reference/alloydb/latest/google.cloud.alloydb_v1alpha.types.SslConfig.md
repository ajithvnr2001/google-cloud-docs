---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SslConfig
title: Class SslConfig (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:58.271886+00:00
---

# Class SslConfig (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SslConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SslConfig (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    SslConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

SSL configuration.

## Attributes  
  
---  
**Name** | **Description**  
`ssl_mode` |  `[google.cloud.alloydb_v1alpha.types.SslConfig.SslMode](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SslConfig.SslMode)`   
Optional. SSL mode. Specifies client-server SSL/TLS connection behavior.   
`ca_source` |  `[google.cloud.alloydb_v1alpha.types.SslConfig.CaSource](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SslConfig.CaSource)`   
Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value.   
  
## Classes 

### CaSource
    
    
    CaSource(value)

Certificate Authority (CA) source for SSL/TLS certificates.

### SslMode
    
    
    SslMode(value)

SSL mode options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
