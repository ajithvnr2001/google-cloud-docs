---
url: https://docs.cloud.google.com/mainframe-connector/docs/api-reference/
title: Mainframe Connector API commands \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:47:43.248910+00:00
---

# Mainframe Connector API commands  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/api-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Mainframe Connector API commands Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the BigQuery, Cloud Storage, and other Google Cloud commands that you can use with Mainframe Connector.

**Note:** For the commands that support remote execution, you can use the option `remoteUrl` instead of `remoteHost` and `remotePort`. The `remoteUrl` option must contain the scheme, host, and port. If the scheme is `https`, and no trust store is provided as an option `trustCertCollectionFilePath` or environment variable `TRUST_CERT_COLLECTION_FILE_PATH`, the system's default trust store is used.Product | Command | Description | Supports remote transcoding  
---|---|---|---  
**BigQuery commands** | 

###### [`bq export`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_export)

| Use this command to create a binary file. The command accepts a [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) as input.   
  
**Note:** We recommend that you use the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-decode) and [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-encode) commands to perform this task. For information on the advantages of using the `qsam` commands, see [Advantages of `qsam` commands](https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding#advantages_of_qsam_commands).   
  
The `bq export` command supports some performance tuning capabilities. For more information, see Performance improvements for the `bq export` command. You can use customized character sets with the `bq export` command. For more information, see Use customized character sets.   
  
**Note:** The `bq export` command fails requests to export large Bigtable tables. To avoid errors, add the `-allowLargeResults` flag to the `bq export` command when you want to export large tables. | Yes  
| 

###### [`bq load`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_load)

| Use this command to load data into a table. | No  
| 

###### [`bq mk`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_mk)

| Use this command to create BigQuery resources, such as built-in tables or external tables, that need partitioning and clustering to be set up.   
  
You can also use the `bq mk` command to generate a BigQuery table directly from parsing COBOL copybooks. For more information, see Create a BigQuery table from a copybook.  | No  
| 

###### [`bq query`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_query)

| Use this command to create a query job that runs the specified SQL query. The command reads the SQL query either from the `--sql` flag or from [QUERY DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names). If both are provided, the query in the `--sql` flag takes precedence.   
  
Use the `--follow=true` flag to generate a report that displays the results of a select query. In order to write this report to a file in the mainframe, define a DD statement `AUDITL` that points to the file that should contain the audit logs report. Don't use the `--follow` flag if you want normal logging behavior.   
  
Some query results may return a large number of rows, sometimes in millions. In order for the output to remain human readable the number of lines displayed is capped. To control the number of rows being displayed, use the `--report_row_limit` flag. For example, use `--report_row_limit 10` to limit the results to 10 lines. By default, the number of lines displayed is limited to 30.   
  
To use `bq query` parameterization, see bq query parameterization.  | Yes  
| 

###### `bq rm`

| Use this command to permanently delete a BigQuery resource. As this command permanently deletes a resource, we recommend that you use it with caution.  | No  
**Cloud Run commands** | 

###### [`cloud run job execute`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#cloud_run_job_execute)

| Use this command to trigger a Cloud Run job from your Mainframe.  | No  
| 

###### [`cloud run job logs`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#cloud_run_job_log)

| Use this command to view the logs for a specific Cloud Run job execution.  | No  
| 

###### [`cloud run job cancel`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#cloud_run_job_cancel)

| Use this command to cancel a Cloud Run job.  | No  
**Cloud Storage commands** | 

###### [`scp`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#scp)

| Use this command to copy text or binary data to Cloud Storage. You can use the simple binary copy mode to copy a dataset from [IBM z/OS](https://www.ibm.com/products/zos) to Cloud Storage unmodified as part of a data pipeline. Optionally, you can convert the character encoding from extended binary coded decimal interchange code (EBCDIC) to ASCII UTF-8, and add line breaks.   
  
**Note:** We recommend that you use the [`copy text`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#copy-text) commands to perform this task as it provides better capabilities.   
  
You can also use this command to copy application source code defined in [job control language (JCL)](https://www.ibm.com/docs/en/zos-basic-skills?topic=collection-basic-jcl-concepts).  | No  
`gsutil` utility | 

###### [`gsutil cp`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#gsutil_cp)

| Use this command to transcode a dataset and write it to Cloud Storage in the [Optimized Row Columnar (ORC)](https://orc.apache.org/) file format. The command reads the data from the [INFILE DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).   
  
**Note:** We recommend that you use the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-decode) and [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-encode) commands to perform this task. For information on the advantages of using the `qsam` commands, see [Advantages of `qsam` commands](https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding#advantages_of_qsam_commands).   
  
If you want the command to read the data from a Data Source Name (DSN) file, use the following flags: 

  * `--inDsn`: the input dataset DSN. If provided, this flag overrides INFILE DD. 
  * `--cobDsn`: the copybook DSN. If provided, this flag overrides COPYBOOK DD. 

The command then opens a configurable number of parallel connections to the Cloud Storage API and transcodes the COBOL dataset to the columnar and GZIP compressed ORC file format. You can expect about 35% compression ratio.   
  
Optionally, you can use this command to interact with the Mainframe Connector [gRPC](https://grpc.io/) service running on a VM on the mainframe. To do so, set the `SRVHOST` and `SRVPORT` environment variables, or provide the hostname and port number using command line options. When the gRPC service is used, the input dataset is first copied to Cloud Storage by the Mainframe Connector, and then a remote procedure (RPC) call is made to instruct the gRPC service to transcode the file.   
  
You can also perform the following tasks with the `gsutil cp` command: 

  * Perform a dry run of the `gsutil cp` command
  * Copy a file from Cloud Storage to your Mainframe
  * Fine tune performance of the `gsutil cp` command
  * Use customized character sets with the `gsutil cp`.

| Yes  
| 

###### [`gsutil rm`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#gsutil_rm)

| Use this command to delete buckets or objects within a bucket.  | No  
`gszutil` utility | 

###### `gszutil`

| The `gszutil` utility runs using the [IBM JZOS Java SDK](https://www.ibm.com/docs/en/semeru-runtime-ce-z/17?topic=sdk-user-guide) and provides a shell emulator that accepts `gsutil` and BigQuery command line invocations using JCL.   
  
**Note:** We recommend that you use the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-decode) and [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-encode) commands to perform this task. For information on the advantages of using the `qsam` commands, see [Advantages of `qsam` commands](https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding#advantages_of_qsam_commands).   
  
The `gszutil` utility extends the functionality of the `gsutil` utility by accepting a schema in the form of a [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), using it to transcode COBOL datasets directly to ORC before uploading to Cloud Storage. The `gszutil` utility also lets you execute BigQuery `query` and `load` using JCL.   
  
The `gszutil` utility works with the [gRPC](https://grpc.io/) server, which helps you reduce the million instructions per second (MIPS) consumption. We recommend using the `gszutil` utility in your production environment to convert binary files in Cloud Storage to the ORC format.  | No  
**`qsam` and `vsam` commands** | 

###### [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode)

| Use this command to transcode QSAM file records to the format you want using the `--output-format` argument. The original QSAM file is split into chunks based on the value you specify with the `--max-chunk-size` argument. The transcoded output is saved in the target path as lexicographically sorted files.  | No  
| 

###### [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode)

| Use this command to convert data from an external source to a QSAM file. The input is defined by the value you specify using the `--input-format` argument.  | No  
| 

###### [`vsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#vsam_decode)

| Use this command to transcode Virtual Storage Access Method (VSAM) file records to the format you want using the `--output-format` argument. The original VSAM file is split into chunks based on the value you specify with the `--max-chunk-size` argument. The transcoded output is saved in the target path as lexicographically sorted files.  | No  
**Pub/Sub commands** | 

###### [`pubsub topics publish`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#pubsub_topics_publish)

| Use this command to publish a message to a Pub/Sub topic.  | No  
**Other commands** | 

###### [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary)

| Use this command to copy a binary dataset from a source path to a destination path.  | No  
| 

###### [`copy text`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_text)

| Use this command to copy a file to a storage location of your choice, such as Cloud Storage, and the other way around.  | No  
| 

###### `curl`

| Use this command to make an HTTP request to a web service or REST APIs.  | No  
| 

###### `gcloud dataflow flex-template run`

| Use this command to trigger the execution of a Dataflow flex template. The command runs a job from the specified flex template path. For more information, see [gcloud dataflow flex-template run](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run).  | No  
| 

###### [`systemreport`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#systemreport)

| Use this command to print the necessary system data to the standard output (stdout). This allows the Mainframe Connector support team to gather the required information to diagnose an issue without the need for extensive customer interaction.   
Based on the flag you use, the `systemreport` command prints the following system data: 

  * `--supported_ciphers`: Supported ciphers
  * `--available_security_providers`: Available security providers

| No  
  
## Use customized character sets

Mainframe Connector supports different character sets that decode bytes into BigQuery strings, and the other way around. Mainframe Connector lets you configure your own customized charset. You can configure a customized character set by building a Unicode Character Mapping (UCM) file. Mainframe Connector supports the following subset of the UCM format:
    
    
    <code_set_name>               "<name>"
    <uconv_class>                 "SBCS"
    <subchar>                     \x1A #Example
    
    CHARMAP
    #_______ _________
    <U0000> \x00 |0       #For the third column, only 0 is supported.
    <U0001> \x01 |0
    #etc
    END CHARMAP
    

If you want to use a customized character set, define a configuration file in the UCM format. You can use this customized character set with the [`gsutil cp`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#gsutil-cp) or [`bq export`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#bq-export) commands by setting the `--encoding=charset` flag.

When you create a customized character set, verify the following:

  * While defining a UCM file, keep the following in mind: 
    * Mainframe Connector only supports customized character sets using a single byte character set (SBCS).
    * Mainframe Connector only supports the UCM precision indicator `|0`.
    * Verify that the UCM files are located in the z/OS Unix System Services (USS) and not on a multiple virtual storage partitioned dataset (MVS PDS).
    * Verify that the UCM files are saved in American Standard Code for Information Interchange (ASCII) format and not in the Extended Binary Coded Decimal Interchange Code (EBCDIC) format.
  * Provide explicit mapping for every possible single byte value to a Unicode character. If you're unsure about which Unicode character you want to map a byte to, we recommend that you map it to `U+FFFD`. You can map different byte sequences to the same Unicode character. However, in these cases the mapping is not bidirectional, that is, when you load data to BigQuery and later export it back to a binary file, the output might differ from the original input.
  * Verify that the byte sequences in the second column are unique. If multiple byte sequences map to the same Unicode character, this Unicode character is decoded to a byte sequence of the last defined mapping in the UCM file.
  * Verify that Mainframe Connector can find the UCM file by setting the environment variable [`BQSH_FEATURE_CUSTOM_CHARSET`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_custom_charset) to the UCM file's path. If you want to use multiple character sets, you can provide the paths to multiple characters sets separated by the semi-colon delimiter. For example, `BQSH_FEATURE_CUSTOM_CHARSET=path1;path2`. path can either point to a local file or to a file stored on Cloud Storage. If you execute the `gsutil cp` or `bq export` commands with the `--remote` flag to perform [remote transcoding](https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding), Mainframe Connector uses the local value set for the `BQSH_FEATURE_CUSTOM_CHARSET` environment variable. The same applies when you run Mainframe Connector in [standalone mode](https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode). If the `--encoding` flag refers to a customized character set that doesn't correspond to the value you set for `BQSH_FEATURE_CUSTOM_CHARSET` (or if you've not set `BQSH_FEATURE_CUSTOM_CHARSET` at all), the command exits with an error message.



## Performance tuning configuration for the `bq export` command

Mainframe Connector supports the following performance tuning configuration for the `bq export` command:

  * `exporter_thread_count`: (Optional) Set the number of worker threads. The default value is 4.
  * `max_read_streams`: (Optional) Set the maximum read streams. The default value is the same as that of the value set for `exporter_thread_count`.
  * `order_response`: (Optional) If you set this flag to true, the exporter retains the query result order. This flag affects the export performance. The default value is false.
  * `max_read_queue`: (Optional) Set the maximum number of read record queues. The default value is twice the number of threads.
  * `transcoding_buffer`: (Optional) Set the size of the transcoding buffer per thread in MBs. The default value is 20 MB.



Note that you can also try increasing the transport window size by setting the [`OVERRIDE_GRPC_WINDOW_MB`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#override_grpc_window_mb) environment variable to improve performance. The default window size is 4 MB.

## Create a BigQuery table from a copybook

You can use the `bq mk` command to generate a BigQuery table directly from parsing COBOL copybooks. The native copybook parser extracts default values from the `VALUE` clause within a copybook, and assigns them to the corresponding columns in a newly created BigQuery table.

**Note:** This feature is not supported by the legacy parser.

To help you test this feature, the `bq mk` command also provides a _dry run_ mode. This mode lets you preview the generated `CREATE TABLE SQL` command without actually creating the table in BigQuery.

The `bq mk` command provides the following configuration options to support this feature:

  * `--schema_from_copybook`: Specifies the copybook to use to create the table.
  * `--dry_run`: (Optional) When enabled, the command only prints the generated `CREATE TABLE SQL` command without executing it. This flag is set to false by default.
  * `--tablespec "[PROJECT_ID]:[DATASET].[TABLE]"`: Specifies the BigQuery project ID, dataset, and table name for the target table.
  * `--encoding`: Specifies the encoding used to read the copybook file. The default value is `CP037`.



The following `VALUE` clauses are supported:
    
    
    VAR1   PIC 9(5) VALUE 55.
    *-- Set VAR1 to 55
    VAR1   PIC X(5) VALUE aaaa. Set VAR1 to aaaa
    VAR1   PIC 9(3) COMP VALUE 3. Set VAR1 to 3 (binary)
    VAR1   PIC [9(5), X(5)] VALUE <literal>. Set VAR1 to <literal>
    VAR1   PIC [9(5), X(5)] VALUE ZERO. Set VAR1 to 0 or "0"
    VAR1   PIC [9(5), X(5)] VALUE ZEROS. Set VAR1 to 0 or "00000"
    VAR1   PIC [9(5), X(5)] VALUE ZEROES. Set VAR1 to 0 or "00000"
    VAR1   PIC X(5) VALUE SPACE. Set VAR1 to  " "
    VAR1   PIC X(5) VALUE SPACES. Set VAR1 to  "     "
    

`HIGH-VALUE` and `LOW-VALUE` clauses are supported for alphanumeric variables only.
    
    
    VAR1   PIC X(5) VALUE HIGH-VALUE. Set VAR1 to `X"FF "
    VAR1   PIC X(5) VALUE HIGH-VALUES. Set VAR1 to 0 or `X"FFFFFFFFFF"
    VAR1   PIC X(5) VALUE LOW-VALUE. Set VAR1 to `X"00" (NULL)
    VAR1   PIC X(5) VALUE LOW-VALUES. Set VAR1 to `X"0000000000" (NULL)
    VAR1   PIC X(5) VALUE QUOTE. Set VAR1 to `"`
    VAR1   PIC X(5) VALUE `QUOTES`. Set VAR1 to 0 or `""""`
    VAR1   PIC [9(5), X(5)] VALUE NULL. Not defined and won't be supported
    VAR1   PIC [9(5), X(5)] VALUE ALL <literal>. Set all fields with the value ALL to <literal>
    

## `bq query` parameterization

Mainframe Connector lets you use parameterized queries with `bq query`.

The following is an example of how to you can use a parameterized `bq query` query:

**Query file**
    
    
    SELECT * FROM `bigquery-public-data.samples.wikipedia` WHERE title = @xtitle
    

The following is an example with multiple parameters.

**Query file**
    
    
    SELECT * FROM bigquery-public-data.samples.wikipedia WHERE title = @mytitle AND num_characters > @min_chars;
    

**Execution example**
    
    
    bq query \
    --project_id=mainframe-connector-dev \
    --location="US" \
    --parameters=mytitle::Hippocrates,min_chars:INT64:42600
    

## Perform a dry run of the `gsutil cp` command

The `gsutil cp` command decodes a QSAM file using a COBOL copybook, and generates an ORC file on Cloud Storage. You can perform a dry run of the `gsutil cp` command using the `dry_run` flag and test the following steps:

  * Parse a COBOL copybook or data file and check whether it is compatible with Mainframe Connector.
  * Decode a QSAM file without writing it Cloud Storage.



Use the following command to perform a dry run:
    
    
    gsutil cp \
    --dry_run \
    gs://result-dir
    

If all steps are executed successfully, the command exits with return code 0. If any issues are encountered, an error message is displayed.

When you use the `dry_run` flag, all statistics such as total bytes read, number of written records, total errors, are logged.

If you use the `dry_run` flag and the data source doesn't exist, the command doesn't return an error. It instead only checks the copybook parser and and then completes execution.

## Copy a file from Cloud Storage to your Mainframe

You can use the `gsutil cp` command to copy a file from Cloud Storage to a Mainframe dataset. Note that you cannot copy partitioned data sets (PDS).

To copy a file from Cloud Storage to a Mainframe dataset, specify the DSN and space requirements of the file you want to download to the Mainframe in JCL, as shown in the following example:
    
    
    //OUTFILE  DD DSN=MAINFRAME.DSN.FILE,DISP=(,CATLG),
    //            RECFM=FB,DSORG=PS,
    //            SPACE=(10,(2,1),RLSE),
    //            AVGREC=M,
    //            UNIT=SYSDA
    //SYSPRINT DD SYSOUT=*
    //SYSDUMP  DD SYSOUT=*
    //STDIN DD *
    

Specify the `gsutil cp` command in the following format. If the file already exists on your Mainframe, verify that you add the \--replace flag to the command.
    
    
    gsutil cp GCS_URI DSN --recfm=RECFM --lrecl=LRECL --blksize=BLKSIZE --noseek
    

Replace the following:

  * GCS_URI: The Cloud Storage uniform resource identifier (URI) of the Cloud Storage file. For example, `gs://bucket/sample.mainframe.dsn`.
  * DSN: The DSN destination location on the Mainframe.
  * RECFM: The record format (RECFM) of the Mainframe file. The valid values are F, FB, and U. Note that these values are case-insensitive.
  * LRECL: (Optional) The record length (LRECL) of the file. The value must be an integer >= 0. If LRECL is not specified the file is assumed to be in the undefined-length record format (U).
  * BLKSIZE: (Optional) The block-size of the file. If set to 0, the system will determine the optimal block-size. The value must be an integer >= 0. If you don't specify a value, the file is treated as an unblocked file.
  * noseek: (Optional) Include this parameter if you want to improve download performance. This flag is set to false by default, that is, seek operations are enabled.



**Execution example**
    
    
    gsutil cp gs://sample-bucket/MAINFRAME.DSN.FILE MAINFRAME.DSN.FILE \
    --lrecl=16 --blksize=0 --recfm=fb
    

## Performance tuning configuration for the `gsutil cp` command

Mainframe Connector supports the following performance tuning configuration for the `gsutil cp` command.

  * Use the `--parallelism` flag to set the number of threads. The default value is 1 (single threaded).
  * Use the `--maxChunkSize` argument to set the maximum size of each chunk. Each chunk will have its own ORC file. Increase this value to reduce the number of chunks created at the cost of larger memory requirements during the transcoding process. For details, see Parse the `maxChunkSize` argument. The default value is 128 MiB.
  * Use `--preload_chunk_count` argument to set the amount of data to preload to memory while all workers are busy. This argument can improve performance at the cost of memory. The default value is 2.



**Execution example**
    
    
    gsutil cp \
      --replace \
      --parser_type=copybook \
      --parallelism=8 \
      --maxChunkSize=256MiB \
      gs://$BUCKET/test.orc
    

In this example, we've considered a large file and so have used 8 threads at which line rate is reached. If you have enough memory, we recommend that you increase the chunk size to 256 MiB or even 512 MiB since it reduces creating overhead and finalizing Cloud Storage objects. For small files using less threads and smaller chunks might produce better results.

### Parse the `maxChunkSize` argument

The `maxChunkSize` flag accepts values in the form of an amount and a unit of measurement, for example 5 MiB. You can use whitespace between the amount and magnitude.

You can provide the value in the following formats:

  * **Java format:** b/k/m/g/t, for byte, kibibyte, mebibyte, gibibyte, and tebibyte respectively
  * **International format:** KiB/MiB/GiB/TiB, for kibibyte, mebibyte, gibibyte, and tebibyte respectively
  * **Metric format:** b/kb/mb/gb/tb, for kilobyte, megabyte, gigabyte, and terabyte respectively



Data size parsing is case insensitive. Note that you can't specify partial amounts. For example, use 716 KiB instead of 0.7 MiB.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
