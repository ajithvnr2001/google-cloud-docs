---
url: https://docs.cloud.google.com/mainframe-connector/docs/reference/
title: Mainframe Connector reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:52.932336+00:00
---

# Mainframe Connector reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Mainframe Connector reference Stay organized with collections  Save and categorize content based on your preferences. 

## Set up Cloud Logging

For information about configuring Cloud Logging for Mainframe Connector, see [Set up Cloud Logging](https://docs.cloud.google.com/mainframe-connector/docs/set-up-cloud-logging).

## Enable load statistics

The load statistics feature logs every command that you execute using Mainframe Connector in a SQL table. To enable the load statistics feature, create a table using the following command and add the flag `--stats_table TABLE_NAME` to the `cp` command, where TABLE_NAME is the name of the SQL table.
    
    
    CREATE TABLE
      `[PROJECT_ID].[DATASET_NAME].[TABLE_NAME]` (
        timestamp TIMESTAMP,
        job_id STRING,
        job_name STRING,
        job_date DATE,
        job_time TIME,
        job_step_name STRING,
        job_type STRING,
        source STRING,
        destination STRING,
        job_json STRING,
        rows_read INT64,
        rows_written INT64,
        rows_affected INT64,
        rows_inserted INT64,
        rows_deleted INT64,
        rows_updated INT64,
        rows_unmodified INT64,
        rows_before_merge INT64,
        rows_loaded INT64,
        bq_job_id STRING,
        bq_job_project STRING,
        bq_job_location STRING,
        statement_type STRING,
        query STRING,
        execution_ms INT64,
        queued_ms INT64,
        bytes_processed INT64,
        slot_ms INT64,
        slot_utilization_rate FLOAT64,
        slot_ms_to_total_bytes_ratio FLOAT64,
        shuffle_bytes FLOAT64,
        shuffle_bytes_to_total_bytes_ratio FLOAT64,
        shuffle_spill_bytes FLOAT64,
        shuffle_spill_bytes_to_shuffle_bytes_ratio FLOAT64,
        shuffle_spill_bytes_to_total_bytes_ratio FLOAT64,
        shuffle_spill_gb FLOAT64,
        bq_stage_count INT64,
        bq_step_count INT64,
        bq_sub_step_count INT64,
        bq_stage_summary STRING)
    PARTITION BY job_date
    CLUSTER BY job_name, job_id, job_step_name
    OPTIONS (
      partition_expiration_days=1000,
      description="Log table for mainframe jobs",
      require_partition_filter=true)
    

Replace the following:

  * `PROJECT_NAME`: the name of the project in which you want to execute the command.
  * `DATASET_NAME`: the name of the dataset file.
  * `TABLE_NAME`: the name of the SQL table in which you want to log the details.



## Dataset names

You can use the following [dataset definition (DD) files](https://www.ibm.com/docs/en/zos-basic-skills?topic=concepts-jcl-statements-what-does-dd-statement-do) in your BQSH JCL procedure. Ensure that all [MVS datasets](https://www.ibm.com/docs/en/zos/3.1.0?topic=tsoe-mvs-data-sets) referenced by a DD file uses the [fixed block (FB)](https://www.ibm.com/docs/en/zos-basic-skills?topic=set-data-record-formats) record format.

DD name | Description  
---|---  
COPYBOOK | An MVS dataset containing a COBOL copybook for the dataset referenced by an INFILE DD. You can use the copybook DD with a few restrictions. For more information, see [COPYBOOK DD usage restrictions](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#native-copybook-parser).  
INFILE | An MVS dataset containing a COBOL dataset to be uploaded to Cloud Storage.  
KEYFILE | An MVS dataset containing an Identity and Access Management service account JSON keyfile.  
OUTFILE | An MVS dataset containing a COBOL dataset to be loaded from BigQuery.  
QUERY | An MVS dataset containing a BigQuery standard SQL query. The QUERY DD is a FB file with a logical record size (LRECL) of 80. This means that every record in the file is 80 bytes long.  
STDIN | Stream input used to provide shell commands.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
