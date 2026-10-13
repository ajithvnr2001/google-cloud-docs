---
url: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_execute_query_metadata/
title: Execute Query Metadata \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:37.421331+00:00
---

# Execute Query Metadata  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_execute_query_metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Execute Query Metadata Stay organized with collections  Save and categorize content based on your preferences. 

2.50.0 (latest)  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.26.0  2.25.0  2.24.0  2.23.1  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.0  2.14.1  2.13.2  2.12.0  2.11.3  2.10.1  2.9.0  2.8.1  2.7.1  2.6.0  2.5.2  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.34.0 

This module provides the SqlType class used for specifying types in ExecuteQuery and some utilities.

The SqlTypes are used in Metadata returned by the ExecuteQuery operation as well as for specifying query parameter types explicitly.

### _class_ google.cloud.bigtable.data.execute_query.metadata.Metadata(columns: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)], google.cloud.bigtable.data.execute_query.metadata.SqlType.Type]]] = None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Metadata class for the ExecuteQuery operation.

  * **Parameters**

**columns** (_List_ _[__Tuple_ _[__Optional_ _[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str) _]__, **SqlType.Type_ _]__]_) – List of column metadata tuples. Each tuple contains the column name and the column type.




### _class_ google.cloud.bigtable.data.execute_query.metadata.SqlType()

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Classes denoting types of values returned by Bigtable’s ExecuteQuery operation.

Used in `Metadata`.

#### _class_ Array(element_type: google.cloud.bigtable.data.execute_query.metadata.SqlType.Type)

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Array SQL type.

#### _class_ Bool()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Bool SQL type.

#### expected_type()

alias of [`bool`](https://docs.python.org/3/builtins/functions.html#bool)

#### _class_ Bytes()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Bytes SQL type.

#### expected_type()

alias of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes)

#### _class_ Date()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Date SQL type.

#### expected_type()

alias of [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date)

#### _class_ Enum()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Enum SQL type.

#### _class_ Float32()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Float32 SQL type.

#### expected_type()

alias of [`float`](https://docs.python.org/3/builtins/functions.html#float)

#### _class_ Float64()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Float64 SQL type.

#### expected_type()

alias of [`float`](https://docs.python.org/3/builtins/functions.html#float)

#### _class_ Int64()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Int64 SQL type.

#### expected_type()

alias of [`int`](https://docs.python.org/3/builtins/functions.html#int)

#### _class_ Map(key_type: google.cloud.bigtable.data.execute_query.metadata.SqlType.Type, value_type: google.cloud.bigtable.data.execute_query.metadata.SqlType.Type)

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Map SQL type.

#### _class_ Proto()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Proto SQL type.

#### _class_ String()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

String SQL type.

#### expected_type()

alias of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str)

#### _class_ Struct(fields: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)], google.cloud.bigtable.data.execute_query.values.T]]] = None)

Bases: `google.cloud.bigtable.data.execute_query.values._NamedList`[`google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`], `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Struct SQL type.

#### _class_ Timestamp()

Bases: `google.cloud.bigtable.data.execute_query.metadata.SqlType.Type`

Timestamp SQL type.

Timestamp supports `DatetimeWithNanoseconds` but Bigtable SQL does not currently support nanoseconds precision. We support this for potential compatibility in the future. Nanoseconds are currently ignored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
