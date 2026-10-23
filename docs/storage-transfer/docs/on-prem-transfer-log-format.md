---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format/
title: File system transfer logs \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:55.526304+00:00
---

# File system transfer logs  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  File system transfer logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the current file system transfer log format.

**Note:** The log format described on this page is subject to change. We recommend that you avoid writing scripts, programs, or design processes that depend on the ordering, naming, or presence of columns or values in this log. Refer to this page and [Storage Transfer Service release notes](https://docs.cloud.google.com/storage-transfer/docs/release-notes) for updates to the log format.

## View transfer logs

File system transfers produce detailed transfer logs that you can use to verify the results of your transfer job. Each job produces a collection of transfer logs that are stored in the transfer's Cloud Storage bucket: the source bucket, destination bucket, or intermediate bucket, depending on the transfer direction. Anyone that has access to the Cloud Storage bucket has access to the transfer logs.

Logs are produced while the transfer job is running. The complete logs are typically available within 15 minutes of job completion.

**Caution:** File system transfer logs for `TRANSFER` and `DELETE` actions include names and paths of objects and files processed by the transfer job, for all logged states. If these include personally identifiable information or security data, configure permissions on the log bucket accordingly. 

### View logs in the Cloud Storage bucket

Transfer logs are stored in the transfer's Cloud Storage bucket at the following path:

`bucket-name/storage-transfer/logs/transferJobs/job-name/transferOperations/operation-name`

where the path components are as follows:

  * `bucket-name` is the name of the Cloud Storage bucket involved in this transfer.
  * `job-name` is the job name, as displayed in the job list.
  * `operation-name` is the name of the individual transfer operation, comprised as the IS08601 timestamp and generated ID.



Logs are aggregated and stored as objects. Each batch of logs is named by its creation time. For example:

`my bucket/storage-transfer/logs/transferOperations/job1/2019-10-19T10_52_56.519081644-07_00.log`

## Run BigQuery queries on transfer logs

To run BigQuery queries on your transfer logs:

  1. [Load the CSV log data into BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv).

  2. Run your [BigQuery query](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax).




### Example queries

**Display the number of files that attempted transfer and whether they failed or succeeded**
    
    
    select ActionStatus, count(*) as num_files
    from big-query-table
    where Action="TRANSFER"
    group by 1;
    

Where `big-query-table` is the name of the BigQuery table that contains the transfer log.

**Display all files that failed to transfer**
    
    
    select Src_File_Path
    from big-query-table
    where Action="TRANSFER" and ActionStatus="FAILED";
    

Where `big-query-table` is the name of the BigQuery table that contains the transfer log.

**Display checksum and timestamp for each file that successfully transferred**
    
    
    select Timestamp, Action, ActionStatus, Src_File_Path, Src_File_Size,
    Src_File_Crc32C, Dst_Gcs_BucketName, Dst_Gcs_ObjectName, Dst_Gcs_Size,
    Dst_Gcs_Crc32C, Dst_Gcs_Md5
    from big-query-table
    where Action="TRANSFER" and ActionStatus="SUCCEEDED";
    

Where `big-query-table` is the name of the BigQuery table that contains the transfer log.

**Display all error information for directories that failed to transfer**
    
    
    select FailureDetails_ErrorType, FailureDetails_GrpcCode, FailureDetails_Message
    from big-query-table
    where Action="FIND" and ActionStatus="FAILED";
    

Where `big-query-table` is the name of the BigQuery table that contains the transfer log.

## Format description

File system transfer logs are saved in tab-separated values (TSV) format, and contain a header row with field names. The order that the fields are displayed are generally stable, but aren't guaranteed, and must be inferred from the header row.

Each line represents a single log record, that is a status update on part of the overall transfer operation.

**Note:** Storage Transfer Service doesn't record log entries for skipped files.

The following table describes the fields in the log file:

Log field | Description  
---|---  
**Timestamp** | ISO 8601-compliant timestamp when we recorded the event.   
**Operation Name** | The fully-qualified operation name.  
**Action** | Describes the action of this particular task. One of the following:

  * **FIND** : Finding work to do, such as listing files on-premises
  * **TRANSFER** : Transferring files
  * **DELETE** : Deleting files at destination

  
**ActionStatus** | The high-level status of the action. One of the following:

  * **SUCCEEDED** : The action completed successfully.
  * **FAILED** : The action failed. Additional details about the failure are in the **FailureDetails** fields.

  
**FailureDetails.ErrorType** | A string that represents the type of error encountered. For example, **FILE_NOT_FOUND**. Populated only if an error was encountered.  
**FailureDetails.GrpcCode** | A string value of the Google RPC code. For example, **FAILED_PRECONDITION**. Populated only if an error was encountered.  
**FailureDetails.Message** | A human-readable error message for the failure. Populated only if an error was encountered.  
**Src.Type** | String that describes the source's storage system type. This is always **ON_PREM**.  
**Src.File.Path** | Path of the transferred on-premises file.  
**Src.File.LastModified** | The POSIX modified time (mtime) of the on-premises file.  
**Src.FileSize** | The file size in bytes.  
**Src.File.Crc32C** | The CRC32C checksum of the file's contents.  
**Dst.Type** | String that describes the destination storage system type. This is always **`GCS`**.  
**Dst.Gcs.BucketName** | The destination Cloud Storage bucket name.  
**Dst.Gcs.ObjectName** | The object prefix for the destination object.  
**Dst.Gcs.LastModified** | The POSIX modified time (mtime) of the destination object.  
**Dst.Gcs.Size** | The object size in bytes.  
**Dst.Gcs.Crc23C** | The CRC32C checksum of the object's contents.  
**Dst.Md5** | The MD5 checksum of the final object in Cloud Storage.  
  
## Example log entry

The following is an example of two lines of log output, the header and a data line:
    
    
    Timestamp       OperationName   Action  ActionStatus    FailureDetails.ErrorType        FailureDetails.GrpcCode FailureDetails.Message     Src.Type        Src.File.Path   Src.File.LastModified   Src.File.Size   Src.File.Crc32C Dst.Type   Dst.Gcs.BucketName      Dst.Gcs.ObjectName      Dst.Gcs.LastModified    Dst.Gcs.Size    Dst.Gcs.Crc32C  Dst.Gcs.Md5
    2019-10-18T21:06:17Z    transferOperations/agent-manual_transferJobs/OPI1494275376193533620_0000000001571432448     TRANSFER        SUCCEEDED                               ON_PREM_FILE    /mnt/disks/disk-1/directory1/file.txt      1561409931      406     3089075447      GCS_OBJECT      destination-gcs-bucket    file.txt  1571432776      406     3089075447      FDjya7dWbd0OrgnZ7g9ZJw==
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
