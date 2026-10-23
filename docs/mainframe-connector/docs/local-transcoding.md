---
url: https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding/
title: Move locally transcoded mainframe data to Google Cloud \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:42.132375+00:00
---

# Move locally transcoded mainframe data to Google Cloud  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Move locally transcoded mainframe data to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to transcode mainframe data locally on the mainframe to a [supported format](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat), and then move the content to Google Cloud.

## Before you begin

[Install Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/installation) to any mainframe partitioned dataset that you want to use as a procedure library (PROCLIB).

## The `qsam` and `vsam` commands

Transcoding is the process of converting information from one form of coded representation to another. Mainframe Connector provides the `qsam` and `vsam` commands to transcode data locally on the mainframe.

The `qsam decode` and `vsam decode` commands use a COBOL copybook to convert the records of a mainframe dataset into a file format such as ORC, CSV, JSONL, or AVRO, and write the output locally or to a Cloud Storage bucket. For example, you can convert an EBCDIC-encoded QSAM dataset into UTF-8 ORC files. For all the supported output formats, see [`TranscodeFormat`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat).

The `qsam encode` command does the opposite: it converts CSV, JSONL, ORC, or AVRO data, or the results of a BigQuery query, into a QSAM dataset. For all the supported input formats, see [`TranscodeInputFormat`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeinputformat).

These commands provide the following capabilities:

  * Support for compound data types, including the OCCURS clause (lists), REDEFINES clause, and nested records. For more information about these data types, see [`qsam` and `vsam` transcoding reference](https://docs.cloud.google.com/mainframe-connector/docs/qsam-vsam-transcoding).
  * Support for the configuration of the transcoding process through a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration). This capability offers more flexibility when decoding data to Google Cloud, and encoding the data back to the mainframe.
  * Support for the creation of a [spillover dataset](https://docs.cloud.google.com/mainframe-connector/docs/spillover-dataset), which is a table of transcoding errors that can be used for error inspection.
  * Support for [multiple input and output formats](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat). This capability lets you load your data to and from various data warehouses.



## Transcode mainframe data locally and move it to Google Cloud

Mainframe Connector lets you transcode data locally on the mainframe and then move it to Cloud Storage. Follow these steps:

  1. Create a job to read the dataset on your mainframe and transcode it to the ORC format. Read the data from the [`INFILE` dataset](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).

You can modify the default behavior of the Mainframe Connector transcoding process by providing a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) using the [`--transcode-configuration`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) argument.

     * If your input dataset is a Queued Sequential Access Method (QSAM) file with a fixed or variable record length, use the following command:
           
           //STEP01 EXEC BQSH
           //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
           //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.CPY
           //CONFIG DD DISP=SHR,DSN=<HLQ>.CONFIG.SETTINGS
           //STDIN DD *
           BUCKET=BUCKET_NAME
           qsam decode --copybook dd:COPYBOOK --transcode-configuration dd:CONFIG dd:INFILE gs://$BUCKET/tablename
           /*
           

     * If your input dataset is a Virtual Storage Access Method (VSAM) file with a fixed or variable record length, use the following command:
           
           //STEP01 EXEC BQSH
           //INFILE DD DSN=<HLQ>.DATA.FILENAME,DISP=SHR
           //COPYBOOK DD DISP=SHR,DSN=<HLQ>.COPYBOOK.CPY
           //CONFIG DD DISP=SHR,DSN=<HLQ>.CONFIG.SETTINGS
           //STDIN DD *
           BUCKET=BUCKET_NAME
           vsam decode --copybook dd:COPYBOOK --transcode-configuration dd:CONFIG dd:INFILE gs://$BUCKET/tablename
           /*
           

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket to which you want to copy mainframe data.

In this example, the `DD DataPath` is used to specify the path of the copybook, input, and transcoding configuration. See [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) for other options.

To avoid specifying variables such as project IDs and bucket names in each job control language (JCL) procedure, you can add them in the BQSH PROCLIB and reference them across several JCL procedures as environment variables. This approach also simplifies the transition between production and non-production environments, as environment-specific variables are set in the environment's BQSH PROCLIB.

If you want to log the commands executed during this process, you can [enable load statistics](https://docs.cloud.google.com/mainframe-connector/docs/reference#enable_load_statistics).

  2. Create and submit a BigQuery load job that loads the transcoded file to BigQuery. For example, if you transcoded the data to ORC format, you can load the ORC file partitions from `tablename.orc` into `MY_DATASET.MY_TABLE`, as follows:
         
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
  3. Optional: Create and submit a BigQuery query job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). Typically the query will be a `MERGE` or `SELECT INTO DML` statement that results in transformation of a BigQuery table. Note that Mainframe Connector logs job metrics but doesn't write query results to a file.

You can query BigQuery in various ways: inline, with a separate dataset using `DD`, or with a separate dataset using `DSN`.
         
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
     * `LOCATION`: the location where the query will be executed. We recommend that you execute the query in a location close to the data.
  4. Optional: Create and submit an export job that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and exports the resulting dataset to a mainframe as a binary file.
         
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
     * `LOCATION`: the location where the query will be executed. We recommended that you execute the query in a location close to the data.

You can modify the default behavior of the Mainframe Connector transcoding process by providing a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) using the [`--transcode-configuration`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) argument.

The data is exported to the [`OUTFILE DD`](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) dataset. The record layout is described by the [`COPYBOOK DD`](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). For other options for copybook, outfile, and transcoding configuration paths, see [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
