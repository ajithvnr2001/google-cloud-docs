---
url: https://docs.cloud.google.com/alloydb/docs/measure-address-table-index-bloat/
title: Measure and address table and index bloat \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:59.686163+00:00
---

# Measure and address table and index bloat  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/measure-address-table-index-bloat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Measure and address table and index bloat Stay organized with collections  Save and categorize content based on your preferences. 

Table and index bloat occurs when the vacuum operation doesn't keep up with the rate of Data Manipulation Language (DML) against a table. Some table and index bloat is unavoidable and generally acceptable because transactions can reuse that space. Severe bloat causes performance issues, such as slower query times, increased I/O, less efficient shared buffer and cache usage, and increased storage costs.

The best way to estimate bloat is to use the [`pgstattuple`](https://www.postgresql.org/docs/current/pgstattuple.html) module. However, using `pgstattuple` is less efficient when the extension must read all the pages of a relation. If you can't use `pgstattuple`, you can use other scripts to estimate bloat, although this approach provides less accuracy.

## Read pgstattuple output

When you use `pgstattuple` to report the physical storage characteristics of a table or index, the output is in the following format:
    
    
    > SELECT * FROM pgstattuple('large_table');
    -[ RECORD 1 ]------+-----------
    table_len          | 7431888896
    tuple_count        | 66666666
    tuple_len          | 2796296271
    tuple_percent      | 37.63
    dead_tuple_count   | 0
    dead_tuple_len     | 0
    dead_tuple_percent | 0
    free_space         | 3873153652
    free_percent       | 52.12
    

The following describes the output:

`table_len` (`7431888896`)
    The total size of the table in bytes. It includes all live tuples, dead tuples, and free space. In this case, `large_table` occupies approximately 7,088 GB.
`tuple_count` (`66666666`)
    Represents the number of live tuples—visible and active rows—that are in the table. The table contains approximately 66 million active rows.
`tuple_len` (`2796296271`)
    The total length in bytes of all the live tuples combined, which is approximately 2.6 GB.
`tuple_percent` (`37.63`)
    

The percentage of the `table_len` that live tuples occupy. You calculate it as follows:

(`tuple_len`/`table_len`) ∗ 100 = (`2796296271`/`7431888896`) ∗ 100 ≈ `37.63` percent

    

This output indicates that active data uses less than 40% of the table's disk space.

`dead_tuple_count` (`0`)
    

The number of dead tuples—rows that vacuum operations haven't yet removed after updates or deletions. A value of `0` means that the table is clean and has no dead tuples waiting to be reclaimed. This often suggests that `VACUUM`, or autovacuum, runs efficiently on the table.

`dead_tuple_len` (`0`)
    

The total length in bytes of all the dead tuples. Consistent with `dead_tuple_count`, a value of `0` means that dead rows don't consume any space.

`dead_tuple_percent` (`0`)
    

The percentage of the `table_len` that dead tuples occupy. You calculate it as follows:

(`dead_tuple_len`/`table_len`) ∗ 100 = (`0`/`7431888896`) ∗ 100 = `0` percent

`free_space` (`3873153652`)
    

This value represents the amount of free space in the table's data pages. You can reuse this space for new inserts or updates without requiring table expansion. This indicates a significant amount of free space, approximately 3.7 GB.

`free_percent` (`52.12`)
    

This value represents the percentage of the `table_len` that's free space. You calculate it as follows:

(`free_space`/`table_len`) ∗ 100 = (`3873153652`/`7431888896`) ∗ 100 ≈ `52.12` percent

## Estimate bloat using queries

You can estimate bloat using queries against system catalog tables, though this method is less accurate than using extensions such as `pgstattuple`. If you use scripts like [PostgreSQL table bloat check](https://docs.cloud.google.com/alloydb/docs/reference/postgres-table-bloat-check), your table statistics must be up to date, otherwise the estimate is inaccurate.

When you compare the output of a query with the `pgstattuple` module, the estimates are comparable, but not exact measurements of bloat. The module is still the more accurate gauge of bloat because the SQL query relies on the cumulative statistics engine of PostgreSQL, whereas the module reads the actual data pages.

The following example compares the output of two different methods for analyzing table bloat in PostgreSQL for a table named `large_table`.
    
    
    > SELECT * FROM pgstattuple('large_table');
    -[ RECORD 1 ]------+-----------
    table_len          | 2475892736
    tuple_count        | 22000000
    tuple_len          | 922925931
    tuple_percent      | 37.28
    dead_tuple_count   | 0
    dead_tuple_len     | 0
    dead_tuple_percent | 0
    free_space         | 1293696900
    free_percent       | 52.25
    
    Vs.
    
    -[ RECORD 1 ]+------------
    databasename | postgres
    schemaname   | public
    tablename    | large_table
    can_estimate | t
    est_rows     | 21965400
    pct_bloat    | 54
    mb_bloat     | 1269.24
    table_mb     | 2361.195
    

## Address bloat

You can manage bloat in the following ways, each of which has advantages and disadvantages, which require careful planning:

  * Perform a full vacuum. This operation requires a full table lock for the duration of the vacuum, and requires downtime.
  * Move data to new table. To use this method, you must quiesce table changes to make sure that changes aren't transferred to the new relation.
  * Use [`pg_squeeze`](https://github.com/cybertec-postgresql/pg_squeeze). This extension mitigates bloat online. The extension creates a shadow table, inserts all the data, and then maintains table changes using a replication slot until the last step, which is switching out the bloated table with the newly created un-bloated table. Then, it requests a brief table lock to move the non-bloated table to replace the bloated table. This method requires twice the object's space for the duration of the operation, but it's the least intrusive to normal operation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
