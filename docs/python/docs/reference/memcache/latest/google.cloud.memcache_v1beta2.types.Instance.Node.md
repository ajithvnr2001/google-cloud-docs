---
url: https://docs.cloud.google.com/python/docs/reference/memcache/latest/google.cloud.memcache_v1beta2.types.Instance.Node
title: Class Node (1.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:31.224191+00:00
---

# Class Node (1.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/memcache/latest/google.cloud.memcache_v1beta2.types.Instance.Node

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Node (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.2  1.11.0  1.10.1  1.9.5  1.8.0  1.7.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.1  1.1.3  1.0.0  0.3.2  0.2.0  0.1.0 
    
    
    Node(mapping=None, *, ignore_unknown_fields=False, **kwargs)

## Attributes  
  
---  
**Name** | **Description**  
`node_id` |  `str`   
Output only. Identifier of the Memcached node. The node id does not include project or location like the Memcached instance name.   
`zone` |  `str`   
Output only. Location (GCP Zone) for the Memcached node.   
`state` |  `[google.cloud.memcache_v1beta2.types.Instance.Node.State](https://docs.cloud.google.com/python/docs/reference/memcache/latest/google.cloud.memcache_v1beta2.types.Instance.Node.State)`   
Output only. Current state of the Memcached node.   
`host` |  `str`   
Output only. Hostname or IP address of the Memcached node used by the clients to connect to the Memcached server on this node.   
`port` |  `int`   
Output only. The port number of the Memcached server on this node.   
`parameters` |  `[google.cloud.memcache_v1beta2.types.MemcacheParameters](https://docs.cloud.google.com/python/docs/reference/memcache/latest/google.cloud.memcache_v1beta2.types.MemcacheParameters)`   
User defined parameters currently applied to the node.   
`update_available` |  `bool`   
Output only. Returns true if there is an update waiting to be applied   
  
## Classes 

### State
    
    
    State(value)

Different states of a Memcached node.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
