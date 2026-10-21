---
url: https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference/
title: Mainframe Connector command-line reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:23.339199+00:00
---

# Mainframe Connector command-line reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Mainframe Connector command-line reference Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the syntax, commands, flags, and arguments for the Mainframe Connector command-line tool. 

## Commands

### `agent skill-file`

Extracts the internal `SKILL` file from the Mainframe Connector JAR and creates a `mainframe-connector/SKILL.md` file in the specified output directory.

#### Synopsis
    
    
    agent skill-file [-h] --output-dir=OUTPUTDIR
    

#### Flags and arguments

The `agent skill-file` command uses the following flags and arguments:

**`--help` or `-h`**
    (Optional) Display this help message.
**`--output-dir`=OUTPUTDIR : DataPath**
    Specify the output directory.

### `bq export`

**Deprecated.** Use `qsam encode` instead. 

Export a table from BigQuery.

#### Synopsis
    
    
    bq export [options]
    

#### Flags and arguments

To run this command you must provide an SQL query (see flags `--sql` and `query_dsn`) and a copybook (see flag `cobDsn`). You can run this command in local, remote, and standalone mode. For remote mode, see the flags `--bucket`, `--remoteHost`, `--remotePort`, and `--remoteUrl`. The `bq export` command uses the following flags and arguments:

**`--project_id`=ID**
    Specify the project to use to execute this command.
**`--allow_large_results`**
    (Optional) Use large destination table sizes for legacy SQL queries.
**`--batch`**
    (Optional) Run the query in batch mode.
**`--bucket`=BUCKET**
    (Optional) Specify a location within Cloud Storage to write the command's output. If the `run_mode` is `gcsoutput`, then this parameter should be set to a Cloud Storage URI in the format `gs://example-bucket/example-prefix/example-filename.orc`. Otherwise, the output files are written to the destination path `gs://BUCKET/EXPORT/`. This argument is required for remote mode.
**`--cobDsn`=DSN**
    (Optional) Specify the copybook DSN that you want to use. If you don't provide a value, Mainframe Connector reads from [DD COPYBOOK](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--dataset_id`=ID**
    (Optional) Specify the default dataset to use with the command. You can set the value to [PROJECT_ID]:[DATASET] or [DATASET]. If [PROJECT_ID] is missing, the default project is used.
**`--destination_table`=TABLE**
    (Optional) Specify the intermediate destination table to write the query results to. To make this work, `--allow_large_results` must also be specified.
**`--dry_run`**
    (Optional) Validate the query without running it.
**`--encoding`=ENCODING**
    (Optional) Specify the character set to use for encoding and decoding character fields. When provided, this value overrides the default set by the [`ENCODING`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#encoding) environment variable.
**`--exporter_thread_count`=COUNT**
    (Optional) Set the number of exporter threads. The default value is 4.
**`--help` or `-h`**
    Display this help message.
**`--keepAliveTimeInSeconds`=SECONDS**
    (Optional) Specify the keep alive timeout in seconds for an HTTP channel. The default value 480 seconds.
**`--location`=LOCATION**
    (Optional) Specify a region or multi-region location to execute the command. The default value is US.
**`--max_read_queue`=NUMBER**
    (Optional) Set the maximum size of the Avro records queue. The default value is twice the number of threads.
**`--max_read_streams`=NUMBER**
    (Optional) Set the maximum number of read streams threads. The default value is 4.
**`--maximum_bytes_billed`=BYTES**
    (Optional) Limit the bytes billed for the query.
**`--order_response`**
    (Optional) Keep the response ordered as returned from BigQuery.
**`--outDD`=OUTPUT**
    (Optional) Write the output records to the specified dataset in z/OS. The default value is [DD OUTFILE](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--parser_type`=TYPE**
    (Optional) Set the configuration parser to `legacy`, `copybook`, or `auto`. The default value is `auto`.
**`--query_dsn`=DSN**
    (Optional) Read a query from the specified dataset in z/OS. Use the format HLQ.MEMBER or HLQ.PDS(MEMBER). If you don't provide a value, Mainframe Connector reads from [DD QUERY](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--remoteHost`=HOST**
    (Optional) Specify the IP address of the remote host. To run Mainframe Connector in remote mode, set the `--bucket` flag.
**`--remotePort`=PORT**
    (Optional) Specify the remote port. The default value is 51770. To run Mainframe Connector in remote mode, set the `--bucket` flag.
**`--remoteUrl`=URL**
    (Optional) Specify the remote URL. To run Mainframe Connector in remote mode, set the `--bucket` flag.
**`--run_mode`=MODE**
    (Optional) Select the export implementation. You can use one of the following options: 

  * `directstorage`: the binary file is saved locally (default)
  * `gcsoutput`: the binary file is saved in Cloud Storage


**`--sql`=SQL**
    (Optional) Specify the BigQuery SQL query to execute.
**`--stats_table`=TABLE**
    (Optional) Specify the table to insert statistics into.
**`--timeOutMinutes`=MINUTES**
    (Optional) Set the timeout in minutes for the remote gRPC call. The default value is 90 minutes.
**`--transcoding_buffer`=BUFFER**
    (Optional) Sets the size of the transcoding buffer per thread, in MB. The default value is 20.
**`--use_cache`={true|false}**
    (Optional) To cache the query results, set to true.
**`--use_legacy_sql`**
    (Optional) Use legacy SQL instead of standard SQL.

### `bq load`

Load data into a BigQuery table.

#### Synopsis
    
    
    bq load [options] tablespec path
    

#### Flags and arguments

The `bq load` command uses the following flags and arguments:

**path**
    Specify a comma-separated list of source file URIs. Supported format is `gs://bucket/path`. Example: `gs://my-bucket/data.orc,gs://my-bucket/more-data.orc`.
**tablespec**
    Specify the destination table for the data. The supported format is [PROJECT]:[DATASET].[TABLE]
**`--project_id`=ID**
    Specify the project to use to execute this command.
**`--allow_jagged_rows`**
    (Optional) Allow missing trailing optional columns in CSV data.
**`--allow_quoted_newlines`**
    (Optional) Allow quoted newlines within CSV data.
**`--append_table`**
    (Optional) Append the loaded data to the existing data in the destination table.
**`--autodetect`**
    (Optional) Enable automatic schema detection for CSV and JSON data.
**`--clustering_fields`=FIELDS**
    (Optional) If specified, a comma-separated list of columns is used to cluster the destination table in a query. This flag must be used with the time partitioning flags to create either an ingestion-time partitioned table or a table partitioned on a `DATE` or `TIMESTAMP` column. When specified, the table is first partitioned, and then it is clustered using the supplied columns.
**`--dataset_id`=ID**
    (Optional) Specify the default dataset to use with the command. You can set the value to [PROJECT_ID]:[DATASET] or [DATASET]. If [PROJECT_ID] is missing, the default project is used.
**`--debug_mode`={true|false}**
    (Optional) Set logging level to debug.
**`--destination_kms_key`=KEY**
    (Optional) The Cloud KMS key for encryption of the destination table data.
**`--encoding` or `-E`=ENCODING**
    (Optional) Specify the character set to use for encoding and decoding character fields. When specified, this value overrides the default set by the [`ENCODING`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#encoding) environment variable.
**`--field_delimiter` or `-F`=FIELD**
    (Optional) Specify the column delimiter in the CSV data. Use `\t` or `tab` for tab delimiters.
**`--help` or `-h`**
    Display this help message.
**`--ignore_unknown_values`=VALUES**
    (Optional) Ignore extra unrecognized values in CSV or JSON data.
**`--location`=LOCATION**
    (Optional) Specify a region or multi-region location to execute the command. The default value is US.
**`--max_bad_records`=RECORDS**
    (Optional) Set the maximum number of invalid records allowed before the job fails. A maximum of five errors of any type are returned regardless of the `--max_bad_records` value. This flag applies for loading CSV, JSON, and Google Sheets data only. The default value is 0.
**`--max_polling_interval_ms`=MILLISECONDS**
    (Optional) The maximum wait time for a BigQuery job.
**`--null_marker`=MARKER**
    (Optional) Specify a custom string that represents a `NULL` value in CSV data.
**`--projection_fields`=FIELDS**
    (Optional) If you set `--source_format` to `DATASTORE_BACKUP` then this flag indicates the entity properties to load from a datastore export. Specify the property names in a comma-separated list. Property names are case sensitive and must refer to top-level properties. You can also use this flag with Firestore exports.
**`--quote`=QUOTE**
    (Optional) Specify a quote character to surround fields in the CSV data. You can specify any one-byte character as the argument. The default value is a double quote ("). To specify that there is no quote characters, use an empty string.
**`--replace`**
    (Optional) Replace existing data in the destination table with the loaded data.
**`--require_partition_filter`={true|false}**
    (Optional) To have a partition filter for queries over the supplied table, set to true. This argument applies only to partitioned tables, and if the `--time_partitioning_field` flag is set to true. The default value is false.
**`--schema`=SCHEMA**
    (Optional) Define the schema of the destination table. Specify the value as a comma-separated list of column definitions in the form [FIELD]:[DATA_TYPE]. Example: `name:STRING,age:INTEGER,city:STRING`
**`--schema_update_option`=OPTION**
    (Optional) When appending data to a table (in a load job or a query job), or when overwriting a table partition, specify how to update the schema of the destination table. Use one of the following values: 

  * `ALLOW_FIELD_ADDITION`: Allow new fields to be added
  * `ALLOW_FIELD_RELAXATION`: Allow relaxing `REQUIRED` fields to `NULLABLE`

Repeat this flag to specify multiple schema update options.
**`--skip_leading_rows`=NUMBER**
    (Optional) Specify the number of rows to skip at the beginning of the source file. The default value is 0.
**`--source_format`=FORMAT**
    (Optional) Specify the format of the source data. You can use one of the following values: `CSV`, `NEWLINE_DELIMITED_JSON`, `AVRO`, `DATASTORE_BACKUP` (use this value for Filestore), `PARQUET`, `ORC`. The default value is `ORC`.
**`--stats_table`=TABLE**
    (Optional) Specify the table to insert statistics into.
**`--time_partitioning_expiration`=SECONDS**
    (Optional) Specify when a time-based partition should be deleted, in seconds. The expiration time evaluates to the partition's UTC date plus the specified value. If you provide a negative number, the time-based partition never expires.
**`--time_partitioning_field`=FIELD**
    (Optional) Specify the field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, then the table is partitioned based on the load time.
**`--time_partitioning_type`=TYPE**
    (Optional) Enable time-based partitioning on a table and set the partition type using the following value: `DAY`.
**`--use_avro_logical_types`={true|false}**
    (Optional) If `--source_format` is set to `AVRO`, then set this flag to true to convert logical types into their corresponding types (such as `TIMESTAMP`) instead of only using their raw types (such as `INTEGER`). The default value is false.

### `bq mk`

Create a BigQuery resources such as built-in tables or external tables that need partitioning and and clustering to be set up. You can also use the `bq mk` command to generate a BigQuery table directly from parsing COBOL copybooks using the `--schema_from_copybook` flag.

#### Synopsis
    
    
    bq mk [options]
    

#### Flags and arguments

The `bq mk` command uses the following flags and arguments:

**`--project_id`=ID**
    Specify the project to use to execute this command.
**`--tablespec`=TABLE**
    Specify the destination table for the data. The supported format is [PROJECT]:[DATASET].[TABLE].
**`--clustering_fields`=FIELDS**
    (Optional) Specify a comma-separated list of up to four column names that specify the fields to use for table clustering.
**`--dataset_id`=ID**
    (Optional) Specify the default dataset to use with the command. You can set the value to [PROJECT_ID]:[DATASET] or [DATASET]. If [PROJECT_ID] is missing, the default project is used.
**`--description`=DESCRIPTION**
    (Optional) Provide a description for the dataset or table.
**`--dry_run`**
    (Optional) Print the table's Data Definition Language (DDL) statement.
**`--encoding`=ENCODING**
    (Optional) Specify the character set to use for encoding and decoding character fields. When specified, this value overrides the default set by the [`ENCODING`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#encoding) environment variable.
**`--expiration`=EXPIRATION**
    (Optional) Specify the lifetime for the table. If you don't specify a value, BigQuery creates the table with the dataset's default table lifetime, or the table doesn't expire.
**`--external_table_definition` or `-e`=TABLE**
    (Optional) Specify a name and schema definition to create an external table. Example: `ORC=gs://bucket/table_part1.orc/_,gs://bucket/table_part2.orc/_.`
**`--help` or `-h`**
    Display this help message.
**`--location`=LOCATION**
    (Optional) Specify a region or multi-region location to execute the command. The default value is US.
**`--parser_type`=TYPE**
    (Optional) Set the configuration parser to `legacy`, `copybook`, or `auto`. The default value is `auto`.
**`--require_partition_filter`={true|false}**
    (Optional) To have a partition filter for queries over the supplied table, set to true. This argument applies only to partitioned tables, and if the `--time_partitioning_field` flag is set to true. The default value is true.
**`--schema`=SCHEMA**
    (Optional) Specify either the path to a local JSON schema file or a comma-separated list of column definitions in the format FIELD:DATA_TYPE, FIELD:DATA_TYPE and so on.
**`--schema_from_copybook`=SCHEMA**
    (Optional) Generate the schema from a copybook.
**`--table` or `-t`=TABLE**
    (Optional) Create a table.
**`--time_partitioning_expiration`=SECONDS**
    (Optional) Specify when a time-based partition should be deleted, in seconds. The expiration time evaluates to the partition's UTC date plus the specified value. If you provide a negative number, the time-based partition never expires.
**`--time_partitioning_field`=FIELD**
    (Optional) Specify the field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, then the table is partitioned based on the load time.
**`--view`**
    (Optional) Create a view.

### `bq query`

Execute a BigQuery query.

#### Synopsis
    
    
    bq query [options]
    

#### Flags and arguments

You can run this command in the local and remote modes. For the remote mode, see the flags `--remoteHost`, `--remotePort`, and `--remoteUrl`, and the environment variable [`BQ_QUERY_REMOTE_EXECUTION`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bq_query_remote_execution). The `bq query` command uses the following flags and arguments:

**`--project_id`=ID**
    Specify the project to use to execute this command.
**`--allow_large_results`**
    (Optional) Use large destination table sizes for legacy SQL queries.
**`--append_table`**
    (Optional) Append the loaded data to the existing data in the destination table.
**`--batch`**
    (Optional) Run the query in batch mode.
**`--clustering_fields`=FIELDS**
    (Optional) Specify a comma-separated list of up to four column names that specify the fields to use for table clustering. If you specify this value with partitioning, then the table is first partitioned, and then each partition is clustered using the supplied columns.
**`--create_if_needed`**
    (Optional) Create destination table if it doesn't exist.
**`--dataset_id`=ID**
    (Optional) Specify the default dataset to use with the command. You can set the value to [PROJECT_ID]:[DATASET] or [DATASET]. If [PROJECT_ID] is missing, the default project is used.
**`--destination_table`=TABLE**
    (Optional) Specify the destination table that you want to write the query results to.
**`--dry_run`**
    (Optional) Validate the query without running it.
**`--follow`={true|false}**
    (Optional) To track individual query steps or the script as a whole, set to true. The default value is false. This option is not supported in remote mode.
**`--help` or `-h`**
    Display this help message.
**`--location`=LOCATION**
    (Optional) Specify a region or multi-region location to execute the command. The default value is US.
**`--maximum_bytes_billed`=BYTES**
    (Optional) Specify the limit of the bytes billed for the query.
**`--parameters`=PARAMETERS**
    (Optional) Specify comma-separated query parameters in the format [NAME]:[TYPE]:[VALUE]. An empty name creates a positional parameter. You can omit [TYPE] to assume a `STRING` value in the format name::value or ::value. `NULL` produces a null value.
**`--query_dsn`=DSN**
    (Optional) Specify the DSN to read the query from, in the format HLQ.MEMBER or HLQ.PDS(MEMBER). If `query_dsn` is not provided, [QUERY DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) is used.
**`--remoteHost`=HOST**
    (Optional) Specify the IP address of the remote host. To run the query in remote mode, set the [`BQ_QUERY_REMOTE_EXECUTION`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bq_query_remote_execution) environment variable.
**`--remotePort`=PORT**
    (Optional) Specify the remote port. The default value is 51770. To run the query in remote mode, set the [`BQ_QUERY_REMOTE_EXECUTION`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bq_query_remote_execution) environment variable.
**`--remoteUrl`=URL**
    (Optional) Specify the remote URL. To run the query in remote mode, set the [`BQ_QUERY_REMOTE_EXECUTION`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bq_query_remote_execution) environment variable.
**`--replace`**
    (Optional) Overwrite the destination table with the query results.
**`--report_row_limit`=LIMIT**
    (Optional) Specify the maximum rows to print in the audit report. The default value is 30. This option is not supported in remote mode.
**`--require_partition_filter`={true|false}**
    (Optional) To have a partition filter for queries over the supplied table, set to true. The default value is true.
**`--schema_update_option`=OPTION**
    (Optional) Update the schema of the destination table when appending data. Use the following values: 

  * `ALLOW_FIELD_ADDITION`: Allows new fields to be added.
  * `ALLOW_FIELD_RELAXATION`: Allows relaxing `REQUIRED` fields to `NULLABLE`.


**`--split_sql`={true|false}**
    (Optional) To split input SQL script into individual queries, set to true. The default value is true.
**`--stats_table`=TABLE**
    (Optional) Specify the table to insert statistics into. This option is not supported in remote mode.
**`--sync`={true|false}**
    (Optional) Run the command in synchronous mode.
**`--synchronous_mode`={true|false}**
    (Optional) An alternative to `--sync`.
**`--timeOutMinutes`=MINUTES**
    (Optional) Specify the timeout in minutes for a BigQuery job response. The default value is 240 minutes.
**`--time_partitioning_expiration`=SECONDS**
    (Optional) Specify when a time-based partition should be deleted, in seconds. The expiration time evaluates to the partition's UTC date plus the specified value. If you provide a negative number, the time-based partition never expires.
**`--time_partitioning_field`=FIELD**
    (Optional) Specify the field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, then the table is partitioned based on the load time.
**`--time_partitioning_type`=TYPE**
    (Optional) Enable time-based partitioning on a table and set the partition type using one of the following values: `DAY`, `HOUR`, `MONTH`, `YEAR`.
**`--use_cache`={true|false}**
    (Optional) To cache the query results, set to true. The default value is true.
**`--use_legacy_sql`**
    (Optional) Use legacy SQL instead of standard SQL.

### `cloud run job cancel`

Cancel a specific job execution.

#### Synopsis
    
    
    cloud run job cancel [-h] --project=PROJECT
                                --region=REGION EXECUTION
    

#### Flags and arguments

The `cloud run job cancel` command uses the following flags and arguments:

**EXECUTION**
    Specify the name of the Cloud Run job execution id.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--project`=PROJECT**
    Specify the project ID.
**`--region`=REGION**
    Specify the region in which the resource can be found.

### `cloud run job execute`

Execute a specific job.

#### Synopsis
    
    
    cloud run job execute [-h] [--async] [--tail-logs] [--wait]
                                 [--dump-execution-id=EXECUTION-ID]
                                 [--polling-interval=POLLINGINTERVAL]
                                 --project=PROJECT
                                 --region=REGION
                                 [--task-timeout=TIMEOUT]
                                 [--args=ARGS]...
                                 [--update-env-vars=ENVVARS]...
                                 JOB
    

#### Flags and arguments

The `cloud run job execute` command uses the following flags and arguments:

**JOB**
    Specify the name of the Cloud Run job to execute.
**`--args`=ARGS**
    (Optional) Comma-separated arguments passed to the command run by the container image. If provided, an execution will be created with the input values.
**`--async`**
    (Optional) Specify this flag if you want to return immediately, without waiting for the operation in progress to complete.
**`--dump-execution-id`=EXECUTION-ID : DataPath**
    (Optional) Specify the file to write the execution ID to.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--polling-interval`=POLLINGINTERVAL**
    (Optional) Sets the polling interval for displaying logs when `--tail_logs` is enabled. The default value is 60s.
**`--project`=PROJECT**
    Specify the project ID.
**`--region`=REGION**
    Specify the region in which the resource can be found.
**`--tail-logs`**
    (Optional) If you run the command in the synchronous mode by specifying the `--tail_logs` flag, Mainframe Connector displays the progress logs on the screen. If you specify both the `--tail_logs` and `--async` flags, an error message is displayed. As Cloud Logging does not support real-time logging, the command only displays logs that have already been recorded in the logs. As a result, some logs may be missing when you use the `--tail_logs` flag. To view the complete job logs, use the `cloud run job logs` command after the job has finished.
**`--task-timeout`=TIMEOUT**
    (Optional) Displays the existing maximum time (deadline) a job task attempt can run for. If not specified will use job default.
**`--update-env-vars`=ENVVARS**
    (Optional) List of key-value pairs to set as environment variables overrides for an execution of a job.
**`--wait`**
    (Optional) Specify this flag if you want the command to wait until the execution has completed running before exiting.

### `cloud run job logs`

Display cloud run logs

#### Synopsis
    
    
    cloud run job logs [-h] [--tail] [--log-filter=FILTER]
                              [--polling-interval=POLLINGINTERVAL]
                              --project=PROJECT
                              --region=REGION
                              [--timeout=TIMEOUT] EXECUTION-ID
    

#### Flags and arguments

The `cloud run job logs` command uses the following flags and arguments:

**EXECUTION-ID**
    The name of the Cloud Run job execution id.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--log-filter`=FILTER**
    (Optional) Filter expression that specifies the log entries to return.
**`--polling-interval`=POLLINGINTERVAL**
    (Optional) Sets the polling interval for displaying logs when `--tail_logs` is enabled. The default value is 60s.
**`--project`=PROJECT**
    Specify the project ID.
**`--region`=REGION**
    Specify the region in which the resource can be found.
**`--tail`**
    (Optional) Displays only new logs starting from now when set. If not set, all job logs will be shown.
**`--timeout`=TIMEOUT**
    (Optional) Timeout, after the command will exit. If not set the command will time out when the execution exits.

### `copy binary`

Copy a binary dataset from a source path to a destination path.

#### Synopsis
    
    
    copy binary [-h] [--buffer-size=BUFFERSIZE] INPUT
                       OUTPUT
    

#### Flags and arguments

The `copy binary` command uses the following flags and arguments:

**INPUT : DataPath**
    Specify the data path of the input file you want to copy.
**OUTPUT : DataPath**
    Specify data path of the output file you want to copy to.
**`--buffer-size`=BUFFERSIZE : DataSize**
    (Optional) Indicate the memory read size for each chunk of data. The default value is 64 MiB.
**`--help` or `-h`**
    (Optional) Display this help message.

### `copy text`

Copy text dataset.

#### Synopsis
    
    
    copy text [-h] [--trim-suffix] [--buffer-size=BUFFERSIZE]
                     INPUT OUTPUT
    

#### Flags and arguments

Copies a dataset or file and outputs it as a newline-delimited text file. Unlike [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary), `copy text` strips Record Descriptor Words (RDWs), formats records into newline-delimited lines, and transcodes data using the encodings configured on the input and output [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) URIs.

**Note:** To preserve exact byte-for-byte binary structure and RDWs without character conversion, use [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary) instead.

The `copy text` command uses the following flags and arguments:

**INPUT : DataPath**
    Specify the data path of the input file you want to copy.
**OUTPUT : DataPath**
    Specify data path of the output file you want to copy and encode to.
**`--buffer-size`=BUFFERSIZE : DataSize**
    (Optional) Indicate the memory read size for each chunk of data. The default value is 64 MiB.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--trim-suffix`**
    (Optional) When set to true, any whitespace at the end of the record will be trimmed. Note that records that consist only of whitespaces will become empty records.

### `gsutil cp`

**Deprecated.** Use `qsam decode` instead. 

Transcode data from your Mainframe to a Cloud Storage bucket.

#### Synopsis
    
    
    gsutil cp [options] gcsUri [dest]
    

#### Flags and arguments

You can use this command for the following different purposes: 

  * Copy and transcode a file from a Mainframe or a Linux environment to Cloud Storage.
    * Source: `--inDSN`. If not provided, is specified by [DD INFILE](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
    * Destination: `gcsUri`
  * Copy and transcode a file within Cloud Storage
    * Source: `gcsUri`
    * Destination: `--destPath`
  * Copy a file from Cloud Storage to a Mainframe.
    * Source: `gcsUri`
    * Destination: `--destDSN`
    * Relevant flags: `--lrecl`, `--blksize`, `--recfm`, `--noseek`.
  * Copy a file from Cloud Storage to a Linux environment.
    * Source: `gcsUri`
    * Destination: `--destPath`

This command can run in local, remote, and standalone modes. For remote mode, see the flags `--remote`, `--remoteHost`, `--remotePort`, and `--remoteUrl`. The `gsutil cp` command uses the following flags and arguments: 

**dest**
    (Optional) The local path or data source name (DSN). Example formats: `/path/to/file`, DATASET.MEMBER
**gcsUri**
    The Cloud Storage URI in the format `gs://bucket/path`. Can represent both the source and destination location, depending on usage.
**`--batchSize`=SIZE**
    (Optional) Specify the blocks to be used per batch. The default value is 1000.
**`--blksize`=SIZE**
    (Optional) Specify the block size of file to copy to the Mainframe. If `blksize=0` and the `recfm` is not U, the mainframe system determines the optimal block size for the file.
**`--cobDsn`=DSN**
    (Optional) Specify the copybook DSN that you want to use. If you don't provide a value, Mainframe Connector reads from [DD COPYBOOK](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--connections`=NUMBER**
    (Optional) Specify the number of connections that can made to the remote receiver. The default value is 10.
**`--dataset_id`=ID**
    (Optional) Specify the default dataset to use with the command. You can set the value to [PROJECT_ID]:[DATASET] or [DATASET]. If [PROJECT_ID] is missing, the default project is used.
**`--destDSN`=OUTPUT**
    (Optional) Specify the destination DSN.
**`--destPath`=OUTPUT**
    (Optional) Specify the destination path.
**`--dry_run`**
    (Optional) Test copybook parsing and decoding of the QSAM file.
**`--encoding`=ENCODING**
    (Optional) Specify the character set to use for encoding and decoding character fields. When specified, this value overrides the default set by the [`ENCODING`](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#encoding) environment variable.
**`--help` or `-h`**
    Display this help message.
**`--inDsn`=DSN**
    (Optional) Specify the infile DSN that you want to use. If you don't provide a value, Mainframe Connector reads from [DD INFILE](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--keepAliveTimeInSeconds`=SECONDS**
    (Optional) Specify the keep alive timeout in seconds for an HTTP channel. The default value 480 seconds.
**`--location`=LOCATION**
    (Optional) Specify a region or multi-region location to execute the command. The default value is US.
**`--lowerCaseColumnNames`**
    (Optional) Create lowercase column names for copybook fields.
**`--lrecl`=LRECL**
    (Optional) Specify the logical record length (lrecl) of the file that you want to copy to the Mainframe.
**`--maxChunkSize`=SIZE**
    (Optional) Specify the maximum chunk size per batch. You should use K, KiB, KB, M, MiB, MB, G, GiB, GB, T, TiB, or TB to describe the size. The default value is 128MiB.
**`--max_error_pct`=PCT**
    (Optional) Specify the job failure threshold for row decoding errors. Valid values are within the range [0.0, 1.0]. The default value is 0.
**`--noseek`**
    (Optional) Improve download performance from Cloud Storage to the Mainframe.
**`--parallel` or `-m`**
    (Optional) Set the number of concurrent writers to 4.
**`--parallelism` or `-p`=NUMBER**
    (Optional) Specify the number of concurrent writers. The default value is 4.
**`--parser_type`=TYPE**
    (Optional) Set the configuration parser to `legacy`, `copybook`, or `auto`. The default value is `auto`.
**`--preload_chunk_count`=NUMBER**
    (Optional) Specify the number of chunks to preload from disks while all workers are occupied. The default value is 2.
**`--project_id`=ID**
    (Optional) Specify the project to use to execute this command.
**`--recfm`=REFCM**
    (Optional) Specify the recfm of the file that you want to copy to the Mainframe. You can use one of the following values: F, FB, V, VB, U. The default value is FB.
**`--remote`**
    (Optional) Use a remote decoder.
**`--remoteHost`=HOST**
    (Optional) Specify the IP address of the remote host. To run Mainframe Connector in remote mode, set the `--remote` flag.
**`--remotePort`=PORT**
    (Optional) Specify the remote port to be used. The default value is 51770. To run Mainframe Connector in remote mode, set the `--remote` flag.
**`--remoteUrl`=URL**
    (Optional) Specify the remote URL. To run Mainframe Connector in remote mode, set the `--remote` flag.
**`--replace`**
    (Optional) Delete the destination recursively before uploading.
**`--stats_table`=TABLE**
    (Optional) Specify the table to insert statistics into.
**`--tfDSN`=DSN**
    (Optional) Specify the transformations from a DSN, DATASET.MEMBER, or PDS(MBR).
**`--tfGCS`=GCS**
    (Optional) Specify the transformations file from Cloud Storage.
**`--timeOutMinutes`=MINUTES**
    (Optional) Specify the timeout in minutes for a remote gRPC call. The default value is 90 minutes for Cloud Storage and 50 minutes for a Mainframe.

### `pubsub topics publish`

Publish a message to a Pub/Sub topic.

This command lets you send message data either directly using the `--data` flag or through a file using the `--data-path` flag. You can also include attributes, an ordering key, and apply message properties. Additionally, you can apply dynamic string substitutions to the message content.

#### Synopsis
    
    
    pubsub topics publish [-h] [--data=DATA]
                                 [--data-path=DATAPATH]
                                 [--ordering-key=ORDERING-KEY]
                                 [--attributes=NAME=VALUE[,
                                 NAME=VALUE...]]...
                                 [--message-property=KEY=VALUE]...
                                 [--substitution=KEY=VALUE]...
                                 TOPIC
    

#### Flags and arguments

The `pubsub topics publish` command uses the following flags and arguments:

**TOPIC**
    Specify the name of the topic in the format `projects/{project}/topics/{topic}`.
**`--attributes`=NAME=VALUE**
    (Optional) Specify a comma-separated list of attributes. Each ATTRIBUTE has the form `name=value`. You can specify up to 100 attributes. For a full list of attribute guidelines, see [Use attributes to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes).
**`--data-path`=DATAPATH : DataPath**
    (Optional) Specify the path to the file containing the data of the message. You must set one of the flags `--data` or `--data-path`, but not both. For more information on message formatting and size limits, see [Publish messages to topics](https://docs.cloud.google.com/pubsub/docs/publisher#publish).
**`--data`=DATA**
    (Optional) Specify the body of the message that you want to publish to the given topic name. You must set one of the flags `--data` or `--data-path`, but not both. For more information on message formatting and size limits, see [Publish messages to topics](https://docs.cloud.google.com/pubsub/docs/publisher#publish).
**`--help` or `-h`**
    (Optional) Display this help message.
**`--message-property`=KEY=VALUE**
    (Optional) Specify properties to apply to the message. A valid property key is `encoding`. This property key specifies the character encoding to use for the message string. The message string is converted into bytes using this encoding before being sent to the Pub/Sub topic. For a list of supported encoding values, see [supported encodings](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html). The default is `UTF-8`.
**`--ordering-key`=ORDERING-KEY**
    (Optional) Specify the key for the ordered delivery of messages to subscribers. All messages with the same ordering key are sent to subscribers in the order that Pub/Sub receives them.
**`--substitution`=KEY=VALUE**
    

(Optional) Using either `--data` or `--data-path`, specify the key-value pairs to be used for the dynamic substitution to be applied on the Pub/Sub message data. Mainframe Connector scans the message data for placeholders and replaces them with their corresponding values. Define the placeholders in the data using the syntax ${KEY}, for example ${NAME}. Specify each substitution as a key-value pair using the format `KEY=VALUE`. You can specify multiple substitutions by repeating the option: `--substitution key1=value1 --substitution key2=value2`.

    

For example, if the input data is: `Hello, ${username}!` and you use `--substitution username=World`, then the message sent to Pub/Sub will be: `Hello, World!`.

    **Note:** Substitutions are performed as raw string replacements. If your message string is intended to be a JSON payload, special JSON characters (double quotes, backslashes, or newlines) in your substitution values aren't automatically escaped. You must ensure that your substitution values are properly JSON-escaped if you intend for the final message to remain valid JSON.

### `qsam decode`

Decode QSAM data.

This command decodes records from a QSAM file to the format you specify using the `--output-format` argument. The original QSAM file is split into chunks based on the value you specify with the `--max-chunk-size` argument. The transcoded output is saved in the target path as lexicographically sorted files.

#### Synopsis
    
    
    qsam decode [-h] [--replace] [--chunk-size=CHUNK-SIZE]
                       --copybook=COPYBOOK
                       [--max-error-percent=MAX_ERROR_PERCENT]
                       [--output-format=FORMAT]
                       [--parallelism=COUNT]
                       [--preload-chunk-count=PRELOAD_CHUNK_COUNT]
                       [--transcode-configuration=CONFIG]
                       [--input-parameter=KEY=VALUE]... INPUT
                       OUTPUT
    

#### Flags and arguments

The `qsam decode` command uses the following flags and arguments:

**INPUT : DataPath**
    Specify the data path of the QSAM file you want to decode.
**OUTPUT : DataPath**
    Specify the data path of the output prefix. All output is stored under this prefix.
**`--chunk-size`=CHUNK-SIZE : DataSize**
    (Optional) Specify the amount of input data to include in each output file. The output file may be larger or smaller. Chunk size is rounded down to the closest multiple of the logical record length. The default value is 128MiB.
**`--copybook`=COPYBOOK : DataPath**
    Specify the data path of the file containing the copybook.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input-parameter`=KEY=VALUE**
    

(Optional) Specify parameters to configure the input. Each parameter is defined as `KEY=VALUE`. The supported input parameter keys are as follows:

    

  * `csv-dialect`: Configures CSV parsing. The value is a `DataPath` pointing to a [CSV configuration file](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration#com.google.cloud.imf.transcoder.compiler.CsvConfiguration).
  * `json-dialect`: Configures JSON parsing. The value is a `DataPath` pointing to [JSON configuration file](https://docs.cloud.google.com/mainframe-connector/docs/json-configuration#com.google.cloud.imf.transcoder.compiler.JsonConfiguration).
  * `pubsub-publish-configuration`: Configures the messages that get sent to Pub/Sub. The value is a `DataPath` pointing to a [Pub/Sub configuration file](https://docs.cloud.google.com/mainframe-connector/docs/pubsub-publish-configuration#com.google.cloud.imf.transcoder.compiler.PubsubPublishConfiguration).
  * `output-prefix`: Add prefix to the output files.


**`--max-error-percent`=MAX_ERROR_PERCENT**
    

(Optional) Specify the percentage of the processed records that are allowed to have errors before the transcoding process fails. The value can range between 0.0 (fail if there are any transcoding errors) and 1.0 (do not fail if there are transcoding errors). The default value is 0.

**`--output-format`=FORMAT : TranscodeFormat**
    

(Optional) Specify the format of the output file. If you provide a `DataPath` of a Pub/Sub topic as the value to `OUTPUT`, then the default output format is `JSONL`. For all other `DataPaths`, the default output format is `ORC`.

**`--parallelism`=COUNT**
    

(Optional) Specify the number of processing threads. The value should be equal or less than the number of cores available. The default value is 1.

**`--preload-chunk-count`=PRELOAD_CHUNK_COUNT**
    

(Optional) Specify the number of data chunks to preload when all threads are processing. The default value is 1.

**`--replace`**
    

(Optional) If specified, deletes the output path recursively before writing the decoding results.

**`--transcode-configuration`=CONFIG : DataPath**
    

(Optional) Specify the file containing the transcoding configuration. For more information on the transcoder configuration format, see [Transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

### `qsam encode`

Encode QSAM data.

This command takes data from an external source and converts it to a QSAM file. The input is defined by the value you specify using the `--input-format` argument.

#### Synopsis
    
    
    qsam encode [-h] --copybook=COPYBOOK
                       --input-format=FORMAT
                       [--input-stream-count=COUNT]
                       [--max-error-percent=MAX_ERROR_PERCENT]
                       [--parallelism=COUNT]
                       [--spillover=SPILLOVER]
                       [--transcode-configuration=CONFIG]
                       [--input-parameter=KEY=VALUE]... INPUT
                       OUTPUT
    

#### Flags and arguments

The `qsam encode` command uses the following flags and arguments:

**INPUT : DataPath**
    Specify the data path of the input file you want to encode into a QSAM file.
**OUTPUT : DataPath**
    Specify data path of the QSAM file you want to encode to.
**`--copybook`=COPYBOOK : DataPath**
    Specify the data path of the file containing the copybook.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input-format`=FORMAT : TranscodeInputFormat**
    Specify the format of the input.
**`--input-parameter`=KEY=VALUE**
    

(Optional) Specify parameters to configure the input. Each parameter is defined as `KEY=VALUE`. The supported input parameter keys are as follows:

    

  * `csv-dialect`: Configures CSV parsing. The value is a `DataPath` pointing to a [CSV configuration file](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration#com.google.cloud.imf.transcoder.compiler.CsvConfiguration).
  * `json-dialect`: Configures JSON parsing. The value is a `DataPath` pointing to [JSON configuration file](https://docs.cloud.google.com/mainframe-connector/docs/json-configuration#com.google.cloud.imf.transcoder.compiler.JsonConfiguration).
  * `project-id`: Cloud Storage project ID in case of ORC.


**`--input-stream-count`=COUNT**
    

(Optional) Specify the number of input streams. This is a maximum value, in reality fewer streams may be used. The default value is 1.

**`--max-error-percent`=MAX_ERROR_PERCENT**
    

(Optional) Specify the percentage of the processed records that are allowed to have errors before the transcoding process fails. The value can range between 0.0 (fail if there are any transcoding errors) and 1.0 (do not fail if there are transcoding errors). The default value is 0.

**`--parallelism`=COUNT**
    

(Optional) Specify the number of processing threads. The value should be equal to or less than the number of available cores. The default value is 1.

**`--spillover`=SPILLOVER : DataPath**
    

(Optional) Specify a data path for the spillover dataset. If you don't specify this information, error details will be discarded.

**`--transcode-configuration`=CONFIG : DataPath**
    

(Optional) Specify the file containing the transcoding configuration. For more information on the transcoder configuration format, see [Transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

### `remove`

Remove Cloud Storage objects.

#### Synopsis
    
    
    remove [-hR] URL...
    

#### Flags and arguments

The `remove` command uses the following flags and arguments:

**URL**
    Specify the Cloud Storage location in the format `gs://bucket/prefix`.
**`--help` or `-h`**
    (Optional) Display this help message.
**`-R` or `-r`**
    (Optional) Recursively delete the contents of directories or objects that match the path expression. Does not throw an error if the directory or object does not exist.

### `scp`

**Deprecated.** Use `copy text` or `copy binary` instead. 

Copy files to Cloud Storage.

#### Synopsis
    
    
    scp [options] [input] [output]
    

#### Flags and arguments

To use this command, you must ensure the following: 

  * Set one unique input value through `input`, `--inDD`, or `--inDsn`.
  * Set one unique output value through output or `--gcsOutUri`.



The `scp` command uses the following flags and arguments:

**input**
    (Optional) Specify the DD or DSN to be copied. You can use `--inDD` or `--inDsn` instead.
**output**
    (Optional) Specify the URI of the output using the format gs://[BUCKET]/[PREFIX]. You can use `--gcsOutUri` instead.
**`--compress`**
    (Optional) Compress output with gzip.
**`--count` or `-n`=RECORDS**
    (Optional) Specify the number of records to copy. The default is unlimited.
**`--encoding`=ENCODING**
    (Optional) Specify the input character encoding. The default value is CP037.
**`--gcsOutUri`=URI**
    (Optional) Specify the destination Cloud Storage URI of the file copy.
**`--help` or `-h`**
    Display this help message.
**`--inDD`=INPUT**
    (Optional) Specify the DD file to be copied. The default value is [DD INFILE](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
**`--inDsn`=INPUT**
    (Optional) Specify the DSN to be copied.
**`--noConvert`**
    (Optional) Disable conversion of character input to ASCII. Character conversion is enabled by default.

### `systemreport`

Provide system report.

#### Synopsis
    
    
    systemreport [-h] [--available-security-providers] [--supported-ciphers]
    

#### Flags and arguments

The `systemreport` command uses the following flags and arguments:

**`--available-security-providers`**
    (Optional) Print supported security providers.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--supported-ciphers`**
    (Optional) Print supported ciphers.

### `vsam decode`

Decode VSAM data.

This command decodes records from a VSAM file to the format you specify using the `--output-format` argument. The original VSAM file is split into chunks based on the value you specify with the `--max-chunk-size` argument. The transcoded output is saved in the target path as lexicographically sorted files.

#### Synopsis
    
    
    vsam decode [-h] [--replace] [--chunk-size=CHUNK-SIZE]
                       --copybook=COPYBOOK
                       [--max-error-percent=MAX_ERROR_PERCENT]
                       [--output-format=FORMAT]
                       [--parallelism=COUNT]
                       [--preload-chunk-count=PRELOAD_CHUNK_COUNT]
                       [--transcode-configuration=CONFIG]
                       [--input-parameter=KEY=VALUE]... INPUT
                       OUTPUT
    

#### Flags and arguments

The `vsam decode` command uses the following flags and arguments:

**INPUT : DataPath**
    Specify the data path of the VSAM file you want to decode.
**OUTPUT : DataPath**
    Specify the data path of the output prefix. All output is stored under this prefix.
**`--chunk-size`=CHUNK-SIZE : DataSize**
    (Optional) Specify the amount of input data to include in each output file. The output file may be larger or smaller. Chunk size is rounded down to the closest multiple of the logical record length. The default value is 128MiB.
**`--copybook`=COPYBOOK : DataPath**
    Specify the data path of the file containing the copybook.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input-parameter`=KEY=VALUE**
    

(Optional) Specify parameters to configure the input. Each parameter is defined as `KEY=VALUE`. The supported input parameter keys are as follows:

    

  * `csv-dialect`: Configures CSV parsing. The value is a `DataPath` pointing to a [CSV configuration file](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration#com.google.cloud.imf.transcoder.compiler.CsvConfiguration).
  * `json-dialect`: Configures JSON parsing. The value is a `DataPath` pointing to [JSON configuration file](https://docs.cloud.google.com/mainframe-connector/docs/json-configuration#com.google.cloud.imf.transcoder.compiler.JsonConfiguration).
  * `pubsub-publish-configuration`: Configures the messages that get sent to Pub/Sub. The value is a `DataPath` pointing to a [Pub/Sub configuration file](https://docs.cloud.google.com/mainframe-connector/docs/pubsub-publish-configuration#com.google.cloud.imf.transcoder.compiler.PubsubPublishConfiguration).
  * `output-prefix`: Add prefix to the output files.


**`--max-error-percent`=MAX_ERROR_PERCENT**
    

(Optional) Specify the percentage of the processed records that are allowed to have errors before the transcoding process fails. The value can range between 0.0 (fail if there are any transcoding errors) and 1.0 (do not fail if there are transcoding errors). The default value is 0.

**`--output-format`=FORMAT : TranscodeFormat**
    

(Optional) Specify the format of the output file. If you provide a `DataPath` of a Pub/Sub topic as the value to `OUTPUT`, then the default output format is `JSONL`. For all other `DataPaths`, the default output format is `ORC`.

**`--parallelism`=COUNT**
    

(Optional) Specify the number of processing threads. The value should be equal or less than the number of cores available. The default value is 1.

**`--preload-chunk-count`=PRELOAD_CHUNK_COUNT**
    

(Optional) Specify the number of data chunks to preload when all threads are processing. The default value is 1.

**`--replace`**
    

(Optional) If specified, deletes the output path recursively before writing the decoding results.

**`--transcode-configuration`=CONFIG : DataPath**
    

(Optional) Specify the file containing the transcoding configuration. For more information on the transcoder configuration format, see [Transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

## Parameter Types

These common types are used in Mainframe Connector commands. 

### `DataPath`

`DataPath` is a string representing an input or an output. Each `DataPath` type has its own prefix and arguments as follows:

  * **`DD:`** \- Data paths with this prefix point to a data definition statement (DD) when running in a Job Control Language (JCL) job. You can change the DD encoding by adding `encoding=encoding` to the DD. For example, `DD:DDNAME` or `DD:DDNAME?encoding=UTF-8`. The default DD encoding is the default OS encoding.

  * **`DSN:`** \- Data paths with this prefix point to a data source name (DSN) when running on a mainframe. You can change the DSN encoding by adding `encoding=charset` to the DSN. You can change the DSN write mode by adding `writemode=OLD/MOD/SHR` to the DSN.

    * **`MOD:`** Appends data to the end of an existing file. If the file doesn't exist, it's created. This mode allows concurrent read access (DISP=SHR logic) by default.
    * **`OLD:`** Overwrites the file starting from the beginning. This mode grants exclusive control; no other job can access the DSN while it is open.
    * **`SHR:`** Overwrites the file starting from the beginning. This mode allows concurrent read and write access, but should be used with extreme caution as it offers no serialization.

For example, `DSN:HQ.FOO.BAR`, `DSN:HQ.FOO.BAR?encoding=cp037` or `DSN:HQ.FOO.BAR?encoding=cp037&writemode=OLD`.

  * **`file:`** \- Data paths with this prefix point to a Unix file. You can specify the following in the Unix file:

    * The logical record length (LRECL) by adding `?lrecl=lrecl` before the `:`.
    * The record format (RECFM) by adding `?recfm=recfm` before the `:`. The default RECFM is `F`.
    * The encoding by adding `?encoding=charset` before the `:`. The default encoding is `UTF-8`.

For example, `file:/path/to/file`, `file?lrecl=80:/path/to/file`, `file?lrecl=80&recfm=FB:/path/to/file`, or `file?lrecl=80&recfm=FB&encoding=cp037:/path/to/file`.

  * **`gs://`** \- Data paths with this prefix point to a file in Cloud Storage. You can specify the following in the file:

    * The LRECL by adding `?lrecl=lrecl` after the bucket prefix.
    * The RECFM by adding `?recfm=recfm` after the bucket prefix. The default RECFM is `F`.
    * The encoding by adding `?encoding=charset` after the bucket prefix. The default encoding is `UTF-8`.
    * The checksum algorithms to verify by adding `?checksums=algorithms` after the bucket prefix. Supported values: `md5`, `crc32c`, `none`, `all`. The default is `all`.
    * The content encoding by adding `?content-encoding=charset` after the bucket prefix. Supported values: `gzip`, `identity`. The default is `identity`. Note: this applies exclusively for Cloud Storage writes; reads dynamically infer content encoding from the upstream storage blob metadata.

    * Parallelism can be set by adding `?parallelism=num` after the bucket prefix. When set, some operations will use multiple GCS streams when transferring data to and from GCS.

For example, `gs://my_bucket/my/file.txt`,`gs://my_bucket/my/file.txt?encoding=cp037`,`gs://my_bucket/my/file.txt?recfm=fb&encoding=cp037`, or `gs://my_bucket/my/file.txt?lrecl=80&recfm=fb&encoding=cp037`.

  * **`pubsub:`** \- Data paths with this prefix point to a Pub/Sub resource. For example, `pubsub:projects/projectId/topics/topicId`.




Mainframe Connector frames each record in variable-length Cloud Storage or Unix files using a 4-byte Record Descriptor Word (RDW). This applies when reading or writing records with commands such as [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary), [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode), or [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode).

  * **`RECFM=V`** (LLzz format):

    * The first two bytes represent the data size + 4 bytes.
    * The subsequent two bytes are always `0x0000`.
    * The remaining bytes constitute the actual record data.
  * **`RECFM=VC`** (zzLL format):

    * The first two bytes are always `0x0000`.
    * The subsequent two bytes represent the data size.
    * The remaining bytes constitute the actual record data.



### `DataSize`

`DataSize` represents a size in the form of an amount and a unit of measurement, for example 5 MiB. You can use whitespace between the amount and magnitude. Data size parsing is case-insensitive, so you can specify units of measurement in both upper and lower cases.

**Note:** You can't specify partial amounts. For example, use 716 KiB instead of 0.7 MiB.

You can specify the value in the following formats:

  * **Java format:** b/k/m/g/t, for byte, kibibyte, mebibyte, gibibyte, and tebibyte respectively.
  * **International format:** KiB/MiB/GiB/TiB, for kibibyte, mebibyte, gibibyte, and tebibyte respectively.
  * **Metric format:** b/kb/mb/gb/tb, for kilobyte, megabyte, gigabyte, and terabyte respectively. 



### `TranscodeFormat`

`TranscodeFormat` represents the format to be used during the transcoding process.

Valid values are:

  * **_`ORC`_** \- `ORC` is a self-describing type-aware columnar file format.
  * **_`CSV`_** \- `CSV` is a plain text format that stores tabular data with each line representing a row. You can specify the CSV parameters using the `csv-dialect` input parameter. You can define it as `--input-parameter csv-dialect=`DataPath where DataPath points to the location of these parameters.
  * **_`JSONL`_** \- `JSONL` is a plain text format that stores tabular data with each line representing a row. You can specify the JSON parameters using the `json-dialect` input parameter. You can define it as `--input-parameter json-dialect=`DataPath where DataPath points to the location of these parameters.
  * **_`AVRO`_** \- `AVRO` is a self describing type-aware row oriented binary serialization format. 



### `TranscodeInputFormat`

The format to be used during transcode.

Valid values are:

  * **_`BIGQUERY`_** \- Pulls data directly from BigQuery. `INPUT` must be a path to a query file.

Available input parameters are:

    * `keep-order` \- Use if the exact order of records is important. Note that this will limit the input stream.
    * `project-id` \- Project ID to use when executing the job.
    * `location` \- Location to use when executing the job.
  * **_`CSV`_** \- `CSV` is a plain text format that stores tabular data with each line representing a row. You can specify the CSV parameters using the `csv-dialect` input parameter. You can define it as `--input-parameter csv-dialect=`DataPath where DataPath points to the location of these parameters.

  * **_`JSONL`_** \- `JSONL` is a plain text format that stores tabular data with each line representing a row. You can specify the JSON parameters using the `json-dialect` input parameter. You can define it as `--input-parameter json-dialect=`DataPath where DataPath points to the location of these parameters.

  * **_`ORC`_** \- `ORC` is a self-describing type-aware columnar file format. To transcode `ORC` files from Cloud Storage, set the value of `project-id` to the project ID in which the Cloud Storage is present.

  * **_`AVRO`_** \- `AVRO` is a self describing type-aware row oriented binary serialization format. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
