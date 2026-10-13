---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag
title: Class SupportedDatabaseFlag (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:56.668399+00:00
---

# Class SupportedDatabaseFlag (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SupportedDatabaseFlag (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    SupportedDatabaseFlag(mapping=None, *, ignore_unknown_fields=False, **kwargs)

SupportedDatabaseFlag gives general information about a database flag, like type and allowed values. This is a static value that is defined on the server side, and it cannot be modified by callers. To set the Database flags on a particular Instance, a caller should modify the Instance.database_flags field.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`string_restrictions` |  `[google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.StringRestrictions](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.StringRestrictions)`   
Restriction on STRING type value. This field is a member of `oneof`_ `restrictions`.   
`integer_restrictions` |  `[google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.IntegerRestrictions](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.IntegerRestrictions)`   
Restriction on INTEGER type value. This field is a member of `oneof`_ `restrictions`.   
`recommended_string_value` |  `str`   
The recommended value for a STRING flag. This field is a member of `oneof`_ `recommended_value`.   
`recommended_integer_value` |  `google.protobuf.wrappers_pb2.Int64Value`   
The recommended value for an INTEGER flag. This field is a member of `oneof`_ `recommended_value`.   
`name` |  `str`   
The name of the flag resource, following Google Cloud conventions, e.g.: \- projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.   
`flag_name` |  `str`   
The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.   
`accepts_multiple_values` |  `bool`   
Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified.   
`supported_db_versions` |  `MutableSequence[[google.cloud.alloydb_v1alpha.types.DatabaseVersion](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.DatabaseVersion)]`   
Major database engine versions for which this flag is supported.   
`requires_db_restart` |  `bool`   
Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's).   
`scope` |  `[google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.Scope](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.SupportedDatabaseFlag.Scope)`   
The scope of the flag.   
  
## Classes 

### IntegerRestrictions
    
    
    IntegerRestrictions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Restrictions on INTEGER type values.

### Scope
    
    
    Scope(value)

The scope of the flag.

### StringRestrictions
    
    
    StringRestrictions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Restrictions on STRING type values

### ValueType
    
    
    ValueType(value)

ValueType describes the semantic type of the value that the flag accepts. Regardless of the ValueType, the Instance.database_flags field accepts the stringified version of the value, i.e. "20" or "3.14".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
