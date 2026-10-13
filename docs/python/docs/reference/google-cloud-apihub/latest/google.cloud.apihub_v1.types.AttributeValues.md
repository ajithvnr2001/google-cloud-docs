---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues
title: Class AttributeValues (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:29.640225+00:00
---

# Class AttributeValues (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AttributeValues (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    AttributeValues(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The attribute values associated with resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`enum_values` |  `[google.cloud.apihub_v1.types.AttributeValues.EnumAttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues.EnumAttributeValues)`   
The attribute values associated with a resource in case attribute data type is enum. This field is a member of `oneof`_ `Value`.   
`string_values` |  `[google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues)`   
The attribute values associated with a resource in case attribute data type is string. This field is a member of `oneof`_ `Value`.   
`json_values` |  `[google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues)`   
The attribute values associated with a resource in case attribute data type is JSON. This field is a member of `oneof`_ `Value`.   
`uri_values` |  `[google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues.StringAttributeValues)`   
The attribute values associated with a resource in case attribute data type is URL, URI or IP, like gs://bucket-name/object-name. This field is a member of `oneof`_ `Value`.   
`attribute` |  `str`   
Output only. The name of the attribute. Format: projects/{project}/locations/{location}/attributes/{attribute}   
  
## Classes 

### EnumAttributeValues
    
    
    EnumAttributeValues(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The attribute values of data type enum.

### StringAttributeValues
    
    
    StringAttributeValues(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The attribute values of data type string or JSON.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
