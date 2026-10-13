---
url: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.TableFieldSchema
title: Class TableFieldSchema (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:36.080292+00:00
---

# Class TableFieldSchema (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.TableFieldSchema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TableFieldSchema (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.2  2.35.0  2.34.0  2.33.1  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.2  2.15.0  2.14.2  2.13.2  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.8.0  0.7.0  0.6.0 
    
    
    TableFieldSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

TableFieldSchema defines a single field/column within a table schema.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (\\_), and must start with a letter or underscore. The maximum length is 128 characters.   
`type_` |  `[google.cloud.bigquery_storage_v1.types.TableFieldSchema.Type](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.TableFieldSchema.Type)`   
Required. The field data type.   
`mode` |  `[google.cloud.bigquery_storage_v1.types.TableFieldSchema.Mode](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.TableFieldSchema.Mode)`   
Optional. The field mode. The default value is NULLABLE.   
`fields` |  `MutableSequence[google.cloud.bigquery_storage_v1.types.TableFieldSchema]`   
Optional. Describes the nested schema fields if the type property is set to STRUCT.   
`description` |  `str`   
Optional. The field description. The maximum length is 1,024 characters.   
`max_length` |  `int`   
Optional. Maximum length of values of this field for STRINGS or BYTES. If max_length is not specified, no maximum length constraint is imposed on this field. If type = "STRING", then max_length represents the maximum UTF-8 length of strings in this field. If type = "BYTES", then max_length represents the maximum number of bytes in this field. It is invalid to set this field if type is not "STRING" or "BYTES".   
`precision` |  `int`   
Optional. Precision (maximum number of total digits in base 10) and scale (maximum number of digits in the fractional part in base 10) constraints for values of this field for NUMERIC or BIGNUMERIC. It is invalid to set precision or scale if type is not "NUMERIC" or "BIGNUMERIC". If precision and scale are not specified, no value range constraint is imposed on this field insofar as values are permitted by the type. Values of this NUMERIC or BIGNUMERIC field must be in this range when: \- Precision (P) and scale (S) are specified: [-10^(P-S) + 10^(-S), 10^(P-S) - 10^(-S)] \- Precision (P) is specified but not scale (and thus scale is interpreted to be equal to zero): [-10^P + 1, 10^P - 1]. Acceptable values for precision and scale if both are specified: \- If type = "NUMERIC": 1 <= precision="" -="" scale=""><= 29="" and="" 0=""><= scale=""><= 9.="" -="" if="" type="BIGNUMERIC" :="" 1=""><= precision="" -="" scale=""><= 38="" and="" 0=""><= scale=""><= 38.="" acceptable="" values="" for="" precision="" if="" only="" precision="" is="" specified="" but="" not="" scale="" (and="" thus="" scale="" is="" interpreted="" to="" be="" equal="" to="" zero):="" -="" if="" type="NUMERIC" :="" 1=""><= precision=""><= 29.="" -="" if="" type="BIGNUMERIC" :="" 1=""><= precision=""><= 38.="" if="" scale="" is="" specified="" but="" not="" precision,="" then="" it="" is="" invalid.="">  
`scale` |  `int`   
Optional. See documentation for precision.   
`default_value_expression` |  `str`   
Optional. A SQL expression to specify the [default value] (https://cloud.google.com/bigquery/docs/default-values) for this field.   
`timestamp_precision` |  `google.protobuf.wrappers_pb2.Int64Value`   
Optional. Precision (maximum number of total digits in base 10) for seconds of TIMESTAMP type. Possible values include: \- 6 (Default, for TIMESTAMP type with microsecond precision) \- 12 (For TIMESTAMP type with picosecond precision)   
`range_element_type` |  `[google.cloud.bigquery_storage_v1.types.TableFieldSchema.FieldElementType](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.TableFieldSchema.FieldElementType)`   
Optional. The subtype of the RANGE, if the type of this field is RANGE. If the type is RANGE, this field is required. Possible values for the field element type of a RANGE include: \- DATE \- DATETIME \- TIMESTAMP   
  
## Classes 

### FieldElementType
    
    
    FieldElementType(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the type of a field element.

### Mode
    
    
    Mode(value)

### Type
    
    
    Type(value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
