---
url: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations
title: Module mutations (2.50.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:33.119881+00:00
---

# Module mutations (2.50.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module mutations (2.50.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.50.0 (latest)  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.26.0  2.25.0  2.24.0  2.23.1  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.0  2.14.1  2.13.2  2.12.0  2.11.3  2.10.1  2.9.0  2.8.1  2.7.1  2.6.0  2.5.2  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.34.0 

API documentation for `bigtable.data.mutations` module.

## Classes 

### [AddToCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.AddToCell)
    
    
    AddToCell(family: str, qualifier: bytes | str, value: int, timestamp_micros: int)

Adds an int64 value to an aggregate cell. The column family must be an aggregate family and have an "int64" input type or this mutation will be rejected.

Note: The timestamp values are in microseconds but must match the granularity of the table (defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If `qualifier` is not `bytes` or `str`.  
`TypeError` | If `value` is not `int`.  
`TypeError` | If `timestamp_micros` is not `int`.  
`ValueError` | If `value` is out of bounds for a 64-bit signed int.  
`ValueError` | If `timestamp_micros` is less than 0.  
  
### [DeleteAllFromFamily](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteAllFromFamily)
    
    
    DeleteAllFromFamily(family_to_delete: str)

Mutation to delete all cells from a column family.

### [DeleteAllFromRow](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteAllFromRow)
    
    
    DeleteAllFromRow()

Mutation to delete all cells from a row.

### [DeleteRangeFromColumn](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteRangeFromColumn)
    
    
    DeleteRangeFromColumn(
        family: str,
        qualifier: bytes,
        start_timestamp_micros: typing.Optional[int] = None,
        end_timestamp_micros: typing.Optional[int] = None,
    )

Mutation to delete a range of cells from a column.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `start_timestamp_micros` is greater than `end_timestamp_micros`.  
  
### [Mutation](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.Mutation)
    
    
    Mutation()

Abstract base class for mutations.

This class defines the interface for different types of mutations that can be applied to Bigtable rows.

### [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.RowMutationEntry)
    
    
    RowMutationEntry(
        row_key: bytes | str,
        mutations: (
            google.cloud.bigtable.data.mutations.Mutation
            | list[google.cloud.bigtable.data.mutations.Mutation]
        ),
    )

A single entry in a `MutateRows` request.

This class represents a set of mutations to apply to a specific row in a Bigtable table.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `mutations` is empty or contains more than `_MUTATE_ROWS_REQUEST_MUTATION_LIMIT` mutations.  
  
### [SetCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.SetCell)
    
    
    SetCell(
        family: str,
        qualifier: bytes | str,
        new_value: bytes | str | int,
        timestamp_micros: typing.Optional[int] = None,
    )

Mutation to set the value of a cell.

**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If `qualifier` is not `bytes` or `str`.  
`TypeError` | If `new_value` is not `bytes`, `str`, or `int`.  
`ValueError` | If `timestamp_micros` is less than `_SERVER_SIDE_TIMESTAMP`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
