---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/troubleshoot-scann-indexes/
title: Troubleshoot ScaNN index errors \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:32:55.384283+00:00
---

# Troubleshoot ScaNN index errors  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/troubleshoot-scann-indexes/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Troubleshoot ScaNN index errors Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/troubleshoot-scann-indexes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/troubleshoot-scann-indexes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/troubleshoot-scann-indexes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/troubleshoot-scann-indexes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/troubleshoot-scann-indexes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/troubleshoot-scann-indexes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/troubleshoot-scann-indexes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/troubleshoot-scann-indexes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/troubleshoot-scann-indexes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/troubleshoot-scann-indexes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/troubleshoot-scann-indexes)

This document describes errors you might encounter when you generate a ScaNN index. Examples of errors and recommended fixes are also provided. 

## Cannot create ScaNN index with empty table

### Description

When you try to generate an index on a table with no data, or if you try to truncate a table with a ScaNN index generated on it, the following error occurs:
    
    
    ERROR: Cannot create ScaNN index "[INDEX_NAME]" for table "[TABLE_NAME]", error: FAILED_PRECONDITION: Cannot create ScaNN index "[INDEX_NAME]" with empty table "[TABLE_NAME]". Once the table is populated with data, create the index. See documentation to bypass this validation.
    

### Sample queries that cause the error

  * Query Example A
        
        create table t1 (a INT, b VECTOR(512));
        CREATE TABLE
        create index on t1 using ScaNN(b cosine) with (num_leaves = 10, quantizer = 'sq8');
        

  * Query Example B
        
        truncate t1;
        




### Recommended fix

  * Before you generate a ScaNN index, make sure that your table is populated with embedding vectors.
  * To create an index on a table with no data, you can enable deferred index creation. For more information, see [Create a deferred index for empty or nearly empty tables](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/create-scann-index#deferred-index-creation-for-empty-tables-insufficient-rows).



## Cannot create ScaNN index

### Description

When you try to generate an index on a table with few rows populated, the following error occurs:
    
    
    ERROR: Cannot create ScaNN index "[INDEX_NAME]" for table "[TABLE_NAME]", error: INVALID_ARGUMENT: Number of rows ([ACTUAL]) must be larger than ([EXPECTED]).
    

### Sample query that causes the error
    
    
    create table t1 (a INT, b VECTOR(512));
    CREATE TABLE
    insert into t1 select (random()*1e9)::int, random_vector(512) from generate_series(1, 5);
    INSERT 0 5
    create index on t1 using scann(b cosine) with (num_leaves = 100, quantizer = 'sq8');
    

### Recommended fix

  * Before you generate a ScaNN index, make sure that your table is populated with embedding vectors. The required number of rows depends on the index creation mode: 
    * For `AUTO` mode, we recommend at least 10,000 rows.
    * For `MANUAL` mode, we recommend that the number of rows in the table is greater than the value defined in the `num_leaves` parameter.
  * To create an index on a table with an insufficient number of rows, you can enable deferred index creation. For more information, see [Create a deferred index for empty or nearly empty tables](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/create-scann-index#deferred-index-creation-for-empty-tables-insufficient-rows).



## Cannot create ScaNN index for a table with only one row

### Description

This error happened because ScaNN (and most ANN indexes like IVFFlat) needs a training set to build its internal structures (clusters/leaves). When you insert exactly one row , you get the following error:
    
    
    ERROR: Cannot create ScaNN index "[INDEX_NAME]" for table "[TABLE_NAME]", error: INVALID_ARGUMENT: Number of samples "[NUM_SAMPLES]" must be larger than 1 and the number of leaves "[NUM_LEAVES]"
    

### Sample query that causes the error
    
    
    create table t1 (a INT, b VECTOR(512));
    CREATE TABLE
    insert into t1 select (random()*1e9)::int, random_vector(512) from generate_series(1, 1);
    INSERT 0 1
    create index on t1 using scann(b cosine) with (num_leaves = 1, quantizer = 'sq8');
    

### Recommended fix

Make sure that your table is populated with embedding vectors before you generate a ScaNN index. We recommend that the number of rows in the table is:

  * Greater than 1
  * Greater than the value defined in the `num_leaves` parameter



## Cannot create an automatically-tuned ScaNN index for a table with less than 10k rows

### Description

This error occurs when you try to create an [automatically-tuned](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/create-scann-index#create-auto-tuned-scann-index) ScaNN index on a table that has less than 10k rows. When you try to do so, you receive the following error:
    
    
    "ERROR: Cannot create ScaNN index "products_embedding_idx" for table "products", error: FAILED_PRECONDITION: Number of rows: 100 must be 10000 or more."
    

### Sample query that causes the error
    
    
    CREATE INDEX product_index ON product
    USING scann (embedding cosine)
    

### Recommended fix

Ensure that your table has at least 10k rows before trying to create an automatically-tuned ScaNN index. If you need to override this limit for development or testing purposes, see [Force index creation on empty or small tables](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/create-scann-index#force-index-creation).

## Cannot create ScaNN index on parent partition table

### Description

If you created partitioned tables from a parent table, then creating a ScaNN index on the parent table generates the following error:
    
    
    ERROR: Cannot create ScaNN index "[INDEX_NAME]" for parent partition table
    "[TABLE_NAME]". Create ScaNN indexes on the child tables instead. See
    documentation to bypass this validation.
    

### Sample query that causes the error
    
    
    create table t1 (a INT, b VECTOR(512)) partition by range(a);
    CREATE TABLE
    CREATE TABLE t1_one_ten PARTITION of t1 for values from (1) to (10);
    CREATE TABLE
    insert into t1_one_ten select (random()*1e9)::int, random_vector(512) from generate_series(1, 100);
    INSERT 0 100
    CREATE TABLE t1_eleven_twenty PARTITION of t1 for values from (11) to (20);
    CREATE TABLE
    insert into t1_eleven_twenty select (random()*1e9)::int, random_vector(512) from generate_series(1, 100);
    INSERT 0 100
    
    create index on t1 using scann(b cosine) with (num_leaves = 10, quantizer = 'sq8');
    

### Recommended fix

  * You can't generate a `ScaNN` index on the parent table of a partitioned table.
  * You must generate the `ScaNN` indexes on the partitioned table.
  * Try bypassing this validation by following the steps in [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/create-scann-index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
