---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.types.LookupVersionRequest
title: Class LookupVersionRequest (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:50.384137+00:00
---

# Class LookupVersionRequest (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.types.LookupVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LookupVersionRequest (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.0 
    
    
    LookupVersionRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for LookupVersion.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The subject to lookup the schema in. Structured like: `projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}` or `projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}`  
`schema_type` |  `[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType)`   
Optional. The schema type of the schema. This field is a member of `oneof`_ `_schema_type`.   
`schema` |  `str`   
Required. The schema payload   
`references` |  `MutableSequence[[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference)]`   
Optional. The schema references used by the schema.   
`normalize` |  `bool`   
Optional. If true, the schema will be normalized before being looked up. The default is false. This field is a member of `oneof`_ `_normalize`.   
`deleted` |  `bool`   
Optional. If true, soft-deleted versions will be included in lookup, no matter if the subject is active or soft-deleted. If false, soft-deleted versions will be excluded. The default is false. This field is a member of `oneof`_ `_deleted`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
