---
url: https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding/
title: Transcode mainframe data remotely on Google Cloud \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.739463+00:00
---

# Transcode mainframe data remotely on Google Cloud  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Transcode mainframe data remotely on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Transcoding data locally on a mainframe is a CPU-intensive process that results in high million instructions per second (MIPS) consumption. To avoid this, you can use Cloud Run to move and transcode mainframe data remotely on Google Cloud to optimized row columnar (ORC) format and then move the data to Cloud Storage. This frees up your mainframe for business critical tasks and also reduces MIPS consumption.

The following figure describes how you can move your mainframe data to Google Cloud and transcode it remotely to ORC format using Cloud Run, and then move the content to BigQuery.

![Remotely transcode mainframe data](https://docs.cloud.google.com/static/mainframe-connector/docs/images/remote-transcoding-procedure.png)Remotely transcode mainframe data 

## Before you begin

  * [Deploy Mainframe Connector on Cloud Run](https://docs.cloud.google.com/mainframe-connector/docs/deploy-mainframe-connector).
  * [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) or identify an existing service account to use with Mainframe Connector. This service account must have permissions to access Cloud Storage buckets, BigQuery datasets, and any other Google Cloud resource that you want to use.
  * Verify that the service account you created is assigned the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker).



## Move mainframe data to Google Cloud and transcode it remotely using Cloud Run

To move your mainframe data to Google Cloud and transcode it remotely using Cloud Run, you must perform the following tasks:

  1. Read and transcode a dataset on a mainframe, and upload it to Cloud Storage in ORC format. Transcoding is done during the [`gsutil cp`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#gsutil_cp) operation, where a mainframe extended binary coded decimal interchange code (EBCDIC) dataset is converted to the ORC format in UTF-8 during the copy to a Cloud Storage bucket.
  2. Load the dataset to a BigQuery table.
  3. (Optional) Execute a SQL query on the BigQuery table.
  4. (Optional) Export data from BigQuery into a binary file in Cloud Storage.



To perform these tasks, follow these steps:

  1. On your mainframe, create a job to read the dataset on your mainframe and transcode it to ORC format, as follows. Read the data from the [INFILE dataset](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). The input dataset must be a queued sequential access method (QSAM) file with fixed or variable record length.

**Note**

     * Not all Google Cloud commands support remote transcoding. For more information, see [Mainframe Connector API reference](https://docs.cloud.google.com/mainframe-connector/docs/reference).
     * Variables with the suffix `FILLER` are ignored during the import process.
     * From version 5.12.0 onwards, Mainframe Connector replaces hyphens ("-") with underscores ("_") in variable names. If you want to keep hyphens in your variable names, disable this automatic conversion by setting the database variable `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME` to `false`.

For the complete list of environment variables supported by Mainframe Connector, see [Environment variables](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables).
    
    //STEP01 EXEC BQSH
    //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
    //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.FILENAME
    //STDIN DD *
    gsutil cp --replace gs://mybucket/tablename.orc --remote \
      --remoteHost <mainframe-connector-url>.a.run.app \
      --remotePort 443
    /*
    

If you want to log the commands executed during this process, you can [enable load statistics](https://docs.cloud.google.com/mainframe-connector/docs/reference#enable_load_statistics).

  2. (Optional) Create and submit a BigQuery query job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). Typically the query will be a `MERGE` or `SELECT INTO DML` statement that results in transformation of a BigQuery table. Note that Mainframe Connector logs in job metrics but doesn't write query results to a file.

You can query BigQuery in various ways-inline, with a separate dataset using DD, or with a separate dataset using DSN.
         
         Example JCL
         //STEP03 EXEC BQSH
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         PROJECT=PROJECT_NAME
         LOCATION=LOCATION
         bq query --project_id=$PROJECT \
           --location=$LOCATION \
           --remoteHost <mainframe-connector-url>.a.run.app \
           --remotePort 443/*
         /*
         

Additionally, you must set the environment variable `BQ_QUERY_REMOTE_EXECUTION=true`.

Replace the following:

     * `PROJECT_NAME`: The name of the project in which you want to execute the query.
     * `LOCATION`: The location for where the query will be executed. We recommended that you execute the query in a location close to the data.
  3. (Optional) Create and submit an export job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and exports the resulting dataset to Cloud Storage as a binary file.
         
         Example JCL
         //STEP04 EXEC BQSH
         //OUTFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
         //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.FILENAME
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         PROJECT=PROJECT_NAME
         DATASET_ID=DATASET_ID
         DESTINATION_TABLE=DESTINATION_TABLE
         BUCKET=BUCKET
         bq export --project_id=$PROJECT \
           --dataset_id=$DATASET_ID \
           --destination_table=$DESTINATION_TABLE \
           --location="US" \
           --bucket=$BUCKET \
           --remoteHost <mainframe-connector-url>.a.run.app \
           --remotePort 443
         /*
         

Replace the following:

     * `PROJECT_NAME`: The name of the project in which you want to execute the query.
     * `DATASET_ID`: The BigQuery dataset ID that contains the table that you want to export.
     * `DESTINATION_TABLE`: The BigQuery table that you want to export.
     * `BUCKET`: The Cloud Storage bucket that will contain the output binary file.



## What's next

  * [Move locally transcoded mainframe data to Google Cloud](https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding)

  * [Transcode mainframe data moved to Google Cloud using a virtual tape library](https://docs.cloud.google.com/mainframe-connector/docs/vtl-transcoding)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
