---
url: https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding/
title: Move data transcoded locally on the mainframe to Google Cloud \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:12.133449+00:00
---

# Move data transcoded locally on the mainframe to Google Cloud  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Move data transcoded locally on the mainframe to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses how you can transcode mainframe data locally on the mainframe to a [supported format](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat), and then move the content to BigQuery. Transcoding is the process of converting information from one form of coded representation to another. This page discusses how you can use Mainframe Connector to transcode mainframe data to optimized row columnar (ORC) and then save the data to Cloud Storage.

Mainframe Connector provides three ways in which you can transcode mainframe data locally on the mainframe.

  * Using `qsam` commands (release 5.16.0 and later)
  * Using the `vsam decode` command (release 5.18.0 and later)
  * Using the `gsutil cp` command



### Advantages of `qsam` and `vsam` commands

The `qsam` and `vsam` commands provide the following advantages:

  * Support for compound data types, including the OCCURS clause (lists), REDEFINES clause, and nested records. For more information about these data types, see [`qsam` and `vsam` transcoding reference](https://docs.cloud.google.com/mainframe-connector/docs/qsam-vsam-transcoding).
  * Support for the configuration of the transcoding process through a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration). This capability offers more flexibility when decoding data to Google Cloud, and encoding the data back to the mainframe.
  * Support for the creation of a [spillover dataset](https://docs.cloud.google.com/mainframe-connector/docs/spillover-dataset), which is a table of transcoding errors that can be used for error inspection.
  * Support for [multiple input and output formats](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat). This capability lets you load your data to and from various data warehouses.



## Before you begin

[Install Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/installation) to any mainframe-partitioned dataset that you want to use as a procedure library (PROCLIB).

## Move data transcoded locally on the mainframe to Google Cloud

To transcode data locally on a mainframe and then move it to BigQuery, you must perform the following tasks:

  1. Read and transcode a dataset on a mainframe, and upload it to Cloud Storage in the ORC format (for other formats supported only by the `qsam` or `vsam` commands, see [TranscodeFormat](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat)). Transcoding is done during the `qsam decode`, `vsam decode`, or `gsutil cp` operations (based on the command you choose), where a mainframe extended binary coded decimal interchange code (EBCDIC) dataset is converted to the ORC format in UTF-8 during the copy to a Cloud Storage bucket.
  2. Load the dataset to a BigQuery table.
  3. (Optional) Execute a SQL query on the BigQuery table.
  4. (Optional) Export data from BigQuery back to the mainframe.



The following sections describe in detail how you can move data transcoded locally on the mainframe to Google Cloud using `qsam` or `vsam` commands and the `gsutil cp` command.

### Transcode locally using `qsam` and `vsam` commands

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To transcode your mainframe data locally on your mainframe using `qsam` or `vsam` commands, use the following steps:

  1. Create a job to read the dataset on your mainframe and transcode it to the ORC format, as shown in the following command. Read the data from the [INFILE dataset](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).

You can modify the default behavior of the Mainframe Connector transcoding process by providing a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) using the [`--transcode-configuration`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) argument.

     * If your input dataset is a Queued Sequential Access Method (QSAM) file with fixed or variable record length, use the following command:
           
           //STEP01 EXEC BQSH
           //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
           //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.CPY
           //CONFIG DD DISP=SHR,DSN=<HLQ>.CONFIG.SETTINGS
           //STDIN DD *
           BUCKET=BUCKET_NAME
           qsam decode --copybook dd:COPYBOOK --transcode-configuration dd:CONFIG dd:INFILE gs://$BUCKET/tablename
           /*
           

     * If your input dataset is a Virtual Storage Access Method (VSAM) file with fixed or variable record length, use the following command:
           
           //STEP01 EXEC BQSH
           //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
           //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.CPY
           //CONFIG DD DISP=SHR,DSN=<HLQ>.CONFIG.SETTINGS
           //STDIN DD *
           BUCKET=BUCKET_NAME
           vsam decode --copybook dd:COPYBOOK --transcode-configuration dd:CONFIG dd:INFILE gs://$BUCKET/tablename
           /*
           

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket to which you want to copy mainframe data.

To avoid specifying variables such as project IDs and bucket names in each job control language (JCL) procedure, you can add them in the BQSH PROCLIB and reference them across several JCL procedures as environment variables. This approach also helps give you a seamless transition between production and non-production environments, as environment-specific variables are set in the environment's BQSH PROCLIB.

In this example, the `DD DataPath` is used to specify the path of the copybook, input, and transcoding configuration. See [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) for other options.

If you want to log the commands executed during this process, you can [enable load statistics](https://docs.cloud.google.com/mainframe-connector/docs/reference#enable_load_statistics).

  2. Create and submit a BigQuery load job that loads ORC file partitions from `tablename.orc` into `MY_DATASET.MY_TABLE`, as follows.
         
         Example JCL
         //STEP02 EXEC BQSH
         //STDIN DD *
         BUCKET=BUCKET_NAME
         PROJECT=PROJECT_NAME
         bq load --project_id=$PROJECT \
           myproject:MY_DATASET.MY_TABLE \
           gs://$BUCKET/tablename.orc/*
         /*
         

Replace the following:

     * `BUCKET_NAME`: the name of the Cloud Storage bucket which contains the ORC files that you want to load to BigQuery.
     * `PROJECT_NAME`: the name of the project in which you want to execute the query.
  3. (Optional) Create and submit a BigQuery query job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). Typically the query will be a `MERGE` or `SELECT INTO DML` statement that results in transformation of a BigQuery table. Note that Mainframe Connector logs in job metrics but doesn't write query results to a file.

You can query BigQuery in various ways - inline, with a separate dataset using DD, or with a separate dataset using DSN.
         
         Example JCL
         //STEP03 EXEC BQSH
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         PROJECT=PROJECT_NAME
         LOCATION=LOCATION
         bq query --project_id=$PROJECT \
         --location=$LOCATION/*
         /*
         

Replace the following:

     * `PROJECT_NAME`: the name of the project in which you want to execute the query.
     * `LOCATION`: The location for where the query will be executed. We recommended that you execute the query in a location close to the data.
  4. (Optional) Create and submit an export job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and exports the resulting dataset to a mainframe as a binary file.

You can modify the default behavior of the Mainframe Connector transcoding process by providing a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) using the [`--transcode-configuration`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) argument.
         
         //STEP04 EXEC BQSH
         //OUTFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
         //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.CPY
         //CONFIG DD DISP=SHR,DSN=<HLQ>.CONFIG.SETTINGS
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         
         PROJECT=PROJECT_NAME
         qsam encode \
           dd:QUERY
           dd:OUTFILE
           --copybook dd:COPYBOOK
           --transcode-configuration dd:CONFIG
           --input-format=BIGQUERY \
           --input-parameter project_id=PROJECT_NAME \
           --input-parameter location=LOCATION/*
         /*
         

Replace the following:

     * `PROJECT_NAME`: the name of the project in which you want to execute the query.
     * `LOCATION`: The location for where the query will be executed. We recommended that you execute the query in a location close to the data.

The data is exported to the [OUTFILE DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) dataset. The record layout is described by the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). For other options for copybook, outfile, and transcoding configuration paths, see [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath).




### Transcode locally using `gsutil cp` command

To transcode your mainframe data locally on your mainframe using the `gsutil cp` command, use the following steps:

  1. Create a job to read the dataset on your mainframe and transcode it to the ORC format, as shown in the following command. Read the data from the [INFILE dataset](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).

The input dataset must be a Queued Sequential Access Method (QSAM) file with fixed or variable record length.
         
         //STEP01 EXEC BQSH
         //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
         //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.FILENAME
         //STDIN DD *
         BUCKET=BUCKET_NAME
         gsutil cp --replace gs://$BUCKET/tablename.orc
         /*
         

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket to which you want to copy mainframe data.

**Note**
     * From version 5.12.0 onwards, Mainframe Connector replaces hyphens ("-") with underscores ("_") in variable names. If you want to keep hyphens in your variable names, disable this automatic conversion by setting the database variable `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME` to `false`.
     * Variables with the suffix `FILLER` are ignored during the import process.

To avoid specifying variables such as project IDs and bucket names in each JCL procedure, you can add them in the BQSH PROCLIB and reference them across several JCL procedures as environment variables. This approach also helps give you a seamless transition between production and non-production environments, as environment-specific variables are set in the environment's BQSH PROCLIB. For the complete list of environment variables supported by Mainframe Connector, see [Environment variables](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables).

In this example, standard input (STDIN) is provided as in-stream data to the [STDIN DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). Alternately, you can provide this input using a data source name (DSN), which makes it easier to manage symbol substitution.

If you want to log the commands executed during this process, you can [enable load statistics](https://docs.cloud.google.com/mainframe-connector/docs/reference#enable_load_statistics).

  2. Create and submit a BigQuery load job that loads ORC file partitions from `tablename.orc` into `MY_DATASET.MY_TABLE`, as follows.
         
         Example JCL
         //STEP02 EXEC BQSH
         //STDIN DD *
         BUCKET=BUCKET_NAME
         PROJECT=PROJECT_NAME
         bq load --project_id=$PROJECT \
           myproject:MY_DATASET.MY_TABLE \
           gs://$BUCKET/tablename.orc/*
         /*
         

Replace the following:

     * `BUCKET_NAME`: the name of the Cloud Storage bucket which contains the ORC files that you want to load to BigQuery.
     * `PROJECT_NAME`: the name of the project in which you want to execute the query.
  3. (Optional) Create and submit a BigQuery query job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). Typically the query will be a `MERGE` or `SELECT INTO DML` statement that results in transformation of a BigQuery table. Note that Mainframe Connector logs in job metrics but doesn't write query results to a file.

You can query BigQuery in various ways - inline, with a separate dataset using DD, or with a separate dataset using DSN.
         
         Example JCL
         //STEP03 EXEC BQSH
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         PROJECT=PROJECT_NAME
         LOCATION=LOCATION
         bq query --project_id=$PROJECT \
         --location=$LOCATION/*
         /*
         

Replace the following:

     * `PROJECT_NAME`: the name of the project in which you want to execute the query.
     * `LOCATION`: The location for where the query will be executed. We recommended that you execute the query in a location close to the data.
  4. (Optional) Create and submit an export job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and exports the resulting dataset to a mainframe as a binary file.
         
         Example JCL
         //STEP04 EXEC BQSH
         //OUTFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
         //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.FILENAME
         //QUERY DD DSN=<HLQ>.QUERY.FILENAME,DISP=SHR
         //STDIN DD *
         PROJECT=PROJECT_NAME
         DATASET_ID=DATASET_ID
         DESTINATION_TABLE=DESTINATION_TABLE
         bq export --project_id=$PROJECT \
           --dataset_id=$DATASET_ID \
           --destination_table=$DESTINATION_TABLE \
           --allow_large_results \
           --location="US" \
           --remoteHost <mainframe-connector-url>.a.run.app \
           --remotePort 443
         /*
         

Replace the following:

     * `PROJECT_NAME`: The name of the Google Cloud project in which you want to execute the query.
     * `DATASET_ID`: The BigQuery dataset ID. It is used as the fallback dataset for any table names in the SQL query that don't explicitly specify a dataset. It is also used to resolve the location of the DESTINATION_TABLE if a dataset is not explicitly defined in the table spec.
     * `DESTINATION_TABLE`: An intermediate BigQuery table where the query results are written before being exported. This is only used if `allow_large_results` is set. If `allow_large_results` is `false` or omitted, query results are written to an anonymous temporary table instead.

The data is exported to the [OUTFILE DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) dataset. The record layout is described by the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
