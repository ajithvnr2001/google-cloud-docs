---
url: https://docs.cloud.google.com/mainframe-connector/docs/release-notes/
title: Mainframe Connector release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:01.107989+00:00
---

# Mainframe Connector release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Resources ](https://docs.cloud.google.com/mainframe-connector/docs/release-notes)



Send feedback 

#  Mainframe Connector release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Mainframe Connector. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/mainframeconnector-release-notes.xml) directly. 

## October 08, 2026

v5.21.0

Feature

Mainframe Connector 5.21.0 supports the following new feature:

  * Improved transcoding to optimize throughput.



v5.21.0

Fixed

The following issues are fixed in Mainframe Connector 5.21.0:

  * Fixed an issue where the [`bq query` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_query) command terminated even if query execution succeeded.
  * Fixed nullability of Avro fields.



## August 13, 2026

v5.20.2

Fixed

The following issues are fixed in Mainframe Connector 5.20.2:

  * Fixed an issue where the [`bq query` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#bq_query) wrote excessive log messages to standard output, potentially exceeding mainframe spool line limits and triggering an S722 system abend.
  * Fixed an issue where the [`gsutil cp` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#gsutil_cp) failed to decode date and timestamp fields containing null characters.



## July 30, 2026

v5.20.1

Feature

Mainframe Connector 5.20.1 supports the following new features:

  * Supports AI integration with Antigravity using a specialized `SKILL` file and dedicated agent CLI endpoints. This feature lets you perform AI-assisted data modernization and Mainframe Connector configuration.

For more information, see [Use Google Antigravity to transcode and migrate data](https://docs.cloud.google.com/mainframe-connector/docs/agentic-tools-to-transcode-and-migrate-data).

  * The [transcoding configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) has the following new capabilities:

    * Supports applying [`unnest`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#unnest) or [`rename`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#rename) to specific tables created by [`split`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#split).
    * The field modifier [`formatDate`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#formatdate) supports numeric fields.
    * The field modifier [`packedDecimal`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#packeddecimal) supports a configurable negative-sign nibble.
    * The [`record_filter_condition`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#configuration) parameter has been optimized to support date constants and nested fields.
  * Adds a `ByteOffset` field to the `qsam decode` [spillover schema](https://docs.cloud.google.com/mainframe-connector/docs/spillover-dataset), reporting the absolute byte position of each failing record.

  * Supports enhanced performance for [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary) and [`copy text`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_text) via parallel multipart uploads, compression, and [hashing options](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath).

  * Supports trimming white-space in the [`copy text`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_text) command.

  * Supports enabling performance counters that record data upload metrics, to help diagnose throughput bottlenecks.

  * Supports mainframes using Java 21 (later than version 21.0.10.1), in addition to Java 17 and Java 8.

  * Supports QSAM to AVRO encoding, and the other way around. 

  * Adds the `bqsh.dataset.encoding` property to specify the default character encoding used for mainframe dataset operations (DSN and DD). If unset on z/OS, Mainframe Connector attempts to dynamically detect the native encoding using the `native.encoding` or `sun.jnu.encoding` system properties, falling back to `IBM-1047`. On non-mainframe environments, it falls back to the JVM default charset.




v5.20.1

Change

Remote mode and standalone mode now use Java 21 instead of Java 17.

v5.20.1

Fixed

The following issues are fixed in Mainframe Connector 5.20.1:

  * Fixed an issue that could print inaccurate locations for the syntax errors in the original copybook source.
  * Fixed issue that produced an incorrect record descriptor word (RDW) when writing variable-length record files.
  * Fixed data path string formatting to match the documented syntax.
  * Fixed handling [`nullif`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#nullif) and [`move`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#move) field modifiers for nested fields.
  * Fixed issue with the [`DecodeAsNull`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#decodeasnull) field modifier where a matched null value could cause the remaining fields in the record to be decoded incorrectly.



## December 04, 2025

v5.19.0

Feature

Mainframe Connector 5.19.0 supports the following new features:

  * Supports a new [`split` transformation](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#split) for the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) command. This transformation enables splitting datasets into multiple tables.
  * Supports configuring a `writemode=OLD/MOD/SHR` for DSN [`DataPaths`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath).



Fixed

The following issues are fixed in Mainframe Connector 5.19.0:

  * Optimized the [`copy binary`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary) and [`copy text`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_text) commands.
  * Fixed issue with opening DSN files and added support for new write modes in the [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath). 



## September 09, 2025

v5.18.0

Feature

Mainframe Connector 5.18.0 supports the following new features:

  * The [`qsam encode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) supports the [ORC input format](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeinputformat).
  * The [`qsam decode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) supports [new filtering capabilities](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#configuration) within the transcoder configuration.
  * Supports a new [`copy binary` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_binary) that copies a binary file from the mainframe to Google Cloud and the other way around.
  * Supports a new [`vsam decode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#vsam_decode) that decodes Virtual Storage Access Method (VSAM) files.
  * Supports [new schema validation modes](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#schemavalidationmode) for PostgreSQL and MySQL within the transcoder configuration.
  * Supports variable length records ([`recfm=V`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)) according to the standard LLZZ format by default.
  * Supports referencing nested fields within the [transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).



v5.18.0

Fixed

The following issue is fixed in Mainframe Connector 5.18.0:

Fixed issue with applying the [rename transformation](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#rename) to both inner and outer nested fields.

## July 03, 2025

v5.17.1

Fixed

The following issues are fixed with the [`qsam` commands](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-decode) in Mainframe Connector 5.17.1:

  * Fixed issues with reading QSAM V records that have a record descriptor word (RDW) greater than 32767.
  * Fixed issue with inline dynamic occurs.



v5.17.1

Feature

Mainframe Connector 5.17.1 supports the following new feature:

  * Supports a configurable prefix for output files and spillover files with the [`qsam decode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode).



## June 19, 2025

v5.17.0

Fixed

The following issues are fixed in Mainframe Connector 5.17.0:

  * Fixed issues with [`String`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#com.google.cloud.imf.transcoder.compiler.fieldmodifiers.String) and [`VarLen`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#com.google.cloud.imf.transcoder.compiler.fieldmodifiers.VarLen) field modifiers.
  * Fixed issues with nested redefines used with the [exclude transformation](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#exclude).
  * Better error handling and error messages in the new transcoding framework.



v5.17.0

Issue

Mainframe Connector 5.17.0 has the following known limitation:

  * Mainframe Connector returns an error when you configure the `null_representation` field in the [CSV configuration](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration) with the [`qsam encode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode).



v5.17.0

Feature

Mainframe Connector 5.17.0 supports the following new features:

  * Supports [QSAM to CSV transcoding](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration) and the other way around.
  * Supports [QSAM to JSON transcoding](https://docs.cloud.google.com/mainframe-connector/docs/json-configuration) and the other way around.
  * The transcoding commands [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) and [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) are now generally available with the following new capabilities: 
    * Support variable [`recfm=V`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath) QSAM files.
    * Support new field modifiers for better null handling - [`DecodeAsNull`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#decodeasnull) and [`EncodeNullAs`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#encodenullas).
    * Support multiple values in the [`NullIf`](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration#nullif) field modifier.
  * Supports [sending messages to a Pub/Sub topic](https://docs.cloud.google.com/mainframe-connector/docs/pub-sub) using the [`qsam decode` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) or using the new [`pubsub topics publish` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#pubsub_topics_publish).
  * Supports a new [`copy text` command](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#copy_text) to copy a file from mainframe to cloud and the other way around.
  * Supports mainframes using Java 17, in addition to Java 8.



## April 03, 2025

v5.16.0

Feature

Mainframe Connector 5.16.0 supports the following new features:

  * Supports a new transcoding framework ([preview](https://cloud.google.com/products/#product-launch-stages)) by introducing two new commands [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-decode) and [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#qsam-encode). The `qsam decode` command is similar in functionality to the `gsutil cp` command, and the `qsam encode` command is similar to the `bq export` command. The following are the advantages of `qsam` commands: 
    * Supports compound data types, including the [OCCURS clause (lists), REDEFINES clause, and nested records](https://docs.cloud.google.com/mainframe-connector/docs/qsam-transcoding).
    * Supports transcoder configuration to meet specific needs through a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration), using defaults, field modifiers, field suffixes, transformations, and a schema validation mode.
    * Supports the creation of a [spillover dataset](https://docs.cloud.google.com/mainframe-connector/docs/spillover-dataset), which is a table of transcoding errors that can be used for auditing or debugging.
  * Remote and standalone modes now use Java 17 ([Docker image ibm-semeru-runtimes:open-17.0.14_7-jre-noble](https://hub.docker.com/_/ibm-semeru-runtimes)) instead of the Java 8.



v5.16.0

Fixed

The following issues are fixed in Mainframe Connector 5.16.0:

  * Fixed issue with [custom charsets](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#customized-charsets).
  * The `qsam` commands support copybooks that contain fields with the same name under different parents.
  * Fixed a bug that caused incorrect handling of double-byte character set (DBCS).



## March 04, 2025

v5.15.1

Fixed

The following issue is fixed in Mainframe Connector 5.15.1:

  * If you want Mainframe Connector to assign `FILLER` values based on the results of a [`bq export`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#bq-export) query, set the [`BQSH_FEATURE_RESPECT_FILLER_ON_EXPORT`](https://cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_respect_filler_on_export) environment variable to true.



## February 13, 2025

v5.15.0

Feature

Mainframe Connector 5.15.0 supports the following new features:

  * Supports the integration of your extraction, transformation, and loading (ETL) tools with Mainframe Connector using Cloud Run jobs. For more information see, [Use Cloud Run with Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/run-jobs).
  * Mainframe Connector uses Google Analytics to collect usage data. This helps us improve the software and provide a better user experience. By default, Google Analytics is enabled. You can disable this feature using the `DISABLE_ANALYTICS` environment variable.
  * Supports configuring the maximum time you want Mainframe Connector to wait for a BigQuery job to complete using a new flag `max_polling_interval_ms` with the `bq load` command. The default value is 60000 milliseconds (1 minute).
  * For more granular control over data transfer, you can now specify chunk sizes below 64MiB using the `maxChunkSize` flag with the `gsutil cp` command.



v5.15.0

Fixed

The following issues are fixed in Mainframe Connector 5.15.0:

  * Fixed Mainframe file handling leaks.
  * Fixed Mainframe Connector remote mode issues.



## November 21, 2024

v5.14.0

Feature

Mainframe Connector 5.14.0 supports the following new features:

  * Supports defining [customized character sets](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#customized-charsets) when importing data to BigQuery, and when exporting from BigQuery using the `gsutil cp` or `bq export` commands.
  * Supports a [dry-run mode](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#gsutil-cp-dryrun) while importing data to BigQuery using the `gsutil cp` command.
  * Supports making the [null termination configurable](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_terminate_strings_on_null) using the `gsutil cp` command.
  * Supports the [bytes null indicator](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator).



v5.14.0

Fixed

The following issues are fixed in Mainframe Connector 5.14.0:

  * Fixed the issue of the `scp` command writing dummy bytes in case less bytes are read than the logical record length.
  * Fixed security vulnerabilities.



## October 15, 2024

v5.13.1

Fixed

The following issue is fixed in Mainframe Connector 5.13.1:

  * Fixed security vulnerabilities.



## September 30, 2024

v5.13.0

Fixed

The following issues are fixed in Mainframe Connector 5.13.0:

  * Supports new ciphers and automatic selection of the preferred ciphers provider.
  * Fixed security vulnerabilities.
  * Fixed the issue of `gsutil cp` statistics miscounting the number of errors. This is applicable only if you set `--max_error_pct` to a value greater than 0. This resulted in the unintended inclusion of certain rows in BigQuery that should have been excluded.
  * Fixed the issue of non-standard Latin characters not getting decoded correctly as UTF-8 strings in variable length fields.
  * Added stricter checks to ensure that date, timestamp, and null indicator fields have the correct data types during parsing. A `ParseException` is thrown if any of these fields have an invalid corresponding picture type, that is, date and timestamp fields must only contain `Pic X(n)`. A null indicator field can only contain `Pic X(n)` for strings and `Pic (S)9(n)` for digits.



v5.13.0

Feature

Mainframe Connector 5.13.0 supports the following new features:

  * Supports the [standalone mode](https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode) for both data import and export flows.
  * The `gsutil cp` command supports [copying a file from Cloud Storage to a Mainframe dataset](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#copy-file).
  * Supports [`bq export` performance improvements](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#performace-updates-bqexport) for local and remote modes.
  * Supports [null indicator fields](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator).
  * Supports [creating a BigQuery table from a given a copybook](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#create-table-from-copybook).
  * Supports the `VALUE` clause.
  * The `gsutil cp` command supports using the parameters [`--inDsn` (input data DSN) and `--cobDsn` (copybook DSN)](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#gsutil-cp)
  * Supports new command [`systemreport`](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#systemreport).
  * Supports the `BQSH_FEATURE_EMPTY_VALUES_ARE_NULL` feature flag. The default value is true. This flag is applicable only if the `BQSH_FEATURE_FAIL_ON_INVALID_DATA` is set to true. This flag ensures that empty values (only null, only spaces, only high bytes) are decoded as null, and an error doesn't occur for packed decimal and zoned decimal types.



v5.13.0

Issue

Mainframe Connector 5.13.0 has the following open issue:

  * Mainframe Connector doesn't support copybooks that contain fields with the same name under different parents.



## August 12, 2024

v5.12.1

Fixed

The following issues are fixed in Mainframe Connector 5.12.1:

  * Mainframe Connector 5.12.1 provides the `BQSH_FEATURE_FAIL_ON_INVALID_DATA` feature flag that lets you enforce stricter error handling. This flag is disabled by default. Enabling this flag throws failures if the data contains empty strings or whitespaces in date and timestamp fields, or invalid packed decimal fields. Ensure the following while using packed decimal fields: 
    * The last sign nibble must be in the range `0xA - 0xF`, otherwise, it is invalid.
    * All the other nibbles must not be in the range `0xA - 0xF`, otherwise, it is invalid.
  * Fixed the issue of some jobs continuing to run despite encountering an error due to inconsistent transcoding error tracking.
  * Fixed the issue of `PIC X` non-standard latin characters not getting decoded correctly as UTF-8 strings.
  * Fixed the following issues of zoned decimal backward compatibility: 
    * `PIC 9` without scale is being loaded as `INTEGER` to BigQuery instead of `NUMERIC`.
    * Added an auto-detection mode to load decimal numbers with more than 18 digits into BigQuery. For new tables, decimal numbers are loaded as `BIGNUMERIC` numbers. To ensure backward compatibility for existing tables for releases before 5.11.0, decimal numbers will continue to be loaded as a `STRING`.



## July 01, 2024

v5.12.0

Feature

Mainframe Connector 5.12.0 supports the following new features:

  * The `gsutil cp` command supports some performance improvements. For more information, see [Performance improvements for the `gsutil cp` command](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#performace-updates-gsutilcp). 
  * The `bq export` command supports the Native copybook parser. We recommend that you explicitly set the Native copybook parser using the `--parser_type=native` flag. For more information, see [Define the copybook parser](https://docs.cloud.google.com/mainframe-connector/docs/define-parser). This ensures that Mainframe Connector doesn't fall back to the Legacy copybook parser in case of copybook syntax errors.
  * Supports all double-byte character set (DBCS) textual types (N/G). DBCS fields that are not surrounded by SO/SI should have a `_DBCS` or `-DBCS` field suffix.
  * Supports both single and double IBM hexadecimal floating point (HFP) data types for copybook fields.
  * Supports [`bq query` audit logs](https://docs.cloud.google.com/mainframe-connector/docs/api-reference).
  * Supports the following log improvements: 
    * New and improved logging format
    * More resilient Cloud Logging implementation
    * The `scp` command prints the file size and the number of records
    * The Remote transcoding process prints the version number
    * Displays an error when you use the deprecated PIC T field with the Native copybook parser
  * Mainframe Connectors displays an updated error when deprecated PIC T is used with the new copybook parser.
  * Commands in the remote mode can use the option `remoteUrl` instead of `remoteHost` and `remotePort`. The `remoteUrl` should contain the scheme, host, and port. If the scheme is https and no trust store is provided as an option or environment variable, the system's default trust store is used.



v5.12.0

Fixed

The following issues are fixed in Mainframe Connector 5.12.0:

  * Fixed the issue where the `gsutil cp` command statistic miscounts added rows when the error count was more than 0. This is only applicable if you set the `--max_error_pct` flag to a value greater than 0. The `--max_error_pct` argument for `gsutil cp` command is also fixed. By default, the value is 0.0, which means failure on copybook or data error.
  * Fixed the `--parallelism` argument for the `gsutil cp` command.
  * Fixed incorrect error handling for any issues in the copybook. For example, the Mainframe Connector job should fails or aborts if there are errors such as data type mismatches the data, or there's a logical record length (LRECL) mismatch.
  * Fixed cases where remote transcoding replaced underscore (_) in the column name with (-) in the copybook. To disable this behavior during both local and remote transcoding, set the `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME` feature flag to true.
  * Fixed zoned decimal binary data decoding when the zoned decimal has more than 19 digits, and contains a decimal point.
  * Fixed `gsutil cp` command to work with uncompressed files. The command previously accepted gzip flies only.
  * Shows an explicit error message when you use `REDEFINE` keyword as `REDEFINE` is not supported.
  * Fixed the declaration of big numbers with decimal point (numbers with more than 19 digits) in BigQuery. These numbers were declared as `STRINGS` instead of `BIGNUMERIC`. 
  * Fixed `gsutil cp` command to work when the source file is located in Cloud Storage and the converted file's destination is also in Cloud Storage.



## May 02, 2024

v5.11.0

Issue

Mainframe Connector 5.11.0 has the following open issue:

  * Zoned decimal bin data is incorrectly decoded when the zoned decimal has more than 18 digits, and contains a decimal point.



v5.11.0

Fixed

The following issue are fixed in Mainframe Connector 5.11.0:

  * Optimized `gsutil cp` string handling performance.



v5.11.0

Feature

Mainframe Connector 5.11.0 supports the following new features:

  * Support for [variable length data type](https://docs.cloud.google.com/mainframe-connector/docs/reference#variable-length-strings).
  * Support for the `SIGN` clause.
  * Support for picture types [`PIC U` and `PIC N` (national & DBCS fields)](https://docs.cloud.google.com/mainframe-connector/docs/reference#dbcs-usage).
  * Support for [`DATE` and `TIMESTAMP` BigQuery types](https://docs.cloud.google.com/mainframe-connector/docs/reference#date-timestamp). This includes the ability to configure the field suffix and format patterns of a date or timestamp using environment variables. 
  * Support for [signed and unsigned zoned decimal data type (max precision 38, max scale 38)](https://docs.cloud.google.com/mainframe-connector/docs/reference#copybook-restrictions).



## March 28, 2024

v5.10.0

Issue

Mainframe Connector 5.10.0 has the following open issue:

  * The `bq export` command doesn't support the new `copybook` parser.



v5.10.0

Feature

Mainframe Connector 5.10.0 supports the following new features:

  * Support for Cloud Run remote service deployment using Terraform.
  * Support for the `bq export` command with Mainframe Connector Remote Service.
  * Optimized `bq query` command with the `split_sql=true` field that supports the following: 
    * Skips SQL statements with only comments.
    * Makes `split_sql=true` as the default mode which splits multiple SQL statements into multiple requests that are executed in parallel.



v5.10.0

Fixed

The following issues are fixed in Mainframe Connector 5.10.0:

  * Fixed the recursive mode `--recursive` of the `gsutil rm` command.
  * Fixed the issue where the `bq export` command with more than nine parts or rows was exported out of order when all the data was loaded.
  * Fixed the issue where the `bq export` command issued more queries than necessary.
  * Fixed the issue where the `bq export` command generated redundant empty parts.
  * Fixed the issue of parsing `Varchar` fields - In the old copybook parser, `Varchar` fields of the size of 1000 and above are parsed as a `Byte` data type. In the new copybook parser, `Varchar` fields of the size of 1000 and above are parsed as a `String` datatype. If you want to parse `Varchar` fields of any size as a `Byte` data type in the new copybook parser, ensure that the Picture (PIC) name ends with `BTYE` or `BT`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
