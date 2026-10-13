---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Edge
title: Class Edge (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:18.138609+00:00
---

# Class Edge (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Edge

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Edge (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    Edge(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single edge connecting two nodes in the graph.

## Attributes  
  
---  
**Name** | **Description**  
`properties` |  `google.protobuf.struct_pb2.Struct`   
Properties associated with the edge. Refer to https://apptopology.googleapis.com/v1/GetSchema for a detailed list of edge properties.   
`source_node_name` |  `str`   
The name of the source node for this edge. This is the `name` field in the Node.   
`destination_node_name` |  `str`   
The name of the destination node for this edge. This is the `name` field in the Node.   
`labels` |  `MutableSequence[str]`   
Labels attached to the edge. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the edge type.   
`context` |  `[google.cloud.apptopology_v1.types.EntityContext](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.EntityContext)`   
The context of the edge.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
