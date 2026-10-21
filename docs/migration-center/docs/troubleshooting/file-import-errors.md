---
url: https://docs.cloud.google.com/migration-center/docs/troubleshooting/file-import-errors/
title: Troubleshoot file import errors \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:26.814532+00:00
---

# Troubleshoot file import errors  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/troubleshooting/file-import-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Troubleshoot file import errors Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to troubleshoot errors with [manual file import](https://docs.cloud.google.com/migration-center/docs/import-data-tables).

## Errors reference

The following tables describe the possible errors you might find with manual file import, and the possible error messages.

### Blocking errors

The following errors prevent you from uploading your infrastructure data.

Error message | Error explanation  
---|---  
Import job `JOB_NAME` contains no files | You didn't upload any files.  
Import job `JOB_NAME` has mixed format files. | You uploaded mixed files formats.  
File `FILE_NAME` with format `FORMAT` size `SIZE` is over the allowed limit: `LIMIT_VALUE` | You uploaded a file that is too large.  
Missing required file "vmInfo" | You didn't upload the required vmInfo file.  
  
### vmInfo file

Column | Error case | Error message | Import behavior  
---|---|---|---  
Any column | Unexpected column | Unable to find column mapping for `COLUMN_NAME` | The cell is ignored.  
MachineId | Missing column | Missing field(s) which can uniquely identify the Asset | **Every row shows the error message, and the row is not parsed.**  
Empty UUID | Missing field(s) which can uniquely identify the Asset | **The row is not parsed.**  
PrimaryMACAddress | None, `AA-BB-CC-DD-EE-FF` or `AA:BB:CC:DD:EE:FF` formats | Unexpected MAC address `INPUT_MAC`, want pattern "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$" | The cell is ignored.  
TotalDiskAllocatedGiB | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
TotalDiskUsedGiB | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
Not higher than Allocated | "TotalDiskUsedGiB" is higher than "TotalDiskAllocatedGiB" | The cell is ignored.  
AllocatedProcessorCoreCount | Non int | Invalid syntax | The cell is ignored.  
Negative int | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
MemoryGiB | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
CreateDate | Empty string | Empty timestamp | The cell is ignored.  
Wrong format | Unexpected timestamp format `INPUT_VALUE`, want "2006-01-02 15:04:05-07:00" | The cell is ignored.  
IsPhysical | Not in {"","0","false","False","FALSE"} | Physical machines are not supported yet | **The row is not parsed.**  
Source | AWS/Azure only (none for manual) |  | **The row is not parsed.**  
  
### diskInfo file

Column | Error case | Error message | Import behavior  
---|---|---|---  
Any column | Unexpected column | unable to find column mapping for `COLUMN_NAME` | The cell is ignored.  
MachineId | Missing column | Missing field(s) which can uniquely identify the Asset | **Every row shows the error message, and the row is not parsed.**  
Empty UUID | Missing field(s) which can uniquely identify the Asset | **The row is not parsed.**  
SizeInGib | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
UsedInGib | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
Not higher than Size | "UsedInGib" is higher than "SizeInGib" | The cell is ignored.  
  
### perfInfo file

Column | Error case | Error message | Import behavior  
---|---|---|---  
Any column | Unexpected column | unable to find column mapping for `COLUMN_NAME` | The cell is ignored.  
MachineId | Missing column | Missing field(s) which can uniquely identify the Asset | **Every row shows the error message, and the row is not parsed.**  
Empty UUID | Missing field(s) which can uniquely identify the Asset | **The row is not parsed.**  
TimeStamp | Empty string | empty timestamp | **The row is not parsed.**  
Wrong format | Unexpected timestamp format `INPUT_VALUE`, want "2006-01-02 15:04:05-07:00" | **The row is not parsed.**  
CpuUtilizationPercentage | Non float | Invalid syntax | The cell is ignored.  
X < 0 || X > 100 | Invalid percentage `INPUT_VALUE` | The cell is ignored.  
MemoryUtilizationPercentage | Non float | Invalid syntax | The cell is ignored.  
X < 0 || X > 100 | Invalid percentage `INPUT_VALUE` | The cell is ignored.  
UtilizedMemoryBytes | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
DiskReadOperationsPerSec | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
DiskWriteOperationsPerSec | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
NetworkBytesPerSecSent | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
NetworkBytesPerSecReceived | Non float | Invalid syntax | The cell is ignored.  
Negative float | Unexpected negative value `INPUT_VALUE` | The cell is ignored.  
  
### tagInfo file

Column | Error case | Error message | Import behavior  
---|---|---|---  
Any column | Unexpected column | Unable to find column mapping for `COLUMN_NAME` | The cell is ignored.  
MachineId | Missing column | Missing field(s) which can uniquely identify the Asset | **Every row shows the error message, and the row is not parsed.**  
Empty UUID | Missing field(s) which can uniquely identify the Asset | **The row is not parsed.**  
Key | Invalid according to GCP guidelines | Key `INPUT_VALUE` was converted to `OUTPUT_VALUE` according to GCP guidelines | The converted name is used for the key.  
Already exists | Key `INPUT_VALUE` already exists | **The label is not parsed.**  
Value | Invalid according to GCP guidelines | Value `INPUT_VALUE` was converted to `OUTPUT_VALUE` according to GCP guidelines | The converted name is used for the value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
