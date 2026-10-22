---
url: https://docs.cloud.google.com/bigtable/docs/table-stats/
title: Table stats \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:30.642175+00:00
---

# Table stats  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/table-stats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Table stats

Bigtable provides _table stats_ — metadata about a table — that give you summary information about the table, such as the number of rows or average number of cells per column.

This document describes table stats and explains how to get them using the Google Cloud CLI. Before you read this page, you should understand the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model) and be familiar with [schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design) and [garbage collection](https://docs.cloud.google.com/bigtable/docs/garbage-collection).

Table stats provide observability into a Bigtable table. They can be useful when you are troubleshooting issues with performance or storage or when you want to determine the source of storage costs. They can also help you determine whether you are storing more data than you need.

## Expected precision

When you retrieve table stats for a table, the data that you get is approximate – the table stats reflect the state of your table in one of your instance's clusters as of the most recent compaction.

A full set of table stats is not available until after initial [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions), which typically occurs about a week after the table is created. Table stats are accurate as of the most recent compaction, which might be as much as a week ago.

## Table stats fields

A request for a table's table stats returns the following fields. Details and examples are in the next section.

**Table stats field** | **API name** | **Description**  
---|---|---  
Row count | `row_count` | The number of rows in the table. For details, see Row count.  
Average number of columns per row | `average_columns_per_row` | The average number of columns in each row for the entire table. For details and an example, see Average number of columns per row   
Average number of cells per column | `average_cells_per_column` | The average number of cells stored in all columns in all rows. For details, see Average number of cells per column.  
Logical data in bytes | `logical_data_bytes` | The amount of space the table occupies. For details, see Logical data in bytes.  
  
Table stats also include the following fields for each column family in the table.

**Column family stats field** | **API name** | **Description**  
---|---|---  
Average number of columns per row | `average_columns_per_row` | The average number of columns per row in the column family. For details and an example, see Average number of columns per row.  
Average number of cells per column | `average_cells_per_column` | The number of cells in each column, averaged over all rows that have columns in the column family. For details and an example, see Average number of cells per column.  
Logical data in bytes | `logical_data_bytes` | The amount of space the column family occupies. For details, see Logical data in bytes.  
  
## Table stats field details

### Row count

The row count is the number of rows in the table. Each row is identified by its row key.

### Average number of columns per row

To arrive at the average number of columns per row for a table, Bigtable counts the number of columns in the entire table and divides that value by the number of rows in the table.

**Key term** : A _column_ is the combination of column family and column qualifier in a row. If the same combination of a column family and column qualifier is used in 1,000 rows, the combination is counted as a column 1,000 times. 

As an example, consider the following table. The first row has three columns, and the second row has two columns.

Row key | Column family family-A | Column family family-B  
---|---|---  
row key 1 | family-A:qualifier-W | family-A:qualifier-X | family-B:qualifier-Y |   
row key 2 | family-A:qualifier-W |  |  | family-B:qualifier-Z  
  
The table has five columns and two rows, so the average number of columns per row is `2.5`.

This table stat gives you a general idea of whether your table is tall and narrow (few columns per row) or short and wide (many columns in each row).

### Average number of cells per column

To get the average number of cells per column for a table, Bigtable takes the total number of cells stored in the table and divides it by the number of columns in the table.

**Key term** : A _cell_ contains a timestamped value for a column. Every column contains at least one cell. 

Depending on your schema design and garbage collection policies, your table might have multiple cells in a column, or it might have only one. The number of cells that you can store is bound by the data size limits outlined on the Quotas and limits page under [Data size within tables](https://docs.cloud.google.com/bigtable/quotas#limits-data-size).

If you find that this number is higher than you expect, examine your garbage collection rules to see if you are retaining more cells than you need. You might also ask whether your schema and write patterns should be adjusted.

### Logical data in bytes (table)

This value represents the approximate number of bytes that would be needed to read your entire table. This table stat gives you an idea of how many bytes are stored in the table. Knowing the logical data in bytes can help you understand the impact of compression on the table. For example, if the table size reported in Cloud Monitoring is the same as or larger than logical data in bytes for the table, then you might be storing your data in a format that isn't easily compressed.

## Column family stats field details

Table stats for a table include the following fields for each column family in the table.

### Average number of columns per row

This number is calculated by taking the number of columns in the column family and dividing that number by the number of rows in the table.

As an example, consider the following table. The table has three rows with columns in column families `family-A` and `family-B`.

Row key | Column family family-A | Column family family-B  
---|---|---  
row key 1 | family-A:qualifier-W | family-A:qualifier-X | family-B:qualifier-Y |   
row key 2 | family-A:qualifier-W |  |  |   
row key 3 | family-A:qualifier-W | family-A:qualifier-X | family-B:qualifier-Y | family-B:qualifier-Z  
  
Column family `family-A` has a total of five columns in the table. Divided by three rows, that means that the average number of cells per column for `family-A` is `1.67` (rounded here to two decimal places).

Column family `family-B` has a total of three columns in the table. Divided by three rows, the average number of columns per row for `family-A` is `1`.

### Average number of cells per column

To determine a column family's average number of cells per column, Bigtable takes the count of all cells in the column family in all rows of the table and divides it by the number of rows in the table.

As an example, consider the following rows in column family `family-D`.

Row key | Column family family-D  
---|---  
row key 1 | family-D:qualifier-W (3 cells) | family-D:qualifier-X (1 cell) |   
row key 2 |  | family-D:qualifier-X (10 cells) |   
row key 3 | family-D:qualifier-W (7 cells) |  | family-D:qualifier-Y (6 cells)  
  
The count of cells in the column family is 3 + 1 + 10 + 7 + 6 = 27. That value divided by 3 (the number of rows) means that column family `family-D` has an average of cells per column of `9`.

### Logical data in bytes (column family)

The logical data in bytes reflects the space that the column family occupies. This value is approximately the number of bytes that you need to read all the data in the column family at the time the table stats were returned.

## Example using the gcloud CLI

To get table stats for a table called `sample-table`, use the [`bigtable instances table describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe) command:
    
    
    gcloud bigtable instances tables describe TABLE_ID \
        --instance=INSTANCE_ID --view stats
    

Replace the following:

  * `TABLE_ID`: the permanent identifier for the table
  * `INSTANCE_ID`: the permanent identifier for the instance



The output is similar to the following:
    
    
      columnFamilies:
        my-family:
         stats:
           averageCellsPerColumn: 12.34
           averageColumnsPerRow: 56.78
           logicalDataBytes: 314159
      name: projects/my-project/instances/INSTANCE_ID/tables/TABLE_ID
      stats:
        averageCellsPerColumn: 12.34
        averageColumnsPerRow: 56.78
        logicalDataBytes: 314159
        rowCount: 271828

## What's next

  * [Monitor your Bigtable resources.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)
  * [Use Key Visualizer to analyze your usage patterns.](https://docs.cloud.google.com/bigtable/docs/keyvis-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
