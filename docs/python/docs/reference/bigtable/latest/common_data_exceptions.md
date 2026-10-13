---
url: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_exceptions/
title: Custom Exceptions \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:02.134031+00:00
---

# Custom Exceptions  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_exceptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Custom Exceptions Stay organized with collections  Save and categorize content based on your preferences. 

2.50.0 (latest)  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.26.0  2.25.0  2.24.0  2.23.1  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.0  2.14.1  2.13.2  2.12.0  2.11.3  2.10.1  2.9.0  2.8.1  2.7.1  2.6.0  2.5.2  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.34.0 

### _exception_ google.cloud.bigtable.data.exceptions.EarlyMetadataCallError()

Bases: [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)

Execption raised when metadata is request from an ExecuteQueryIterator before the first row has been read, or the query has completed

### _exception_ google.cloud.bigtable.data.exceptions.FailedMutationEntryError(failed_idx: [int](https://docs.python.org/3/builtins/functions.html#int) | [None](https://docs.python.org/3/builtins/constants.html#None), failed_mutation_entry: [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_mutations#google.cloud.bigtable.data.mutations.RowMutationEntry), cause: [Exception](https://docs.python.org/3/builtins/exceptions.html#Exception))

Bases: [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception)

Represents a single failed RowMutationEntry in a bulk_mutate_rows request. A collection of FailedMutationEntryErrors will be raised in a MutationsExceptionGroup

### _exception_ google.cloud.bigtable.data.exceptions.FailedQueryShardError(failed_index: [int](https://docs.python.org/3/builtins/functions.html#int), failed_query: 'ReadRowsQuery' | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Any], cause: [Exception](https://docs.python.org/3/builtins/exceptions.html#Exception))

Bases: [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception)

Represents an individual failed query in a sharded read rows operation

### _exception_ google.cloud.bigtable.data.exceptions.InvalidChunk(message, errors=(), details=(), response=None, error_info=None)

Bases: [`google.api_core.exceptions.GoogleAPICallError`](https://googleapis.dev/python/google-api-core/latest/exceptions.html#google.api_core.exceptions.GoogleAPICallError)

Exception raised to invalid chunk data from back-end.

### _exception_ google.cloud.bigtable.data.exceptions.InvalidExecuteQueryResponse(message, errors=(), details=(), response=None, error_info=None)

Bases: [`google.api_core.exceptions.GoogleAPICallError`](https://googleapis.dev/python/google-api-core/latest/exceptions.html#google.api_core.exceptions.GoogleAPICallError)

Exception raised to invalid query response data from back-end.

### _exception_ google.cloud.bigtable.data.exceptions.MutationsExceptionGroup(excs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[google.cloud.bigtable.data.exceptions.FailedMutationEntryError], total_entries: [int](https://docs.python.org/3/builtins/functions.html#int), message: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] = None)

Bases: `google.cloud.bigtable.data.exceptions._BigtableExceptionGroup`

Represents one or more exceptions that occur during a bulk mutation operation

Exceptions will be of type FailedMutationEntryError.

  * **Parameters**

    * **excs** – the exceptions in the group

    * **total_entries** – the total number of entries attempted, successful or not

    * **message** – the message for the exception group. If None, a default message will be generated




#### _static_ __new__(cls, excs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[google.cloud.bigtable.data.exceptions.FailedMutationEntryError], total_entries: [int](https://docs.python.org/3/builtins/functions.html#int), message: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] = None)

  * **Parameters**

    * **excs** – the exceptions in the group

    * **total_entries** – the total number of entries attempted, successful or not

    * **message** – the message for the exception group. If None, a default message

  * **Returns**

the new instance

  * **Return type**

MutationsExceptionGroup




#### _classmethod_ from_truncated_lists(first_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[google.cloud.bigtable.data.exceptions.FailedMutationEntryError], last_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[google.cloud.bigtable.data.exceptions.FailedMutationEntryError], total_excs: [int](https://docs.python.org/3/builtins/functions.html#int), entry_count: [int](https://docs.python.org/3/builtins/functions.html#int))

Create a MutationsExceptionGroup from two lists of exceptions, representing a larger set that has been truncated. The MutationsExceptionGroup will contain the union of the two lists as sub-exceptions, and the error message describe the number of exceptions that were truncated.

  * **Parameters**

    * **first_list** – the set of oldest exceptions to add to the ExceptionGroup

    * **last_list** – the set of newest exceptions to add to the ExceptionGroup

    * **total_excs** – the total number of exceptions associated with the request Should be len(first_list) + len(last_list) + number of dropped exceptions in the middle

    * **entry_count** – the total number of entries attempted, successful or not

  * **Returns**

the new instance

  * **Return type**

MutationsExceptionGroup




### _exception_ google.cloud.bigtable.data.exceptions.ParameterTypeInferenceFailed()

Bases: [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError)

Exception raised when query parameter types were not provided and cannot be inferred.

### _exception_ google.cloud.bigtable.data.exceptions.RetryExceptionGroup(excs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Exception](https://docs.python.org/3/builtins/exceptions.html#Exception)])

Bases: `google.cloud.bigtable.data.exceptions._BigtableExceptionGroup`

Represents one or more exceptions that occur during a retryable operation

### _exception_ google.cloud.bigtable.data.exceptions.ShardedReadRowsExceptionGroup(excs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[google.cloud.bigtable.data.exceptions.FailedQueryShardError], succeeded: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[google.cloud.bigtable.data.row.Row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/common_data_row#google.cloud.bigtable.data.row.Row)], total_queries: [int](https://docs.python.org/3/builtins/functions.html#int))

Bases: `google.cloud.bigtable.data.exceptions._BigtableExceptionGroup`

Represents one or more exceptions that occur during a sharded read rows operation

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
