---
url: https://docs.cloud.google.com/spanner/docs/modify-gcloud/
title: Inserting, updating, and deleting data using the Google Cloud CLI \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:53.083667+00:00
---

# Inserting, updating, and deleting data using the Google Cloud CLI  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/modify-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Inserting, updating, and deleting data using the Google Cloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to insert, update, and delete data using the [`gcloud`](https://docs.cloud.google.com/sdk) command-line tool.

## Modifying data using DML

To execute Data Manipulation Language (DML) statements, use the `gcloud spanner databases execute-sql` command . The following example adds a new row to the `Singers` table.
    
    
    gcloud spanner databases execute-sql example-db --instance=test-instance \
        --sql="INSERT Singers (SingerId, FirstName, LastName) VALUES (1, 'Marc', 'Richards')"

To execute a Partitioned DML statement, use the `gcloud spanner databases execute-sql` command with the `--enable-partitioned-dml` option. The following example updates rows in the `Albums` table.
    
    
    gcloud spanner databases execute-sql example-db \
        --instance=test-instance --enable-partitioned-dml \
        --sql='UPDATE Albums SET MarketingBudget = 0 WHERE MarketingBudget IS NULL'

**Note:** Spanner does not support `--query-mode=PLAN` and `--query-mode=PROFILE` for partitioned DML.

For the Spanner DML reference, see [Data Manipulation Language syntax](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/dml-syntax).

## Modifying rows using the rows command group

Use the `gcloud spanner rows` command group to modify data in a database:

  * Insert new rows into a table.
  * Update columns in existing rows in a table.
  * Delete rows from a table.



The `rows` command group recognizes literals for all [valid column types](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#allowable_types).

### Insert a row in a table

To insert a new row in a table, you must include values for the key columns and any other required columns:
    
    
    gcloud spanner rows insert --instance=INSTANCE_ID --database=DATABASE_ID \
        --table=TABLE_NAME \
        --data=COL_NAME_1=COL_VALUE_1,COL_NAME_2=COL_VALUE_2,COL_NAME_3=COL_VALUE_3,...,COL_NAME_N=COL_VALUE_N

The following example inserts a new row in the `Singers` table:
    
    
    gcloud spanner rows insert --instance=test-instance --database=example-db \
        --table=Singers \
        --data=SingerId=1,FirstName='Marc',LastName='Richards'

### Update a row in a table

To update a row in a table, you must include values for the key columns and the columns you want to update:
    
    
    gcloud spanner rows update --instance=INSTANCE_ID --database=DATABASE_ID \
        --table=TABLE_NAME \
        --data=COL_NAME_1=COL_VALUE_1,COL_NAME_2=COL_VALUE_2,COL_NAME_3=COL_VALUE_3,...,COL_NAME_N=COL_VALUE_N

The following example updates a row in the `Singers` table:
    
    
    gcloud spanner rows update --instance=test-instance --database=example-db \
        --table=Singers \
        --data=SingerId=1,FirstName='Marc',LastName='Richards'

You cannot change the key values using the `update` command. To update a key value, you must create a new row and delete the existing row.

### Delete a row from a table

To delete a row, you must specify the values for the primary key columns:
    
    
    gcloud spanner rows delete --instance=INSTANCE_ID --database=DATABASE_ID  \
        --table=TABLE_NAME \
        --keys=KEY_VALUE_1,KEY_VALUE_2,KEY_VALUE_3

The following example deletes a row from the `Singers` table: 
    
    
    gcloud spanner rows delete --instance=test-instance --database=example-db \
        --table=Singers \
        --keys=1

### Specify ARRAY values

To insert or update values in an [`ARRAY` column](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/arrays), put the data in a YAML file and use the [`--flags-file`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) option.

For example, this YAML file specifies the array `[1,2,3]` for the `Numbers` column:
    
    
    # stats.yaml
    --data:
        Id: 1
        Locked: True
        Numbers:
            -   1
            -   2
            -   3
    

To insert a row with the YAML data, use the `--flags-file` option:
    
    
    gcloud spanner rows insert --instance=test-instance --database=example-db \
         --table=Stats \
         --flags-file stats.yaml

For a `NULL` array, don't include a value for `Numbers` in the file:
    
    
    # stats.yaml
    --data:
        Id: 1
        Locked: True
    

For an empty array, define the array as `[]`:
    
    
    # stats.yaml
    --data:
        Id: 1
        Locked: True
        Numbers: []
    

### Specify commit timestamps

To insert or update a value automatically in a [commit timestamp](https://docs.cloud.google.com/spanner/docs/commit-timestamp) column, pass `spanner.commit_timestamp()` as the value of the column. The following example writes the commit timestamp in the `LastUpdated` column when the row is inserted.
    
    
    gcloud spanner rows insert --instance=test-instance --database=example-db \
        --table=Singers \
        --data=SingerId=1,LastUpdated='spanner.commit_timestamp()'

The following example writes a specific timestamp value in the `LastUpdated` column:
    
    
    gcloud spanner rows update --instance=test-instance --database=example-db \
        --table=Singers \
        --data=SingerId=1,LastUpdated=2017-01-02T12:34:00.45Z

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
