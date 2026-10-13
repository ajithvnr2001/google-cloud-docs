---
url: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema
title: Class PhysicalSchema (3.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:20.908786+00:00
---

# Class PhysicalSchema (3.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PhysicalSchema (3.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.32.0 (latest)  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.1  3.25.1  3.24.1  3.23.0  3.22.0  3.21.1  3.20.1  3.19.1  3.18.3  3.17.2  3.16.0  3.15.1  3.14.0  3.13.1  3.12.0  3.11.1  3.10.0  3.9.3  3.8.1  3.7.1  3.6.2  3.5.0  3.4.3  3.3.2  3.2.1  3.1.1  3.0.0  2.0.2  1.0.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    PhysicalSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Native schema used by a resource represented as an entry. Used by query engines for deserializing and parsing source data.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`avro` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.AvroSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.AvroSchema)`   
Schema in Avro JSON format. This field is a member of `oneof`_ `schema`.   
`thrift` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.ThriftSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.ThriftSchema)`   
Schema in Thrift format. This field is a member of `oneof`_ `schema`.   
`protobuf` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.ProtobufSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.ProtobufSchema)`   
Schema in protocol buffer format. This field is a member of `oneof`_ `schema`.   
`parquet` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.ParquetSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.ParquetSchema)`   
Marks a Parquet-encoded data source. This field is a member of `oneof`_ `schema`.   
`orc` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.OrcSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.OrcSchema)`   
Marks an ORC-encoded data source. This field is a member of `oneof`_ `schema`.   
`csv` |  `[google.cloud.datacatalog_v1.types.PhysicalSchema.CsvSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.PhysicalSchema.CsvSchema)`   
Marks a CSV-encoded data source. This field is a member of `oneof`_ `schema`.   
  
## Classes 

### AvroSchema
    
    
    AvroSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Schema in Avro JSON format.

### CsvSchema
    
    
    CsvSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Marks a CSV-encoded data source.

### OrcSchema
    
    
    OrcSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Marks an ORC-encoded data source.

### ParquetSchema
    
    
    ParquetSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Marks a Parquet-encoded data source.

### ProtobufSchema
    
    
    ProtobufSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Schema in protocol buffer format.

### ThriftSchema
    
    
    ThriftSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Schema in Thrift format.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
