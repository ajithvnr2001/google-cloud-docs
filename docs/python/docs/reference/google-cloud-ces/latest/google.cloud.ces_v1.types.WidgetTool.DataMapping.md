---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.WidgetTool.DataMapping
title: Class DataMapping (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:25.844691+00:00
---

# Class DataMapping (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.WidgetTool.DataMapping

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataMapping (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    DataMapping(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for mapping data from a source tool to the widget's input parameters.

## Attributes  
  
---  
**Name** | **Description**  
`source_tool_name` |  `str`   
Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`field_mappings` |  `MutableMapping[str, str]`   
Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.   
`python_function` |  `[google.cloud.ces_v1.types.PythonFunction](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.PythonFunction)`   
Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.   
`mode` |  `[google.cloud.ces_v1.types.WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1.types.WidgetTool.DataMapping.Mode)`   
Optional. The mode of the data mapping.   
`python_script` |  `str`   
Deprecated: Use `python_function` instead.   
  
## Classes 

### FieldMappingsEntry
    
    
    FieldMappingsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### Mode
    
    
    Mode(value)

The strategy used to map data from the source tool to the widget.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
