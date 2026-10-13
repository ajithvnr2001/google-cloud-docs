---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Schema
title: Class Schema (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:39.749829+00:00
---

# Class Schema (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Schema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Schema (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    Schema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Schema is a collection of supported node & edge labels and properties for an overlay.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the schema. Format: `projects/{project}/locations/{location}/domains/{domain}/schema`  
`node_types` |  `MutableSequence[[google.cloud.apptopology_v1.types.NodeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.NodeType)]`   
A list of `NodeType`\ s defined within this schema. Refer to the documentation of `NodeType` for more details.   
`edge_types` |  `MutableSequence[[google.cloud.apptopology_v1.types.EdgeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.EdgeType)]`   
A list of `EdgeType`\ s defined within this schema. Refer to the documentation of `EdgeType` for more details.   
`label_properties` |  `MutableSequence[[google.cloud.apptopology_v1.types.LabelProperties](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.LabelProperties)]`   
A list of supported labels and corresponding properties.   
`edge_rules` |  `MutableSequence[[google.cloud.apptopology_v1.types.EdgeRule](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.EdgeRule)]`   
Edge rules. These will indicate which node types can be connected and through what edge type. This is a list of (source_node_type, edge_type, destination_node_type) tuples.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
