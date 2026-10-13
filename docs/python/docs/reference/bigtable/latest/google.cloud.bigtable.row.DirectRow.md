---
url: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row.DirectRow
title: Class DirectRow (2.50.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:42.288203+00:00
---

# Class DirectRow (2.50.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row.DirectRow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DirectRow (2.50.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.50.0 (latest)  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.26.0  2.25.0  2.24.0  2.23.1  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.0  2.14.1  2.13.2  2.12.0  2.11.3  2.10.1  2.9.0  2.8.1  2.7.1  2.6.0  2.5.2  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.34.0 
    
    
    DirectRow(row_key, table=None)

Google Cloud Bigtable Row for sending "direct" mutations.

These mutations directly set or delete cell contents:

  * `set_cell`
  * `delete`
  * `delete_cell`
  * `delete_cells`



These methods can be used directly::

> > > row = table.row(b'row-key1') row.set_cell(u'fam', b'col1', b'cell-val') row.delete_cell(u'fam', b'col2')

**Note:** A `DirectRow` accumulates mutations locally via the `set_cell`, `delete`, `delete_cell` and `delete_cells` methods. To actually send these mutations to the Google Cloud Bigtable API, you must call `commit`. 

## Parameters  
  
---  
**Name** | **Description**  
`row_key` |  `bytes`   
The key for the current row.  
`table` |  `[Table](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table)`   
(Optional) The table that owns the row. This is used for the :meth: `commit` only. Alternatively, DirectRows can be persisted via [mutate_rows](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table).  
  
## Properties 

### row_key

Row key.

For example:

.. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_row_key] :end-before: [END bigtable_api_row_row_key] :dedent: 4

**Returns**  
---  
**Type** | **Description**  
`bytes` | The key for the current row.  
  
### table

Row table.

For example:

.. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_table] :end-before: [END bigtable_api_row_table] :dedent: 4

**Returns**  
---  
**Type** | **Description**  
`table: [Table](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table)` | table: The table that owns the row.  
  
## Methods 

### clear
    
    
    clear()

Removes all currently accumulated mutations on the current row.

For example:

.. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_clear] :end-before: [END bigtable_api_row_clear] :dedent: 4

### commit
    
    
    commit()

Makes a `MutateRow` API request.

If no mutations have been created in the row, no request is made and a ValueError is raised instead.

Mutations are applied atomically and in order, meaning that earlier mutations can be masked / negated by later ones. Cells already present in the row are left unchanged unless explicitly changed by a mutation.

After committing the accumulated mutations, resets the local mutations to an empty list.

For example:

.. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_commit] :end-before: [END bigtable_api_row_commit] :dedent: 4

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if no mutations have been created in the row or if the number of mutations is greater than 100,000.  
**Returns**  
---  
**Type** | **Description**  
``google.rpc.status_pb2.Status`` | A response status (`google.rpc.status_pb2.Status`) representing success or failure of the row committed.  
  
### delete
    
    
    delete()

Deletes this row from the table.

**Note:** This method adds a mutation to the accumulated mutations on this row, but does not make an API request. To actually send an API request (with the mutations) to the Google Cloud Bigtable API, call `commit`.  .. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_delete] :end-before: [END bigtable_api_row_delete] :dedent: 4

### delete_cell
    
    
    delete_cell(column_family_id, column, time_range=None)

Deletes cell in this row.

**Note:** This method adds a mutation to the accumulated mutations on this row, but does not make an API request. To actually send an API request (with the mutations) to the Google Cloud Bigtable API, call `commit`.  .. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_delete_cell] :end-before: [END bigtable_api_row_delete_cell] :dedent: 4

**Parameters**  
---  
**Name** | **Description**  
`column_family_id` |  `str`   
The column family that contains the column or columns with cells being deleted. Must be of the form `<code>_a-zA-Z0-9][-_.a-zA-Z0-9]</code>*`.  
`column` |  `bytes`   
The column within the column family that will have a cell deleted.  
`time_range` |  ``TimestampRange``   
(Optional) The range of time within which cells should be deleted.  
  
### delete_cells
    
    
    delete_cells(column_family_id, columns, time_range=None)

Deletes cells in this row.

**Note:** This method adds a mutation to the accumulated mutations on this row, but does not make an API request. To actually send an API request (with the mutations) to the Google Cloud Bigtable API, call `commit`.  .. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_delete_cells] :end-before: [END bigtable_api_row_delete_cells] :dedent: 4

**Parameters**  
---  
**Name** | **Description**  
`column_family_id` |  `str`   
The column family that contains the column or columns with cells being deleted. Must be of the form `<code>_a-zA-Z0-9][-_.a-zA-Z0-9]</code>*`.  
`columns` |  ``list` of `str` / `unicode `, or `object``   
The columns within the column family that will have cells deleted. If `ALL_COLUMNS` is used then the entire column family will be deleted from the row.  
`time_range` |  ``TimestampRange``   
(Optional) The range of time within which cells should be deleted.  
  
### get_mutations_size
    
    
    get_mutations_size()

Gets the total mutations size for current row

For example:

.. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_get_mutations_size] :end-before: [END bigtable_api_row_get_mutations_size] :dedent: 4

### set_cell
    
    
    set_cell(column_family_id, column, value, timestamp=None)

Sets a value in this row.

The cell is determined by the `row_key` of this `DirectRow` and the `column`. The `column` must be in an existing `.ColumnFamily` (as determined by `column_family_id`).

**Note:** This method adds a mutation to the accumulated mutations on this row, but does not make an API request. To actually send an API request (with the mutations) to the Google Cloud Bigtable API, call `commit`.  .. literalinclude:: snippets_table.py :start-after: [START bigtable_api_row_set_cell] :end-before: [END bigtable_api_row_set_cell] :dedent: 4

**Parameters**  
---  
**Name** | **Description**  
`column_family_id` |  `str`   
The column family that contains the column. Must be of the form `<code>_a-zA-Z0-9][-_.a-zA-Z0-9]</code>*`.  
`column` |  `bytes`   
The column within the column family where the cell is located.  
`value` |  `bytes or `int``   
The value to set in the cell. If an integer is used, will be interpreted as a 64-bit big-endian signed integer (8 bytes).  
`timestamp` |  ``datetime.datetime``   
(Optional) The timestamp of the operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
