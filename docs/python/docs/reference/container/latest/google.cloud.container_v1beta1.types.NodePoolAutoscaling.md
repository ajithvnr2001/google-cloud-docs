---
url: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodePoolAutoscaling
title: Class NodePoolAutoscaling (2.67.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:47.432860+00:00
---

# Class NodePoolAutoscaling (2.67.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodePoolAutoscaling

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NodePoolAutoscaling (2.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.67.0 (latest)  2.66.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.1  2.55.1  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.4  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.2  2.10.8  2.9.0  2.8.1  2.7.1  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.1  1.0.3  0.5.0  0.4.0  0.3.0 
    
    
    NodePoolAutoscaling(mapping=None, *, ignore_unknown_fields=False, **kwargs)

NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage.

## Attributes  
  
---  
**Name** | **Description**  
`enabled` |  `bool`   
Is autoscaling enabled for this node pool.   
`min_node_count` |  `int`   
Minimum number of nodes for one location in the node pool. Must be greater than or equal to 0 and less than or equal to max_node_count.   
`max_node_count` |  `int`   
Maximum number of nodes for one location in the node pool. Must be >= min_node_count. There has to be enough quota to scale up the cluster.   
`autoprovisioned` |  `bool`   
Can this node pool be deleted automatically.   
`location_policy` |  `[google.cloud.container_v1beta1.types.NodePoolAutoscaling.LocationPolicy](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodePoolAutoscaling.LocationPolicy)`   
Location policy used when scaling up a node pool.   
`total_min_node_count` |  `int`   
Minimum number of nodes in the node pool. Must be greater than or equal to 0 and less than or equal to total_max_node_count. The total\\_*_node_count fields are mutually exclusive with the \\*_node_count fields.   
`total_max_node_count` |  `int`   
Maximum number of nodes in the node pool. Must be greater than or equal to total_min_node_count. There has to be enough quota to scale up the cluster. The total\\_*_node_count fields are mutually exclusive with the \\*_node_count fields.   
  
## Classes 

### LocationPolicy
    
    
    LocationPolicy(value)

Location policy specifies how zones are picked when scaling up the node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
