---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformBlueprint
title: Class TerraformBlueprint (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:51.294835+00:00
---

# Class TerraformBlueprint (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformBlueprint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TerraformBlueprint (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    TerraformBlueprint(mapping=None, *, ignore_unknown_fields=False, **kwargs)

TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`gcs_source` |  `str`   
URI of an object in Google Cloud Storage. Format: `gs://{bucket}/{object}` URI may also specify an object version for zipped objects. Format: `gs://{bucket}/{object}#{version}` This field is a member of `oneof`_ `source`.   
`git_source` |  `[google.cloud.config_v1.types.GitSource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GitSource)`   
URI of a public Git repo. This field is a member of `oneof`_ `source`.   
`input_values` |  `MutableMapping[str, [google.cloud.config_v1.types.TerraformVariable](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformVariable)]`   
Optional. Input variable values for the Terraform blueprint.   
`external_values` |  `MutableMapping[str, [google.cloud.config_v1.types.ExternalValueSource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExternalValueSource)]`   
Optional. Map of input variable names in this blueprint to configurations for importing values from external sources.   
  
## Classes 

### ExternalValuesEntry
    
    
    ExternalValuesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### InputValuesEntry
    
    
    InputValuesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
