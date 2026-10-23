---
url: https://docs.cloud.google.com/mainframe-dual-run/docs/batch-comparison-overview/
title: Batch comparison overview \u00a0|\u00a0 Dual Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:31.722711+00:00
---

# Batch comparison overview  |  Dual Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-dual-run/docs/batch-comparison-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Dual Run ](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview)



Send feedback 

#  Batch comparison overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Dual Run Batch Comparison, which is designed to help you compare the outputs of batch workloads. With this feature, you can ensure that the batch jobs running on the mainframe and on Google Cloud generate identical outputs for the same given inputs.

## How batch comparisons work

Dual Run's batch comparison feature lets you analyze files by first configuring the comparison settings, then setting up the triggers to start the process, and finally reviewing the results.

Learn how abtch comparison works in the following sections.

![Batch comparison diagram](https://docs.cloud.google.com/static/mainframe-dual-run/docs/images/dual-run-batch-comparison.png)

### File transfer from the mainframe

Before you can run a file comparison, the first step is to transfer files from the mainframe to a Cloud Storage bucket in Google Cloud.

You can transfer files from the mainframe in two ways:

  * with FTP/HTTPS transfers
  * with the [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/get-started).



In both cases, Dual Run can read EBCDIC formats, and supports `UNLOAD` output without the need for any additional transformation.

### Comparison configuration

Dual Run provides you with full flexibility on how to compare your mainframe and modernized files. For each file, you specify which fields to compare, and their expected formats.

Dual Run file comparison supports advanced configurable options, such as data obfuscation, tolerance settings, field merging, custom labels, and filtering for precise and flexible file analysis.

  * **Obfuscate specific fields when you perform the file comparison**. This is useful for hiding sensitive data that shouldn't appear in the reports or in the dashboards as clearly visible content.
  * **Allow for tolerance when comparing numeric values** of specific fields. This is useful when comparing floating point numbers originating from different systems.
  * **Allow tolerance when comparing timestamp values** of specific fields. This is useful when comparing timestamps originating from different systems.
  * **Merge multiple fields together with an optional joining string** , and treat them as a single field during the comparison.
  * **Configure custom labels to categorize your comparison jobs**. Labels are key-value pairs that you can use to tag your comparison jobs, and to differentiate them between different functional or business objectives.
  * **Ignore leading and trailing whitespaces** in specific fields.
  * **Ignore letter case in strings**.
  * **Apply filters to ignore records during the comparison** , allowing multiple filters to be applied at the same time.



### Automated configuration generation

Dual Run provides you with automated tools to help configure File Comparison. These tools create the required configuration files based on your mainframe copybooks, or based on sample JSON and CSV files that you provide.

### Comparison results

When comparing two files, Dual Run returns three possible results:

  * **Full match:** the record is present in both files, and the fields content matches within your specified constraints.
  * **Partial match:** the record is present in both files, but some of the fields don't match. You can check the differences in the results output.
  * **Missing record:** the record is present only in the actual or expected files.



In case of a mismatch between the compared files, you can configure Dual Run to show all the compared records within the files, and not just the mismatched records, for easier troubleshooting.

Dual Run offers a feature called **deferred comparisons** to address situations where data might be temporarily missing. This is particularly useful for iterative comparisons, like those performed on daily database snapshots. If a field is absent in one iteration but appears in the next, Dual Run stores and compares it later, ensuring that no data discrepancies are created. This provides a more robust and accurate comparison process, especially for dynamic datasets.

## Supported files

Dual Run supports the following files for comparison:

  * z/OS fixed block sequential files
  * JSON array files
  * JSON Lines (JSONL) files
  * CSV files



### Supported z/OS data types

Dual Run supports the following z/OS data types, both in EBCDIC and ASCII:

  * COMP1
  * COMP2
  * PACKED_DECIMAL
  * COMP4
  * COMP5
  * ZONED_DECIMAL
  * ALPHANUMERIC



### Supported JSON files

Dual Run supports the following JSON formats:

  * JSONL: in this file, each line contains a single JSON object. No newlines are present within the object.
  * JSON array: in this file, two types of files are supported: 
    * A JSON array where the entire array and elements are in a single line. There are no newlines at all in this file.
    * A JSON array with a newline separating the elements in the array. Each JSON object can contain newlines as well.



### Supported CSV files

Dual Run supports CSV files that follow the [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) standard. You can configure how Dual Run parses the file, including delimiters, headers, escape characters, and multiline.

## What's next

Learn about [Online Comparison](https://docs.cloud.google.com/mainframe-dual-run/docs/online-comparison-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
